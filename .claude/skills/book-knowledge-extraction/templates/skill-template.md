# New Skill Template

Use this template for every skill produced by book-knowledge-extraction.
Do not leave fields blank without stating why.

---

```markdown
---
name: [skill-name]
version: "1.0.0"
description: >
  [One-paragraph description. Include what it does, when to trigger it,
  and specific user phrases. Make the description pushy enough to prevent
  undertriggering.]

provenance:
  source_title: ""
  source_author: ""
  extraction_date: ""
  extraction_confidence: "high | medium | low"

calls: []
called-by: []
---

# [Skill Name]

## Purpose

[Clear description of what the skill does. One to three sentences.]

## Scope

This skill handles:
- [item]
- [item]

This skill does not handle:
- [item]
- [item]

## Inputs

- [input type]
- [input type]

## Outputs

- [output type]
- [output type]

## Activation Conditions

Use this skill when:
- [condition]
- [condition]

## Operating Rules

1. [rule]
2. [rule]
3. [rule]

## Sub-Skills

| Sub-skill | Role | Parent relationship | Weight difference from parent |
|---|---|---|---|
| [name] | [role] | [required/supportive/optional/etc.] | [reason weight differs] |

## Relationship Contracts

[Insert structured contracts here using relationship-contracts.md schema.]

## Failure Modes

- [failure mode and repair]
- [failure mode and repair]

## Audit Checks

- [check]
- [check]

## Update Notes

- [Brief plain-language note on what was added or changed and why.]
```
