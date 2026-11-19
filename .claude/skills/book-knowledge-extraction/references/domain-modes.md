# Domain-Specific Extraction Modes

Four modes. Select based on Phase 1 source classification. Modes affect which extraction
layers receive the most attention and how Phase 5 skill conversion is framed.

---

## Mode A — Fiction and Craft

Activate when: the source is a novel, story collection, craft guide, writing manual,
literary criticism, or author interview.

**Emphasis layers:** 3 (concept), 5 (procedure), 8 (compression without loss).

**Additional extractions:**
- Voice: what register, tone, sentence rhythm, and narrator relationship does the source demonstrate or describe?
- Technique: which craft moves are named or implied?
- Contra-lean: does the source deliberately violate standard advice? Record the violation and its justification.
- Genre tradition: which lineage does the source sit in? (Weird fiction, military gothic, golden age, etc.)

**Phase 5 routing:** `golden-age-author`, `weird-fiction-forensics`, `military-gothic-voice`,
`plot-paradigms-engine` depending on domain.

**Clause emphasis:** behavioural impact, contrast, exception (see `clause-writing.md`).

---

## Mode B — Game Design

Activate when: the source is a game design book, rulebook, playtest methodology guide,
player psychology text, or boardgame theory essay.

**Emphasis layers:** 4 (argument), 5 (procedure), 6 (skill conversion).

**Additional extractions:**
- Mechanic: what decision structures, player actions, or system interactions does the source describe?
- Playtest: does the source contain testable design claims? Mark each as `falsifiable | asserted`.
- Player psychology: what does the source say about player motivation, cognitive load, or table behaviour?
- Genre: which game genre does the content primarily address?

**Phase 5 routing check:** Is this eurogame theory (`eurogames-the-elegant-design-culture-and-play-workshop`)
or general game design (`boardgame-design-hydra`)? If both — route to the more specific first.

**Clause emphasis:** conditional, evidence, audit.

---

## Mode C — Technical and Academic

Activate when: the source is an academic paper, technical manual, research methodology
guide, scientific text, or formal analysis.

**Emphasis layers:** 2 (structure), 3 (concept), 4 (argument).

**Additional extractions:**
- Evidence quality: is each claim empirical, theoretical, or speculative?
- Methodological limits: what does the source exclude or assume?
- Transferability: can the method be applied outside its original domain?

**Confidence scoring:** apply stricter confidence levels. Asserted claims without evidence
must be labelled `asserted | unverified`.

**Phase 5 routing:** depends on discipline. Route to closest installed domain skill.
If no domain skill exists, produce standalone skill and flag for `skill-creator` evaluation.

**Clause emphasis:** definition, limiting, causal.

---

## Mode D — SEO, Marketing, and Persuasion

Activate when: the source is an SEO strategy guide, marketing framework, persuasion theory,
consumer behaviour research, or digital marketing playbook.

**Emphasis layers:** 5 (procedure), 4 (argument), 8 (compression).

**Additional extractions:**
- Operational rules: what does the source say to do, specifically?
- Signals and triggers: what user behaviours or search signals does the source address?
- Costly signal logic: does the source describe interventions that work because they are hard to fake?
- Bee Colony fit: does the content map to scout, follower, memory, or outlier page roles?

**Phase 5 routing:** `alchemy-hive`. Extracted content must translate into an operational
protocol before being added. Generic advice that cannot map to a page role or execution rule
is low-value. Flag it.

**Clause emphasis:** evidence, exception, behavioural impact.

---

## Mode Selection Ambiguity

When a source spans two modes (e.g., a book on player psychology that is also a craft guide
for writing game fiction):

1. Identify the primary domain from the source's central claim.
2. Assign primary mode.
3. Run primary mode fully.
4. Run secondary mode on the layers that don't overlap.
5. Route to primary skill target first; secondary target second.

Do not merge mode outputs into a single undifferentiated extraction.
