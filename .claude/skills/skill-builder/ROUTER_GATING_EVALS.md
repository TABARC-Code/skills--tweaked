# Router Gating Evals

**Author:** TABARC-Code
**Purpose:** Verify that the six sub-skills stay gated behind `skill-builder` and never trigger standalone. This is a qualitative eval set — read and judge the transcript, there is no automated runner for this file. Bundled `skill-creator/evals/evals.json` tests skill-creator's own drafting/audit behaviour; this file tests the router boundary that the sub-skill split depends on.

## Why this exists

The sub-skills used to ship as standalone `SKILL.md` files with their own trigger descriptions, which let them fire independently of the router — the exact failure this rename/restructure fixed. Nothing previously verified that the fix actually holds. This does.

## Test 1 — Direct sub-skill language, no router mention

**Prompt:** "Brainstorm some rough ideas for a skill that summarises legal contracts."

**Expected:** Claude should route through `skill-builder`'s default workflow (Creative Exploration Engine first), not answer as if a standalone "creative exploration" skill triggered directly. The response should reflect `skill-builder`'s Operating Rule (creative output doesn't self-certify) rather than jumping straight to a finished draft.

**Fails if:** the response shows no trace of the router's gating language, or treats creative output as final/certified without a handoff step.

## Test 2 — Sub-skill name spoken aloud

**Prompt:** "Use the structured skill engineering system to audit my SKILL.md for contradictions."

**Expected:** Claude should still enter through `skill-builder`, apply the Change-Control Procedure (define change boundary, classify affected components) before editing anything, and only then defer to the structured-engineering sub-skill's audit logic.

**Fails if:** Claude skips straight to editing without stating a change boundary first, or acts as though `structured-skill-engineering-system` is an independently installed skill with no relationship back to the router.

## Test 3 — Skill-creator name collision check

**Prompt:** "Help me create a new skill from scratch."

**Expected:** Claude should use `skill-builder`'s bundled `skill-creator/SUBSKILL.md`, reachable only through the router, and should not confuse it with any other, unrelated skill-creator that might also be installed.

**Fails if:** behaviour is ambiguous about which skill-creator is running, or the response can't be traced back to `skill-builder`'s routing.

## Recording results

Log outcomes in `NOTES.md` under the relevant version entry — pass/fail per test, plus the version number this was run against, so drift is visible over time.
