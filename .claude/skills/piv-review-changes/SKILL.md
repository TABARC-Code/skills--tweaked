---
name: piv-review-changes
description: Performs a technical code review of recently changed files for bugs, security issues, and standards compliance, then writes a report. Use before committing as a pre-commit quality gate, and whenever the user asks for a review, a second look at their diff, or says review my changes, even if they don't name this skill. Dewey 005.14.
---

# Code Review

Perform technical code review on recently changed files.

## Core Principles

Review Philosophy:

- Simplicity is the ultimate sophistication - every line should justify its existence
- Code is read far more often than it's written - optimize for readability
- The best code is often the code you don't write
- Elegance emerges from clarity of intent and economy of expression

## What to Review

Start by gathering codebase context to understand the codebase standards and patterns.

Start by examining:

- CLAUDE.md
- README.md
- Key files in the core module
- Documented standards in the docs directory (and any `.claude/references/` docs)

After you have a good understanding, run these commands:

```bash
git status
git diff HEAD
git diff --stat HEAD
```

Then check the list of new files:

```bash
git ls-files --others --exclude-standard
```

Read each new file in its entirety. Read each changed file in its entirety (not just the diff) to understand full context.

For each changed file or new file, analyze for:

1. **Logic Errors**
   - Off-by-one errors
   - Incorrect conditionals
   - Missing error handling
   - Race conditions

2. **Security Issues**
   - SQL injection vulnerabilities
   - XSS vulnerabilities
   - Insecure data handling
   - Exposed secrets or API keys

3. **Performance Problems**
   - N+1 queries
   - Inefficient algorithms
   - Memory leaks
   - Unnecessary computations

4. **Code Quality**
   - Violations of DRY principle
   - Overly complex functions
   - Poor naming
   - Missing type hints/annotations

5. **Adherence to Codebase Standards and Existing Patterns**
   - Adherence to standards documented in the docs directory
   - Linting, typing, and formatting standards
   - Logging standards
   - Testing standards

## Over-engineering pass
Run `lazy-review` over the same diff: it hunts reinvented standard library, needless dependencies and speculative abstractions, which this review otherwise skips.

## Verify Issues Are Real

- Run specific tests for issues found
- Confirm type errors are legitimate
- Validate security concerns with context

## Output Format

Save a new file to `.claude/code-reviews/[appropriate-name].md`

**Stats:**

- Files Modified: 0
- Files Added: 0
- Files Deleted: 0
- New lines: 0
- Deleted lines: 0

**For each issue found:**

```
severity: critical|high|medium|low
file: path/to/file.py
line: 42
issue: [one-line description]
detail: [explanation of why this is a problem]
suggestion: [how to fix it]
```

If no issues found: "Code review passed. No technical issues detected."

Critical or high findings block the commit. Hand the file to `piv-fix-review-findings` to triage and fix; its fields (severity, file, line, issue) are the ones above.

## Important

- Be specific (line numbers, not vague complaints)
- Focus on real bugs, not style
- Suggest fixes, don't just complain
- Flag security issues as CRITICAL

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-commit** · type: gate · source: description
  - This skill (weight 2): Runs before a commit as the pre-commit quality gate.
  - piv-commit: Expects the pre-commit review to have run first.
- **rules-check-drift** · type: reference · source: body
  - This skill (weight 1): Can be extended with the rules-drift check.
  - rules-check-drift: Can be folded into the code-review pass.
- **lazy-review** · type: chain · source: body
  - This skill (weight 2): Runs it over the same diff for over-engineering.
  - lazy-review: Adds the complexity pass to a pre-commit review.
<!-- relationships:end -->
