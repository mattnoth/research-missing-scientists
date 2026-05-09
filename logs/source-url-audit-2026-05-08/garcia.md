# Source-URL Audit — Garcia (2026-05-08)

## Summary

- 2 citations point to local audit pages only (lines 74–75, Primary sources section)
- 2 URLs verified 200
- 0 URLs returned 403
- 0 URLs are downloadable binaries
- 1 audit page has no primary URL recorded (nnsa-statement.md)
- 1 audit page exists in the folder but is orphaned — not cited anywhere in the case file (albuquerque-police-missing-person.md)

---

## Detail

### Citation 1

- **Case-file line:** L74 — `**NM DPS Missing Persons record M101688** -- See \`appendices/primary-sources/garcia/nm-dps-missing-persons.md\``
- **Audit page:** `appendices/primary-sources/garcia/nm-dps-missing-persons.md`
- **Source URL:** https://missingpersons.dps.nm.gov/mpweb/mpdetailreport_serv?id=M101688
- **Verification status:** 200 — page loads; displays Garcia's official NM DPS record (name, DOB, physical description, APD contact). Content matches audit-page paraphrase.
- **Binary?** No (HTML database record page; no downloadable PDF offered)
- **Action recommended:** Patch — add primary URL inline in case file so citation reads: `NM DPS record M101688 (<url>); local notes: appendices/primary-sources/garcia/nm-dps-missing-persons.md`
- **Notes:** The NM DPS "Generate Poster" feature suggests a poster PDF may be generatable, but there is no static binary file to archive. Dynamic query URL; direct link is stable as of verification date.

---

### Citation 2

- **Case-file line:** L75 — `**NNSA general statement** (acknowledging awareness of reports) -- See \`appendices/primary-sources/garcia/nnsa-statement.md\``
- **Audit page:** `appendices/primary-sources/garcia/nnsa-statement.md`
- **Source URL:** None recorded — audit page states: "Not directly located as standalone document; quoted in multiple secondary sources including Newsweek and CBS News"
- **Verification status:** Not recorded — no primary URL exists to verify
- **Binary?** No
- **Action recommended:** Annotate — case file and audit page should both note that no standalone NNSA press-release URL has been located. The statement appears to have been delivered verbally or via email to journalists, not published. Until a URL surfaces, cite as "NNSA statement to media (via Newsweek, CBS News; no standalone document located)" with a link to the Newsweek article as the best available secondary access point.
- **Notes:** Newsweek article (https://www.newsweek.com/missing-government-security-man-compared-to-neil-mccasland-case-11828116, verified 200) quotes NNSA in context. CBS News (https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/) also carries the statement. Neither constitutes a T1 direct-access URL; T1 rating in the audit page should carry a qualifier ("T1 content accessed only via T4 secondary").

---

## URL-already-inline (consider local archive)

The following secondary-source citations in the case file already carry direct URLs. None are binaries; all appear to be standard news articles. Local archiving is low priority but noted for completeness.

| Line | URL | Outlet | Verified? |
|---|---|---|---|
| L13 | https://www.kob.com/new-mexico/4-missing-persons-with-nuclear-ties-spark-concern-in-new-mexico/ | KOB 4 | Not re-verified this session (out of scope per task) |
| L16 | https://britbrief.co.uk/crime/police/nuclear-secrets-contractor-vanishes-in-new-mexico-mystery.html | British Brief | Not re-verified this session |
| L30 | https://www.newsnationnow.com/space/ufo/steven-garcia-disappearance-neil-mccasland/ | NewsNation | Not re-verified this session |
| L81 | https://www.newsweek.com/missing-government-security-man-compared-to-neil-mccasland-case-11828116 | Newsweek | **200 — verified this session** |
| L82 | https://www.newsweek.com/fbi-investigating-missing-dead-scientists-what-we-know-11852176 | Newsweek | Not re-verified this session |
| L83 | https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/ | CBS News | Not re-verified this session |
| L84 | https://www.livenowfox.com/news/missing-us-scientists-white-house | LiveNOW from FOX | Not re-verified this session |
| L85 | https://www.kob.com/new-mexico/4-missing-persons-with-nuclear-ties-spark-concern-in-new-mexico/ | KOB 4 (duplicate) | Not re-verified this session |
| L86 | https://www.newsnationnow.com/space/ufo/steven-garcia-disappearance-neil-mccasland/ | NewsNation (duplicate) | Not re-verified this session |
| L87 | https://www.newsnationnow.com/missing/who-missing-dead-scientists-connection-government/ | NewsNation | Not re-verified this session |
| L88 | https://britbrief.co.uk/crime/police/nuclear-secrets-contractor-vanishes-in-new-mexico-mystery.html | British Brief (duplicate) | Not re-verified this session |
| L89 | https://www.dailywire.com/news/top-scientists-are-turning-up-dead-or-missing-now-the-white-house-is-stepping-in | Daily Wire | Not re-verified this session |
| L102 | https://news-pravda.com/world/2026/04/12/2233631.html | Pravda EN | Not re-verified this session |

These URLs are outside the scope of this audit (task: local-audit-page-only citations). Secondary-source URL verification is a separate pass.

---

## No-primary-URL audit pages

### nnsa-statement.md

- **File:** `appendices/primary-sources/garcia/nnsa-statement.md`
- **Declared Source URL:** "Not directly located as standalone document"
- **Status:** No primary URL has been recorded. The NNSA statement appears to be a media-statement-to-journalists, not a published press release. No standalone URL exists on nnsa.energy.gov or kcnsc.doe.gov as of original access date (April 20, 2026).
- **Action:** Annotate audit page and case file citation to explicitly flag the absence of a direct URL. Downgrade T1 rating to "T1-via-T4" pending location of original document.

---

## Orphaned audit page (not cited in case file)

### albuquerque-police-missing-person.md

- **File:** `appendices/primary-sources/garcia/albuquerque-police-missing-person.md`
- **Declared Source URL:** https://www.newsweek.com/missing-government-security-man-compared-to-neil-mccasland-case-11828116
- **Verification status:** 200 — verified this session
- **Notes:** This audit page exists in the garcia primary-sources folder but is not referenced by any citation in `cases/garcia.md`. Its Source URL is the same Newsweek article already cited inline in the case file. The page's content describes the APD missing-person report as reconstructed from Newsweek reporting — it is not itself a primary APD document. The case file's known-unknowns section (line 77) correctly notes that no APD press release was located. This orphaned page should either be linked from the case file or acknowledged as a dead-end stub. It does not add T1 evidence; it is T3 content labeled as if it were an APD primary document.
