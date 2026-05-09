# Source-URL Audit — Hicks (2026-05-08)

## Summary

- **0** citations point to local audit pages only (all inline citations use direct URLs)
- **7** URLs verified 200
- **3** URLs returned 403 (dps.aas.org, oversight.house.gov, thehill.com)
- **0** URLs are downloadable binaries
- **0** audit pages have no primary URL recorded
- **1** coroner finding documented in a local audit page (`la-county-coroner-cause-of-death.md`) but never cited inline — gap flagged below

---

## Detail

### No local-audit-page-only citations found

`cases/hicks.md` contains **no citations** that link only to a local
`appendices/primary-sources/hicks/*.md` audit page. Every inline citation
uses a direct external URL. The two files in `appendices/primary-sources/hicks/`
are never linked from the case file at all.

---

## URL-already-inline — verification results

All 10 distinct URLs cited inline or in the Primary/Secondary Sources tables
were fetched. Results:

| # | Line(s) | URL | Status | Notes |
|---|---------|-----|--------|-------|
| 1 | L41, L53, L79 | https://obituaries.forestlawn.com/obituaries/michael-hicks | **200** | Content confirmed: Hicks obituary, death July 30 2023. No cause of death listed. |
| 2 | L41, L55, L82 | https://dps.aas.org/news/michael-david-hicks-1964-2023/ | **403** | Previously 403 on 2026-04-20; still 403. Consider local archive download. |
| 3 | L41, L54, L80 | https://lpl.arizona.edu/about/memoriam/michael-hicks | **200** | Content confirmed: LPL memorial page for Hicks. |
| 4 | L47, L56, L83 | https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/ | **403** | Previously 403 on 2026-04-20; still 403. Consider local archive download. |
| 5 | L47 | https://www.newsweek.com/fbi-investigating-missing-dead-scientists-what-we-know-11852176 | **200** | Content confirmed: Newsweek FBI-investigation article. |
| 6 | L61, L91 | https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza | **200** | Content confirmed: Fox 11 LA article on 11 scientists. Also the `Source URL` for `la-county-coroner-cause-of-death.md`. |
| 7 | L62, L92 | https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/ | **200** | Content confirmed: CBS News article on scientist deaths/disappearances. |
| 8 | L63, L93 | https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/ | **403** | New finding — no prior 403 noted in source-index.md. Consider local archive. |
| 9 | L60, L89 | https://www.newsweek.com/list-dead-or-missing-scientists-suspicious-michael-david-hicks-11805585 | **200** | Content confirmed: Newsweek list article naming Hicks. |
| 10 | L81, L90 | https://www.newsweek.com/obituaries-shed-light-on-wave-of-dead-missing-scientists-as-white-house-probes-11841019 | **200** | Content confirmed: Newsweek obituaries article. |
| 11 | L81 (table only) | https://lpl.arizona.edu/news/2023/fall/michael-david-hicks-1964-2023 | **200** | Content confirmed: LPL news article on Hicks (1964-2023). In Primary Sources table; not linked from inline prose. |

### 403 citations — action recommended

**Citation at L41/L55/L82 — AAS DPS obituary**
- **Case-file line L41:** `The [AAS Division for Planetary Sciences](https://dps.aas.org/news/michael-david-hicks-1964-2023/) and the [University of Arizona's Lunar and Planetary Laboratory]...`
- **Case-file line L55:** `- **[AAS Division for Planetary Sciences obituary](https://dps.aas.org/news/michael-david-hicks-1964-2023/)** (T1 -- professional society): Published formal obituary notice consistent with above details.`
- **Audit page:** `appendices/primary-sources/hicks/source-index.md` (Source 4)
- **Source URL:** https://dps.aas.org/news/michael-david-hicks-1964-2023/
- **Verification status:** 403 (confirmed on 2026-04-20 and again 2026-05-08)
- **Binary?** No
- **Action recommended:** Attempt Wayback Machine retrieval; download HTML snapshot to `appendices/primary-sources/hicks/`; annotate `source-index.md` with `Local archive` frontmatter.
- **Notes:** Source index notes "search snippet confirmed existence and content consistent with other memorials." URL is valid; block is bot-filtering.

**Citation at L47/L56/L83 — House Oversight Committee press release**
- **Case-file line L47:** `His case was included in [House Oversight Committee](https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/) Chairman James Comer and Rep. Eric Burlison's letters...`
- **Case-file line L56:** `- **[House Oversight Committee press release](https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/)** (T1 -- government): Confirms Congressional inquiry...`
- **Audit page:** `appendices/primary-sources/hicks/source-index.md` (Source 5)
- **Source URL:** https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/
- **Verification status:** 403 (confirmed on 2026-04-20 and again 2026-05-08)
- **Binary?** No
- **Action recommended:** Attempt Wayback Machine retrieval; download HTML snapshot; annotate `source-index.md` with `Local archive` frontmatter.
- **Notes:** oversight.house.gov blocks automated fetchers; content confirmed via search snippets and secondary reporting.

**Citation at L63/L93 — The Hill**
- **Case-file line L63:** `- **[The Hill](https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/)** (T4): Reported Hicks' death as part of pattern but noted no established link between cases.`
- **Audit page:** Not in `source-index.md` (secondary source only; no audit page created)
- **Source URL:** https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/
- **Verification status:** 403 (new — not flagged in prior session notes)
- **Binary?** No
- **Action recommended:** Attempt Wayback Machine retrieval; create audit page for this source if archived; annotate with `Local archive` frontmatter.
- **Notes:** T4 secondary; lower priority than T1 403s above, but new 403 status should be recorded.

---

## No-primary-URL audit pages

None. Both audit pages have `Source URL` frontmatter recorded:

| File | Source URL |
|------|-----------|
| `source-index.md` | Multiple (5 sources inline) |
| `la-county-coroner-cause-of-death.md` | https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza |

---

## Gap: coroner finding not cited inline

`appendices/primary-sources/hicks/la-county-coroner-cause-of-death.md` documents
the LA County Coroner's determination (cause: arteriosclerotic cardiovascular disease;
manner: natural) sourced from the Fox 11 LA article (200, confirmed). This is the
only known public disclosure of the cause of death — a materially significant fact —
yet the case file's narrative (L129, Open Question #1) states "no source...has
disclosed the cause of death" and Open Question #2 asks whether an autopsy was
conducted.

The coroner finding is not cited anywhere in the case-file inline prose or the
Documented section. The audit page exists but is not linked. The Fox 11 LA URL
(L61, L91) is cited inline for a different claim (White House/FBI investigation),
not for the coroner finding.

**Action recommended:** Update the case file to cite the Fox 11 LA article for
the coroner finding; revise the "What Is Documented" section and Open Questions
accordingly. This is a content gap, not a link-format gap.
