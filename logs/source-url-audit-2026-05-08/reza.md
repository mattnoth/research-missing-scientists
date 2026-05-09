# Source-URL Audit — Reza (2026-05-08)

## Summary

- **0** citations in `cases/reza.md` point to a local audit page only — the case file already uses direct inline URLs throughout. Convention is correct; no patching needed on that axis.
- **1** inline URL is a soft-404 (solvethecase.org loads but has no case data populated)
- **3** URLs returned 403 (oversight.house.gov, ktla.com secondary in audit page, thehill.com)
- **1** audit page (`la-county-sheriff-missing-hiker-search.md`) is an orphan — not cited from the case file
- **5** audit pages exist; all have `Source URL` recorded
- **0** binaries / downloadable files in the audit folder
- All 3 Google Patents URLs verified 200 with correct content
- All 2 Sentinel Briefing URLs verified 200 with correct content
- solvethecase.org entry annotated in case file header as soft-404 as of 2026-05-08 (already noted)

---

## Detail — Inline URLs already in case file (verify for 403 / soft-404 / local-archive candidacy)

All citations in `cases/reza.md` are direct external URLs. There are no local-audit-page-only citations to patch. The following records the verification status of every cited URL.

---

### S1 — solvethecase.org (LASD missing person listing)

- **Case-file lines:** L94, L95, L98 — `[LASD](https://www.solvethecase.org/case/2025-56/monica-reza)`; also L68 (narrative), L135 (Sources table)
- **Audit page:** `appendices/primary-sources/reza/lasd-missing-person-listing.md`
- **Source URL:** https://www.solvethecase.org/case/2025-56/monica-reza
- **Verification status:** 200 — but **soft-404**: page loads as a structural template; case-data fields (name, date, description) are blank as of 2026-05-08. The record exists at the URL but content is unpopulated.
- **Binary?** No
- **Action recommended:** Already annotated in case-file header (line 3) and Sources table (line 135). Confirm the audit page reflects the soft-404 state. Consider Wayback snapshot of any prior populated version.
- **Notes:** The case-file header note ("record exists; content fields blank as of 2026-05-08") accurately captures current state. No further patching needed unless a populated snapshot is located.

---

### S2 — crescentavalleyweekly.com (Vienna/LASD statement)

- **Case-file lines:** L78, L96, L97 — `[Acting Captain Ryan A. Vienna](https://www.crescentavalleyweekly.com/news/07/03/2025/update-on-efforts-to-locate-missing-hiker-monica-reza/)`; also L136 (Sources table)
- **Audit page:** `appendices/primary-sources/reza/lasd-vienna-statement-2025-07-03.md`
- **Source URL:** https://www.crescentavalleyweekly.com/news/07/03/2025/update-on-efforts-to-locate-missing-hiker-monica-reza/
- **Verification status:** 200 — page loads; article title "Update On Efforts to Locate Missing Hiker Monica Reza" confirmed; key Vienna quotes present.
- **Binary?** No
- **Action recommended:** Consider local archive — this is a small community paper and a primary law-enforcement statement. High value to preserve.
- **Notes:** Content matches audit page excerpts exactly.

---

### S3 — Google Patents US20100266442A1

- **Case-file lines:** L66, L99, L100 — `[Mondaloy](https://patents.google.com/patent/US20100266442A1/en)`; also L137 (Sources table)
- **Audit page:** `appendices/primary-sources/reza/patent-us20100266442a1.md`
- **Source URL:** https://patents.google.com/patent/US20100266442A1/en
- **Verification status:** 200 — loads; title "Burn-resistant and high tensile strength metal alloys," inventors Monica A. Jacinto and Dallis Ann Hardwick confirmed. Patent status: Abandoned.
- **Binary?** No (HTML page; PDF available via USPTO but not currently archived locally)
- **Action recommended:** Consider archiving the USPTO PDF version for permanence.
- **Notes:** Content matches audit page. Audit page notes patent is abandoned but does not note the assignee chain (individual → Boeing → Pratt & Whitney Rocketdyne per other patent records); minor enrichment opportunity.

---

### S4 — Google Patents US20030053926A1

- **Case-file lines:** L33 (Key Dates), L138 (Sources table)
- **Audit page:** None — not backed by a dedicated audit page. (Covered by cross-reference in `patent-us20100266442a1.md`.)
- **Source URL:** https://patents.google.com/patent/US20030053926A1/en
- **Verification status:** 200 — loads; title "Burn-resistant and high tensile strength metal alloys," inventors Monica Jacinto and Dallis Hardwick confirmed. Assignee: Boeing Company. Status: Abandoned (failed to respond to office action, June 2004).
- **Binary?** No
- **Action recommended:** Create dedicated audit page or expand `patent-us20100266442a1.md` to cover all three patent numbers explicitly.
- **Notes:** Boeing Company listed as assignee on this filing (not individual as stated in patent-us20100266442a1.md for the 2010 application). Minor discrepancy worth capturing.

