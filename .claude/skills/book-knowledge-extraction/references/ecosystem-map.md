# Ecosystem Cross-Fertilisation Contracts

Bidirectional relationship contracts between `book-knowledge-extraction` and the installed skill ecosystem.

These are structured contracts, not vague backlinks.

---

## book-knowledge-extraction -> weird-fiction-forensics

```yaml
relationship_contract:
  id: "rel-book-extraction-weird-fiction-forensics-source-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "weird-fiction-forensics"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> weird-fiction-forensics"
  relationship_type: "dependency"
  relationship_strength: "strong"
  strength_reason: >
    Weird fiction and cosmic horror books are the primary source material for
    weird-fiction-forensics writer profiles and technique cards. Extraction from
    source texts directly populates and extends the forensic corpus.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When a weird fiction or cosmic horror source is processed, Phase 5 skill
    conversion must route extracted procedures and voice techniques to
    weird-fiction-forensics as candidate technique card additions or writer
    profile extensions.
  reciprocal_update_required: true
```

**Reciprocal (weird-fiction-forensics <- book-knowledge-extraction):**
> weird-fiction-forensics receives new writer profiles, technique cards, and voice
> registers from book-knowledge-extraction when source material is processed from
> the tradition. It must flag which profiles need updating when new sources arrive.

---

## book-knowledge-extraction -> golden-age-author

```yaml
relationship_contract:
  id: "rel-book-extraction-golden-age-author-craft-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "golden-age-author"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> golden-age-author"
  relationship_type: "influence"
  relationship_strength: "strong"
  strength_reason: >
    Fiction craft books are a primary source of council lens calibration material.
    Extracted techniques directly extend the editor, storyteller, and teacher
    lenses with new procedural content.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When a fiction craft book is extracted, derived sub-skills must be evaluated
    for whether they extend an existing council lens or warrant a new specialist
    voice. The council does not automatically absorb book-derived content; it must
    be evaluated against the narrowest-lens-first constraint.
  reciprocal_update_required: true
```

**Reciprocal (golden-age-author <- book-knowledge-extraction):**
> golden-age-author should be consulted before finalising skill conversion from
> fiction craft sources, to ensure extracted sub-skills are consistent with
> existing council lens structure and do not duplicate current coverage.

---

## book-knowledge-extraction -> military-gothic-voice

```yaml
relationship_contract:
  id: "rel-book-extraction-military-gothic-voice-voice-extension"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "military-gothic-voice"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> military-gothic-voice"
  relationship_type: "influence"
  relationship_strength: "moderate"
  strength_reason: >
    Military fiction, gothic fiction, and grimdark sources extend the prose
    voice corpus. The effect is moderate rather than strong because voice
    calibration from a single new source typically adjusts weighting within
    an established system rather than replacing it.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When military or gothic source material is extracted, Phase 5 must check
    whether extracted voice procedures conflict with, refine, or extend existing
    military-gothic-voice sub-skills (forensic analysis, six-book corpus,
    seven sub-skills). New sub-skills must be classified before addition.
  reciprocal_update_required: true
```

---

## book-knowledge-extraction -> boardgame-design-hydra

```yaml
relationship_contract:
  id: "rel-book-extraction-hydra-design-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "boardgame-design-hydra"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> boardgame-design-hydra"
  relationship_type: "dependency"
  relationship_strength: "strong"
  strength_reason: >
    Game design books, playtest methodology texts, and player psychology sources
    are the primary expansion source for HYDRA's genre engines, balance tools,
    and playtest persona library. Extraction directly populates HYDRA reference
    files.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When a game design source is extracted, Phase 5 routing must check
    which HYDRA reference file the content belongs in:
    references/genres.md, references/engines.md, references/mechanic-invention.md,
    references/playtest-system.md, or references/personas.md.
    Content must be placed in the correct file, not added as a free-standing skill.
  reciprocal_update_required: true
```

---

## book-knowledge-extraction -> eurogames-the-elegant-design-culture-and-play-workshop

```yaml
relationship_contract:
  id: "rel-book-extraction-eurogames-theory-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "eurogames-the-elegant-design-culture-and-play-workshop"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> eurogames"
  relationship_type: "dependency"
  relationship_strength: "strong"
  strength_reason: >
    Eurogame theory, game design culture texts, and player experience research
    directly extend the eurogames skill's genre analysis, mechanics taxonomy,
    and play pleasure models.
  direct_or_indirect: "direct"
  behavioural_impact: >
    Game design theory books must be evaluated against eurogame coverage before
    routing to boardgame-design-hydra. The eurogames skill is the more specific
    target for theory-first game design content.
  reciprocal_update_required: true
```

---

## book-knowledge-extraction -> plot-paradigms-engine

```yaml
relationship_contract:
  id: "rel-book-extraction-plot-paradigms-narrative-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "plot-paradigms-engine"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> plot-paradigms-engine"
  relationship_type: "influence"
  relationship_strength: "moderate"
  strength_reason: >
    Narrative theory, story structure, and screenwriting books can extend or
    challenge the existing sixteen paradigm models. Effect is moderate because
    the engine already has a mature paradigm set; new sources typically refine
    rather than restructure.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When a narrative theory source is extracted, Phase 5 must check whether
    the derived material updates an existing paradigm, warrants a new paradigm,
    or belongs as a sub-skill within an existing one. New paradigms must be
    wired bidirectionally into the sixteen existing ecosystem skills.
  reciprocal_update_required: true
```

---

## book-knowledge-extraction -> alchemy-hive

```yaml
relationship_contract:
  id: "rel-book-extraction-alchemy-hive-marketing-feed"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "alchemy-hive"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> alchemy-hive"
  relationship_type: "influence"
  relationship_strength: "moderate"
  strength_reason: >
    SEO strategy texts, persuasion theory, and marketing frameworks can extend
    the Alchemy Hive scout/follower/memory/outlier models and Sutherland protocols.
    Effect is moderate because theory-level additions require translation into
    the Bee Colony operational model before they affect execution.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When SEO or marketing source material is extracted, Phase 5 must evaluate
    which Alchemy Hive page role or protocol is affected. Content must map to
    an operational rule, not be added as generic advice.
  reciprocal_update_required: true
```

---

## book-knowledge-extraction -> skill-creator

```yaml
relationship_contract:
  id: "rel-book-extraction-skill-creator-meta"
  source:
    name: "book-knowledge-extraction"
    type: "skill"
  target:
    name: "skill-creator"
    type: "skill"
  relationship_direction: "book-knowledge-extraction -> skill-creator"
  relationship_type: "reference"
  relationship_strength: "contextual"
  strength_reason: >
    skill-creator is the quality control and packaging layer. After book
    extraction produces a new skill, skill-creator governs the evaluation,
    iteration, and packaging process. The link is contextual because book
    extraction does not always result in a new standalone skill.
  direct_or_indirect: "direct"
  behavioural_impact: >
    When extraction produces a complete new skill document, route to skill-creator
    for the draft > test > review > improve loop before installing.
  reciprocal_update_required: true
```

---

## router -> book-knowledge-extraction

The router should route to this skill when the user asks to:
- extract from a book or source
- build a skill from a document
- turn research into reusable knowledge
- add reading to the skill system
- analyse what a text can contribute to an existing skill

This route does not yet appear in the router's routing table. When the skill is installed,
the router's SKILL.md must be updated with:

```
- extract knowledge from a book or source, convert reading to skills -> book-knowledge-extraction
```
