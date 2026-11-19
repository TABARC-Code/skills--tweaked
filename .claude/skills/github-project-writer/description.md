# Project Description

Author: TABARC-Code

## The short version

A Claude skill that writes repository documentation the way a maintainer would, with the
evidential discipline that maintainers usually skip. It treats every technical assertion
as a claim that has to be traceable to something, and it treats the README and the
description as two different documents with two different jobs rather than one document
split across two files. As of 3.0.0 it also does the job at two speeds, having absorbed
the sibling skill that used to exist purely to offer the fast one.

## The problem

Generated project documentation fails in a small number of very predictable ways.

It invents commands that look right. It promotes a TODO into a feature. It reads a test
file and concludes the tests pass. It writes "robust", "seamless" and "comprehensive" into
sentences that carry no information. It produces a README and a description that say the
same thing twice, once at length and once at slightly less length.

Underneath all of those is one failure: the drafter treats its own fluency as evidence.
A sentence that reads confidently gets shipped as fact. That's the thing this skill is
built to interrupt.

There was a second, quieter problem, specific to this skill's own history. The machinery
built to interrupt the first problem (an evidence hierarchy, an eight-category rubric,
eight Kaizen stages, adversarial checks) earns its place when documentation has drifted
and needs repair. It earns nothing when there's no documentation yet and someone just
wants two files written properly the first time. Having the rubric sitting in context
shapes a draft even when the score is never computed, so a genuinely fast path needed the
rubric absent, not just unused. For a while the answer was a second skill,
`repo-doc-writer`. Its own description named the cost directly: two never-invent lists,
two evidence hierarchies, two document outlines, kept in sync by hand, which meant not
kept in sync at all. This version folds the fast path back in as a mode rather than a
skill.

## The approach

Three mechanisms now, where there used to be two plus a whole second skill.

The first is an evidence hierarchy. Executable behaviour outranks configuration, which
outranks tests, which outranks manifests, which outranks user statements, which outranks
existing docs, which outranks comments, which outranks a suggestive filename. Every
material claim gets an internal status: verified, supported, user-stated, planned, or
unknown, at reviewed speed. At draft speed the status is skipped and the hedge word goes
straight into the sentence, because the label only exists to drive a rubric that draft
speed doesn't load.

The second is a bounded Kaizen loop, run at reviewed speed only. Draft, critique as though
reviewing somebody else's work, repair only what the critique named, regression check,
stop. The critique is a separate pass on purpose. A first draft cannot certify itself, and
an unbounded improvement loop is just a slow rewrite of the same paragraph.

The third is the speed choice itself. Draft speed is the ordinary case and the default for
a fresh pair of files: work the sequence in section 0.1, apply the section 14 gate, ship
it. Reviewed speed is everything the rubric governs: audits, rewrites, patches, and any
fresh draft where the material is sensitive enough to want the loop run over it before it
goes out. The two speeds share every rule that governs a first draft (the never-invent
list, the evidence weighting, the house voice, the document outlines, the handoff between
them) and differ only in whether the review machinery gets loaded at all.

## Architecture

Four files, one always loaded and three loaded on demand, one of which now loads
conditionally rather than automatically.

`SKILL.md` carries the invariants, the evidence machinery, the writing rules, the accuracy
prohibitions, the document-set overview, the two-speed output modes and the delivery
rules. It is the part that applies to every job regardless of speed.

`references/readme-spec.md` and `references/description-spec.md` carry the section-by-
section specifications for the two output documents. Each ends with a handshake table
listing what it hands to the other, plus the positive and negative signals it collects for
the review loop. Both load for any job that touches the relevant document, at either
speed.

`references/quality-loop.md` carries the eight Kaizen stages, the eight-category rubric,
the adversarial checks and the final self-review gate, followed by the feedback-loop
notation. It loads for reviewed-speed jobs only. Draft speed never opens it.

## Data or control flow

Read `SKILL.md`. Establish intent, including which speed the job needs. Gather evidence.
Classify claims, in full at reviewed speed or straight to hedge words at draft speed.
Decide which documents are in scope and load the matching specification files. Draft. If
both documents exist, apply the separation test. At reviewed speed, load
`references/quality-loop.md` and run the loop; at draft speed, run the section 14 gate
directly against this file instead. Deliver.

The interesting part is still that the drafting stage isn't linear across the two
documents, at either speed. They are written as a pair, with material crossing in both
directions while the drafting happens. A design decision surfaced while explaining an
awkward setup step belongs in the description. An architectural constraint that forces a
manual step belongs back in the README as a setup line. The handshake tables exist so
that traffic is explicit rather than left to judgement, and that part of the mechanism is
identical whichever speed is running.

## Design decisions

