---
name: mycelium-organism-analysis
description: "Analyse a problem as a living fungal organism: branching, metabolic, decentralised, and inseparable from its environment. Use when the visible issue is the fruiting body of a larger hidden system, when something is growing, decaying, defending itself, or quietly feeding on the conditions around it. Triggers on: systems that regrow after being cut, recurring problems that survive every fix, organisational dysfunction that protects itself, slow change, recovery after damage, what feeds a problem, what it decomposes, hidden dependencies beneath a surface symptom, \"we keep solving this and it keeps coming back\", \"the real problem is somewhere we're not looking\". Complements slime-mold (allocation and retraction), spider (relational power structure), and bat (inference from signal) by owning the metabolic lens: appetite, defence, reproduction, dormancy, decomposition. Dewey 579.5."
metadata:
  author: TABARC-Code
  author_url: https://github.com/TABARC-Code/
  version: 1.1.0
  dewey_code: '006.363'
  classification_label: AI analysis - living-systems and metabolic modelling
  status: production
  source_grounding:
    - Tlalka et al. / Boddy - nutrient translocation in mycelial networks.
    - Calcium-signalling study, Aspergillus nidulans - decentralised local stress response (PMC9991499).
    - Fukasawa / ISME - ecological memory and relocation decisions in fungal networks.
  bidirectional_links:
    - skill: slime-mold-analysis
      this_provides: metabolism, defence, reproduction, dormancy framing
      this_consumes: allocation-and-retraction logic (which path carries load)
    - skill: spider-web-analyst
      external_one_way: true  # mature installed skill; we reference it, no back-link required
      this_provides: living-system view of why a structure persists
      this_consumes: relational power-map when a deliberate centre exists
    - skill: bat-indirect-inference
      this_provides: surface-vs-organism distinction (the mushroom is not the fungus)
      this_consumes: technique for inferring hidden structure from weak signal
---

# Mycelium Organism Analysis

Author: TABARC-Code

Study a problem the way a mycologist studies a fungus: not as an object or an event, but as a living organism with appetite, boundaries, defences, and a hidden body far larger than the part you can see.

## The one idea that runs everything

The mushroom is not the organism. It's the fruiting body: the reproductive announcement of a vast network of hyphae threaded through the substrate out of sight. The visible problem is almost always the mushroom. The thing worth understanding is the mycelium underneath that produced it, fed it, and made its appearance inevitable.

Get this backwards and you spend your effort picking mushrooms while the organism that grows them is untouched. That's why recurring problems recur. You keep removing the fruiting body and the network keeps making new ones.

## Why this organism, specifically

Fungal mycelium has properties that are genuinely useful as an analytical lens, and they're grounded in real biology rather than the lazy "wood-wide-web magic" version.

It's **decentralised**. There's no command node. A study visualising calcium signalling in *Aspergillus nidulans* found the network responds to local stress with local signalling, producing decentralised responses rather than centralised ones. Each part reacts to its own conditions.

It **translocates**. Mycelial networks move carbon, nitrogen and water across considerable distances to wherever they're needed, equilibrating imbalances between distant regions. Nutrient flow and defence signals propagate long-distance along the hyphae, and in some species the direction of flow reverses every few hours.

It **decomposes and converts**. Fungi secrete enzymes that break down dead material in the environment, then absorb it. Decomposition isn't destruction here; it's how the organism turns waste into its own structure. What looks like rot is feeding.

It **defends**. When one part is attacked by a fungivore, a defence response propagates to parts not yet under attack, saving vital regions ahead of the threat.

It **remembers**. Relocation studies show fungal networks carrying a memory of growth direction, regrowing preferentially on the side that previously faced a resource. The organism's history shapes its present behaviour.

Decentralised, translocating, decomposing, defending, remembering. Those five are the analytical engine. The rest of this skill is how to use them.

## The move that makes this skill different

Slime mold prunes. Spider maps power. Bat infers structure. This skill does something none of them do: it treats the problem as **alive and self-sustaining**: something with an appetite that must be fed, defences that fire when threatened, and a reproductive strategy that replaces whatever you remove.

The distinctive question is: *what is feeding this, and what would it take to starve it?* Not how to fight the symptom, but how to change the conditions the organism depends on for survival.

## The deployable prompt

