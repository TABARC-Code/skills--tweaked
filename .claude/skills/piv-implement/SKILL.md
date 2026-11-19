---
name: piv-implement
description: Executes an implementation plan task-by-task with validation at every step. Use when a completed feature plan exists and the user wants it built, says implement it, build the plan, or start coding from the plan, even if they don't name this skill. Validate after each task rather than once at the end. Dewey 005.1.
argument-hint: [path-to-plan]
---

# Execute: Implement from Plan

## Plan to Execute

Read plan file: `$ARGUMENTS`

## Before you start — work on a feature branch

A ticket gets built on its own branch, so it can become one PR. **Ideally you're already on that branch — cut it
before planning — so the plan commit you made is on it and rides into the PR; a plan committed on the base branch
won't be in this branch's PR.** If you're still on base, this step creates the branch now. Detect the base branch
(don't hardcode `main`): `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@'`
(fallback `main`).

- **On the base branch, clean** → create one: `git checkout -b feature/<plan-slug>`.
- **Already on a feature branch or in a worktree** → use it.
- **On the base branch with uncommitted changes** → STOP: commit or stash first.

(One branch per ticket is also what makes parallel worktrees clean later.)

## Execution Instructions

### 1. Read and Understand

- Read the ENTIRE plan carefully
- Understand all tasks and their dependencies
- Read the plan's **Open Questions / Assumptions** and its confidence score. If a question blocks a task and is unresolved, stop and ask before starting that task. A plan with a low confidence score gets a stated plan-risk note in the report.
- Note the validation commands to run
- Stay surgical: touch only what the plan names, and follow `karpathy-code-discipline` for scope, assumptions and success criteria
- Review the testing strategy

### 2. Execute Tasks in Order

For EACH task in "Step by Step Tasks":

#### a. Navigate to the task
- Identify the file and action required
- Read existing related files if modifying

#### b. Implement the task
- Follow the detailed specifications exactly
- Maintain consistency with existing code patterns
- Include proper type hints and documentation
- Add structured logging where appropriate

#### c. Verify as you go
- After each file change, check syntax
- Ensure imports are correct
- Verify types are properly defined
- **Run the task's own `VALIDATE` command before starting the next task.** Every task in the plan carries one.
  A task is not done until its check passes — if it fails, fix it now rather than carrying the failure forward.
  The full suite still runs at step 4; this is the per-task gate that keeps step 4 from becoming a pile-up.

### 3. Implement Testing Strategy

After completing implementation tasks:

- Create all test files specified in the plan
- Implement all test cases mentioned
- Follow the testing approach outlined
- Ensure tests cover edge cases

### 4. Run Validation Commands

Execute ALL validation commands from the plan in order:

```bash
# Run each command exactly as specified in plan
```

If any command fails:
- Fix the issue
- Re-run the command
- Continue only when it passes- **Retry cap:** the same check failing three times means stop and report the output and what you tried. Repeated failure usually means the plan is wrong, and more patching hides it. Never weaken or delete a test to get green. Set the report Status to PARTIAL if you stop.


### 5. Final Verification

Before completing:

- ✅ All tasks from plan completed
- ✅ All tests created and passing
- ✅ All validation commands pass
- ✅ Code follows project conventions
- ✅ Documentation added/updated as needed

## Output — write an implementation report

Write a short report to `.claude/reports/<plan-slug>-report.md` (and print the summary). This is what the PR body
and the `piv-review-pr` gate read — especially the **deviations** (a documented deviation is an *intentional*
decision the reviewer should not flag):

```markdown
# Implementation Report — <feature>

**Plan**: <path>   **Branch**: <feature/...>   **Status**: COMPLETE | PARTIAL

## Summary
{What was built, 2-4 sentences.}

## Tasks completed
- [task] → `path/to/file` (CREATE/UPDATE)

## Tests added
{Test files + cases + results.}

## Validation results
{Type-check / lint / tests / build — pass/fail with counts.}

## Deviations from the plan
{What changed vs the plan and WHY — or "none". This is the reviewer's signal of intent.}

## Issues encountered
{Anything notable, or "none".}
```

### Ready for the next step
- Confirm all changes are complete and validations pass.
- Next: `piv-commit` the work, then `piv-create-pr` to open the PR (the report fills the PR body), then `piv-review-pr`.

## Notes

- If you encounter issues not addressed in the plan, document them
- If you need to deviate from the plan, explain why
- If tests fail, fix implementation until they pass
- Don't skip validation steps

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-plan-implementation** · type: handoff · source: description
  - This skill (weight 2): Executes an implementation plan from piv-plan-implementation.
  - piv-plan-implementation: The implementation plan it writes is what piv-implement executes.
- **piv-commit** · type: handoff · source: body
  - This skill (weight 2): Hands finished work to piv-commit.
  - piv-commit: Commits what piv-implement left uncommitted.
- **piv-create-pr** · type: handoff · source: body
  - This skill (weight 2): Hands the committed branch to piv-create-pr.
  - piv-create-pr: Opens the pull request for a branch piv-implement produced.
- **piv-review-pr** · type: reference · source: body
  - This skill (weight 1): Named as the review step once the pull request exists.
  - piv-review-pr: Named as the review step for the pull request piv-implement opened.
- **piv-run-full-loop** · type: chain · source: body
  - This skill (weight 2): Runs as the implementation stage of piv-run-full-loop.
  - piv-run-full-loop: Runs implementation as the third stage of the chain.
- **system-evolution-review** · type: feedback · source: body
  - This skill (weight 2): Its divergences are what the evolution review classifies.
  - system-evolution-review: Recommends process changes for the implement step.
- **karpathy-code-discipline** · type: reference · source: body
  - This skill (weight 1): Follows it for scope, assumptions and success criteria.
  - karpathy-code-discipline: Governs the implementation step of the loop.
<!-- relationships:end -->
