---
name: quality-loop
description: The bounded Kaizen workflow, quality rubric, adversarial checks and final self-review. Read before any critique, audit or repair pass.
---

# Quality loop

Sequence: Kaizen stages (section 1) drive the work, the rubric (section 2) scores it, the
adversarial checks (section 3) attack it, and the self-review (section 4) is the gate
before anything is returned. Run them in that order. Do not score before drafting and do
not return before the gate.

Loading order note: if both documents are being produced, `references/readme-spec.md` and
`references/description-spec.md` should already be in context. The rubric's category D
cannot be judged otherwise.

---

# 1. Bounded Kaizen workflow

Use this workflow for creation, major rewrites and audits.

## Stage A - Intent kernel

State internally the user's actual outcome in one sentence.

Example:
> Produce trustworthy public documentation that a novice can follow without losing the
> programmer's voice.

Protect that outcome through every later stage.

## Stage B - Baseline

Identify the current documentation state:
- missing
- weak
- inaccurate
- incomplete
- duplicated
- overly promotional
- technically sound but hard to use

Do not assume a rewrite is necessary when a small repair would work.

## Stage C - Evidence map

Create an internal map of the important claims and their evidence status.

Prioritise claims that affect:
- installation
- permissions
- security
- destructive actions
- network exposure
- compatibility
- feature status

## Stage D - Draft or targeted repair

Make the smallest change that materially improves the outcome.

A complete rewrite is permitted when structure or trust is fundamentally broken.

## Stage E - Independent critique

Evaluate the result as though reviewing somebody else's draft.

The critique must identify concrete failures, not vague preferences.

Check:
- factual grounding
- missing setup steps
- contradictions
- implied but unsupported claims
- duplicated material
- template residue
- beginner traps
- false certainty
- security ambiguity
- monotonous cadence
- excessive wit or persona
- roadmap leakage into current features

The creator's preference is not a pass condition.

## Stage F - Targeted repair

Repair the failures found in Stage E.

Do not rewrite unaffected sections merely to make the pass feel substantial.

## Stage G - Regression check

Confirm that the repair did not:
- remove required information
- turn uncertainty into certainty
- change project intent
- introduce invented commands
- make beginner guidance less actionable
- duplicate the second document
- increase personality at the expense of clarity

## Stage H - Stop decision

Stop when all material failures are either:
- repaired
- explicitly UNKNOWN
- blocked by missing evidence

Do not continue polishing simply because another pass is possible.

Maximum default cycle:
- one draft/repair pass
- one independent critique
- one targeted repair
- one regression check

Perform a second cycle only if the first regression check exposes a material failure.

Never loop indefinitely.

---

---

# 2. Quality rubric

Score internally from 0–3.

## A. Factual grounding
0 - invented or contradicted claims
1 - major claims weakly grounded
2 - generally grounded with minor uncertainty problems
3 - material claims are properly evidenced or clearly qualified

## B. Setup usability
0 - cannot realistically follow it
1 - substantial missing steps
2 - workable for a technical reader
3 - novice can reach a recognisable successful result

## C. Status honesty
0 - roadmap and current features are mixed
1 - several ambiguous capability claims
2 - mostly clear
3 - implemented/experimental/planned/unknown are consistently distinct

## D. Document separation
0 - README and description substantially duplicate
1 - heavy duplication
2 - some overlap but different jobs
3 - each document has a clear purpose

## E. Programmer voice
0 - generic marketing/AI prose
1 - occasional perspective but mostly generic
2 - credible maintainer voice
3 - specific, grounded perspective without invented autobiography

## F. Human cadence
0 - visibly templated/monotone
1 - frequent rhythmic repetition
2 - mostly natural
3 - varied without becoming performative

## G. Security clarity
0 - dangerous ambiguity or false guarantees
1 - relevant boundaries mostly omitted
2 - adequate
3 - clear permissions, secrets, exposure and destructive scope

## H. Concision
0 - bloated or repetitive
1 - substantial unnecessary material
2 - mostly efficient
3 - every major section earns its place

Target:
- no category below 2
- A, B and C should reach 3 for documentation that will be published as authoritative
- if evidence prevents a 3, preserve the uncertainty rather than inventing a fix

Do not print the score unless the user asks for an audit or evaluation.

---

---

# 3. Adversarial checks

Before publication-quality output, ask internally:

- What would mislead a novice here?
- Which sentence sounds factual but is actually inferred?
- Could a planned feature be mistaken for a current one?
- Is any command syntactically plausible but unverified?
- Have I implied tests pass merely because tests exist?
- Have I claimed safety without describing the threat boundary?
- Does the README tell the user how to recognise success?
- Is the programmer voice based on evidence, or am I role-playing a fictional biography?
- Did the 2% cynicism become 12% because one line amused me?
- Could I delete 10% without losing useful information?

Act on concrete failures.

---

---

# 4. Final self-review

Before returning the result, verify:

- UK English is consistent.
- Material claims have evidence or qualification.
- No capabilities were invented.
- No release history was fabricated.
- Planned work is labelled.
- Setup commands are known rather than guessed.
- A beginner can recognise a successful first run where evidence permits.
- Security language describes boundaries rather than promising perfection.
- Paragraph and sentence rhythm is varied.
- The programmer voice is grounded and not fictional autobiography.
- Cynicism is incidental.
- README and description perform different jobs.
- No section exists merely because templates traditionally include it.
- Weak sections identified by the critique were repaired.
- The final regression check passes or remaining uncertainty is visible.

Return the useful artefact, not the internal reasoning.

---

# 5. Feedback loops

This skill is not a fixed procedure. It is a loop that is supposed to get better on each
run, and the loop only works if both kinds of signal are actually recorded.

## 5.1 Positive reinforcement

When a pass produces something that clearly works, note what caused it so the next pass
reaches for it earlier:

- a claim that was traced back to a manifest, route or command rather than a name
- a beginner step that named the physical action and the failure mode in the same breath
- a section that was deleted and not missed
- an aside that landed once and was not repeated
- a boundary between the two documents that held without effort

These become defaults, not one-off wins.

## 5.2 Negative correction

When a pass produces a failure, record the class of failure rather than the instance:

- inference presented as observation
- roadmap material drifting into current features
- cadence flattening into template rhythm
- cynicism climbing above its budget
- duplication reappearing between README and description
- setup guidance that stops at "run the command"

A repeated class of failure is a signal that the specification needs amending, not that
the draft needs another polish. Amend the reference file, not just the output.

## 5.3 Loop discipline

Positive signals raise the floor. Negative signals lower the ceiling. Both are bounded by
the stop decision in section 1, stage H. An improvement loop that never terminates is
just an expensive way of rewriting the same paragraph, which is the failure mode this
whole section exists to prevent.
