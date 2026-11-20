---
name: piv-run-full-loop
description: Autonomously develops a complete feature from priming through planning, execution, and commit by chaining the four core PIV-loop skills. Use when you want a full hands-off feature build from a single description. Dewey 005.1.
argument-hint: [feature-description]
---

# End-to-End Feature Development

**Feature Description**: $ARGUMENTS

This skill chains the 4 core PIV-loop skills for autonomous feature development.

---

## Gates between steps

This chain runs without a human, so each step has to earn the next one. If a gate fails, stop, report the step that failed and why, and do not run later steps.

- Before Step 1: if you are on the base branch with a dirty tree, stop. Commit or stash first.
- After Step 2: read the plan's Open Questions and confidence score. Unresolved blocking questions, or a score below 7 out of 10, means stop and ask. Do not implement a guess.
- After Step 3: read the implementation report. Status must be COMPLETE and validation must pass. PARTIAL means stop.
- The final summary shows what actually happened. A step that did not run or did not pass is marked with a cross and a reason, never a tick.

---

## Step 1: Prime - Load Codebase Context

Execute the priming workflow to understand the codebase.

Run the `prime-codebase` skill (`.claude/skills/prime-codebase/SKILL.md`).

---

## Step 2: Planning - Create Implementation Plan

Create a detailed implementation plan for the feature.

Run the `piv-plan-implementation` skill (`.claude/skills/piv-plan-implementation/SKILL.md`) with the feature description: **$ARGUMENTS**.

**IMPORTANT**: Note the feature name (and plan file path) that the planning step creates. You'll need it for the next step.

---

## Step 3: Execute - Implement the Feature

Implement the feature from the plan document.

Run the `piv-implement` skill (`.claude/skills/piv-implement/SKILL.md`) with the plan file path: `.claude/plans/[feature-name].md`.

(Use the feature name from Step 2.)

---

## Step 4: Commit - Save Changes

Create a git commit for all changes.

Run the `piv-commit` skill (`.claude/skills/piv-commit/SKILL.md`).

---

## Final Summary

After completing all 4 steps, provide:

### Feature Implementation Complete

**Original Request**: $ARGUMENTS

**Feature Name**: [feature-name from planning step]

**Steps Executed:**
1. ✅ Prime - Codebase context loaded
2. ✅ Planning - Plan created at `.claude/plans/[feature-name].md`
3. ✅ Execute - Feature implemented and validated
4. ✅ Commit - Changes committed to git

**Outputs:**
- Plan document: `.claude/plans/[feature-name].md`
- Files created/modified: [list]
- Tests added: [list]
- Commit hash: [hash]

**Next Steps:**
- Push to remote: `git push`
- Create pull request (if applicable)
- Continue with next feature

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-plan-implementation** · type: chain · source: body
  - This skill (weight 2): Runs planning as the second stage of the chain.
  - piv-plan-implementation: Runs as the planning stage of piv-run-full-loop.
- **piv-implement** · type: chain · source: body
  - This skill (weight 2): Runs implementation as the third stage of the chain.
  - piv-implement: Runs as the implementation stage of piv-run-full-loop.
- **piv-commit** · type: chain · source: body
  - This skill (weight 2): Ends the chain with a commit.
  - piv-commit: Runs as the final commit stage of piv-run-full-loop.
- **prime-codebase** · type: chain · source: body
  - This skill (weight 2): Starts the chain by priming the codebase.
  - prime-codebase: Runs as the first stage of piv-run-full-loop.
- **router** · type: handoff · source: body
  - This skill (weight 2): Is the route for requests to run the build loop end to end.
  - router: Routes whole-loop requests to it.
<!-- relationships:end -->
