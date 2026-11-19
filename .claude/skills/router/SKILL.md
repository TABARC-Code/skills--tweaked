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

## Command routes

- /constitution
- /specify
- /clarify
- /plan
- /tasks
- /write
- /analyze
- /draft-scene
- /audit-aiisms

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

Use `skill-execution-governor` whenever routing pressure causes overlap or ambiguity.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

No links declared yet. Add one in network/edges.json and rebuild.
<!-- relationships:end -->
