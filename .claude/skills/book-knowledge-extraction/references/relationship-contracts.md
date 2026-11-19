# Relationship Contract Schemas

Every skill-to-skill, skill-to-sub-skill, sub-skill-to-skill, or sub-skill-to-sub-skill relationship
must be recorded as a structured contract. Vague backlinking is not sufficient.

The following phrases are not acceptable without a full contract:
- related to
- linked with
- see also
- connected
- associated
- useful for

---

## Primary Relationship Contract

```yaml
relationship_contract:
  id: "rel-[source]-[target]-[short-purpose]"
  source:
    name: ""
    type: "skill | sub-skill | note | source | manifest | index"
    parent: ""
  target:
    name: ""
    type: "skill | sub-skill | note | source | manifest | index"
    parent: ""
  relationship_direction: "source -> target"
  reciprocal_direction: "target <- source"
  relationship_type: "dependency | influence | prerequisite | inheritance | specialisation | support | override | reference | conflict | chain | contextual"
  relationship_strength: "critical | strong | moderate | weak | contextual | optional"
  strength_reason: ""
  direct_or_indirect: "direct | indirect"
  chain_position:
    chain_id: ""
    upstream: []
    downstream: []
    distance_from_source: 0
    propagation_weight: ""
  behavioural_impact: ""
  execution_effect: ""
  interpretation_effect: ""
  update_requirements:
    source_side: ""
    target_side: ""
    indexes_or_manifests: []
    notes: ""
  reciprocal_update_required: true
  audit_status:
    status: "pending | passed | failed | partial"
    checked_items: []
    issues: []
```

---

## Reciprocal Contract

The reciprocal side must not be a mirror. It must explain what the relationship means from the target's perspective.

```yaml
reciprocal_relationship_contract:
  id: "rel-[target]-[source]-reciprocal-[short-purpose]"
  source:
    name: ""
    type: "skill | sub-skill | note | source | manifest | index"
  target:
    name: ""
    type: "skill | sub-skill | note | source | manifest | index"
  relationship_direction: "target <- source"
  reciprocal_direction: "source -> target"
  relationship_type: "received_dependency | received_influence | received_reference | received_override | received_context"
  relationship_strength: "critical | strong | moderate | weak | contextual | optional"
  strength_reason: ""
  direct_or_indirect: "direct | indirect"
  chain_position:
    chain_id: ""
    upstream: []
    downstream: []
    distance_from_origin: 0
    propagation_weight: ""
  behavioural_impact_on_this_skill: ""
  what_this_skill_must_check_before_execution: []
  what_this_skill_must_update_when_changed: []
  audit_status:
    status: "pending | passed | failed | partial"
    checked_items: []
    issues: []
```

---

## Relationship Strength Categories

### Critical
Target cannot function correctly without the source.
Example: a citation-formatting sub-skill may be critical to an academic reference generator.

### Strong
Source heavily shapes the target; target can still function in degraded form without it.
Example: complex clause writing strongly shapes a technical documentation skill.

### Moderate
Source meaningfully influences the target but does not control its core behaviour.
Example: a book-derived metaphor extraction skill may moderately influence a creative writing skill.

### Weak
Source lightly informs the target.
Example: a formatting skill weakly influences a planning skill.

### Contextual
Relationship only matters under defined conditions.
Example: a legal-style clause precision skill contextually influences a writing skill only when drafting contracts.

### Optional
Source improves the target but is not required.
Example: a literary style analysis sub-skill may optionally improve a general summarisation skill.

---

## Weight Assignment Rules

For every weight, ask:
1. Does the target fail without the source?
2. Does the source alter behaviour or merely provide reference material?
3. Is the link always active or condition-specific?
4. Is the influence direct or propagated through a chain?
5. Does the relationship affect execution, interpretation, output formatting, or audit only?

The chosen strength must include a stated reason.

---

## Chain Propagation

For a chain: `A -> B -> C -> D -> E`

Default weighting:
- distance 1 (A-B): direct — original weight applies
- distance 2 (A-C): reduce one level unless behaviourally important
- distance 3 (A-D): usually weak or contextual
- distance 4+ (A-E): usually weak, contextual, or audit-only

Do not apply this mechanically. A distant source can still be critical if it supplies a rule that governs the whole chain.

Example of a recorded indirect relationship:

```yaml
indirect_relationship:
  source: "A"
  target: "E"
  direct_or_indirect: "indirect"
  chain_position:
    upstream: ["A", "B", "C", "D"]
    downstream: ["E"]
    distance_from_source: 4
  relationship_strength: "weak"
  strength_reason: "A reaches E through four intermediaries; influence is structural rather than directly behavioural."
  behavioural_impact: "E should preserve awareness of A's originating assumptions during audit, but not defer to A during ordinary execution."
```

---

## Reverse and Cross-Chain Rules

Do not assume reverse links exist automatically.

In a chain `A -> B -> C -> D -> E`, these require explicit contracts if they exist:
```
B -> E
D -> A
E -> C
```

Each must explain:
- why the link exists
- whether it alters execution
- whether it creates dependency, influence, override, support, or reference
- whether it changes chain propagation
- which files must be updated
