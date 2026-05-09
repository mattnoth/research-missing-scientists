# Source-URL Audit — Loureiro (2026-05-08)

## Summary

- **0** inline citations in the case file point to local audit pages only (no patch action needed)
- **7** audit pages exist in `appendices/primary-sources/loureiro/`
- **5** audit-page Source URLs verified 200
- **1** audit-page Source URL returned 429 (rate-limited; not a dead link)
- **1** audit page has no primary URL recorded (DOJ page accessed via media only)
- **1** duplicate audit page (two `.md` files reference the same Source URL)
- **2** inline case-file URLs returned 403 (NBC News — paywalled)
- **11** inline case-file URLs total checked across narrative and source sections

---

## Part 1: Audit Pages — Source URL Verification

No inline citation in `cases/loureiro.md` points *only* to a local audit page. All inline citations already use direct external URLs. Part 1 has no patch actions.

---

## Part 2: Audit Page Inventory

### Audit Page 1 — brookline-pd-investigation-details.md

- **Audit page:** `appendices/primary-sources/loureiro/brookline-pd-investigation-details.md`
- **Source URL:** `https://brookline.news/police-reports-reveal-shooters-movements-on-day-of-mit-professors-murder/`
- **Secondary URL:** `https://www.cbsnews.com/boston/news/mit-professor-nuno-loureiro-murder-new-reports/`
- **Verification status:** 429 (rate-limited on three consecutive attempts; not a 404/403 dead-link error)
- **Binary?** No
- **Action recommended:** Flag for manual spot-check. The secondary CBS Boston URL verified 200 and covers the same content. Consider archiving the brookline.news article locally given the outlet's smaller footprint; the secondary CBS Boston URL provides live backup coverage.
- **Notes:** 429 is a rate-limit response from the host, not an indication the page is gone. The audit page content matches CBS Boston reporting from the same release of police reports.

---

### Audit Page 2 — brown-shooting-wikipedia-summary.md

- **Audit page:** `appendices/primary-sources/loureiro/brown-shooting-wikipedia-summary.md`
- **Source URL:** `https://en.wikipedia.org/wiki/2025_Brown_University_shooting`
- **Verification status:** 200 OK — "2025 Brown University shooting - Wikipedia"
- **Binary?** No
- **Action recommended:** None. Note: Wikipedia is T5; this audit page is appropriate as a cross-reference but should not be sole support for any factual claim.
- **Notes:** Page confirmed live and on-topic.

---

### Audit Page 3 — doj-confession-transcript-summary.md

- **Audit page:** `appendices/primary-sources/loureiro/doj-confession-transcript-summary.md`
- **Source URL:** None recorded
- **Verification status:** Not recorded — accessed via media reports only
- **Binary?** No
- **Action recommended:** No-primary-URL (see section below). Attempt to locate the direct DOJ/US Attorney press release URL and add a `Source URL` field. The U.S. Attorney's Office for the District of Massachusetts press release page (`https://www.justice.gov/usao-ma/`) should have the January 6, 2026 release.
- **Notes:** The audit page explicitly notes "Direct DOJ release page not fetched." This is the only audit page without a Source URL. The DOJ press release is T1 and the most authoritative single document in the case; direct URL retrieval is a priority gap.

---

### Audit Page 4 — mit-obituary.md

- **Audit page:** `appendices/primary-sources/loureiro/mit-obituary.md`
- **Source URL:** `https://news.mit.edu/2025/nuno-loureiro-professor-director-plasma-science-and-fusion-center-dies-1216`
- **Verification status:** 200 OK — "Nuno Loureiro, professor and director of MIT's Plasma Science and Fusion Center, dies at 47 | MIT News"
- **Binary?** No
- **Action recommended:** Consider local archive (HTML or PDF). This is the primary T1 biographical source used in multiple case-file inline citations. Archiving protects against MIT link rot.
- **Notes:** Page confirmed live and on-topic.

---

### Audit Page 5 — mit-president-statement-dec16.md

- **Audit page:** `appendices/primary-sources/loureiro/mit-president-statement-dec16.md`
- **Source URL:** `https://president.mit.edu/writing-speeches/professor-nuno-loureiro-1977-2025`
- **Verification status:** 200 OK — "Professor Nuno Loureiro (1977–2025) | MIT Office of the President | MIT"
- **Binary?** No
- **Action recommended:** None urgent. This URL is not cited inline in the case file; the case file cites `news.mit.edu` URLs instead. If the president's statement is used as source support, add inline citation in case file.
- **Notes:** Page confirmed live. Note that the case file attributes the Kornbluth quote to `[T1 (MIT), Confirmed]` without linking this specific URL inline; the source is real and verifiable.

---

### Audit Page 6 — mit-statement-20251219.md

- **Audit page:** `appendices/primary-sources/loureiro/mit-statement-20251219.md`
- **Source URL:** `https://news.mit.edu/2025/statement-professor-nuno-loureiro`
- **Verification status:** 200 OK — "Statement on Professor Nuno Loureiro | MIT News"
- **Binary?** No
- **Action recommended:** None. Duplicate overlap with Audit Page 7 noted below.
- **Notes:** Page confirmed live.

