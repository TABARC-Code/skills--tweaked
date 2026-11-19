---
name: piv-commit
description: Creates a new git commit for all uncommitted changes with an atomic, conventionally-tagged message. Use when a task or feature is finished, when the user says commit this, save my work, make a commit, or wants a clean commit message, and whenever changes are ready to be committed even if they never name this skill. Dewey 005.8.
---

# Commit: Create a New Commit

Create a new commit for all of our uncommitted changes.

## Process

0. **Read this project's conventions.** If `.claude/references/conventions.md` exists, read its `## commit`
   section and follow it — those rules win over the defaults below. That file is where a project's specifics
   live; this skill stays general.
1. Run `git status && git diff HEAD && git status --porcelain` to see what files are uncommitted.
1b. **Look before you add.** Read the untracked list. Never stage `.env` files, keys, tokens, credentials, build output, `node_modules` or large binaries. If one is untracked and not ignored, leave it out and tell the user it should go in `.gitignore`. If the changes cover two unrelated concerns, say so and offer to commit them separately, because "all uncommitted changes" and "atomic" cannot both hold for a mixed diff.
2. Add the untracked and changed files.
3. Write an atomic commit message with an appropriate, descriptive summary. For the subject and body rules (under 50 characters, imperative, the why in the body only when the diff doesn't show it), follow `terse-commit`.
3b. If the project has a validation skill or command and nothing has run since the last edit, say so before committing. Do not claim the work passes on the strength of an earlier run.
4. Add a tag such as `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, etc. that reflects our work.

## Output

A single commit containing all uncommitted changes, with a conventional-commit-style message
(`<tag>: <atomic description>`) that accurately reflects the work done.

After the commit succeeds, print two clearly labelled summaries:

### What Changed
One short paragraph (3–6 sentences) describing the feature/fix/refactor that was committed — what problem it solves and what files were the key touch points. Write for a developer skimming the git log.

### AI Layer Changes
Only include this section if any files under `.claude/` were modified or added (CLAUDE.md, `.claude/references/`, `.claude/skills/`, `.claude/agents/`, etc.).

List each changed AI-layer file with a one-line note on what evolved and why. If nothing in `.claude/` changed, omit this section entirely.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-implement** · type: handoff · source: body
  - This skill (weight 2): Commits what piv-implement left uncommitted.
  - piv-implement: Hands finished work to piv-commit.
- **piv-review-changes** · type: gate · source: description
  - This skill (weight 2): Expects the pre-commit review to have run first.
  - piv-review-changes: Runs before a commit as the pre-commit quality gate.
- **piv-fix-review-findings** · type: handoff · source: body
  - This skill (weight 2): Commits the fixes that piv-fix-review-findings made.
  - piv-fix-review-findings: Passes the fixes to piv-commit.
- **piv-implement-issue** · type: handoff · source: body
  - This skill (weight 2): Commits changes made by piv-implement-issue.
  - piv-implement-issue: Passes the regression-tested fix to piv-commit.
- **piv-run-full-loop** · type: chain · source: body
  - This skill (weight 2): Runs as the final commit stage of piv-run-full-loop.
  - piv-run-full-loop: Ends the chain with a commit.
- **rules-check-drift** · type: reference · source: body
  - This skill (weight 1): Named alongside rules-check-drift for rules-file changes.
  - rules-check-drift: Named alongside the commit step for rules-file changes.
- **terse-commit** · type: reference · source: body
  - This skill (weight 1): Follows its subject and body rules for the commit message.
  - terse-commit: Supplies the message rules that piv-commit applies.
<!-- relationships:end -->
