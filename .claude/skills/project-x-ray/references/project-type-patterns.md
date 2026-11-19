# Project Type Patterns

Signal reading for non-code and mixed projects.
Used during PHASE 1 of Project X-Ray when the project type is unclear.

---

## How to Classify

This file is loaded during PHASE 1 Step 1 when the project type is unclear from the
top-level structure alone. The node taxonomy for mapping project contents lives in
PHASE 2 Lens 1 of the main SKILL.md.



Read the top-level folder and root documents before deciding. Do not assume software.
Common mistake: a folder with a README and some scripts is immediately labelled a code project.
It might be a research study with some data processing attached. Read first.

**Classification order:**
1. What are the most prominent file types?
2. What does the root-level document (if any) say this is?
3. What folder names suggest?
4. Who appears to be the intended audience?
5. What would someone do with this?

Multiple types can coexist. A product folder might contain a PRD (business), wireframes
(creative), and a prototype (software). Label all types present.

---

## Software / Code

**Clear signals:**
- Source files (.py, .js, .ts, .go, .rb, .php, .rs, .java)
- Dependency manifests (package.json, requirements.txt, Cargo.toml, go.mod)
- Build configs (Makefile, Dockerfile, vite.config.js, webpack.config.js)
- Test directories with test files
- CI configuration (.github/workflows, .gitlab-ci.yml)
- Version control artifacts (.gitignore, CHANGELOG.md)

**Ambiguous signals (could be something else):**
- README.md alone — many non-code projects use these
- YAML or JSON files — could be data, config, or automation
- Scripts (.sh, .ps1) — could be deployment, admin tooling, or automation docs

→ See `references/framework-fingerprints.md` for language and framework identification.

---

## Creative / Design

**Clear signals:**
- Brand guidelines document (PDF or DOCX titled brand, guidelines, identity, standards)
- Asset folders named by type: logos, fonts, icons, imagery, photography, illustrations
- File formats: .ai, .eps, .psd, .fig, .sketch, .xd, .indd, .afdesign
- Exported assets in web formats alongside source files (suggests production workflow)
- Colour palette documents or swatches
- Typography specification documents
- Mood boards or visual reference collections
- Style guide or design system documentation

**Domain signals:**
- A "logo" folder almost always means brand identity work
- "Mockups" folder suggests client presentation or pitch
- "Production" or "print-ready" folder suggests delivered or near-delivered work
- "Archive" or "OLD" alongside current versions suggests iterative client work

**Common structural patterns:**
```
brand-project/
  01_brief/           ← project started here
  02_concepts/        ← multiple routes proposed
  03_development/     ← chosen route built out
  04_final/           ← client-approved
  05_production/      ← delivered or print-ready
  assets/             ← live brand files
```

**Red flags for creative projects:**
- No brief present — how was this project defined?
- Multiple "final" folders with no clear current version
- Source files absent (only exports) — original editables missing or not shared
- No client approval document or sign-off email

---

## Marketing / Campaign

**Clear signals:**
- Documents named brief, strategy, plan, campaign, audience, insight, messaging
- Channel-specific folders: social, email, paid, organic, PR, events
- Campaign calendar or content calendar
- Copy decks or messaging documents
- Audience definitions, personas, or segmentation files
- Analytics reports or performance dashboards
- Budget tracker or media plan

**Domain signals — campaign structure:**
A typical campaign project moves through these domains:
- **Brief** — problem, objective, audience, budget, timeline
- **Strategy** — insight, positioning, message hierarchy, channel plan
- **Creative** — concepts, copy, visuals, formats
- **Production** — assets built, reviewed, approved
- **Activation** — launch, trafficking, going live
- **Measurement** — tracking setup, results, reporting

If you can identify where in this chain the project currently sits, say so. That is often
the most useful orientation information for someone new.

**Common file naming red flags:**
- `brief_v4_FINAL_amended.docx` — brief has been through four rounds, suggesting scope instability
- Multiple audience documents with no "approved" or "current" marker
- Campaign plan dated from six months ago with no update

---

## Advertising / Pitch

**Clear signals:**
- Pitch deck or credentials document
- Creative concepts named (Concept A, Concept B, Route 1)
- Treatment documents (usually for film or production)
- Media plan or media strategy
- Budget or cost estimate
- Tissue session or tissue presentation (early concept review)
- Mandatories or mandatories list (things the client requires)
- SOW or Statement of Work

**Domain signals:**
An advertising pitch typically contains:
- **Problem** — what the brand or client needs to solve
- **Insight** — the human truth that makes the work relevant
- **Idea** — the core creative concept
- **Execution** — how the idea becomes campaigns, content, or activations
- **Production plan** — how it gets made
- **Budget** — what it costs

If any of these are missing from a pitch, say so. A pitch without an idea section has not
yet been developed past the brief stage.

**What to check:**
- Is there a client or brand brief? (External input the work is responding to)
- Is there a response or creative brief? (Internal document translating the client brief)
- Are the concepts named and differentiated? (Not just "creative concept")
- Is there a recommended option? (A pitch usually has a preferred route)

---

## Editorial / Content

**Clear signals:**
- Editorial calendar or content calendar
- Article drafts or scripts
- Interview notes or transcripts
- Research files or source documents
- Fact-check documents
- Style guide (editorial, not visual)
- Commissioning briefs or pitches
- Headline options or copy variants
- Author bios or contributor information

**Domain signals:**
- **Commissioning** — what was asked for, by whom, for when
- **Research** — evidence, sources, interviews, data
- **Writing** — drafts, versions, edits
- **Editing** — tracked changes, comments, editorial notes
- **Fact-checking** — verified claims, contested points
- **Legal or compliance** — cleared or not
- **Publication** — where it goes, when, in what format

