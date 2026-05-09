# Source-URL Audit — Thomas (2026-05-08)

## Summary
- 0 citations point to local audit pages only (all inline citations use direct URLs)
- 8 URLs verified 200
- 3 URLs returned 403
- 1 URL returned 403 (pre-existing, already flagged in audit page)
- 0 URLs are downloadable binaries
- 0 audit pages have no primary URL recorded
- 3 audit pages exist in `appendices/primary-sources/thomas/`; none are referenced inline from the case file

---

## Detail

### Local-audit-page-only citations
None. Every inline citation in `cases/thomas.md` uses a direct URL. No citation points exclusively to a local `../appendices/primary-sources/thomas/*.md` audit page.

---

## URL-already-inline (verified status)

All URLs appearing inline in `cases/thomas.md` were fetched. Results:

### T1 — Official / Primary

| URL | Line(s) | Status | Notes |
|-----|---------|--------|-------|
| `https://www.wakefieldma.gov/m/newsflash/Home/Detail/113` | 15, 21, 40, 66 | **200** | DA Ryan + Chief Skory statement on body recovery. Content matches case file. |
| `https://www.middlesexda.com/press-releases/news/body-recovered-lake%C2%A0quannapowitt-wakefield` | 16, 20, 21, 40, 67 | **403** | Middlesex DA press release — automation blocked. Flagged below. |
| `https://www.legacy.com/us/obituaries/name/jason-thomas-obituary?id=61184839` | 12, 13, 22, 26, 28, 68 | **200** | Obituary live; confirms DOB, age 46 at death, Novartis, wife, parents. |
| `https://scholar.google.com/citations?user=T2VhMtYAAAAJ&hl=en` | 26, 69 | **200** | Google Scholar profile live; 4,645 citations, h-index 25. |
| `https://www.researchgate.net/profile/Jason-Thomas-6` | 26, 70 | **403** | ResearchGate blocks automation. Flagged below. |

### T3/T4 — News / Secondary

| URL | Line(s) | Status | Notes |
|-----|---------|--------|-------|
| `https://www.boston25news.com/news/local/he-literally-vanished-wakefield-woman-asks-public-help-search-husband/FPPCD6SIIFFM3LW4I4WHNG2D6I/` | 14, 28, 30, 32, 34, 38, 75 | **200** | Live; wife's account, parents' deaths, phone/wallet detail confirmed. |
| `https://www.nbcnews.com/dateline/missing-in-america/jason-thomas-missing-wakefield-massachusetts-rcna263785` | 17, 32, 36, 73 | **403** | NBC News blocks automation. Flagged below. |
| `https://www.nbcboston.com/news/local/massachusetts-man-wakefield-jason-thomas-vanished/3916919/` | 74 | **200** | Live; NBC Boston local coverage confirmed. |
| `https://www.boston.com/news/local-news/2026/01/05/wakefield-man-vanished-has-been-missing-for-3-weeks-wife-says/` | 18, 76 | **200** | Live; January 5 disappearance coverage confirmed. |
| `https://www.boston.com/news/local-news/2026/03/17/body-pulled-from-wakefield-lake-believed-to-be-that-of-missing-man/` | 77 | **200** | Live; body recovery reporting confirmed. |
| `https://www.newsweek.com/obituaries-shed-light-on-wave-of-dead-missing-scientists-as-white-house-probes-11841019` | 78 | **200** | Live; contextual pattern-narrative article confirmed. |
| `https://www.gofundme.com/f/samu3c-help-us-bring-jason-home` | 79 | **200** | Live; fundraiser by Brianna Florovito and Katherine Biggar for Kristen Bartoli confirmed. |

---

## 403-flagged URLs — Requires user action

### 1. Middlesex DA press release
- **URL:** `https://www.middlesexda.com/press-releases/news/body-recovered-lake%C2%A0quannapowitt-wakefield`
- **Case-file lines:** 16, 20, 21, 40, 67
- **Audit page:** `appendices/primary-sources/thomas/wakefield-da-body-recovery-statement.md` — content already reconstructed there from the Wakefield town website (which is 200).
- **Status:** 403 (automation blocked)
- **Action recommended:** Download via browser and archive to `appendices/primary-sources/thomas/middlesex-da-press-release.pdf` (or `.html`). The Wakefield town website mirror (`wakefieldma.gov`) is live at 200 and carries the identical text — acceptable fallback primary source already cited inline.

### 2. ResearchGate profile
- **URL:** `https://www.researchgate.net/profile/Jason-Thomas-6`
- **Case-file lines:** 26, 70
- **Audit page:** `appendices/primary-sources/thomas/sources.md` (entry 4)
- **Status:** 403 (automation blocked — standard ResearchGate behavior)
- **Action recommended:** Browser-verify and screenshot/archive if desired. The Google Scholar profile (200, same claim) is a sufficient parallel T1 citation. No urgent gap.

### 3. NBC Dateline "Missing in America"
- **URL:** `https://www.nbcnews.com/dateline/missing-in-america/jason-thomas-missing-wakefield-massachusetts-rcna263785`
- **Case-file lines:** 17, 32, 36, 73
- **Audit page:** `appendices/primary-sources/thomas/wakefield-pd-missing-person-bulletin.md` lists this as secondary URL (the bulletin audit page's primary hoodline.com URL is also 403 — pre-existing, already noted in that audit page).
- **Status:** 403 (NBC News blocks automation — common)
- **Action recommended:** Browser-verify. No local archive exists. This is the primary source for Chief Skory's search details and wife's NBC account; consider saving page to `appendices/primary-sources/thomas/nbc-dateline-missing-in-america.html` or PDF.

---

## No-primary-URL audit pages
None. All three audit pages in `appendices/primary-sources/thomas/` have a `Source URL` recorded.

---

## Audit page coverage note

Three audit pages exist:
- `sources.md` — index of all T1/T3/T4 sources (not cited inline; reference document only)
- `wakefield-da-body-recovery-statement.md` — reconstructed DA statement; Source URL `wakefieldma.gov` (200)
- `wakefield-pd-missing-person-bulletin.md` — reconstructed PD bulletin; Source URL `hoodline.com` (403, pre-existing); secondary NBC Dateline URL also 403

None are linked from the case file inline — the case file cites source URLs directly per convention. The audit pages serve as reconstruction notes only.

---

## Alt-URL note (sources.md)

`sources.md` lists `https://sullivanfuneralhome.net/tribute/details/4495` as an alt URL for the obituary. Verified: **200**, content matches Legacy.com obituary (age 46, Kristen Bartoli, Novartis). This is a usable backup if Legacy.com goes dark. Not currently cited inline in the case file; no action required unless Legacy.com degrades.
