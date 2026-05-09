# Source-URL Audit — Casias (2026-05-08)

## Summary

- **0 citations point to local audit pages only** — no inline citation in `cases/casias.md` links to any `../appendices/primary-sources/casias/*.md` file
- **2 audit-page Source URLs not yet inline in case file** (see "Audit-page URLs missing from case file" section)
- **11 URLs already inline** in case file; verified below
- **10 URLs returned 200** (some implicitly — page content confirmed)
- **2 URLs returned 403** (nbcnews.com/dateline, krqe.com)
- **0 downloadable binary URLs identified**
- **1 audit page has no standalone primary URL** (`nmsp-statements.md` — all citations are via media; the media URLs are already inline in the case file)
- **1 NamUs URL is a soft-404** — page loads but all data fields are blank (confirmed pattern documented in case file)

---

## Detail

### No local-audit-page-only citations found

A grep for `../appendices/primary-sources/casias/` in `cases/casias.md` returned zero matches. Every inline citation in the case file already uses a direct external URL. There are no citations of the target type (local-audit-page only) in this file.

Wave 2 patch action for this file: **none of type "replace local link with primary URL."**

---

## Inline URL Verification (URL-already-inline)

All URLs extracted from `cases/casias.md` and verified below.

### URL 1 — NamUs MP150628
- **Case-file line:** L75 — `https://namus.nij.ojp.gov/missing-person-namus-mp150628 *(record exists; content fields blank as of 2026-05-08)*`
- **Verification status:** 200 (page loads; data fields dynamically populated but blank — soft-404 pattern)
- **Binary?** No
- **Action recommended:** No patch needed. Existing annotation `*(record exists; content fields blank as of 2026-05-08)*` is correct and sufficient.
- **Notes:** NamUs pages load via JS; WebFetch confirmed the record shell exists with no populated fields. The case file already documents this accurately.

### URL 2 — ABQ Journal (primary reporting article)
- **Case-file lines:** L16, L17, L18, L19, L20, L21, L22, L25, L83 — `https://www.abqjournal.com/news/taos-county-woman-lanl-employee-missing-for-two-months/497899`
- **Verification status:** 200 — article confirmed live with substantive content (factory-reset phones, timeline, volunteer search, reward details)
- **Binary?** No
- **Action recommended:** No change needed. Already inline; content confirmed.

### URL 3 — Santa Fe New Mexican
- **Case-file lines:** L16, L18, L19, L20, L22, L82 — `https://www.santafenewmexican.com/news/local_news/state-police-investigates-disappearance-of-lanl-worker-from-ranchos-de-taos/article_5e975bb9-e5d2-4853-8368-06504c936020.html`
- **Verification status:** 200 — article confirmed live (physical description, timeline, 125 volunteers, phone-wiping quote from niece)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 4 — Taos News, "Family divided" (July 9, 2025)
- **Case-file lines:** L23, L84 — `https://www.taosnews.com/public-safety/family-divided-amid-search-for-missing-lanl-worker/article_b113f95a-a27b-5edf-9771-7c7cb27abc6a.html`
- **Verification status:** 200 — article confirmed live (family conflict, FBI/DHS involvement noted, phones wiped detail, $2,500 reward)
- **Binary?** No
- **Action recommended:** No change needed.
- **Notes:** Previously noted as "not fully accessible" in case file (line 128, open question 4). WebFetch confirms the article is now accessible with substantive content. Wave 2 may want to update the open question to reflect that the article IS accessible and summarize what it says about the family division.

### URL 5 — Taos News, "Every angle" (July 23, 2025)
- **Case-file lines:** L24, L85 — `https://www.taosnews.com/public-safety/state-police-consider-every-angle-of-melissa-casias-disappearance/article_c218ed80-fc97-531d-ae54-d84c83fe9efd.html`
- **Verification status:** 200 — article confirmed live (blue truck cleared, phones wiped confirmed, voluntary departure theory noted)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 6 — Taos News, "No breakthroughs" (Sept 3, 2025)
- **Case-file lines:** L26, L86 — `https://www.taosnews.com/public-safety/state-police-report-no-breakthroughs-in-melissa-casias-case/article_0cfb4a66-9422-5e23-9040-74378e898ee8.html`
- **Verification status:** 200 — article confirmed live (Wilson Silver quoted, $2,500 reward, NM 518 sighting confirmed)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 7 — NBC Dateline
- **Case-file line:** L87 — `https://www.nbcnews.com/dateline/missing-in-america/melissa-casias-new-mexico-missing-rcna219956`
- **Verification status:** 403 — blocked to bots; candidate for user browser-access confirmation
- **Binary?** No
- **Action recommended:** User must confirm browser access. If live, no change needed (URL already inline). If dead, mark with `*(link may require direct browser access)*`.

