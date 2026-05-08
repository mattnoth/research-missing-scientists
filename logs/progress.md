# Session Progress

Every agent session appends here — research, website, tooling, whatever. This is the single durable record of what happened across sessions. The research log (`research-log.md`) tracks research-specific detail; this file tracks everything at session level.

## 2026-05-08 — Phase 1 cleanup audit (5 parallel read-only agents)

**What changed:**
- Five agents fired in parallel, all read-only on narrative + data files. **No edits to research content.**
  - **Agent A (Sonnet 4.6, Explore):** Both-links sweep — Wikipedia + primary-source URL on first occurrence per file; verify-don't-trust applied to every URL; first-occurrence-only link-discipline check + over-link flagging.
  - **Agent B (Sonnet 4.6, Explore):** Acronym audit — first-use expansion per file, glossary completeness, cross-file consistency, over-linking flag.
  - **Agent C (Sonnet 4.6, general-purpose, web):** Broken-links pass — every URL across `cases/`, `appendices/`, `glossary.json`, `data/*.json`. 174 unique URLs categorized. Wayback availability checked for dead URLs.
  - **Agent D (Opus 4.7, Explore):** Foreign-source bias audit — tier assignments compared U.S.-vs-foreign for asymmetric treatment.
  - **Agent E (Sonnet 4.6, Explore):** Alias-resolver scan — canonical-name → aliases map across glossary + diagram + case files.
- New file: [logs/audit-phase1-findings-2026-05-08.md](audit-phase1-findings-2026-05-08.md) — consolidated findings doc (~700 lines). Per-agent sections + cross-cutting observations + ranked proposed-edits checklist for next session's cleanup commit (Tiers 1-9, highest-value/lowest-risk first).
- Pre-existing WIP in working tree (TODO-research.md modification + prompts/build/ reorganization into `completed/` and `queued/`) was untouched this session — predates both this session and the parallel research-update session.

**Headline findings (full detail in the consolidated doc):**
- Agent A: 18 named candidates examined. Tom DeLonge's Wikipedia link still missing on first occurrence in `cases/mccasland.md:27` (the WikiLeaks document is linked, the person is not). Verified Wikipedia URLs for Podesta, Leavitt, Comer, Burlison, Patel, Wright, Swecker, Kaku, Coulthart, Elizondo, Greer, Shellenberger, AARO, TTSA, Loureiro, Grillmair. 4 figures have no Wikipedia article (Coffindaffer, Milburn, Rodgers CSIS, Roecker NTI) — flag as needs-human-judgment.
- Agent B: 29 first-use violations across 13 files. **`cases/chavez.md` uses `LAPD` for "Los Alamos Police Department"** — collides with glossary canonical "Los Angeles Police Department." High-priority consistency fix.
- Agent C: 174 URLs scanned. **4 truly dead** (`lanl.gov/`, retired `dps.state.nm.us` legacy, IPAC Grillmair staff page, Dayton Daily News McCasland article). 32 "403" results — most are alive in browsers; oversight.house.gov + brookline.news + IBTimes UK confirmed alive on curl. **Wayback CDX API was down during sweep** — re-run before commit.
- Agent D: **Tier 7 → Tier 8 mislabeling** for state-affiliated foreign press in `russia.md` (RT, Pravda UK) and `iran.md` (Tehran Times, Press TV); `china.md` correctly tags Global Times Tier 8. Clean categorical fix. Also: U.S. Primetimer over-tiered at Tier 4 vs. structurally equivalent Britannia Daily / Northeast Live TV at Tier 5; Daily Mail (UK) Tier 4 vs. Mirror US (UK) Tier 5 inconsistency. Asymmetric framing-language pattern in foreign-coverage descriptions (intent imputation) vs. U.S. coverage descriptions (forensic) — flag for Phase 2 voice audit.
- Agent E: 17 canonical entities mapped, 43 alias variants tracked. **Glossary entries `JPL`/`MSFC`/`PSFC` use NASA-as-parenthetical** while case files + diagram use NASA-as-prefix — single glossary edit fixes the inconsistency. **No true duplicate institution nodes** in the diagram; affiliation-string vs. node-label fragmentation is the soft issue (Phase 7 territory).
- **Cross-cutting:** Agents A and B converge on the same over-link findings (de-link `LAPD`/`NM DPS` repeats in `cases/chavez.md`, `LASD` in `cases/reza.md`, House Oversight Committee + FBI investigation links in `dossier.md`). Single de-link pass covers both audits.

