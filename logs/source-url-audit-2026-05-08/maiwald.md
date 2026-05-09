# Source-URL Audit — Maiwald (2026-05-08)

## Summary

- **0** citations point to local audit pages only (all inline citations use direct URLs)
- **9** URLs verified 200
- **3** URLs returned 403
- **0** URLs are downloadable binaries (JPL dataverse page links to a PDF but the page itself is HTML; see Detail)
- **0** audit pages have no primary URL recorded
- **1** audit page (`frank-maiwald-obituary.md`) notes "Officials confirmed that no autopsy was performed" — wording stronger than the case file's own hedge; flagged for inconsistency

---

## Detail

### No citations point exclusively to local audit pages

Every inline citation in `cases/maiwald.md` uses a direct external URL. There are no citations whose only link is `../appendices/primary-sources/maiwald/*.md`. This section is therefore empty.

---

## URL-already-inline (consider local archive)

These URLs appear directly in the case file body or source tables. Verification results follow.

### Primary Sources (source table, lines 87–92)

#### PS-1 — Legacy.com obituary
- **Case-file line:** L87 / L57 (narrative) / L45 (narrative) — `https://www.legacy.com/us/obituaries/legacyremembers/frank-maiwald-obituary?id=55630404`
- **Audit page:** `appendices/primary-sources/maiwald/frank-maiwald-obituary.md` (exists; `Source URL` matches)
- **Verification status:** 200 OK — page loads; obituary record for Frank Werner Maiwald confirmed present
- **Binary?** No
- **Action recommended:** Consider local archive — the obituary page is a commercial site and could be edited or removed. A PDF/screenshot archive in `appendices/primary-sources/maiwald/` is advisable.
- **Notes:** The dedicated audit page (`frank-maiwald-obituary.md`) exists and holds a content extract. However, the audit page states "Officials confirmed that an autopsy was never performed" whereas the case file correctly hedges "reportedly no autopsy performed… not been confirmed on-record." The audit-page wording is stronger than the evidence warrants; flag for correction when edits re-open.

#### PS-2 — Google Scholar profile
- **Case-file line:** L43 / L88 — `https://scholar.google.com/citations?user=PPfNthEAAAAJ&hl=en`
- **Audit page:** `appendices/primary-sources/maiwald/source-index.md` (Source 2)
- **Verification status:** 200 OK — profile loads; confirms Frank Maiwald, JPL/CalTech, 3,447 citations, h-index 27, research areas match
- **Binary?** No
- **Action recommended:** No urgent archive needed (Google Scholar profiles are stable for deceased researchers), but consider screenshot. Source-index notes "Fetched but rendered as code" from prior session; current fetch resolved cleanly.

#### PS-3 — ResearchGate profile
- **Case-file line:** L43 / L89 — `https://www.researchgate.net/profile/Frank-Maiwald`
- **Audit page:** `appendices/primary-sources/maiwald/source-index.md` (Source 3)
- **Verification status:** **403 Forbidden** — ResearchGate blocks automated fetches; prior session also noted "confirmed via search, not directly fetched"
- **Binary?** No
- **Action recommended:** Annotate 403 in source-index. Consider manual archive (browser PDF) since ResearchGate profiles for deceased researchers may become inaccessible. The substantive data (citation count, research areas) is cross-confirmed by Google Scholar (PS-2), so evidentiary impact is low.

#### PS-4 — SPIE proceedings — SBG-VSWIR paper
- **Case-file line:** L58 / L90 — `https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12798/1279810/Optical-design-study-of-surface-biology-and-geology-SBG-visible/10.1117/12.2692105.short`
- **Audit page:** `appendices/primary-sources/maiwald/source-index.md` (Source 4)
- **Verification status:** 200 OK — page loads; abstract confirmed; authors including Maiwald listed; publication date May 2024 confirmed; institution JPL confirmed
- **Binary?** No (abstract/landing page only; full PDF requires SPIE subscription)
- **Action recommended:** Consider archiving the abstract page. Full PDF is paywalled; DOI-based access is stable.
- **Notes:** Source-index previously noted "not directly fetched; confirmed via search" — this session confirms direct fetch resolves 200.

