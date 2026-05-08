# Phase 1 cleanup-audit findings — 2026-05-08

Read-only audit. Five agents launched in parallel; this document consolidates their output into a ranked edits list for the next session's cleanup commit. **No edits to research content were made in this session.**

Session prompt: [prompts/build/queued/...](../prompts/build/queued/) (Phase 1 launcher). Plan-of-record: [SESSION-PLAN.md](../SESSION-PLAN.md) Phase 1.

---

## Summary of findings counts per agent

| Agent | Task | Items surfaced | Verification successes | Verification failures |
|---|---|---|---|---|
| A — Both-links sweep | Public-figure + primary-source link enrichment (Wikipedia + primary URL on first occurrence per file) | 18 named candidates examined (10 from initial brief + 8 surfaced during sweep) | 14 Wikipedia URLs verified; 5 primary-source URLs verified | 4 Wikipedia 404s (Coffindaffer, Milburn, Rodgers, Roecker — no article exists); 3 primary-source 403/404 (oversight.house.gov press release, NTI staff page, White House admin page) |
| B — Acronym audit | First-use expansion, glossary completeness, cross-file consistency, over-linking | 29 first-use violations across 13 files; 3 glossary gaps; 1 cross-file inconsistency; 4 over-linking instances | n/a | n/a |
| C — Broken-links pass | URL health categorization with Wayback fallback | 174 unique URLs scanned | 107 alive, 1 redirect, 5 false-positive 403s (alive on curl) | 4 dead, 32 403, 2 soft-404, 0 Wayback recoveries (CDX API was down — flag for re-run) |
| D — Foreign-source bias audit | Are foreign Tier-3/4 outlets held to a stricter standard than U.S. equivalents? | 7 origin-bias flags + 1 counter-direction flag (U.S. over-tiered); 4 asymmetric-language findings | n/a | n/a |
| E — Alias-resolver scan | Canonical-name → aliases map; diagram-node and glossary deduplication | 17 canonical entities mapped; 43 alias variants tracked; 9 dedup actions identified | n/a | n/a |

---

## Agent A — Both-links sweep

### Verified link proposals (priority order, highest-value first)

**Initial-brief candidates:**

