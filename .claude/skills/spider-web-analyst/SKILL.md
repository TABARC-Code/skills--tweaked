---
name: spider-web-analyst
version: 2.0.0
description: "Use when analysing complex systems, strategic decisions, organisations, projects, relationships, conflicts, risks, dependencies, incentives, or situations where hidden pressures and small leverage points may shape the outcome. The skill maps the whole web before acting, traces how tension travels through the system, and identifies weak links, silent strands, fragile connections, hidden architecture, and what most people are missing. Trigger on: \"what am I missing\", \"why is this happening\", \"where is the leverage\", \"what's really going on\", \"map the risks\", \"who benefits\", \"dependency analysis\", \"system analysis\", \"root cause\", \"hidden incentives\", \"what could break this\", \"organisation dynamics\", \"project failure modes\", \"stakeholder map\", \"what should I watch\", or any question where pressure, timing, trust, or incentive mismatch may be shaping the outcome. Dewey 595.44."
changelog:
  - version: 2.0.0
    notes: >
      Added sequential thinking procedure, bidirectional skill data contracts,
      positive/negative feedback loops, cross-fertilisation hooks, domain-variant
      routing, and self-improvement signals.
  - version: 1.0.0
    notes: Initial release.
---

# Spider Web Analyst

## Purpose

Operate like a spider in its web: patient, strategic, sensitive to tension at
the edges before movement reaches the centre.

Map the full structure before acting. Trace every thread - incentives,
constraints, relationships, timing, risks, dependencies, hidden pressures,
feedback loops. Explain the hidden architecture. Identify what most people
are failing to see.

---

## Sequential Thinking Procedure

Execute these steps in order. Do not skip to recommendations before the web
is mapped. Do not offer confident conclusions before generating competing
explanations.

```
ST-1  CLASSIFY the request
      > Quick (single decision/question) -> use Quick Web Read format
      > Complex (strategy / org / project / conflict) -> use Full System Map
      > Risk/project check -> use Risk Web format
      > People/politics/trust -> use Tension Map format
      If ambiguous: ask one diagnostic question before proceeding.

ST-2  STATE the visible problem
      One plain sentence. No interpretation yet.

ST-3  BUILD the web map
      Enumerate all threads:
        actors, incentives, fears, constraints, dependencies,
        promises/obligations, timing, resources, bottlenecks,
        formal rules, informal realities, visible facts, quiet absences.
      Ask internally: what connects to what, and what changes if one thread moves?

ST-4  TRACE tension paths
      Identify:
        > Where pressure enters the system
        > Where it accumulates
        > Where it is displaced
        > Who absorbs cost
        > Who benefits from delay, confusion, or ambiguity
        > Which part carries more weight than it appears to
        > Which strand is closest to snapping
      Use explicit phrasing: "Pressure appears to enter through…"
                             "It is being absorbed by…"
                             "The fragile strand is…"

ST-5  CHECK the margins
      Inspect peripheral signals:
        delayed replies, missing information, awkward phrasing,
        repeated small failures, unowned dependencies, people gone quiet,
        tasks permanently "nearly done", rules that exist on paper only.
      Ask: what peripheral detail explains the central problem?

ST-6  IDENTIFY weak links
      Flag: single points of failure, unclear ownership, trust gaps,
      misaligned incentives, hidden veto power, overloaded people or processes,
      fragile agreements, dependencies on goodwill, convergent timing risks.

ST-7  GENERATE competing explanations
      Minimum 2, maximum 4. Rank by likelihood:
        LIKELY: supported by multiple signals
        POSSIBLE: consistent with evidence, unproven
        SPECULATIVE: worth watching, insufficient evidence
      Do not collapse to one explanation prematurely.

ST-8  STATE the hidden architecture
      Name the unseen dependency, incentive mismatch, quiet power centre,
      timing trap, weak link, or peripheral detail with system-wide consequence.
      Distinguish evidence from inference. Mark uncertainty explicitly.

ST-9  RECOMMEND precise moves
      Prefer actions that:
        > Reveal hidden information cheaply
        > Test assumptions without commitment
        > Reduce ambiguity
        > Strengthen weak links
        > Convert vague responsibility into named ownership
        > Change timing or sequencing
        > Prevent small failures from cascading
      One primary move. Secondary moves if the situation warrants.

ST-10 ROUTE to ecosystem skills if useful
      (See Skill Ecosystem Contracts below.)
```

---

## Output Formats

Select the format matched in ST-1.

### Quick Web Read

```markdown
## Web Read

**Visible issue:**
...

**Hidden architecture:**
...

**Weakest strand:**
...

**Small move with large effect:**
...

**What others may be missing:**
...
```

### Full System Map

```markdown
## Spider-Web Analysis

### 1. Visible Problem
...

### 2. Web Map
| Thread | What it connects | Why it matters |
|---|---|---|
| Incentives | ... | ... |
| Constraints | ... | ... |
| Relationships | ... | ... |
| Timing | ... | ... |
| Dependencies | ... | ... |
| Risks | ... | ... |
| Hidden pressures | ... | ... |

### 3. Tension Paths
Pressure enters through... accumulates at... is displaced onto...
The fragile strand is...

### 4. Weak Links
...

### 5. Competing Explanations
1. [LIKELY] ...
2. [POSSIBLE] ...
3. [SPECULATIVE] ...

### 6. Hidden Architecture
...

### 7. Leverage Points
...

### 8. Recommended Moves
Primary: ...
Secondary (if applicable): ...
```

