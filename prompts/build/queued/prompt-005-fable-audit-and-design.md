# Prompt 005 — Fable: Project Audit → Design-Strengthening Document

## Model & intent

One Fable 5 (`claude-fable-5`) session, run in **two phases in order**:

- **Phase 1 — Audit.** A fast, mechanical, whole-repo audit of the dossier's internal consistency, hygiene, and product-strength. This phase produces *the plan*: the findings that Phase 2 builds on.
- **Phase 2 — Design-strengthening document.** Building directly on the Phase 1 findings, write **one** design document that strengthens how the project works going forward. It must cover three named pillars: **(A) how we find new information (including video), (B) how we source the material, (C) missing scientists from other countries.**

No new web research. No new factual claims about any case. No new conclusions. This is a consistency + product-quality + methodology-design pass, not a research pass. Re-runnable: a second run refines the outputs in place rather than duplicating them.

## Non-interactive execution

May run via `claude -p` print mode with no stdin. Decide autonomously; do not ask questions. If something is genuinely ambiguous, log it under "Flagged for human judgment" (Phase 1) or as an explicit "Open decision" with a recommended default and trade-off (Phase 2), and proceed. Only exit non-zero on an unavoidable hard-safety-rule violation.

## Hard safety rules

- Working directory: `/Users/mnoth/source/research-missing-scientists/`. Read-only elsewhere.
- No new web research. No new claims about any case. No new conclusions, hypotheses, or reframings.
- **Never overwrite original narrative prose.** Prose/claim/tier/confidence corrections are *flagged*, not applied — except the pure mechanical fixes enumerated in Phase 1. When in doubt, recommend rather than edit.
- No `sudo`, no installs, no push, no contacting anyone. Preserve every source URL and citation.

## Read the ground rules first

Before auditing, read so the work measures against the repo's own standards: `CLAUDE.md`, `README.md` (the 8-tier taxonomy + confidence-rating definitions), `NAVIGATION.md`, `STATUS.md`, `TODO-research.md`, `logs/known-unknowns.md`, `logs/contradictions.md`, and one complete case (`cases/hicks.md`) as the schema reference.

## Capabilities already proven (ground truth — design Phase 2 to these; do not exceed)

Tested on the maintainer's machine 2026-07-05 and known to work. Treat anything beyond this list as "not yet verified — would require X."

- **YouTube caption pull:** `yt-dlp` retrieves native/auto captions directly — no login, no API key, instant, free.
- **Video without captions (incl. TikTok):** `yt-dlp -x` → audio → **faster-whisper** transcribes locally on CPU (`ffmpeg` present). Proven on a 5:19 TikTok → clean ~900-word transcript.
- **Programmatic discovery:** `yt-dlp "ytsearchN:<query>" --flat-playlist --print ...` returns YouTube search hits (id/title/channel/views) with **no browser, no API key, in any language** — a Chinese-language query surfaced Chinese/Taiwanese outlets (TVBS, ETTV, SETN, 中天) invisible to English search, including a distinct "US is scapegoating China" counter-narrative.
- **Creator enumeration:** a channel URL expands to that creator's full catalog via `yt-dlp`.
- **Built-in `WebSearch`** is US/English-biased; **`ytsearch` is not** — native-language queries are the unlock for foreign material.

**Known weak spots (state plainly, do not paper over):** TikTok has no clean *search* extractor (blind discovery leans on `WebSearch site:tiktok.com`, hashtag pages, cross-posted duplicates, creator enumeration; ingesting a *known* TikTok URL is solid). No Douyin/Weibo/Bilibili *search* integration (yt-dlp pulls a *known* Bilibili URL only); Baidu/Weibo go through `WebFetch` and may hit bot-blocks. Whisper is the compute-heavy step, so a **relevance gate before transcription is mandatory.**

---

# PHASE 1 — Audit (produce the plan)

Work through every dimension. For each finding record: file, location, issue, severity (High/Med/Low), disposition (fixed / flagged).

1. **Schema consistency** — every `cases/` file carries the same top-level sections in the same order (Status, Key Dates, Affiliation, Inclusion rationale, Narrative, Documented/Reported/Alleged/Speculated, Primary Sources, Secondary Sources, Named Expert Commentary, Foreign Coverage, Contradictions, Related Cases, Analysis Cross-References, Open Questions). Flag missing/misordered sections.
2. **Source tiering consistency** — every source carries a tier matching `README.md`. Flag mis-tiers. **Known systemic issue: foreign outlets defaulting to Tier 8.** Tier 8 is state-controlled propaganda organs only, not foreign national/local outlets. Produce a dedicated **"Foreign Tier-8 inventory"** — every foreign source currently at T8 and whether it is actually a state organ — but do **not** auto-retier (that is Phase 2 design + a later dedicated turn).
3. **Confidence-tag coverage** — every load-bearing claim carries Confirmed/Reported/Alleged/Speculated. Flag untagged claims.
4. **Link hygiene (static only, no fetching)** — collect every URL across `cases/`, `analysis/`, `appendices/`, `glossary.json`, `data/*.json`; report duplicates, malformed URLs, anchor-vs-target mismatches. No live-link checking (no web access in this pass).
5. **Cross-reference integrity** — every internal `[...](file.md)` / `(../analysis/...)` link resolves to an existing file and heading; report dead links and expected-but-missing back-links.
6. **Acronym discipline** — full expansion + link on first use per file, bare after. Flag bare first-uses and repeat expansions/links.
7. **Contradiction & known-unknown sync** — entries in `logs/contradictions.md` and `logs/known-unknowns.md` still match live case text, and case-level cross-case conflicts are represented in the logs. Flag drift both directions.
8. **Data ↔ prose sync** — every node in `data/diagram-data.json` and event in `data/timeline-data.json` has a prose basis, and prose entities appear in the data. Validate both JSONs parse and conform to `data/schema/`.
9. **Neutrality & voice** — flag verdict language, sensational framing in repo prose (vs. quoted/attributed source language), interested-party characterizations stated as fact. Report only.
10. **Product strength** — rank the weakest cases (thin/single-sourced/one-anonymous-claim, e.g. Garcia KCNSC); name the load-bearing analytical gaps (never-computed base rate; English-only foreign search; unverified "no autopsy" claims); check H1–H9 Mulder-vs-Scully balance; note what a hostile skeptic and a hostile believer each attack first.