**Common problems:**
- Drafts present but no brief — what was the editorial intent?
- Multiple versions with no version labelling
- Research files present but not linked to specific claims in the draft
- No stated audience or publication target

---

## Research / Analysis

**Clear signals:**
- Research question or hypothesis document
- Survey instrument or interview guide
- Raw data files (.csv, .xlsx, .spss, .json datasets)
- Analysis scripts (R, Python, Stata, SPSS)
- Codebook or data dictionary
- Findings or results document
- Literature review or references list
- Ethics approval or consent forms

**Domain signals:**
- **Question** — what is being investigated
- **Method** — how data is collected
- **Data** — the raw evidence
- **Analysis** — how the data is processed
- **Findings** — what the analysis shows
- **Interpretation** — what the findings mean
- **Output** — the report, paper, or presentation

**What to check:**
- Is the research question stated explicitly?
- Is the methodology documented?
- Is raw data present or only processed/summarised data?
- Is the analysis reproducible from what is provided?
- Are findings clearly distinguished from interpretation?

---

## Business / Strategy

**Clear signals:**
- Strategy or strategic plan document
- Financial model or forecast (.xlsx with scenarios)
- OKR tracker or goal document
- Board presentation or investor deck
- Competitive analysis
- SWOT or similar framework document
- Roadmap (product, business, or technology)
- Stakeholder map
- Risk register

**Domain signals:**
- **Context** — market, competitive landscape, current state
- **Problem** — what needs to change and why
- **Options** — routes considered
- **Recommendation** — preferred path
- **Plan** — how to execute
- **Metrics** — how success is measured

**Common problems:**
- Financial model present but assumptions not documented
- Recommendation present but options analysis absent (was there actually a choice?)
- Roadmap present but no resourcing or ownership
- Strategy document last updated when circumstances have clearly changed

---

## Product

**Clear signals:**
- Product Requirements Document (PRD) or product spec
- User stories or job stories
- Wireframes or mockups
- User research documents
- Backlog file (Jira export, linear export, spreadsheet)
- Acceptance criteria
- Technical architecture document
- Roadmap

**Domain signals:**
- **Discovery** — problem definition, user research
- **Definition** — requirements, spec, acceptance criteria
- **Design** — wireframes, mockups, prototypes
- **Development** — technical spec, architecture, implementation
- **Testing** — QA plan, test cases
- **Launch** — release plan, go-to-market

**What to check:**
- Is there a stated problem the product solves?
- Are user needs documented separately from feature lists?
- Do wireframes match requirements?
- Is there a definition of done?

---

## Event / Production

**Clear signals:**
- Run-of-show or show order document
- Venue brief or site plan
- Vendor or supplier list
- Budget tracker
- Schedule or timeline
- Script or presenter notes
- Contact sheet
- Technical specification (AV, lighting, staging)
- Guest list or registration management

**Domain signals:**
- **Concept** — what the event is and why
- **Brief** — client or organisational requirements
- **Planning** — logistics, vendors, timeline
- **Production** — build, rehearsal, show
- **On-the-day** — run of show, team responsibilities
- **Post-event** — reporting, debrief, learnings

**Common problems:**
- Run-of-show present but not reconciled with the script
- Vendor list without confirmed bookings
- Budget without approvals or sign-off
- No emergency contact list or contingency plan

---

## Mixed Projects

When multiple types are present, analyse each domain separately, then address the integration.

**Step 1 — Classify all types present.**
Do not pick one and ignore the others. A product folder with a PRD, wireframes, a technical
spec, and a go-to-market plan is a coherent four-type mixed project. Name all four.

**Step 2 — Identify the lead type.**
Which type is the primary purpose? The others are supporting. A software project with a
marketing brief attached is a software project with marketing context — not a campaign.

**Step 3 — Map the interaction points.**
Where do the types connect? A campaign brief that commissions creative work that produces code
has three handoff points: brief→creative, creative→spec, spec→code. Each handoff is a domain
boundary. Each boundary is a risk point — information that needs to survive the transition.

**Step 4 — Diagnose integration quality.**
Are the types well-integrated or siloed? Signs of siloing: documents that do not reference
each other, inconsistent terminology across domains, deliverables in one domain that are not
reflected in another, conflicting version dates.

**Step 5 — Distinguish coherent mixed from dumped files.**
A coherent mixed project has a reason for each component and visible connections between them.
A storage dump has files from different projects, different clients, or different time periods
with no unifying purpose. They require different handling:

- Coherent mixed: analyse as described above
- Storage dump: declare what you are looking at, ask which project or subset to analyse,
  or if forced to proceed, analyse each apparent project cluster separately

**Common coherent mixed patterns:**

| Pattern | Types present | Notes |
|---|---|---|
| Product launch | Product + Marketing + Software | PRD + campaign brief + codebase |
| Consultancy engagement | Strategy + Research + Editorial | Deck + data + report |
| Brand refresh | Creative + Marketing + Editorial | Guidelines + campaign + copy |
| Agency pitch | Advertising + Creative + Strategy | Pitch deck + concepts + brief |
| Research publication | Research + Editorial + Data | Study + paper + datasets |

---

## Cross-reference

Project type identification feeds into:
- PHASE 2 node mapping — which node types are relevant
- PHASE 3 domain extraction — which domain patterns apply
- Section 8 — the "process guide" language adapts to project type
- `references/risk-audit-checklist.md` — non-code risk categories by type
