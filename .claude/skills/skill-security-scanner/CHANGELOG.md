# Changelog

## [1.0.0] — 2026-08-05

### Added
- Full rule set ported from book-to-skill's `scan_generated_skill.py` (virgiliojr94): seven injection rules (INJECT-001 through INJECT-007), one Unicode rule (UNICODE-001), one exfiltration rule (EXFIL-001) with compound AND condition, two frontmatter authority rules (AUTH-001, AUTH-002)
- Abort condition protocol: symlink detection at directory, SKILL.md, and file level; size limits (2MB per file, 20MB total, 1,000 file cap); UTF-8 validation
- Advisory findings model with two-tier severity guidance (high-priority-for-review vs context-dependent)
- Structured findings report format with rule IDs and line numbers
- Composition interface: callable from source-ingestion-forge phase 10.5 and skill-audit-repair
- Standalone use case: vetting externally sourced or downloaded skills before installation
- 8 evals covering positive trigger, negative trigger, rule-specific faithfulness, two edge cases, shallow-reading trap, out-of-scope boundary, external-source trigger
- Bidirectional links to source-ingestion-forge and skill-audit-repair

### Design rationale
Extracted from source-ingestion-forge audit-and-repair subskill as a standalone skill. Security scanning is a different discipline from quality auditing — different failure modes, different severity model, different expertise. Separation allows standalone use for vetting any skill, not just forge-generated ones.
