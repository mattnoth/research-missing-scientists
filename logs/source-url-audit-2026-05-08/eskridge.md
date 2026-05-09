# Source-URL Audit — Eskridge (2026-05-08)

## Summary

- **0** citations point to local audit pages only (zero local-only links found)
- **11** unique external URLs audited
- **9** URLs verified 200
- **1** URL returned 403 (NewsNation — needs user browser confirmation)
- **1** URL returned 405 (Primetimer — method-not-allowed; needs user browser confirmation)
- **1** URL is a downloadable binary (HAL5 PDF — 200, 2.4 MB)
- **0** audit pages have no primary URL recorded (both audit pages have Source URL)
- **Action item:** Both audit pages (`amy-eskridge-obituary.md`, `sources.md`) are standalone reference files, not linked from the case file inline citations. The case file already uses direct URLs everywhere — convention is already correct for this case.

---

## Local-only citation scan

No citations in `cases/eskridge.md` link to `../appendices/primary-sources/eskridge/*.md`. The local audit pages exist as background reference but are not cited inline. No patching required.

---

## URL-already-inline (consider local archive)

All inline citations use direct external URLs. Three URLs warrant local archive consideration based on content type or volatility:

### A. HAL5 Presentation PDF
- **Case-file line:** L17 — `[HAL5 PDF](https://www.hal5.org/PDF/HAL5-Dec2018-Talk-AntiGravity.pdf)`
- **Also:** L79 (Primary Sources section)
- **Verification status:** 200 — confirmed PDF, 2.4 MB, Google Slides export, 23+ pages
- **Binary?** Yes (PDF)
- **Action recommended:** Download to `appendices/primary-sources/eskridge/` and add `Local archive` frontmatter to audit page. HAL5 is a small non-profit site; link stability is uncertain.
- **Notes:** WebFetch retrieved the binary directly. `sources.md` lists this URL but no local copy exists.

### B. Arab Tribune Obituary
- **Case-file line:** L12, L13, L14, L19, L26 (×3), L28, L41, L43, L77
- **URL:** `https://www.thearabtribune.com/obituaries/amy-eskridge/article_3779ff44-ecd0-11ec-b084-a70e496e902a.html`
- **Verification status:** 200 — fully accessible, no paywall
- **Binary?** No
- **Action recommended:** Consider local archive (HTML save). This is the single most-cited T1 source; small regional paper with uncertain long-term archival stability.
- **Notes:** `amy-eskridge-obituary.md` exists as a content reconstruction but does not hold a downloaded binary. A proper archive would be an HTML or PDF save.

### C. Legacy.com Obituary Mirror
- **Case-file line:** L78
- **URL:** `https://www.legacy.com/us/obituaries/legacyremembers/amy-eskridge-obituary?id=35311909`
- **Verification status:** 200 — fully accessible, no paywall
- **Binary?** No
- **Action recommended:** Low priority — Legacy.com has stable long-term archival; Wayback Machine covers it. Monitor only.

---

## Full URL verification table

| # | URL | Case-file line(s) | Status | Binary | Notes |
|---|-----|-------------------|--------|--------|-------|
| 1 | https://www.thearabtribune.com/obituaries/amy-eskridge/article_3779ff44-ecd0-11ec-b084-a70e496e902a.html | L12–L43, L77 | 200 | No | Fully accessible |
| 2 | https://www.hal5.org/PDF/HAL5-Dec2018-Talk-AntiGravity.pdf | L17, L79 | 200 | **Yes (PDF)** | 2.4 MB; consider local archive |
| 3 | https://www.legacy.com/us/obituaries/legacyremembers/amy-eskridge-obituary?id=35311909 | L78 | 200 | No | Fully accessible |
| 4 | https://www.newsweek.com/who-is-amy-eskridge-scientist-death-queried-us-expert-mysteries-11843659 | L22, L28, L30, L41, L45, L82 | 200 | No | Fully accessible |
| 5 | https://www.foxnews.com/politics/11th-scientist-death-emerges-string-missing-dead-officials-access-us-secrets | L22, L28, L30, L34, L41, L83 | 200 | No | Fully accessible |
| 6 | https://www.newsnationnow.com/space/ufo/father-dead-scientist-denies-suspicious/ | L47, L59, L60, L85 | **403** | No | Blocked to automated fetch; needs user browser confirmation |
| 7 | https://www.ibtimes.co.uk/grieving-father-dismisses-conspiracy-theories-1792374 | L84, L95 | 200 | No | Fully accessible |
| 8 | https://www.primetimer.com/features/i-can-learn-a-new-field-in-three-months-ufo-scientist-amy-eskridges-interview-resurfaces-after-she-passed-away-in-2022 | L86 | **405** | No | Method Not Allowed — likely bot-blocked; needs user browser confirmation |
| 9 | https://www.uniladtech.com/science/space/scientist-disclosure-ufos-reveals-threats-made-before-death-904628-20260417 | L87 | 200 | No | Fully accessible |
| 10 | https://www.ibtimes.co.uk/mysterious-death-anti-gravity-scientist-ufo-conspiracy-1792209 | L96 | 200 | No | Fully accessible |
| 11 | https://www.themirror.com/news/science/ufo-linked-scientist-warned-my-1794646 | L97 | 200 | No | Fully accessible |
| 12 | https://britanniadaily.com/anti-gravity-researchers-death-sparks-questions/ | L98 | 200 | No | Fully accessible |
| 13 | https://en.wikipedia.org/wiki/Michael_Shellenberger | L49 | 200 | No | Wikipedia; enrichment link for Shellenberger |

---

## No-primary-URL audit pages

Both audit pages in `appendices/primary-sources/eskridge/` have primary URLs recorded:

- `amy-eskridge-obituary.md` — Source URL: `https://www.thearabtribune.com/obituaries/amy-eskridge/article_3779ff44-ecd0-11ec-b084-a70e496e902a.html` (frontmatter field name: `Source URL`)
- `sources.md` — Contains a URL inventory (not a single-source audit page; URLs embedded in body). No `Source URL` frontmatter, which is appropriate given this is a multi-source index, not a single-source reconstruction.

Neither is flagged as no-primary-URL.

---

## Items requiring user action

1. **NewsNation (403):** `https://www.newsnationnow.com/space/ufo/father-dead-scientist-denies-suspicious/` — cited at L47, L59, L60, L85. Please open in browser to confirm accessible. If confirmed, no patch needed; if dead/paywalled, flag for Wayback substitution.
2. **Primetimer (405):** `https://www.primetimer.com/features/i-can-learn-a-new-field-in-three-months-ufo-scientist-amy-eskridges-interview-resurfaces-after-she-passed-away-in-2022` — cited at L86. Please open in browser to confirm accessible. 405 from automation does not necessarily mean the page is dead; many sites block HEAD/automated GET but serve normally in a browser.
3. **HAL5 PDF — local archive recommended:** Binary confirmed live at 200; small non-profit site. Download to `appendices/primary-sources/eskridge/hal5-dec2018-antigravity.pdf` and update `sources.md` with `Local archive` note.
4. **Arab Tribune — consider local archive:** Most-cited T1 source; small regional paper. HTML or PDF save to `appendices/primary-sources/eskridge/` would harden the dossier against link rot.