| # | Name/Org | First-occurrence file:line | Current state | Wikipedia URL (verified) | Primary-source URL |
|---|---|---|---|---|---|
| 1 | Tom DeLonge | `cases/mccasland.md:27` | unlinked-as-person (WikiLeaks doc is linked, person is not) | `https://en.wikipedia.org/wiki/Tom_DeLonge` ✓ | `https://wikileaks.org/podesta-emails/emailid/3099` ✓ |
| 2 | John Podesta | `cases/mccasland.md:27` | unlinked | `https://en.wikipedia.org/wiki/John_Podesta` ✓ | `https://wikileaks.org/podesta-emails/emailid/3099` ✓ (shared) |
| 3 | Karoline Leavitt | `dossier.md:17` | linked to Fox News only — no Wikipedia | `https://en.wikipedia.org/wiki/Karoline_Leavitt` ✓ | existing Fox News link kept; whitehouse.gov bio is 404 |
| 4 | Rep. James Comer | `dossier.md:17` | unlinked individually (only as part of Committee link) | `https://en.wikipedia.org/wiki/James_Comer_(politician)` ✓ | oversight.house.gov press release — 403 from WebFetch but **alive on curl** |
| 5 | Rep. Eric Burlison | `dossier.md:17` | unlinked | `https://en.wikipedia.org/wiki/Eric_Burlison` ✓ | same press release as Comer (alive on curl) |
| 6 | Kash Patel | `dossier.md:11` | unlinked | `https://en.wikipedia.org/wiki/Kash_Patel` ✓ | Newsweek article ✓ |
| 7 | Chris Wright (DOE Sec.) | `analysis/foreign-intel-layer.md:81` + `appendices/named-expert-commentary/chris-wright-doe.md:1` | unlinked | `https://en.wikipedia.org/wiki/Chris_Wright` ✓ (NOT `_(businessman)`) | `https://www.energy.gov/person/chris-wright` ✓ |
| 8 | Chris Swecker | `analysis/foreign-intel-layer.md:67` + appendix | unlinked | `https://en.wikipedia.org/wiki/Chris_Swecker` ✓ (stub but correct) | n/a |
| 9 | Michio Kaku | `analysis/foreign-intel-layer.md:71` + appendix | unlinked | `https://en.wikipedia.org/wiki/Michio_Kaku` ✓ | n/a (CUNY page didn't fetch) |
| 10 | Ross Coulthart | `appendices/named-expert-commentary/ross-coulthart.md:1` | unlinked | `https://en.wikipedia.org/wiki/Ross_Coulthart` ✓ | n/a |
| 11 | David Grusch | not found in any narrative file | n/a — name not in dossier | `https://en.wikipedia.org/wiki/David_Grusch_UFO_whistleblower_claims` ✓ (if added later) | n/a |

**Additional candidates surfaced during sweep:**

| # | Name/Org | First-occurrence file:line | Wikipedia URL | Primary-source URL |
|---|---|---|---|---|
| 12 | Luis Elizondo | `appendices/named-expert-commentary/luis-elizondo.md:1` | `https://en.wikipedia.org/wiki/Luis_Elizondo` ✓ | n/a |
| 13 | Steven Greer | `appendices/named-expert-commentary/steven-greer.md:1` + `analysis/hypotheses.md:237` | `https://en.wikipedia.org/wiki/Steven_M._Greer` ✓ (note middle initial) | n/a |
| 14 | Michael Shellenberger | `cases/eskridge.md:47` | `https://en.wikipedia.org/wiki/Michael_Shellenberger` ✓ | n/a |
| 15 | AARO | first narrative use `analysis/hypotheses.md:200` (already in glossary, not linked in prose) | `https://en.wikipedia.org/wiki/All-domain_Anomaly_Resolution_Office` ✓ | `https://www.aaro.mil/` (not fetched — official .mil) |
| 16 | To The Stars (TTSA) | `cases/mccasland.md:169` | `https://en.wikipedia.org/wiki/To_the_Stars_(company)` ✓ | n/a |
| 17 | Nuno Loureiro | `dossier.md:22` (linked only to local case file) | `https://en.wikipedia.org/wiki/Nuno_Loureiro` ✓ | `https://news.mit.edu/2025/...` ✓ |
| 18 | Carl Grillmair | `dossier.md:22` (linked only to local case file) | `https://en.wikipedia.org/wiki/Carl_Grillmair` ✓ | Caltech IPAC page TBD |

**No-Wikipedia-article cases (handle via in-context credentialing only — flag as needs-human-judgment):**

- Jennifer Coffindaffer — Newsweek quote-source can serve as the "who is this" link
- Joseph Rodgers (CSIS) — `https://www.csis.org/programs/project-nuclear-issues` ✓ as primary source
- Scott Roecker (NTI) — NTI staff page returns 403; needs manual confirmation
- Franc Milburn — no Wikipedia, no verifiable primary; existing in-text caveat about unverified credentials should remain

### Over-link findings (redundant repeat-links to remove)

**`cases/chavez.md`:**
- `LAPD` (link to Los Alamos county news): linked at lines 12, 13, 15, 23, 27, 29 — keep line 12, remove rest
- `NM DPS` (link to missingpersons.dps.nm.gov): linked at lines 10, 21, 23, 29, 31 — keep line 10, remove rest

**`cases/reza.md`:**
- `LASD` (link to solvethecase.org/case/2025-56): linked at lines 92 and 93 — keep line 92, remove line 93

**`dossier.md`:**
- "House Oversight Committee" (oversight.house.gov press release URL) at lines 11, 17, 44, 109 — keep line 11, remove rest
- "FBI investigation" (Newsweek URL) at lines 11 and 108 — keep line 11, remove line 108

### Verification failures with proposed alternatives

- `https://en.wikipedia.org/wiki/Chris_Wright_(businessman)` → 404; use `https://en.wikipedia.org/wiki/Chris_Wright` (resolves to DOE Secretary article)
- `https://en.wikipedia.org/wiki/To_the_Stars_Academy_of_Arts_%26_Science` → 404; use `https://en.wikipedia.org/wiki/To_the_Stars_(company)`
- `https://www.whitehouse.gov/administration/karoline-leavitt/` → 404; keep existing Fox News link
- oversight.house.gov press release → 403 from WebFetch, **200 from curl** (Agent C confirms alive); link is correct, the 403 is a bot-block

---

## Agent B — Acronym audit

### Per-file first-use violations (29 instances across 13 files)

**`dossier.md`** (12 violations) — `LANL`, `JPL`, `KCNSC`, `AFRL`, `SAPOC`, `CSIS`, `NTI`, `IPAC`, `USAF`, `BCSO`, `NMSP`, `UAP` all first-appear bare. None are expanded anywhere in this file. Fix: expand the first occurrence of each per glossary form (e.g., "Los Alamos National Laboratory (LANL)").

**`cases/casias.md`** (3) — `NamUs` (expanded later at line 46, move to first use at line 3), `NMSP` (full name written at line 46 without parenthetical abbreviation), `NNSA` (used at line 7 without expansion).

**`cases/chavez.md`** (2) — `LAPD` (first-use violation + cross-file inconsistency, see below), `NNSA` (used at line 7 without expansion).

**`cases/eskridge.md`** (2) — `MSFC` (full name at line 7 without parenthetical), `DEW` (abbreviation debuts bare at line 54 even though full phrase appears earlier in prose).

**`cases/garcia.md`** (3) — `KCNSC` (debuts bare in table at line 14), `APD` (bare at line 11 before expansion at line 19), `NNSA` (used at line 30 without expansion).

**`cases/grillmair.md`** (2) — `NEOWISE` (never expanded; glossary has the expansion), `LASD` (never expanded in this file).

**`cases/hicks.md`** (4) — `DART` (bare at line 7 before expansion at line 28), `DOD`, `DOE`, `FOIA` (all used without expansion).

**`cases/loureiro.md`** — none. All major acronyms expanded correctly.

**`cases/maiwald.md`** (5) — `SBG-VSWIR` (bare at line 7 before line 35), `COWVR` (never expanded), `SWOT` (never expanded), `DOD`, `DOE` (both bare).

**`cases/mccasland.md`** (4) — `OUSD(AT&L)` (never given parenthetical expansion), `SAPOC` (bare at line 24 before line 56), `AFRL` (bare at line 25 before line 57), `SAP` (standalone abbreviation never given its own expansion).

**`cases/reza.md`** — none.

**`cases/thomas.md`** (1) — `NEMLEC` (bare at line 15 before line 34).

**`analysis/connection-analysis.md`** (4+) — `IPAC`, `KCNSC`, `PSFC`, `DART/NEAT/SBG-VSWIR/AMR/HIFI` all bare without expansion in this file (per "new file = reset" rule).

**`analysis/foreign-intel-layer.md`** (9) — `SAPOC`, `DOD`, `OUSD(AT&L)`, `AFRL`, `MSS`, `GRU`, `SVR`, `IRGC`, `MOIS`, `DOE`, `CSIS`, `NTI` — none expanded in this file.

**`analysis/hypotheses.md`** (4) — `IGIC` (no glossary entry), `CSIS`, `NTI`, `SAPOC` — none expanded.

### Glossary gaps (acronyms in narrative but not in `data/glossary.json`)

| Acronym | First seen at | Proposed expansion |
|---|---|---|
| `IGIC` | `analysis/hypotheses.md:218` | Intelligence Community Inspector General |
| `USAF` | `cases/mccasland.md:21`, `dossier.md:74` | U.S. Air Force |
| `C4ISR` | `cases/mccasland.md:63` | Command, Control, Communications, Computers, Intelligence, Surveillance, and Reconnaissance |

### Cross-file inconsistency

| Acronym | Variant A (which file) | Variant B (which file) | Recommended canonical |
|---|---|---|---|
| `LAPD` | "Los Alamos Police Department" — `cases/chavez.md` (lines 13, 27, etc.) | "Los Angeles Police Department" — `data/glossary.json` | **Los Angeles Police Department (LAPD)** is glossary-canonical. `cases/chavez.md` should spell out "Los Alamos Police Department" in full and **stop using `LAPD` as the abbreviation** in that file (high collision risk; LAPD is too well-known as Los Angeles PD). |

### Over-linking findings — see Agent A consolidation above (overlap)

Agents A and B identify the same over-linked items in `dossier.md` (`House Oversight Committee`, `FBI investigation`), `cases/chavez.md` (`LAPD`, `NM DPS`), and `cases/reza.md` (`LASD`). One de-link pass covers both audits.

---

## Agent C — Broken-links pass

### Dead URLs (4)

| URL | First seen at | Wayback available? |
|---|---|---|
| `http://missingpersons.dps.state.nm.us/mpweb/mpdetailreport_serv?id=M100749` (TLS cert invalid — legacy domain retired) | `appendices/primary-sources/casias/nm-missing-persons-database-entry.md:3` | **No.** Replace with `.nm.gov` equivalent (the new domain hosts the same record IDs, confirmed alive). |
| `https://www.lanl.gov/` (entire domain dead — every path 404, S3/CloudFront fallback) | `data/glossary.json:6` | No snapshot indexed. Annotate the glossary URL field; LANL site appears to be in active redesign. |
| `https://www.ipac.caltech.edu/people/staff/carl_grillmair` (staff page removed after death) | `appendices/primary-sources/grillmair/...` | No snapshot. Use Caltech memorial URL (`https://www.caltech.edu/about/news/caltech-mourns-the-passing-of-carl-grillmair-19592026`) which is alive. |
| `https://www.daytondailynews.com/local/.../DQHLHBMP2FCSXPNNJHG3PHC6IU/` (CMS migration broke URL) | `cases/mccasland.md:214` | No snapshot. Annotate as "link dead — no archive recovered" per scratch.txt convention. |

### 403 / blocked-by-server URLs (32)

The vast majority are **alive** but block automated user agents. Agent C verified several with curl that returned 200, including:
- `oversight.house.gov` press release + PDF (alive — keep links)
- `brookline.news` Loureiro article (alive — keep link)
- All 4 IBTimes UK articles (alive on browser-like UA — keep links)

True bot-blocks (legacy.com, gatewaypundit.com, researchgate.net, hoodline.com, NewsNation 8 URLs, NTI staff, Hill, Middlesex DA): **all probably alive in browsers** but cannot be confirmed by automated fetch. Recommend annotating with a "link blocks automated checks; viewable in browser" footnote rather than re-tiering.

### Soft-404 (2)

| URL | First seen at | Note |
|---|---|---|
| `https://namus.nij.ojp.gov/missing-person-namus-mp150628` | `cases/casias.md:73` | Page loads but all case fields are empty — shell record, not populated. Annotate as "NamUs MP150628 record exists but fields are blank as of 2026-05-08." |
| `https://www.solvethecase.org/case/2025-56/monica-reza` | `cases/reza.md:133` | Case structure loads, content section empty. Same annotation pattern. |

### Redirected (1)

`https://www.losalamosnm.gov/News-articles/Search-Continues-Anthony-Chavez` → `https://www.losalamosnm.gov/News-media/Search-Continues-Anthony-Chavez` (path rename `News-articles` → `News-media`). Update citation in `cases/chavez.md:12`.

### Cross-cutting note

**Wayback CDX API was down during the sweep.** All "no Wayback available" findings should be re-checked when CDX is restored — the availability API only returns the closest single snapshot and may report empty even when snapshots exist. Worth a re-run (5-min job) before the next session's commit.

---

## Agent D — Foreign-source bias audit

### Cleanest finding: Tier 7 vs Tier 8 mislabeling (4 citations)

Per `README.md` source-tier definitions: **Tier 7 = independent commentary / Substack / YouTube / TikTok / podcasts / social media**; **Tier 8 = foreign state-affiliated press**. The dossier defines Tier 8 specifically for state-funded outlets but applies Tier 7 in two foreign-coverage files:

| Outlet | File:line | Current | Should be |
|---|---|---|---|
| RT (Russia Today) | `appendices/foreign-coverage/russia.md:7` | Tier 7 | **Tier 8** |
| Pravda UK | `appendices/foreign-coverage/russia.md:14` | Tier 7 | **Tier 8** |
| Tehran Times | `appendices/foreign-coverage/iran.md:7` | Tier 7 | **Tier 8** |
| Press TV | `appendices/foreign-coverage/iran.md:15` | Tier 7 | **Tier 8** |

`appendices/foreign-coverage/china.md:7` correctly tags Global Times at Tier 8 — proving the convention is known. Fix is purely categorical (no judgment call needed).

### Tier-treatment inconsistencies between U.S. and foreign equivalents

| Outlet | Country | File:line | Current | Proposed | Reasoning |
|---|---|---|---|---|---|
| Daily Mail | UK | `cases/maiwald.md:67`, foreign-coverage/UK | Tier 4 | **Tier 5** OR demote-to-match | Daily Mail is the canonical Tier-6 originator (per README's KCNSC example) but its outlet-level tier is Tier 4; meanwhile Mirror US (also UK national tabloid) is Tier 5. Pick one — they cannot diverge. |
| Mirror US | UK | `cases/eskridge.md:95` | Tier 5 | **Match Daily Mail** | If Daily Mail is Tier 4, Mirror US should be Tier 4. Current asymmetry favors one UK tabloid over another for no editorial-content reason. |
| Primetimer | U.S. | `cases/eskridge.md:84` | Tier 4 | **Tier 5** | Counter-direction U.S.-over-tiered finding. Primetimer is an entertainment-aggregation site, structurally equivalent to Britannia Daily (UK Tier 5) and Northeast Live TV (India Tier 5). README's Tier 4 list is "CNN/CBS/ABC/NBC/Reuters/AP/WaPo/NYT" — Primetimer doesn't qualify. |
| Unilad Tech | U.S./UK | `cases/eskridge.md:85` | Tier 4/5 hedge | **Tier 5** | Same logic — pick a tier and apply consistently. The hedge mirrors the WION (India) "Tier 3-4" hedge. |
| WION | India | `appendices/foreign-coverage/india.md:8` | Tier 3-4 hedge | **Tier 4** | Independent commercial international broadcaster (Zee Media) — analogous to Newsweek/NewsNation, which are flat Tier 4 in this dossier. The hedge reads as origin-uncertainty. |

### Asymmetric language findings (4)

These are foreign-coverage descriptions that impute editorial intent in a way U.S.-coverage descriptions don't:

1. `appendices/foreign-coverage/russia.md:20-22` — RT/Pravda UK described with "credulity," "conspiracy-adjacent tone," "all-caps headline formatting" caveats. Fox News in `eskridge.md:81` (which carries similar UAP-conspiracy material) gets no such caveat. Either symmetric caveats or strip both.
2. `appendices/foreign-coverage/iran.md:26` — Press TV "framing emphasized American institutional vulnerability" is intent-imputation; comparable U.S.-outlet behavior in `cases/garcia.md:30` (Fox News repeating Daily Mail's anonymous claim) is described in forensic, not editorial-intent terms. Recommend symmetric language.
3. `appendices/foreign-coverage/iran.md:40` — "Tehran Times dressed up unsubstantiated geopolitical theorizing in technical language" imputes intent. Same charge could be levied at Daily Mail's anonymous-source framing — but isn't. Drop intent imputation across the board, or apply symmetrically.
4. `appendices/foreign-coverage/china.md:31` — "By emphasizing the UFO theories... the coverage implicitly portrays U.S. governance and media culture as prone to conspiracy thinking." Newsweek's "List of dead or missing scientists 'suspicious'" headline gets no parallel inferential caveat. Apply symmetric framing.

### Structural observation (for future discussion)

The README's Tier 8 ("Foreign state-affiliated press") is **itself a structural origin-bias** — there is no parallel skeptical Tier for U.S. state-adjacent or partisan outlets. The user's stated standing rule ("National mainstream = Tier 4 regardless of country") is in tension with Tier 8's existence as a separate, by-definition-lower category for state-affiliated foreign outlets. **Cleanest long-term fix** would be to evaluate state-press articles on content (propaganda → Tier 5/6, news-aggregation → Tier 4) rather than maintaining a blanket origin tier. **Out of scope for this cleanup commit** — flagging as a methodology question for Phase 7.

---

## Agent E — Alias-resolver scan

### Glossary fixes (clean wins)

| Acronym | Glossary current | Should be | Why |
|---|---|---|---|
| `JPL` | `Jet Propulsion Laboratory (NASA)` | `NASA Jet Propulsion Laboratory` | All case files and the diagram label use NASA-as-prefix; glossary uses NASA-as-parenthetical. Mismatch. |
| `MSFC` | `Marshall Space Flight Center (NASA)` | `NASA Marshall Space Flight Center` | Same NASA-prefix issue. |
| `PSFC` | `Plasma Science and Fusion Center (MIT)` | `MIT Plasma Science and Fusion Center` | All files use MIT-as-prefix. |
| `ATA` | `Applied Technology Associates` | `Applied Technology Associates (BlueHalo subsidiary)` | Glossary entry orphans the BlueHalo relationship that's central to McCasland's profile. |

### Glossary-gap entities (no entry currently — add)

| Entity | Used in | Proposed entry |
|---|---|---|
| Sandia National Laboratories | `dossier.md`, both analysis files, diagram | new acronym entry SNL → "Sandia National Laboratories" + bare-form for "Sandia" |
| Kirtland AFB | `cases/mccasland.md`, `analysis/hypotheses.md`, `analysis/connection-analysis.md`, `dossier.md` | full-form "Kirtland Air Force Base, Albuquerque, NM" |
| Riverside Research | `cases/mccasland.md`, diagram (affiliation only — no node) | full-form, no acronym; flag as orphan affiliation |
| Institute for Exotic Science | `cases/eskridge.md`, diagram (affiliation only — no node) | full-form, no acronym |
| HoloChron LLC | `cases/eskridge.md`, diagram (affiliation only — no node) | full-form |
| Aerojet Rocketdyne | `cases/reza.md`, diagram | full-form, no acronym |
| Honeywell FM&T | `cases/garcia.md` description, diagram description | "Honeywell Federal Manufacturing & Technologies" (KCNSC operator) |

### Diagram-affiliation-string vs node-label mismatches

Person-node `affiliation` strings frequently use the acronym alone (`"JPL"`, `"LANL"`, `"AFRL"`, `"MIT PSFC"`, `"Novartis"`) while institution nodes use full labels (`"NASA Jet Propulsion Laboratory (JPL)"`, etc.). For any future tooling that joins person → institution by string match, this fragments the graph. **Two fix options** (Phase 7 decision):
- (a) Standardize all affiliations to the full label form, OR
- (b) Add an explicit `institution_node_id` field to person-node affiliation metadata.

For this cleanup commit: **flag only**, do not change diagram structure (Phase 7 territory).

### Specific diagram-node observations

- `inst-jpl` label `"NASA Jet Propulsion Laboratory (JPL)"` — node fine; affiliation strings (`"JPL"`) fragment.
- `inst-caltech-ipac` label `"Caltech / IPAC"` (with spaces) vs affiliation `"Caltech/IPAC"` (no spaces) — cosmetic, pick one.
- `inst-bluehalo` label `"Applied Technology Associates / BlueHalo"` vs affiliation `"Applied Technology Associates/BlueHalo"` — same spacing issue.
- `inst-novartis` label `"Novartis Institutes for Biomedical Research"` vs affiliation `"Novartis"` — bare parent-brand affiliation while node is the specific research subsidiary; ambiguity.
- **No true duplicate institution nodes exist** — all 9 institution + 1 related-institution nodes (`inst-nasa-msfc`) map to distinct entities. The "JPL ↔ Caltech" relationship is correctly preserved as two separate-but-related entities (both are Caltech-managed, but JPL and IPAC are institutionally distinct).

### Predecessor-entity dangling references

`cases/reza.md:26-27` references "Rocketdyne (Rockwell International division)" and "Rockwell Science Center" as Reza's early employers. These are historical predecessors of Aerojet Rocketdyne (now part of L3Harris). Diagram node `inst-aerojet` description mentions L3Harris (forward step) but not Rockwell (backward step). For reader-tracing purposes, add a corporate-history note to `inst-aerojet`'s description.

---

## Cross-cutting observations

1. **Agents A and B converge on the same over-link findings.** `dossier.md` (House Oversight Committee, FBI investigation), `cases/chavez.md` (LAPD, NM DPS), `cases/reza.md` (LASD). One de-link pass covers both audits — no work duplication.

2. **Agents B and E both flag the JPL/MSFC/PSFC name-order inconsistency.** Glossary uses `(NASA)`/`(MIT)` parenthetical; case files and diagram use NASA/MIT as prefix. Single fix: update glossary entries.

3. **Agents B, C, and E converge on `data/glossary.json` needing edits.** B finds 3 missing acronyms (IGIC, USAF, C4ISR); E finds 3-7 missing institution entries (Sandia, Kirtland AFB, Riverside Research, etc.) and 4 ordering fixes; C finds 1 dead URL in glossary (`https://www.lanl.gov/`). Single glossary-edit pass handles all three.

4. **Agent C's bot-block findings need symmetric treatment.** Many "403" results are alive in browsers (oversight.house.gov, IBTimes UK, brookline.news, NewsNation, Legacy.com, ResearchGate). Recommended convention for the cleanup commit: **leave the URLs, add a footnote convention** like `*(automated checks blocked — viewable in-browser)*` rather than retire links that work for human readers.

5. **Wayback CDX was down during sweep — re-run before commit.** Agent C's "no Wayback available" findings are unreliable. A 5-minute re-check when CDX is restored will surface recovery options for the 4 truly-dead URLs. Cheap, do it before the commit.

6. **`LAPD` collision (Agent B) is the highest-priority cross-file consistency fix.** `cases/chavez.md` uses `LAPD` for "Los Alamos Police Department" while glossary canonically defines it as "Los Angeles Police Department." This is high-collision (LAPD is universally Los Angeles in any reader's mind) and should be resolved by spelling out "Los Alamos Police Department" in full throughout `cases/chavez.md` and *not* using the LAPD abbreviation at all in that file.

7. **Agent A and E both surface "no Wikipedia article" entities** — Joseph Rodgers (CSIS), Scott Roecker (NTI), Jennifer Coffindaffer, Franc Milburn, Honeywell FM&T, HoloChron LLC, Institute for Exotic Science. These are real entities with no Wikipedia footprint; the right enrichment is an institutional/about-page link or a credentials footnote, not a "needs Wikipedia link" tag.

---

## Proposed-edits checklist for next session's cleanup commit

Single ranked list, derived from all five agents. Order is pragmatic: highest-value, lowest-risk first.

### Tier 1 — clean categorical fixes (no judgment, applies-as-stated)

- [ ] **Tom DeLonge enrichment** — Wikipedia link + WikiLeaks email URL on first occurrence in `cases/mccasland.md` (line 27) and other files where his name is bare. *(SESSION-PLAN's "already resolved" item.)*
- [ ] **Tier 7 → Tier 8 retag** for state-affiliated foreign outlets in `appendices/foreign-coverage/russia.md` (RT line 7, Pravda UK line 14) and `appendices/foreign-coverage/iran.md` (Tehran Times line 7, Press TV line 15). Pure categorical correction — `china.md` already does this right.
- [ ] **Update glossary `JPL`/`MSFC`/`PSFC` entries** — change full-form expansions from `(NASA)`/`(MIT)` parenthetical to NASA/MIT prefix to match case-file and diagram convention.
- [ ] **Add 3 missing acronym entries to glossary**: `IGIC` (Intelligence Community Inspector General), `USAF` (U.S. Air Force), `C4ISR` (Command, Control, Communications, Computers, Intelligence, Surveillance, and Reconnaissance).
- [ ] **Update glossary `LANL` URL** — `https://www.lanl.gov/` is dead; either remove URL field or replace with a working LANL subdomain after research.
- [ ] **Update `cases/chavez.md:12` URL** — `losalamosnm.gov/News-articles/...` redirects to `News-media/...`. Single URL swap.
- [ ] **Update `appendices/primary-sources/casias/nm-missing-persons-database-entry.md:3`** — replace dead `dps.state.nm.us` URL with `dps.nm.gov` equivalent (record IDs are the same; new domain alive).

### Tier 2 — first-occurrence enrichment links (Wikipedia + primary-source where verified)

- [ ] **`dossier.md`**: Add Wikipedia + primary-source links for Karoline Leavitt (line 17), Rep. James Comer (line 17), Rep. Eric Burlison (line 17), Kash Patel (line 11), Nuno Loureiro (line 22), Carl Grillmair (line 22). Apply DeLonge template (Wikipedia + primary URL on first occurrence).
- [ ] **`cases/mccasland.md`**: Add Wikipedia link for Tom DeLonge (line 27, person — currently only the document is linked), John Podesta (line 27), TTSA / "To The Stars" (line 169).
- [ ] **`analysis/foreign-intel-layer.md`**: Add Wikipedia + DOE primary-source links for Chris Wright (line 81). Add Wikipedia for Chris Swecker (line 67), Michio Kaku (line 71). Add primary-source URL for AARO (`https://www.aaro.mil/`) — needs manual verification.
- [ ] **`appendices/named-expert-commentary/`**: Add Wikipedia links on first line of each — `ross-coulthart.md`, `luis-elizondo.md`, `steven-greer.md` (note `Steven_M._Greer`), `chris-wright-doe.md`, `chris-swecker.md`, `michio-kaku.md`.
- [ ] **`cases/eskridge.md:47`**: Add Wikipedia link for Michael Shellenberger.
- [ ] **`analysis/hypotheses.md:200`**: Add Wikipedia link for AARO on its first narrative occurrence.

### Tier 3 — over-link removal (drop redundant repeat-links)

- [ ] **`dossier.md`**: De-link "House Oversight Committee" at lines 17, 44, 109 (keep line 11). De-link "FBI investigation" at line 108 (keep line 11).
- [ ] **`cases/chavez.md`**: De-link `LAPD` at lines 13, 15, 23, 27, 29 (keep line 12). De-link `NM DPS` at lines 21, 23, 29, 31 (keep line 10).
- [ ] **`cases/reza.md`**: De-link `LASD` at line 93 (keep line 92).

### Tier 4 — acronym first-use expansion (29 instances)

Apply per Agent B's per-file checklist. High-value files first (most violations):
- [ ] `dossier.md` — 12 acronyms expand on first use.
- [ ] `analysis/foreign-intel-layer.md` — 12 acronyms expand on first use (or earliest narrative occurrence).
- [ ] `cases/maiwald.md` — 5 acronyms (SBG-VSWIR, COWVR, SWOT, DOD, DOE).
- [ ] `cases/hicks.md` — 4 acronyms (DART, DOD, DOE, FOIA).
- [ ] `cases/mccasland.md` — 4 acronyms (OUSD(AT&L), SAPOC, AFRL, SAP).
- [ ] `analysis/hypotheses.md` — 4 acronyms (IGIC, CSIS, NTI, SAPOC).
- [ ] `analysis/connection-analysis.md` — 4 acronyms (IPAC, KCNSC, PSFC, plus DART/NEAT/SBG-VSWIR/AMR/HIFI).
- [ ] `cases/casias.md` — 3 acronyms (NamUs, NMSP, NNSA).
- [ ] `cases/garcia.md` — 3 acronyms (KCNSC, APD, NNSA).
- [ ] `cases/chavez.md` — 2 acronyms (LAPD-rename, NNSA).
- [ ] `cases/eskridge.md` — 2 acronyms (MSFC, DEW).
- [ ] `cases/grillmair.md` — 2 acronyms (NEOWISE, LASD).
- [ ] `cases/thomas.md` — 1 acronym (NEMLEC).

### Tier 5 — LAPD collision fix (HIGH-PRIORITY consistency)

- [ ] **`cases/chavez.md`**: Replace every use of the abbreviation `LAPD` with full-spelled "Los Alamos Police Department" (or short bare "Los Alamos PD"). Glossary canonically defines `LAPD` = Los Angeles Police Department; using LAPD for Los Alamos PD in this file creates collision risk for any reader. Do NOT add "Los Alamos PD (LAPD)" — the abbreviation should be retired from this file entirely.

### Tier 6 — broken-link annotations (per scratch.txt convention)

- [ ] **Annotate the 4 truly-dead URLs** (after Wayback CDX re-check confirms no recovery): `lanl.gov` glossary URL, `dps.state.nm.us` legacy domain (already covered above), `ipac.caltech.edu/people/staff/carl_grillmair`, `daytondailynews.com` Mccasland article.
- [ ] **Annotate 2 soft-404 URLs**: `namus.nij.ojp.gov/missing-person-namus-mp150628` (in `cases/casias.md:73`) and `solvethecase.org/case/2025-56/monica-reza` (in `cases/reza.md:133`) — note "record exists but content fields are blank as of 2026-05-08."
- [ ] **Add bot-block convention** for 32 403 URLs that are alive in-browser (legacy.com obits, NewsNation, IBTimes UK, oversight.house.gov, brookline.news, etc.) — add an inline footnote like `*(blocks automated checks; viewable in browser)*` rather than retire the links.

### Tier 7 — foreign-source asymmetric language (Phase 2 territory mostly)

- [ ] **Symmetric framing or strip-from-both** — choose either to add caveats to U.S. outlets running similar UAP/aggregation material (Fox News, Newsweek, NewsNation) or remove intent-imputing language from foreign-coverage descriptions (russia.md, iran.md, china.md). Recommend the latter — describe behavior, not intent. **Discuss in Phase 2 voice audit; flag here for cross-reference.**

### Tier 8 — items that need-human-judgment (don't bulk-edit)

- [ ] **Daily Mail vs Mirror US tier consistency** — pick a tier and apply across the dossier. Not a clean categorical fix; needs a methodology call.
- [ ] **Primetimer Tier 4 → Tier 5 demote** — confirm with you; Agent D's reasoning is solid (entertainment-aggregation site, structurally below the README's Tier 4 list).
- [ ] **Coffindaffer/Milburn/Rodgers/Roecker** — no Wikipedia article exists; decide on credential-footnote vs. organizational-link pattern for each.
- [ ] **WION Tier 3-4 hedge → flat Tier 4** — confirm with you.
- [ ] **AARO `aaro.mil` URL** — verify manually (.mil domain didn't fetch automatically) before adding as primary-source link.
- [ ] **Diagram affiliation-string standardization** (Agent E option a vs b) — Phase 7 territory; do NOT change in cleanup commit.
- [ ] **Tier 8 structural question** — keep as separate origin-based tier or move to content-based evaluation? Methodology question; defer to Phase 7 discussion.

### Tier 9 — pre-commit hygiene

- [ ] **Re-run Wayback CDX** for the 4 truly-dead URLs once `web.archive.org/cdx/` is back up. Cheap; before commit.
- [ ] **Apply revision-marker convention** per SESSION-PLAN session-3 spec on every file touched: top-of-file `*Last revised: 2026-05-08*` line + inline `*(updated 2026-05-08 — see GitHub for details)*` markers where existing prose was reworded.
- [ ] **Tag current HEAD `pre-rebalance-2026-05-06`** before reviewing findings (preserves the pre-rebalance baseline; per SESSION-PLAN session 3 step 1).

---

## Stop conditions met

- [x] All five agents returned without errors.
- [x] Findings consolidated into single doc.
- [x] No edits to research content (`dossier.md`, `cases/*.md`, `analysis/*.md`, `appendices/`, `data/`, `glossary.json`).
- [x] No commits, no pushes.

Next session per SESSION-PLAN session 3: tag `pre-rebalance-2026-05-06`, review this doc together, single commit pass applying approved Tier-1 through Tier-6 edits with revision markers.
