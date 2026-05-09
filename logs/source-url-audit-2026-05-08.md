# Source-URL Audit — Consolidated (2026-05-08)

Per-case detail in `logs/source-url-audit-2026-05-08/{case}.md`. This file is the master summary used to plan Wave 2 patches.

## Scope clarification

The session prompt anticipated widespread "case-file inline citation links only to a local audit page" patterns. Wave 1 found this is **not** the dominant pattern. Out of 11 case files, only **3 cases** have any such citations to patch: mccasland (1 missed in worked-example pass), garcia (2), grillmair (3). The other 8 cases already use direct external URLs as primary inline citations.

The work that *is* live for Wave 2:

1. **Citation-link patches** — narrow (6 lines across 3 files).
2. **Audit-page hygiene** — broader (annotate no-primary-URL pages, fix stale Source URL paths, consolidate duplicates).
3. **Local-archive downloads** — selective (HAL5 PDF, possibly JPL dataverse PDF, BCSO PDF already done).
4. **Inventory of 403-blocked URLs** — for user browser-access confirmation pass.

Several findings are **out of scope** for this session (content gaps, voice issues, orphan audit pages with no inline citation) and are routed to `TODO-research.md` instead of patched here.

---

## Wave 2 patch plan

### A. Citation-link patches (URL-primary + reconstruction-notes-secondary)

| Case | Line | Audit page | URL to add | Verified |
|---|---|---|---|---|
| mccasland | L30 (Key Dates, Riverside Research entry) | `riverside-research-appointment.md` | https://www.prnewswire.com/news-releases/riverside-research-elects-major-general-usaf-retired-william-n-mccasland-to-its-board-of-trustees-300921796.html | 200 |
| garcia | L74 (Primary Sources bullet, NM DPS) | `nm-dps-missing-persons.md` | https://missingpersons.dps.nm.gov/mpweb/mpdetailreport_serv?id=M101688 | 200 |
| grillmair | L86 (Primary Sources, Caltech memorial) | `caltech-memorial.md` | Caltech memorial URL (per audit page frontmatter) | 200 |
| grillmair | L87 (Primary Sources, LA County BoS) | `la-county-bos-adjournment.md` | kathrynbarger.lacounty.gov press release | 200 |
| grillmair | L88 (Primary Sources, LASD initial report) | `lasd-initial-report.md` | CBS LA + MyNewsLA URLs (no direct LASD URL exists; documented gap) | 200 |

### B. Audit-page no-primary-URL annotations

These audit pages have no `Source URL` (information was sourced from agency-to-journalist comms, not a standalone press release). Wave 2 annotates the audit page with explicit "No primary URL located — sourcing reconstructed from T3/T4 outlets quoting agency communications" rather than implying via-media is the access framing.

| Case | Audit page | Reason |
|---|---|---|
| garcia | `nnsa-statement.md` | NNSA statement delivered to journalists; never appeared as standalone press release on nnsa.energy.gov or kcnsc.doe.gov |
| casias | `nmsp-statements.md` | Already documents the absence of a standalone NMSP press release; verify annotation is in current convention |
| loureiro | `doj-confession-transcript-summary.md` | No `Source URL` field; the Jan 6 2026 DOJ/USAO-MA press release URL was never fetched and recorded |

### C. Audit-page Source-URL fixes

| Case | Audit page | Issue | Fix |
|---|---|---|---|
| chavez | `los-alamos-county-search-update.md` | Source URL has stale `/News-articles/` path | Update to `/News-media/` path (case file already uses corrected path) |
| chavez | `lapd-missing-person-notices.md` | Source URL has stale `/News-articles/` path | Same |

### D. Local-archive downloads (binaries)

| Case | Source | URL | Size | Notes |
|---|---|---|---|---|
| eskridge | HAL5 antigravity talk PDF | https://hal5.org/PDF/HAL5-Dec2018-Talk-AntiGravity.pdf | 2.4 MB | T1, only T1 binary; small non-profit with link-rot risk |
| mccasland | BCSO PDF | (already done in worked-example pass) | — | Verify present in folder |

Maiwald JPL dataverse PDF (3 MB) was flagged as a candidate but the dataset listed Pearson et al. as authors — Maiwald authorship needs cross-check before downloading. **Defer to future pass.**

