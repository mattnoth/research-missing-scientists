# Research TODO

Items deferred from the prompt-001 cycle. Revisit before or after PDF/website generation.

> **For phased execution + agent strategy, see [SESSION-PLAN.md](SESSION-PLAN.md).** This file holds the canonical task list; the plan handles ordering and parallelization.

## Editorial & framing

- [x] **Project-purpose + AI-disclosure banner** — Completed 2026-05-08 (commit `c8f1465`). Banner applied to top of `dossier.md` (markdown surface). Website surface in mattnoth-dev still pending — separate session.
- [x] **Strip verdict language from dossier abstract + executive summary** — Completed 2026-05-08 (commit `c8f1465`). Abstract paras 2–3 rewritten with attributed-source framing; exec-summary headings replaced; originals preserved in Update block at bottom of `dossier.md`.
- [x] **Reframe the H1–H9 hypothesis-evaluation table** — Completed 2026-05-08 (commit `c8f1465`). Table reframed to "Evidence for" + "Evidence against" columns in `dossier.md`. Per-hypothesis writeups in `analysis/hypotheses.md` use the same parallel structure plus a `### Context (category-level)` subsection where structural inputs needed separation from case-specific bullets (H4, H5, H6, H7, H9).
- [x] **X-Files presentation layer for analysis pages** — Completed 2026-05-08 (commit `c8f1465`). Each hypothesis writeup enumerates evidence-for and evidence-against in parallel; closing synthesis paragraphs removed (originals in Update block). Mulder-side hardening on H6, H7, H9 added affirmative evidence-for bullets where the prior writeup carried only absence-of-evidence framing.

## Tooling — Snapshot pipeline (Playwright / headless browser)

- [ ] **Build `scripts/snapshot-source` (Playwright)** — Input: URL. Output: raw HTML + linked assets + screenshot + PDF + extracted text + manifest (timestamp, source URL, http status, content hash). Stored under `appendices/primary-sources/<case>/snapshots/<slug>/`. Used by both broken-links recovery and the standing self-host primary-source workflow. Decide language: Python (Playwright Python) or Node. See SESSION-PLAN.md Phase 3.
- [ ] **Backfill pass** — Run snapshot pipeline against every external URL currently cited as primary source. Existing markdown archives get an HTML + screenshot + PDF companion in their case's `snapshots/` directory.
- [ ] **Document self-host workflow in RUNBOOK.md** — How and when to snapshot; where files live; how citations should reference both local archive and external URL.

## Actionable now (web search could fill)

- [ ] **House Oversight briefing results** — Comer/Burlison requested briefing by April 27, 2026. Check for public statements, press releases, or news coverage of what was disclosed.
- [ ] **FBI investigation updates** — Patel said they'd "produce information to the White House and the world." Search for any findings released since April 20, 2026.
- [ ] **Daily Mail articles** — Original source for Garcia KCNSC employment claim and a key narrative originator for international coverage. Prior searches returned nothing; retry with fresh queries.
- [ ] **BBC coverage** — Absence noted but unconfirmed. One more targeted search to close the gap or confirm the absence.
- [ ] **T1 sources that returned HTTP 403** — BCSO press release PDF, House Oversight press release page. May now be accessible. Retry fetches.

## Formatting fixes (no research needed)

- [ ] **Reza case file** — Add missing section headers: inclusion rationale, named expert commentary, foreign coverage (WION India covered this case).
- [ ] **Hicks case file** — Add inline tier/confidence tags to narrative prose.
- [ ] **Maiwald case file** — Same as Hicks.
- [ ] **Grillmair case file** — Add explicit Documented/Reported/Alleged/Speculated section header (substance already inline).

## Contact list (for future outreach)
- [ ] **Build a people-of-interest list** — Compile names, roles, affiliations, and publicly available contact info for key people across the cases: local beat reporters who covered these stories, named experts quoted in coverage (former FBI, think tank analysts, etc.), family spokespeople who have spoken publicly, congressional staffers involved in oversight hearings. This is prep for eventual direct outreach — no contact until the human operator decides to proceed. Store as a structured file (JSON or markdown table) with name, role, relevance to which case(s), and any public contact info found.
- [ ] **Identify the best local/beat reporters per case** — Who has the deepest coverage? Who broke stories vs. who rewrote wire copy? These are the highest-value outreach targets.

