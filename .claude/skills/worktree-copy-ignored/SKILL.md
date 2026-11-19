---
name: "worktree-copy-ignored"
description: "Use when setting up git worktrees for parallel Claude or agent work, to copy gitignored dependencies and build caches into a new worktree with Worktrunk's copy-ignored step instead of a cold install. Dewey 005.8."
---

# Worktree copy-ignored

Author: TABARC-Code. Version 1.0.0. Classification: 005.1-WT (programming tooling, worktree operations).

A fresh git worktree gets the tracked code and nothing else. No `node_modules`, no `target/`, no `.venv`, no `.env`. Five agents means five cold installs and five cold builds. Worktrunk's `wt step copy-ignored` copies the gitignored files across from an existing worktree, using copy-on-write (reflink) when the filesystem allows it.

The job isn't just running one command. It's picking the right strategy per language, keeping secrets out of agent worktrees, proving copy-on-write actually happened, and measuring the result instead of repeating someone else's benchmark.

## 0. Ground truth (Worktrunk docs, checked 2026-11-05)

- **Default copies everything gitignored.** Not just what you list. That includes `.env`. Read section 5 before running it.
- **`.worktreeinclude` is a filter, not a requirement.** If present, a file must be both gitignored and matched by it. Gitignore-style patterns.
- **Built-in exclusions:** `.bzr/ .hg/ .jj/ .pijul/ .sl/ .svn/`, `.conductor/ .entire/ .worktrees/`, and nested worktrees.
- **Extra excludes** go in config: `[step.copy-ignored]` then `exclude = [".cache/", ".turbo/"]`.
- **Idempotent.** Existing files in the destination are skipped. `--force` overwrites.
- **Per-file reflink**, like `cp -Rc`. Time scales with file count, not total size. A 14 GB `target/` of big files clones fast; a `node_modules` with 200,000 tiny files won't.
- **Fallback** when reflink is unavailable is not documented. Probe it (section 4), don't assume.
- **Claude Code's own worktrees require `.worktreeinclude`** to copy anything. Worktrunk doesn't. One well-kept `.worktreeinclude` serves both.

The docs' own figures: 14 GB `target/`, `cp -R` about 2 minutes, `wt step copy-ignored` about 20 seconds; first Rust build about 68s down to about 3s. These are the author's numbers. Treat them as a hypothesis until section 7 says otherwise.

## 1. Preflight the tool

- Run `wt --version` and `git --version`.
- If Worktrunk is missing, ask before installing. Options: `cargo install worktrunk`, or the Homebrew formula named in the Worktrunk docs. Never pipe a remote install script into a shell without consent.
- Run `wt step copy-ignored --help` and check the flags below still match. They drift between releases.

## 2. Flags

| Flag | Does | Default |
|---|---|---|
| `--from <branch>` | source worktree | main worktree |
| `--to <branch>` | destination worktree | current worktree |
| `--dry-run` | list, copy nothing | off |
| `--force` | overwrite existing files | off (skip) |
| `--format text\|json` | output format | text |

Global: `-C`, `--config`, `-v`, `-y`.

## 3. Decide the strategy first

Work through this in order. Stop at the first match.

1. **Python venv?** Don't copy it. Venvs hold absolute paths and break when moved. Exclude `.venv/` and run `uv sync` (or the project's installer) in the new worktree.
2. **Node, no native deps, agents won't change dependencies?** A symlink beats a copy: `ln -sf <main>/node_modules .` in a `pre-start` hook. Shared state means one agent's `npm install` hits everyone.
3. **Node with native deps, or agents that install packages?** Copy. Expect it to be slower than Rust because of file count.
4. **Rust `target/`, Go build cache, large binary artefacts?** Copy. This is where reflink pays off most.
5. **Filesystem without reflink (ext4, most Linux defaults)?** Copy still works but costs full time and space. Tell the user, then decide whether the build-time saving still justifies it. A shared compiler cache such as `sccache` is a different route, not covered here.

Record the decision in one line before doing anything. It feeds the log in section 10.

## 4. Probe the volume

Run on the volume the worktrees will live on, not your home directory if they differ.

```bash
# macOS (APFS): cp -c uses clonefile
dd if=/dev/urandom of=.probe bs=1m count=256 && df -k . && cp -c .probe .probe.clone && df -k . ; rm -f .probe .probe.clone

# Linux (btrfs, XFS with reflink=1)
dd if=/dev/urandom of=.probe bs=1M count=256 && df -k . && cp --reflink=always .probe .probe.clone && df -k . ; rm -f .probe .probe.clone
```

Pass: the clone succeeds and free space drops by about 256 MB once, not twice. Fail: `Operation not supported`, or space drops twice. On fail, go to strategy 5.

## 5. Secret gate

The default copies every gitignored file, so assume secrets are in scope until proven otherwise.

