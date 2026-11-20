---
name: lazy-review
description: "Code review focused only on over-engineering. Finds what to delete: reinvented standard library, unneeded dependencies, speculative abstractions, dead flexibility. One line per finding: location, what to cut, what replaces it. Use when the user says \"review for over-engineering\", \"what can we delete\", \"is this over-engineered\", \"simplify review\", or \"occam review\". Complements correctness review; this one only hunts complexity. Dewey 005.14."
metadata:
  author: TABARC-Code
  version: 1.2.0
  parent: occam
  status: production
---

# Lazy Review

Author: TABARC-Code

Review a diff for one thing only: what can be deleted. Not correctness, not style, not naming. Bloat.

## What to flag

- Reinvented stdlib: hand-rolled what a built-in already does.
- New dependency for what a few lines or an installed package covers.
- Speculative abstraction: interface with one implementation, factory for one product, config for a constant.
- Dead flexibility: parameters never varied, hooks never called, options never set.
- Scaffolding "for later" that later never used.
- `occam:` comments whose stated ceiling is visibly breached in the diff (e.g. a "single caller" shortcut now has three callers). Flag as: `path:line: occam: ceiling breached - [upgrade path from comment].`

## Output

One line per finding. Location, what to cut, what replaces it. No preamble, no praise sandwich, no severity essay.

Pattern: `path:line: cut [X], use [Y] instead.`

Example:
- `auth.py:42: cut hand-rolled base64, use base64.b64encode.`
- `cache.py: cut CacheManager class (one caller), use @lru_cache.`
- `config.py:88: cut RETRY_STRATEGY enum (one value ever set), inline it.`

## Bidirectional links

**terse-review** - complementary pass. terse-review covers correctness; lazy-review covers complexity. Neither owns the other's territory. Running both on a diff gives you a complete picture in two short passes.

**lazy-audit** - lazy-review operates on a diff; lazy-audit operates on a whole repo. If lazy-review finds a class of bloat (e.g. hand-rolled stdlib) appearing repeatedly, that's a signal to run lazy-audit and find every other instance. Feed the finding forward.

**lazy-build** - feeds back. When lazy-review flags something, the fix goes through lazy-build to ensure the replacement is itself the laziest option. Don't replace a complex thing with another complex thing.

## Feedback loops

**Decay rule.** Every pass must retract something, not only add. No decay rate means every line ever grown is locked in.

**Positive:** developer deletes the flagged code, ships, nothing breaks. The complexity wasn't hiding correctness. Ceiling estimated correctly.

**Negative:** a flagged deletion turns out to be load-bearing - it was handling an edge case the stdlib equivalent misses > the risk was underestimated. Note which class of stdlib substitution is risky in this codebase and flag it explicitly in future reviews.

**Negative:** "no over-engineering found" on a diff that had obvious bloat > a specific category was missed. Name it, watch for it.

## Boundary

Only complexity. If the code is wrong but minimal, that's a correctness review's job, not this one. Say "no over-engineering found" rather than inventing some to look thorough.


## Version history

v1.3.0. Retraction pass: version log compressed (1 prior entries removed; an author's record carries no load in a user's runtime).

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-review-changes** · type: chain · source: body
  - This skill (weight 2): Adds the complexity pass to a pre-commit review.
  - piv-review-changes: Runs it over the same diff for over-engineering.
- **terse-commit** · type: chain · source: body
  - This skill (weight 2): Its findings feed the commit body, so the why is not guesswork.
  - terse-commit: Takes what changed and why from lazy-review.
<!-- relationships:end -->