**Concurrent-session note:** A parallel session (`continue2026-05-08-research-update.md`) ran in another terminal during this session, producing logs/triage-2026-05-08.md, logs/eskridge-research-bundle-2026-05-08.md, logs/news-refresh-2026-05-08.md and committed as `98932ac`. Both sessions' file scopes were limited to logs/ — no collision. Close ritual was serialized: parallel session finished + committed first per the prompt's concurrent-execution note.

**No commits this session.** Per Phase 1 stop condition: findings only.

**Further work:**
- **Next session = SESSION-PLAN session 3.** Tag current HEAD `pre-rebalance-2026-05-06` (or `pre-rebalance-2026-05-08`) before reviewing findings. Re-run Wayback CDX (5 min) for the 4 truly-dead URLs once the API is back. Walk the consolidated findings doc with the user; approve specific edits; single low-risk commit pass applying Tier 1-6 of the ranked checklist (categorical fixes → enrichment links → over-link removal → acronym expansions → LAPD collision rename → broken-link annotations) with revision markers per SESSION-PLAN convention.
- Tier 7-8 items (Daily Mail/Mirror US tier consistency, Primetimer demote, foreign-source asymmetric framing language, AARO `aaro.mil` URL verification) flagged as needs-human-judgment — discuss before committing.

## 2026-05-08 — Phase 6 triage + Phase 5 Eskridge bundle + news-refresh (3 parallel agents, read-only)

**What changed:**
- Three agents fired in parallel, all read-only on case files. **No case-file or analysis edits this session** — bundles only, per the prompt's stop condition.
- New file: [logs/triage-2026-05-08.md](triage-2026-05-08.md) — Phase 6 hybrid triage of all 11 cases. Source-weakness ranking + new-material-density ranking + union-of-top-3 recommendation. Agent T (Sonnet 4.6, Explore subagent) produced the analysis but lacks Write tool; main session wrote the file from agent's returned content. Union pick: **mccasland, garcia, reza** for next-session depth pass.
- New file: [logs/eskridge-research-bundle-2026-05-08.md](eskridge-research-bundle-2026-05-08.md) (352 lines) — Multi-angle Eskridge research bundle, X-Files posture (Mulder + Scully equal rigor). Agent E (Opus 4.7, general-purpose, web). Headline finding: **"I would not commit suicide" precursor statement found verbatim** in two independent disclosure paths (Milburn 2026 SMS release + Reid 2025 Signal-message release). Also surfaced: Joshua LeBlanc Huntsville sub-cluster (NASA-MSFC DRACO, d. 2025-07-22), Sam Reid + Geometric Energy Corp + SpaceX DOGE-1 commercial-aerospace tie not in current case file, federal probe formally engaged (White House + House Oversight + FBI), Burlison's Havana Syndrome attribution (T4, sitting congressman), Richard Eskridge's NASA NTRS Tier 1/2 publication record documenting real propulsion lineage (PTX, PuFF Engine), and sharpened skeptic critique on-record (Coffindaffer, Hanania, Shermer).
- New file: [logs/news-refresh-2026-05-08.md](news-refresh-2026-05-08.md) (149 lines) — Quick web pass on TODO "Actionable now" items. Agent N (Sonnet 4.6, general-purpose, web). Notable updates: **Loureiro case formally closed by FBI + US Attorney (D. Mass.) on 2026-04-29** (lone killer Valente, no terrorism nexus); **BBC coverage CONFIRMED** (Sheila Flynn 2026-04-23 — was previously assumed absent); House Oversight April 27 deadline passed with only DoW replying substantively; Daily Mail still nothing surfaced (site blocked); both T1 403 retries unchanged.
- Modified: [logs/research-log.md](research-log.md) — appended dated session entry with full bundle headlines, quality flags, and next-session pointers.