**Absorbing `repo-doc-writer` as a speed rather than deleting it or keeping it separate.**
The two skills had drifted: the leaner one had picked up an explicit Oxford comma rule,
a number-spelling convention and an arrow-glyph ban that this file never got. Deleting it
would have thrown that away. Keeping both would have kept the manual-sync problem that
caused the drift in the first place. A mode inside one skill can't drift from itself.

**Draft speed skips the labels, not just the rubric.** It would have been simpler to keep
the VERIFIED/SUPPORTED/etc. classification at both speeds and only skip the scoring. It
doesn't skip the labelling too, because the labels exist purely to feed the rubric, and
carrying machinery for a rubric you're not going to load is exactly the kind of dead
weight draft speed was built to avoid.

**Splitting the specs out rather than keeping one file.** The original 1.1.0 was a single
905-line `SKILL.md`. Everything loaded every time, including the full README specification
on jobs that only wanted a description audit. Splitting costs an extra read when both
documents are in scope, and that's the trade. Progressive disclosure won.

**Handshake tables rather than a general instruction to cross-reference.** "Consider what
belongs in the other document" is the kind of instruction that gets nodded at and ignored.
A table of specific transfers is harder to skip.

**Keeping the writing rules in `SKILL.md`.** They apply to every job at both speeds
without exception, and a rule you always need shouldn't be behind a conditional load.

**A bounded loop rather than "iterate until good", at reviewed speed.** The stop decision
is the load-bearing part. Without it the skill would keep finding improvements, because
there are always improvements, and the marginal value of pass four is close to zero while
the cost is not.

**2% cynicism as a direction, not a target.** It isn't measurable and it drifts upward.
The alternative was banning it, which produces the flat institutional register that makes
documentation unreadable. Drift plus an explicit check, at both speeds now, beats
flatness.

## Trust and boundaries

The skill owns nothing at runtime. It's instructions. No filesystem access of its own, no
network calls, no credentials, no execution.

The boundary that matters is evidential. The skill consumes whatever material the user
supplies and it cannot verify anything beyond that material. It cannot run tests, execute
commands or confirm that a documented endpoint responds. Where the specifications say
"only claim passing tests when the result is supplied or actually observed", that's the
boundary being enforced by convention, because there's no mechanism available to enforce
it otherwise. This holds identically at both speeds.

Anything the skill writes about security in a target project describes boundaries. It does
not audit them.

## Current state

Working: all four files, the routing between them, the six output shapes across two
speeds, the evidence hierarchy, the Kaizen loop at reviewed speed, the rubric, the
draft-speed gate.

New in 3.0.0 and not yet exercised across many real projects: draft speed itself, and the
section 14 gate that stands in for the rubric when it's running. The gate was built by
trimming the existing checklist to binary pass/fail rather than independently designed, so
it inherits reviewed speed's judgement without reviewed speed's evidence that the
judgement holds up at scale.

Unknown: whether draft speed actually produces output indistinguishable from reviewed
speed on straightforward jobs, which was the entire premise for building it this way
rather than just always running the loop. That's an eval question, and there isn't an eval
set yet.

## Operational notes

No dependencies. No install step beyond placing the folder. Editing is plain markdown.

If you amend a reference file, check the section numbers referenced from `SKILL.md`
sections 8, 9, 10, 13 and 14, since those point at specific numbered sections inside the
references, and section 14 in particular now branches on speed.

## Limitations and awkward bits

`SKILL.md` is now just under 660 lines against a 500-line guideline, further over than
before the merge. The source-inspection checklist in section 4 is the obvious next thing
to move out, and it wasn't moved because the split was already three files deep and
over-fragmenting a skill has its own costs.

The rubric is scored internally and never printed unless an audit is requested, and the
draft-speed gate has the same property. That means there's no external record of either,
which makes it hard to tell after the fact whether a given output actually passed cleanly
or scraped through. Useful, hard to inspect.

The speed decision itself is a judgement call in section 10 ("when genuinely unsure, ask
once"), not a hard rule. That's deliberate, because a hard rule based on document
existence alone would send small internal tools and public-facing security tooling through
the same default path, which is the wrong call for at least one of them.

The feedback loop is written down but not persisted. Signals recorded during one run don't
survive into the next session. To actually close the loop you'd have to amend a reference
file, by hand, which is exactly what section 5.2 of the quality loop tells you to do and
exactly what nobody does at half past eleven on a Friday.

## Future direction

Planned, not implemented:

- an eval set comparing draft-speed and reviewed-speed output on the same fresh project,
  since the entire justification for draft speed's existence is an untested claim about
  what rubric-in-context does to a draft
- moving the source-inspection checklist to `references/evidence-gathering.md` if
  `SKILL.md` grows further
- a worked example pair, one README and one description for a small real project, as an
  `assets/` reference showing the separation test passing rather than describing it
