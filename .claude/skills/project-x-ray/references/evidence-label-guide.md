# Evidence Label Guide

How to classify and label claims in Project X-Ray reports.
Consistent labelling is what separates a useful report from a plausible-sounding lie.

---

## The Four Labels

### Observed

Directly readable in the provided files. You have seen it with your own inspection.

Use when:
- You have read the actual file and can cite line number or content
- The folder structure itself proves something (a `migrations/` folder exists - Observed)
- A dependency file explicitly lists a package
- A config file contains the setting you are describing
- An import statement names a module you are claiming is used

Examples:
- "Uses PostgreSQL - Observed: `psycopg2==2.9.6` in requirements.txt"
- "JWT authentication - Observed: `PyJWT` in requirements.txt; `jwt.decode()` in auth.py:47"
- "No test suite - Observed: no test directory, no test files, no testing framework in dependencies"

### Inferred

Logically likely from structure, naming convention, framework convention, or partial evidence.
You have not confirmed it by reading the actual logic path.

Use when:
- A folder exists that suggests something but you have not read its contents
- Framework convention implies something (a Django `apps/` structure implies certain routing patterns)
- A dependency is listed but you cannot confirm it is actually called
- A file name suggests a function but the file was not read
- Pattern-matching on naming: `tasks.py` probably contains tasks; not confirmed

Examples:
- "Likely uses Celery - Inferred: `celery` in requirements.txt and a `tasks/` folder present; actual task registration not read"
- "API appears RESTful - Inferred: route naming in routes.py follows REST conventions; handler logic not verified"

**Critical distinction:** Inferred is not a weaker Observed. It is a categorically different
epistemic state. Do not upgrade an Inferred to Observed because you are confident. Confidence
does not change the category - it changes the confidence rating within it.

### Unknown

Cannot be determined from the submitted material.

Use when:
- Something is referenced in code but the referenced file was not submitted
- A feature is implied by comments or README but no implementation is visible
- Configuration is expected (a database connection) but no config file was provided
- The question cannot be answered without running the code or seeing missing files

Examples:
- "Whether rate limiting is applied - Unknown: no middleware config visible in submitted files"
- "Database connection pooling settings - Unknown: .env not submitted"
- "Whether the tests pass - Unknown: test framework identified but tests not run"

Unknown is not a failure state. It is an honest statement of the report's boundary.

### Broken or incomplete

Visible evidence of non-function, incompleteness, or active inconsistency.

Use when:
- A function body is empty, contains only `pass`, or raises `NotImplementedError`
- A route is registered but points to a handler that does not exist in the files provided
- An import references a module that does not exist in the submission
- A migration references a table not present in the schema
- A config references an environment variable not documented in any env sample
- Two conflicting implementations of the same thing exist in the same file
- Code is visibly mid-refactor: old and new patterns mixed without clear intent

Examples:
- "`send_invoice()` - Broken or incomplete: defined in billing.py:112 with body `pass`"
- "`/admin/reports` route - Broken or incomplete: registered in routes.py:88; handler `generate_reports` not found in any submitted file"
- "Auth module - Broken or incomplete: two implementations (`auth_v1.py` and `auth.py`) both imported in different parts of the codebase"

---

## Confidence Levels

Combine with the label. Both pieces of information are needed.

| Level | Meaning |
|---|---|
| High | Multiple converging pieces of evidence. Would be surprised to be wrong. |
| Medium | One solid piece of evidence, or two weak ones. Could be wrong if context is outside the submission. |
| Low | Naming pattern or structural convention only. A hypothesis, not an assertion. |

Unknown does not receive a confidence rating - you have nothing to measure confidence against.

---

## Label + Confidence Combinations

| Combination | What it means | Example use |
|---|---|---|
| Observed, High | Read it, it is there, evidence is unambiguous | Package dependency, explicit config value |
| Observed, Medium | Read it, but the meaning requires interpretation | File exists but purpose inferred from name |
| Inferred, Medium | Reasonable structural deduction, not confirmed | Framework convention implies routing pattern |
| Inferred, Low | Naming guess - be explicit that this is a hypothesis | Folder called `workers/` might contain workers |
| Unknown, - | No basis for any rating | File not submitted, env var not documented |
| Broken or incomplete, High | Clearly non-functional, evidence is direct | `pass` body, missing handler, broken import |
| Broken or incomplete, Medium | Looks broken, but might be intentional or in progress | `TODO` in active path, partial refactor |

---

## Anti-Patterns

**Upgrading inferences.** If you have not read the file, it is not Observed. "I'm confident it
works like that" is not a basis for Observed. Observed means you have seen it.

**Using Unknown to avoid commitment.** Unknown means you genuinely have nothing.
If you have something weak, it is Low-confidence Inferred. The distinction matters - 
Unknown says "I have no basis"; Low Inferred says "I have a weak basis."

**Hiding gaps.** A clearly stated gap is more useful than a confident assertion that papers over it.
If something important is missing from the submission, say so.

**Using Broken or incomplete pejoratively.** A placeholder in a work-in-progress is a documented
state, not a moral failing. Label accurately. If the code is genuinely poor, the evidence will
make that plain without editorialising. (You are still allowed to be blunt when the evidence
supports it.)

**Making claims without file paths.** Every Observed claim must trace to a file. Every Inferred
claim must name the convention or structural basis. No floating assertions.

---

## Quick Reference Card

```
OBSERVED   = I have read it in the files. [cite file:line]
INFERRED   = I am deducing it from [structure / naming / convention]. [name the basis]
UNKNOWN    = The files needed to answer this were not submitted. [name what is missing]
BROKEN     = There is visible evidence of non-function. [cite file:line + what is broken]

High   = Multiple converging evidence sources
Medium = One solid source, or two weak ones
Low    = Naming or structural pattern only

DO NOT:
- Upgrade Inferred to Observed
- Use Unknown instead of Low-confidence Inferred
- Make claims without citing a file
- Hide gaps
```

---

## Bidirectional Position

This file is loaded during PHASE 2 Lens 1 (structural claims) and Lens 2 (semantic signal classification) of Project X-Ray. It is also relevant during Lens 4 when classifying information about actors and incentives.

It is also relevant to `source-bound-skill-forge`, which uses a compatible but distinct
evidence confidence system. If generating a skill from a codebase, both systems apply:
X-Ray's labels describe the code; the Forge's confidence scoring describes how reliably
the code supports a doctrine claim.