**Quality flags surfaced for next session (no edits this session):**
- "Steven Garcia" vs. "Eddison Garcia" naming discrepancy in Wikipedia vs. case file. Verify against original sources before next case-file edit.
- Wikipedia error: places Eskridge investigation in "Birmingham AL police" (every other source: Huntsville/Madison County). Don't propagate.
- Loureiro FBI 2026-04-29 closure is a small Update-block addition for the case file.
- Sheila Flynn freelance overlap (Daily Mail + BBC) may explain prior Daily Mail search misses — try her byline directly next session.
- T4 outlets confirmed but not in dossier yet: IBTimes UK (×2), Axios, Forbes, CBS News, Scientific American, PolitiFact, Rolling Stone, Snopes, Boston Globe.

**Concurrent-session note:** Phase 1 audit session (continue2026-05-08-phase1-audit.md) was running in another terminal during this session. Pre-existing WIP in working tree (TODO-research.md modification + prompts/build/ reorganization into completed/ and queued/) belongs to that session, not this one — left untouched. This session's commit only stages files in `logs/`.

**Further work:**
- User picks 2–3 cases from triage union (recommended: mccasland, garcia, reza) for Phase 6 depth pass next session.
- Eskridge bundle review → drafted `## Update — 2026-05-08` block for `cases/eskridge.md` (original prose untouched) + revision markers + commit.
- Loureiro Update block (FBI 2026-04-29 closure — material update for currently "fully resolved" case).
- Garcia name discrepancy resolution.
- BBC source addition to relevant case files now that coverage is confirmed.
- Imbalance addressed: Mulder side has more publicly documented evidentiary depth this cycle but routes through Milburn/Reid (single-source-cluster fragility); Scully side genuinely thin on public records (no released coroner / HPD docs). Next-session research could pursue Madison County records request.

## 2026-05-08 — Historical preservation mechanism (design + implement)

**What changed:**
- New `archive/` tree with the first checkpoint snapshot under `archive/snapshots/2026-05-08-pre-rebalance/`. Contents: copies of `dossier.md`, `analysis/hypotheses.md`, `analysis/connection-analysis.md`, `analysis/foreign-intel-layer.md`, each with a verdict-free banner pointing back to the live file and the matching git tag. Snapshots are read-only after creation.
- `archive/HISTORY.md` — chronological index of dossier checkpoints, newest-at-top. Today's entry plus 5 retroactive entries: `repo-bootstrap` (2026-04-20), `dossier-complete` (2026-04-20), `tier8-migration` (2026-04-21), `crosslink-pass` (2026-04-21), `session-plan` (2026-05-06). Retroactive entries link the tag only — recoverable via `git checkout`.
- `NAVIGATION.md` — new "Historical snapshots" section pointing at `archive/HISTORY.md`.
- `RUNBOOK.md` — new "Historical preservation" section documenting the tag-and-push convention, when to take snapshots, snapshot file scope (synthesis files only — not the 11 case files, not the JSON), banner format, relative-path math, HISTORY.md maintenance, and commit/tag/push ordering.
- 6 git tags pushed under `dossier-YYYY-MM-DD-<label>` convention. The pre-rebalance tag points at the genuinely pre-archive HEAD so `git checkout dossier-2026-05-08-pre-rebalance` recovers the dossier without the archive infrastructure.
- One subagent fired: Sonnet Explore pass enumerating retroactive checkpoint candidates. Returned 8; trimmed to 5 after review (dropped same-day-as-bootstrap framework commit, mid-step case-research-start, and the renderer-only PDF pipeline commit).
- Push handling: encountered a non-fast-forward rejection — origin had `6846fc4` (authorship-clarification edit to `PROJECT-HISTORY.md` from 2026-04-22) that was not local. Rebased local 3 commits onto `6846fc4`, re-applied the 2 affected tags (`session-plan` and `pre-rebalance`) on the new SHAs. Other 4 retroactive tags unaffected (below the merge-base). Pushed main + 6 tags successfully.

