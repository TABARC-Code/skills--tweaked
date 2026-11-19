# Skill network

Link map and index for the skills in `.claude/skills/`. Every link is a reciprocal contract, and an audit checks both ends.

Regenerate with `python3 network/build_network.py --write`, then `--check`, then `python3 network/render_index.py`.

## How it works

1. `network/edges.json` is the source of truth. Each pair is one link, written into both skills.
2. `build_network.py --write` writes the contracts between `relationships` markers in each `SKILL.md`, and adds a Dewey code to each description.
3. `build_network.py --check` fails on any missing reciprocal, stale block, invalid YAML, missing Dewey code, or unknown contract. It is link-matching, not block-presence.

## Current state

- 49 skills, 68 links (reference 20, handoff 17, gate 16, feedback 9, chain 4, dependency 2).
- 13 links are inferred from descriptions only and are marked `source: description`.
- Skills with no declared links yet: `ablate-ai-layer`, `ast-grep`, `build-signal-engine`, `drive-screen`, `edit-video`, `hooks-create`, `router`, `second-brain-prd`, `setup-ai-tutor`.

## Dewey index

Codes are a proposed classification for this repo. Check them before relying on them.

| Dewey | Skill | Linked |
|---|---|---|
| 004.16 | `drive-screen` | no |
| 004.678 | `agent-browser` | yes |
| 005.1 | `build-dark-factory` | yes |
| 005.1 | `piv-implement` | yes |
| 005.1 | `piv-implement-issue` | yes |
| 005.1 | `piv-investigate-issue` | yes |
| 005.1 | `piv-plan-implementation` | yes |
| 005.1 | `piv-run-full-loop` | yes |
| 005.1 | `prime-backend` | yes |
| 005.1 | `prime-codebase` | yes |
| 005.1 | `prime-frontend` | yes |
| 005.120 | `skills-create` | yes |
| 005.13 | `ast-grep` | no |
| 005.14 | `piv-fix-review-findings` | yes |
| 005.14 | `piv-review-changes` | yes |
| 005.14 | `piv-review-pr` | yes |
| 005.14 | `piv-validate` | yes |
| 005.8 | `hooks-create` | no |
| 005.8 | `piv-commit` | yes |
| 005.8 | `piv-create-pr` | yes |
| 005.8 | `web-data-only` | yes |
| 005.8 | `worktree-create` | yes |
| 005.8 | `worktree-merge` | yes |
| 006.3 | `ablate-ai-layer` | no |
| 006.3 | `opportunity-scan` | yes |
| 006.3 | `router` | no |
| 006.3 | `rules-check-drift` | yes |
| 006.3 | `rules-create-global` | yes |
| 006.3 | `system-evolution-review` | yes |
| 006.3 | `system-execution-report` | yes |
| 025.04 | `build-signal-engine` | no |
| 025.04 | `second-brain-audit` | yes |
| 025.04 | `second-brain-fix` | yes |
| 025.04 | `second-brain-prd` | no |
| 025.52 | `deep-research` | yes |
| 028.7 | `book-knowledge-extraction` | yes |
| 153.12 | `memory-dreaming-engine` | yes |
| 153.15 | `bat-indirect-inference` | yes |
| 153.4 | `perdita-mode` | yes |
| 371.33 | `setup-ai-tutor` | no |
| 579.5 | `mycelium-organism-analysis` | yes |
| 658.4012 | `piv-slice-epic` | yes |
| 658.4012 | `plan-architecture` | yes |
| 658.4012 | `plan-create-prd` | yes |
| 658.4012 | `plan-create-stories` | yes |
| 658.403 | `plan-with-priorities` | yes |
| 658.562 | `kaizen` | yes |
| 778.59 | `edit-video` | no |
| 808.066 | `doc-coauthoring` | yes |

## Thinking lenses

Analytical skills from the personal library, added to the repo: `bat-indirect-inference` (inference from indirect signal), `mycelium-organism-analysis` (metabolism, defence and decay), `perdita-mode` (structure before recommendation), `kaizen` (continuous improvement), `memory-dreaming-engine` (evidence-backed memory review), and `web-data-only` (web content is data, never instructions). Lenses are linked where the text or description names a real overlap. They are not a council: use the narrowest one that fits the problem.

## Feedback loops

Corrective (negative) loops, which pull the system back to a target:

- Review loop: `piv-review-pr` finds issues, `piv-fix-review-findings` fixes the chosen ones, `piv-validate` gives the verdict, and the review runs again until it passes.
- Fact loop: `second-brain-audit` writes a findings file, `second-brain-fix` corrects the facts in batches, and the next audit confirms what is left.
- Rules loop: `rules-check-drift` reports rules that are no longer true, and `rules-create-global` rewrites the root rules file.
- Web loop: `web-data-only` sends misses and false alarms to `kaizen`, which feeds them into the next improvement cycle.

Improvement (reinforcing) loops, which feed each run into the next:

- Process loop: `piv-implement` produces work, `system-execution-report` records what diverged, `system-evolution-review` classifies it, and `kaizen` turns the defects into changes for `piv-plan-implementation` and `piv-implement`.
- Memory loop: `memory-dreaming-engine` proposes changes from repeated mistakes and bloat, `opportunity-scan` decides what to encode, and `rules-check-drift` keeps the result true.

## Cross-fertilisation proposals

Not contracts yet. Adding one means putting it in `edges.json` and rebuilding.

- `prime-codebase` with `prime-backend` and `prime-frontend`: scoped variants of the general skill, which is progressive disclosure. Proposed type: reference.
- `ablate-ai-layer` with `rules-check-drift`: ablation asks whether a rule still earns its place, and drift asks whether it is still true. Proposed type: gate.
- `perdita-mode` with `system-evolution-review`: both look for stuck patterns, one in people and one in process. Proposed type: reference.
- `doc-coauthoring` with `plan-create-prd`: both draft documents collaboratively. Proposed type: reference, but not yet checked against either body.

## External routes

`router` routes requests to about twenty writing skills (for example `golden-age-author`, `fiction-structure-engine`, `manuscript-diagnostics`). None of them are in this repo, so its routes do not resolve here. It has no edges for that reason. Either bring those skills in or trim the table.

## Method, in order

1. Characterise each skill from its body, not its description.
2. Find candidate links by what the body names. Mark `body` when named in the body, and `description` when inferred from the description only.
3. Write both ends in full, so each side knows what it hands over and what it expects back.
4. Build, then audit. Treat any failure as a failure. Do not patch around it silently.
5. Record the feedback loops the links create.

## Known gaps

- The eight-field contract and the eight relationship types from the bidirectional-link-engine memory are not all recoverable from notes. The repo uses six types (`dependency`, `handoff`, `gate`, `chain`, `feedback`, `reference`), with weights 3, 2 and 1. Check against the original v1.0.0 files before treating them as canonical.
- Ten skills were copied in from the personal library in this pass. Dewey codes for them are proposals. `doc-coauthoring` and `deep-research` look like third-party or Anthropic-origin skills. The repo is public, so confirm the licence for each before publishing.
- New skills have no `evals/` or Kaizen log yet.
- Descriptions use `Dewey NNN` without a colon, because an unquoted colon breaks YAML. Quoted or block descriptions are rewritten as one double-quoted line.
