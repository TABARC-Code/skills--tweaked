# Risk Audit Checklist

Full checklist for Section 10 of Project X-Ray.
Run all categories. Report every finding. Do not skip categories - write "No findings"
and note whether absence is reassuring or simply a result of limited evidence.

---

## Severity Scale

| Level | Definition | Action |
|---|---|---|
| Critical | Data loss, credential exposure, or system compromise possible. | Flag at top of Section 10 before the table. |
| High | Likely to cause failures, bugs, or security problems under normal use. | List prominently. |
| Medium | May cause problems under load, edge cases, or future changes. | List with context. |
| Low | Poor practice or technical debt - not immediately dangerous. | List; do not inflate. |

**Rule:** If a Critical finding exists, call it out at the very top of Section 10 as a
standalone warning before the table begins. Do not bury it.

---

## Category 1: Secrets and Credential Exposure

- [ ] API keys, tokens, or passwords hardcoded as string literals in source files
- [ ] `.env` file committed to version control (check .gitignore - is it listed?)
- [ ] Database credentials visible in config files or source code
- [ ] Secret keys as literals in settings (Django SECRET_KEY, Flask secret, JWT secret)
- [ ] Private keys or certificates committed to the repo
- [ ] OAuth client secrets in code or committed config
- [ ] Third-party service credentials (Stripe, SendGrid, Twilio, AWS) in source

Default severity: Critical for all items in this category.

---

## Category 2: Authentication and Authorisation

- [ ] Routes that appear to require authentication have no visible auth middleware
- [ ] Authentication present but no authorisation - authenticated users can access anything
- [ ] Session tokens not invalidated on logout (if session code is present)
- [ ] Weak or absent CSRF protection on state-changing endpoints
- [ ] Password reset flow present but not time-limited or single-use
- [ ] Admin routes with no separate permission check beyond general authentication
- [ ] API endpoints returning user data without verifying the requesting user owns it
- [ ] JWT secret weak, absent, or algorithm not validated (alg: none vulnerability)

---

## Category 3: Input Handling and Injection

- [ ] SQL queries built by string concatenation with user input
- [ ] User input passed to `eval()`, `exec()`, `subprocess`, `shell=True`, or `os.system()`
- [ ] File paths constructed from user input without sanitisation
- [ ] HTML rendered from user input without escaping (XSS)
- [ ] File upload handling without MIME type, extension, or size validation
- [ ] Redirect targets built from user-supplied URL parameters (open redirect)
- [ ] Deserialisation of user-supplied data without type checking (pickle, YAML load, etc.)
- [ ] XML parsing without disabling external entity resolution (XXE)

---

## Category 4: Data Integrity

- [ ] Multi-step database writes with no transaction wrapping (partial write risk)
- [ ] No foreign key constraints in schema where they logically should exist
- [ ] Fields nullable where logic implies they should always have a value
- [ ] Soft delete pattern (`deleted_at`) without corresponding WHERE filters in queries
- [ ] No input validation before database writes
- [ ] Concurrent write paths with no locking or optimistic concurrency control
- [ ] Background job failure with no rollback or compensating transaction
- [ ] Data migration with no rollback path

---

## Category 5: Error Handling

- [ ] Bare `except:` or `except Exception:` catching all exceptions silently
- [ ] Exceptions caught and discarded without logging
- [ ] No global error handler or last-resort fallback
- [ ] HTTP errors returned as 200 OK with error message in body
- [ ] Stack traces or internal error details exposed to end users in production
- [ ] Unhandled promise rejections in JavaScript (`.catch()` absent)
- [ ] No retry logic on operations that fail transiently (network, external API calls)
- [ ] Background job failure with no alert, log, or dead letter queue

---

## Category 6: Configuration and Environment

- [ ] No environment separation visible (dev / staging / production configs)
- [ ] Required environment variables not documented anywhere
- [ ] Debug mode enabled in an apparent production configuration
- [ ] Open CORS policy (`Allow-Origin: *`) in apparent production config
- [ ] HTTPS not enforced or not configured
- [ ] Sensitive config values with hardcoded defaults that are production-unsafe
- [ ] Feature flags or kill switches absent for risky new features

---

## Category 7: Dependencies

- [ ] No lockfile present (requirements.txt without .lock, package.json without package-lock or yarn.lock)
- [ ] Very old dependency versions - over two years without update
- [ ] Dependencies pinned to git branches or commit hashes rather than releases
- [ ] Unused packages in dependency file (bloat and attack surface)
- [ ] Known-vulnerable package versions (note if recognisably old; do not claim CVE knowledge)
- [ ] No dependency update tooling visible (Dependabot, Renovate, similar)
- [ ] Transitive dependencies with no lockfile (cannot audit what is actually installed)

---

## Category 8: Deployment and Infrastructure

- [ ] Docker image built FROM latest rather than a pinned version
- [ ] No health check endpoint
- [ ] No graceful shutdown handling
- [ ] Secrets passed as environment variables to containers with no secrets management
- [ ] Build process undocumented or only partially recoverable from source
- [ ] Deployment instructions absent or out of date
- [ ] No rollback procedure documented or apparent
- [ ] Database migrations run automatically on startup with no safety gate

---

## Category 9: Code Quality Risks

- [ ] Dead code - functions or files defined but never referenced
- [ ] Commented-out logic blocks in active files (disabled code left in production paths)
- [ ] TODO or FIXME comments in critical execution paths
- [ ] Functions over ~200 lines with no clear decomposition
- [ ] Deeply nested conditionals (more than four levels) increasing error-path complexity
- [ ] Magic numbers or magic strings without named constants
- [ ] Circular imports
- [ ] Two conflicting implementations of the same responsibility

---

## Category 10: Testing Gaps