---

### Audit Page 7 — mit-statement-dec19-suspect-identified.md

- **Audit page:** `appendices/primary-sources/loureiro/mit-statement-dec19-suspect-identified.md`
- **Source URL:** `https://news.mit.edu/2025/statement-professor-nuno-loureiro`
- **Verification status:** 200 OK — same URL as Audit Page 6
- **Binary?** No
- **Action recommended:** Consolidate. Audit Pages 6 and 7 point to the same Source URL (`https://news.mit.edu/2025/statement-professor-nuno-loureiro`) and cover the same document. One of the two files is redundant. Recommend merging content into `mit-statement-20251219.md` and deleting `mit-statement-dec19-suspect-identified.md`, or adding a `Superseded-by` note.
- **Notes:** Both files were accessed 2026-04-20 from the same URL. Content is consistent but duplicated.

---

## Part 3: URL-Already-Inline (Consider Local Archive)

These inline citations in `cases/loureiro.md` already use direct external URLs and verified 200. They are candidates for local archiving given research-preservation value.

| URL | Status | Priority | Rationale |
|-----|--------|----------|-----------|
| `https://news.mit.edu/2025/nuno-loureiro-professor-director-plasma-science-and-fusion-center-dies-1216` | 200 | High | Primary T1 biographical source; most-cited URL in case file; MIT pages can be reorganized |
| `https://news.mit.edu/2024/nuno-loureiro-named-director-mit-plasma-science-fusion-center-0501` | 200 | Medium | T1 appointment record; used for career timeline |
| `https://news.mit.edu/2025/statement-professor-nuno-loureiro` | 200 | Medium | T1 MIT official statement; links both shootings |
| `https://president.mit.edu/writing-speeches/professor-nuno-loureiro-1977-2025` | 200 | Medium | T1 presidential statement; captured in audit page but not archived as binary |
| `https://www.wbur.org/news/2025/12/19/brown-mit-professor-shootings-timeline-investigation-what-to-know` | 200 | Low | T3 local radio; investigation timeline; no audit page |
| `https://www.pbs.org/newshour/nation/we-got-em-the-major-break-in-the-brown-university-shooting-that-led-police-to-the-suspect` | 200 | Low | T3 national public media; Reddit-tip narrative |
| `https://abcnews.com/US/lengthy-grudge-motivated-brown-mass-shooting-mit-professor/story?id=128961044` | 200 | Low | T4; sole source for "20-year grudge" law enforcement characterization |

---

## Part 4: 403-Blocked Inline URLs

Two inline citations in `cases/loureiro.md` return 403 (paywalled/bot-blocked). Content is not retrievable via automation.

### NBC News — Brown suspect background

- **Case-file lines:** L51, L53, L55, L88, L153
- **URL:** `https://www.nbcnews.com/news/us-news/brown-suspect-was-top-student-portugal-promising-future-rcna250095`
- **Verification status:** 403
- **Action recommended:** Annotate; per repo convention, 403-on-automation is a footnote. The key claims from this article (Valente graduated first in class; Scott Watson quote; former classmate characterizations) are partially corroborated by Wikipedia (T5) and Portuguese media sources referenced elsewhere. A manual browser check should confirm live status.

### NBC News — Initial professor killed report

- **Case-file lines:** L140 (secondary sources section only)
- **URL:** `https://www.nbcnews.com/news/us-news/mit-professor-killed-shooting-home-rcna249582`
- **Verification status:** 403
- **Action recommended:** Annotate in secondary sources section. This is a secondary source and not relied upon for any unique factual claim in the narrative; lower priority than the Brown-suspect NBC URL.

---

## No-Primary-URL Audit Pages

| Audit page | Issue |
|------------|-------|
| `appendices/primary-sources/loureiro/doj-confession-transcript-summary.md` | No `Source URL` field. Direct DOJ/US Attorney press release URL was not fetched during original research. Recommended action: locate the DOJ USAO-MA press release for January 6, 2026 (search `https://www.justice.gov/usao-ma/pr/`) and add `Source URL` to audit page. |

---

## Summary Table

| Audit page | Source URL recorded? | Verification | Binary? | Action |
|------------|---------------------|--------------|---------|--------|
| `brookline-pd-investigation-details.md` | Yes | 429 (rate-limited) | No | Manual spot-check; consider archive |
| `brown-shooting-wikipedia-summary.md` | Yes | 200 | No | None |
| `doj-confession-transcript-summary.md` | No | — | No | Add DOJ press release URL |
| `mit-obituary.md` | Yes | 200 | No | Consider local archive (high priority) |
| `mit-president-statement-dec16.md` | Yes | 200 | No | Add inline citation to case file |
| `mit-statement-20251219.md` | Yes | 200 | No | Consolidate with duplicate |
| `mit-statement-dec19-suspect-identified.md` | Yes (duplicate) | 200 | No | Merge into mit-statement-20251219.md |

**Inline citations pointing only to local audit pages: 0**
**Inline citations returning 403: 2 (both NBC News)**
**Inline citations verified 200: 9**
**Audit pages with no Source URL: 1**
**Duplicate audit pages (same Source URL): 1 pair**
