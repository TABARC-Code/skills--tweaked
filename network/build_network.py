#!/usr/bin/env python3
"""Write and audit the skill network.

edges.json is the single source of truth. Each pair is written into BOTH
SKILL.md files, so every link has a reciprocal contract (link-matching, not
block presence). Dewey codes go at the end of each description.

    python3 network/build_network.py --write   # apply edges and Dewey codes
    python3 network/build_network.py --check   # audit; exit 1 on any failure
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
EDGES = os.path.join(ROOT, "network", "edges.json")
START, END = "<!-- relationships:start -->", "<!-- relationships:end -->"
BLOCK_RE = re.compile(re.escape(START) + r"(.*?)" + re.escape(END), re.S)
LINE_RE = re.compile(r"^- \*\*(?P<other>[\w-]+)\*\* · type: (?P<type>\w+) · source: (?P<source>\w+)$", re.M)
TYPE_WEIGHT = {"dependency": 3, "handoff": 2, "gate": 2, "chain": 2, "feedback": 2, "reference": 1}


def load():
    with open(EDGES, encoding="utf-8") as fh:
        return json.load(fh)


def skill_path(name):
    return os.path.join(SKILLS, name, "SKILL.md")


def all_names():
    return sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(SKILLS, "*", "SKILL.md")))


def block_for(name, pairs):
    lines = []
    for p in pairs:
        if name not in (p["a"], p["b"]):
            continue
        other = p["b"] if name == p["a"] else p["a"]
        mine = p["a_to_b"] if name == p["a"] else p["b_to_a"]
        theirs = p["b_to_a"] if name == p["a"] else p["a_to_b"]
        weight = TYPE_WEIGHT[p["type"]]
        lines.append(f"- **{other}** · type: {p['type']} · source: {p['source']}")
        lines.append(f"  - This skill (weight {weight}): {mine}")
        lines.append(f"  - {other}: {theirs}")
    body = "\n".join(lines) if lines else "No links declared yet. Add one in network/edges.json and rebuild."
    return (f"{START}\n## Relationships\n\n"
            "Bidirectional contracts. Generated from network/edges.json, so edit there, not here.\n\n"
            f"{body}\n{END}")


def add_dewey(text, code):
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines[:10]) if l.startswith("description:")]
    if len(idx) != 1:
        raise SystemExit("expected exactly one description line in frontmatter")
    if re.search(r"Dewey \d", lines[idx[0]]):
        return text
    raw = lines[idx[0]][len("description:"):].strip()
    if raw.startswith('"') or raw.startswith("'"):
        # Quoted scalar: re-emit as a double-quoted string so the Dewey code
        # stays inside the value and the YAML still parses.
        value = yaml.safe_load("description: " + raw)["description"]
        lines[idx[0]] = "description: " + json.dumps(value + f" Dewey {code}.", ensure_ascii=False)
    else:
        lines[idx[0]] = lines[idx[0]].rstrip() + f" Dewey {code}."
    return "\n".join(lines)


def write():
    data = load()
    pairs, dewey = data["pairs"], data["dewey"]
    names = all_names()
    missing = set(names) - set(dewey)
    if missing:
        raise SystemExit(f"no Dewey code for: {sorted(missing)}")
    for name in names:
        path = skill_path(name)
        text = add_dewey(open(path, encoding="utf-8").read(), dewey[name])
        block = block_for(name, pairs)
        if BLOCK_RE.search(text):
            text = BLOCK_RE.sub(lambda _m: block, text)
        else:
            text = text.rstrip("\n") + "\n\n" + block + "\n"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"wrote {len(names)} skills, {len(pairs)} pairs")


def check():
    data = load()
    pairs, dewey = data["pairs"], data["dewey"]
    failures = []
    names = all_names()
    declared = {}
    for name in names:
        text = open(skill_path(name), encoding="utf-8").read()
        fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        try:
            meta = yaml.safe_load(fm.group(1))
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{name}: frontmatter is not valid YAML ({exc})")
            continue
        desc = meta.get("description", "")
        if meta.get("name") != name:
            failures.append(f"{name}: name field does not match folder")
        if not re.search(r"Dewey \d{3}", desc):
            failures.append(f"{name}: description has no Dewey code")
        if len(desc) > 1024 or "<" in desc:
            failures.append(f"{name}: description over 1024 chars or has angle brackets")
        if name not in dewey:
            failures.append(f"{name}: no Dewey entry in edges.json")
        m = BLOCK_RE.search(text)
        if not m:
            failures.append(f"{name}: no relationships block")
            continue
        declared[name] = {(x["other"], x["type"]) for x in LINE_RE.finditer(m.group(1))}
        if block_for(name, pairs) != m.group(0):
            failures.append(f"{name}: relationships block is stale; run --write")
    for p in pairs:
        for end, other in ((p["a"], p["b"]), (p["b"], p["a"])):
            if end not in declared:
                failures.append(f"link {p['a']} <-> {p['b']}: skill {end} not found")
            elif (other, p["type"]) not in declared[end]:
                failures.append(f"link {p['a']} <-> {p['b']} ({p['type']}): {end} has no reciprocal contract")
    valid = {frozenset((p["a"], p["b"])) for p in pairs}
    for name, links in declared.items():
        for other, _t in links:
            if frozenset((name, other)) not in valid:
                failures.append(f"{name}: contract with {other} is not in edges.json")
    for f in failures:
        print("FAIL", f)
    print(f"{len(names)} skills, {len(pairs)} pairs, {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--write" in sys.argv:
        write()
    sys.exit(check())
