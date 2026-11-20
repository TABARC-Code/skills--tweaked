# Project Description

## The short version

A skill-building system split into stages on purpose, because doing idea generation, engineering validation, and practical building inside one file tends to produce something that looks clever and behaves like wet cardboard. Currently at v2.3.2, having just had a real triggering bug fixed across all six of its sub-skills.

## The problem

Skill repositories drift in two opposite directions. Left unstructured, they accumulate vague, half-finished ideas with no evaluation discipline. Over-engineered from the start, they choke fast iteration before an idea has had a chance to prove itself. Both failure modes get worse as a repository grows, because nothing is checking whether the links between skills still mean anything.

There's a more specific version of the drift problem this version fixes directly. Every one of this repository's six sub-skills used to carry its own `name`/`description` frontmatter - reasonable-looking on a file-by-file basis, and exactly the pattern that makes a file independently triggerable rather than read only when its router sends Claude there. This repository's own `skill-creator` sub-skill shares a name with an entirely unrelated, separately-installed `skill-creator` skill; with both carrying triggering frontmatter, nothing prevented an ambiguous request from firing the wrong one.

## The approach

Four sequential stages, deliberately kept separate: creative exploration, controlled handoff, structured engineering, practical building. Two sidecar layers - relationship contracts and classification - that activate on their own trigger condition rather than only running at the end of the pipeline. And, as of v2.3.1, exactly one file in the whole repository carries triggering frontmatter: the router. Every sub-skill lost its own `name`/`description` block and gained a one-line header instead, stating plainly that it's a sub-skill, not independently installable, with its identifier and Dewey code.

## Architecture

```text
SKILL.md - router; the only file with triggering frontmatter
├── creative-exploration-engine/SUBSKILL.md
├── skill-handoff-bridge/SUBSKILL.md
├── structured-skill-engineering-system/SUBSKILL.md
├── skill-creator/SUBSKILL.md - plus scripts/, agents/, assets/, references/, evals/
├── relationship-contract-engine/SUBSKILL.md
└── skill-classification-engine/SUBSKILL.md
```

`SKILL_MANIFEST.md` assigns each sub-skill a layer (L0 through L4, hybrids where a sub-skill spans two) and a Dewey-style code - 005.120 for the router itself, 153.350 for creative exploration, and so on through the table. The codes are an identity and shelf-mark system; they don't carry behavioural weight on their own. `RELATIONSHIP_MAP.md` carries the actual behavioural contracts.

`skill-creator` is the heaviest sub-skill by file count - bundled agent instructions, JSON schemas, HTML review assets, and Python scripts for benchmarking and packaging sit underneath it. Its own `SUBSKILL.md` stays short and points to the heavier resources only when a given task actually needs them, rather than loading all of it up front.

## Design decisions

**Exactly one router, no exceptions, even for a resource-heavy sub-skill.** `skill-creator` carries by far the most bundled material of the six, and it would have been simple to give it its own triggering frontmatter on the reasoning that it's substantial enough to stand alone. That reasoning is exactly how the collision this version fixes got introduced in the first place. The rule holds without a size exception.

**The rename that took three passes.** The repository used to be called `option-b-skill-builder`. The first rename pass updated the identity files - `SKILL.md`, `CLASSIFICATION_INDEX.md`, `SKILL_MANIFEST.md`, the docs. It missed two self-references buried in body text. The second pass (v2.3.1) caught those and, separately, did the frontmatter-stripping fix described above. It still missed six more mentions of the old name sitting in running prose inside `RELATIONSHIP_MAP.md` and five sub-skills' closing sections - headers and titles get caught by a rename pass; sentences describing the system in passing don't, unless someone greps the whole repository rather than trusting the previous pass's file list. v2.3.2 did that full-repo grep and fixed the remainder. Recorded here because the pattern (rename catches structure, misses prose, requires a second look) is likely to recur somewhere else in this repository eventually.

**Sidecar engines instead of pipeline stages.** Relationship contracts and classification codes don't sit at the end of the four-stage workflow - they trigger whenever their specific condition is met, mid-pipeline if needed. A link created during the creative stage still needs a contract; waiting until packaging to write it down invites exactly the drift the contract system exists to prevent.

## Trust and boundaries

The Change-Control Procedure in `SKILL.md` bounds what an edit is allowed to touch: classify what the change directly affects, indirectly affects, or leaves alone, then make the smallest valid change and stop. Discovered problems outside a request's scope get reported, not fixed silently mid-task - `SKILL_MANIFEST.md`'s Change Discipline section states this as a standing rule, not a per-task judgement call. No credentials or external services; the Python scripts under `skill-creator/scripts/` operate on local skill files only.

## Current state

v2.3.2. NOTES.md carries the full changelog; the two most consequential entries are the v2.3.1 frontmatter fix and the v2.3.2 cleanup of the six remaining rename leftovers, both described above. `ROUTER_GATING_EVALS.md` is new in this version and exists specifically to verify the gating fix holds - three qualitative test prompts, not a full regression suite. `skill-creator`'s own eval tooling (`evals/evals.json`, the grading/comparison/benchmark scripts) is bundled and structurally present; nothing in this repository demonstrates a completed run of it end to end.

## Limitations and awkward bits

Six sub-skills plus two sidecar engines is a lot of surface area for a solo-maintained repository to keep internally consistent, and the rename history above is evidence that "internally consistent" takes more than one pass to actually achieve. `ROUTER_GATING_EVALS.md` checks the gating mechanism, not the quality of what `skill-creator` produces when it builds a skill - those are different questions, and only one of them currently has a test.

## Future direction

An eval suite for `skill-creator`'s actual output quality would be the natural next addition, parallel to the gating evals that now exist for the router mechanism. Beyond that, the rename-leftover pattern found twice now (v2.3.1 missing prose, v2.3.2 fixing it) suggests a full-repository grep for stale self-references might be worth adding as a standing step in the Change-Control Procedure itself, rather than something that only happens when a pass happens to catch it.