---

### S5 — Google Patents US20040208777

- **Case-file lines:** L35 (Key Dates), L139 (Sources table)
- **Audit page:** None — same situation as S4.
- **Source URL:** https://patents.google.com/patent/US20040208777
- **Verification status:** 200 — loads; title "Burn-resistant and high tensile strength metal alloys," inventors Monica Jacinto and Dallis Hardwick confirmed. Assignee: Pratt & Whitney Rocketdyne (after chain). Status: Abandoned (2009).
- **Binary?** No
- **Action recommended:** Same as S4 — document in audit page.
- **Notes:** URL in case file omits `/en` suffix and the `A1` suffix (writes `US20040208777` not `US20040208777A1`). Google Patents resolves this via redirect, so it works, but normalizing to full canonical form (`US20040208777A1/en`) would be cleaner.

---

### S6 — House Oversight Committee press release

- **Case-file lines:** L88, L101 — `[House Oversight Committee](https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/)`; also L140 (Sources table)
- **Audit page:** None
- **Source URL:** https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/
- **Verification status:** **403** — request blocked. Government site; likely blocks automated fetches. May be accessible in browser. Wayback snapshot recommended.
- **Binary?** No
- **Action recommended:** Check Wayback Machine for a working snapshot; add Wayback URL as fallback. If the live page is browser-accessible (not truly down), annotate accordingly.
- **Notes:** This is a Tier 1 congressional record. 403 on automation does not mean the page is gone, but local archiving is high priority given gov-site volatility.

---

### S7 — FOX 11 Los Angeles

- **Case-file lines:** L114, L146 (Sources table) — https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza
- **Audit page:** None
- **Source URL:** https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza
- **Verification status:** 200 — loads; article dated April 18, 2026; content confirmed (Reza, Grillmair, Hicks, Maiwald LA County cluster; Leavitt quote).
- **Binary?** No
- **Action recommended:** No action required.
- **Notes:** URL uses foxla.com (FOX 11 LA domain). Content confirmed.

---

### S8 — Yahoo News / Men's Journal

- **Case-file lines:** L106, L108, L113 — `[Yahoo/Men's Journal](https://www.yahoo.com/news/articles/monica-reza-missing-scientist-strange-151253761.html)`; also L147 (Sources table)
- **Audit page:** None
- **Source URL:** https://www.yahoo.com/news/articles/monica-reza-missing-scientist-strange-151253761.html
- **Verification status:** 200 — loads; article title "Monica Reza Is a Missing Scientist: The Strange Circumstances of Her Disappearance" confirmed; key details (companion running, scent terminating at hat) confirmed.
- **Binary?** No
- **Action recommended:** Yahoo News syndication URLs are fragile over time. Consider archiving.
- **Notes:** Article describes 37+ years at Aerojet Rocketdyne and prior experience at "Pratt & Whitney" — the case file does not include the Pratt & Whitney detail; minor enrichment opportunity.

---

### S9 — Newsweek (FBI investigating)

- **Case-file lines:** L88, L148 (Sources table) — `[FBI](https://www.newsweek.com/fbi-investigating-missing-dead-scientists-what-we-know-11852176)`
- **Audit page:** None
- **Source URL:** https://www.newsweek.com/fbi-investigating-missing-dead-scientists-what-we-know-11852176
- **Verification status:** 200 — loads; title "FBI Investigating Missing and Dead Scientists: What We Know So Far" confirmed; Kash Patel quote confirmed.
- **Binary?** No
- **Action recommended:** No action required.

---

### S10 — Newsweek (Comer "national security threat")

- **Case-file lines:** L149 (Sources table)
- **Audit page:** None
- **Source URL:** https://www.newsweek.com/top-republican-says-dead-missing-scientists-national-security-threat-11855262
- **Verification status:** 200 — loads; title "Top Republican Says Dead, Missing Scientists Are 'National Security Threat'" confirmed; Comer quotes confirmed.
- **Binary?** No
- **Action recommended:** No action required.

---

### S11 — The Hill

- **Case-file lines:** L150 (Sources table)
- **Audit page:** None
- **Source URL:** https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/
- **Verification status:** **403** — request blocked. The Hill is known to block automation.
- **Binary?** No
- **Action recommended:** Verify manually in browser. If accessible, consider Wayback snapshot. Low urgency (T4 source, not cited inline in narrative).
- **Notes:** Only appears in Sources table; not cited in narrative body. Lower archival priority than S6.

---

### S12 — Fortune

