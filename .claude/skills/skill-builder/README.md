# Skill Builder

**Author:** TABARC-Code

A six-part system for building Claude skills, split so that fast, messy idea generation never has to share a file with formal engineering standards. One router (`SKILL.md`), six reference sub-skills, and two sidecar layers that keep links and identity codes honest as the repository grows.

## What it does

Turns a rough idea into a packaged, tested skill through four sequential stages - creative exploration, a controlled handoff, structured engineering, and practical building - plus two sidecar layers that run whenever links or classification codes are touched, not just at the end. It also builds and evaluates other skills directly: `skill-creator` carries the grading, comparison, and packaging tooling that does the actual work.

## Status

Implemented and current at v2.3.2: the router, all six sub-skills, the Change-Control Procedure (cascade prevention for edits), and `ROUTER_GATING_EVALS.md` - three test prompts checking that the sub-skills stay gated behind the router rather than triggering independently.

That gating fix is the headline change in this version. Earlier releases gave every sub-skill its own `name`/`description` frontmatter, which made each one independently triggerable - the same class of bug that let an unrelated `skill-creator` skill collide with this repository's own sub-skill of the same name. v2.3.1 stripped that frontmatter from all six sub-skills and replaced it with a plain router-only header; v2.3.2 caught and fixed six leftover mentions of the repository's old name ("Option B") that the rename missed on the first pass. Full history in `NOTES.md`.

Unverified: whether `skill-creator`'s bundled scripts run cleanly end-to-end in a given environment hasn't been confirmed here - the scripts and their schemas exist (`skill-creator/scripts/`, `skill-creator/references/schemas.md`), but no run output is bundled as evidence.

## The system

| Sub-skill | Role |
|---|---|
| `creative-exploration-engine` | Fast ideation - variants, fragments, rough direction |
| `skill-handoff-bridge` | Turns creative material into a structured handoff packet |
| `structured-skill-engineering-system` | Defines architecture, evaluation, failure logic, scale control |
| `skill-creator` | Builds, tests, packages, and description-optimises the actual skill, using bundled eval tooling |
| `relationship-contract-engine` | Keeps skill and sub-skill links reciprocal, weighted, and auditable |
| `skill-classification-engine` | Assigns Dewey-style identity codes for indexing and future linking |

None of the six are independently installable - see `description.md` for why that matters more than it might sound.

## How it works

```text
Creative Exploration Engine
Next: Skill Handoff Bridge
Next: Structured Skill Engineering System
Next: Skill Creator
<> Relationship Contract Engine - whenever links, sub-skills, or reciprocal updates are involved
<> Skill Classification Engine - whenever a skill needs a catalogue identity or Dewey-style code
```

The creative stage doesn't self-certify its own output. The bridge doesn't over-evaluate what it's handed. Structured engineering defines what "reliable" actually means before anything gets built. Skill Creator does the practical work and runs the eval loop. The two sidecar engines run whenever their trigger condition is met, not only at the end of the pipeline.

## Requirements

Markdown instruction content plus a small set of Python scripts under `skill-creator/scripts/` for benchmarking, review generation, and packaging. No external services; the scripts operate on local skill files.

## Setup

Place the repository wherever Claude's skill discovery looks for user skills. No configuration file - sub-skill routing and eval tooling are all in the bundled files.

## Usage

Full walkthrough in `USAGE.md`; worked example in `EXAMPLE_WORKFLOW.md`. In brief: start with `creative-exploration-engine` for a foggy idea, hand off through `skill-handoff-bridge` once there's a direction, define the architecture with `structured-skill-engineering-system`, then build with `skill-creator`. Bring in the two sidecar engines whenever the work changes a link or needs a catalogue code - not only at the end.

## Known limitations

This is heavier than a single-file skill, on purpose - see `description.md` for the reasoning - but that means more files to keep in sync when something changes, which is exactly what the Change-Control Procedure in `SKILL.md` exists to bound. `ROUTER_GATING_EVALS.md` checks that the gating fix holds; it doesn't check the quality of skills `skill-creator` produces, which has no equivalent eval suite yet.

## Licence

MIT - repository convention; no `LICENSE` file is bundled in this package.