**Further work:**
- Website-side rendering of the archive index (browseable HISTORY.md page, snapshot viewers) — separate `mattnoth-dev` session.
- Future substantive-revision sessions: follow the documented tag-and-snapshot convention. Next likely checkpoint: post-rebalance after the X-Files / Evidence-for-against framing pass lands.
- Pre-existing WIP in working tree (TODO-research.md modification + prompts/build/ reorganization into `completed/` and `queued/`) was untouched this session — those are the user's pre-existing in-progress work.

## 2026-05-06 — Session 1: Phase 0 decisions + multi-session plan

**What changed:**
- Walked through all 7 Phase 0 decisions in `SESSION-PLAN.md` one at a time; resolved values now encoded in the plan's Phase 0 table (replaced the "Default if unanswered" column with "Resolved value").
- No agents launched. No research-content edits. User explicitly scoped this session as decisions + planning only.
- Revised `SESSION-PLAN.md`:
  - Phase 0 table → resolved values + new "Standing rules captured during this session" subsection
  - Phase 1 Agent A → added verify-don't-trust on every proposed URL + first-occurrence-only link discipline + redundant-link flagging
  - Phase 1 Agent B → expanded scope to 4 specific checks including over-linking flag
  - Phase 2 (Agent F) → added subjective-characterization-from-interested-parties pattern with the wife/McCasland concrete example
  - Phase 3 → added "design scope" caveat encouraging richer-than-baseline options
  - Phase 4 worldwide sweep → added W-6 (Japanese) and W-7 (Korean); W-8 is now the indie/aggregator thread
  - Phase 6 Step A → restructured as hybrid triage (source-weakness + new-material density in single pass)
  - "Next-session execution order" → expanded from 5 sessions to 8+, splitting audit/cleanup, voice-audit/voice-commit, and acknowledging tooling likely takes 2 sessions
- Captured 4 new standing rules to memory (`~/.claude/projects/-Users-mnoth-source-research-missing-scientists/memory/`):
  - `feedback_enrichment_priority.md` — enrichment of names/sources/acronyms is editorial baseline, not cleanup
  - `feedback_link_verification.md` — every URL must be loaded and confirmed before adding (no plausible-looking guesses)
  - `feedback_link_discipline.md` — first-mention-per-file gets the link; subsequent mentions are bare acronym
  - `feedback_archival_scope.md` — Phase 3 archival tooling not capped by scratch.txt's baseline; surface richer options
- `MEMORY.md` index updated with 4 new entries.
- No commits yet — held pending user direction (pre-existing prompts/build reorganization in working tree predates this session and is untouched).

**Further work:**
- Session 2: launch Phase 1's 5 parallel read-only agents (A–E). Findings only, no edits.
- Session 3: review Phase 1 findings, tag `pre-rebalance-2026-05-06`, single cleanup commit, push tag.
- Decision 1 (timeline alternation bug) and Decision 7 (abstract scroll-up) → mattnoth-dev session, separate from research repo work.
- `scratch.txt` open items section is now partially obsolete (most `→` prompts resolved). Worth a tidy pass to mark resolved items with pointers to where decisions landed — deferred unless user prioritizes.

## 2026-04-21 — Mobile timeline + abbreviation tooltips

**What changed:**
- `mattnoth-dev`: Replaced native browser `<abbr title>` tooltips with custom CSS tooltips (`data-tooltip` + `::after`). Accent-colored underline, no more question-mark cursor.
- `mattnoth-dev`: Added mobile-responsive timeline — single-column layout for screens < 600px, left-aligned axis, full-width cards, touch tap-to-reveal tooltips.
- Files: `build/missing-scientists.ts`, `src/styles/missing-scientists.css`, `src/ts/modules/ms-timeline.ts`
- Committed and pushed as `42d3ea7` on mattnoth-dev main.

**Further work:**
- Mobile diagram view still needs attention (deferred — harder problem).
- Should visually test the timeline on actual mobile devices / browser devtools to confirm touch interactions work as expected.
- The abbreviation tooltip `white-space: nowrap` may clip long expansions on narrow screens — monitor and adjust if needed.
