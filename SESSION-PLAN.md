# SESSION-PLAN.md

Living plan for upcoming research and dossier work. No agents have been fired yet — this captures the order, the agent strategy per phase, and the decisions that need to be made first.

Cross-reference: working notes in [scratch.txt](scratch.txt); canonical TODO in [TODO-research.md](TODO-research.md). When this plan and those files conflict, this plan wins for execution order; scratch/TODO win for scope detail.

---

## Standing rules (apply across all phases)

These are durable principles from memory. They override defaults whenever they conflict.

- **Global scope by default.** The dossier covers scientists in defense, advanced research, and related sensitive fields who die or go missing — *worldwide*. The existing 11 U.S. cases are historical artifact, not principled scope. Foreign cases get the same Tier 1–8 vetting and case schema. No "foreign" downgrade.
- **National mainstream = Tier 4 regardless of country.** Don't downweight foreign outlets. Local/beat (Tier 3) ranks above national mainstream from *any* country.
- **Conclusion neutrality.** Don't assert "no connection" or equivalent. Surface human-instinct patterns (factory-reset phones, walking out together, missing belongings, precursor statements) without verdicting either way. Note that human pattern-recognition is itself fallible.
- **Self-host primary sources.** Every external URL cited as a primary source gets a full-fidelity local archive (HTML + screenshot/PDF via Playwright or equivalent). Local copy = canonical reference; external URL = pointer.
- **Append, don't overwrite.** Original prose is preserved. Two patterns depending on edit type:
  - **Pure additions** (new info, no change to existing claims) → dated `## Update — YYYY-MM-DD` block under existing narrative.
  - **Revisions to existing prose** (rephrasing, retiering a source, fixing a confidence rating, applying conclusion-neutrality) → inline italic marker at end of the changed paragraph or section: `*(updated YYYY-MM-DD — [see GitHub for details](https://github.com/mattnoth/research-missing-scientists/commits/main/PATH/TO/FILE))*`. The GitHub link points to that file's commit history, so readers can diff the change without git knowledge.
  - **Top-of-file header** (any file substantively revised post-publication) → italic line under the H1 title: `*Last revised: YYYY-MM-DD — [see history](github-commit-history-url-for-this-file)*`.
  - Original prose is never deleted. If a change is substantive enough that rewording would lose the original meaning, move the original into a dated update block with annotation rather than overwriting in place.
- **Quote-provenance rule.** Tier 4+ claims must trace to higher-tier origin where possible.
- **Research log is append-only.** Every session writes to `logs/research-log.md` so work history is reproducible.
- **Multi-angle analysis.** Before settling on any framing, apply multiple lenses *in parallel*: (1) geographic clustering, (2) industry-insider voices (TikTok is the primary venue in 2026), (3) "weird" anomalous details, (4) mainstream-vs-grassroots asymmetries, (5) domain-specific research communities. Confirmation bias — locking in the rational framing early and filtering subsequent research through it — is the failure mode. If the user expects something to surface and it doesn't, that's a flag that scope is too narrow, not evidence of absence.
- **X-Files investigation posture.** Mulder-side hypotheses ("zero gravity is involved," "international government coordination," etc.) get the **same investigative rigor** as Scully-side. Every hypothesis: list evidence-for AND evidence-against, gather both with equal effort, never pre-tag speculative claims "Speculated" as a default while skeptical claims get "Reported"/"Confirmed" on thin evidence. Investigation ≠ endorsement; conclusion-neutrality still rules the writeup.

---

## Phase 0 — Decisions (resolved 2026-05-06)

All 7 resolved during planning session 1 (2026-05-06). No agents launched; this session was decisions-only.