**Phase 1 fix-now scope (apply directly; everything else is flag-only):** broken internal-link paths with an unambiguous target; malformed markdown; skipped heading levels; table/whitespace noise; adding a missing acronym expansion whose text is already established elsewhere (copy, don't invent); fixing an unambiguous Update-block/top-marker date inconsistency; re-ordering case-file sections to canonical order without changing content. **Flag-only:** any prose/claim/tier/confidence change, foreign Tier-8 retiering, any diagram/timeline node change.

**Phase 1 outputs:**
- `logs/audit-fable-YYYY-MM-DD.md` — findings tables per dimension; "Fixes applied" list; "Flagged for human judgment" list (prioritized High→Low); the Foreign Tier-8 inventory; a **≤20-item prioritized improvement backlog** (each item tagged effort S/M/L and impact High/Med/Low).
- Mechanical fixes committed (`audit(fable): <dimension> — <what>`; no push).
- `STATUS.md` "Flags for review" refreshed from the flagged list.

---

# PHASE 2 — Design-strengthening document

Building on the Phase 1 backlog and Foreign Tier-8 inventory, write **one** document: `docs/design-strengthening.md`. Its job is to make the project's design stronger and more durable, not to re-audit. It has three required pillars plus framing.

**Framing (short):** one paragraph restating the project's trust mechanism — provenance tiering × confidence rating, quote-provenance, refuse-to-invent, evidence-collection separated from prose — so every design choice below is justified against it.

### Pillar A — How we find new information (including video)
The discovery architecture. Cover: the pipeline stages (**seed → discover → relevance-gate → ingest → extract → tier & confidence → dedup vs. existing cases → merge → log**) with a diagram (mermaid or ASCII); a proposed **seed-query registry** (repo location + schema; per-case and per-topic queries, each with target language(s); how a new case adds seeds); per-channel discovery method (YouTube via `ytsearch`; open web + TikTok via `WebSearch`/hashtag/creator-enum; foreign press via native-language queries + `WebFetch`) referencing the proven commands and stating the weak spots plainly; the **relevance gate** (inputs, rubric, threshold, per-run transcription budget) so Whisper compute is spent only on likely-relevant items; and the ingestion detail (caption path vs. audio→Whisper path; where raw transcripts are archived — tie to the Phase 3 snapshot pipeline and `appendices/primary-sources/<case>/`; manifest fields: source URL, platform, uploader, date, capture date, content hash).

### Pillar B — How we source the material
The sourcing/provenance methodology, hardened. Cover: how a video/social transcript maps onto the 8-tier taxonomy and confidence ratings (local-news clip vs. anonymous creator vs. foreign state media); the **foreign-tiering fix** — a concrete proposed rule so foreign ≠ Tier 8 (nationality and state-control are separate axes; national/local foreign outlets tier alongside their US equivalents; only genuine state organs sit at T8, flagged for *bias* not *reliability floor*) — presented as a design recommendation feeding the dedicated re-tier turn, **not** applied here; the append-only merge discipline (dated `## Update — YYYY-MM-DD` blocks; original narrative never overwritten; mechanical vs. prose passes in separate commits); and dedup/new-case intake (how a discovered name is checked against the existing cases so a real new case — e.g. the **Matthew Sullivan** lead — gets a full case file rather than being lost or duplicated).

### Pillar C — Missing scientists from other countries
The scope-expansion design. The dossier's 11 U.S. cases are a historical artifact, not a principled scope — the artifact is worldwide by intent. Cover: how non-US cases are discovered (native-language `ytsearch` + foreign press; the proven Chinese-query result is the worked example), vetted, and admitted; what schema extensions a foreign case may need (agency/jurisdiction types, non-US legal/coroner equivalents) and the extend-only-when-≥2-cases-share-it guardrail; how foreign cases are tiered and confidence-rated under Pillar B's rules; language handling (native transcript kept + machine-translated summary, or translate-on-ingest — present as an Open decision with a default); and an explicit scope note that historical precedent (e.g. the 1980s European defense-scientist cluster) is **out of scope for now** per maintainer decision, recorded so it isn't silently dropped.

**Close with "Open decisions"** — each with a recommended default and its trade-off (Whisper model size vs. speed; relevance-gate aggressiveness; foreign-language translate-on-ingest vs. keep-native; cadence of the planned scheduled trigger).

**Phase 2 outputs:** `docs/design-strengthening.md` written; a one-line entry appended to `logs/research-log.md` describing the session; if a prompt-spec issue was found, note it in `logs/prompt-alterations.md`.

---

## Done criteria

- Phase 1: audit report written, mechanical fixes committed, `STATUS.md` flags refreshed, Foreign Tier-8 inventory produced.
- Phase 2: `docs/design-strengthening.md` written with all three pillars, grounded only in proven capabilities (anything beyond labeled "not yet verified").
- No case narrative, tier, confidence, or data-node was edited in either phase.
- Re-running surfaces no new mechanical fixes and refines (not duplicates) the two documents.
