---
name: skill-builder
description: "Build, improve, test, classify, link, and maintain reusable skills using a split workflow: creative exploration, controlled handoff, structured engineering, practical Skill Creator execution, relationship contracts, and Dewey-style future indexing. Use this when creating a new skill system, improving an existing skill, organising sub-skills, preparing evals, auditing links, or building a scalable skill repository rather than a one-off prompt. Dewey 005.120."
metadata:
  author: TABARC-Code
  author_url: https://github.com/TABARC-Code/
  dewey_decimal_code: '005.120'
  classification_label: Computer programming, programs, and skill-building systems
  version: '2.3.2'
---

# Skill Builder

Author: TABARC-Code  
Repository: https://github.com/TABARC-Code/

Use this as the main entry skill for the repo. It routes work to the correct sub-skill instead of trying to do everything in one swollen Markdown beast.

## Purpose

Turn rough ideas into reusable, tested, classified, and maintainable skills.

## Default Routing

```text
Creative Exploration Engine
Next: Skill Handoff Bridge
Next: Structured Skill Engineering System
Next: Skill Creator
```

Use the sidecar sub-skills when needed:

- **Relationship Contract Engine** when skills, sub-skills, links, reciprocal contracts, chains, or relationship maps change.
- **Skill Classification Engine** when assigning or updating Dewey-style identity codes for listing, indexing, future discovery, or skill linking.

## Operating Rule

Do not let creative ideation certify itself. Do not let engineering smother early exploration. Use the bridge. Use classification for future retrieval. Use relationship contracts when links actually change behaviour.

## Change-Control Procedure (Cascade Prevention)

Applies to every edit made through this workflow, including edits done inside the sub-skills below.

**The failure mode:** a requested change spawns a follow-up fix, that fix spawns another, and the task quietly expands into a redesign. Each step looks locally reasonable. The combined result silently alters behaviour nobody asked to change. A dependency being affected is not permission to modify it.

**Before editing**, state:
- the exact requested change
- files/sections/rules directly affected
- dependencies that may be indirectly affected
- behaviour that must stay unchanged
- the limit of the authorised edit

**Classify every touched component:**
- *Directly affected* - edit required to fulfil the request
- *Indirectly affected* - check it, do not edit it without separate authorisation
- *Unaffected* - leave it alone

**Make the smallest valid change.** No refactoring unrelated sections, no renaming working concepts, no rewriting stable text for style, no new abstractions, no fixing unrelated defects in the same pass.

**Stop and reassess (do not continue automatically) when:**
- a fix needs changes in more than one further subsystem
- the update starts changing existing public behaviour
- a new rule contradicts an established rule
- examples, schemas, or docs all need broad revision
- the change is becoming a redesign rather than a correction
- more than one follow-up change is needed to repair the last one

When this fires, record: the original request, the newly discovered dependency, the consequence of touching it, and the safest options. Then stop.

**After the edit, validate:**
1. reciprocal links/references still hold
2. no contradictions with existing instructions
3. examples still match the rules
4. schemas, inputs, outputs, tool contracts still line up
5. previously valid behaviour still works
6. no unrelated section changed
7. every correction made during validation gets re-checked

**Report out-of-scope findings, never fix them silently:**

```
Discovered issue: ...
Cause: ...
Current impact: ...
Recommended fix: ...
Scope expansion: ...
```

**Completion markers:**
- `[VALIDATION_COMPLETE]` - requested behaviour works, all direct dependencies checked, nothing unrelated changed, no unresolved contradiction in scope, all fixes re-checked.
- `[VALIDATION_BLOCKED: CASCADE_RISK]` - unresolved cascade risk remains; stop and report instead of continuing.

## Expected Output

When building or updating a skill, produce:

1. a clear skill draft or patch
2. relevant eval/test material where useful
3. relationship contract updates where links changed
4. a Dewey-style classification identity for the new or changed skill, applied quietly every time, not only when it feels significant
5. brief notes saying what changed, without corporate fog machine language

## Sub-Skill References

This package contains exactly one installable `SKILL.md`. The operational sub-skills live as referenced instruction files:

- `creative-exploration-engine/SUBSKILL.md`
- `skill-handoff-bridge/SUBSKILL.md`
- `structured-skill-engineering-system/SUBSKILL.md`
- `skill-creator/SUBSKILL.md`
- `relationship-contract-engine/SUBSKILL.md`
- `skill-classification-engine/SUBSKILL.md`

Before delivering or publishing a skill, run `skill-security-scanner` on the folder. For a quick single skill, `skills-create` is the lighter route.

Read only the referenced sub-skill file needed for the current phase. Do not treat these files as separately installable skills.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **skills-create** · type: reference · source: body
  - This skill (weight 1): Is the heavier route; skills-create is the lighter route for a single skill.
  - skills-create: Points to it for skill systems, relationship networks, Dewey codes and evals.
- **skill-security-scanner** · type: gate · source: body
  - This skill (weight 2): Runs it before delivering or publishing a skill.
  - skill-security-scanner: Is called by skill-builder before delivery or publication.
- **router** · type: handoff · source: body
  - This skill (weight 2): Is the route for skill-system requests.
  - router: Routes skill systems, links and evals to it.
<!-- relationships:end -->
