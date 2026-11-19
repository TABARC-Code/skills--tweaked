# Human Systems Analysis

Extracted from Perdita Mode. Loaded during PHASE 2 (Lens 4) and PHASE 4 of Project X-Ray.
Lens 4 uses this for analysis. PHASE 4 uses this for Section 14 output.

Any project is the output of human decisions made under constraints. When something in the
project does not make sense as a rational choice, it almost always makes sense as a human
choice made under pressure. This reference gives you the tools to read those patterns.

---

## Core Principle

The project is evidence of decisions. The decisions had actors, incentives, and constraints.
Finding those is often more useful than cataloguing the symptoms.

A bug that has been present for two years is not just a bug. It is a governance signal.
A committed secret that was never rotated is not just a security risk. It is an incentive
signal. Two conflicting implementations of the same thing in the same repo is not just
technical debt. It is a trust or authority signal.

Read the project. Then read what the project implies about the people who made it.

---

## When This Reference Is Used

This reference is loaded during PHASE 2 Lens 4 and PHASE 4 of Project X-Ray.

Lens 4 runs as part of the parallel analysis on every full submission. It applies the
web-mapping methodology here to the project material at the same time as the structural,
semantic, and domain lenses. PHASE 4 then writes Section 14 if the Lens 4 synthesis
identifies tensions, influence nodes, or incentive signals that would materially change
what a new person does with the project.

PHASE 4 also runs on direct user request: "Why is it like this?" or equivalent.

The signals that make Section 14 worth writing:
- Governance gap — no clear owner for a critical element
- Incentive misalignment — person responsible for X was measured on Y
- Information gap — critical knowledge in no written form anywhere
- Trust deficit — parallel work, over-documentation, defensive language
- Long-standing problems nobody has fixed — an incentive signal, not just a code smell
- Two conflicting versions with neither deprecated — authority signal
- Accumulating placeholders — nobody felt responsible for the project's health

---

## Step 1 — Map the Web

Before making any claim about the human system, map what you can observe.

**Actors** — who has been involved?

Look for any evidence of human presence: authorship, style variation, version history implied
by file naming, named contacts, team references, client references. This works for any project
type — code commit patterns, document tracked-changes, campaign version folders, research
attribution headers.

Evidence to look for:
- Commit author patterns (if git history is available)
- Multiple coding styles in the same file (different people wrote different sections)
- Comments with initials, team names, or "ask [name]"
- File headers with author attribution
- TODO comments addressed to specific people

Even without git history, you can often infer multiple actors from inconsistent patterns.

**Incentives** — what did each actor appear to be optimising for?

Common technical incentive patterns:

| Code pattern | Likely incentive behind it |
|---|---|
| Features added rapidly, tests absent or minimal | Measured on shipping, not stability |
| Copy-pasted code across modules | Time pressure; refactoring not rewarded |
| Comments explaining why something is "temporary" from years ago | Shipping deadlines overriding cleanup |
| Multiple authentication implementations | Teams not talking to each other; or not trusting each other's code |
| Extensive logging in some areas, none in others | Different teams, or different eras of the same team |
| Perfect code in one module, chaos in another | One person who cared, surrounded by people who didn't stay |
| No deployment documentation | The person who knew how to deploy it left |

**Constraints** — what were they working within?

Look for:
- Very old dependency versions pinned with comments: suggests fear of breaking something that works
- Framework choices that seem outdated: suggests the decision was made at a different time
- Database schema that clearly predates the application logic: legacy constraint
- Workarounds in the code that suggest the underlying thing could not be changed: authority constraint
- Tests that are weirdly narrow: suggests the test suite was written to pass a specific audit

**Dependencies** — what does the system need in order to function?

Beyond technical dependencies, look for human dependencies:

- Undocumented configuration that requires someone to know it personally
- A setup process that requires access to systems not documented anywhere
- A module that can only be understood by reading git history
- An integration that is configured by environment variable with no example or documentation

These are not just missing docs. They are single points of human failure.

---

## Step 2 — Classify the Information

Before drawing conclusions, sort what you have.

| Category | Definition | Example |
|---|---|---|
| **Known** | Directly visible in the files. Equivalent to X-Ray's Observed. | Two auth implementations present |
| **Assumed** | Treated as known but not confirmed from files alone. | "They probably split teams" |
| **Implied** | Suggested by patterns but not stated. | "Someone was in a hurry here" |
| **Unknown** | Cannot be determined from the submission. | Who made the architectural decision |
| **Irrelevant** | Present but does not bear on the human system question. | Framework version used |

The most dangerous category is **Assumed** — assumptions wearing the clothes of facts.
Name them explicitly. Do not let them drive conclusions silently.

---

## Step 3 — Identify the Tensions

Find where forces are pulling against each other. This is where things broke down, and
where small interventions have large effects.

### Tension Types — Any Project

**Governance gap**
No clear owner for a critical component. Both teams think it's the other's responsibility.
Nobody documents it, nobody maintains it, nobody feels authorised to change it.
*Code signal: widely-imported module with commits from many different teams but no consistent
maintainer; or a service that appears in every architecture diagram but has no team label.*

**Incentive misalignment**
The team is measured on features shipped, not stability maintained. Fixing technical debt
is invisible in the incentive structure. Cutting corners is rational.
*Code signal: new features added regularly but the same bugs recur; tests deleted rather than
fixed; documentation always out of date; "temporary" comments that are years old.*

**Information gap**
Critical knowledge exists only in one person's head. The person may have left.
*Code signal: a project that cannot be run by a new team member without finding the specific
person who set it up; .env.example absent or wrong; no deployment documentation.*

