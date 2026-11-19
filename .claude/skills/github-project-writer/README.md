# GitHub Project Writer

A Claude skill for writing, auditing and repairing the two documents every repository
ends up needing: `README.md` and `description.md`. It's aimed at the case where you know
the project inside out, you've written the code, and you cannot face writing the front
door for it again.

Author: TABARC-Code

## What it does

It produces documentation in the voice of the person who built the thing. Not marketing
copy. The skill grades every material claim against the evidence actually available (code
first, then config, then tests, then manifests, and so on down), and where the evidence
runs out it says so rather than inventing a plausible command.

It also keeps the two documents doing different jobs. The README answers "can I use
this". The description answers "why is it like this, and what should I know before I
change it". If a paragraph would sit equally well in either file, that's a fault, and the
skill treats it as one.

## Status

Implemented and in use. Version 3.0.0.

Version 3.0.0 absorbs a sibling skill, `repo-doc-writer`, that used to sit alongside this
one. The split had made sense for a while: this skill carries an eight-category rubric, a
bounded Kaizen loop and five output modes, and none of that earns its place when there's
no documentation yet and someone just wants two files written properly. So
`repo-doc-writer` existed as a leaner, write-only drafting path.

The trouble is the two skills carried the same never-invent list, the same evidence
hierarchy and the same document outlines, maintained by hand in two places.
`repo-doc-writer`'s own description admitted as much: "Keeping them in sync is manual, and
it won't happen, so expect them to drift." It had, by the time this merge happened,
drifted in exactly the direction you'd expect: sharper number and punctuation
conventions, an explicit Oxford comma rule and an arrow-glyph ban that had never made it
back into this file.

Rather than keep two skills or delete the leaner one outright, `repo-doc-writer`'s actual
reason for existing, drafting without the rubric sitting in context at all, survives here
as **draft speed**, a mode of `CREATE` (section 10). Reviewed speed is everything this
skill already did: the full loop for audits, rewrites, patches and anything published as
authoritative. `repo-doc-writer` itself is retired.

## Layout

```
github-project-writer/
├── SKILL.md                        core rules, routing, output modes, both speeds
├── README.md                       this file
├── description.md                  design notes
└── references/
    ├── readme-spec.md              section-by-section README specification
    ├── description-spec.md         section-by-section description specification
    └── quality-loop.md             Kaizen stages, rubric, adversarial checks, gate
                                     (reviewed speed only)
```

`SKILL.md` is always read. The reference specs load when a document is in scope.
`quality-loop.md` loads only for reviewed-speed work, which is most jobs except a fresh
draft of both files.

## Installation

Copy the `github-project-writer` folder into your skills directory. For Claude.ai that
means uploading the packaged `.skill` file and saving it from the file card. For Claude
Code, drop it in your skills path and restart the session.

There's no build step. There's nothing to configure. This is one of the few genuinely
boring installs you'll do today.

If you still have `repo-doc-writer` installed anywhere, remove it. This skill's
description now covers the same trigger phrases, and running both risks a genuinely
confusing double-trigger.

## Using it

Say what you want in ordinary language. The skill triggers on README work, repository
descriptions, setup guides, "idiot's guide" sections, documentation audits, and the more
plaintive variants like "this README is rubbish, fix it" or "I need a README for this".

Six output shapes, across two speeds:

- **CREATE, draft speed** (the default for a fresh pair of files) when nothing useful
  exists yet and you just want it written properly the first time
- **CREATE, reviewed speed** when the same is true but the material is sensitive enough
  to want the full loop run over it before it ships
- **REWRITE** when the structure is broken but the facts are sound
- **AUDIT** when you want the problems listed and nothing touched
- **AUDIT + REWRITE** when you want both
- **PATCH** when the docs are basically fine and you want the smallest possible change

PATCH is the default preference where it'll do. A rewrite that changes nothing material is
just churn with better formatting.

### Feeding it evidence

Give it the repository if you can. Manifests, entry points, config, routes, tests, the
Dockerfile if there is one. The skill reads for use rather than for names, so a function
called `syncEverything` won't become a documented feature unless something actually calls
it.

If you can't supply source, it'll still work, but the output will carry more hedging. That
hedging is deliberate. Don't strip it out unless you know the claim holds.

## What it won't do

It won't invent commands, benchmarks, contributors, release history, changelog entries,
supported platforms or passing tests. If you want a README that makes a two-week-old
project look like a mature ecosystem, this is the wrong tool and honestly the wrong idea.

It also won't redesign your software on paper. If the documentation exposes a contradiction
in the project, it flags the contradiction. It doesn't quietly document the version you
meant to build.

## Known limitations

The skill can only be as accurate as the material you give it. Point it at a repo with
stale docs and no source and it will do its best, but "its best" in that situation is a
lot of qualified language.

The 2% cynicism budget is a stylistic direction, not something measurable. In practice it
drifts upward when the subject matter is amusing, which is why there's an explicit check
for it in both the draft-speed gate and the reviewed-speed loop. It still drifts
occasionally.

`SKILL.md` now sits at just under 660 lines, further above the 500-line guideline than
before the merge. The obvious next candidate for splitting out is the source-inspection
checklist in section 4, which hasn't moved yet because three reference files already felt
like enough fragmentation for a skill this size.

Draft speed's own gate (section 14) hasn't been run against the same volume of real
repositories that reviewed speed has. It's a reasonable checklist built by trimming the
existing rubric down to binary pass/fail, not something independently validated.

## Licence

Not specified here. Set one before you publish the repository.