| # | Decision | Resolved value |
|---|---|---|
| 1 | Timeline asymmetry — encode meaning or rebalance? | **Rebalance only.** Underlying issue is a rendering bug (alternation parks on one side); fix lives in mattnoth-dev, not research repo. |
| 2 | Opinion-in-hypothesis — specific hypothesis or full audit? | **Full audit.** Includes hunting for subjective characterizations from interested parties (family, employer, official spokespersons) stated as neutral fact — the wife/McCasland pattern is the concrete example. Plus X-Files balance check on H1–H9. |
| 3 | Worldwide discovery sweep — greenlight + initial language scope? | **Greenlit.** Languages: English + Russian + Chinese + French + German + Spanish + **Japanese + Korean**. Hebrew + Persian/Farsi held back for round 2. |
| 4 | Update-pass scope — breadth (a) or depth (b)? | **Hybrid depth-first.** Phase 6 Step A triage does double duty: source-weakness ranking *and* new-material density scan. Depth pass goes deep on the union of 2–3 cases. |
| 5 | Path B "to a point" — schema-extension guardrail | **Extend only when ≥2 cases share the new feature.** Each extension is documented (methodology section) and case files using the field link back, so readers understand why a structured field exists. |
| 6 | Acronym sweep — specific or general? | **General sweep.** First-use expansion per file; glossary completeness; cross-file consistency; **over-linking flag** (any acronym hyperlinked more than once per file). |
| 7 | Abstract on scroll up | **Deferred to mattnoth-dev** (and styling/UX work generally). |

### Standing rules captured during this session (added to memory)

- **Enrichment is primary value, not cleanup** — every named person/organization gets a Wikipedia/about-page link plus a primary-source link on first occurrence per file.
- **Verify-don't-trust on every clickable link** — every URL must be loaded and confirmed to resolve to the claimed target (no plausible-looking guesses); agents that propose URLs include a verification step.
- **Link discipline: once per page** — full name + link on first mention per file, bare acronym on subsequent mentions, no repeat links. New file = reset. Tooltips for in-page acronym hover are a website-side feature.
- **Archival workflow not capped by scratch.txt's spec** — Phase 3 surfaces richer options (link graphs, cross-referenced captures, evolution snapshots) before defaulting to the baseline.

**Already resolved (no decision needed):**
- Tom DeLonge link — both Wikipedia + actual WikiLeaks email URL. Action queued in Phase 1.
- Foreign-news equal footing — codified in standing rules above.
- Chinese scientists framing — folded into Phase 4 (worldwide sweep). They get full case-file treatment if surfaced.

---

## Phase 1 — Parallel cleanup audit (5 agents, read-only, all parallel)

No narrative writing → no voice coupling → safe to parallelize. Output is a consolidated findings doc; you approve before any edits.

| Agent | Type | Task |
|---|---|---|
| A | Explore | **Both-links sweep.** Tom DeLonge is the template (Wikipedia + WikiLeaks URL). Sweep narrative files for every public figure and primary-source document that needs both: (1) a "who/what is this" link (Wikipedia/about-page), and (2) a primary-source link. Initial candidates from survey: **John Podesta, Rep. Eric Burlison, Rep. James Comer, FBI Director Kash Patel, Karoline Leavitt, DOE Sec. Wright, Chris Swecker, Michio Kaku, Ross Coulthart, David Grusch**, plus institutional acronyms in glossary (AARO, TTSA, etc.). **Verify-don't-trust:** every proposed URL must be loaded and confirmed to resolve to the claimed target — no plausible-looking guesses. Wikipedia disambiguation pages, soft-404s, and stub redirects all count as verification failures. **Link discipline:** propose links *only* for the first occurrence per file; flag any file where the same person/org is currently linked multiple times so we can drop the redundant ones. Output: table of name → file:line → current state → proposed Wikipedia URL → proposed primary-source URL → **verification status (loaded? right page? final URL after redirect?)**. |
| B | Explore | **Acronym audit.** Scan glossary.json + case files + analysis files + dossier.md for: (1) first-use full expansion per file; (2) glossary completeness (every acronym used in narrative has a glossary entry); (3) cross-file consistency (same expansion); (4) **over-linking** — any acronym hyperlinked more than once per file. Output: per-file checklist with proposed fixes. |
| C | general-purpose (web) | **Broken-links pass.** Every URL in case files / appendices / glossary.json / data JSON. Categorize: alive / dead / 403 / soft-404 / redirected. For dead: Wayback availability check. Output: link health report. No edits. |
| D | Explore | **Foreign-source bias audit.** Walk existing tier assignments looking for foreign outlets scored below comparable U.S. outlets. Specifically: are foreign Tier-3 / Tier-4 outlets being held to a different standard? |
| E | Explore | **Alias-resolver scan.** glossary.json + data/diagram-data.json + case files → canonical-name → aliases map; flag dangling/duplicate references (JPL ↔ Jet Propulsion Laboratory, AFRL ↔ Air Force Research Laboratory, etc.). |

**Blockers:** none. Findings only, no edits.

