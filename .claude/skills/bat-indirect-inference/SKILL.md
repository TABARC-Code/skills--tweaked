---
name: bat-indirect-inference
description: "Analyse a problem by inference from indirect signal, the way a bat navigates in darkness: emit, listen for the return, build a map from the echoes. Use when you can't observe the thing directly and must reconstruct hidden structure from what comes back: feedback, weak signals, silence, resistance, timing, and the gap between what you expected to hear and what you did. Triggers on: opaque systems, incomplete information, \"what am I not being told\", reading a situation from indirect evidence, probing to learn, what the silence means, why the response was delayed, inferring intent from behaviour, due diligence on something opaque from the outside, reverse-engineering a black box. Complements slime-mold (decentralised optimisation), mycelium (metabolism), and spider (relational structure) by owning the epistemics of indirect detection: how to know what stays hidden. Dewey 153.15."
metadata:
  author: TABARC-Code
  author_url: https://github.com/TABARC-Code/
  version: 1.1.0
  dewey_code: '006.364'
  classification_label: AI analysis — inference and signal reconstruction
  status: production
  source_grounding:
    - Echolocators separate outgoing pulse from returning echo in time to avoid masking (Springer, Echolocation review).
    - Doppler shift compensation cancels self-motion, isolating prey-wing modulation (ScienceDirect, Neurobiology of echolocation).
    - Approach phase — pulse rate rises and duration shortens as the bat closes on target.
  bidirectional_links:
    - skill: slime-mold-analysis
      this_provides: technique for inferring hidden structure from weak signal
      this_consumes: emergent-coherence reading of decentralised systems
    - skill: mycelium-organism-analysis
      this_provides: technique for inferring the hidden body from partial signal
      this_consumes: surface-vs-organism distinction (the mushroom is not the fungus)
    - skill: spider-web-analyst
      external_one_way: true  # mature installed skill; we reference it, no back-link required
      this_provides: method for probing a closed system from outside
      this_consumes: relational map once enough structure is inferred to draw one
---

# Bat Indirect Inference

Author: TABARC-Code

Reconstruct what stays hidden the way a bat flies a dark cave: send a signal out, listen carefully to what returns, and build a map from the pattern of echoes, including the silences where an echo should have come back and didn't.

## The core method

A bat in darkness doesn't see the cave. It builds the cave from sound. It emits a call, waits for the echo, and reads the delay, the frequency shift, and the texture of what returns. From a stream of these it assembles a precise three-dimensional map of a space it has never seen, accurate enough to catch a moth mid-air.

The analytical translation isn't atmospheric. It's a method: when you can't observe something directly, you probe it, you read what comes back, and you treat the gaps in the return as information rather than noise.

This is the discipline for any opaque system. You don't have the inside view. You have only what the system emits in response to pressure, and what it conspicuously fails to emit. Both carry structure.

## Why this animal, specifically

Real echolocation has features that sharpen the metaphor beyond "listen carefully".

**Emit, then listen, never both at once.** Most echolocating bats can't broadcast and receive at the same time; the outgoing call would mask the faint returning echo. They separate pulse from echo in time. The lesson: you cannot probe and absorb simultaneously. Send the question, then go quiet and listen. People who talk through the answer hear nothing.

**Cancel your own motion.** Doppler-shift-compensating bats adjust their call frequency to cancel the frequency change caused by their own flight speed, isolating the tiny modulation that comes from a fluttering insect's wings. The lesson: subtract your own movement from the signal. Your assumptions, your speed of approach, your expectations all colour the return. Compensate for them or you'll mistake your own motion for the target's.

**Close faster, sample faster.** As a bat approaches prey, it emits pulses faster and shorter: the buzz before capture. The lesson: as you near the thing you're tracking, increase the sampling rate. Probe more often, in finer detail, the closer you get.

