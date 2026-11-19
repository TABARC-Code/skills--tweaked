---
name: terse-commit
description: "Write ultra-compressed commit messages: Conventional Commits format, subject under 50 chars, body only when the \"why\" isn't obvious from the diff. Cuts noise while preserving intent and reasoning. Use when the user says \"write a commit\", \"commit message\", \"generate commit\", or invokes it directly. Pairs with terse-prose for full-session compression, or stands alone for artefact output only. Dewey 005.8."
metadata:
  author: TABARC-Code
  version: 1.2.0
  parent: occam
  status: production
---

# Terse Commit

Author: TABARC-Code

Write commit messages like a senior who has pushed ten thousand commits: exact type, exact scope, exact subject, nothing else unless the why is non-obvious.

## Rules

Conventional Commits format: `type(scope): subject`.

Types: feat, fix, refactor, chore, docs, test, perf, ci, style, revert.

Subject: under 50 chars, imperative mood, no capital, no period. "add login" not "Added login." and not "This commit adds a login feature to the application".

Body: include only when the why isn't readable from the diff. Two blank lines after subject. Explain the reason, not the mechanism (the diff already shows the mechanism).

Never: "WIP", "stuff", "changes", "update", "minor tweak", "various fixes". Each commit says one thing.

## Output

`type(scope): subject`

Body if needed (after blank line): why this change, not what it does.

## Examples

One-line:
```
fix(auth): use <= not < for token expiry check
```

With body (why isn't obvious):
```
refactor(cache): replace CacheManager with lru_cache

CacheManager was added anticipating per-user TTL, which never shipped.
lru_cache covers the actual use case (single maxsize). Removes 120 lines.
```

## Bidirectional links

**terse-prose** — runs the session; terse-commit handles the commit artefact only. When terse-prose is active, commit messages are already covered; invoke terse-commit explicitly only when writing commits outside a terse-prose session.

**lazy-review** — feeds terse-commit with what changed and why, so the body isn't guesswork. Run lazy-review on the diff first; use its output as the source for the commit body.

## Feedback loops

**Decay rule.** Every pass must retract something, not only add. No decay rate means every line ever grown is locked in.

**Positive:** reviewer reads the commit and understands the change without opening the diff. One sentence body, zero follow-up questions. Calibrated correctly.

**Negative:** reviewer opens the diff to understand why → the body was omitted when it shouldn't have been, or it described the mechanism (what) instead of the reason (why). Write the why next time.

**Negative:** commit message exceeds 50 chars on the subject → "one thing" wasn't enforced. Split the commit or tighten the subject.

## Boundary

Commit message only. Code review and PR description are lazy-review's territory.


## Version history

v1.3.0. Retraction pass: version log compressed (1 prior entries removed; an author's record carries no load in a user's runtime).

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-commit** · type: reference · source: body
  - This skill (weight 1): Supplies the message rules that piv-commit applies.
  - piv-commit: Follows its subject and body rules for the commit message.
- **lazy-review** · type: chain · source: body
  - This skill (weight 2): Takes what changed and why from lazy-review.
  - lazy-review: Its findings feed the commit body, so the why is not guesswork.
<!-- relationships:end -->