**After Phase 1 returns:** consolidate; you approve specific edits; execute as a single low-risk commit pass (Tom DeLonge + other public-figure links, alias deduplication, acronym fixes, broken-link annotations).

---

## Phase 2 — Conclusion-neutrality + opinion audit (single agent, read-only)

Cannot parallelize. Voice consistency matters; the new neutrality rule needs coherent application.

| Agent | Type | Task |
|---|---|---|
| F | Plan or general-purpose | Scan analysis/hypotheses.md, analysis/connection-analysis.md, dossier.md, and all case files for: (a) opinion-tinted phrasing; (b) "definitely no connection" / "did not know each other" / equivalent absence-of-connection assertions; (c) **subjective characterizations from interested parties stated as neutral fact** — concrete pattern: "his wife characterizes it as brief, unpaid consulting for fiction writing" reads as fact rather than as one party's framing of a contested connection. Sweep for family / employer / official-spokesperson / friend / associate quotes that are presented as settled fact rather than attributed claim; flag for rewriting as "*Spouse X characterized the relationship as Y*" with attribution; (d) **hypothesis-balance check** — are H1–H9 split fairly between Scully-side (skeptical/rational) and Mulder-side (speculative/anomalous), or are Mulder-side hypotheses getting thinner investigative effort and faster downgrades to "Speculated"? Identify which Mulder hypotheses (zero-gravity research involvement, international cover-up coordination, UAP-disclosure adjacency, others) deserve more investigative weight. Output: candidates list with proposed neutral rewrites + hypothesis-rebalance proposals. **Does not edit.** |

You approve/edit candidates; single-pass commit.

**Blockers:** Phase 0.2.

---

## Phase 3 — Tooling: snapshot-source pipeline

Build the Playwright/headless-browser archive tooling **before** any deep research runs, so all new citations get archived at time of capture.

**Design scope:** the descriptions below are the *baseline* — Phase 3 should surface richer options before committing to a build. Worth considering: link-graph capture (snapshot the page *and* its linked references one hop out), evolution-over-time snapshots (re-capture quarterly to track changes), cross-referenced material harvesting (when an article cites three other sources, capture all four). Don't default to the minimum spec because it's what's written here.

- **Web pages — Playwright:** Script `scripts/snapshot-source.sh` (or `.py`). Input: URL. Output: raw HTML + linked assets + screenshot + PDF + extracted text + manifest (timestamp, source URL, http status, content hash). Stored under `appendices/primary-sources/<case>/snapshots/<slug>/`. Decide: Python (Playwright Python binding) or Node (Playwright npm). Python likely lower friction.
- **Video — yt-dlp + Whisper:** Script `scripts/snapshot-video.sh`. Input: TikTok / YouTube / Reddit-hosted video URL. Output: video file + auto-captions (yt-dlp) + Whisper transcript when no captions exist + thumbnail + manifest. Same directory layout as web pages.
- **Reddit threads — full-tree archive:** Script `scripts/snapshot-reddit.sh`. Input: thread URL. Output: full comment tree (including deleted/removed via Reveddit/Unddit/Wayback), thread metadata, manifest. Single archive captures the discussion as it stood at archive time.
- **Backfill pass:** run web/video/reddit snapshots against every external URL currently cited as primary source. Existing markdown archives (e.g., `wikileaks-podesta-email-3099.md`) get an HTML + screenshot + PDF companion in their case's `snapshots/` directory.
- **Integrate with Phase 1 Agent C output:** dead links from the broken-links report → try Wayback → snapshot the Wayback rendering locally.

**Agents:** none required for the build itself; one Explore agent may enumerate all current external primary-source URLs as input to the backfill pass.

**Blockers:** none.

---

## Phase 4 — Worldwide discovery sweep

This **is** the scope of the dossier. Existing 11 U.S. cases are one slice. Foreign-language coverage explicitly included.