> *Operate like a fungal organism: branching, adaptive, metabolic, and inseparable from its environment. Don't treat the problem as a symptom or an isolated event; study it as a living system with structure, appetite, boundaries, growth zones, defence mechanisms, reproductive strategies, and conditions for survival. Trace how it feeds, spreads, repairs, competes, cooperates, decomposes obstacles, absorbs value, and responds to pressure. Identify the nutrients, the barriers, the weak tissues, the fertile zones, the dormant sections, and the points where growth either accelerates or collapses. Then explain the organism's internal logic, its relationship with the surrounding environment, its vulnerabilities, its likely next phase of growth, and what most people miss because they separate the visible form from the living system that sustains it.*

The framework below is for the full analysis. The prompt above is the fast reset.

## When to use this skill

Reach for mycelium analysis when:

**The visible problem is clearly just the visible problem.** An organisation has had the same argument for three years and solved it five times without it staying solved. A product keeps failing at the same stage despite new teams, new budgets, new approaches. Something underneath is regrowing the mushroom.

**Something regrows after being cut.** You removed it and it came back. That's the signature of an organism, not an event. Events don't regenerate.

**The system is decomposing something.** A team is quietly running on the breakdown of trust, goodwill, or institutional memory. Something is being consumed to feed something else.

**You need to understand persistence, not structure.** Spider tells you who holds power. This tells you why the whole thing stays alive and what it's living on.

**Recovery and regeneration matter.** After damage, what regrows first, what stays dormant, what conditions trigger reactivation.

If the system has a clear controller deliberately steering it, that's spider. If the useful move is pruning a network down to load-bearing paths, that's slime mold. Mycelium is for when the thing is *alive* and you need to know what sustains it.

## Analytical framework

Run in order. State any skipped step and why; no silent skips.

### Step 1 - Separate the mushroom from the organism

What's the visible fruiting body (the symptom, the event, the complaint) and what's the hidden mycelium (the living system that produces it)? Name both. If you can't find the organism beneath the mushroom, you may have an event, not a fungus, so consider whether this is the right skill.

### Step 2 - Map the substrate

A fungus is inseparable from what it grows in. What's the environment: the physical, social, economic, emotional, political and historical conditions the organism lives inside? Explain how the substrate makes this organism possible. Change the substrate and you change the organism.

### Step 3 - Identify the nutrients

What feeds it? Money, attention, time, fear, novelty, convenience, status, secrecy, dependency, scarcity, conflict, routine, permission. Separate the essential nutrients from the incidental ones. The essential nutrient is the one that, removed, starves the organism.

### Step 4 - Trace translocation

What moves across the system to where it's needed? Where is value, energy, or effort being carried from a rich region to a growing one? What's being equilibrated, and what imbalance would the organism move to correct?

### Step 5 - Find the decomposition

What is the organism breaking down and absorbing? What dead or waste material is being converted into structure? And the sharp question: what's being decomposed that shouldn't be (trust, goodwill, a person, a budget, a culture) and fed into the organism's growth?

### Step 6 - Locate the defences

Every living system protects itself. Look for denial, bureaucracy, silence, gatekeeping, protective narratives, immune responses, the punishment of dissent, camouflage. When you threaten the organism, what propagates to defend the parts not yet under attack? The defence response is often the clearest proof you've found something alive.

### Step 7 - Read the reproductive strategy

How does the organism replace what you remove? Copying behaviour, training new participants, embedding rituals, normalising dysfunction, replicating patterns across personnel. This is why removing the mushroom fails: the network just fruits again. Find the reproduction and you find why your fixes don't hold.

### Step 8 - Detect dormancy

What appears inactive but is still alive? Postponed decisions, unresolved conflict, latent demand, suppressed creativity, technical debt, social debt, institutional memory. What conditions would reactivate it? Dormant tissue is the organism's reserve; it's why systems you thought dead come back.

### Step 9 - Identify the starve point and forecast

Where could the organism be redirected, weakened, or transformed by changing its conditions rather than attacking its body? What's the nutrient chokepoint? Then forecast: if conditions hold, what's the next phase of growth? And what single change to the substrate or nutrient supply would force the biggest reorganisation?

Rate the starve point. Naming the essential nutrient is a hypothesis, not a fact, until you've tested it. Mark how confident you are that the nutrient you've named is the essential one rather than an incidental one, because acting on the wrong nutrient wastes the intervention and teaches the organism nothing.