## Re-tag case files for new tier system
- [x] **Update all case file tier references** — Completed 2026-04-21 via `prompts/build/prompt-retag-tiers.md`. All 11 case files migrated.
- [x] **Update dossier.md tier references** — No actionable tier tags found; only Tier 1 references which are unchanged.
- [x] **Update analysis/ tier references** — Already migrated in prior pass; verified correct.
- [x] **Update CLAUDE.md and any prompt files** — Already updated per prompt-retag-tiers.md exclusion list.

## Methodology — Patterns to port from Weirwood Network

Four patterns from `/Users/mnoth/source/asoiaf-chat/` (Weirwood Network) that map onto this dossier's workflow. Captured 2026-05-06. Context and rationale in `scratch.txt` ("Continuation — Weirwood transfer + general update pass").

- [ ] **Path B "categorizer extension"** — when a new case has features the existing case schema doesn't cover (a new agency type, a new death classification), extend the schema rather than force-fit. Applies whenever cases are added (e.g., the Chinese-scientists item). *Action:* document the extension protocol in `RUNBOOK.md` (or the case-file template) so future case adds follow it; record each extension when it happens. **Phase 0.5 guardrail:** extend only when ≥2 cases share the new feature.
- [ ] **Alias resolver / orphan-edge resolution** — same entity under name variants (JPL ↔ Jet Propulsion Laboratory, AFRL ↔ Air Force Research Lab). Worth applying to glossary + connection diagram, where there are likely dangling references. *Action:* scan `glossary.json`, `data/diagram-data.json`, and case files for entity name variants; build a canonical-name → aliases map; deduplicate diagram nodes and cross-link glossary entries. (Phase 1 Agent E in SESSION-PLAN.)
- [ ] **Stage-1 prose-only re-emission ("Option C")** — re-extract just the prose layer to enrich existing nodes without rerunning the whole pipeline. This is the pattern that satisfies "don't overwrite original narrative" — append/enrich rather than replace. *Action:* adopt as the standing update pattern; new info appended as dated `## Update — YYYY-MM-DD` blocks under existing narrative; original prose never overwritten. Document in `prompts/build/queued/prompt-004-update.md` so all future maintenance runs follow it.
- [ ] **Mechanical vs. prose extraction split** — implicit in our case schema (mechanical fields vs. narrative), but Weirwood's discipline of touching them in *separate passes* is healthier than mixed edits. *Action:* document the split in `RUNBOOK.md`. Mechanical = case schema fields (dates, names, agencies, source URLs, tier/confidence tags). Prose = narrative. Never mix in one commit.
- [ ] **Reconsider scaled-extraction patterns once Phase 4 grows** — Wave-based parallel extraction, race protection, and a multi-agent fleet were filtered out as overkill for 11 cases. If the worldwide discovery sweep (Phase 4) surfaces ≥50 candidate cases across 8 languages, revisit: wave-based parallel may become worthwhile, and race protection matters once multiple agents touch the same case files. Decision deferred until candidate volume is known.

## Research-phase backlog (mirror of SESSION-PLAN, scratch.txt items)

Every scratch.txt open item also lives here as a trackable checkbox. **For the operating context, decisions, and agent strategy per item, see [SESSION-PLAN.md](SESSION-PLAN.md) and [scratch.txt](scratch.txt).** This list is the index — those files hold the substance.

