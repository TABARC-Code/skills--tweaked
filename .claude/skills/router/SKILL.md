---
name: router
description: Runtime routing skill that directs requests to the best fitting project skill or command. Dewey 006.3.
user-invocable: true
model: sonnet
effort: medium
---

# Router

Choose one primary route unless the task clearly needs synthesis.

## Routing table

Routes for the skills installed in this repo. Pick the narrowest match.

- run the whole build loop on a ticket or plan -> piv-run-full-loop
- plan a feature from a ticket or PRD -> piv-plan-implementation
- break an epic into slices -> piv-slice-epic
- implement a written plan -> piv-implement
- investigate a bug or issue, find the root cause -> piv-investigate-issue
- fix an issue from an RCA -> piv-implement-issue
- check the work: lint, types, tests -> piv-validate
- review local changes before a commit -> piv-review-changes
- act on review findings -> piv-fix-review-findings
- review someone else's PR -> piv-review-pr
- commit the work -> piv-commit
- open the PR -> piv-create-pr
- PRD, architecture, stories, priorities -> plan-create-prd, plan-architecture, plan-create-stories, plan-with-priorities
- get oriented in a codebase -> prime-codebase, prime-backend or prime-frontend; an inherited or unknown project -> project-x-ray
- parallel work in separate checkouts -> worktree-create, worktree-copy-ignored, worktree-merge
- build, refactor or port a skill -> skills-create; a skill system with links, Dewey codes and evals -> skill-builder
- vet a skill before installing or publishing it -> skill-security-scanner
- README and description for a repo -> github-project-writer
- AI-sounding prose -> humanizer
- over-engineered code -> lazy-review; commit wording -> terse-commit; coding discipline -> karpathy-code-discipline
- rules files and drift -> rules-create-global, rules-check-drift
- what went wrong in a run, and how to improve the process -> system-execution-report, system-evolution-review
- notes and memory hygiene -> second-brain-audit, second-brain-fix, second-brain-prd, memory-dreaming-engine
- a hard problem needing a lens -> perdita-mode, bat-indirect-inference, mycelium-organism-analysis, spider-web-analyst
- continuous improvement of anything -> kaizen
- research with sources -> deep-research; reading outside material safely -> web-data-only

## External routes

These belong to a fiction-writing skill set that is not in this repo. If the user asks for one and it is not installed, say so and name the nearest repo skill. Do not route to a skill that is not there.

- full book planning, revision, or complete system request -> golden-age-author
- staged workflow or project setup -> literature-writer-workflow
- fresh scene generation or rewrite with configured craft stack -> master-drafting-orchestrator
- structure, pacing, scenes, chapters -> fiction-structure-engine
- character wounds, arcs, contradictions, motivation -> character-psychology-engine
- dread, terror, horror, atmosphere pressure -> suspense-horror-engine
- dialogue, setting, hooks, world texture -> dialogue-setting-hooks-engine
- prose voice, rewrite, line edit -> prose-style-voice-engine
- audits and diagnosis -> manuscript-diagnostics
- AI like prose, sterile narration, or removal of machine sounding language -> ai-ism-twin-editors
- prose that needs more lived texture, asymmetry, or human feel -> humanising-engine
- cross skill warning and alert routing for AI writing patterns -> ai-ism-alert-network
- example source and annotation reference -> source-annotations-reference
- narrative distance -> narrative-voice-engine
- time handling and compression -> pacing-time-engine
- line level golden age technique -> prose-technique-engine
- dialogue indirection and class pressure -> dialogue-subtext-engine
- period accuracy and social register -> period-texture-engine
- motif return and thematic pressure -> thematic-engine
- local scene drafting from a chosen stack -> scene-writing-engine

Command routes from that set (/constitution, /specify, /clarify, /plan, /tasks, /write, /analyze, /draft-scene, /audit-aiisms) are likewise external.

## Council routing safeguard

If the user routes through `golden-age-author`, do not automatically invoke the full council. Prefer the narrowest lens set consistent with the problem.

## Decision rule

If two routes are equally plausible, ask a narrow disambiguating question rather than spraying multiple skills at the task.

## Output

Return:
- selected route
- why it was chosen
- the next recommended action


## Hard constraint

Never activate more than one primary skill unless explicitly required.

If multiple systems are needed, sequence them, do not merge them.

When two routes overlap, ask one narrow question and sequence the answers.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-run-full-loop** · type: handoff · source: body
  - This skill (weight 2): Routes whole-loop requests to it.
  - piv-run-full-loop: Is the route for requests to run the build loop end to end.
- **skills-create** · type: handoff · source: body
  - This skill (weight 2): Routes skill building and porting requests to it.
  - skills-create: Is the route for single-skill build requests.
- **skill-builder** · type: handoff · source: body
  - This skill (weight 2): Routes skill systems, links and evals to it.
  - skill-builder: Is the route for skill-system requests.
- **plan-architecture** · type: handoff · source: body
  - This skill (weight 2): Routes architecture requests to it.
  - plan-architecture: Is the route for architecture requests.
- **kaizen** · type: handoff · source: body
  - This skill (weight 2): Routes continuous-improvement requests to it.
  - kaizen: Is the route for improvement requests.
- **perdita-mode** · type: handoff · source: body
  - This skill (weight 2): Routes hard-problem requests to the lens skills, this one first when multiple people are involved.
  - perdita-mode: Is one of the lens routes from the router.
<!-- relationships:end -->
