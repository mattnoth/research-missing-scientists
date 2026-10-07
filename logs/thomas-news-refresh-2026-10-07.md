# Thomas news-refresh bundle — 2026-10-07

**Agent:** sub-pass news-refresh (research subagent, Fable 5.1)
**Scope:** Coverage of Jason R. Thomas published roughly 2026-05-08 through 2026-10-07, plus pre-window items surfaced this pass that are **not** in `cases/thomas.md` (flagged "pre-window"). X-Files posture; Mulder + Scully equal rigor.
**Read-only on cases/thomas.md** — bundle feeds next session's drafted Update block.
**Canonical name anchor:** Jason R. Thomas (b. 1980-01-10; Novartis Institutes for BioMedical Research, Associate Director of Chemical Biology; Murray Street, Wakefield MA; last seen ~2025-12-12 midnight; body recovered Lake Quannapowitt 2026-03-17). Wife: Kristen Bartoli.
**Tool constraint this pass:** WebSearch turn budget exhausted after ~38 queries across three cases; four planned Thomas queries (site:wakefieldma.gov, site:wakefielditem.com, OCME manner-of-death sweep, YouTube) were not run — listed under Queries logged as NOT PERFORMED.

## Headline findings

- **Nothing new in the window.** No Office of the Chief Medical Examiner (OCME) cause/manner ruling located. No formal identification announcement located (every source still says "preliminary… clothing"). No Middlesex DA or Wakefield PD statement after 2026-03-17 located. No Novartis statement. No post-recovery public statement by Kristen Bartoli. No Oversight/FBI Thomas-specific output. Websleuths thread title still reads "awaiting confirmation"; last post 2026-04-22. GoFundMe story text unchanged — still says the family is "holding onto hope." [Confirmed as negative search result; see Queries logged]
- **"Drowning" is circulating as an established fact without any on-record ruling — and Wikipedia carries it.** LA Mag (Lauren Conlin, 2026-04-24): Thomas "tragically drowned in a lake" — unsourced. ABC Australia (Lewis Wiseman, 2026-05-10, **in window**): "Died on December 12, 2025, by drowning" and "The Middlesex County, Massachusetts, medical examiner stated no foul play was involved" — **double error**: no cause has been announced, and the no-foul-play line came from DA Marian Ryan / Chief Steven Skory, not a medical examiner (Massachusetts has a statewide OCME, not a county ME). en.wikipedia.org/wiki/Missing_scientists_conspiracy_theory lists Thomas as deceased 2025-12-12 "drowning, Lake Quannapowitt" and repeats the "Middlesex County… medical examiner" misattribution nearly verbatim — Wikipedia appears to be sourcing ABC AU or a shared upstream. **Wikipedia disagrees with the case file (which correctly says the OCME has not ruled). Flag; propagate neither.** Also note: a 12-12 death date is an assumption (last-seen date), not a finding.
- **Case-file T1 URL is dead:** https://www.wakefieldma.gov/m/newsflash/Home/Detail/113 → **404**; non-mobile variant /newsflash/Home/Detail/113 → **404**; CivicAlerts.aspx?AID=113 → timeout. The Middlesex DA release (https://www.middlesexda.com/press-releases/news/body-recovered-lake%C2%A0quannapowitt-wakefield) returns **403** to this agent but is index-confirmed extant (~204 days old per index metadata). The Wakefield PD **Facebook** statement of 2026-03-17 ("no foul play is currently suspected," per Daily Caller) is an alternative T1 but not fetchable. **Flag for archive/backfill.**
- **NBC Dateline "Missing in America" URL is now fetchable (HTTP 200)** — closes the Dateline line in the 403 inventory (TODO line 24) for this URL. Page (Sarah Dahlberg, 2026-03-16 5:13 PM) carries a 2026-03-17 update; **no later update.** Verbatim: "The medical examiner has not yet identified the cause and manner of death." Case-file quotes attributed to Dateline can now be re-verified against the live page.
- **New pattern-of-life and search details not in the case file (NBC Boston, Sarah Dahlberg, 2026-03-17 — T3/T4; corroborated in part by CrimeOnline 01-05 and index snippets):**
  - Wife "heard a distinct bang" — "the sound of the mailbox closing"; she **found his Apple Watch in the mailbox**.
  - Phone and wallet "were on the bathroom counter"; he had emptied his jacket pockets on coming upstairs.
  - Train: "the conductor told her no one boarded the train there that night."
  - Clothing last seen: gray/white Columbia puffer jacket, black "Turtle Fur" hat, blue wool sweater, dark blue jeans, blue sneakers with white stripes.
  - Chief Skory: "No gloves, no hat, no jacket. Nothing," — **in tension with the same article's clothing description** (puffer jacket and hat). Likely Skory meant items *left behind* vs the article's *last-seen* list, or two different moments; flag as an intra-source contradiction to resolve, not propagate.
  - **Lake search (answers case-file OQ#3):** Skory: "The lake was partially frozen on December 13th, and it froze over completely shortly thereafter"; police "covered the lake in the first hours" (shoreline), dogs and drones combed the area, but "no one has ever been able to search the water"; dive team + sonar planned for spring thaw. The body was found by a detective on 2026-03-17 as the thaw began — consistent with that plan. **OQ#3 can be closed: the water itself was not searched in December because it was frozen.**
  - Bartoli to Dateline (pre-recovery): "There's no sign that he's in it," re the lake.
- **Pre-window items not in case file:** Daily Caller (Ireland Owens, 2026-03-23) — Rep. Tim Burchett quotes ("I don't think we should trust our government"); Thomas via People; Wakefield PD Facebook 03-17 line. Patch Wakefield (Joseph Hosey, 2026-03-17). Boston Globe (2026-03-17) body-recovery piece. Wakefield Daily Item (2026-03-18, via Local Headline News mirror; paywalled after lede) — **the only local-paper item located.** NBC Boston 3870926 (Dec 2025 search). CrimeOnline (Jacquelyn Gray, 01-05). Newsweek 04-27 (Coffindaffer) quotes the obituary: "passed away unexpectedly after having been missing since December 12, 2025."
- **Mulder-side, all pre-window, none sourced:** he8ter.substack (2026-04-24): "He had explicitly stated he was not suicidal" — **no attribution, no quote, no link**; embeds truncated @DrMargaretShow X post (2026-03-28) calling the death "suspicious." Substack S. Whitney (04-25, Perplexity-researched): work "reportedly intersected with Department of Defense contracts" — unsourced. uapmurders.com (ACT 3 AI, Inc.; "built by Grok and Claude AI research"): adds "left without a coat, gloves, or hat" (now traceable to Skory's "No gloves, no hat, no jacket") and Novartis-DoD via Daily Mail while conceding "Thomas's involvement in defense work is not publicly reported." WION (04-08): "had previously worked with the Department of Health and Human Services" — unsourced, not in case file. **No new in-window Mulder content located.**
- **Age discrepancy already in case file** (45 vs 46) persists across outlets; no new information.

## Scully-side findings

### A1. Mainstream press refresh

**ABC Australia — "FBI investigating recent deaths and disappearances of multiple US scientists"**
- **URL:** https://www.abc.net.au/news/2026-05-10/us-scientists-missing-dead-fbi-nasa/106646664
- **HTTP status:** 200 · **Date:** 2026-05-10 (**in window**) · **Byline:** Lewis Wiseman · T4 (foreign public broadcaster)
- **Confidence:** Reported; **contains errors**
- **Extract:** "Died on December 12, 2025, by drowning." "He was the assistant director of chemical biology for the pharmaceutical company Novartis." "The Middlesex County, Massachusetts, medical examiner stated no foul play was involved." — cause, date-of-death, and attributing office are all unestablished or wrong relative to the DA release.

**Mother Jones — "How the 'missing scientists' conspiracy theory went mainstream…"**
- **URL:** https://www.motherjones.com/politics/2026/05/missing-ufo-scientists-rumors-holistic-doctors/ · 200 · 2026-05-14 (**in window**) · Anna Merlan · T4
- **Extract:** Does not name Thomas. Logged as in-window cluster meta-coverage with no case content.

**Fox News — "Trump says FBI finds no clear link in missing scientists cases"**
- **URL:** https://www.foxnews.com/us/congressman-vows-find-answers-missing-deceased-scientists-cases-trump-gives-update-investigation · 200 · 2026-05-01 (pre-window) · Peter D'Abrosca · T4
- **Extract:** Thomas (45) listed among the deceased; appears in a photo caption of cases "under review." No Thomas-specific content.

**LA Mag — "Missing Scientists Mystery: Which Cases May Not Be Connected"**
- **URL:** https://lamag.com/crimeinla/missing-scientists-and-officials-whos-likely-not-part-of-the-mystery/ · 200 · 2026-04-24 (pre-window) · Lauren Conlin · T4
- **Extract:** Thomas "tragically drowned in a lake in Massachusetts in March 17, 2026" — **unsourced cause; also conflates recovery date with death date.** Train-track footage "via PEOPLE"; wife "confirmed he was struggling with mental health." Quotes @DrMargaretShow "suspicious" tweet without endorsing. **Origin candidate for the "drowned" meme in T4 space.**

**Daily Caller — "High-Profile Scientists Dead, Missing As GOP Rep Suggests Conspiracy At Play"**
- **URL:** https://dailycaller.com/2026/03/23/high-profile-scientists-dead-missing-gop-rep-suggestsconspiracy-play/ · 200 · 2026-03-23 (pre-window) · Ireland Owens · T4
- **Extract:** Body "is believed to belong to Jason Thomas, a 45-year-old scientist with multinational pharmaceutical corporation Novartis"; disappearance date via People; **Wakefield PD Facebook 03-17: "no foul play is currently suspected in the incident."** Burchett: "I think we ought to be paying attention to it." No Novartis–DoD claim here.

**Newsweek — "Missing, dead scientists: Retired FBI agent breaks down 'conspiracy' claims"**
- **URL:** https://www.newsweek.com/missing-dead-scientists-retired-fbi-agent-breaks-down-conspiracy-claims-11884556 · 200 · 2026-04-27 (pre-window) · Anna Skinner · T4 w/ T2 (Jennifer Coffindaffer)
- **Extract:** Thomas entry quotes obituary language: "passed away unexpectedly after having been missing since December 12, 2025."

**Men's Journal (AOL mirror)** — https://www.aol.com/lifestyle/eight-scientists-dead-missing-investigating-005158031.html · 200 · 2026-04-05 · Jessica McBride · T4 — Thomas via People ("no foul play is expected"); DA/PD body recovery; "Thomas, 45."

**People** — multiple pieces (Jan 5; Mar 17–18) syndicated on Yahoo/AOL; index-confirmed; originals not fetched. People is the T4 node most downstream outlets cite for the wife's account.

**Mainstream silences in window:** No NYT, WaPo, AP, Reuters, CNN, NBC, CBS, ABC (US), Boston Globe, Boston Herald, Boston.com, NBC Boston, Boston 25, WCVB, or People **Thomas-named** piece located 2026-05-08 → 2026-10-07.

### A2. Local / beat press

**NBC Boston — "Massachusetts man Jason Thomas vanished from Wakefield three months ago. Have you seen him?"**
- **URL:** https://www.nbcboston.com/news/local/massachusetts-man-wakefield-jason-thomas-vanished/3916919/
- **HTTP status:** 200 · **Date:** 2026-03-17, upd. 3:54 PM (pre-window; case file cites it as "NBC Boston report" but not these details) · **Byline:** Sarah Dahlberg | NBC News · T3 (Boston local; NBC News Dateline reporter)
- **Confidence:** Reported (wife and chief, named)
- **Extract:** Mailbox "bang"; Apple Watch in mailbox; phone/wallet on bathroom counter; conductor: no one boarded; last-seen clothing list; Skory: "No gloves, no hat, no jacket. Nothing," / "we've hit a dead end" / "wait for the lake to unfreeze"; lake partially frozen 12-13, fully frozen shortly after; shoreline covered, water never searched; spring dive/sonar plan. Bartoli: "He would not leave us." **Richest single source on search mechanics; closes OQ#3.**

**Wakefield Daily Item (via Local Headline News mirror) — "Authorities believe body of missing Murray St. man found in Lake"**
- **URL (mirror):** https://localheadlinenews.com/wakefield-daily-item-authorities-believe-body-of-missing-murray-st-man-found-in-lake/
- **HTTP status:** 200 (paywalled after lede) · **Date:** 2026-03-18 · **Byline:** none shown · T3 (hometown daily)
- **Extract:** DA Ryan and Chief Skory "confirmed that a body was recovered… yesterday afternoon"; preliminary clothing ID; reported missing 12-13. Body text behind paywall. **Only Daily Item item located; direct site: query not run (budget). Note: itemlive.com is the Lynn Daily Item — a different paper; the Wakefield paper is wakefielditem.com.**

**Patch Wakefield — "Wakefield Man Missing Since December Possibly Found In Thawed Lake: DA"**
- **URL:** https://patch.com/massachusetts/wakefield/wakefield-man-missing-december-possibly-found-thawed-lake-da · 200 · 2026-03-17 4:43 PM · Joseph Hosey · T3
- **Extract:** DA release verbatim: "Preliminary information, [including the clothing] of the victim, suggests…"; OCME "will determine the identity and the cause and manner of death"; "no foul play is suspected." No update note. Patch also has an earlier "dead male found Lake Quannapowitt" item (index).

**Boston Globe — "Missing man's body recovered from Wakefield lake, officials say"** — https://www.bostonglobe.com/2026/03/17/metro/missing-man-recovered-wakefield-lake/ · index-confirmed, not fetched · 2026-03-17 · T3 — snippet: prosecutors identified him "based on his clothing." Not in case file.

**Boston 25 News (03-17 body recovery)** — https://www.boston25news.com/news/local/body-found-north-shore-lake-believed-be-man-who-vanished-months-ago-da-says/GE72QWYDCVE3TO75AG2TW4W44A/ · index-confirmed · T3 — not in case file (case file has the Jan wife interview).

**CrimeOnline — "'He Literally Vanished'…"** — https://www.crimeonline.com/2026/01/05/he-literally-vanished-scientist-still-missing-weeks-after-hes-seen-walking-near-train-tracks/ · 200 · 2026-01-05 · Jacquelyn Gray · T5 (aggregator citing WFXT/NBC Boston) — "the train conductor said he never boarded the train that night." Earliest conductor mention located.

**NBC Boston (Dec 2025 search)** — https://www.nbcboston.com/news/local/wakefield-missing-man/3870926/ · index-confirmed · T3 — not in case file.

**Wicked Local / Wakefield Observer:** a Bartoli interview is referenced in index snippets ("stepped out to get the dogs water"); URL not captured. **Flag.**

### A3. Court / official / medical-examiner sources

- **Middlesex DA press release (2026-03-17)** — https://www.middlesexda.com/press-releases/news/body-recovered-lake%C2%A0quannapowitt-wakefield — **403** to this agent; extant per index (~204 days old). **No subsequent DA release naming Thomas or Quannapowitt located** (site:middlesexda.com query returned only this page).
- **Wakefield town newsflash (case-file T1)** — **404** at both URL forms. **Dead link; needs archive recovery (Wayback not reachable by this tool) or replacement with the DA release / PD Facebook post.**
- **Wakefield PD Facebook (2026-03-17):** "no foul play is currently suspected in the incident" (via Daily Caller). Not fetchable. T1 for PD's own statement.
- **Massachusetts OCME:** No public ruling located. OCME does not publish individual rulings; releases flow through the DA. **Absence of a DA follow-up is therefore the operative negative** — and it is a meaningful one: 6+ months post-recovery with no identification confirmation or cause announcement is longer than typical for a non-suspicious drowning with a strong clothing match, but is not unusual where the family requests privacy or where the DA sees no public-safety reason to update. Both readings are consistent with the record.
- **House Oversight / FBI:** No Thomas-specific document. Thomas is in the cluster lists (Fox 05-01 "13"; Union Leader "expanded list of 13" — 403, date unverified) but no official has addressed him individually. Burchett (Daily Caller 03-23) is the only member of Congress whose remarks have been paired with Thomas by name, and only by the outlet's juxtaposition.
- **Death certificate:** Massachusetts death records are available by request to the town clerk (Wakefield) — a lawful public-records route; out of scope for a web-only pass; note for RUNBOOK.

### A4. Family / employer comms

- **Kristen Bartoli:** No statement after 2026-03-17 located in any indexed item. Pre-window quotes (NBC Boston 03-17; Dateline 03-16; Boston 25 Jan; Wicked Local) are the family voice. GoFundMe (organizers Brianna Florovito, Katherine Biggar; beneficiary Kristen Bartoli) — **$65,751 of $70K, 726 donors; no organizer updates at all**, story still describes him as missing. [T1 for family-side fundraiser; Confirmed as static]
- **Novartis / NIBR:** No statement located; dedicated query returned only unrelated NIBR leadership items. **Negative.**
- **Obituary (Legacy / Edward V. Sullivan Funeral Home):** 403 on fetch this pass; Newsweek quotes it ("passed away unexpectedly after having been missing since December 12, 2025"). The obituary's own phrasing — dating the loss to the disappearance, not the recovery — is the family's chosen framing and is consistent with the age-46 statement if death is dated to March.
- **Community:** No vigil, bench, memorial run, or Novartis tribute located. **Contrast Loureiro** (school naming, 10K, parliament vote, $423K fund): Thomas's public memorial footprint is essentially the GoFundMe and the obituary.

## Mulder-side findings

### B1. Precursor / disclosure-community venues

- **he8ter.substack.com — "Big Medicine aka 'Rockefeller Medicine'"** — https://he8ter.substack.com/p/big-medicine-aka-rockefeller-medicine — 200 — 2026-04-24 — Thomas "working on promising non-chemo approaches," "found dead under suspicious circumstances," "He had explicitly stated he was not suicidal." **No source, quote, or link for the last claim.** Embeds truncated @DrMargaretShow post. [T7, Alleged by an anonymous Substack; unverifiable]
- **X — @DrMargaretShow** (status 2037734682993827941; 2026-03-28) — "CANCER SCIENTIST FOUND DEAD UNDER SUSPICIOUS CIRCUMSTANCES." Not fetched (X returns 402 to this pipeline). [T7]
- **smbwhitney233757.substack.com (S. M. Belanger Whitney, 2026-04-25)** — 200 — "a Novartis researcher whose work reportedly intersected with Department of Defense contracts" — unsourced; "Researched by Perplexity." [T7, AI-assisted]
- **uapmurders.com** — https://uapmurders.com/physics/Details/Jason_Thomas/ — 200 — "Copyright © 2026 ACT 3 AI, Inc."; "built by Grok and Claude AI research." Two internally inconsistent profile versions (11:53 PM vs "around midnight"; parents "within hours" vs "roughly 90 minutes"; "Kristen Bartoli" vs "Kristen Thomas"). Rates UAP link "UNCERTAIN"/"speculative." Cites a Daily Mail URL (article-14607417) for Novartis–DoD contracts. **AI-compiled; use only as a map of claims in circulation.** [T7]
- **Threads — @chrislim.ig** (index) — list-post; "no foul play is expected." [T7]
- **Decrypted Matrix "Dead Scientists Files (1994–2026)"** — index-confirmed database page. [T7]
- **Podcast — "UFO WARNING," episode "MISSING UFO EXPERTS"** — https://podscan.fm/podcasts/ufo-warning/episodes/missing-ufo-experts — 200 — 2026-03-29 — 24 min — names "Jason Thomas, 45, an assistant director of chemical biology at Novartis"; renders Loureiro as "Nuno Lurio." [T7]
- **Nothing new in window.** All Mulder-side Thomas items cluster in 03-23 → 04-25.

### B2. Insider venue — expert commentary

- **Jennifer Coffindaffer** (ret. FBI; Newsweek 04-27; Men's Journal) — "not buying the conspiracy"; lists Thomas. [T2]
- **Steven Novella MD** (NeuroLogica 04-21) — "Jason Thomas—Pharmaceutical researcher. Found dead: March 2026." Base-rate argument; separately notes the list's inclusion of a "pharmaceutical worker" as evidence of over-broad cohort construction. [T2; pre-window; not in case file]
- **David Hand** (SciAm 05-07) — does not name Thomas. [T2]
- **Rep. Tim Burchett** (Daily Caller 03-23) — generic distrust-of-government remarks juxtaposed with Thomas by the outlet; no Thomas-specific claim. [T1 for his own words; T4 juxtaposition]

### B3. Domain investigation — Novartis / chemical biology / DoD-contract claim

- **Novartis–DoD contracts claim:** appears only in T7 (uapmurders, citing Daily Mail; Whitney Substack). Novartis, like every large pharma, holds federal contracts (e.g., BARDA/DoD medical countermeasures); that is not evidence Thomas's chemoproteomics/phenotypic-screening work touched them. uapmurders itself concedes his "involvement in defense work is not publicly reported." **Case file's inclusion-rationale ("no documented connection to defense") stands; nothing surfaced this pass changes it.**
- **HHS claim (WION 04-08):** "had previously worked with the Department of Health and Human Services" — unsourced; could reflect NIH-funded postdoc work (Scripps) mis-rendered as "worked with HHS." Not propagated.
- **"Non-chemo approaches" / "cure for cancer" framing** (he8ter; X posts per uapmurders) — rhetorical inflation of chemical-biology drug-discovery work; no publication cited.

### B4. Foreign coverage

- **Australia:** ABC AU 05-10 (in window; three errors on Thomas). [T4]
- **France:** fr.helm.news (2026-03-18) — "Un corps trouvé dans un lac du Massachusetts…" — **404** on fetch; index-confirmed; appears to be an aggregator translation. [T5]
- **India:** WION 04-08 (HHS claim). [T4]
- **Russia/China state media:** none located naming Thomas.
- Case file's "No significant foreign coverage" remains accurate; the two items above are list-inclusions, not reporting.

### B5. Geographic context — Massachusetts cluster

- No change. Thomas (Wakefield) and Loureiro (Brookline) remain the two MA cases, ~15 miles apart, both with official no-foul-play / lone-actor framings. Boston Globe/Boston.com 04-24/28 ("including two in Mass.") is the only in-state cluster framing; pre-window. No MA official has characterized the two as related.
- **Lake Quannapowitt micro-geography (from NBC Boston 03-17):** the lake was shoreline-covered on 12-13 but ice prevented water search; the recovery point was reached by a detective on foot at the thaw. Case-file OQ#2 (how he entered the lake; route from North Ave/Chestnut St railroad crossing to the lake) remains **open** — no source reconstructs it. The railroad crossing at North Avenue/Chestnut Street is on the lake's west side; the distance is short, but no outlet has stated where on the shore the body was found.

## Anomalies

1. **"Drowning" without a ruling.** LA Mag (04-24) → ABC AU (05-10) → Wikipedia cluster table. No OCME/DA source. The case file should add a Contradictions entry: "cause of death reported as drowning in T4/T5 sources without official ruling."
2. **"Middlesex County medical examiner" misattribution** (ABC AU; Wikipedia). Massachusetts has a statewide OCME; the no-foul-play line is DA Ryan's. Wikipedia disagreement logged; propagate neither.
3. **Death date rendered as 12-12** (ABC AU; Wikipedia table) — assumption from last-seen; obituary says age 46 (implies death dated after 01-10-2026, i.e., recovery-dated). Three different implicit death dates now circulate (12-12, 03-17, "unknown").
4. **Case-file T1 URL dead (404)** — wakefieldma.gov newsflash. Replace/archive.
5. **Dateline URL now 200** — 403-inventory item resolved for this URL.
6. **Skory "No gloves, no hat, no jacket" vs same article's "puffer jacket… black hat"** — intra-source tension in NBC Boston 03-17; resolve before quoting either.
7. **Apple Watch in mailbox** — well-sourced (NBC Boston, wife's account) and absent from the case file. Behaviorally significant either way: deliberate shedding of a trackable device (Scully: intent; Mulder: "left everything") — both sides can claim it; record it neutrally.
8. **"Explicitly stated he was not suicidal"** (he8ter) — unsourced; contradicts nothing on record (no one has said he was) but asserts a fact no named person has reported. Not propagated; logged.
9. **No DA follow-up in 6+ months** — meaningful negative; consistent with family-privacy or no-public-safety-interest, also consistent with a pending toxicology/undetermined manner. Not resolvable from public web.
10. **GoFundMe never updated post-recovery** — family has chosen total public silence since 03-17. Datapoint, not inference.
11. **uapmurders internal inconsistencies** (two versions, two wife surnames, two parent-death intervals) — illustrates AI-compiled case files drifting; cite only as claims-map.
12. **Wicked Local interview** referenced but URL uncaptured — flag.

## Imbalance note

**Scully side holds; Mulder side has not moved since late April.** The in-window record is a single foreign T4 list-piece with three errors and a Wikipedia table that inherited them. Everything substantive is pre-window and Scully-leaning: a frozen lake that could not be searched, a thaw, a detective, a clothing match, a DA's no-foul-play, a family that has gone quiet.

Where the Scully side is thin: (a) **the OCME has still said nothing** — "drowning" is a media inference, and manner (accident/suicide/undetermined) is unknown; (b) no formal identification has been publicly confirmed; (c) OQ#2 (route to the lake) is unreconstructed; (d) the one T1 web document in the case file is now a dead link.

Where the Mulder side is thin: its three distinctive claims — "not suicidal," DoD contracts, HHS — have **zero** named sources among them; its strongest datapoint (watch + phone + wallet left behind) is shared with the Scully side and is more parsimoniously read as intent.

**Evidentiary parity check:** "Found in a lake after a thaw, no foul play" (Scully) and "died under suspicious circumstances" (Mulder) both rest on the same DA sentence plus the absence of an OCME ruling. The case file should say so, and should resist importing "drowning" until the DA or OCME says it.

**To balance next session:** (1) browser-fetch Middlesex DA release and save; (2) locate/replace the dead Wakefield newsflash (Wayback via browser); (3) run the four unperformed queries (site:wakefieldma.gov, site:wakefielditem.com, OCME manner sweep, YouTube); (4) capture Wicked Local interview URL; (5) consider a Wakefield town-clerk death-record request path for RUNBOOK (public record, not contact).

## Queries logged

WebSearch (Google index), in order run. Turn budget exhausted at #38 across the three cases.

1. `"Jason Thomas" Wakefield Lake Quannapowitt medical examiner cause of death`
2. `site:middlesexda.com "Jason Thomas" Wakefield`
3. `Wakefield Daily Item "Jason Thomas" OR "Kristen Bartoli" 2026`
4. `"Jason Thomas" Wakefield Novartis drowning OR "cause of death" OR "medical examiner" ruled 2026`
5. `"Jason Thomas" Wakefield identified OR identification confirmed "medical examiner" April 2026 OR May 2026 OR June 2026`
6. `"Jason Thomas" Wakefield "Lake Quannapowitt" memorial OR vigil OR tribute OR Novartis statement 2026`
7. `"Kristen Bartoli" Jason Thomas Wakefield interview OR statement OR Dateline update`
8. `"Jason Thomas" Wakefield Novartis YouTube OR TikTok OR podcast scientist lake 2026`
9. `"Jason Thomas" Wakefield "Apple Watch" OR mailbox OR "train conductor" missing December 2025`
10. `"Daily Item" Wakefield "Jason Thomas" obituary OR funeral OR "Murray Street" 2026`
11. `Novartis NIBR "Jason Thomas" chemical biology tribute OR memoriam OR dedication 2026`
12. `"Jason Thomas" Wakefield Massachusetts Dateline YouTube OR "NBC Boston" video lake body 2026`
13. (cross-case) `FBI report missing dead scientists findings released Patel 2026 White House review conclusion`
14. (cross-case) `House Oversight Comer Burlison missing scientists briefing results Maiwald Loureiro Thomas`
15. (cross-case) `FBI "missing scientists" final report released OR concluded OR findings June 2026 OR July 2026 OR August 2026 OR September 2026`
16. (cross-case) `site:oversight.house.gov scientists missing dead briefing 2026`

**NOT PERFORMED (budget exhausted):** `site:wakefieldma.gov "Jason Thomas" OR Quannapowitt body recovered 2026`; `site:wakefielditem.com "Jason Thomas" OR Quannapowitt OR "Murray Street" 2026`; `"Jason Thomas" Wakefield "manner of death" OR "undetermined" OR "accidental" OR "ruled" "Chief Medical Examiner" Massachusetts 2026`; `YouTube "Jason Thomas" Wakefield missing Novartis scientist video`.

**WebFetch log (URL → observed status):**
uapmurders.com Jason_Thomas → 200 · middlesexda.com release → **403** (extant per index) · websleuths.com thread 757676 → 200 · dailycaller.com 2026/03/23 → 200 · **wakefieldma.gov/m/newsflash/Home/Detail/113 → 404** · wakefieldma.gov/newsflash/Home/Detail/113 → 404 · wakefieldma.gov/CivicAlerts.aspx?AID=113 → timeout · localheadlinenews.com (Daily Item mirror) → 200 (paywalled) · fr.helm.news → 404 · he8ter.substack.com → 200 · gofundme.com samu3c → 200 · nbcboston.com 3916919 → 200 · legacy.com Thomas obit id=61184839 → 403 · crimeonline.com 2026/01/05 → 200 · **nbcnews.com Dateline rcna263785 → 200** · patch.com wakefield possibly-found → 200 · podscan.fm UFO-Warning → 200 · lamag.com → 200 · abc.net.au 05-10 → 200 · motherjones.com → 200 · foxnews congressman-vows → 200 · newsweek 11884556 → 200 · aol.com Men's Journal mirror → 200 · wionews.com → 200 · theness.com → 200 · en.wikipedia Missing_scientists_conspiracy_theory → 200 · unionleader 13-list → 403 · thehill psychological-autopsies → 403.

## Candidate videos for ingestion

Not transcribed. **No in-window video located.** Pre-window candidates:

| Platform / host | Uploader | Title (as shown) | Upload date | Approx length | Why it matters |
|---|---|---|---|---|---|
| nbcnews.com/dateline (web feature; video likely embedded) | NBC News / Dateline "Missing in America" (Sarah Dahlberg) | "Missing husband Jason Thomas was last seen three months ago in Wakefield, Massachusetts" | 2026-03-16 (upd. 03-17) | unknown | Sole source for several case-file quotes (Skory on scent/trains; Bartoli); now fetchable at 200 |
| boston25news.com (embedded) | Boston 25 / WFXT | "'He literally vanished': Wakefield woman asks public for help in search for husband" | 2026-01-05 | unknown | Wife's on-camera appeal; parents'-deaths account; T3 |
| nbcboston.com (embedded) | NBC Boston (WBTS) | "Body recovered from lake in Wakefield believed to be that of missing man" (3917208) | 2026-03-17 | unknown | DA/Chief on-camera; recovery footage |
| nbcboston.com (embedded) | NBC Boston | "Wakefield search for missing man Jason Thomas" (3870926) | Dec 2025 | unknown | NEMLEC K-9/drone search footage; Skory |
| podscan.fm — "UFO WARNING" | UFO WARNING (host unnamed) | "MISSING UFO EXPERTS" | 2026-03-29 | 24 min | T7 audio; names Thomas; "Nuno Lurio" mis-rendering |
| x.com/DrMargaretShow (status 2037734682993827941) | The Dr. Margaret Show | "JASON THOMAS: CANCER SCIENTIST FOUND DEAD UNDER SUSPICIOUS CIRCUMSTANCES" | 2026-03-28 | n/a (post; may link video) | Origin node for the "suspicious" framing re-amplified by he8ter; X returns 402 |
| youtube.com/watch?v=nukN1ooaNik | unknown (page shell only) | "Missing scientists: FBI probes 11 missing or dead nuclear scientists" | unknown | unknown | Cluster explainer; identify uploader before use |