## Output structure

1. **Mushroom and organism**: the visible symptom and the living system beneath it.
2. **Substrate**: the conditions that make this organism possible.
3. **Nutrients**: what feeds it, essential separated from incidental.
4. **Translocation**: what's carried where, and what imbalance it corrects.
5. **Decomposition**: what's being broken down and fed into growth, including what shouldn't be.
6. **Defences**: how it protects itself and what its defence response reveals.
7. **Reproduction**: how it replaces what you remove, and why fixes don't hold.
8. **Dormancy**: what's inactive but alive, and what would reactivate it.
9. **Starve point and next phase**: where to change conditions, and the one change that reorganises the most.
10. **Confidence**: how sure you are that you've found the real organism and its essential nutrient, rather than a plausible-sounding story. Mark hypotheses as hypotheses.

## Worked examples

### Example 1: The dysfunction that survives every reorg

**Mushroom:** the recurring turf war between two departments that flares up every planning cycle.

**Organism:** a resource-allocation system where ambiguity about ownership is permanently advantageous to whoever exploits it. The argument is the fruiting body; the network is the incentive structure that rewards unclear boundaries.

**Substrate:** a budgeting process that funds whoever shouts loudest, plus a leadership that values visible conflict-resolution over invisible prevention.

**Nutrients:** the essential one is ambiguity. As long as ownership is unclear, the organism feeds. Remove the ambiguity (clear, enforced boundaries) and it starves. Everything else (personalities, specific disputes) is incidental.

**Decomposition:** it's slowly breaking down trust between the teams and converting it into individual political capital for the people who profit from the fights.

**Defences:** every attempt to clarify ownership gets reframed as "we shouldn't be too rigid", "we value collaboration". That reframing is the immune response.

**Reproduction:** new managers are socialised into the fight within weeks. The pattern reproduces faster than people rotate. That's why five resolutions didn't hold.

**Starve point:** not another mediation. Change the substrate: make the budget process reward prevented conflict and clear ownership, and the organism loses its essential nutrient.

### Example 2: A codebase nobody can safely change

**Mushroom:** every attempt to modify one core module breaks something unrelated, and the team has learned to route around it rather than touch it.

**Organism:** an accumulation of implicit dependencies and undocumented assumptions that has grown through the codebase like hyphae through soil. The fragile module is the fruiting body; the network is years of decisions that quietly entangled themselves.

**Substrate:** delivery pressure that always rewarded the fast patch over the documented one, plus turnover that took the original authors and their unwritten knowledge with them.

**Nutrients:** the essential one is *avoidance*. Every time someone routes around the module instead of through it, the tangle is fed and the knowledge of how it works decays further. Remove the avoidance (force controlled, tested change with the lights on) and the organism stops growing.

**Decomposition:** it's slowly consuming the team's ability to estimate. Every task near the module takes unpredictably long, and that unpredictability is being absorbed as a permanent tax on planning.

**Defences:** the module is protected by fear. "Don't touch it, it's load-bearing and nobody understands it." That fear is the immune response, and it's effective: it keeps the organism alive by preventing the one thing that would dismantle it.