**Information leaks both ways.** A bat's call also tells the moth a bat is coming; some moths hear it and drop. The lesson: probing is not free or invisible. Every question you send reveals that you're asking, and a system that knows it's being probed can change its behaviour or go still.

Emit then listen, cancel your own motion, sample faster on approach, mind the leakage. Four mechanics, each a distinct analytical instruction.

## The move that makes this skill different

Spider maps structure it can see. Mycelium reads a living body. Slime mold traces flow. All three assume you have access to the system.

Bat assumes you don't. Its distinctive move is **treating absence as data**: reading the echo that didn't return, the question that went unanswered, the silence where a reaction was due. The other skills analyse what's present. This one specialises in inferring what's hidden from the shape of what's missing.

## The deployable prompt

> *Operate like a bat in darkness: don't depend only on what is visible. Send out questions, listen for the echoes, and build a map from the responses. Analyse the problem through feedback, weak signals, silence, resistance, timing, and environmental clues. Cancel your own motion first, subtracting what your assumptions and expectations are adding to the signal. Treat the echo that doesn't return as information, not noise: an unanswered question, a delayed response, a conspicuous silence all describe the shape of what you can't see. Find the invisible architecture behind the obvious facts, then explain what others are failing to detect and how confident you are in each inference.*

The framework below is the full method. The prompt is the fast reset.

## When to use this skill

Reach for bat analysis when:

**The interior is closed to you.** A competitor, a black-box vendor, a counterparty in a negotiation, an organisation you're doing due diligence on. You have no internal view, only what it emits.

**The information is deliberately incomplete.** Someone is managing what you're told. The gaps are structured, not random. What's withheld describes its own shape.

**Silence and delay carry meaning.** A question went unanswered. A response came suspiciously fast or slow. A reaction that should have happened didn't. These are echoes too.

**You're probing to learn.** You can send signals (ask a question, make an offer, float a proposal) and read the system from how it responds. Each probe returns structure.

**You're reverse-engineering a black box.** You can't open it, but you can feed it inputs and study outputs, and from enough input-output pairs reconstruct the mechanism.

If you can already see the structure, you don't need to infer it; use spider. If the thing is alive and regenerating, use mycelium. Bat is for when the lights are off and all you have is the return signal.

## Analytical framework

Run in order. State any skipped step and why; no silent skips.

### Step 1 — Establish what you can't see

Name the hidden structure precisely. What exactly is opaque? Intent, capability, internal state, true position, the mechanism inside the box? You can't infer well until you've said clearly what you're inferring.

### Step 2 — Cancel your own motion

Before reading any signal, subtract yourself. What are your assumptions, hopes, and expectations adding to the return? What would you *prefer* to hear, and how might that be colouring your read? A bat that doesn't compensate for its own flight mistakes its speed for the target's. Do this first, every time.

### Step 3 — Inventory the echoes you already have

What has the system already emitted, unprompted? Past behaviour, public statements, the pattern of what it does versus what it says, how it has reacted to pressure before. Build the first rough map from existing returns before sending new ones.

### Step 4 — Read the silences

This is the step the other skills don't have. What echo should have come back and didn't? What question went unanswered, what topic gets deflected, what reaction was conspicuously absent? Map the holes. The shape of what's missing often describes the hidden structure more precisely than what's present.

### Step 5 — Design probes

What signals can you send to make the system reveal structure? A question whose answer (or refusal) is diagnostic. An offer that tests a boundary. A small proposal that reveals priorities by how it's received. Design probes whose return is informative whichever way it comes back. Remember the leakage: each probe tells the system you're probing.

### Step 6 — Read delay, texture, and shift

For each return, read more than its content. How long did it take (delay encodes processing, reluctance, or coordination)? What's the texture (confident, hedged, rehearsed, improvised)? What shifted from what you expected (the Doppler reading, where the gap between predicted and actual is where the information concentrates)?

### Step 7 — Build the map and rate confidence

