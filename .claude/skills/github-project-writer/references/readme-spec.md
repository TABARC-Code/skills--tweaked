---
name: readme-spec
description: Section-by-section specification for README.md. Read before drafting, auditing or repairing a README.
---

<!-- Read this together with references/description-spec.md. The two documents are
     written as a pair and the separation test in SKILL.md section 8 assumes both
     specifications are in context when both files are being produced. -->

# README.md specification

The README is the practical public front door.

Its primary question is:

> Can the intended reader understand what this is and get from repository to useful
> first run without being misled?

Use only sections that help answer that question.

A suitable structure may include:

# Project Name

A compact opening paragraph explaining what it is, who it is for and why it exists.

## What it does

Explain observable behaviour in plain English.

Prefer:
> It reads WordPress posts through the REST API and can create new posts as drafts.

Over:
> It provides a robust content-management integration.

## Status

When helpful, state clearly which parts are:
- implemented
- experimental
- incomplete
- planned

Do not make users infer maturity from tone.

## Why it exists

Give project rationale when known.

## Features

Use a list only when it is easier to scan than prose.

Separate implemented, experimental and planned capabilities.

## How it works

Explain the relevant architecture or data flow.

Use Mermaid or ASCII diagrams only when they reduce explanation rather than decorate it.

## Requirements

State real prerequisites:
- runtimes
- supported versions where known
- accounts/services
- permissions
- hardware
- network access

## Installation

Give exact commands when known.

Never invent commands to make the section look complete.

## Setup

Explain first-run configuration and environment variables.

For each important value, explain:
- what it is
- whether it is required
- where it comes from
- safe/default behaviour when known
- consequences of changing it

## Idiot's guide

When requested, provide a genuinely beginner-safe walkthrough.

Assume the reader may not know:
- what a terminal is
- what directory a command runs in
- how to create an `.env` file
- how hidden file extensions behave on Windows
- where credentials are obtained
- how to recognise a successful start
- where logs or errors appear

Do not infantilise the reader.

Explain the physical action.

Weak:
> Configure the environment.

Better:
> In the project folder, create a file named `.env`. Open it in a text editor and add the
> following values. On Windows, make sure the file has not silently become `.env.txt`.

Where commands differ materially by operating system, separate them.

## First successful run

Where possible, show what success looks like:
- expected console line
- endpoint response
- created draft
- generated file
- visible UI state

This is more useful than ending installation at "run the command".

## Usage

Give realistic examples supported by the implementation.

## Configuration

Explain meaningful values, defaults and consequences.

## Security

Describe actual:
- trust boundaries
- secrets
- credentials
- permissions
- network exposure
- write capabilities
- destructive capabilities
- logging implications

Do not claim the project is "completely secure".

## Troubleshooting

Include only problems that can be derived from the implementation, supplied experience or
very direct dependency behaviour.

Prefer:
**Symptom > probable cause > check > fix**

Do not manufacture a FAQ from imaginary support tickets.

## Known limitations

State practical shortcomings without theatre.

## Development notes

Use programmer perspective where it explains architecture or maintenance choices.

## Roadmap

Only include plausible future work.

Label it as planned.

## Contributing

Include only when appropriate and supported.

## Licence

Include only when known.

---

---

# Handshake with `description.md`

The README is the operational document. It answers *can I use this*. Whenever drafting a
README section, note the material that surfaced but does not belong here, and pass it
across:

| Surfaced while writing the README | Send to `description.md` |
|---|---|
| A design decision explaining why setup is awkward | Design decisions |
| An internal component discovered while tracing a command | Architecture |
| A trade-off behind a conservative default | Design decisions |
| A boundary the user does not cross but a maintainer does | Trust and boundaries |
| A limitation caused by structure rather than configuration | Limitations and awkward bits |

Flow runs both ways. If `references/description-spec.md` produces a constraint that
changes what a user must actually do, that constraint returns here as a Requirements,
Setup or Security line. Neither document is finished until the other has been read.

# Feedback signals this spec collects

Record these while drafting so the Kaizen loop in `references/quality-loop.md` has
something concrete to act on.

**Positive signals** (reinforce and keep):
- a setup step that can be traced to a real command or manifest entry
- a success indicator taken from observed output
- a section that was deleted because it added nothing

**Negative signals** (repair before returning):
- a command whose syntax is plausible but unsourced
- a Features entry with no evidence class attached
- a section that reads as a template heading with one sentence beneath it
- a paragraph that would sit equally well in `description.md`
