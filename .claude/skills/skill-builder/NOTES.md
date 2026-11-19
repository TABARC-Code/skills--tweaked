# Notes

**Author:** TABARC-Code

- Tightened the repo into a five-part skill builder.
- Added Skill Creator as the practical build/test/improve/package layer.
- Kept the chunky Skill Creator source in references so the main skill file does not become a wall with YAML on top.
- Added the eval agents, scripts, schemas, and review assets from the uploaded Skill Creator bundle.
- Updated the relationship map so Skill Creator has proper reciprocal links instead of vague “also related” fluff.
- Added usage and worked-example files so the system has fuel, not just an engine on a bench.

- Fixed the small relationship-contract cleanup and added Dewey-style skill classification for future listing.
- Added TABARC-Code author metadata and repo link across the main skill identity.
- Updated the manifest, README, relationship map, and classification index so the new shelf-mark system is actually findable.
- Added quiet Dewey tags to skill descriptions so future listings and linking can sort things without making a song and dance about it.

- Added a Change-Control Procedure (cascade prevention) to the main SKILL.md: define the change boundary, classify every touched component before editing, make the smallest valid change, stop and report instead of silently repairing anything outside scope. Registered it in the manifest under Change Discipline so it applies system-wide, not just to the entry file.

- Renamed the system from option-b-skill-builder to skill-builder across SKILL.md, CLASSIFICATION_INDEX.md, SKILL_MANIFEST.md, DESCRIPTION.md, and README.md.
- Fixed a real collision: all six sub-skills were shipping as standalone SKILL.md files with their own name/description frontmatter, meaning they could auto-trigger independently instead of only through the router — and the bundled skill-creator sub-skill shared its name with an unrelated pre-existing skill-creator. Converted all six to SUBSKILL.md with no name/description frontmatter, added a router-only header note to each, and added a Sub-Skill References section to the main SKILL.md stating they are not independently installable. Updated the two stale SKILL.md path references in RELATIONSHIP_MAP.md to match.

## v2.3.1

No prior version was tracked anywhere in this package — starting the count here.

- Fixed two more leftover stale `SKILL.md` self-references missed in the previous pass: one in `SKILL_MANIFEST.md`'s Resource-Heavy Sub-Skill note, one in `skill-classification-engine/SUBSKILL.md`'s Current Repository Codes table (still said `option-b-skill-builder`).
- Made Dewey-style classification tagging unconditional: every skill created or changed now gets a quiet `Dewey: xxx.xxx.` suffix and metadata entry, not just ones judged to need future discovery. Removed the now-contradictory guardrail line in `skill-classification-engine/SUBSKILL.md` ("do not over-classify tiny helper files").
- Added `version: '2.3.1'` to `SKILL.md` metadata and a version line to `SKILL_MANIFEST.md` — no version field existed before this.
- Added `ROUTER_GATING_EVALS.md`: three qualitative test prompts that verify the sub-skills actually stay gated behind the router, which nothing previously tested for. Kept separate from `skill-creator/evals/evals.json` since that suite tests skill-creator's own behaviour, not router-level gating.

## v2.3.2

- The v2.3.1 rename pass caught every identity-file self-reference but missed six body-prose mentions of the old "Option B" name sitting inside `RELATIONSHIP_MAP.md` and the closing "Relationship Contracts" sections of five sub-skill files (`creative-exploration-engine`, `skill-handoff-bridge`, `structured-skill-engineering-system`, `relationship-contract-engine`, `skill-creator`). Same class of bug as the previous two passes — a rename that touched headers and titles but not the sentences describing the system in running text. Fixed all six; verified clean with a full-repo grep afterwards rather than trusting the file list from the last pass.
