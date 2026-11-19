# Kaizen log

One entry per pass. Each lists the defect, the fix, and how it was checked. Checks here are structural (`network/check_skills.py`) or by reading. Nothing below was proven by running a model against a test case, and the entries say so.

## Pass 1: skills that read outside content

| Skill | Defect found | Fix | Check |
|---|---|---|---|
| piv-implement-issue | Investigate can end with Low confidence and "flag for a human before any fix", but implement never read that field, so a guessed root cause could be built on. | New step 1b stops on Low confidence or an undetermined cause. | check_skills.py asserts the gate exists. Not run end to end. |
| piv-implement-issue | Validation loop had no exit: "don't proceed until all pass". Invites weakening tests. | Three-attempt retry cap, and never weaken or delete a test to get green. | Read only. |
| piv-implement-issue | `allowed-tools` lacked git and gh although the body branches and uses gh. | Added `Bash(git:*)` and `Bash(gh:*)`. | Read only. |
| piv-review-pr | `gh pr checkout` run with no dirty-tree check. | Check `git status --porcelain` first, prefer a throwaway worktree. | Read only. |
| piv-review-pr | Validation executes the PR's own code, which for a fork is untrusted. | Note: inspect scripts and CI changes first, sandbox or skip, and record a skip as a limitation. | Read only. |
| plan-create-stories | Creation not re-runnable. A failure at ticket 17 of 30 leaves duplicates on retry. | Manifest of created keys, title search before create, resume. | Read only. |
| piv-slice-epic | Tickets created with no confirmation step and no graph validation. | Step 4b: cycle and dangling-dependency check, show the list, wait for go-ahead. | Read only. |
| prime-codebase | Assumed `tree` exists, and read the whole file list on huge repos. | Fallback command and a depth cap. | Read only. |
| deep-research | Data guard sat in the coordinator, but the subagents do the web reading and never saw it. | Rule added to `references/researcher.md`. | check_skills.py asserts it. |

## Self-exemption sweep

The previous pass added a Low-confidence path to piv-investigate-issue without checking its consumer. That is the defect above in piv-implement-issue, caused by my own earlier change. Lesson: when a producer gains a new output state, search for every consumer in the same pass.

## Not done

- piv-plan-implementation, plan-architecture, prime-backend, prime-frontend and agent-browser were read for guard coverage only, not audited line by line.
- No skill was run against a test prompt, so there are no eval results or pass rates.
- The remaining 37 skills have not had a Kaizen pass.