| Thread | Priority | Focus |
|---|---|---|
| W-1 | **Critical** | **TikTok / YouTube / video creators — primary insider discourse venue.** Mainstream coverage is thin; insiders, family, adjacent voices aggregate on TikTok specifically. **Discovery is hybrid:** (a) agent uses `WebSearch site:tiktok.com <terms>` for indexed videos; (b) agent picks up TikTok URLs cross-posted on Reddit / blogs / X; (c) **user supplies curated URLs** from in-app TikTok hashtag search (#missingscientists, #losalamos, #UAP, #zerogravity, etc.) — the most reliable channel for niche content since TikTok blocks scraping. Snapshot-video pipeline (Phase 3) handles the rest. Treat creators as Tier 6–7 unless they cite primary sources, but **document what insiders are saying even when mainstream is silent — the asymmetry itself is a data point**. |
| W-2 | High | **Reddit deep dive:** topical subs (r/HighStrangeness, r/UFOs, r/UAP, r/conspiracy) + case-specific or institution-specific subs (r/LosAlamos, r/JPL, r/NewMexico, r/Aerospace, r/Huntsville, etc.). Walk full comment trees, including deleted/removed comments via Reveddit / Unddit / Wayback. Snapshot every thread (Phase 3 pipeline). |
| W-3 | High | Russian-language press: TASS, Kommersant, Meduza, regional outlets. Defense/aerospace scientist deaths or disappearances since 2022. |
| W-4 | High | Chinese-language press: Xinhua, People's Daily, regional outlets. Same scope. |
| W-5 | Medium | French / German / Spanish: Le Monde, Der Spiegel, El País, regional outlets. |
| W-6 | Medium | Japanese-language press: Asahi, Yomiuri, NHK, regional outlets. Defense/aerospace/research scientist deaths or disappearances. |
| W-7 | Medium | Korean-language press: Chosun, Hankyoreh, Yonhap, regional outlets. Same scope. |
| W-8 | Medium | English-language indie / Substack writers tracking similar patterns; aggregator lists ("scientists dying" compilations); Wayback for takedowns. Verify each lead independently — these are leads, not sources. |

**Across all W-* threads:** every lead is traced to its original primary source and tiered before any case-file work. Discovery layer, not authoritative.

**Output per agent:** candidate-case bundle (name, location, date, claimed circumstances, source links, language). No case files written. Findings consolidated; you triage which warrant full case-file builds.

**Blockers:** Phase 0.3 (sweep greenlight + language scope). Phase 3 tooling (so discoveries are snapshotted at the moment of capture).

---

## Phase 5 — Amy Eskridge case update (research-then-write)

| Agent | Type | Task |
|---|---|---|
| G | general-purpose (web) | Research Amy Eskridge update. Primary/court/local/beat sources first, national mainstream as Tier 4. **Specifically hunt for the "I would not commit suicide" precursor statement** — interviews, social posts, video, third-party reporting. Tier all sources. Eskridge is already in the dossier (`cases/eskridge.md`); this is a case-update, not a new file. Returns research bundle. **Does not write.** |

You + me update the case file from the bundle (schema discipline + conclusion-neutrality voice).

**Blockers:** Phase 2 (so update inherits the new neutrality voice). Phase 3 tooling (snapshot any new sources at capture).

---

## Phase 6 — Depth-first update on existing cases

Two-pass shape from earlier conversation. Triage first.

| Step | Agent(s) | Task |
|---|---|---|
| A | 1 × Explore | **Hybrid triage** (Phase 0.4 resolution): rank all 11 by source weakness *and* surface "what's new since last reviewed" across all 11 in a single pass. Output: two ranked lists — (1) source weakness (count Tier 4+ claims, count "Reported"/"Alleged" confidence ratings); (2) new-material density (substantive findings since last reviewed date). User picks 2–3 from the union for depth treatment. Surface scan only on the news side — depth happens in Step B/C. |
| B | 2–3 × general-purpose, parallel | Source-deepening pass on top-N (union from Step A). One agent per case. Higher-tier origin search per claim. Output: source-swap proposals. No narrative edits. |
| C | 2–3 × general-purpose, parallel | News-refresh pass on same top-N. One agent per case. New material → dated `## Update — YYYY-MM-DD` block drafts. |

You approve proposals before any commit.

**Blockers:** Phase 0.4. Phase 2 (neutrality voice). Phase 3 tooling.

---

## Phase 7 — Methodology adoption (conversation, no agents)

Documentation work, no research.

- Document mechanical-vs-prose split in `RUNBOOK.md`.
- Document Path B extension protocol + the "to a point" guardrail (Phase 0.5).
- Document Option C re-emission (`## Update — YYYY-MM-DD` block pattern) in `prompts/build/queued/prompt-004-update.md`.
- Document the self-host primary-source workflow + snapshot tooling in `RUNBOOK.md`.
- Apply Phase 1 Agent E's alias map to deduplicate glossary/diagram entries.

**Blockers:** Phase 0.5; Phase 1 Agent E output.

---

## Phase 9 — Geographic & domain clustering analysis (multi-angle lens application)

The case-by-case view misses cross-cutting patterns. This phase applies the multi-angle rule explicitly — slice the data by lenses other than "person."

### 9a. Geographic clustering

For every known location associated with a case (residence, employer, death/disappearance site, prior posts), build the cluster map:

- **Huntsville, AL** — Eskridge is in the dossier as a Huntsville case, but Huntsville itself is a major aerospace/defense hub (Redstone Arsenal, Marshall Space Flight Center, U.S. Space Command, dozens of defense contractors). The dossier currently does not analyze Huntsville as a regional hotbed. **Action:** scope a dedicated Huntsville pass — what other deaths / disappearances / scandals at Huntsville-based entities since 2022, who else worked there, what's the local-press / TikTok discourse?
- **Los Alamos** (LANL) — already heavy in the dossier, but cluster-analyze: how many LANL-affiliated incidents since 2022 vs. baseline?
- **Pasadena** (JPL / Caltech) — same.
- **Wright-Patterson** (AFRL).
- **Cambridge** (MIT, Lincoln Lab).
- Any location surfaced by the Phase 4 worldwide sweep.

Output: regional cluster map with case density per location, weighted against workforce density to identify *unusual* concentrations vs. baseline activity.

| Agent | Type | Task |
|---|---|---|
| H | general-purpose | Per-region research pass: scoped to one location, finds adjacent cases not yet in the dossier, surfaces local-press coverage and community discourse. |

### 9b. Domain clustering — antigravity / exotic propulsion / zero-gravity

The dossier currently treats antigravity as a "weak signal" attached to one case (Eskridge). That framing was decided early and never reopened. **Re-examine** as a research domain:

- What is the antigravity / zero-gravity / exotic-propulsion research community? Who are its public-facing figures (Podkletnov, Ning Li, Hal Puthoff, Eric Davis, others)?
- Which of the 11 dossier subjects have any documented connection to this domain — even tangential — that hasn't been mapped?
- What entities operate in this space (Institute for Exotic Science, HoloChron, EarthTech, Skinwalker Ranch–adjacent operations, TTSA, etc.)? Are any of these connected to dossier subjects or to each other?
- What's the relationship between this domain and the UAP-disclosure community already documented for McCasland?

| Agent | Type | Task |
|---|---|---|
| I | general-purpose | Antigravity / exotic propulsion domain map. Public-facing figures, research entities, institutional history, connections to dossier subjects. Output: domain context document plus a connections list. |

### 9c. Other domain lenses (if Phase 4 surfaces them)

If the worldwide sweep surfaces other clustering domains (specific weapons programs, specific intel-related fields, etc.), each gets the same treatment.

**Blockers:** Phase 4 worldwide sweep should ship first to feed candidates; Phase 2 (neutrality voice) for the writeup.

---

## Phase 8 — Pattern-recognition framing layer (single-thread)

Cross-case appendix that names the human-instinct patterns and surfaces them without verdicting:

- Factory-reset phones
- Walking out / leaving belongings
- Undisclosed cause of death
- **Precursor statements** (e.g., "I would not commit suicide" type comments made before death — Eskridge is one instance; sweep all 11 cases for others)

Lists which cases share each pattern. Includes the human-fallibility caveat (pattern-recognition is biased — this is partly why conspiracy theories exist; the dossier surfaces patterns, doesn't endorse interpretations).

- New file: `appendices/behavioral-patterns.md` *(or `analysis/behavioral-patterns.md` — decide based on whether this is descriptive cataloging or analytical interpretation)*.
- Cross-link from each affected case file.
- Single-threaded write for voice consistency.

**Blockers:** Phase 2 (voice). Phase 5 (may surface more precursor-statement examples).

---

## Phasing principle: discrete, independently runnable

Each phase is **standalone**. You can run Phase 1 today, walk away, and not touch Phase 4 for weeks. The plan tracks dependencies (the "Blockers" lines under each phase) but not sequencing pressure — there is no requirement to push through phases continuously. Sessions can be one phase at a time, or one *thread* of one phase (e.g., just W-1 Reddit deep-dive, leaving the foreign-press threads for another session).

The "Suggested execution order" below is one viable sequencing, not a mandate.

## Next-session execution order (revised 2026-05-06)

Session 1 was decisions-and-planning only (no agents). Subsequent sessions split into smaller, independently runnable units. Stop at any point; pick up next time.

| Session | Goal | Time | What happens |
|---|---|---|---|
| 1 ✅ | **Decisions + plan** | done | Walked through all 7 Phase 0 decisions; encoded them above; captured 4 new standing rules to memory; revised this plan to reflect the multi-session split. No agents, no research-content edits. |
| 2 | **Phase 1 audit** | ~1 hr | Launch Phase 1's 5 parallel read-only agents (A: both-links sweep with verify-don't-trust + first-occurrence-only discipline; B: acronym sweep with over-linking flag; C: broken-links pass; D: foreign-source bias audit; E: alias-resolver scan). Session ends when agents return findings. **No edits.** |
| 3 | **Cleanup commit** | ~45 min | **First**: `git tag pre-rebalance-2026-05-06` on current HEAD to preserve the pre-rebalance dossier — anyone can `git checkout pre-rebalance-2026-05-06` to recover. Then review Phase 1 findings, approve specific edits, single commit pass: enrichment links (DeLonge template + other public figures), first-occurrence-only discipline applied, acronym fixes, alias dedup, broken-link annotations, foreign-source retag where the audit flagged bias. **Apply the revision-marker convention** (standing rules, "Append, don't overwrite") on every file touched: top-of-file `*Last revised: YYYY-MM-DD*` line + inline `*(updated YYYY-MM-DD — see GitHub for details)*` markers where existing prose was reworded. Push the tag with `git push origin pre-rebalance-2026-05-06`. |
| 4 | **Phase 2 voice audit** | ~1 hr | Launch single neutrality + hypothesis-balance agent (read-only). Returns candidates list including subjective-characterization-as-fact flags. **No edits.** |
| 5 | **Voice commit** | ~45 min | Review Phase 2 candidates, approve rewrites, single commit. Confirms neutrality + X-Files posture across analysis layer. |
| 6–7 | **Phase 3 tooling build** | ~3–4 hr (likely 2 sessions) | Build snapshot pipelines: web (Playwright), video (yt-dlp + Whisper), Reddit (full-tree). **Surface richer-than-baseline options before committing to design.** Test on 3–5 known URLs. Document in RUNBOOK.md. **Unlocks every research phase after this.** |
| 8+ | **Research phases — pick by priority** | varies | After tooling lands, sessions can target one phase or one thread: Phase 4 W-1 (TikTok seed run), W-3 (Russian press), W-4 (Chinese press), W-6/W-7 (Japanese / Korean), Phase 5 (Eskridge update + Zero Gravity domain), Phase 6 (hybrid triage → depth pass on top 2–3), Phase 9 (Huntsville hotbed; antigravity domain map), Phase 8 (pattern appendix). Phase 7 (methodology docs incl. Path B extension protocol) interleaves whenever convenient. |

**Stop conditions per session:** session 2 ends when Phase 1 agents return; session 3 ends after the cleanup commit; session 4 ends after the voice-audit agent returns; session 5 ends after the voice commit; session 6/7 ends when tooling is tested + committed. Each is a clean handoff.

## Suggested execution order (full sequencing)

1. **Phase 0 decisions** — you, ~10 min
2. **Phase 1 cleanup audit** — 5 parallel agents, returns findings overnight
3. **Phase 2 neutrality audit** — 1 agent + your review, single commit
4. **Phase 3 snapshot tooling build** — interactive, ~1 session
5. **Phase 4 worldwide sweep** *or* **Phase 5 Amy Eskridge** — pick by urgency, both wait on Phase 3
6. **Phase 6 depth pass** on existing cases
7. **Phase 7 methodology docs** — when convenient
8. **Phase 8 pattern-recognition appendix** — last, after voice + Eskridge land

Phases 4, 5, 7, 8 can interleave once 0–3 are done.

---

## Out of this plan (website / mattnoth-dev side)

Belong in a separate session focused on the website repo:

- Tom DeLonge link rendering on the deployed site (after Phase 1 markdown edits, the website needs a rebuild)
- Timeline asymmetry visual fix (Phase 0.1 decision flows here)
- Abstract on scroll-up sticky behavior
- Other items under "Website — *" sections in `TODO-research.md`
