# Skill network

This folder holds the link map for the skills in `.claude/skills/`. It was built with the same method as the bidirectional-link-engine: every link is a reciprocal contract, and an audit checks both ends.

## How it works

1. `network/edges.json` is the source of truth. Each pair is one link, written into both skills.
2. `python3 network/build_network.py --write` writes the contracts into each `SKILL.md` between `relationships` markers, and adds a Dewey code to each description.
3. `python3 network/build_network.py --check` audits the result. It fails if a link lacks its reciprocal contract, if a contract has no entry in `edges.json`, if a block is stale, if frontmatter is not valid YAML, or if a Dewey code is missing. It exits 1 on any failure.

The check is link-matching, not block-presence. A skill that mentions another in passing does not pass unless the reciprocal contract exists and names the same link type.

## Current state

- 39 skills, 41 links (handoff 16, reference 11, feedback 5, chain 4, gate 3, dependency 2).
- Skills with no declared links yet: `ablate-ai-layer`, `agent-browser`, `ast-grep`, `build-signal-engine`, `drive-screen`, `edit-video`, `hooks-create`, `opportunity-scan`, `prime-backend`, `prime-frontend`, `second-brain-prd`, `setup-ai-tutor`, `skills-create`.

Isolated does not mean useless. It means no contract has been written, so these skills are not yet linked into any chain.

## Dewey index

Codes are a proposed classification, assigned for this repo. Check them before relying on them.

| Dewey | Skill | Linked |
|---|---|---|
| 004.16 | `drive-screen` | no |
| 004.678 | `agent-browser` | no |
| 005.1 | `build-dark-factory` | yes |
| 005.1 | `piv-implement` | yes |
| 005.1 | `piv-implement-issue` | yes |
| 005.1 | `piv-investigate-issue` | yes |
| 005.1 | `piv-plan-implementation` | yes |
| 005.1 | `piv-run-full-loop` | yes |
| 005.1 | `prime-backend` | no |
| 005.1 | `prime-codebase` | yes |
| 005.1 | `prime-frontend` | no |
| 005.120 | `skills-create` | no |
| 005.13 | `ast-grep` | no |
| 005.14 | `piv-fix-review-findings` | yes |
| 005.14 | `piv-review-changes` | yes |
| 005.14 | `piv-review-pr` | yes |
| 005.14 | `piv-validate` | yes |
| 005.8 | `hooks-create` | no |
| 005.8 | `piv-commit` | yes |
| 005.8 | `piv-create-pr` | yes |
| 005.8 | `worktree-create` | yes |
| 005.8 | `worktree-merge` | yes |
| 006.3 | `ablate-ai-layer` | no |
| 006.3 | `opportunity-scan` | no |
| 006.3 | `rules-check-drift` | yes |
| 006.3 | `rules-create-global` | yes |
| 006.3 | `system-evolution-review` | yes |
| 006.3 | `system-execution-report` | yes |
| 025.04 | `build-signal-engine` | no |
| 025.04 | `second-brain-audit` | yes |
| 025.04 | `second-brain-fix` | yes |
| 025.04 | `second-brain-prd` | no |
| 371.33 | `setup-ai-tutor` | no |
| 658.4012 | `piv-slice-epic` | yes |
| 658.4012 | `plan-architecture` | yes |
| 658.4012 | `plan-create-prd` | yes |
| 658.4012 | `plan-create-stories` | yes |
| 658.403 | `plan-with-priorities` | yes |
| 778.59 | `edit-video` | no |

## Feedback loops

Corrective (negative) loops, which pull the system back to a target:

- Review loop: `piv-review-pr` finds issues, `piv-fix-review-findings` fixes the chosen ones, `piv-validate` gives the verdict, and the review runs again until it passes.
- Fact loop: `second-brain-audit` writes a findings file, `second-brain-fix` corrects the facts in batches, and the next audit confirms what is left.
- Rules loop: `rules-check-drift` reports rules that are no longer true, and `rules-create-global` rewrites the root rules file.

Improvement (reinforcing) loop, which feeds each run into the next:

- `piv-implement` produces work, `system-execution-report` records what diverged, `system-evolution-review` classifies the divergences, and the fixes go back into `piv-plan-implementation` and `piv-implement` for the next run.

## Cross-fertilisation proposals

These are not contracts yet. Adding one means putting it in `edges.json` and rebuilding.

- `prime-codebase` with `prime-backend` and `prime-frontend`. The two scoped skills are narrower variants of the general one, which is progressive disclosure. Proposed type: reference.
- `opportunity-scan` with `hooks-create`. The scan finds what to encode, and the hook skill encodes it. Proposed type: handoff.
- `ablate-ai-layer` with `rules-check-drift`. Ablation asks whether a rule still earns its place, and drift asks whether it is still true. Proposed type: gate.

## Method, in order

1. Characterise each skill from its body, not its description.
2. Find candidate links by what the body names. Mark a link `body` when it is named in the body and `description` when it is inferred from the description only.
3. Write both ends in full. Each end gets its own sentence, so each side knows what it hands over and what it expects back.
4. Build, then audit. Treat any failure as a failure. Do not patch around it silently.
5. Record the feedback loops that the links create.

## Known gaps

- The eight-field contract and the eight relationship types from the bidirectional-link-engine memory are not all recoverable from notes. This repo uses six types (`dependency`, `handoff`, `gate`, `chain`, `feedback`, `reference`), with weights 3, 2 and 1. Check these against the original v1.0.0 files before treating them as canonical.
- Six of the 41 links are inferred from descriptions alone. They are marked `source: description`.
- The Dewey codes are assigned, not derived from a standard library.
- The description field uses `Dewey NNN` without a colon. A colon in an unquoted YAML value breaks parsing, which is why the `Dewey: NNN` form is not used here.
