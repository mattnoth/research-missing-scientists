# Source-URL Audit — Grillmair (2026-05-08)

## Summary

- **3** citations in the Primary Sources table point to local audit pages only
- **7** primary/secondary URLs verified 200 (all live)
- **0** URLs returned 403
- **0** downloadable binaries
- **0** audit pages have no primary URL recorded
- **2** audit pages exist in the folder that are not cited anywhere in the case file

---

## Detail

### Citation 1 — Caltech memorial statement

- **Case-file line:** L86 — `| Caltech memorial statement | Institutional statement | T1 | [appendices/primary-sources/grillmair/caltech-memorial.md](../appendices/primary-sources/grillmair/caltech-memorial.md) |`
- **Audit page:** `appendices/primary-sources/grillmair/caltech-memorial.md`
- **Source URL:** https://www.caltech.edu/about/news/caltech-mourns-the-passing-of-carl-grillmair-19592026
- **Verification status:** 200 — live. Title confirmed: "Caltech Mourns the Passing of Carl Grillmair (1959–2026)"
- **Binary?** No
- **Action recommended:** Patch — add primary URL directly in the case-file table cell alongside the local audit-page link (follow mccasland convention: primary URL first, audit page as secondary).
- **Notes:** Audit page frontmatter has `Source URL` correctly recorded. No local binary downloaded; consider archiving if PDF/print version is available.

---

### Citation 2 — LA County Board of Supervisors adjournment

- **Case-file line:** L87 — `| LA County Board of Supervisors adjournment | Government action | T1 | [appendices/primary-sources/grillmair/la-county-bos-adjournment.md](../appendices/primary-sources/grillmair/la-county-bos-adjournment.md) |`
- **Audit page:** `appendices/primary-sources/grillmair/la-county-bos-adjournment.md`
- **Source URL:** https://kathrynbarger.lacounty.gov/supervisor-barger-adjourns-board-of-supervisors-meeting-in-memory-of-slain-antelope-valley-astrophysicist-dr-carl-grillmair-caltech-scientist-honored-for-groundbreaking-space-research/
- **Verification status:** 200 — live. Title confirmed: "Supervisor Barger Adjourns Board of Supervisors Meeting in Memory of Slain Antelope Valley Astrophysicist Dr. Carl Grillmair"
- **Binary?** No
- **Action recommended:** Patch — add primary URL directly in the case-file table cell. Government press releases on supervisor sites are at risk of link rot; local archive recommended.
- **Notes:** Audit page frontmatter has `Source URL` correctly recorded.

---

### Citation 3 — LASD initial report (via CBS/media)

- **Case-file line:** L88 — `| LASD initial report (via CBS/media) | LE report (indirect) | T1/T3 | [appendices/primary-sources/grillmair/lasd-initial-report.md](../appendices/primary-sources/grillmair/lasd-initial-report.md) |`
- **Audit page:** `appendices/primary-sources/grillmair/lasd-initial-report.md`
- **Source URL (primary):** https://www.cbsnews.com/losangeles/news/llano-fatal-shooting-homicide-investigation-antelope-valley/
- **Source URL (secondary):** https://mynewsla.com/crime/2026/02/20/man-who-fatally-shot-caltech-scientist-had-been-released-after-gun-arrest/
- **Verification status:** Both 200 — live. CBS title: "67-year-old man fatally shot on front porch of LA County home, deputies say." MyNewsLA title: "Authorities Release Shooting Suspect Behind Caltech Scientist Slaying."
- **Binary?** No
- **Action recommended:** Patch — expose both URLs inline in the case-file table cell. Note: audit page documents that no direct lasd.org press release URL was found; this gap is already logged in the audit page. No further action needed on the gap itself unless a direct LASD URL is later located.
- **Notes:** Audit page `Source URL` field contains two URLs, both verified. The T1/T3 mixed-tier rating is appropriate given the indirect relay.

---

## URL-already-inline (consider local archive)

The following URLs appear directly in the case-file prose or Secondary Sources section. All verified 200. None currently have a local archive binary. Ordered by appearance:

| Line | URL | Status | Archive recommended? |
|---|---|---|---|
| L58 | https://www.foxla.com/news/caltech-scientist-carl-grillmair-suspect-freddy-snyder-charged | 200 | Yes — news article, link-rot risk. Audit page `la-county-da-murder-charges-snyder.md` exists but is not linked from this line. |
| L92 | https://abc7.com/post/man-charged-killing-caltech-astrophysicist-carl-grillmair-llano-carjacking-own-relative-burglarizing-home/18626990/ | 200 | Yes — audit page `la-county-da-murder-charges-snyder.md` exists; link the audit page. |
| L93 | https://www.foxla.com/news/caltech-scientist-carl-grillmair-suspect-freddy-snyder-charged | 200 | Duplicate of L58 inline. Already has audit page. |
| L94 | https://mynewsla.com/crime/2026/02/20/man-who-fatally-shot-caltech-scientist-had-been-released-after-gun-arrest/ | 200 | Also cited in lasd-initial-report.md. |
| L95 | https://mynewsla.com/crime/2026/03/26/arraignment-postponed-for-man-charged-with-killing-caltech-scientist/ | not fetched | Not in any audit page; low priority. |
| L96 | https://pasadenanow.com/main/man-charged-with-killing-caltech-scientist-had-been-released-after-loaded-gun-arrest | not fetched | No audit page. |
| L97 | https://www.cbsnews.com/losangeles/news/caltech-scientist-shot-to-death-in-front-of-los-angeles-county-home/ | not fetched | Different CBS URL from lasd-initial-report.md (that page cites the earlier breaking-news CBS URL). No audit page for this later article. |
| L98 | https://www.yahoo.com/news/articles/accused-killer-caltech-astrophysicist-stalked-193708646.html | not fetched | Yahoo/LA Times syndication; ephemeral. No audit page. |
| L99 | https://tech.caltech.edu/2026/03/17/caltech-astrophysicist-carl-griillmair-dies-at-67/ | 200 | Audit page `caltech-ipac-memorial-statement.md` exists but is not linked from Secondary Sources. |
| L100 | https://en.wikipedia.org/wiki/Carl_Grillmair | not fetched | Tertiary source; low archive priority. |

**Note on unfetched secondary URLs:** Per audit scope, Wave 1 fetches primary-source audit-page URLs and URLs already inline in the case file that have a corresponding audit page. The four secondary-section URLs without audit pages (L95, L96, L97, L98) were out of scope for this wave. Recommend a Wave 2 pass to verify those four.

---

## No-primary-URL audit pages

None. All five audit pages in `appendices/primary-sources/grillmair/` have a `Source URL` field recorded.

---

## Orphaned audit pages (in folder, not cited in case file)

Two audit pages exist in the folder but are not linked from `cases/grillmair.md`:

1. `appendices/primary-sources/grillmair/caltech-ipac-memorial-statement.md`
   - Source URL: https://tech.caltech.edu/2026/03/17/caltech-astrophysicist-carl-griillmair-dies-at-67/ — **200, verified**
   - Document type: Caltech student newspaper institutional memorial
   - This URL appears in the Secondary Sources section (L99) but the audit page is not linked from there.
   - **Action recommended:** Link the audit page from Secondary Sources L99, or promote to Primary Sources table (it carries institutional quotes).

2. `appendices/primary-sources/grillmair/la-county-da-murder-charges-snyder.md`
   - Source URL: https://abc7.com/post/man-charged-killing-caltech-astrophysicist-carl-grillmair-llano-carjacking-own-relative-burglarizing-home/18626990/ — **200, verified**
   - Secondary URL: https://www.foxla.com/news/caltech-scientist-carl-grillmair-suspect-freddy-snyder-charged — **200, verified**
   - Document type: Criminal charging report via ABC7/FOX11
   - Both URLs appear in Secondary Sources (L92, L93) but the audit page is not linked from either.
   - **Note:** The bail amount in this audit page ($2 million) conflicts with the case file's prose ($3.175 million at L58) and the Contradictions table. The audit page may be an earlier draft; the Contradictions table correctly flags this discrepancy.
   - **Action recommended:** Link the audit page from L92 or L93 in Secondary Sources.