### URL 8 — KOB, "4 missing persons with nuclear ties"
- **Case-file line:** L88 — `https://www.kob.com/new-mexico/4-missing-persons-with-nuclear-ties-spark-concern-in-new-mexico/`
- **Verification status:** 200 — article confirmed live (all four NM cases covered, White House acknowledgment, expert caution on pattern-finding)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 9 — CBS News, "Deaths and disappearances"
- **Case-file line:** L89 — `https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/`
- **Verification status:** 200 — article confirmed live (FBI investigation into 10 cases, DOE involvement, Casias referenced)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 10 — KOB, "Family still looking" (July 25, 2025)
- **Case-file line:** L90 — `https://www.kob.com/news/top-news/family-of-taos-woman-still-looking-for-her-a-month-after-disappearance/`
- **Verification status:** 200 — article confirmed live (doorbell camera footage, $7,500 combined reward, blue truck/highway witness detail)
- **Binary?** No
- **Action recommended:** No change needed.

### URL 11 — KRQE, "8th week"
- **Case-file line:** L91 — `https://www.krqe.com/news/new-mexico/search-for-missing-los-alamos-national-laboratory-employee-goes-into-8th-week/`
- **Verification status:** 403 — blocked to bots; candidate for user browser-access confirmation
- **Binary?** No
- **Action recommended:** User must confirm browser access. If live, no change needed. If dead, mark with `*(link may require direct browser access)*`.

---

## Audit-page URLs Missing from Case File

Two audit pages contain Source URLs that do not appear anywhere in `cases/casias.md`. These are not "local-audit-page-only citations" (there are none of those), but they represent sourcing documented in the audit layer that has not been surfaced inline in the case file. Flagging for Wave 2 to decide whether to add them.

### Missing URL A — NM DPS Missing Persons Database
- **Audit page:** `appendices/primary-sources/casias/nm-missing-persons-database-entry.md`
- **Source URL:** `https://missingpersons.dps.nm.gov/mpweb/mpdetailreport_serv?id=M100749`
- **Verification status:** 200 — record confirmed live with Casias's photo, physical description (age 54, 5'4", brown hair/eyes), last known clothing, and NMSP hotline contact
- **Binary?** No
- **Currently cited in case file?** No. The case file mentions NamUs (T1) in the Primary Sources table but does not cite the NM DPS state database entry separately.
- **Action recommended:** Consider adding to Primary Sources table as a second T1 source (NM DPS is a state law-enforcement database, complementary to NamUs). Would strengthen the documented basis for NMSP's "missing, endangered" classification.

### Missing URL B — Los Alamos Reporter article (NMSP bulletin)
- **Audit page:** `appendices/primary-sources/casias/nmsp-missing-person-case.md`
- **Source URL:** `https://losalamosreporter.com/2025/07/07/new-mexico-state-police-seeks-53-year-old-melissa-shirley-casias-missing-from-taos-since-june-26/`
- **Verification status:** 200 — page confirmed live; article body text partially loaded (metadata/structure visible, byline and publication date confirmed July 7, 2025)
- **Binary?** No
- **Currently cited in case file?** No. The case file cites ABQ Journal, Santa Fe New Mexican, and Taos News as T3 sources, but not the Los Alamos Reporter article that explicitly reproduces the NMSP missing-person bulletin.
- **Action recommended:** Consider adding to Secondary Sources table. The Los Alamos Reporter piece is a direct relay of the NMSP bulletin and closer to a T2 source than the longer-form reporting; it may be useful if other T3 articles go behind a paywall.

---

## No-primary-URL Audit Pages

### `appendices/primary-sources/casias/nmsp-statements.md`
- **Status:** No standalone primary URL. The audit page explicitly notes: "No standalone NMSP press release was located on the NMSP website." All cited URLs in the audit page are T3 media articles (ABQ Journal, Taos News, Santa Fe New Mexican) already inline in the case file.
- **Action:** No case-file patch needed. The "via media" attribution is correctly documented. Wave 2 may annotate the audit page to note that this page's function is documentation of the absence of a standalone NMSP release, not a primary-URL redirect.

---

## Open Question for Wave 2 (not a citation issue)

- **Taos News "family divided" article (URL 4 above):** The case file's open question #4 (line 128) says the article was "not fully accessible." WebFetch on 2026-05-08 returned substantive content including: confirmed family conflict between daughter/niece, FBI and DHS involvement reported, blue truck cleared, phones wiped. Wave 2 should update open question #4 to reflect current accessibility and incorporate the FBI/DHS involvement detail, which is not currently mentioned in the case file narrative.
