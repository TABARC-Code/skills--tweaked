# Extraction Layers Reference

Eight-layer protocol for full-depth source extraction.

---

## Layer 1 - Bibliographic and Context Capture

Record:
- title
- author
- publication date
- source type
- genre or discipline
- intended audience
- historical or cultural context (where relevant)
- reason the source matters to the skill system
- extraction priority: `high | medium | low | deferred`
- confidence level: `high | medium | low | uncertain`

---

## Layer 2 - Structural Map

Extract the visible architecture:
- table of contents
- chapters, sections, recurring headings
- sequence of ideas
- narrative or argumentative progression
- structural turning points (where the argument pivots or the method changes)

This layer answers: *How is the source built?*

---

## Layer 3 - Concept Map

Extract the conceptual machinery:
- key terms with definitions
- repeated concepts
- contrasts and binaries
- hierarchies and categories
- models and taxonomies
- principles

Mark each concept: `well-supported | asserted | contested | implied`.

This layer answers: *What are the building blocks of meaning?*

---

## Layer 4 - Argument and Claim Map

Extract:
- central thesis
- supporting claims with evidence
- subsidiary claims
- assumptions (stated or unstated)
- implied claims
- counterarguments the source engages or ignores
- unresolved tensions

This layer answers: *What is the source trying to prove, show, teach, or change?*

---

## Layer 5 - Procedure and Method Extraction

Extract anything that can become an action:
- step-by-step methods
- decision trees
- diagnostic checks
- craft processes and writing techniques
- design methods
- repeatable habits
- heuristics

Label each: `reusable | conditional | context-specific | deprecated | speculative`.
Assign confidence: `high | medium | low`.

This layer answers: *What can someone do because of this source?*

---

## Layer 6 - Skill Conversion

Convert extracted knowledge into:
- parent skills
- sub-skills with independent functions
- micro-skills
- operating principles
- reusable prompts
- templates
- checklists
- failure modes
- audit tests

Sub-skill relationship types to assign:
- `inherited` - carries parent logic downward
- `required` - parent cannot function without it
- `optional` - parent can function without it but improves with it
- `specialised` - handles a narrower case
- `conditional` - activates only under defined conditions
- `supportive` - improves parent but does not control it
- `overriding` - can alter normal parent behaviour in specific cases
- `downstream` - receives parent output
- `upstream` - prepares input for the parent

This layer answers: *What should the system now be able to perform?*

---

## Layer 7 - Relationship Mapping

Map every meaningful relationship between extracted and existing skills:
- dependencies
- influences
- prerequisites
- overlaps
- conflicts (flag, do not suppress)
- reinforcements
- specialisations
- inheritance links
- chain relationships
- reverse links
- contextual links

Read `relationship-contracts.md` for full contract schema.

This layer answers: *How does this knowledge alter the wider skill system?*

---

## Layer 8 - Compression Without Loss

After extraction, compress without flattening the intelligence.

Preserve:
- the source's strongest ideas
- working distinctions
- procedural value
- edge cases
- limits
- best examples
- conflicts with other sources

Remove:
- repeated phrasing
- decorative padding
- unsupported claims (unless clearly labelled as claims)
- long quotations unless necessary

Check: can each retained sentence be used directly? If not - revise or cut.

---

## Image-Only Sources

When the source material is image-only (scanned text, photograph of notes, PDF rendered as images):

1. State explicitly: `source_type: image-only`.
2. If the image is visually readable in context, extract directly and label `extraction_confidence: medium` (visual OCR is lossy).
3. If the image is not readable, state the limitation and request a transcription or text version. Do not attempt extraction from descriptions of image content.
4. All image-only extractions must carry a note in the provenance record: `"Source was image-only; extraction confidence is reduced and may miss fine-grained procedural detail."`

---

## Multi-Source Collision Check

When two or more sources cover the same domain, run this collision check after completing Phase 7 for each source independently.

1. List all procedures and claims from Source A that address the same topic as Source B.
2. Classify each intersection as: `agreement | conflict | complement | overlap`.
3. For each conflict, classify the type: `factual | methodological | scope | emphasis`.
4. Do not suppress conflicts. Record them with both source positions.
5. Decide precedence per procedure: which source governs, and why. Record in provenance.
6. Build a synthesis layer in `extracted-knowledge.yml` under `multi_source_synthesis`.
7. Update the derived skill's relationship contracts to reference both sources.

After Layer 8, run a gap check:
- What skill domain does this source target?
- What does the domain skill still need that this source did not supply?
- Which other sources might fill the gap?
- Is the gap worth flagging in the output?

Record gaps in the update notes. Do not leave them silent.

---

## Provenance Record

For every skill derived from a source, record:

```yaml
provenance:
  source_title: ""
  source_author: ""
  extraction_date: ""
  extraction_depth: "surface | standard | deep | forensic"
  extraction_confidence: "high | medium | low"
  derived_skills: []
  derived_sub_skills: []
  gaps_identified: []
  supersedes: []
  superseded_by: []
  review_trigger: "When a second source on the same domain arrives, re-run collision check."
```
