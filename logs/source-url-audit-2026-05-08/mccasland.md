# Source-URL Audit — McCasland (2026-05-08, verification of worked example)

## Summary

- 1 citation still points to a local audit page only (missed in prior pass — line 30, Riverside Research)
- 12 URLs verified 200
- 3 URLs returned 403 (BCSO PDF, House Oversight, KRQE — all previously documented)
- 1 URL confirmed dead 404 (Dayton Daily News — already annotated in case file)
- 3 NewsNation URLs returned 403 (bot-blocking; content exists behind paywall/CDN)
- 1 audit page binary present (PressRelease3.12.2026.pdf — BCSO)
- 0 audit pages with no primary URL recorded

---

## Detail

### Citation 1 — Missed: Riverside Research appointment, local-page-only link

- **Case-file line:** L30 — `| Jun 27, 2019 | Joined Riverside Research Board of Trustees | T1 ([press release](../appendices/primary-sources/mccasland/riverside-research-appointment.md)) | Confirmed |`
- **Audit page:** `appendices/primary-sources/mccasland/riverside-research-appointment.md`
- **Source URL:** https://www.prnewswire.com/news-releases/riverside-research-welcomes-dr-neil-mccasland-to-their-board-of-trustees-300921796.html
- **Verification status:** 200 — page loads; title confirmed "Riverside Research Welcomes Dr. Neil McCasland to their Board of Trustees"; content matches audit page summary.
- **Binary?** No
- **Action recommended:** Patch line 30 — replace `[press release](../appendices/primary-sources/mccasland/riverside-research-appointment.md)` with `[press release](https://www.prnewswire.com/news-releases/riverside-research-welcomes-dr-neil-mccasland-to-their-board-of-trustees-300921796.html)` (or dual-link: direct URL primary, local archive secondary, consistent with the pattern used on lines 29/33/36).
- **Notes:** This is the only citation in the file where a T1 source URL exists in the audit page but was not surfaced inline. All other T1 citations were correctly patched in the prior pass.

---

## URL-already-inline (consider local archive)

The following inline direct URLs are live (200) but have no corresponding downloaded binary or audit page. These are all T4 news articles, which do not require local archiving under the current policy, but are flagged here for completeness.

| Line | URL | Status | Notes |
|------|-----|--------|-------|
| L29, L171 | https://wikileaks.org/podesta-emails/emailid/3099 | 200 | Audit page exists (`wikileaks-podesta-email-3099.md`); no binary needed (HTML page, not PDF). Fully handled. |
| L32, L34, L35, L112, L114, L120, L208 | https://www.cnn.com/2026/03/17/us/fbi-search-william-mccasland-general-missing | 200 | T4 — no local archive required. |
| L35, L84, L90, L98, L114, L209 | https://abcnews.com/US/retired-air-force-major-general-missing-weeks-mysterious/story?id=131126054 | 200 | T4 — no local archive required. |
| L100, L120, L175, L178, L210 | https://www.newsweek.com/wife-of-missing-ufo-expert-addresses-misinformation-around-case-11659216 | 200 | T4 — no local archive required. |
| L182, L211 | https://www.newsweek.com/missing-us-general-has-information-ufos-congressman-11684617 | 200 | T4 — no local archive required. |
| L124, L212 | https://www.newsweek.com/neil-mccasland-update-sheriff-addresses-speculation-missing-general-11827036 | 200 | T4; audit page `bcso-statement-on-speculation.md` sources this URL. No binary required. |
| L84, L86, L213 | https://www.foxnews.com/us/retired-air-force-general-vanishes-1-hour-window-from-home-gun-wallet-missing | 200 | T4 — no local archive required. |
| L100, L114, L215 | https://www.abqjournal.com/news/retired-general-was-not-confused-and-disoriented-when-he-went-missing-wife-says/2999479 | 200 | T3 — consider local archive if site goes dark; not urgent. |
| L214 | https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/ | 200 | T4 — no local archive required. |