- [ ] No test suite present
- [ ] Tests exist but cover only trivial paths, not critical logic
- [ ] Tests rely on specific environment state and are not reproducible
- [ ] No integration or end-to-end tests for API endpoints
- [ ] No tests for error handling or failure paths
- [ ] Test suite has not been run recently (last modified dates suggest drift)
- [ ] CI pipeline present but not running tests (or test step disabled)

---

## Category 11: Performance

- [ ] N+1 query pattern: database call inside a loop, especially in list endpoints
- [ ] No pagination on endpoints returning potentially large datasets
- [ ] Missing indexes on fields used in WHERE, JOIN, or ORDER BY clauses
- [ ] Large file or data operations done synchronously in request handlers
- [ ] No caching on expensive repeated computations or queries
- [ ] Background job queue with no concurrency limit or rate limit
- [ ] In-memory data structures that grow without bound

---

## Category 12: Privacy

- [ ] PII stored without encryption at rest
- [ ] PII logged in plain text (names, emails, IDs in log statements)
- [ ] User data returned in API responses without field-level filtering
- [ ] No data retention policy apparent (data accumulates indefinitely)
- [ ] Third-party analytics or tracking present without consent mechanism
- [ ] User passwords or tokens stored in reversible form

---


---

## Non-Code Project Risk Categories

Apply these for any project type that is not primarily software. Adapt severity to context.

---

### Category 13: Creative and Brand Risks

- [ ] No approved brief - work has proceeded without a documented starting point
- [ ] Client sign-off not documented for any stage
- [ ] Multiple "final" versions with no clear current one
- [ ] Source files absent - only exports provided, originals missing or not shared
- [ ] No version control or naming convention for assets
- [ ] Brand guidelines contradicted by delivered assets
- [ ] Assets in formats incompatible with stated delivery requirements
- [ ] Rights or licensing not documented for third-party assets (photography, fonts, music)
- [ ] No clear ownership of master files

---

### Category 14: Marketing and Campaign Risks

- [ ] Campaign objective not stated or measurable
- [ ] Audience not defined - no persona, no segmentation, no stated target
- [ ] Brief references research or insight not present in the files
- [ ] Campaign plan and creative brief appear to be for different campaigns
- [ ] No measurement or tracking plan
- [ ] Budget not signed off or no budget present where expected
- [ ] Channel plan references platforms or vendors not confirmed
- [ ] No approval chain documented for live content
- [ ] Compliance or legal review absent where regulatory environment requires it
- [ ] Timeline has passed with no evidence of delivery or extension

---

### Category 15: Strategy and Business Document Risks

- [ ] Recommendation present but options analysis absent - was there actually a choice?
- [ ] Financial model present but assumptions not documented
- [ ] Roadmap with no resourcing or named ownership
- [ ] Success metrics not defined or not measurable
- [ ] Decision recorded but rationale absent - reasoning lost or sensitive
- [ ] Strategy document last updated when circumstances have visibly changed
- [ ] Stakeholder alignment not documented - who has seen and approved this?
- [ ] Dependencies on external factors not acknowledged
- [ ] Conflicting strategies or plans both apparently current

---

### Category 16: Research and Evidence Risks

- [ ] Research question not stated
- [ ] Methodology not documented - findings cannot be evaluated or replicated
- [ ] Raw data absent - only summary or processed data provided
- [ ] Sample size or data quality not stated
- [ ] Findings and interpretations not clearly distinguished
- [ ] Claims not attributed to sources
- [ ] Analysis appears to support a predetermined conclusion - check for framing capture
- [ ] Ethics documentation absent where expected
- [ ] Data contains PII with no anonymisation or consent documentation

---

### Category 17: Editorial and Content Risks

- [ ] No editorial brief - why was this written, for whom, in what context?
- [ ] Facts asserted without visible sourcing
- [ ] Multiple draft versions with no clear current one
- [ ] Legal or compliance review absent for regulated topics
- [ ] Rights not cleared for quoted material, images, or data
- [ ] No stated publication target or audience
- [ ] Content appears repurposed from another project without adaptation
- [ ] Author or contributor unclear

---

### Category 18: Governance and Process Risks (Any Project Type)

- [ ] No named owner for the project or for critical deliverables within it
- [ ] Approval process not documented
- [ ] Decision log absent - decisions traceable only through file naming history
- [ ] Key person dependency - critical knowledge held by one person, not documented
- [ ] Handover documentation absent for a project clearly being handed over
- [ ] No stated status - is this live, in progress, on hold, or abandoned?
- [ ] Contacts or responsible parties not identified
- [ ] Conflicting documents both apparently current with no deprecation notice
- [ ] Archive and current files mixed without clear separation

## Output Format

For each finding, record in the Section 10 table:

| Risk | Severity | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|

For the Suggested fix column: indicate direction only. Do not write implementation.
"Parameterise the query" not a full code rewrite. "Move to environment variable" not a diff.

**Calibration rule:** If a project has no Critical or High findings, say so plainly.
An empty risk category is useful information - provided you note whether it is genuinely
clean or simply unverifiable from the submitted files.

---

## Cross-reference

Risk findings feed into:
- Section 13 (Final Verdict) - "What needs fixing first"
- Section 12 (README/Handover Summary) - "Known Limitations"
- PHASE 4 / Section 14 - if risks involve people, teams, or organisational failure modes;
  these should already have been caught by Lens 4, but if Section 10 surfaces new signals,
  note them as a Lens 4 calibration gap

Security signals detected during PHASE 1 (from `references/framework-fingerprints.md`)
should appear in the PHASE 1 intake declaration as immediate red flags, then again here
in the risk table. Do not wait for Section 10 to surface a Critical finding visible at intake.
