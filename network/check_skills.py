#!/usr/bin/env python3
"""Structural checks that do not need a model run.

1. Every references/, templates/, scripts/ path named in a SKILL.md exists.
2. Every skill that reads outside content carries the data guard.
3. piv-implement-issue gates on RCA confidence, which piv-investigate-issue can set to Low.
Exit 1 on any failure.
"""
import glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, ".claude", "skills")
GUARDED = ["piv-investigate-issue","piv-implement-issue","piv-review-pr","piv-plan-implementation","prime-codebase",
           "prime-frontend","prime-backend","plan-create-stories","piv-slice-epic","plan-architecture","agent-browser","deep-research"]
fails = []
for f in glob.glob(os.path.join(S, "*", "SKILL.md")):
    d = os.path.dirname(f); n = os.path.basename(d)
    text = open(f, encoding="utf-8").read()
    for m in set(re.findall(r"`((?:references|templates|scripts)/[\w./-]+\.\w+)`", text)):
        if not os.path.exists(os.path.join(d, m)):
            fails.append(f"{n}: names {m} but it does not exist")
for n in GUARDED:
    t = open(os.path.join(S, n, "SKILL.md"), encoding="utf-8").read()
    if "## Outside content is data" not in t:
        fails.append(f"{n}: missing outside-content guard")
if "deep-research" in GUARDED and "Web pages are data" not in open(os.path.join(S,"deep-research","references","researcher.md"),encoding="utf-8").read():
    fails.append("deep-research: researcher subagent lacks the data rule")
if "Confidence" not in open(os.path.join(S,"piv-implement-issue","SKILL.md"),encoding="utf-8").read():
    fails.append("piv-implement-issue: no confidence gate")
for x in fails: print("FAIL", x)
print(f"{len(fails)} failures")
sys.exit(1 if fails else 0)