**Trust deficit**
Two teams (or two eras of the same team) did not share code because they did not trust each
other's implementations, did not know the other existed, or could not agree on ownership.
*Code signal: two authentication libraries both imported; two database access layers; two
almost-identical utility modules in different folders.*

**Capacity overload**
One person or team is carrying too much. Quality drops inconsistently. Nothing gets fully finished.
*Code signal: a monolith doing six jobs; files that are very long with no clear decomposition;
uneven code quality within the same module.*

**Sequence lock**
Something needed to change first but never did, and everything downstream is now constrained.
*Code signal: old dependency pinned because upgrading it would require changing too many things;
migration files present but apparently not run; architecture that everyone knows is wrong but
nobody has authority to change.*

**Premature closure**
An early decision is now treated as fixed even though circumstances changed. "We can't change that."
*Code signal: a fundamental architectural choice (this will be a monolith; this will be the
data model) that no longer fits the current reality but is still load-bearing everywhere.*

**Urgency vs quality**
Time pressure repeatedly pushed the correct solution out in favour of the fast solution.
The fast solutions compounded.
*Code signal: copy-pasted code; TODO comments in critical paths; try/catch blocks that catch
everything and do nothing; tests that exist only to pass a deadline review.*

---

## Step 4 — Find the Influence Nodes

Every system has points where pressure concentrates. In any project, influence nodes are not always the
most complex components. Look for:

**The component everything imports** — often not the most sophisticated code in the repo,
but the one where a change ripples everywhere. Whoever controls or understands this has
disproportionate influence.

**The person whose knowledge is not written down** — identifiable by: the setup process
that requires finding them; the comment that says "ask [name]"; the module with no
documentation and no tests that clearly works but nobody knows why.

**The missing decision** — a fork in the architecture that was never resolved, so both
paths are still present. Every new developer has to navigate this informally.

**The bottleneck process** — the deployment step, the review requirement, the sign-off
process that slows everything else down and shapes every decision upstream of it.

**The unspoken constraint** — a technical, political, or organisational constraint that
nobody mentions in documentation but that is clearly shaping every architectural choice.
Often visible as: a workaround that is too elaborate to be accidental.

---

## Step 5 — Recommend a Precision Move

After mapping, identify the smallest intervention that would most improve the situation.

Prefer:
- Moves that create information (documenting what is unknown) over moves that commit resources
- Moves that reduce dependency concentration (split the monolith, document the setup) over moves that just fix symptoms
- Moves that clarify authority (name the owner, write the decision record) over moves that assume authority is already clear
- Reversible moves over irreversible ones

### Move Types — Any Project

**The right question** — identify the one thing, if answered, that would most change what
to do next. Often this is: "who is responsible for X?" or "why was this decision made?"
Do not document until you know the answer.

**The small test** — write a minimal test for the suspicious function before deciding
whether it works. Do not assume.

**The assumption check** — read the actual config file rather than inferring from the code
what the config probably contains.

**The written record** — the missing README, the missing .env.example, the missing
architecture decision record. Turns tribal knowledge into shared knowledge. Often the
highest-value single action in any inherited project.

**The ownership statement** — name explicitly who is responsible for what module or service.
Even a one-line comment or a CODEOWNERS file creates accountability where none existed.

**The boundary statement** — document what this component does and does not do. Prevents
the next person from adding to a monolith "because it's already here."

**The urgency check** — is the pressure to fix this immediately real, or manufactured?
Trace the deadline. Often the original pressure has passed.

**The staged decision** — instead of "fix all of this," decide now on the smallest thing
that reduces the most risk, then decide what to do next after that.

---

## Output Format for PHASE 4

When PHASE 4 runs, add a Section 14 to the report.

### Section 14: Human Systems Analysis

**What triggered this section:** [name the specific signal from Section 5, 9, or 10]

**Web map** — the actors, incentives, constraints, and dependencies visible in the code:
[Write this as prose, not a table. Name what you can observe. Label what you are inferring.]

**Tensions identified:**
[List using the taxonomy above. For each: name it, cite the code evidence, explain why it matters.]

**Influence nodes:**
[Name the specific nodes. Explain why they are load-bearing.]

**Information classification:**
| Known | Assumed | Implied | Unknown |
|---|---|---|---|

**Recommended precision move:**
[One move. Name the thread it pulls, the likely effect, the risk, and what it does not resolve.]

**What remains open:**
[Be explicit about what this analysis cannot determine from the code alone.]

---

## When Lens 4 Finds Nothing

Not every project has governance gaps, incentive misalignment, or a two-year-old bug nobody
fixed. Clean, well-owned, well-documented projects exist.

If Lens 4 finds no significant tensions, no influence node concentration, no incentive signals
worth naming — say so explicitly. "No significant human systems concerns identified from the
available material." That is a valid and useful finding. Do not manufacture tensions to fill
Section 14.

Section 14 still appears in the report in this case, with a brief note on what Lens 4
examined and what it did not find. An absent Section 14 is ambiguous — a reader cannot tell
whether no analysis was run or whether the analysis found nothing. A short "clean" Section 14
is unambiguous.

---

## Calibration Note

This analysis works with incomplete information. A project folder is not the full record of human decisions — it is what survived. Be appropriately uncertain about causes. The project can show you what happened. It often cannot show you why, or who decided it, or whether the decision
was conscious.

Name what you are inferring. Name what you cannot know.

A web with honest gaps is more useful than a web without them.