### Phase 1 — Cleanup audit (5 parallel read-only agents)
*Findings consolidated 2026-05-08 in [logs/audit-phase1-findings-2026-05-08.md](logs/audit-phase1-findings-2026-05-08.md). Cleanup commit applied 2026-05-08 (Tier 1–6); Tier 7 deferred to Phase 2 voice audit; Tier 8 needs-human-judgment items pending discussion.*
- [x] **Agent A — both-links sweep** (Tom DeLonge + other public figures: Wikipedia + primary-source URL on first occurrence per file; verify-don't-trust)
- [x] **Agent B — acronym audit** (first-use expansion per file; glossary completeness; cross-file consistency; over-linking flag)
- [x] **Agent C — broken-links pass** (every URL across case files / appendices / glossary.json / data JSON; alive/dead/redirected; Wayback availability for dead) — *Wayback CDX API was down during sweep; re-run before cleanup commit.*
- [x] **Agent D — foreign-source bias audit** (existing tier assignments; flag US-favored tiering of comparable foreign outlets)
- [x] **Agent E — alias-resolver scan** (glossary + diagram + case files; canonical → aliases map; dedup proposals)

### Phase 2 — Conclusion-neutrality + X-Files balance audit (single agent)
- [ ] **Voice + neutrality + hypothesis-balance audit** — opinion-tinted phrasing; "no connection" type assertions; subjective characterizations from interested parties stated as fact (e.g., "*his wife characterizes it as brief, unpaid consulting for fiction writing*"); H1–H9 Mulder vs. Scully balance check. See SESSION-PLAN Phase 2.

### Phase 4 — Worldwide discovery sweep (8 threads)
- [ ] **W-1 — TikTok / video creators** (Critical priority; primary insider venue; hybrid: WebSearch + cross-posted URLs + user-curated hashtag picks)
- [ ] **W-2 — Reddit deep dive** (topical + case-specific subs; full comment trees; Reveddit/Unddit/Wayback for deleted)
- [ ] **W-3 — Russian-language press** (TASS, Kommersant, Meduza, regional)
- [ ] **W-4 — Chinese-language press** (Xinhua, People's Daily, regional) — **also covers the "Add Chinese scientists" scratch item; surfaced cases get full case-file treatment**
- [ ] **W-5 — French / German / Spanish press** (Le Monde, Der Spiegel, El País)
- [ ] **W-6 — Japanese press** (Asahi, Yomiuri, NHK, regional)
- [ ] **W-7 — Korean press** (Chosun, Hankyoreh, Yonhap, regional)
- [ ] **W-8 — English-language indie / Substack / aggregator lists** (Wayback for takedowns; verify each lead independently)

### Phase 5 — Amy Eskridge case update
- [ ] **Eskridge research bundle + precursor-statement hunt** — primary/court/local first; specifically hunt for the "I would not commit suicide" precursor statement (interviews, social posts, video, third-party reporting); Tier carefully (such claims often originate low-tier and need primary verification). Research only — case file update happens after, with neutrality voice.

### Phase 6 — Depth-first update on existing cases
- [ ] **Step A — hybrid triage** (rank all 11 by source weakness AND surface new-material density; user picks 2–3 from the union)
- [ ] **Step B — source-deepening pass** on top-N (parallel agents, one per case)
- [ ] **Step C — news-refresh pass** on same top-N (dated `## Update —` blocks, originals untouched)

### Phase 8 — Pattern-recognition appendix
- [ ] **Behavioral-patterns appendix** — factory-reset phones, walking out / leaving belongings, undisclosed cause of death, **precursor statements (Eskridge plus any others surfaced)**. Lists which cases share each pattern. Includes human-fallibility caveat. New file: `appendices/behavioral-patterns.md` or `analysis/behavioral-patterns.md`.

### Phase 9 — Geographic & domain clustering
- [ ] **9a — Huntsville hotbed analysis** — Huntsville hosts Redstone Arsenal, Marshall Space Flight Center, U.S. Space Command HQ, dozens of defense contractors. Other deaths/disappearances/scandals at Huntsville-based entities since 2022; people in Eskridge's research circle; local-press + TikTok/Reddit insider discourse.
- [ ] **9b — Antigravity / zero-gravity / exotic-propulsion domain map** — Public-facing figures (Podkletnov, Ning Li, Hal Puthoff, Eric Davis, others); research entities (Institute for Exotic Science, HoloChron, EarthTech, TTSA, etc.); connections to dossier subjects; relationship to UAP-disclosure community already documented for McCasland. Dossier currently treats this as a "weak signal" attached to one case — re-examine as a domain.
- [ ] **9c — Other domain lenses** — instantiate per-domain if the worldwide sweep surfaces them.

## Significant gaps (harder to fill)

- [ ] **Base-rate actuarial analysis** — Compare observed rate (11 events, ~4-year window) against expected rate for the combined defense/aerospace workforce (~30k+ across LANL, JPL, Sandia, KCNSC, etc.). Most important analytical gap. May require workforce demographic data that isn't freely public.
- [ ] **Non-English foreign coverage** — Search TASS, Xinhua, Press TV, NHK, Al Jazeera, Le Monde, Der Spiegel, Haaretz in native languages. Only English-language editions were searched in prompt-001.
- [ ] **Reza-McCasland professional connection** — WION flagged a "Mondaloy connection." Both touched the AFRL ecosystem. No documented link found yet. Patent co-author networks, conference proceedings, or AFRL contract records might surface something.

## Cannot fill with open-source research

- Classified program overlap between subjects (only FBI/DOE/DOD can address)
- Inter-case social network analysis from phone/email records
- Cell phone forensic results for Reza (LASD has not released)
- McCasland USAF sweatshirt forensic results (pending)
- Hicks and Maiwald autopsy status (LA County ME has not confirmed or denied)




- can we get around the above?
- make the prompt resuable in such a way as to update the research. also ask if i can put that on an automatic clock to the deployed website for updated research every day?

## Automated Trigger
- [ ] **Set up a scheduled Claude Code trigger** to run prompt-004 (maintenance/update) on a daily or weekly cron. Should: check for new developments (House Oversight findings, FBI updates, new cases, case resolutions), update research artifacts, bump version, and flag if PDFs/website need regeneration. Needs: a trigger prompt adapted from prompt-004 that runs non-interactively and commits results. Consider whether to also auto-rebuild the website (`npm run build` in mattnoth-dev) or just flag it for manual rebuild.

## Website — Timeline Improvement
- [ ] Better layout and spacing — current visualization is too basic
- [ ] More readable event labels and descriptions
- [ ] Improved zoom/scroll UX
- [ ] Better mobile experience (consider vertical layout for mobile)
- [ ] Group overlapping events more clearly
- [ ] Add more context events (media milestones, congressional actions)

## Website — Diagram Enrichment
The connection diagram needs significantly more data to match the richness of the research:
- [ ] Add more specific locations (Los Alamos neighborhoods, specific trails, specific addresses)
- [ ] Add specific projects/programs (DART, NEAT, Dawn for Hicks; Mondaloy for Reza; PSFC fusion programs for Loureiro; SAPs for McCasland)
- [ ] Expand speculative/corkboard layer — research contains extensive speculation analysis not yet visualized
- [ ] Add behavioral pattern nodes (left without belongings, undisclosed cause of death)
- [ ] Consider temporal proximity edges (events close in time)
- [ ] Current: 34 nodes / 44 edges — research supports significantly more

## Website — Diagram Interactivity & Animations
- [ ] **Fix click-to-highlight connections** — Current implementation isn't working well; clicking a node should reliably highlight its direct connections and dim everything else. Needs debugging.
- [ ] **Make connection lines clickable** — Clicking an edge should show details about the relationship (type, strength, relevant cases, etc.)
- [ ] Make graph nodes clickable (navigate to relevant case or detail)
- [ ] Add more cool animations to the diagram (transitions, hover effects, edge pulses, etc.)

## Website — Diagram Layout & Readability
- [ ] **Fix force-directed auto-spreading** — When there are too many nodes, the graph is unreadable because nodes pile up on top of each other. The auto-spreading/repulsion that should be keeping nodes apart isn't working. Investigate force simulation parameters (charge strength, link distance, collision radius) and fix so the graph scales gracefully as node count grows. **Specifically: nodes are too close together on initial launch** — bump default link-distance / charge-repulsion so the first render is readable without manual zoom-out.
- [ ] **Surface edge labels in the rendering** — `data/diagram-data.json` already carries a `label` field on every edge ("Retired LANL employee (retired 2017, decades of service)" etc.) and an `edge_type`, but the website doesn't render either. Show edge labels by default (with collision avoidance) or on hover/click — decide per density. Not a data task; the data is there. Pure rendering work in mattnoth-dev.
- [ ] **Fix truncated labels** — Long names like "NASA Jet Propulsion Laboratory" and "Planetary Science & …" are cut off mid-word with ellipsis. Either wrap to two lines, show full text on hover/tooltip, or expand the label bounding box. Decide per node type.
- [ ] **Resolve label/edge collisions** — Case name labels (e.g., "Michael David Hicks") render directly on top of connecting edges, making both unreadable. Add label collision avoidance, a background halo/pill behind text, or reposition labels away from edges.
- [ ] **Resolve label/label collisions** — Adjacent node labels (e.g., "Aerojet Rocketdyne" overlapping an edge and a neighboring label) pile onto each other. Needs label-level collision detection or a force term that repels labels as well as nodes.
- [ ] **Establish visual hierarchy between people and institutions** — Right now a case subject label and an org label look almost identical (same font, same placement). People should be visually dominant; orgs secondary. Consider different font weight, size, color, or label position (above vs. below node).
- [ ] **Improve status tag legibility** — "deceased" / "missing" tags under case names are small and low-contrast. Bump size, increase contrast, or render as a colored pill/badge so status is scannable at a glance.

## Website — UFO/UAP Section
- [ ] Create a dedicated page or section focused on UFO/UAP/alien theories and these scientists' connections to that world
- [ ] Make it prominent in the site navigation (not buried)
- [ ] Collect and link evidence tying cases to UAP-related programs, congressional hearings, whistleblower claims, etc.
- [ ] Include outbound links to key UAP sources (congressional testimony, AARO reports, Grusch claims, etc.)

## Website — Diagram Styles
- [ ] Experiment with a traditional corkboard-style diagram (straight lines, pinned cards, string connections) as an additional view alongside the existing force-directed graph
- [ ] Try other diagram layout styles (hierarchical, radial, etc.) to see what communicates the connections best

## Website — SEO Optimization

### Head / Meta Tags
- [ ] Add proper `<title>` tags per page (descriptive, keyword-rich, under 60 chars)
- [ ] Add `<meta name="description">` per page (compelling summary, under 160 chars)
- [ ] Add Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`) for social sharing
- [ ] Add Twitter Card meta tags (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`)
- [ ] Add canonical URLs (`<link rel="canonical">`) to avoid duplicate content issues
- [ ] Add structured data / JSON-LD (Article schema for case pages, WebSite schema for homepage)
- [ ] Ensure proper `<meta name="robots">` directives
- [ ] Add favicon and `apple-touch-icon` if missing

### In-Article Links & Structure
- [x] Add internal cross-links between related case pages (e.g., Reza ↔ McCasland, Hicks ↔ Grillmair) — Completed 2026-04-21. All 11 case files now have "Related Cases" and "Analysis Cross-References" sections. Analysis files have case back-links in all key tables.
- [x] Link from case pages to relevant analysis sections and vice versa — Completed 2026-04-21. Case→analysis links in every case file; analysis→case links in connection-analysis.md, hypotheses.md, and foreign-intel-layer.md.
- [x] Add outbound links to authoritative sources (news articles, government pages, congressional records) — Completed 2026-04-21. Source tables already had links; glossary acronyms (LANL, JPL, AFRL, KCNSC, DOE, etc.) now link to institutional .gov/.edu/.mil websites site-wide via glossary.json url field. Inline source links added to Reza, McCasland, Grillmair, and Hicks narratives so key claims link directly to sources as you read.
- [x] Use descriptive anchor text (not "click here" — use "House Oversight hearing on scientist deaths") — Already clean. No generic anchor text found in any file.
- [ ] Add a sitemap.xml and submit to Google Search Console — **Website repo task** (mattnoth-dev), not this research submodule.
- [x] Ensure proper heading hierarchy (single H1 per page, logical H2/H3 nesting) — Verified 2026-04-21. All 25 markdown files pass: single H1, logical H2/H3 nesting, no skipped levels.
- [ ] Add breadcrumb navigation with structured data — **Website repo task** (mattnoth-dev), not this research submodule.

### Keywords & Search Visibility
- [ ] Target high-search terms: "missing scientists", "dead scientists 2024 2025", "Los Alamos deaths", "defense scientist deaths", "scientists disappearing", "UAP scientists killed"
- [ ] Target adjacent buzz topics: "government cover-up scientists", "whistleblower scientists", "AARO", "David Grusch", "congressional UFO hearings", "classified programs scientists"
- [ ] Include long-tail keywords naturally in case narratives: names + affiliations + locations + circumstances
- [ ] Add an FAQ section or page targeting question-based searches ("Why are so many scientists dying?", "What happened to scientists at Los Alamos?")
- [ ] Optimize image alt text with descriptive, keyword-relevant descriptions
- [ ] Consider a blog/updates section for fresh content signals (Google favors regularly updated sites)
- [ ] Monitor Google Trends for emerging related search terms and update content accordingly

## Website — Community Contributions
- [ ] **User-submitted connections on the diagram** — Allow visitors to suggest new nodes/edges (e.g., "I think X is connected to Y because…"). Could be a simple form that creates a GitHub issue or a moderated submission queue. Decide: live on site vs. PR-based workflow.
- [ ] **CONTRIBUTING.md in the research repo** — Document how someone can contribute: how to submit a new case or connection, the source-tiering and confidence-rating requirements, the case file schema, and the no-contact policy. Lower the barrier for open-source researchers.
- [ ] **Contributing guide on the website** — A public-facing "How to Contribute" page (friendlier than a raw markdown file) explaining what kinds of contributions are welcome: new cases, source links, corrections, foreign-language coverage, FOIA documents, etc.
- [ ] **Moderation / review process** — Define how submissions get vetted before merging (source tier check, neutrality review, no doxxing/contact). Could be maintainer-only review or a small trusted-reviewer group.

## Website — Natural Language Research Chat (far future)
- [ ] **Embed a chat interface on the website** — Let visitors ask questions in natural language about the cases, connections, and research (e.g., "Which scientists worked at LANL?", "What are the UAP connections?"). Powered by an LLM with this repo as its knowledge base / RAG context.
- [ ] **Use repo as a research harness** — Allow the chat to kick off new research prompts against the repo's prompt pipeline, returning structured results. Essentially turning the site into an interactive research tool, not just a static dossier.
- [ ] **Scope and safety guardrails** — Enforce the no-contact policy, source-tiering standards, and neutrality rules within the chat. Prevent the model from fabricating claims or presenting speculation as fact.

## Website — UI Polish
- [ ] Change the question mark icon
- [x] **Mobile table scroll containers** — Completed 2026-04-22 via `prompts/build/completed/prompt-mobile-table-styling.md`. Tables wrapped in `.ms-table-wrap`, viewport-capped, 7th column hidden on narrow screens.
- [ ] **Mobile TOC overlay** — Contents disclosure should be a compact trigger that opens a floating overlay (not inline expansion). See `prompts/build/queued/prompt-mobile-toc-overlay.md`.
- [ ] **Tighten header-to-content vertical spacing** — "Abstract" too far from page title on mobile. Part of the TOC overlay prompt.
- [ ] **Abstract reveal on scroll-up (mobile)** — Sticky-header pattern: hide abstract on scroll-down, reveal on scroll-up. Confirm interaction: reveal-on-scroll-up + hide-on-scroll-down sticky header, or always-visible pinned-at-top? Mattnoth-dev (website) task. (Scratch.txt origin.)
- [ ] **Horizontal rule alignment on mobile** — `<hr>` lines between sections don't align with content edges on narrow viewports. Pre-existing layout bug, not yet prompted.

## Research — Significant Locations
- [ ] **Significant locations in theories** — Dedicated section/page cataloging recurring physical places across cases and theories: LANL and its sub-facilities (LANSCE, TA-sites), JPL, Sandia, KCNSC, AFRL sites, specific trails/neighborhoods where bodies were found, etc. For each: what happens there, which cases touch it, what public-interest narratives attach to it (UAP/SAP programs, weapons work, etc.), and authoritative outbound links. Would give readers a geographic spine alongside the per-case and per-hypothesis views.

## Research — Government Site Change Tracking
Rationale: federal site churn has been unusually heavy over the last ~2 years (quiet removals, re-orgs, redactions). Treating relevant gov pages as an evidentiary surface — rather than assuming dead links are mundane web rot — could surface a pattern in aggregate, even when any single change is ambiguous. This is an observational/logging layer, not a claim of cover-up; the point is to make the changes *visible and dated* so others can judge.

- [ ] **Define a watchlist of gov URLs** — Candidate seeds: LANL (lanl.gov main, fire-danger page, LANSCE, specific TA pages), DOE (energy.gov program pages relevant to the labs), JPL (jpl.nasa.gov, Dawn/DART/NEAT program pages), AFRL (afrl.af.mil, Mondaloy references), Sandia, KCNSC, NASA, AARO (aaro.mil), and any congressional pages referenced in case coverage. Store as a structured list (JSON or markdown table) with URL, why-it-matters, and which case(s) it touches.
- [ ] **Wayback Machine snapshot pipeline** — For each watchlist URL, capture snapshots at key dates: before/after each case event, before/after congressional hearings, and on a rolling cadence going forward. Log diffs chronologically: what text/links were added, removed, or quietly edited. Can be semi-automated via the Wayback Machine CDX API.
- [ ] **Log entry: LANL fire-danger page 404 (observed 2026-04-21)** — First entry for the change-tracking log. User observed multiple on-site references to a Los Alamos fire-danger rating page returning 404 on lanl.gov. Action: capture the exact referring URLs, check Wayback for prior snapshots of the destination page, record whether the page previously existed and when it was removed/moved.
- [ ] **Decide where this lives in the dossier** — Options: (a) new `logs/site-change-log.md` append-only ledger, (b) a section under `appendices/`, or (c) a dedicated `evidence/` top-level directory if this grows. Pick once there are a handful of entries.