```bash
wt step copy-ignored --dry-run > .copy-plan.txt
grep -Ei '(^|/)\.env|\.pem$|\.key$|id_rsa|id_ed25519|credentials|\.npmrc|\.pypirc|\.aws/|\.netrc|secrets?' .copy-plan.txt
```

Any hit: stop and ask the user. Either add the path to `exclude`, or confirm the agent may see it. Never edit `.gitignore` or `.worktreeinclude` without saying so; they change behaviour for every worktree and for Claude Code. Delete `.copy-plan.txt` after.

## 6. Run it, then wire it in

One-off:

```bash
git worktree add ../<name> -b <branch>
cd ../<name> && wt step copy-ignored
```

Check the new worktree has the expected folders. Then a quick independence test: edit one copied file in the new worktree and confirm the original is unchanged. Copy-on-write should guarantee it; check anyway, once per machine.

Automated, in project config `.config/wt.toml`:

```toml
[post-start]
copy = "wt step copy-ignored"
```

`post-start` runs in the background at low priority (macOS `taskpolicy -b`; Linux `nice -n 19` plus `ionice -c 3`; experimental). Use `[pre-start]` instead if a later hook, or an agent starting straight away, needs the files present. Getting this wrong is the commonest cause of "the agent ran a cold build anyway": it started before the background copy finished.

After the main worktree rebuilds, existing copies go stale but won't be overwritten. Rerun with `--force` to refresh.

## 7. Measure, don't quote

Two throwaway worktrees off the same commit. One cold, one copied.

```bash
git worktree add ../wt-cold -b bench-cold
git worktree add ../wt-warm -b bench-warm
df -k .
( cd ../wt-warm && time wt step copy-ignored )
df -k .
( cd ../wt-cold && time <build command> )
( cd ../wt-warm && time <build command> )
```

Do it twice, ideally on different days, and report both. If the warm build isn't clearly faster, check: did the copy finish, is the toolchain identical, did the build tool treat copied artefacts as stale (path-sensitive caches will). Clean up with `git worktree remove` and delete the bench branches.

Report only measured numbers. If you didn't measure, say "not measured".

## 8. Report plainly

Strategy chosen, filesystem and probe result, secret-gate outcome, what was copied, whether copy-on-write was used, measured times and space, and anything skipped or failed. Nothing else.

## 9. When it goes wrong

| Symptom | Likely cause | Do |
|---|---|---|
| Copy as slow as `cp -R` | no reflink on that volume | run section 4 |
| Copy slow but probe passes | huge file count | symlink, or exclude caches |
| Agent still builds cold | `post-start` hadn't finished | switch to `pre-start` |
| Python errors on import | venv was copied | exclude `.venv/`, use `uv sync` |
| Old artefacts in new tree | skip-existing default | rerun with `--force` |
| Secret visible to agent | default copies all ignored files | section 5, add to `exclude` |
| Claude Code worktree empty | no `.worktreeinclude` | add one; Worktrunk unaffected |
| Full copy on APFS | old Worktrunk, or worktree on another volume | check version and `df` paths |

Two failed attempts at the same fix is the limit. Then report the exact error and stop.

## 10. Feedback loop

Every run adds one entry. Positive and negative signals both count.

```
## YYYY-MM-DD | project | language | filesystem | worktrunk version
- strategy: copy | symlink | reinstall (section 3 step n)
- probe: pass | fail
- secret gate: clean | hits excluded | user approved
- copy time / space used: measured | not measured
- cold vs warm build: measured | not measured
- signal: POS | NEG, and why
- change to this skill: none | what
```

A change stays if the next two runs don't repeat the negative it fixed. A change that causes the same negative twice is reverted. When the docs and a measurement disagree, the measurement wins locally and the disagreement goes in the log.

Information flows both ways. Measurements update section 0 when they contradict it. Language findings update section 3. Recurring failures become rows in section 9.

## 11. Tests

1. Rust repo on APFS, no `.worktreeinclude`. Expect: probe pass, secret gate before copy, `post-start` hook offered, numbers labelled measured or not.
2. Python repo with `.venv` and `.env`. Expect: venv excluded, `uv sync` suggested, `.env` flagged and the user asked.
3. Node repo on ext4. Expect: probe fail reported, user told there's no space saving, symlink raised only if no native deps.

## 12. Related skills

- `superpowers:using-git-worktrees` for worktree creation and cleanup in general.
- `superpowers:dispatching-parallel-agents` when the worktrees feed parallel agents.
- `skill-security-scanner` if this skill gains scripts.
- `kaizen` for reviewing the feedback log across many runs.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **worktree-create** · type: handoff · source: body
  - This skill (weight 2): Is the preferred copy step for the worktrees that worktree-create stands up.
  - worktree-create: Hands the copy of gitignored files to it when Worktrunk is installed.
<!-- relationships:end -->
