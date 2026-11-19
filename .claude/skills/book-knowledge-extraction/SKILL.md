---
name: "book-knowledge-extraction"
description: "Absorbs books, essays, papers, manuals, workshop notes, YouTube transcripts and research packs, extracts their detail, clones their procedures to test the extraction, synthesises them with other sources and installed skills, plans the build, and rebuilds the material from notes to prove understanding. Use this whenever the user wants to learn from a source and turn it into skills, reusable procedures or a synthesis: extract from this, turn this book into a skill, what can I get from this, synthesise these sources, plan a skill from these notes, does the skill actually capture the book, add this to my system. Not for casual summaries the user wants read back to them, and not for operational offensive-security material. Dewey 028.7."
---

# Book Knowledge Absorption, Extraction and Synthesis

Author: TABARC-Code. Version 3.1.0.

Absorb a source, extract its detail, clone its procedures to test that the extraction holds, synthesise it with other sources and installed skills, plan the build, then rebuild from notes alone to prove the understanding is real. Every claim carries a location. Every relationship carries a reason. Where the source is silent, say so and leave the field blank.

Reference files, read only when the stage needs them:
- `references/extraction-layers.md` for the layered extraction protocol and templates
- `references/relationship-contracts.md` for relationship and reciprocal contract schemas
- `references/clause-writing.md` for clause-level writing standards
- `references/ecosystem-map.md` for bidirectional contracts with installed skills
- `references/domain-modes.md` for fiction, game design, academic and SEO modes
- `templates/skill-template.md`, `templates/extracted-knowledge.yml`, `templates/relationship-audit.yml`

Terms used throughout: a **stage** (A to G) is a step in the run order. A **layer** (1 to 8, in `extraction-layers.md`) is a category of content. Layers are filled in during the stages; they are not a second run order.

---

## 1. Operating rules

**1.1 Build the artefact.** Produce the skill, contract, synthesis or audit. Do not describe what a good one would contain. With no repository, produce the complete installable document, give recommended file paths, and say plainly that no live repository was changed.

**1.2 Blank beats wrong.** A wrong claim costs more than a blank. If the source does not support a field, write `unknown` and say why. Never claim a file was edited, checked or audited unless it was actually opened and changed.

**1.3 Every claim has an ID and an authority tier.** Format: `SRC-[source short name]-[location]-[n]`, for example `SRC-goldberg-ch3-p12-C04`.

| Tier | Meaning | Use when |
|---|---|---|
| `A1 quoted` | Short verbatim text, with location | The words are in the source and you have checked them |
| `A2 paraphrased` | Restated in the extractor's words, with location | The source says it, differently worded |
| `A3 example` | An anecdote or worked case | The source illustrates without generalising |
| `A4 inferred` | The extractor's deduction, not in the source | Always labelled. Never written as the author's view |

Authority is separate from confidence. A paraphrase can be high confidence. An inference is never high authority.

**1.4 Copyright and paraphrase.** Skills carry the knowledge, not the book. Paraphrase procedures and ideas in your own words. Quote only short passages (a sentence or two, and rarely more than about 25 words), each one tagged `A1`. Never reproduce chapters, long passages or a book's structure of exercises verbatim. If the user needs the exact text, point them to the book.

**1.5 Author's claim, not established fact.** An argument is the author's claim until a second source, the user's own testing, or evidence the source cites supports it. Write "the author argues that", not "it is the case that". This matters most for causal and statistical claims.

**1.6 Absence needs a complete read.** "The book does not cover X" is allowed only when the coverage record shows every section was read and the index was checked. Otherwise write `not found in sections read: [list]`.

**1.7 Candidate is not proof.** When two things sit side by side (a practice and an outcome, a correlation, a before and after), record a candidate link. Promote it to a cause only with a mechanism from the source or a second source.

---

## 2. Preflight

Run before Stage A. Record the results in the coverage record.

1. **Source present?** If only a description was given, run Stages A and B from the description at `surface` depth, mark confidence `uncertain`, and ask before going further.
2. **Installed targets.** Check the routing table (section 9) against the installed skill list. Do not route to a skill that is not installed. Log unrouted material as `unrouted: [target]` so it is not lost.
3. **Repository.** Check whether skill files, manifests and indexes are available. If not, work in document mode (rule 1.1).
4. **Input provenance.** For transcripts, record the caption track type (manual or auto), whether timestamps are present, and whether chapters exist. Auto captions cap confidence at `medium` and flag quotes as possibly misheard (section 8).
5. **Scope.** If the source's main content is operational offensive technique, decline and say why. Absorbing the ideas behind a field is fine. Producing a usable playbook for attacks is not.