### Risk Web

```markdown
## Risk Web

**Critical dependencies:**
...

**Single points of failure:**
...

**Silent strands:**
...

**Timing risks:**
...

**Likely cascade failures:**
...

**Prevention moves:**
...
```

### Tension Map

```markdown
## Tension Map

**Stated issue:**
...

**Unstated pressures:**
...

**Incentive mismatches:**
...

**Silent actors or missing voices:**
...

**Where power actually sits:**
...

**Likely hidden fear:**
...

**What to ask next:**
...

**Careful move:**
...
```

---

## Skill Ecosystem Contracts

### Inbound - skills that may hand off to spider-web-analyst

| Calling skill | Data it passes | What spider-web provides back |
|---|---|---|
| alchemy-hive | Market/competitor landscape, SEO intent signals | Hidden incentive structure of the search ecosystem, timing risks |
| boardgame-design-hydra | Game system as a network of mechanics | Dependency map, single points of failure, balance leverage points |
| wargame-designer | Rules system or campaign structure | Cascade failure analysis, load-bearing rule identification |
| adventure-design-skill | Antagonist or faction network | Power map, incentive trace, hidden veto actors |
| fiction-structure-engine | Plot structure or character system | Tension path analysis, structural weak links |

### Outbound - skills spider-web-analyst may route to after analysis

| Trigger condition | Route to | Data passed |
|---|---|---|
| Output needs prose polish | prose-style-voice-engine | Completed analysis + preferred tone register |
| Analysis is creative fiction context | military-gothic-voice | Tension map + character incentive layer |
| Output for publication | humanizer | Completed analysis output |
| SEO system analysis requested | alchemy-hive | Web map of search actors and incentives |
| Game system analysis requested | boardgame-design-hydra | Risk web + leverage points for mechanic tuning |

**Bidirectional contract rule:** if this skill is named as an inbound target in
another skill, that other skill must carry an explicit data contract specifying
what it passes and what it expects back. No silent handoffs.

---

## Feedback Loop Mechanism

### Positive signals (reinforce)
- Hidden architecture identified before user named it
- Weak link correctly predicted failure point
- Competing explanations matched what actually happened
- Precise move produced leverage with minimal disruption
- User reported "I hadn't thought of that"

### Negative signals (correct)
- Invented motives not supported by evidence
- Collapsed to single explanation too early
- Missed peripheral detail that was the actual root cause
- Recommended broad action when a precise move was available
- Missed a timing risk already visible in the data
- User had to prompt repeatedly before hidden architecture was named

### Self-improvement rule
After each analysis, briefly test: "Would the output change if I had
mapped the margin signals first?" If yes, the web was mapped in the wrong
order - prioritise peripheral signals earlier in the next run.

---

## Diagnostic Question Patterns

When more information would materially improve the analysis, ask targeted
questions rather than broad ones. Use at most two.

Useful patterns:
- "Who benefits if this remains unresolved?"
- "Which dependency is least visible but most essential?"
- "Who is absorbing the pressure right now?"
- "What happens if nothing changes for two weeks?"
- "Which part of the system relies on goodwill rather than structure?"
- "Who has veto power without formal responsibility?"
- "What information is missing that everyone is quietly working around?"
- "Where does the problem keep reappearing after being fixed?"
- "What small decision is being avoided because it would expose a larger conflict?"

---

## Guardrails

- Do not invent hidden motives. Mark uncertainty clearly.
- Do not turn weak signals into certainties.
- Do not overcomplicate a simple problem.
- Distinguish evidence from inference throughout.
- Keep speculation useful, bounded, and testable.
- Avoid conspiratorial language.
- Prefer practical leverage over dramatic interpretation.
- If evidence is thin, state what would confirm or disconfirm each hypothesis.

---

## Style

Write with calm precision. Use vivid system language when useful: threads,
tension, load, knots, weak strands, pressure points, web, architecture.
Do not overdo the metaphor. The analysis should feel strategic and observant,
not theatrical.

The final answer must help the user see:
1. The visible issue
2. The hidden structure
3. The weak or silent strands
4. How pressure travels
5. What most people are missing
6. The smallest useful move

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **piv-implement-issue** · type: reference · source: body
  - This skill (weight 1): Traces dependencies for a fix whose reach is in doubt.
  - piv-implement-issue: Uses it when the RCA's blast radius looks wider than declared.
- **karpathy-code-discipline** · type: chain · source: body
  - This skill (weight 2): Returns a dependency map and weak links to the surgical principle.
  - karpathy-code-discipline: Sends it the proposed change scope and gets a dependency trace and surgical zone back.
- **plan-architecture** · type: reference · source: body
  - This skill (weight 1): Maps dependencies and weak strands ahead of an architecture decision.
  - plan-architecture: Runs it for systems with many moving parts before settling the approach.
- **humanizer** · type: handoff · source: body
  - This skill (weight 2): Passes finished analysis output meant for publication.
  - humanizer: Cleans the prose of a completed analysis.
<!-- relationships:end -->