### E. Audit-page consolidation (duplicates)

| Case | Issue | Fix |
|---|---|---|
| loureiro | `mit-statement-20251219.md` and `mit-statement-dec19-suspect-identified.md` point to same MIT URL | Consolidate into one canonical page |

---

## 403-blocked URLs — user browser-access confirmation needed

These are documented in audit pages or inline citations and return 403 to automated fetches. None block the patch work for Wave 2 (the URLs are the URLs regardless of fetch status), but they are candidates for a follow-up local-archive pass once user confirms browser access.

| Case | URL | Current citation context |
|---|---|---|
| casias | nbcnews.com/dateline (L87) | Inline |
| casias | krqe.com (L91) | Inline |
| chavez | losalamosnm.gov county press release (`/News-media/...`) | Inline + audit pages |
| eskridge | NewsNation `/father-dead-scientist-denies-suspicious/` | Inline |
| eskridge | Primetimer | Inline (returned 405) |
| hicks | dps.aas.org (AAS DPS obituary, T1) | Inline; recommend Wayback |
| hicks | oversight.house.gov (House Oversight press release, T1) | Inline; recommend Wayback |
| hicks | thehill.com | Inline |
| loureiro | NBC News Brown-suspect background piece | Inline (sole source for several quotes) |
| loureiro | NBC News initial professor-killed report | Secondary Sources |
| maiwald | ResearchGate | Inline |
| maiwald | House Oversight | Inline |
| maiwald | The Hill | Inline |
| maiwald | NewsNation | Inline |
| mccasland | NewsNation `/who-is-william-neil-mccasland/` | Inline |
| mccasland | NewsNation `/missing-air-force-general-wife-911/` | Inline |
| mccasland | NewsNation `/neil-mccasland-missing-timeline/` | Inline |
| reza | oversight.house.gov (T1, congressional record) | Inline (high priority) |
| reza | ktla.com | Audit page only (orphan) |
| reza | thehill.com | Sources table |
| thomas | middlesexda.com | Inline (×5 — but Wakefield town site mirror is 200 and parallel-cited) |
| thomas | NBC Dateline | Inline (×4) |
| thomas | researchgate.net | Inline |

**Recommended user action:** open each in a browser; if accessible, save the rendered page (Cmd-S → "Web Page, Complete") into `appendices/primary-sources/{case}/`. Wave 2 of *this* session does **not** depend on this — it's a follow-up pass.

---

## Out of scope for this session — routed to TODO-research.md

These are real findings from the audit but are content/voice/structure changes, not the inline-source-URL convention work:

1. **hicks.md** — `la-county-coroner-cause-of-death.md` documents cause (arteriosclerotic cardiovascular disease) and manner (natural) per LA County Coroner via Fox 11 LA. Open Question #1 in case file still says "no source has disclosed the cause of death." Needs case-file content update + closing of OQ#1.
2. **casias.md** — Taos News "family divided" article is now returning full content (FBI/DHS involvement). Currently marked "not fully accessible" in OQ#4. Needs content update.
3. **garcia.md** — `albuquerque-police-missing-person.md` is mislabeled (Newsweek-sourced content presented as APD primary document). Needs reclassification.
4. **grillmair** — `la-county-da-murder-charges-snyder.md` records bail at $2M; case file prose / Contradictions table records $3.175M consensus. Internal contradiction in audit page.
5. **reza** — Commenter on Sentinel "Phone Gap" article (identifying as Adriana Jacinto Ostling) claims "Monica's phone was reported dead." Not in case file Cell Phone Evidence section. Provenance uncertain (commenter, not journalist).
6. **reza** — Multiple S-numbered sources have no audit pages (S15 cited 5× inline with no backing page).
7. **maiwald** — `frank-maiwald-obituary.md` overstates "officials confirmed autopsy was never performed"; case file's hedge ("reportedly… not confirmed on-record") is correct.
8. **loureiro** — NBC News URL (sole source for "first in class" claim and Scott Watson quote) returning 403; needs Wayback or browser-archived alternative.
9. **mccasland** — Dayton Daily News URL confirmed dead (404); Wayback CDX was offline at last check; retry.

Full per-case detail in `logs/source-url-audit-2026-05-08/`.
