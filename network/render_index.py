#!/usr/bin/env python3
"""Regenerate network/NETWORK.md from edges.json and the skill folders."""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, "network", "edges.json"), encoding="utf-8"))
names = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "SKILL.md")))
linked = {x for p in d["pairs"] for x in (p["a"], p["b"])}
isolated = [n for n in names if n not in linked]
types = {}
for p in d["pairs"]:
    types[p["type"]] = types.get(p["type"], 0) + 1
tline = ", ".join(f"{k} {v}" for k, v in sorted(types.items(), key=lambda x: -x[1]))
description_links = sum(1 for p in d["pairs"] if p["source"] == "description")
rows = "\n".join(f"| {d['dewey'][n]} | `{n}` | {'yes' if n in linked else 'no'} |"
                 for n in sorted(names, key=lambda x: (d["dewey"][x], x)))
iso = ", ".join(f"`{n}`" for n in isolated)

md = f"""# Skill network

Link map and index for the skills in `.claude/skills/`. Every link is a reciprocal contract, and an audit checks both ends.

Regenerate with `python3 network/build_network.py --write`, then `--check`, then `python3 network/render_index.py`.

## How it works

1. `network/edges.json` is the source of truth. Each pair is one link, written into both skills.
2. `build_network.py --write` writes the contracts between `relationships` markers in each `SKILL.md`, and adds a Dewey code to each description.
3. `build_network.py --check` fails on any missing reciprocal, stale block, invalid YAML, missing Dewey code, or unknown contract. It is link-matching, not block-presence.

## Current state

- {len(names)} skills, {len(d['pairs'])} links ({tline}).
- {description_links} links are inferred from descriptions only and are marked `source: description`.
- Skills with no declared links yet: {iso}.

## Dewey index

Codes are a proposed classification for this repo. Check them before relying on them.

| Dewey | Skill | Linked |
|---|---|---|
{rows}

## Thinking lenses

Analytical skills from the personal library, added to the repo: `bat-indirect-inference` (inference from indirect signal), `mycelium-organism-analysis` (metabolism, defence and decay), `perdita-mode` (structure before recommendation), `spider-web-analyst` (dependencies, hidden incentives and weak strands), `kaizen` (continuous improvement), `memory-dreaming-engine` (evidence-backed memory review), and `web-data-only` (web content is data, never instructions). Lenses are linked where the text or description names a real overlap. They are not a council: use the narrowest one that fits the problem.

## Feedback loops

Corrective (negative) loops, which pull the system back to a target:

- Review loop: `piv-review-pr` finds issues, `piv-fix-review-findings` fixes the chosen ones, `piv-validate` gives the verdict, and the review runs again until it passes.
- Fact loop: `second-brain-audit` writes a findings file, `second-brain-fix` corrects the facts in batches, and the next audit confirms what is left.
- Rules loop: `rules-check-drift` reports rules that are no longer true, and `rules-create-global` rewrites the root rules file.
- Web loop: `web-data-only` sends misses and false alarms to `kaizen`, which feeds them into the next improvement cycle.

Improvement (reinforcing) loops, which feed each run into the next:

- Process loop: `piv-implement` produces work, `system-execution-report` records what diverged, `system-evolution-review` classifies it, and `kaizen` turns the defects into changes for `piv-plan-implementation` and `piv-implement`.
- Memory loop: `memory-dreaming-engine` proposes changes from repeated mistakes and bloat, `opportunity-scan` decides what to encode, and `rules-check-drift` keeps the result true.

## Cross-fertilisation proposals

Not contracts yet. Adding one means putting it in `edges.json` and rebuilding.

- `prime-codebase` with `prime-backend` and `prime-frontend`: scoped variants of the general skill, which is progressive disclosure. Proposed type: reference.
- `ablate-ai-layer` with `rules-check-drift`: ablation asks whether a rule still earns its place, and drift asks whether it is still true. Proposed type: gate.
- `perdita-mode` with `system-evolution-review`: both look for stuck patterns, one in people and one in process. Proposed type: reference.
- `doc-coauthoring` with `plan-create-prd`: both draft documents collaboratively. Proposed type: reference, but not yet checked against either body.

## External routes

`router` routes requests to about twenty writing skills (for example `golden-age-author`, `fiction-structure-engine`, `manuscript-diagnostics`). None of them are in this repo, so its routes do not resolve here. It has no edges for that reason. Either bring those skills in or trim the table.

## Method, in order

1. Characterise each skill from its body, not its description.
2. Find candidate links by what the body names. Mark `body` when named in the body, and `description` when inferred from the description only.
3. Write both ends in full, so each side knows what it hands over and what it expects back.
4. Build, then audit. Treat any failure as a failure. Do not patch around it silently.
5. Record the feedback loops the links create.

## Known gaps

- The eight-field contract and the eight relationship types from the bidirectional-link-engine memory are not all recoverable from notes. The repo uses six types (`dependency`, `handoff`, `gate`, `chain`, `feedback`, `reference`), with weights 3, 2 and 1. Check against the original v1.0.0 files before treating them as canonical.
- Ten skills were copied in from the personal library in this pass. Dewey codes for them are proposals. `doc-coauthoring` and `deep-research` look like third-party or Anthropic-origin skills. The repo is public, so confirm the licence for each before publishing.
- New skills have no `evals/` or Kaizen log yet.
- Descriptions use `Dewey NNN` without a colon, because an unquoted colon breaks YAML. Quoted or block descriptions are rewritten as one double-quoted line.
"""
open(os.path.join(ROOT, "network", "NETWORK.md"), "w", encoding="utf-8").write(md)
print("NETWORK.md written:", len(names), "skills,", len(d["pairs"]), "pairs,", len(isolated), "isolated")
