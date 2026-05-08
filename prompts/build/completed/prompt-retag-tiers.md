# Prompt Retag-Tiers — Migrate Source Tier References from 7-Tier to 8-Tier System

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code operating in `/Users/mnoth/source/research-missing-scientists/`. The repository recently restructured its source tier system from 7 tiers to 8 tiers. Your job is to update every tier reference in the repository to match the new system.

## Setup — Branch first

Before making any changes, create and switch to a working branch:
```
git checkout -b refactor/retag-tiers-8
```

## Hard Safety Rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Do not touch anything outside it.
- No sudo. No system-wide installs.
- No git push. No auth to any service.
- No contacting anyone. Research uses already-public material only.
- If unsure about a classification, log the ambiguity in `logs/research-log.md` and pick the most defensible option — do not leave references in the old numbering.

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt updates tier tags only. It does not change factual claims, confidence ratings, narratives, or analysis conclusions. It is a mechanical migration with one judgment call: splitting old Tier 2 into new Tier 3 (local/beat) vs. new Tier 4 (national mainstream).

## The Migration Map

| Old Tier | New Tier | Category |
|----------|----------|----------|
| Tier 1 | Tier 1 | Primary sources (unchanged) |
| Tier 2 (local/beat outlets) | **Tier 3** | Local and beat reporting |
| Tier 2 (national mainstream outlets) | **Tier 4** | National mainstream reporting |
| Tier 3 | Tier 5 | Tertiary / aggregator |
| Tier 4 | **Tier 2** | Named expert commentary (promoted) |
| Tier 5 | Tier 6 | Reporting relying on anonymous sources |
| Tier 6 | Tier 7 | Independent commentary |
| Tier 7 | Tier 8 | Foreign state-affiliated press |

## Outlet Classification Guide

Use this reference to decide how to split old Tier 2 sources. When in doubt, check whether the outlet has geographic or institutional proximity to the case it's covering.

### New Tier 3 — Local/beat reporting (geographic or institutional proximity)
- **New Mexico:** Albuquerque Journal, Santa Fe New Mexican, Taos News, Los Alamos Reporter, KOB 4, KRQE, Los Alamos Daily Post
- **Massachusetts:** Boston Globe, Boston.com, Boston 25 News, NBC Boston, WBUR
- **California:** CBS Los Angeles, Pasadena Now, MyNewsLA, KTLA, Fox 11 Los Angeles (when covering local LA cases)
- **Specialty/trade press:** Defense One, Aviation Week, Breaking Defense, C4ISRNet, SpaceNews, Physics Today, Nature, Science — when covering their subject-matter beat
- **Wire services used by local outlets:** AP and Reuters articles *published in local outlets* covering local cases may be Tier 3 if the reporter is locally based; otherwise Tier 4

### New Tier 4 — National mainstream reporting (no local proximity)
- **National TV/web:** CNN, CBS News (national), ABC News, NBC News (national), Fox News (national), NewsNation, MSNBC
- **National print/digital:** Washington Post, New York Times, The Hill, Newsweek, USA Today, Politico
- **International English-language:** BBC, The Guardian, IBTimes UK, Daily Mail
- **Wire services in national context:** AP/Reuters articles syndicated nationally without local reporting

### Edge cases — apply judgment
- **Fox 11 Los Angeles** covering a Los Angeles case → Tier 3. Fox News national covering the same case → Tier 4.
- **Dateline NBC** and similar magazine shows → Tier 4 (national), even if covering a local case.
- If an outlet doesn't appear in either list, determine proximity: Does the outlet serve the geographic area or institutional community of the case? If yes → Tier 3. If no → Tier 4.

## Execution Strategy

Work in this order to avoid cascading confusion:

### Phase 1 — Inventory (do not edit yet)
1. Search all files in `cases/`, `dossier.md`, `analysis/`, `appendices/`, and `logs/` for tier references. Common formats: `(T2)`, `(T3)`, `[T2]`, `Tier 2`, `Tier 3`, etc.
2. Build a working list: file, line, current tier tag, the source/outlet it refers to, and proposed new tier.
3. Log the full inventory in `logs/research-log.md` under a new dated entry.

### Phase 2 — Mechanical remaps (unambiguous)
These require no judgment — apply them first:
- Old `(T4)` / `Tier 4` (named expert commentary) → `(T2)` / `Tier 2`
- Old `(T3)` / `Tier 3` (aggregator) → `(T5)` / `Tier 5`
- Old `(T5)` / `Tier 5` (anonymous sources) → `(T6)` / `Tier 6`
- Old `(T6)` / `Tier 6` (independent commentary) → `(T7)` / `Tier 7`
- Old `(T7)` / `Tier 7` (foreign press) → `(T8)` / `Tier 8`

**CRITICAL ordering note:** To avoid double-remapping, process in this order:
1. T7 → T8
2. T6 → T7
3. T5 → T6
4. T3 → T5
5. T4 → T2
This ensures you never remap a tag that was already changed in a prior step.

### Phase 3 — Judgment calls (old Tier 2 split)
For every old `(T2)` / `Tier 2` reference:
1. Identify the specific outlet or source being tagged.
2. Classify it as Tier 3 (local/beat) or Tier 4 (national mainstream) using the guide above.
3. Update the tag.
4. If the classification is genuinely ambiguous, log it in `logs/research-log.md` with your reasoning and pick the more conservative (higher-numbered) tier.

### Phase 4 — Verify and commit
1. Search the entire repo for any remaining old-system tier references. Common traps:
   - Prose that says "Tier 2 sources" generically (update to "Tier 3/4 sources" or rewrite)
   - Section headers like "## Tier 2 reporting" (update)
   - Methodology text that describes the old system (should already be updated in README.md — verify)
2. Run a final grep for `(T2)` — every remaining T2 should now genuinely be named expert commentary. If any T2 tag refers to a news outlet, it was missed in Phase 3.
3. Log a summary in `logs/research-log.md`: total tags updated, breakdown by tier, any ambiguities flagged.
4. Commit all changes with message: `refactor: migrate source tiers from 7-tier to 8-tier system`

## Files to update
- `cases/*.md` (all 11 case files)
- `dossier.md`
- `analysis/*.md`
- `appendices/*.md`
- `logs/research-log.md` (add log entries, also update any existing tier references in log text)
- Any other `.md` file found to contain tier references

## Files NOT to update (already done)
- `README.md` — tier definitions already rewritten
- `CLAUDE.md` — already updated to reference Tier 1-8
- `prompts/research/README.md` — already updated
- This file (`prompts/build/prompt-retag-tiers.md`)

## Quality checks
- No file should contain both old-system and new-system tier tags after completion
- The total number of tier references should be roughly the same before and after (tags are remapped, not added or removed)
- Named expert commentary should be Tier 2 everywhere, not Tier 4
- No news outlet should be tagged Tier 2 — only individual experts speaking on the record