Assemble the inferred structure from all returns and silences. Then rate your confidence in each inference; this is the step people skip. A bat's map is provisional and constantly updated. Mark what you're fairly sure of, what's a working hypothesis, and what's a guess. Inference without calibrated confidence is just assertion in the dark.

### Step 8 — Identify the next probe

What single probe would most reduce your remaining uncertainty? Inference is iterative. End each pass by naming the question whose answer would sharpen the map most, and whether sending it is worth the leakage.

## Output structure

1. **The hidden structure**: what's opaque and what you're trying to infer.
2. **Self-cancellation**: what you've subtracted from the signal (your own assumptions and hopes).
3. **Existing echoes**: what the system has already emitted, and the rough first map.
4. **The silences**: what's conspicuously missing, and what its shape implies.
5. **Probe results**: what you sent, what came back, including delay and texture.
6. **Inferred map**: the reconstructed structure, with a confidence rating on each inference.
7. **Next probe**: the question that would most reduce uncertainty, and its leakage cost.

## Worked examples

### Example 1: Due diligence on an opaque counterparty

**Hidden structure:** whether a potential partner is as financially stable as they present.

**Self-cancellation:** you want this deal to work, which biases you toward hearing stability. Subtract that. Read the signal as if you were indifferent to the outcome.

**Existing echoes:** they've changed auditor twice in three years; their last three press releases emphasise "growth" and never mention margin; senior staff have quietly left. None of these is proof. Together they're a pattern of returns worth mapping.

**The silences:** you asked for management accounts and got a deflection about "commercial sensitivity". The accounts are the echo that didn't return. A stable company usually has nothing to hide here. The silence is shaped like a cash-flow problem.

**Probe:** offer a deal structure with a modest upfront and the rest on verified milestones. A stable partner negotiates the terms; a distressed one pushes hard for more upfront. How they receive it returns more than any statement.

**Inferred map:** moderate confidence they have a liquidity problem they're managing; low confidence on its severity; the milestone probe would sharpen both. Worth the leakage, because the probe also protects you if you're right.

### Example 2: Reading a negotiation you're being managed through

**Hidden structure:** the other side's real walk-away point and their actual priorities, both deliberately concealed behind a presented position.

**Self-cancellation:** you've anchored on the number you want and you're keen to close before quarter-end. Both bias you toward reading flexibility that may not be there. Subtract your deadline pressure from the read; it's your motion, not theirs.

**Existing echoes:** they opened high but conceded the first point fast, then went rigid on a second point that looked minor. The speed of the first concession and the rigidity on the small point are both returns. A negotiator who folds easily on price but won't move on timing is telling you which one actually binds them.

**The silences:** you asked twice about their internal approval process and got vague answers both times. The unanswered question describes its shape: if approval were simple, they'd have said so. The silence is shaped like a constraint they don't want you to price in.

**Probe:** float a version of the deal that gives them everything on the rigid point in exchange for movement on the one they conceded easily. How fast and how warmly they engage tells you whether you've read the real priority correctly.

**Inferred map:** moderate-to-high confidence that timing, not price, is their binding constraint; low confidence on why, which may be an internal deadline or a competing deal; the probe would sharpen both. The leakage cost is acceptable because the probe also advances the deal if the read is right.

### Example 3: When this skill is the wrong tool (negative case)

You have full access to a system's internals. It's your own team, your own codebase, your own documented process. You're asked to analyse why something is failing.

Reach for bat here and you'll manufacture mystery where there's none. You'll start "reading the silences" and "designing probes" for information you could simply go and look at. The whole apparatus of indirect inference is wasted effort when direct observation is available, and worse, it can make you distrust plain facts in favour of clever deductions.

The tell: if you can answer the question by looking directly, looking is better than inferring. Bat is expensive and uncertain by nature; it's a method for when direct observation is genuinely unavailable, not a more sophisticated alternative to it. If the lights are on, use your eyes. That's spider or mycelium, not this.