---

## 3. Coverage record

One per source, updated as you read. It is what makes absence claims and "fully extracted" claims honest.

```yaml
source: "Title, Author, edition or upload date"
extraction_depth: surface | standard | deep | forensic
sections_total: 14
sections_read_fully: [1, 2, 3, 5, 6]
sections_skimmed: [4]
sections_not_read: [7-14]
index_checked: true | false
known_gaps: "Appendix tables not parsed"
```

A source counts as `fully extracted` only when `sections_not_read` is empty and `index_checked` is true.

---

## 4. The seven stages

Run in order. If a stage cannot be completed, write `STAGE_SKIPPED: [stage]: [reason]` and continue. Never drop a stage silently.

### Stage A: Absorb

Read the whole source, or as much as the coverage record allows. Write a first-pass gist in no more than five sentences: what the source is for, what it argues or teaches, who it is for. Make no claims yet.

**Check:** can you state the source's purpose and main argument in one sentence each? If not, read again or ask the user.

**Output:** coverage record, gist, source classification (type, discipline, audience, reliability, depth `surface | standard | deep | forensic`, confidence `high | medium | low | uncertain`).

### Stage B: Extract the detail

Generalities lose the value of a source. Capture the specifics: numbers, thresholds, named conditions, exceptions, order of steps, worked examples, and the author's own words where they carry weight (as `A1`, briefly).

Extract:
- **Structure:** chapters, sections, headings, the sequence of ideas, the turning points. For video, chapter markers become the structure, labelled as the uploader's labels.
- **Terms and distinctions:** definitions, binaries, taxonomies, categories. Mark any distinction too fuzzy to become a rule as `low-confidence`.
- **Claims:** the central thesis, supporting and subsidiary claims, assumptions, implied claims, counterarguments. Each gets an ID and tier.
- **Procedures:** step-by-step methods, decision trees, diagnostic checks, craft processes, repeatable habits. Label each `reusable | conditional | context-specific | deprecated | speculative`, with confidence.
- **Examples:** worked cases that show a procedure in use. Keep the ones that teach the edge, drop the ones that repeat.

**Check:** can each procedure become an operating rule without changing what the source means? If not, mark it `low-confidence` and do not convert it silently.

**Output:** structural map, term list, claim map (IDs and tiers), procedure list.

### Stage C: Clone the procedures

This is the test that the extraction holds. Take each high-value procedure and rebuild it step by step, using only the extraction notes, in your own words, as a runnable procedure. Then compare the clone against the source's procedure and log every divergence:

- **Missing step:** the source has a step the clone lacks.
- **Reordered step:** the sequence has changed, and the source's order mattered.
- **Lost condition:** a "when" or "unless" was dropped.
- **Softened threshold:** a number or limit became vaguer.
- **Invented step:** the clone contains a step the source does not support (tier `A4`, labelled).

Each divergence is a fault. Fix it in the extraction notes and clone again until the divergence list is empty or each remaining item is recorded as a known limit.

The clone is a working test. It is not the shipped skill.

**Output:** clone records per procedure, divergence log, fixes applied.

### Stage D: Synthesise

Synthesis is where the value sits, so do it deliberately. Four moves:

1. **Collision check across sources.** Where do sources agree, conflict or complement each other? Classify conflicts as `factual | methodological | scope | emphasis`. Do not average them. Carry the tension forward unless the user resolves it.
2. **Bridge concepts.** Look for the same idea under different names in different sources, or the same name for different ideas. Naming a bridge concept is often the most useful output of the whole run. Record it with the sources that support it.
3. **Governance.** For each procedure, record which source governs it and why. Precedence needs a reason: the more specific source, the more recent evidence, the source with the worked example, or the source the user trusts for this domain.
4. **Cross-fertilisation with installed skills.** Which installed skills gain a rule, an example or a counter-example from this material? Which contradict an existing rule? Record both, and send contradictions to the unknowns register rather than resolving them in silence.

**Check:** does every procedure have a governing source? Does every conflict have a classification? Does every bridge concept name its supporting sources?

**Output:** synthesis map (agreements, conflicts, bridges, governance, cross-skill effects).