#### PS-5 — JPL Open Repository — HIFI publication
- **Case-file line:** L60 / L91 — `https://dataverse.jpl.nasa.gov/dataset.xhtml?persistentId=hdl:2014/9805`
- **Audit page:** `appendices/primary-sources/maiwald/source-index.md` (Source 5)
- **Verification status:** 200 OK — page loads; dataset confirmed as THz frequency receiver instrumentation for Herschel HIFI; authors listed as Pearson, J.C. + 13 collaborators; a 3.0 MB PDF is available under CC0
- **Binary?** The dataset page links to a downloadable PDF (3.0 MB, CC0 license) — this qualifies for local archive per project convention
- **Action recommended:** Download the PDF to `appendices/primary-sources/maiwald/` and add `Local archive` frontmatter to source-index Source 5 entry. CC0 license permits archival without restriction.
- **Notes:** Source-index previously noted "not directly fetched." This session confirms the page resolves 200 and a freely-licensed binary is available. Maiwald is not listed as one of the 13+ authors in the fetch result — the case file attributes HIFI publications to Maiwald generally via the JPL repository; this specific dataset entry should be cross-checked to confirm Maiwald appears as author or co-author before citing as primary evidence of his HIFI contribution.

#### PS-6 — House Oversight Committee press release
- **Case-file line:** L51 / L61 / L92 — `https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/`
- **Audit page:** `appendices/primary-sources/maiwald/source-index.md` (Source 6)
- **Verification status:** **403 Forbidden** — consistent with prior session finding; government press-release pages commonly block automated fetches
- **Binary?** No
- **Action recommended:** Flag 403 (expected; not a content removal). Consider Wayback Machine snapshot for archival per project gov-site tracking layer. Source-index already notes the 403 from the prior session.

---

### Secondary Sources (source table, lines 98–103)

#### SS-1 — Newsweek
- **Case-file line:** L65 / L98 — `https://www.newsweek.com/obituaries-shed-light-on-wave-of-dead-missing-scientists-as-white-house-probes-11841019`
- **Verification status:** 200 OK — article confirmed; Maiwald included; matches case-file description
- **Action recommended:** No immediate action. Consider archiving given paywalled national news.

#### SS-2 — Fox 11 Los Angeles
- **Case-file line:** L66 / L99 — `https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza`
- **Verification status:** 200 OK — article confirmed; Maiwald listed as one of four LA County cases
- **Action recommended:** No immediate action.

#### SS-3 — CBS News
- **Case-file line:** L67 / L100 — `https://www.cbsnews.com/news/deaths-disappearances-scientists-staff-government-labs/`
- **Verification status:** 200 OK — article confirmed; key skeptical finding ("no links between any of the deaths") confirmed
- **Action recommended:** No immediate action.

#### SS-4 — The Hill
- **Case-file line:** L68 / L101 — `https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/`
- **Verification status:** **403 Forbidden** — automated fetch blocked
- **Action recommended:** Flag 403; confirm via manual browser access. Article may be behind soft paywall or anti-bot protection.

#### SS-5 — NewsNation
- **Case-file line:** L68 / L102 — `https://www.newsnationnow.com/missing/who-missing-dead-scientists-connection-government/`
- **Verification status:** **403 Forbidden** — automated fetch blocked
- **Action recommended:** Flag 403; confirm via manual browser access.

#### SS-6 — IBTimes UK
- **Case-file line:** L103 — `https://www.ibtimes.co.uk/unexplained-deaths-us-scientists-national-security-concerns-1792480`
- **Verification status:** 200 OK — article confirmed; Maiwald named; FBI/Congressional angle confirmed
- **Action recommended:** No immediate action.

---

## No-primary-URL audit pages

None. Both audit pages (`frank-maiwald-obituary.md` and `source-index.md`) contain `Source URL` entries for all sources.

---

## Action Summary

| Priority | Item |
|----------|------|
| High | PS-5 (JPL dataverse): verify Maiwald is named author on the linked dataset; download CC0 PDF to local archive |
| Medium | PS-1 (Legacy.com obituary): archive locally (commercial site, deletion risk) |
| Medium | Audit page `frank-maiwald-obituary.md` line 15: wording "Officials confirmed that an autopsy was never performed" overstates the evidence — case file correctly hedges this; correct on next edit pass |
| Low | PS-3 (ResearchGate): annotate 403 in source-index; manual browser archive recommended |
| Low | PS-6 (House Oversight): add Wayback snapshot per gov-site tracking layer |
| Low | SS-4 (The Hill), SS-5 (NewsNation): confirm 403 is bot-block not dead link; manual verification |
| Info | PS-4 (SPIE): source-index entry says "not directly fetched" — update to reflect 200 confirmed this session |