- **Case-file lines:** L151 (Sources table)
- **Audit page:** None
- **Source URL:** https://fortune.com/2026/04/19/federal-government-investigation-disappearances-deaths-nuclear-space-scientists-energy-secretary-chris-wright-trump/
- **Verification status:** 200 — loads; title "Federal government launches broad probe into mysterious disappearances and deaths of top scientists" confirmed; Chris Wright quote confirmed.
- **Binary?** No
- **Action recommended:** No action required.

---

### S13 — Wikipedia (Monica Jacinto)

- **Case-file lines:** L114, L157 (Sources table)
- **Audit page:** None
- **Source URL:** https://en.wikipedia.org/wiki/Monica_Jacinto
- **Verification status:** 200 — loads; article confirmed; last updated May 1, 2026.
- **Binary?** No
- **Action recommended:** No action required. Wikipedia is inherently unstable; no local archive needed.

---

### S14 — Sentinel Briefing "The Green Burial"

- **Case-file lines:** L118, L125, L163 (Sources table) — `[Sentinel Briefing investigation](https://thesentinel.network/p/the-green-burial-she-was-declared)`
- **Audit page:** `appendices/primary-sources/reza/find-a-grave-memorial-anomaly.md`
- **Source URL:** https://thesentinel.network/p/the-green-burial-she-was-declared
- **Verification status:** 200 — loads; article title "The Green Burial" confirmed; published March 16, 2026; Find a Grave memorial details confirmed; no paywall.
- **Binary?** No
- **Action recommended:** Consider local archive given Substack volatility. High evidentiary value (Find a Grave anomaly is a key claim).
- **Notes:** Audit page (`find-a-grave-memorial-anomaly.md`) source URL matches and content is consistent.

---

### S15 — Sentinel Briefing "The Phone Gap"

- **Case-file lines:** L107, L109, L110, L112, L119 — `[Sentinel Briefing](https://thesentinel.network/p/the-phone-gap-monica-rezas-cell-phone)`; also L164 (Sources table)
- **Audit page:** None
- **Source URL:** https://thesentinel.network/p/the-phone-gap-monica-rezas-cell-phone
- **Verification status:** 200 — loads; article title "THE PHONE GAP: Cell Phone Forensic Data Was Obtained in the Monica Reza Case. It Has Never Been Released." confirmed; published March 23, 2026; Montrose SAR acknowledgment confirmed; no paywall.
- **Binary?** No
- **Action recommended:** Create audit page; consider local archive. This URL is cited inline 5 times across multiple claim categories and has no backing audit page.
- **Notes:** Comments section includes a claim from "Adriana Jacinto Ostling" that "Monica's phone was reported dead." Not currently captured in the case file; may warrant a note under Cell Phone Evidence.

---

## Orphan Audit Page

### la-county-sheriff-missing-hiker-search.md

- **Audit page:** `appendices/primary-sources/reza/la-county-sheriff-missing-hiker-search.md`
- **Status:** Not cited from `cases/reza.md` — orphan.
- **Source URL:** https://www.cbsnews.com/losangeles/news/angeles-national-forest-missing-hiker-monica-reza/ (primary); https://ktla.com/news/local-news/initial-search-phase-concludes-southern-california-hiker-still-missing/ (secondary)
- **CBS URL verification:** 200 — loads; article "Search continues for missing 60-year-old hiker in Angeles National Forest" confirmed; dated June 23, 2025.
- **KTLA URL verification:** **403** — blocked.
- **Action recommended:** Either cite these sources in the case file (CBS is a T3 local TV source corroborating the search timeline) or document why the audit page was not promoted to a citation. KTLA secondary URL should be flagged as 403.

---

## URL-Already-Inline (consider local archive)

The following inline URLs are verified 200 and are good candidates for local archiving given source fragility or evidentiary weight:

| URL | Reason |
|---|---|
| https://www.crescentavalleyweekly.com/…/update-on-efforts-to-locate-missing-hiker-monica-reza/ | Small community paper; primary LE statement |
| https://thesentinel.network/p/the-green-burial-she-was-declared | Substack; key evidentiary claim (Find a Grave anomaly) |
| https://thesentinel.network/p/the-phone-gap-monica-rezas-cell-phone | Substack; 5 inline citations; no audit page |
| https://www.yahoo.com/news/articles/monica-reza-missing-scientist-strange-151253761.html | Yahoo syndication URLs frequently expire |
| https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/ | 403 on automation; gov page; high priority |

---

## No-Primary-URL Audit Pages

None — all five audit pages in `appendices/primary-sources/reza/` have a `Source URL` recorded.

---

## 403 Summary

| URL | Context | Priority |
|---|---|---|
| https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/ | T1 congressional record; cited inline + Sources table | High |
| https://ktla.com/news/local-news/initial-search-phase-concludes-southern-california-hiker-still-missing/ | Secondary URL in orphan audit page only | Low |
| https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/ | T4 national news; Sources table only | Low |