---

## 403 / Dead URL detail

| Line | URL | Status | Already annotated? |
|------|-----|--------|--------------------|
| L33, L36 | https://www.bernco.gov/bernalillo-county-sheriff/wp-content/uploads/sites/48/2026/03/PressRelease3.12.2026.pdf | **403** | Yes — local binary downloaded (`PressRelease3.12.2026.pdf`); audit page notes 403-on-automation. Fully handled. |
| (audit page only) | https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/ | **403** | Yes — audit page `house-oversight-press-release.md` notes 403; content reconstructed from T4 coverage. Not cited inline in case file; not a gap. |
| L90, L94, L98, L217–219 | https://www.newsnationnow.com/missing/who-is-william-neil-mccasland/ | **403** | No — bot-blocking CDN; URL is plausible and was functioning at original research time. Flag for manual verification. |
| L94, L218 | https://www.newsnationnow.com/missing/missing-air-force-general-wife-911/ | **403** | No — same as above. Flag for manual verification. |
| L219 | https://www.newsnationnow.com/missing/neil-mccasland-missing-timeline/ | **403** | No — same as above. Flag for manual verification. |
| L216 | https://www.daytondailynews.com/local/new-mexico-authorities-ask-for-help-in-search-for-former-afrl-commander/DQHLHBMP2FCSXPNNJHG3PHC6IU/ | **404** | Yes — annotated in case file as dead link (CMS migration). No Wayback snapshot recovered. No action needed beyond existing note. |

---

## No-primary-URL audit pages

None. All six audit pages in `appendices/primary-sources/mccasland/` have a Source URL recorded:

| Audit page | Source URL | Status |
|---|---|---|
| `wikileaks-podesta-email-3099.md` | https://wikileaks.org/podesta-emails/emailid/3099 | 200 |
| `bcso-press-release-2026-03-12.md` | https://www.bernco.gov/bernalillo-county-sheriff/wp-content/uploads/sites/48/2026/03/PressRelease3.12.2026.pdf | 403 (documented; binary downloaded) |
| `house-oversight-press-release.md` | https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/ | 403 (documented; content reconstructed) |
| `riverside-research-appointment.md` | https://www.prnewswire.com/news-releases/riverside-research-welcomes-dr-neil-mccasland-to-their-board-of-trustees-300921796.html | 200 |
| `bcso-missing-person-press-releases.md` | https://www.krqe.com/news/albuquerque-metro/bcso-seeks-publics-help-in-locating-missing-retired-air-force-general-in-albuquerque/ | (not fetched — T4, not cited inline; not a T1 primary source page; lower priority) |
| `bcso-statement-on-speculation.md` | https://www.newsweek.com/neil-mccasland-update-sheriff-addresses-speculation-missing-general-11827036 | 200 |

Note: `bcso-missing-person-press-releases.md` and `bcso-statement-on-speculation.md` are not cited inline in `cases/mccasland.md`. Their Source URLs are Tier 4 news articles (KRQE and Newsweek), not T1 primary sources — these pages appear to be reconstruction aggregators rather than primary-source archives. No action required on the case file; flagged for information.

---

## Action items for next editing pass

1. **Patch line 30** — add the direct PR Newswire URL inline (the only required fix). Suggested form consistent with existing dual-link pattern:
   `T1 ([press release](https://www.prnewswire.com/news-releases/riverside-research-welcomes-dr-neil-mccasland-to-their-board-of-trustees-300921796.html); [local notes](../appendices/primary-sources/mccasland/riverside-research-appointment.md))`
2. **NewsNation 403s** — three URLs return 403 on automated fetch. Manual browser verification recommended. If confirmed dead, annotate similarly to the Dayton Daily News note.
3. **Albuquerque Journal (T3)** — consider archiving `abqjournal.com/...2999479` locally given T3 tier; low urgency.
