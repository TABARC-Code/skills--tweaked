---
name: description-spec
description: Section-by-section specification for description.md. Read before drafting, auditing or repairing a project description.
---

<!-- Read this together with references/readme-spec.md. The two documents are written as
     a pair and the separation test in SKILL.md section 8 assumes both specifications are
     in context when both files are being produced. -->

# description.md specification

`description.md` should complement the README rather than paraphrase it.

Its primary question is:

> Why is the project shaped this way, what state is it really in, and what should another
> developer understand before changing it?

Suitable sections may include:

# Project Description

## The short version

One or two paragraphs.

## The problem

Describe the actual problem and constraints.

## The approach

Explain the design approach and governing choices.

## Architecture

Explain major components and their relationships.

## Data or control flow

Include when it clarifies operation.

## Design decisions

Record meaningful trade-offs, rejected simplifications or safety choices when known.

## Trust and boundaries

Describe what the software owns, what external systems own, and where credentials or
authority cross boundaries.

## Current state

Distinguish:
- working
- partial
- experimental
- planned
- unknown

## Operational notes

Mention deployment, maintenance, configuration and expected use.

## Limitations and awkward bits

Use candid programmer language.

This is a natural place for the occasional dry aside, but factual clarity still wins.

## Future direction

Explain plausible development without pretending it already exists.

---

---

# Handshake with `README.md`

`description.md` is the reasoning document. It answers *why is it shaped like this, and
what should I know before I change it*. It inherits facts from the README rather than
re-deriving them.

| Surfaced while writing the description | Send to `README.md` |
|---|---|
| An architectural constraint that forces a manual setup step | Setup |
| A boundary that determines which credentials a user supplies | Security |
| A component whose failure produces a visible error | Troubleshooting |
| A partial subsystem the user will meet immediately | Status |
| A design decision that changes recommended usage | Usage |

Do not restate the README's installation sequence here. Explain instead why it is that
sequence. If the explanation cannot be given without repeating the steps, the steps are
probably under-explained in the README and should be repaired there.

# Feedback signals this spec collects

**Positive signals** (reinforce and keep):
- a trade-off recorded with the option that was rejected
- a boundary described in terms of what crosses it
- a current-state entry that names its evidence class

**Negative signals** (repair before returning):
- rationale invented to make a decision look deliberate
- architecture described from filenames rather than from use
- a paragraph liftable into the README unchanged
- future direction written in the present tense