This earns its own example because indirect inference feels cleverer than direct observation, and that feeling tempts people to use it when they don't need to.

## Diagnostic questions

1. Can you observe the structure directly? Yes → use your eyes; spider or mycelium, not this.
2. Is the information deliberately or unavoidably incomplete? Yes → bat fits.
3. Do silences, delays, and non-responses carry meaning here? Yes → strong bat signal.
4. Can you send probes and read the returns? Yes → bat's method applies.
5. Are you reverse-engineering something from input-output behaviour? Yes → bat fits.
6. Is the system alive and regenerating rather than opaque? Yes → mycelium, not this.

## Common mistakes

**Inferring when you could observe.** The cardinal sin. If you can look, look. Inference is for genuine darkness.

**Not cancelling your own motion.** Reading the signal through your hopes. The single most common inference error: hearing what you wanted to hear and calling it analysis.

**Treating silence as nothing.** The absent echo is the skill's whole edge. A non-response is a response. Map it.

**Inference without confidence rating.** Presenting a guessed map with the same certainty as a well-probed one. Always mark how sure you are. A confident wrong map is worse than an honest uncertain one.

**Forgetting the leakage.** Probing tells the system it's being probed. Over-probe and you teach it to go still or to feed you a managed signal. Spend probes carefully.

## Relationship to sibling skills

**vs slime-mold-analysis.** Slime mold reads how a decentralised system builds coherence from flow. Bat reads how to reconstruct a system that stays closed to direct view. *Bidirectional: this provides the technique for inferring hidden structure from weak signal; slime mold provides the emergent-coherence reading once structure is known.*

**vs mycelium-organism-analysis.** Both share the instinct that the visible thing isn't the whole thing (the mushroom is not the fungus, the surface is not the cave). Mycelium then reads metabolism; bat reads the echo. *Bidirectional: this provides the inference technique for the hidden body; mycelium provides the surface-vs-organism distinction that tells you a hidden body is there.*

**vs spider-web-analyst.** Spider maps structure it can see and locates power within it. Bat is what you run *before* spider when you can't yet see the structure: inference first, then mapping. *Bidirectional: this provides the method for probing a closed system from outside; spider provides the relational map once enough is inferred to draw one.*

Bat is often the first skill in a chain: infer enough structure with bat, then hand the map to spider, mycelium, or slime mold for deeper analysis.

## Feedback loops

**Decay rule.** Every pass must retract something, not only add. No decay rate means every line ever grown is locked in.

**Positive:** when a probe returns exactly the structure you predicted, and later direct evidence confirms the inferred map, the method worked. Log which probe was diagnostic and reuse the pattern.

**Negative:** when the map turns out wrong, the diagnosis is specific. Did you fail to cancel your own motion (you heard what you hoped)? Did you misread a silence (absence meant something other than you thought)? Did you under-rate uncertainty (presented a guess as a finding)? Each failure names the step to tighten.

**Cross-fertilisation:** bat usually feeds another skill. Once you've inferred enough structure, ask whether spider, mycelium or slime mold should take the map and go deeper. Don't keep inferring once you can observe.


## Version history

v1.3.0. Retraction pass: version log compressed (2 prior entries removed; an author's record carries no load in a user's runtime).

<!-- relationships:start -->
## Relationships

Bidirectional contracts. Generated from network/edges.json, so edit there, not here.

- **mycelium-organism-analysis** · type: reference · source: body
  - This skill (weight 1): Complements the mycelium lens by owning inference from indirect signal.
  - mycelium-organism-analysis: Complements the bat lens by owning the metabolic view of the same system.
- **piv-investigate-issue** · type: reference · source: body
  - This skill (weight 1): Its indirect-signal lens is applied when a root-cause analysis stops short.
  - piv-investigate-issue: Uses the silence-and-signal lens when the evidence does not close the chain.
<!-- relationships:end -->