### Stage E: Plan the build

Turn the synthesis into a build plan before writing anything. The plan lists:

- the skills and sub-skills to create or change, each with its one independent function
- the files to write, and where they go
- the build order, with dependencies between items
- the unknowns that must close first (section 5)
- what is ready now and what is blocked, and why

Check the plan against the coverage record. Any planned item that rests on an unread section is blocked, not ready.

**Output:** build plan with ready and blocked items.

### Stage F: Build

Write the skill, sub-skills, relationship contracts and index entries, following the plan. Each sub-skill has an independent function, not a copy of its parent. Every direct link gets a reciprocal written on the other side, with a strength, a reason and a behavioural effect.

Relationship classes: `dependency | influence | prerequisite | specialisation | chain | conflict`. Strengths: `critical | strong | moderate | weak | contextual | optional`. Chain distance 1 is direct, 2 is one level down, 3 or more is weak or contextual unless justified. Read `references/relationship-contracts.md` for the full schema.

**Output:** skill files, contracts, index entries, change notes in plain language.

### Stage G: Rebuild to understand

The final test. A skill that reads well can still hide a misunderstanding. So rebuild the source from the skill alone and compare.

1. Give a fresh agent (a subagent where available, otherwise a clean pass that does not reuse the extraction notes) the built skill and the rebuild brief below. Do not give it the source.
2. Rebuild brief: "Using only these files, reconstruct the source's central argument, its core procedures in order, its key distinctions and its stated limits. Mark each item with the tier you think it has."
3. Compare the rebuild against the Stage B claim map and the Stage C procedure records.
4. Score each core item as `reconstructed correctly`, `reconstructed with altered meaning`, `missing`, or `invented`.

Understanding score = correctly reconstructed core items / total core items. Core items are the central thesis, the top-value procedures, and the main distinctions. Record the score and the list of misses.

Act on the result:
- Score at or above 0.85 with no invented items: pass. Record it.
- Misses or altered meanings: return to Stage B for those items, fix, rebuild, and rescore. Each misunderstanding is a negative signal in the Kaizen log.
- Invented items: check whether the skill is wrong or the rebuild is. Either way, the mismatch is logged.

The threshold is a starting point, not a law. Record the number you used and why. If the source is hard and the rebuild is close, say so and do not pretend it passed.

**Output:** rebuild brief, rebuild output, comparison table, understanding score, misses, actions taken.

---

## 4.1 Extraction playbook

Use this when the source is long, dense or unfamiliar. It sits inside Stages A and B and adds reliability. It does not change the stage order.

### Intake questions (ask once, or assume and state the assumption)