**Reproduction:** every new fragile area learns the same protection. The pattern (route around, don't document, fear the core) reproduces into each new tangle. That's why the problem spreads rather than staying contained.

**Starve point:** not a rewrite, which the fear will resist. Change the substrate by making controlled change to the module the only sanctioned path, with tests that make change safe, so avoidance stops being the rational choice.

**Confidence:** high that avoidance is the essential nutrient; moderate on whether a test harness alone is enough to overcome the fear, because the dormant knowledge loss may be too far gone to recover without the original authors.

### Example 3: When this skill is the wrong tool (negative case)

A one-off product launch failed. Sales were poor, the team is demoralised, leadership wants an analysis.

Reach for mycelium here and you'll invent an organism that isn't there. You'll hunt for what's "feeding" the failure, what it "decomposes", how it "reproduces", and you'll manufacture a living system out of a single event. The launch didn't regrow after being cut. It didn't defend itself. It happened once and stopped.

The tell: if nothing regenerates, nothing defends itself, and nothing reproduces, you don't have a fungus. You have an event. Analyse it as cause and effect, or use spider to map the decision structure that produced it. Forcing the metabolic lens onto a dead, one-off event produces vivid nonsense.

This earns its own example because the metabolic frame is seductive. It can make any problem *sound* alive. The discipline is refusing to animate things that aren't.

## Diagnostic questions

1. Does the problem regrow after you remove it? No > probably an event, not this skill.
2. Does it defend itself when threatened? Yes > strong mycelium signal.
3. Is there a clear controller steering it deliberately? Yes > spider, not this.
4. Is the useful move pruning to load-bearing paths? Yes > slime mold, not this.
5. Can you name what feeds it and what would starve it? Yes > mycelium fits.
6. Is something being decomposed and converted into the organism's growth? Yes > mycelium fits.

## Common mistakes

**Animating the inanimate.** The frame can make any problem sound alive. If nothing regrows, defends, or reproduces, it isn't a fungus. Refuse to manufacture an organism.

**Picking mushrooms.** Treating the visible symptom as the whole system. If your intervention removes the fruiting body without touching the network, expect it back.

**Romanticising decay.** Decomposition isn't automatically bad, and growth isn't automatically good. Some organisms should be cultivated, some contained, some starved. Don't force a positive ending.

**Ignoring the substrate.** The organism exists because the environment allows it. Attacking the organism while leaving the substrate intact rarely works. Change conditions, not just bodies.

**Confusing defence with malice.** A system protecting itself isn't necessarily run by bad actors. Immune responses are automatic. The denial and reframing may be nobody's deliberate plan.

**Naming a nutrient with false certainty.** The metabolic frame produces confident-sounding stories, and a confident wrong story is worse than an honest uncertain one. Until you've tested it, the essential nutrient you've named is a hypothesis. Say so.

## Relationship to sibling skills

**vs slime-mold-analysis.** Slime mold reads allocation and retraction: which path carries load, what to prune. This reads metabolism: what feeds the thing and what would starve it. Use slime mold when the network is carrying dead weight; use this when the problem is alive and regenerating. *Bidirectional: this provides the metabolic and defensive framing; slime mold provides the prune-to-load-bearing logic.*

**vs spider-web-analyst.** Spider maps relational structure and locates power, assuming a centre worth finding. This explains why a structure persists and what sustains it, assuming no centre is required for the thing to stay alive. *Bidirectional: this provides the living-system view of persistence; spider provides the power-map when a deliberate centre exists.*

**vs bat-indirect-inference.** Bat infers hidden structure from weak and indirect signal. This shares bat's core instinct (the visible thing is not the whole thing) but applies it metabolically: the mushroom is not the fungus. *Bidirectional: this provides the surface-vs-organism distinction; bat provides the technique for inferring the hidden body from partial signal.*

## Feedback loops

**Decay rule.** Every pass must retract something, not only add. No decay rate means every line ever grown is locked in.

**Positive:** when the analysis correctly identifies the essential nutrient and starving it actually kills the recurrence, the metabolic map was right. Log the case.

**Negative:** when starving the named nutrient doesn't stop the regrowth, you named the wrong nutrient or missed a dormant reserve. The miss tells you which: regrowth from an unexpected region means dormancy you didn't map; regrowth from the same region means the nutrient wasn't actually essential.

**Cross-fertilisation:** before starting, ask whether slime mold, spider or bat owns part of this. A problem can have a living core (mycelium) wrapped in a power structure (spider). Run both.

**Where this sits in the chain.** If the system is opaque, bat comes first to infer the hidden body, then this skill reads its metabolism. If the useful move turns out to be pruning a network to load-bearing paths rather than starving an appetite, hand off to slime mold. If a deliberate controller is steering, spider owns that; this skill explains only what stays alive on its own.


## Version history

v1.3.0. Retraction pass: version log compressed (2 prior entries removed; an author's record carries no load in a user's runtime).

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **bat-indirect-inference** · type: reference · source: body
  - This skill (weight 1): Complements the bat lens by owning the metabolic view of the same system.
  - bat-indirect-inference: Complements the mycelium lens by owning inference from indirect signal.
- **piv-investigate-issue** · type: reference · source: body
  - This skill (weight 1): Its dormancy and regrowth lens is applied to recurring root-cause analyses.
  - piv-investigate-issue: Checks recurring issues for a cause that the earlier fix did not reach.
<!-- relationships:end -->