1. What should the output do: a new skill, a reference for an existing skill, a synthesis, or a rebuild test only?
2. What should be left out (for example, a book's anecdotes, or a chapter on a topic already covered)?
3. Which installed skills are likely targets? (Used to bias Stage B toward the detail those skills need.)

Record the answers in the coverage record. If the user does not answer, say which assumption was made.

### Long-source protocol

Books and long reports exceed a single pass. Work in chunks.

1. Split by the source's own structure: chapters, parts, or 3,000 to 5,000 word blocks where none exist. Write the split into `sections_total`.
2. Extract each chunk into the extraction YAML before reading the next. Do not hold a chunk in memory and summarise later. Early detail is the first thing lost.
3. After each chunk, update the coverage record: move the chunk from `sections_not_read` to `sections_read_fully` or `sections_skimmed`. A skimmed section must say what was skipped.
4. After the last chunk, run a reconciliation pass over the claim list. Look for claims in chapter 9 that contradict or qualify claims in chapter 2, and record the scope conditions that the later chapter adds.

### Recall and precision checks

Two sampling checks run after Stage B. They catch extraction that looks complete but is not.

- **Recall sample.** Choose at least one section in ten, at random if the source has more than ten. Reread it against the extraction. Count the substantive items in the section (claims, steps, distinctions, worked examples) that are missing from the extraction. Record the count and the missed items. Recall is items found divided by items in the sample. A recall below 0.8 means Stage B is not finished.
- **Precision sample.** Choose five extracted claims or procedures at random. For each, check that the location in the record matches the text, that the authority tier is right, and that no detail has been added. Record any mismatch as an extraction fault.

Both samples are logged in the Kaizen log. If recall or precision fails twice in a row, change how Stage B is done, not just the output.

### Content-type recipes

Each source type has a usual place where the useful material sits. Start there, then read the rest.

| Source type | Where the procedures usually are | Watch for |
|---|---|---|
| Argument book | Introduction (thesis), conclusion (what changed), the chapter that tests the thesis | Thesis stated broadly and qualified later. Record the qualification as the scope. |
| Procedural manual | Numbered steps, warnings, tables of limits and thresholds | Steps out of order in the text. Preserve the source's order and note any reordering the author recommends. |
| Essay | Its one or two central distinctions | Rhetorical flourish. Most of it is A3 or A2 at best. |
| Academic paper | Methods (procedure), limitations (scope), results (claims with evidence) | Claims from the abstract that the results section does not support. Mark them asserted. |
| Transcript or video | Chapters (uploader's labels) and any numbered list spoken aloud | Auto-caption mishearing. Numbers and names are the usual casualties. Check against timestamp. |
| Anthology or collection | Each piece separately, with its own coverage record | Editorial framing in the introduction, which is not the authors' claim. |
| Abridged or translated edition | Whatever the edition contains | Record the edition in provenance. Translator choices can change a technical term. Flag any term that might be mistranslated. |

### Tables, figures and notes

- **Tables** are often the densest procedure in a technical source. Extract each table as a row-level record with its caption and the table's location. Do not paraphrase a table into prose and lose its thresholds.
- **Figures** are extracted only if the text explains them. An unexplained figure is recorded as `figure without text support` and not converted to a claim.
- **Footnotes and endnotes** are extracted as a separate list. A footnote that adds a condition to a claim is a scope clause for that claim. A footnote that is only a citation is not extracted unless the user asks for citations.

### Negative extraction

Record what the source rejects, not only what it endorses. An explicit "do not" is often the most useful rule in a manual. Each rejected practice gets its own record, with its authority tier and the reason the author gives. Without this, a skill built from the source can recommend the thing the source warns against.

### Procedure test

A step counts as a procedure step only if it can be executed. For each step, check that it has:

- an actor (who or what does it)
- an input (what it starts from)
- an action (one verb)
- an output (what it leaves behind)
- a stop condition (when it is done or abandoned)

A step missing any of these is recorded as `incomplete procedure` and sent back to Stage B. It is not promoted to a rule.

### Yield and quality metrics

Track these each run so runs can be compared:

- claims extracted per 1,000 source words
- procedures extracted, and the share that pass the procedure test on the first pass
- items rejected at precision checks, with the reason
- recall and precision scores from the samples
- quote count against the rule 1.4 limit

A falling yield with the same source type means Stage B is missing material. A rising yield with falling precision means it is over-extracting. Both go in the Kaizen log with the signal that caused the change.

---

## 5. Unknowns register

Gaps are tracked, not buried. One register per skill system:

```yaml
id: U-007
question: "Does the source give a sample size for the playtest method?"
needed_authority: "A1 or A2 from a section not yet read"
supporting_claims: []
contradicting_claims: []
status: open | closed
revision: 3
```

- Close an unknown only with evidence at equal or higher authority than the claim it is closed against.
- Update with the current revision. If the revision is stale, reread the entry and retry. Never overwrite blind.
- Closed entries keep their history.

The evidence-tier and unknowns discipline is this skill's own design. An earlier version credited an external project; that attribution could not be verified, so it has been removed.

---

## 6. Audit

Run after every stage that changes files, and at the end of every run.

- **Evidence audit.** Every claim has an ID and tier. No `A4` item is written as the author's view. Every absence claim has a coverage record behind it. No quote exceeds the limit in rule 1.4.
- **Relationship audit.** Every direct link has a reciprocal. Every relationship has a strength and a reason. Every chain position has a weight. Reverse and cross-chain links are written, not assumed.
- **Sub-skill audit.** Each sub-skill has an independent function. Conditional sub-skills state their activation conditions. Sub-skill weights may differ from the parent's.
- **Clone audit.** Every high-value procedure has a clone record and an empty or justified divergence list.
- **Synthesis audit.** Every procedure has a governing source. Every conflict is classified. Every bridge concept names its sources.
- **Understanding audit.** The rebuild score is recorded and above threshold, or the shortfall is stated.
- **Repository audit (when files exist).** Changed files are listed. Nothing skipped silently. Manifests and indexes updated.
- **Writing audit.** Rules are explicit. No clause carries two rules. No corporate fog, no preamble, no arrow glyphs.
- **Blind audit (when subagents are available).** An auditor gets the produced skill and the source excerpts, but not the extraction reasoning. It checks each claim against the source and reports mismatches. A system that marks its own homework passes its own mistakes.

Report each area as passed, failed, partial or not applicable. Never write "passed" for an area you did not check.

---

## 7. Feedback loops and the Kaizen log

Quality is measured across runs. Positive and negative signals are both recorded.

**Positive signals** (keep doing):
- procedures convert to rules without rewriting
- a clone matches its source procedure with no divergence
- a bridge concept resolves an ambiguity in an installed skill
- the rebuild reconstructs core items with the right tier
- relationship contracts need no later correction

**Negative signals** (fix now):
- a procedure has actions but no executable rule
- a clone diverges from its source (missing, reordered, lost condition, softened threshold, invented step)
- the rebuild misreads or invents a core item
- a strength has no reason, or a sub-skill copies its parent
- a reciprocal is missing
- a `high` confidence claim has no location
- an absence claim has no coverage record

**Loop rules:**
- A negative signal triggers a change in the next run, not a note for later.
- A change is kept if the next two runs show positive signals and no repeat of the same negative signal.
- A change that produces the same negative signal twice is reverted.
- Every change is logged with the signal that caused it.

**Kaizen log entry:**

```markdown
## 2026-10-16 | source: [title] | run 4
- signal: NEG | rebuild misread the thesis as a claim about all cases (stage G)
- cause: Stage B recorded the thesis without its scope condition
- change: Stage B now requires a scope field on every thesis-level claim
- metric: understanding score 0.71 in run 3, 0.88 in run 4
- status: keep, pending two positive runs
```

**Four passes after each build:** weakness detection (vague or misreadable rules, contracts with no effect, over-broad sub-skills), execution tightening (usable in a repository, missing-file behaviour defined, honest reports), knowledge density (strongest material kept, knowledge turned into action, weights justified), final audit.

---

## 8. Input from video and transcripts

When the source is a video, use the youtube skill's bundle: `manifest.json`, `chapters.json` (if present) and a timestamped transcript. The file names are assumed from an earlier build; confirm them against the youtube skill's actual output before relying on them.

- `manual` captions allow confidence up to `high`. `auto` captions cap it at `medium`.
- Every quote from an auto-caption track is tagged `A1 quoted (auto-caption, may be misheard)` and checked against its timestamp before use.
- Cite as `[Video title, channel, 12:34]` with the timestamp and the video ID.
- Chapters feed Stage B's structure, labelled as the uploader's labels.
- No captions: say so. Do not extract from the description alone unless the user accepts `surface` depth.

---

## 9. Routing and cross-fertilisation

Route extracted knowledge to the installed skill it feeds. Check that the target is installed before routing.

| Source domain | Target skill | Strength | Status at version 3.0.1 |
|---|---|---|---|
| Fiction craft, long-form narrative | `golden-age-author` | strong | installed |
| Military fiction, gothic voice | `military-gothic-voice` | strong | installed |
| Game design, tabletop, card games | `boardgame-design-hydra` | strong | installed |
| Eurogame theory, player psychology | `eurogames-the-elegant-design-culture-and-play-workshop` | strong | installed |
| SEO, marketing, persuasion | `alchemy-hive` | moderate | installed |
| New skill infrastructure | `skill-creator` | contextual | installed |
| Narrative structure, story paradigms | `plot-paradigms-engine` | moderate | not in the installed list at 3.0.1. Do not route. Log as unrouted. |
| Pulp and weird horror analysis | `weird-fiction-forensics` | strong | not in the installed list at 3.0.1. Do not route until an installed name is confirmed. Candidate names to check on install: `pulp-autopsy`, `weird-prose-forensics`. |

Other skills in this system:
- **youtube**: supplies the Stage A and B input bundle (section 8).
- **skill-creator**: runs the with-skill and baseline tests on this skill's output.
- **skill-builder**: owns the classification and relationship-contract sub-skills. Hand off when a relationship map changes shape.

When the domain is ambiguous, ask before routing.

Router entry (add only if not already covered):
`- extract, synthesise and rebuild knowledge from a book, video or source into skills: book-knowledge-extraction`

---

## 10. Testing this skill

Test the skill, not only the book. Run three test sources through all seven stages:

1. A short essay (about 2,000 words) with clear procedures.
2. One chapter of a book mixing argument and method.
3. A YouTube transcript on an auto-caption track.

Assertions for each run:
- every extracted claim has an ID, a location and a tier
- no `A4` item is presented as the author's claim
- every absence claim has a coverage record
- every high-value procedure has a clone record
- every conflict is classified and every procedure has a governing source
- every direct relationship has a reciprocal, and every strength a reason
- the rebuild understanding score is recorded, and misses are logged
- auto-caption quotes carry the flag
- no quote exceeds the limit in rule 1.4
- no arrow glyphs appear in the output
- unknowns are logged, not dropped

Use `skill-creator` to compare with-skill and baseline runs. Record the results in the Kaizen log.

---

## 11. Final response format

Keep it short. Every run ends with:

```markdown
## Summary
[What was absorbed, extracted, synthesised, built or rebuilt.]

## Files updated or created
- [path]: [what changed]
(Or: No repository files were supplied. Complete installable document produced instead.)

## Synthesis
[Agreements, conflicts, bridge concepts, governing sources, cross-skill effects.]

## Understanding
- Clone divergences: [none / list]
- Rebuild score: [value, threshold used, misses]

## Coverage
- Sections read fully: [list or count]
- Sections not read: [list]
- Fully extracted: [yes / no]

## Audit report
- Evidence tiers and absence claims: [passed / failed / partial]
- Relationship contracts and weights: [passed / failed / partial]
- Sub-skill independence: [passed / failed / partial]
- Clone and synthesis audits: [passed / failed / partial]
- Notes and indexes: [passed / failed / not applicable]
- Blind audit: [run / not run, reason]
- Unverified claims: [none / list]

## Extraction quality
- EXTRACTION_QUALITY: [high / medium / low]
- EXTRACTION_FAULTS: [none / list, with corrections applied]
- Kaizen log entries added: [count]

## Unknowns
[Open items from the register. Specific limits only. Do not invent problems.]
```

---

## 12. Update notes

**3.0.1 (fixes and tightening)**
- Replaced stale "Phase 1 to 8" references in `references/` and `templates/` with stage names. Stages are the run order. Layers are content categories.
- Marked `weird-fiction-forensics` and `plot-paradigms-engine` as not installed at 3.0.1. Routing to them is blocked until an installed name is confirmed.
- Removed an unverified external attribution, and an unverified count of ecosystem skills.
- Marked unverified lens names, sub-skill lists and file lists in `ecosystem-map.md` as unconfirmed until checked on install.
- Added a mapping from layer-6 sub-skill roles to contract link types, so the two vocabularies no longer clash.
- Added `speculative` to the procedure labels in Stage B, to match layer 5.
- Templates now carry claim and procedure IDs, authority tiers, coverage, clone records, bridge concepts, the understanding record and the uninstalled-target check that section 1.3, Stage G and section 6 require.

Kaizen signal for this change: NEG. Stale stage references and unverified claims could send a run to the wrong skill or the wrong stage. Change: stage names throughout, targets checked against the installed list. Keep, pending two positive runs.

**3.1.0 (extraction improvements)**
- Added section 4.1, the extraction playbook: intake questions, long-source chunking with a reconciliation pass, recall and precision sampling, content-type recipes, table, figure and note handling, negative extraction, the procedure test, and yield metrics.
- Recall and precision checks are now required after Stage B, not optional.

Kaizen signal for this change: none observed yet. The change is untested. Reason: the earlier version had no check that Stage B had captured what the source contained. Keep only if a test run on a real source confirms recall and precision are measured and reported.

Before handing the built skill over, run `skill-security-scanner` on it: the source text came from outside the repo.

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **skills-create** · type: handoff · source: description
  - This skill (weight 2): Hands the skill build for an extracted book to skills-create.
  - skills-create: Authors the skill once book-knowledge-extraction has extracted the material.
- **deep-research** · type: reference · source: description
  - This skill (weight 1): Absorbs research packs and sources that deep-research produces.
  - deep-research: Its research pack can be absorbed and synthesised by book-knowledge-extraction.
- **skill-security-scanner** · type: gate · source: body
  - This skill (weight 2): Runs it on the skill built from a source before handing it over.
  - skill-security-scanner: Is called on skills built from outside source text.
<!-- relationships:end -->
