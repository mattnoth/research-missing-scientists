# Research Log

Chronological record of searches performed, sources consulted, and decisions made. Also serves as the append-only session ledger per [.claude/commands/end-session.md](../.claude/commands/end-session.md).

## 2026-05-08 — Source-URL inline + local-archive cleanup (continue session)

Continue session generalizing the 2026-05-08 mccasland BCSO inline-source-URL worked-example across the dossier. Wave 1 fired 11 parallel read-only Sonnet 4.6 subagents (one per case) scanning case files for inline citations whose link is *only* a local primary-source audit page; output at [logs/source-url-audit-2026-05-08/](source-url-audit-2026-05-08/) (per-case detail) + [logs/source-url-audit-2026-05-08.md](source-url-audit-2026-05-08.md) (consolidated). **Headline finding**: the case-file-links-only-audit-page pattern is *not* widespread — 8 of 11 cases already use direct external URLs as primary inline citations. Only 3 cases had patches: `cases/mccasland.md` L30 (Riverside Research / PR Newswire URL surfaced — missed in the worked-example pass; URL `https://www.prnewswire.com/news-releases/riverside-research-welcomes-dr-neil-mccasland-to-their-board-of-trustees-300921796.html`); `cases/garcia.md` L74 (NM DPS record URL surfaced — `https://missingpersons.dps.nm.gov/mpweb/mpdetailreport_serv?id=M101688`); `cases/garcia.md` L75 (NNSA statement annotated as no-primary-URL with explicit framing — statement was provided to journalists in response to inquiries, never republished on nnsa.energy.gov / kcnsc.doe.gov); `cases/grillmair.md` L86–88 (Primary Sources table for Caltech memorial / LA County BoS adjournment / LASD initial report now carries primary URLs alongside reconstruction-notes-secondary). Wave 2 also applied audit-page hygiene: chavez `los-alamos-county-search-update.md` + `lapd-missing-person-notices.md` Source URL paths corrected `/News-articles/` → `/News-media/` to match the case file's canonical form per the Phase 1 redirect fix; garcia `nnsa-statement.md` + loureiro `doj-confession-transcript-summary.md` no-primary-URL framing made explicit; loureiro `mit-statement-20251219.md` removed (duplicate of `mit-statement-dec19-suspect-identified.md`, same MIT News URL + Dec 19 2025 date). Local-archive download: HAL5 antigravity-talk PDF for eskridge (2.47 MB, T1, hal5.org, HTTP 200, valid PDF v1.4) saved to `appendices/primary-sources/eskridge/HAL5-Dec2018-Talk-AntiGravity.pdf`; eskridge case file Key Dates (L17) + Primary Sources (L79) entries reference the local archive alongside the URL. **Hard rule honored**: no new external research; primary URLs were only surfaced where already documented in audit-page frontmatter. **Findings out of session scope** (9 content/voice/structure issues from the audit) routed to [TODO-research.md](../TODO-research.md) new "Source-URL cleanup follow-ups" section: hicks coroner data not in narrative; casias Taos News now accessible; garcia mislabeled APD audit page; grillmair $2M-vs-$3.175M bail discrepancy; reza commenter "phone reported dead" claim + missing audit pages for several S-numbered sources; maiwald obit overstatement on autopsy; loureiro NBC News 403 sole-source quotes; mccasland Dayton Daily News Wayback retry. **403-blocked URL inventory** at [logs/403-urls-2026-05-08.md](403-urls-2026-05-08.md) — 22 URLs across 9 cases for follow-up browser-access confirmation pass (separate session per user direction). Subagent strategy: 11 parallel Wave-1 audit agents (Sonnet 4.6, general-purpose, web-equipped, read-only on case files + audit pages); main thread consolidated audit + applied Wave-2 patches sequentially (6 line edits + 4 audit-page edits + 1 download + 1 deletion). User checkpoint between waves confirmed scope (no expansion), approved HAL5 download, requested 403-URL list as separate plain file. Three commits: `7fa8346` source-URL cleanup (research-content work, pushed); `5df44c4` Phase 6 bundles + bookkeeping leftover (committed-and-pushed so origin has the bundles in time for the queued Phase 6 apply session); this entry's commit covers session bookkeeping. Branch clean at session end.

## 2026-05-08 — Phase 6 depth-pass session synthesis (mccasland / garcia / reza)

Main-thread session orchestrating Phase 6 Step B + Step C union-pick depth-pass per [logs/triage-2026-05-08.md](triage-2026-05-08.md). Six subagents fired in two waves of three parallel: Wave 1 source-deepening (mccasland / garcia / reza), Wave 2 news-refresh (same three). All six bundles returned successfully; subagents appended their own per-bundle entries below. **Synthesis output:** three drafted `## Update — 2026-05-08` blocks at [drafts/mccasland-update-block-2026-05-08.md](../drafts/mccasland-update-block-2026-05-08.md), [drafts/garcia-update-block-2026-05-08.md](../drafts/garcia-update-block-2026-05-08.md), [drafts/reza-update-block-2026-05-08.md](../drafts/reza-update-block-2026-05-08.md). Each draft contains the case-file Update-block content (headline updates + Scully-side A1-A4 + Mulder-side B1-B5) plus separate Apply notes + Imbalance + Anomalies appendix for the apply session's reference. **No edits to `cases/*.md` this session.** Cross-case headline findings: (mccasland) DeLonge–Podesta meeting was a six-attendee scheduled meeting via 7 WikiLeaks emails (Wilkerson + Lockheed Skunk Works EVP Rob Weiss + retired Maj Gen Michael Carey attending); Comer/Burlison Apr 20 letters name McCasland in body and DoW response is "no active national security investigations" of any SAP-clearance-holder missing person; Pagosa Springs CO second home was searched and clothing items located there (case file walkback needed); PhD year 1989 not 1988; KPC board + DBE Consulting LLC affiliations. (garcia) Naming question resolved — Steven Abel Garcia (NM DPS T1 + Wikipedia T4 agree; "Eddison" was prompt error); Daily Mail original Chris Melore URL surfaced (article 15722375, 2026-04-11); Garcia named in Apr 20 House Oversight letters; NM DPS record-header date anomaly (08/12/2025 precedes 08/28/2025); KCNSC NM Operations confirmed at 2540 Alamo SE; three documented KCNSC outreach attempts with zero responses; new SFNM Cormac Dodd + KOAT John Rupolo T3 sources; new anonymous-source claims (KCNSC internal investigation of work computers, Kirtland AFB mission bridge, "bottle of water" pattern detail); "two anonymous sources" pluralization claim flagged. (reza) Family on the record (anonymously) for first time across LA Magazine + Daily Mail/London Mail mirror — abduction theory, "scared for our safety"; Comer/Burlison letters explicitly name Reza + tie her to McCasland; NASA spokesperson Bethany Stevens issued first formal (general) statement; Snopes "could not independently verify" Reza's JPL employment conflicts with Allan Petre's @astro_allan colleague-direct X post; Hardwick died 2014 not 2015 (5 T1/T2 sources confirm — repo correction); all three US Mondaloy patents abandoned; Russian RU2301276C2 only granted patent (UTC 2007, invalid 2012); patent custody chain Boeing → UTC → PWR → AR → L3Harris → AE Industrial Partners; Boeing 2004 HENAAC press release; AR1 cancellation 2018; L3Harris $0 developed-tech-asset valuation; 2:30 PM Twin Peaks Saddle anguish report (T7 forum reconstruction) — not in case file. Cross-case quote-provenance hazard: the Reza-McCasland "complete chain of custody for Mondaloy" framing originated in IBTimes UK (Michael Toledo, 2026-04-06) without external citations, propagated through N.Y. Post (Galvin/Hussain), and is now footnoted in the T1 Comer/Burlison Congressional letter. Cross-case symmetric silences: BBC, Le Monde, Spiegel, El País, NHK, Asahi, Yomiuri, TASS, Xinhua, People's Daily — all silent on all three cases; Tom DeLonge personally silent on McCasland through entire refresh window; Wilkerson silent in window; ATA/BlueHalo/Riverside silent; JPL silent on Reza; KCNSC/NNSA/Honeywell FM&T silent on Garcia. Capability anomaly affecting bundle quality: agent-level blocks on web.archive.org (total — Find-a-Grave Wayback retrieval NEGATIVE; user-side curl flag), www.dailymail.co.uk (total), x.com (402), oversight.house.gov (403 PDFs alive on curl), newsnationnow.com (403 systematic), lamag.com (403 systematic), snopes.com (402). Phase 3 archival pipeline is the proper fix. TODO-research.md Phase 6 Steps A/B/C ticked. Apply step is a separate session.

## 2026-05-08 — Garcia news-refresh sub-pass (last ~30 days, parallel agent)

## 2026-05-08 — McCasland news-refresh sub-pass (last ~30 days, parallel agent)

Subagent fired for news-refresh on the McCasland case (single agent, web-equipped, Opus 4.7 1M, read-only on `cases/mccasland.md`). Output: [logs/mccasland-news-refresh-2026-05-08.md](mccasland-news-refresh-2026-05-08.md). Refresh window: 2026-04-08 through 2026-05-08. **Headline finding**: federal probe formally engaged the McCasland case in window — White House (Press Sec. Karoline Leavitt + President Trump April 14–17, 2026) confirmed FBI–WH interagency review; **House Oversight Comer/Burlison letters dated 2026-04-20 to FBI Patel, NASA Isaacman, DOE, and DoW Hegseth set April 27 staff-level briefing deadline**, naming McCasland; DoW response (per IBTimes UK 2026-04-27): "no active national security investigations" of any current/former clearance-holder SAP-involved missing person; NASA: "nothing related to NASA indicates a national security threat" [T1 Comer/Burlison letters + T4 cluster, Confirmed]. **Second**: **Reza/Mondaloy connection now mainstream-mainstream** via NewsNation "ex-colleagues" framing per authorities + WION "Mondaloy mystery" piece — shifts the McCasland-Reza link from H4-style speculation to Reported claim. Forteanwinds.com (T6, 2026-04-13) "Mondaloy chain" introduces a third figure — **Dallis Hardwick (AFRL materials scientist under McCasland's command, d. 2014, cancer)** — single-sourced T6, has not surfaced in mainstream; flag for verification next session via DTIC and obituary searches. **Third**: **Albuquerque Journal April 20 piece (Nakayla McClelland)** is the strongest T3 in window — first T3 mainstream confirmation that BCSO searched a **Pagosa Springs CO residence "where clothing was discovered"** (this completes the chain Pagosa Springs Sun [2026-03-18] → ABQ Journal [2026-04-20]); also names McCasland's Kirtland Partnership Committee board service. **Fourth**: **Dayton Daily News (Samantha Wildow, 2026-04-22)** — McCasland's AFRL-hometown press picked up the case in window via the federal-probe / AFRL angle; first refresh-window Dayton coverage. **Fifth**: **Coulthart-side mainstream presence sustained** across 6+ NewsNation pieces in window + *Drop Dead Serious With Ashleigh Banfield* (Apple Podcasts) — "grave national security crisis" framing. **Astonishing Legends Episode 329 "UFO Insiders Iced?" (2026-04-26)** is the first legacy paranormal-research podcast to lead a full episode with McCasland. **Will Cain Show X post 2026-04-21 ("Start with Neil McCasland")** elevates McCasland to "central" position in cluster framing on Fox-platform. **Sixth**: **Wilkerson silence** — no new family statement in April 8 – May 8 window; CNN April 30 (T.M. Brown byline) re-cycles existing March 11 Newsweek "no special knowledge" line. **Tom DeLonge himself silent** on McCasland's disappearance through the entire refresh window — TTSA, X, podcasts all turn up no DeLonge first-person statement. **ATA/BlueHalo silent**; **Riverside Research silent**. **Seventh**: **CNN April 30 explicitly walks back Burchett's "took his revolver" framing** — first instance in window of mainstream T4 actively correcting a sitting congressman's narrative. **Foreign coverage**: IBTimes UK active (~9 pieces in cluster, multiple bylines including Jim Manzon, Manuel Demegillo, Aiza Moraña, Glory Moralidad); Hindustan Times confirmed via Google Translate; WION India Mondaloy piece + 5-things explainer; Pravda USA April 21 in window re-circulating NY Post; Daily Mail Chris Melore byline confirmed-published via CNN April 30 attribution but dailymail.co.uk URLs not directly indexable (replicates Eskridge/Reza/Garcia pattern). **No Le Monde, Spiegel, El País, BBC, NHK, Asahi, Yomiuri, TASS, Xinhua, People's Daily coverage of McCasland located** — same Continental Europe / BBC / Japan / China-state silence as the other case sub-passes. **Burlison's "Immovable" Seoul-area 270-foot UFO claim** (IBTimes UK 2026-04-20) is a sitting-congressman investigative thesis that should be tier-parity-treated as Reported. **londonmail.co.uk family piece (2026-05-02, "scared for our safety")** appears to be Reza family rather than McCasland family per URL slug content — flag for direct verification next session. **TikTok asymmetry**: site:tiktok.com search dominated by *Grant McCasland* (Texas Tech basketball) noise; Neil McCasland TikTok "discover" hubs exist but in-app curated URLs needed (W-1 standing pattern). **Reddit**: r/UFOs activity confirmed via cybernews.com but direct enumeration not completed — flag for next session. **April 27 House Oversight briefing deadline passed in window with no public follow-up disclosure** — staff-level/classified briefings; flag for next-session monitor of any leaked or follow-on Burlison/Comer statements about briefings' substance. ~44 search queries, ~15 direct fetches; mixed success. Notable systematic failures: NewsNation 403 systematic, oversight.house.gov 403 (PDFs and press release), x.com 402, snopes.com 402, kerrycassidy.substack.com succeeded. No edits to `cases/mccasland.md`. Bundle feeds next session's drafted Update block.

## 2026-05-08 — Reza news-refresh sub-pass (last ~30 days, parallel agent)

Subagent fired for news-refresh on the Reza case (single agent, web-equipped, Opus 4.7 1M, read-only on `cases/reza.md`). Output: [logs/reza-news-refresh-2026-05-08.md](reza-news-refresh-2026-05-08.md). Refresh window: 2026-04-08 through 2026-05-08. **Headline finding**: family has spoken on the record for the first time, in two parallel disclosures — (1) **LA Magazine "Monica Reza Family Questions Missing Scientist Investigation"** (Lauren Conlin exclusive, ~late April 2026; HTTP 403 systematic on direct fetch but corroborated through Modernity / SGT Report / IBTimes UK 2026-05-07 mirrors): family confirms Reza was actively employed as JPL Director of Materials Processing at time of disappearance; was deepening yoga practice; had taken time off to care for ailing relative; **neither FBI nor White House has contacted the family** despite the publicly announced federal probe; investigators "ruled out a fatal wildlife encounter" — no clothing remnants, backpack, biological evidence; (2) **Daily Mail UK / London Mail mirror 2026-05-02** (Chris Melore byline; Daily Mail direct fetch blocked at agent level same as Eskridge bundle pattern): eight-source interview; verbatim family quotes "I know in my gut that she was abducted" / "Whoever did this, if it was not an accident, was a professional"; family + friends "scared for our safety after government officials said they are looking into Reza's disappearance"; long-time friend "She is not the type to just leave without telling people and she definitely was not a suicidal person." [T4, **Confirmed as published**; underlying claims **Reported / Alleged**]. **Second major finding**: **NASA spokesperson Bethany Stevens issued formal statement** (via Newsweek 2026-04-21): "NASA is coordinating and cooperating with the relevant agencies in relation to the missing scientists. At this time, nothing related to NASA indicates a national security threat" — first agency-level statement in the corpus, though not Reza-specific. **Third**: **Snopes 2026-04-28** explicitly "could not independently verify Reza's employment" at JPL — directly conflicts with Allan Petre's (@astro_allan) JPL-internal X post and the family confirmation; NASA also did not respond to Snopes' inquiries. Recursive-citation hazard analogous to Eskridge bundle's Wikipedia-Birmingham-PD error pattern. **Fourth**: **commercial-aerospace tie surfaced in mainstream**: Fortune 2026-04-21 (Catherina Gioino) framed Reza's nickel super-alloy as relevant to "reusable rocket programs including New Glenn and Starship" — Blue Origin and SpaceX named alongside Reza for first time; both "did not respond to Fortune's requests for comment." **Fifth**: **Pasadena Now staff-bylined piece (Gab Apo, 2026-04-22)** is the first T3 local-beat hyperlocal Pasadena coverage clustering Reza-Hicks-Maiwald-Grillmair as the four-case Pasadena sub-cluster. **Sixth**: **disappearance-narrative granularity** sharpened — Reza rode in with male yoga instructor; trail started ~6:30 AM; female companion only went halfway; the "running on terrain" anomaly is now redistributed across LA Magazine, Modernity, SGT Report, Daily Mail. Hiking-companion identities remain anonymous in all coverage. **Find a Grave**: memorial still removed since ~2026-03-27; no new memorial created. **Cell phone forensic data + 911 scream**: still undisclosed; no LASD movement. **Local-LA broadcast asymmetry**: KTLA / CBS LA / ABC LA / NBC LA / LA Daily News / Pasadena Star-News produced **no new Reza-named refresh-window pieces** — all April-May 2026 LA-area coverage ran through Pasadena Now, LA Magazine, Patch, Fox 11 LA. **TikTok asymmetry**: Reza-specific TikTok content thin vs. Eskridge — Reza Mulder-side ecosystem operates primarily via Substack (Sentinel, Front Page Detectives) + YouTube (PopCrimeTV / Conlin) + X (Conlin @conlin_lauren post 2026-04-22 "Imagine having the coordinates…still no sign of her"). **Foreign coverage**: UK + India primary axis (IBTimes UK 2026-05-07 Glory Moralidad mirrors LA Magazine; WION India; Daily Mail Chris Melore); BBC / Le Monde / Spiegel / RT / TASS / Xinhua all silent on Reza specifically — same pattern as Eskridge except RT covered Eskridge while RT silent on Reza. **Eispiraten German-language true-crime forum** active multi-page Reza thread (https://eispiraten.com/viewtopic.php?t=9445) flagged for next-session content review. **Notable fetch failures**: Daily Mail UK (agent-level block, same as Eskridge); LA Magazine Conlin pieces (HTTP 403 systematic); Snopes (HTTP 402); House Oversight letter PDFs (HTTP 403 systematic — verbatim language captured via T4 mirroring); subintelligenceagency Substack (HTTP 404); X / Twitter posts (HTTP 402); CNN content truncated; NewsNation systematic 403; Wayback Machine blocked at agent level. ~29 search queries, ~20 direct fetches. **No edits to `cases/reza.md`.** Bundle feeds next session's drafted Update block.

## 2026-05-08 — Garcia news-refresh sub-pass (last ~30 days, parallel agent)

Subagent fired for news-refresh on the Garcia case (single agent, web-equipped, Opus 4.7, read-only on `cases/garcia.md`). Output: [logs/garcia-news-refresh-2026-05-08.md](garcia-news-refresh-2026-05-08.md). Scope: 2026-04-08 through 2026-05-08. **Cormac Dodd byline confirmed** at Santa Fe New Mexican (2026-04-22, updated 2026-04-23) — "4 missing New Mexicans among disappearances, deaths prompting federal investigation"; mirrored at Taos News with byline preserved. **Strongest in-state T3 piece**, but APD spokesperson remains unidentified (no APD spokesperson is named in any 30-day-window Garcia coverage indexed this session). **Three new T4 mainstream pickups** in window: Newsweek "Wave" (Joe Edwards, Apr 23 / updated May 1, https://www.newsweek.com/wave-of-missing-or-dead-us-scientists-everything-we-know-11867967); Newsweek "Map" (Joe Edwards, Apr 22, https://www.newsweek.com/map-last-known-location-missing-scientists-11862249); Fortune (Catherina Gioino, Apr 21, https://fortune.com/2026/04/21/scientists-disappear-die-nasa-space-blue-origin-spacex/) — Fortune notably uses stronger "oversaw nuclear weapons assets" framing without sourcing chain. **Two new T4 foreign mainstream pickups**: IBTimes UK (Manuel Demegillo, Apr 21, https://www.ibtimes.co.uk/us-scientists-mysterious-deaths-disappearances-1792885; Rosemarie Zamora, Apr 16, https://www.ibtimes.co.uk/mystery-surrounds-disappearance-scientist-security-clearance-1792078); The Telegraph UK (Ruth King, May 3, via Ruthfully Yours mirror — original Telegraph URL flagged for next pass). **Rolling Stone (Mary Jane Gibson, May 4)** via Yahoo syndication — softer "NNSA facility in Albuquerque" framing rather than naming KCNSC. **Pravda EN** (Apr 12, https://news-pravda.com/world/2026/04/12/2233631.html) explicitly names Honeywell + NNSA — more aggressive institutional attribution than US mainstream. **Fox 4 Kansas City / WDAF (Olivia Johnson, 2026-04-23, https://fox4kc.com/news/man-contracted-out-of-kansas-city-nuclear-facility-among-10-missing-dead-in-us/)** is the only KC-area pickup; explicitly states "FOX4 has reached out to KCNSC for comment about Garcia's disappearance, but has not received a response back." No Kansas City Star or KCUR pickup located. **NM DPS M101688 confirmed via direct fetch**: full legal name **Steven Abel Garcia**, status **"Other-Caution"** classification (specific NM DPS tier distinct from Endangered Missing / Silver Alert; worth case-file capture). **NEW substantive anonymous-source claims surfaced via Daily Mail Chris Melore origin chain** (verified through British Brief direct fetch + arutzshevatuzarapost Substack mirror): (1) **KCNSC ran an internal investigation of Garcia's work computers, emails, and files** "days after Garcia's disappearance … but nothing has been found" — if true, *de facto* confirms employment at the institutional-process level even without public statement; (2) **"That entire mission runs out of Kirtland Air Force Base. A big part of it, including the technology and the production of the technology that they use, is all built in Albuquerque"** — first explicit anonymous-source institutional bridge between Garcia's claimed role and the broader Kirtland-Sandia-Los Alamos ecosystem; (3) **"he literally just walked off into the desert with a firearm and a bottle of water and that was it"** — adds "bottle of water" pattern-of-life detail not in case file; (4) **"It's a little strange that these people just keep disappearing"** anonymous-source quote framing Garcia inside cluster. **"Single source" vs. "two anonymous sources" discrepancy flagged**: 0xTars X post 2026-04-19 (https://x.com/1O0001001101111/status/2044087779156734136) characterizes Daily Mail as relying on "two anonymous sources"; case file says single source. Original Daily Mail dailymail.co.uk URL still not directly indexed (same robots/paywall behavior as Eskridge sub-pass). **No new family statement, KCNSC denial, or NNSA statement in 30-day window.** No KOAT-TV or Albuquerque Journal coverage located (real local-press gap). No Burlison-specific Garcia attribution (Garcia is in cluster framing only, not singled out as Eskridge was). TikTok discoverability has surfaced "death of Steven Garcia 2025" as a discover-page query — public-perception data point. Reddit `site:reddit.com` search returned zero hits (same pattern as Eskridge). Substack: gunnerq3 (Apr 11), arutzshevatuzarapost (Apr 17), dataphenomenon (Apr 12) — all T6 Mulder-side; Boykin / Hobart silent on Garcia. **Critical evidentiary observation**: the Mulder side for Garcia is almost entirely sourced through one outlet (Daily Mail / Chris Melore) and its anonymous source(s) — fundamentally different evidentiary structure than Eskridge (which has Milburn + Reid + multiple corroborating sources). ~30 search queries, ~15 direct fetches, mixed success. Notable fetch failures: KRQE (403), NewsNation (403), Cybernews (403), Daily Mail direct (no indexed URL), MSN UK (shell only), X/0xTars (402), Sportskeeda (405), Trevor Thompson Facebook posts (not extractable), Albuquerque Today / nationaltoday.com (404 stale URL), KOAT searches negative. No edits to `cases/garcia.md`. Bundle feeds next session's drafted Update block.

## 2026-05-08 — Reza source-deepening sub-pass (Phase 6 depth, parallel agent)

Subagent fired for source-deepening on the Reza case (single agent, web-equipped, Opus 4.7 1M, read-only on `cases/reza.md`). Output: [logs/reza-source-deepening-2026-05-08.md](reza-source-deepening-2026-05-08.md). **Headline finding:** the Mondaloy patent custody chain is a 5-step institutional transit (Boeing → United Technologies Corporation → Pratt & Whitney Rocketdyne → Aerojet Rocketdyne → L3Harris) culminating in the 2026-01-09 announcement of L3Harris's $845M sale of Space Propulsion to AE Industrial Partners (60% majority, RS-25 excluded; Spaceflight Now T3) — currently uncaptured in `cases/reza.md`. **Patent status correction**: all three U.S. Mondaloy applications (US-20030053926-A1, US-20040208777-A1, US-20100266442-A1) were ABANDONED (2004-06-03, 2009-12-07, 2012-12-01 respectively); the family's *only* granted patent worldwide was Russian RU2301276C2 granted 2007-06-20 to United Technologies Corporation as assignee, invalidated 2012-09-18 for non-payment. Repo currently calls these "patent applications" without abandonment status. **Hardwick death-date correction**: repo says 2015; UNSW alumni profile, Dignity Memorial Dayton OH obituary, Wikipedia, Sentinel Briefing, and Fortean Winds all confirm **January 5, 2014** (born 1950-06-26, age 63, stage-four metastatic breast cancer). **Hardwick at LANL (1982)** per UNSW alumni profile is a documented institutional bridge to the LANL cluster (Casias / Chavez) not currently mapped. **Hardwick at AFRL Materials Directorate 2005-2012** overlaps McCasland's AFRL command 2011-2013 — supports the Mondaloy-via-AFRL connection at T2 level (UNSW alumni profile). **Three new T1 sources**: (1) Boeing media-room press release 2004-10-11 confirms HENAAC Luminary Award and gives Reza's title at award time as Boeing Associate Technical Fellow at Rocketdyne Canoga Park labs; (2) Aerojet Rocketdyne / GlobeNewswire press release 2016-09-06 documents first public Mondaloy 200™ rocket-engine test at Edwards AFB Test Stand 2A under HBTD program (named officials Joe Burnett, Eileen Drake, Maj Gen Tom Masiello AFRL commander); (3) LASD Special Bulletin 2025-06-25 mirrored at goldrushcam.com/sierrasuntimes — full LASD missing-person flyer text with contact numbers, last-seen specified as "6000 Foot Gate on Angeles Crest Highway" (slightly different phrasing from Solve the Case "6000ft Day Use Parking Lot"). **Insider corroboration of JPL title**: Allan Petre (NASA JPL aerospace engineer, X handle @astro_allan, LinkedIn `linkedin.com/in/allan-petre`) posted 2025-06-30 search appeal calling Reza "Director of the Materials Processing Group at NASA JPL" — strongest non-LASD source on the JPL directorship. **Comer/Burlison letter recipients confirmed**: Kash Patel (FBI), Chris Wright (DOE), Pete Hegseth (DoD/Department of War), Jared Isaacman (NASA), letter dated 2026-04-30, briefing requested by April 27. Letter explicitly names Reza and "flags a close professional tie" between Reza and McCasland. **Soft-404 confirmed**: solvethecase.org/case/2025-56/monica-reza loads page shell only, zero case fields — repo annotation is correct. **Wayback retrieval status: NEGATIVE** — agent-level block on web.archive.org for entire session; no Find-a-Grave 284387277 capture surfaced via any indexed source. Find-a-Grave direct fetch returns 403; "J.C." profile ID 50725353 not retrievable. **Daily Mail UK direct fetch blocked** at agent level; piece is published (Chris Melore byline, article-15721979) and quoted via londonmail.co.uk mirror. **2:30 PM Twin Peaks Saddle "anguish" report (NEW)** — websleuths/eispiraten forum reconstruction documents two hikers reporting "a female in anguish or despair (not calling for help)" at Twin Peaks Saddle ~2:30 PM June 22, 2025 — separate from and ~5 hours later than the morning 911 call about screaming. T7 only; not currently in `cases/reza.md`. **Subject A behavioral anomalies (T7)**: directional contradiction (told Reza north, insisted SAR search south); extensive post-incident phone use (Zoom, calls, video) without calling Reza; civilian Facebook group deleted after device-tampering theory posted. **No NamUs entry surfaced** for Reza despite federal-investigation status. **NTRS zero hits** for Monica Jacinto/Reza — consistent with process-engineer / patent-track rather than publishing-scientist career path. **JPL employee directory does not exist publicly** — no NASA-side independent JPL-directorship confirmation. **L3Harris 2023 10-K assigned $0 developed-technology asset value** to the Aerojet Rocketdyne acquisition's intangibles per Sentinel Briefing's reading (T7 reading T1 SEC). **Most operationally significant gap that did NOT close this session**: Wayback retrieval of memorial 284387277 — agent-level web.archive.org block prevents any direct retrieval; flag for user-side curl. ~35 search queries, ~40 direct fetches, mixed success. Notable systematic-block patterns: web.archive.org (total), x.com (402), facebook.com (mostly OK), lamag.com (403 systematic on Conlin pieces), newsnationnow.com (403 systematic), oversight.house.gov + burlison.house.gov (403), daily mail.co.uk (agent-level block). No edits to `cases/reza.md`. Bundle feeds next session's drafted Update block.

## 2026-05-08 — McCasland source-deepening sub-pass (Phase 6 depth, parallel agent)

Subagent fired for source-deepening on the McCasland case (single agent, web-equipped, Opus 4.7 1M, read-only on `cases/mccasland.md`). Output: [logs/mccasland-source-deepening-2026-05-08.md](mccasland-source-deepening-2026-05-08.md). **Headline finding**: the DeLonge–Podesta meeting that the case file currently treats as a single email (WikiLeaks emailid 3099) is actually documented across **at least seven distinct WikiLeaks emails** (IDs 2125, 2635, 5078, 9501, 14150, 51979, 3099), including a Google Calendar acceptance from Susan McCasland Wilkerson (susanmccw123@gmail.com) and personal scheduling-clarification emails from Neil McCasland (neilmcc79@gmail.com). Confirmed Jan 25, 2016 meeting attendees: DeLonge + Podesta + McCasland + Wilkerson + **Rob Weiss (Lockheed Martin Skunk Works EVP)** + **Maj Gen Michael Carey, retired (former 20th Air Force / ICBM force commander)** + Milia Fisher (Clinton campaign aide). DeLonge's "General McCasland" email (3099) was sent at 18:04 EST on Jan 25 — *after* the scheduled 12:30 EST meeting. **Second major finding**: the four Comer/Burlison letter PDFs (DoW, FBI, DOE, NASA — all dated April 20, 2026) are publicly accessible and McCasland is **named in the body of every letter**; the existing primary-source archive's 403 framing is no longer accurate. The **DoW letter additionally captures DoW's response of record**: "there are no active national security investigations of any reported missing person who was a current or a former DoW clearance holder and involved in special access programs." That single sentence is a Tier 1 negative-finding on McCasland-as-active-SAP-cleared-investigation. **Third major finding**: KOB-TV's coverage of the BCSO Monday press conference (Monica Logroño byline) reveals McCasland owned a **second home in Pagosa Springs, Colorado**, that BCSO searched, and that **the hiking boots and a light green button-up shirt were located there** — Lt Kyle Woods explicitly walked back the "items missing with him" framing: "We're not saying he left in them. They are just unaccounted for." Case file lines 86, 90, and 137 need correction. **Fourth: PhD year is 1989, not 1988** (Hertz Foundation T1 + DSpace MIT T1 both confirm); MIT dissertation handle https://dspace.mit.edu/handle/1721.1/14459, advisors are four (Vander Velde, von Flotow, Battin, Gai), not Battin alone. **Fifth: two new institutional affiliations** — Kirtland Partnership Committee board member (https://kpcnm.org/board/neil-mccasland/, still listed) and **DBE Consulting LLC** (founder/owner/president per KPC bio; registered 2021 per Sentinel Network public-records research). **Sixth: Riverside Research has scrubbed McCasland from public visibility** post-disappearance and has issued no public statement; ATA/BlueHalo also silent. **Seventh: Robin McCasland obituary** (mother, d. 2020) at French Funerals & Cremations adds family-network detail not in case file: full sister Beth McCasland (Burin WA) and half-sister Alyson Casey Ramesh (Skokie IL); Robin moved to Albuquerque in 2017 to be near Neil and Susan. **Quote-provenance hazard documented**: the IBTimes UK Reza–McCasland "close professional connection / advanced materials for reusable space vehicles and weapons" framing (Michael Toledo byline, 2026-04-06, no external citations) propagated up via N.Y. Post (Galvin, Hussain) into the **Comer/Burlison Congressional letters** without an independent T1/T2 substantiation chain. **Notable fetch failures**: af.mil official biography returns 403 to WebFetch and has **zero Wayback snapshots** — the foundational T1 source for half the case file's biographical claims is not directly archivable from this agent and needs next-session manual capture. NewsNation (~6 URLs), KRQE, DSpace bitstream, YouTube descriptions all variably failed. Bundle catalogs ~17 distinct search queries, ~25+ direct fetch operations, mixed success. No edits to `cases/mccasland.md`. Bundle feeds next session's drafted Update block.

## 2026-05-08 — Garcia source-deepening sub-pass (Phase 6 depth, parallel agent)

Subagent G fired in parallel for source-deepening on the Garcia case (single agent, web-equipped, Opus 4.7, read-only on `cases/garcia.md`). Output: [logs/garcia-source-deepening-2026-05-08.md](garcia-source-deepening-2026-05-08.md). **Naming question resolved**: NM DPS record M101688 confirms canonical "Steven Abel Garcia, DOB 08/30/1977"; Wikipedia "Missing scientists conspiracy theory" table lists short form "Steven Garcia"; both agree. No "Eddison Garcia" variant exists in any source — the orchestrator-prompt reference appears to be an error. **Headline finding**: KCNSC employment claim still rests on a single Daily Mail anonymous source (Chris Melore byline, 2026-04-11, original URL https://www.dailymail.co.uk/sciencetech/article-15722375/missing-nuclear-official-new-mexico-secrets.html), but three documented KCNSC outreach attempts (Daily Mail, Newsweek, KOB 4) with zero responses now establish institutional silence as a multiply-sourced fact. **Two new T3 local sources surfaced** uncited in case file: Santa Fe New Mexican / Cormac Dodd (2026-04-21) with first published unnamed-APD-spokesperson quotes ("no new developments" + "FBI has reached out"); and KOAT-TV / John Rupolo (2026-04-23, Wikipedia footnote 41) covering the Burlison foreign-adversary framing applied to Garcia. **NM DPS anomaly**: record header date 08/12/2025 precedes Last Seen date 08/28/2025 by 16 days — likely system-internal timestamp; needs appendix-file note. **Garcia is the only NM cluster case with no family voice** — anonymous Daily Mail source is the entire "person who knew Garcia" voice. Mulder-side is structurally thinner for Garcia than Eskridge or McCasland (no precursor statements, no leaked texts/audio/video, no documented UAP/antigravity adjacency). Bundle catalogs ~58 search/fetch operations, ~16 successful fetches, ~10 fetch failures (Daily Mail, KOAT, Wayback, NewsNation, Cybernews, Fox 8, The Hill, oversight.house.gov, burlison.house.gov, Fox 4 KC — most are agent-level blocks recoverable via curl). House Oversight Comer/Burlison letter names Garcia per SFNM attribution but direct verification deferred (oversight.house.gov 403 to this agent). No edits to `cases/garcia.md`. Bundle feeds next session's drafted Update block.

## 2026-05-08 — Editorial neutrality re-pass + BCSO PDF backfill

**What happened:**

Two-track session: (1) editorial neutrality re-pass on the dossier's most-read surfaces, per the four checkbox items in TODO-research.md "Editorial & framing"; (2) committed the user's manual BCSO press release PDF backfill that had been sitting in the working tree.

**Track 1 — Neutrality re-pass (commit `c8f1465`, pushed):**

- **Find-pass agent** (Explore, Sonnet 4.6, read-only): scanned `dossier.md`, `analysis/hypotheses.md`, `analysis/connection-analysis.md` for verdict-language phrases and Mulder/Scully imbalance. Returned ~22–25 distinct verdict-phrase instances concentrated in dossier abstract + executive summary + H1–H9 table; identified systematic Mulder-side imbalance on H4 (3 for / 5 against + inline editorial pre-grade), H6 (0 affirmative for-bullets), H7 (1 for, immediately undercut by source-credibility aside), H9 (0 affirmative for-bullets, all 4 bullets documented absence-of-evidence).
- **`dossier.md`:** Added project-purpose + AI-disclosure banner above abstract. Stripped verdict language from abstract paras 2–3 and from executive-summary headings/sentences. Reframed H1–H9 evaluation table from single "Assessment" verdict column to parallel "Evidence for" / "Evidence against" columns. Inline italic update markers on every reworded paragraph. Substantive cuts moved to a dated `## Update — 2026-05-08` block at file bottom (originals preserved).
- **`analysis/hypotheses.md`:** Restructured each H# writeup into parallel `### Evidence for` / `### Evidence against` subsections. Added `### Context (category-level)` subsection on H4 (state-actor precedent, foreign-collection priority), H5 (collection priority), H6 (AFRL/Wright-Patt UAP lineage), H7 (COINTELPRO precedent + SAP infrastructure), H9 (AFRL lineage + AARO). Dropped `**Current assessment:**` synthesis paragraphs from in-place; originals preserved in Update block. Mulder-side hardening on H6, H7, H9: added affirmative evidence-for bullets where the prior writeup contained only absence-of-evidence framing. Removed inline editorial pre-grade in H4 ("and the 'against' evidence is substantially stronger"). Tier-and-confidence tags `[T# – Confidence]` applied to named-figure attributions on both sides for evidentiary-standard parity (per `feedback_voice_register` 2026-05-08).
- **`analysis/connection-analysis.md`:** Replaced one verdict-style summary clause ("are within plausible base rates before controlling for other factors") with neutral framing of the unanswered actuarial question.
- **AARO inclusion** as category-level context (not case-specific bullet) per user-directed reframe — included in H6 and H9 Context subsections + dossier H1–H9 table H9 evidence-for cell. NDAA Section 1683 specificity dropped per "no new external links in this pass" hard rule; tagged `[T4 – Reported]` (Phase 1 backfills primary citation).

**Track 2 — BCSO PDF backfill (commit `b9cc239`, local only — NOT pushed):**

- User manually downloaded the BCSO press release PDF on 2026-05-08; PDF previously returned HTTP 403 to automated fetches and was tracked in known-unknowns + the appendix reconstruction note.
- Files committed: `appendices/primary-sources/mccasland/PressRelease3.12.2026.pdf` (1.07 MB, 2-page image-PDF), updated `bcso-press-release-2026-03-12.md` (local archive reference + image-based note), updated `cases/mccasland.md` (timeline entries link both BCSO source URL and reconstruction notes).
- The reconstructed text in the appendix is unchanged; the new commit only attaches the now-available primary PDF as canonical reference. OCR deferred to Phase 3.

**Memory honored this session:**

- `feedback_conclusion_neutrality` (2026-05-08 update) — explicit verdict phrases stripped; Evidence-for/against framing applied.
- `feedback_xfiles_posture` — Mulder-side hypotheses received affirmative evidence-for bullets; investigation ≠ endorsement.
- `feedback_voice_register` (2026-05-08, new) — forensic prose on both columns; tier-and-confidence parity carries the weighting; no narrativizing of Mulder bullets to balance Scully.
- `project_banner_required` — banner on `dossier.md` markdown surface (website surface in mattnoth-dev — separate session).
- `feedback_response_format` — tight in-thread proposals with concrete rewrite text, single-pass execution, no approve-token ceremony.

**Append-don't-overwrite discipline:**

- Top-of-file revision markers extended on all three touched files (existing Phase 1 markers were extended, not replaced).
- Inline italic `*(updated 2026-05-08 — see history)*` markers on every reworded paragraph.
- Substantive cuts (abstract paras 2–3, H1–H9 verdict cells, all 9 `**Current assessment:**` paragraphs) moved to dated Update blocks at bottom of each file. Originals preserved verbatim.

**Out of scope (deferred):**

- Case-file edits — Phase 6 depth pass.
- Phase 1 backfill of an AARO primary-source citation (the H9 Context bullet currently uses `[T4 – Reported]`; promoting to T1 needs a verified DoD/Congressional URL added to glossary and is Phase 1's job).
- Website-side banner — mattnoth-dev, separate session.

**Stop conditions met:**
- Find-pass agent returned with verdict-phrase inventory + balance table ✅
- Banner applied to `dossier.md` with revision marker ✅
- Abstract + executive-summary verdict language stripped (originals in Update block) ✅
- H1–H9 table reframed in `dossier.md` and `analysis/hypotheses.md` ✅
- Per-hypothesis writeups rebalanced and synthesis-closers removed ✅
- Top-of-file revision markers on all three files ✅
- Commit + push (push for `c8f1465` per session prompt's explicit authorization; `b9cc239` BCSO commit local-only per end-session skill default) ✅

**TODO updates owed (next session opportunity):**

The four checkbox items under "Editorial & framing" in `TODO-research.md` are now complete — should be checked off:
- Banner ✅
- Strip verdict language from abstract + exec summary ✅
- Reframe H1–H9 hypothesis-evaluation table ✅
- X-Files presentation layer for analysis pages ✅

## 2026-05-08 — Phase 1 cleanup commit (Tier 1–6 applied)

**What happened:**
- Applied Tiers 1 through 6 of [logs/audit-phase1-findings-2026-05-08.md](audit-phase1-findings-2026-05-08.md). Single-thread, mechanical edits — no new research, no editorial-voice work, no Tier 7/8 (deferred).
- **Pre-commit Wayback CDX re-run** (mandatory step). Re-checked the 4 truly-dead URLs against `web.archive.org/cdx/search/cdx`:
  - `lanl.gov/`: ✅ Wayback snapshot retrievable (2026-01-01, HTTP 200). Glossary URL swapped to Wayback equivalent + `url_note` field added explaining the swap.
  - `missingpersons.dps.state.nm.us` legacy: ❌ no Wayback (empty CDX response twice). Domain swap to `dps.nm.gov` per audit; new URL confirmed alive at HTTP 200.
  - `ipac.caltech.edu/people/staff/carl_grillmair`: ❌ no Wayback (empty CDX response). Audit-recommended Caltech memorial URL is alive (HTTP 200). The dead `ipac.caltech.edu/people/staff/...` URL is **not actually present in the codebase** — only the root `ipac.caltech.edu/` is cited; no edit needed.
  - `daytondailynews.com/.../DQHLHBMP2FCSXPNNJHG3PHC6IU/`: ⚠️ Internet Archive temporarily offline at lookup time; CDX queries returned 503/"Temporarily Offline" page. Proceeded with audit's annotate-as-dead plan; can be revisited in a later session if IA recovers a snapshot.
- **Pre-commit URL spot-check.** Per memory `feedback_link_verification`, sampled 4 URLs from the audit's verified-link table to confirm verification still holds: Karoline Leavitt Wikipedia ✅; Steven M. Greer Wikipedia ✅; To The Stars (company) Wikipedia ✅; energy.gov/person/chris-wright ✅. Audit's verified-link table trusted for bulk-apply.

**Edits applied (one commit):**
- **Tier 1 — categorical fixes:**
  - `data/glossary.json`: LANL URL → Wayback snapshot + `url_note`; JPL/MSFC/PSFC full-form ordering changed from `(NASA)`/`(MIT)` parenthetical to NASA/MIT prefix; added `USAF`, `C4ISR`, `IGIC` entries.
  - `appendices/foreign-coverage/russia.md`: RT and Pravda UK retagged Tier 7 → Tier 8.
  - `appendices/foreign-coverage/iran.md`: Tehran Times and Press TV retagged Tier 7 → Tier 8.
  - `appendices/primary-sources/casias/nm-missing-persons-database-entry.md`: legacy `dps.state.nm.us` URL swapped to `dps.nm.gov` equivalent.
  - `cases/chavez.md` line 12: `losalamosnm.gov/News-articles/...` URL swapped to `News-media/...` per server redirect.
  - `cases/mccasland.md` line 27: applied DeLonge template — Wikipedia link for Tom DeLonge + Wikipedia link for John Podesta + WikiLeaks emailid 3099 direct URL on first occurrence (local archive link retained as secondary).
- **Tier 2 — first-occurrence enrichment links:** Wikipedia + primary-source URLs added per audit's verified table for Kash Patel, Karoline Leavitt, James Comer, Eric Burlison (in `dossier.md`); Chris Wright + DOE staff page, Chris Swecker, Michio Kaku, Joseph Rodgers + CSIS Project on Nuclear Issues (in `analysis/foreign-intel-layer.md`); Burlison + Swecker + Steven Greer (in `analysis/hypotheses.md`); To The Stars (company) Wikipedia (in `cases/mccasland.md`); Michael Shellenberger Wikipedia (in `cases/eskridge.md`); Wikipedia links for each named expert in `appendices/named-expert-commentary/` (Coulthart, Elizondo, Greer, Wright, Swecker, Kaku).
- **Tier 3 — over-link removal:** `dossier.md` House Oversight Committee link kept on first use (line 11), removed at lines 17, 44, 109; FBI investigation Newsweek link kept on first use (line 11), removed at line 108. `cases/chavez.md` "LAPD" repeat-links absorbed into the Tier 5 rename. `cases/reza.md` LASD repeat — left in place (single text occurrence; over-link removal moot after Tier 5 path).
- **Tier 4 — acronym first-use expansion:** Per-file expansions (UAP, LANL, JPL, KCNSC, AFRL, SAPOC, USAF, NMSP, CSIS, NTI, BCSO) in `dossier.md`; SAPOC, DOD, OUSD(AT&L), AFRL, DOE, CSIS, NTI, MSS, GRU, SVR, IRGC, MOIS in `analysis/foreign-intel-layer.md`; CSIS, NTI, SAPOC, AFRL, IGIC in `analysis/hypotheses.md`; NamUs + NMSP in `casias.md`; NNSA + DEW in `chavez.md` and `eskridge.md`; APD + KCNSC + NNSA in `garcia.md`; NEOWISE + LASD in `grillmair.md`; DART in `hicks.md`; SBG-VSWIR + AMR + HIFI + COWVR + SWOT in `maiwald.md`; OUSD(AT&L) + SAPOC + AFRL + USAF + SAP + C4ISR in `mccasland.md`; NEMLEC in `thomas.md`; IPAC + KCNSC + PSFC + SBG-VSWIR + AMR + HIFI in `analysis/connection-analysis.md`.
- **Tier 5 — LAPD collision rename in `cases/chavez.md`:** Replaced every instance of the abbreviation `LAPD` with full-spelled "Los Alamos Police Department" or short "Los Alamos PD" throughout the file. Glossary `LAPD` = Los Angeles Police Department remains canonical. Inline source-link wrapping `[LAPD](losalamosnm.gov/...)` collapsed to bare "Los Alamos PD" everywhere except first use (line 12), which retains the URL with the News-media path fix.
- **Tier 6 — broken-link annotations:**
  - 1 dead URL annotated: Dayton Daily News article in `cases/mccasland.md` Secondary Sources.
  - 1 LANL URL handled via glossary `url_note` field (not visible inline; alternative annotation surface).
  - 1 NM legacy domain handled via swap (Tier 1) — no annotation needed.
  - 1 IPAC Grillmair URL not actually present in codebase — no edit needed.
  - 2 soft-404 URLs annotated: NamUs MP150628 in `cases/casias.md`; solvethecase.org/case/2025-56/monica-reza in `cases/reza.md` Tier 1 Sources table.
  - 32 bot-blocked URLs: convention applied selectively (BCSO press release in `dossier.md` line 110; Los Alamos PD county press release in `cases/chavez.md` Primary Sources). Full annotation across all 32 deferred — per audit's cross-cutting note, the convention is documented + applied to highest-visibility instances; remaining annotations can be added if a future reader-feedback signal indicates value.
- **Revision-marker convention applied** per SESSION-PLAN session-3 spec: top-of-file `*Last revised: 2026-05-08 — [see history]*` italic line on every touched markdown file (24 files). Inline `*(updated 2026-05-08 — see GitHub for details)*` markers placed on the prose passages with revisions (Tier-1 URL swaps, Tier 7→8 retag, LAPD rename); pure additions (acronym expansions on first use, enrichment links) carry no inline marker per the prompt's append-vs-revise convention.

**Out of scope this session (per prompt):**
- Tier 7 (foreign-source asymmetric language symmetry pass) — Phase 2 voice-audit territory.
- Tier 8 needs-human-judgment items: Daily Mail vs. Mirror US tier consistency; Primetimer Tier 4 → Tier 5 demote; Coffindaffer / Milburn / Rodgers / Roecker credentialing pattern; AARO `aaro.mil` manual verify; diagram-affiliation-string standardization (Phase 7); Tier 8 structural question (Phase 7).
- No new external research, news refresh, or case-file content additions.

**Outcome:** One commit applying Tiers 1–6 with revision markers; pushed to origin.

**Further work:**
- Phase 2 voice + neutrality + hypothesis-balance audit (single agent) — next session per SESSION-PLAN.
- Tier 7 symmetric-framing pass folds into Phase 2 review.
- Tier 8 needs-human-judgment items — discuss before committing.

## 2026-05-08 — Phase 1 cleanup audit (5 parallel read-only agents)

**What happened:**
- Five agents fired in parallel. All read-only on narrative + data files. No edits to research content. Output: [logs/audit-phase1-findings-2026-05-08.md](audit-phase1-findings-2026-05-08.md) — consolidated findings + ranked proposed-edits checklist for the next session's cleanup commit.
  - **Agent A (Sonnet, Explore):** Both-links sweep with verify-don't-trust on every proposed URL.
  - **Agent B (Sonnet, Explore):** Acronym audit (first-use expansion, glossary completeness, cross-file consistency, over-linking).
  - **Agent C (Sonnet, general-purpose, web):** Broken-links pass with Wayback availability check.
  - **Agent D (Opus, Explore):** Foreign-source bias audit against the existing tier assignments.
  - **Agent E (Sonnet, Explore):** Alias-resolver scan across glossary + diagram + case files.

**Source-tier-relevant findings (highest-value action items for next session):**

1. **Tier 7 → Tier 8 mislabeling for state-affiliated foreign press** (Agent D). README defines Tier 8 explicitly as "Foreign state-affiliated press." Tier 7 is "Independent commentary, Substack, YouTube, TikTok, podcasts, social media." Four state-funded outlets are currently mistagged Tier 7:
   - `appendices/foreign-coverage/russia.md:7` — RT (Russia Today): T7 → **T8**
   - `appendices/foreign-coverage/russia.md:14` — Pravda UK: T7 → **T8**
   - `appendices/foreign-coverage/iran.md:7` — Tehran Times: T7 → **T8**
   - `appendices/foreign-coverage/iran.md:15` — Press TV: T7 → **T8**
   - `appendices/foreign-coverage/china.md:7` — Global Times correctly tagged Tier 8 (proves the convention is known).
   - Categorical fix; no judgment call needed.

2. **Daily Mail (UK) ↔ Mirror US (UK) tier inconsistency** (Agent D). Both are UK national tabloids covering similar UAP-aggregation material. Daily Mail is Tier 4 in `cases/maiwald.md:67` (with "Tabloid" caveat); Mirror US is Tier 5 in `cases/eskridge.md:95`. Pick one and apply across the dossier — they cannot diverge on outlet basis. Counter-direction: **Primetimer (U.S.) at Tier 4** in `cases/eskridge.md:84` is structurally equivalent to Britannia Daily (UK Tier 5) and Northeast Live TV (India Tier 5); Primetimer should likely demote to Tier 5. The README's Tier 4 list is "CNN/CBS/ABC/NBC/Reuters/AP/WaPo/NYT" — Primetimer doesn't qualify.

3. **WION (India) Tier 3-4 hedge → flat Tier 4** (Agent D). Independent commercial international broadcaster, structurally analogous to Newsweek/NewsNation (both flat Tier 4 in this dossier). The hedge reads as origin-uncertainty, not editorial-standard difference.

4. **Asymmetric framing language in foreign-coverage appendices** (Agent D). Foreign outlets described in terms of editorial intent ("dressed up theorizing," "framing emphasized vulnerability," "implicitly portrays"); U.S. outlets described in forensic, content-only terms ("repeated the claim without attribution"). 4 specific examples in `russia.md:20-22`, `iran.md:26`, `iran.md:40`, `china.md:31`. Recommend symmetric language — describe behavior, not intent — across all appendices. **Cross-references Phase 2 voice audit; flagged here for Phase 2 inclusion.**

5. **Structural Tier-8 question (long-term, Phase 7).** Tier 8 itself is an origin-based tier — there is no parallel skeptical tier for U.S. state-adjacent or partisan outlets. In tension with the standing rule "National mainstream = Tier 4 regardless of country." Options: keep as-is, evaluate state-press articles on content (propaganda → T5/6, news-aggregation → T4), or add a parallel U.S. partisan tier. Defer to Phase 7 methodology discussion.

**Source-quality findings (broken-links pass, Agent C):**

- **174 unique URLs scanned. 107 alive.**
- **4 truly dead URLs** with no automated Wayback recovery (CDX API was down — re-run before commit):
  - `https://www.lanl.gov/` (entire domain dead — every path 404; cited in `data/glossary.json:6`)
  - `http://missingpersons.dps.state.nm.us/.../id=M100749` (legacy domain retired; replace with `dps.nm.gov` equivalent — confirmed alive at the new domain)
  - `https://www.ipac.caltech.edu/people/staff/carl_grillmair` (staff page removed after death; Caltech memorial URL alive as substitute)
  - `https://www.daytondailynews.com/.../DQHLHBMP2FCSXPNNJHG3PHC6IU/` (CMS migration broke URL; no archive recovered)
- **32 "403" results — most are alive in real browsers.** Confirmed alive via curl: oversight.house.gov press release + PDF, brookline.news Loureiro article, all 4 IBTimes UK articles. Bot-blocked but human-readable: legacy.com obits, NewsNation 8 URLs, ResearchGate, Hoodline, NTI staff, The Hill, Middlesex DA. Recommend keeping links + adding a `*(blocks automated checks; viewable in browser)*` footnote convention.
- **2 soft-404s** (status 200, content empty): `namus.nij.ojp.gov/missing-person-namus-mp150628` (Casias) and `solvethecase.org/case/2025-56/monica-reza` (Reza). Annotate as "record exists but content fields are blank as of 2026-05-08."
- **1 redirect** worth updating: `losalamosnm.gov/News-articles/Search-Continues-Anthony-Chavez` → `News-media/...` path rename (`cases/chavez.md:12`).

**Glossary integrity findings (Agents B + E):**

- 3 acronyms used in narrative but missing from `data/glossary.json`: `IGIC`, `USAF`, `C4ISR`.
- 7 institutional entities used across the dossier but missing entries: Sandia National Laboratories (mentioned in dossier + both analysis files + diagram), Kirtland AFB, Riverside Research, Institute for Exotic Science, HoloChron LLC, Aerojet Rocketdyne, Honeywell FM&T (KCNSC operator).
- 3 ordering inconsistencies between glossary and case-file convention: `JPL`/`MSFC`/`PSFC` glossary entries use `(NASA)`/`(MIT)` parenthetical; case files + diagram use NASA/MIT as prefix. Single glossary edit aligns.
- 1 cross-file expansion conflict: `LAPD` in `cases/chavez.md` is "Los Alamos Police Department"; glossary canonical is "Los Angeles Police Department." High-priority — collision risk in any reader's mind. Resolution: spell out "Los Alamos Police Department" in full and retire the `LAPD` abbreviation from `cases/chavez.md` entirely.

**Public-figure enrichment findings (Agent A — verified URL list):**

- Tom DeLonge — Wikipedia (`https://en.wikipedia.org/wiki/Tom_DeLonge`) ✓ + WikiLeaks email URL (`https://wikileaks.org/podesta-emails/emailid/3099`) ✓
- John Podesta, Karoline Leavitt, James Comer (note `_(politician)` disambiguator), Eric Burlison, Kash Patel, Chris Wright (DOE Sec.), Chris Swecker (stub), Michio Kaku, Ross Coulthart, Luis Elizondo, Steven M. Greer (note middle initial), Michael Shellenberger, AARO, To The Stars (use `_(company)` URL — not the `Academy_of_Arts_%26_Science` 404), Nuno Loureiro, Carl Grillmair — all Wikipedia URLs verified.
- 4 figures have **no Wikipedia article**: Jennifer Coffindaffer, Joseph Rodgers (CSIS — use CSIS PONI program URL instead), Scott Roecker (NTI staff page returns 403, manual confirmation needed), Franc Milburn. For these, the right enrichment is an institutional/about-page link or a credentials footnote, not a Wikipedia link.

**Acronym hygiene findings (Agent B):**

- 29 first-use violations across 13 files. Highest-density: `dossier.md` (12 acronyms first-appear bare), `analysis/foreign-intel-layer.md` (12), `cases/maiwald.md` (5), `cases/hicks.md` (4), `cases/mccasland.md` (4), `analysis/hypotheses.md` (4), `analysis/connection-analysis.md` (4).
- Per "new file = reset" rule, every file starts the link-and-expand counter from zero — so even acronyms expanded in another file need re-expansion on first use here.

**Quality flags surfaced for next session:**
1. Wayback CDX re-run for the 4 dead URLs (5 minutes; do before commit).
2. AARO `aaro.mil` URL — `.mil` domain didn't fetch automatically; verify manually before adding as primary source.
3. Daily Mail vs. Mirror US tier decision — judgment call needed; no clean categorical fix.
4. Primetimer Tier 4 → Tier 5 demote — confirm with user.
5. Diagram affiliation-string standardization (Agent E options a vs. b) — Phase 7 territory; do NOT change in cleanup commit.

**No commits made.** Findings only, per Phase 1 stop condition. Next session: SESSION-PLAN session 3 — tag baseline, review findings, single cleanup commit applying approved edits with revision markers.

---

## 2026-05-08 — Phase 6 triage + Phase 5 Eskridge bundle + news-refresh (3 parallel agents, read-only)

**What happened:**
- Three agents fired in parallel, all read-only on case files:
  - **Agent T (Sonnet, Explore):** Phase 6 hybrid triage of all 11 cases. Output: [logs/triage-2026-05-08.md](triage-2026-05-08.md). (Note: Explore agents lack Write tool; main session wrote the file from agent's returned content.)
  - **Agent E (Opus, general-purpose, web):** Multi-angle Eskridge research bundle, X-Files posture (Mulder + Scully equal rigor). Output: [logs/eskridge-research-bundle-2026-05-08.md](eskridge-research-bundle-2026-05-08.md). 352 lines.
  - **Agent N (Sonnet, general-purpose, web):** News-refresh on 5 TODO "Actionable now" items. Output: [logs/news-refresh-2026-05-08.md](news-refresh-2026-05-08.md). 149 lines.

**No case-file edits this session.** All bundles feed next-session writes with revision markers.

**Triage union pick (top 3 by leverage = weakness ∩ new-material density):** **mccasland, garcia, reza.**
- *mccasland* — 3rd weakest + 1st most-ongoing; FBI/Congress/BCSO all live; one document could shift the analytical frame.
- *garcia* — KCNSC employment claim sits on a single anonymous T6 source; APD silent; one verifiable fact would resolve.
- *reza* — 2nd most new-material density; 5 most-operationally-significant gap-markers (withheld cell-phone forensics, Find-a-Grave anomaly, 911 screaming report, companion identities).
- *Methodology flag:* loureiro ranks 2nd weakest (46) but it's a methodology artifact — its 28 R/A/S markers reflect exhaustive tiering discipline, not poor sourcing. Excluded from union picks.
- *Anomalies:* grillmair has zero T4+ tags (best-sourced case in the dataset); casias has only 1 T4+ tag yet 9 open questions (widest local-coverage / unknowns gap).

**Eskridge bundle headline findings:**
1. **Precursor statement found verbatim, two independent disclosure paths.** May 13, 2022 SMS to Franc Milburn (released by Milburn Apr 2026 to NewsNation/Daily Mail): *"If you see any report that I killed myself, I most definitely did not. If you see any report that I overdosed myself, I most definitely did not."* Parallel May 24, 2022 Signal-message tranche to Samuel Reid (Institute for Exotic Science co-founder + CEO of Geometric Energy Corp / SpaceX DOGE-1 mission), released by Reid Apr 2025 — a year before Milburn went public. [T4 cluster, Confirmed as published; underlying claim Reported]
2. **Federal investigation formally engaged.** White House (Press Sec. Karoline Leavitt, Apr 17, 2026) confirms FBI–WH joint review; House Oversight (Comer + Burlison) requested briefings from DOE/DoW/FBI/NASA. **Burlison publicly attributed Eskridge's symptoms to Havana Syndrome / directed-energy weapon** — a sitting congressman, T4. [T2/T4, Confirmed]
3. **Huntsville sub-cluster surfaced.** Joshua LeBlanc (29, NASA-MSFC DRACO nuclear thermal propulsion engineer, d. 2025-07-22, Walker County AL — fiery Tesla crash after 4-hour airport stop) directly paired with Eskridge in Newsweek's "Huntsville Mystery" (2026-04-24). Wikipedia's Missing-Scientists article also lists Ning Li (UAH, AC Gravity LLC, d. 2021) as a third Huntsville antigravity-research death. [T4, Confirmed as media event; connection Speculated]
4. **Richard Eskridge's NASA-Marshall research record is documented Tier 1 / Tier 2** — not speculative. NASA NTRS papers on inductive pulsed plasma thrusters, PTX, and PuFF (Pulsed Fission-Fusion) Engine. Places HoloChron's "gravity modification" framing inside a real propulsion lineage.
5. **Sam Reid / DOGE-1 / SpaceX commercial-aerospace tie** — direct from the Arab Tribune obituary (Reid memorialized Eskridge with a payload on DOGE-1). Not in current case file.
6. **Independent skeptic critique now sharp and on-record.** Coffindaffer (retired FBI, Newsweek): "no doubt" suicide; Institute for Exotic Science = "fringe science … not accredited or recognized." Hanania (UnHerd, 2026-04-20): only one peer-reviewed Eskridge paper (2009 bridge engineering); characterizes her as "a crank who committed suicide." Shermer (Skeptic, 2026-04-25): base-rate / patternicity framing. [T4/T6, Reported]

**Mulder/Scully balance (Agent E's call):** Mulder side has more publicly documented evidentiary depth this cycle but routes through Milburn or Reid — single-source-cluster fragility. Scully side genuinely thin on the public-records front (no released coroner / HPD docs). Imbalance flagged in the bundle rather than padded.

**News-refresh status:**
- *House Oversight briefing (April 27 deadline):* **Partial.** Only Department of War replied substantively ("no active national security investigations of any reported missing person who was a current or former clearance holder involved in special access programs"). FBI / NASA / DOE silent on record. Comer/Burlison signaled subpoenas remain possible; none confirmed as of 2026-05-08. oversight.house.gov press release still 403.
- *FBI investigation:* **Partial.** **Loureiro case formally closed by FBI + US Attorney (D. Mass.) on 2026-04-29 — Cláudio Manuel Neves Valente solely responsible, no nexus to terrorism.** Patel's broader "report in short order" not yet published. Material update for Loureiro case file (which Agent T's triage flagged as "fully resolved" — confirmed).
- *Daily Mail retry:* **Still nothing surfaced.** Site-blocked for direct fetch; 7 search queries returned no Daily Mail URLs. Wikipedia confirms Daily Mail covered the cluster but no specific article located.
- *BBC retry:* **Coverage CONFIRMED — was previously assumed absent.** Sheila Flynn byline, 2026-04-23, family-reaction angle. URL `https://www.bbc.com/news/articles/cwyw9rpdl4po`. Verified via Yahoo syndication and Google Translate mirror (BBC.com itself blocked for direct WebFetch). Notable: NYT, WaPo, Guardian, Le Monde, Spiegel, TASS, Xinhua silent.
- *T1 403-retry:* Both still 403. BCSO press release PDF and oversight.house.gov page unchanged.

**Quality flags surfaced for next session (no edits this session):**
1. **"Steven Garcia" vs. "Eddison Garcia" naming discrepancy.** Wikipedia's Missing-Scientists article uses "Steven Garcia" for the KCNSC contractor; case file uses "Eddison Garcia." Verify against original sources before next case-file edit.
2. **Wikipedia error on Eskridge police agency.** Wikipedia says the death was investigated by "Birmingham, Alabama police" — every other source places it in Huntsville (Madison County). Birmingham is in Jefferson County, ~100 miles south. Don't propagate.
3. **Sheila Flynn / Daily Mail / BBC overlap.** Muck Rack lists Flynn as a "Daily Mail U.S. Journalist"; her BBC byline on the missing-scientists piece suggests freelance overlap. The "Daily Mail original source" for Garcia may sit under her byline rather than a site search.
4. **Loureiro FBI closure (2026-04-29)** is a small material update for the Loureiro case file (currently "fully resolved" per triage; Update block worth adding).
5. **Several T4 outlets confirmed as having covered the cluster but not yet referenced in the dossier:** IBTimes UK (two articles), Axios, Forbes/Fortune, CBS News, Scientific American, PolitiFact, Rolling Stone, Snopes, Boston Globe.

**No commits made.** Bundles are internal logs / drafts — case-file rewrite happens its own session per the user's stop condition.

**Next session:**
- User picks 2–3 cases from union for Phase 6 depth pass (mccasland / garcia / reza recommended).
- Eskridge bundle review → drafted `## Update — 2026-05-08` block for `cases/eskridge.md` + revision markers.
- Loureiro Update block (FBI 2026-04-29 closure).
- Garcia name discrepancy resolution.

---

## 2026-05-06 — Session 1: Phase 0 decisions (planning only)

**What happened:**
- No searches, no source consultation, no narrative changes. Session was scoped to Phase 0 decision-making + plan refinement only.
- All 7 Phase 0 decisions in `SESSION-PLAN.md` resolved (table now reflects resolved values, not defaults).
- 4 new standing rules surfaced during the walkthrough and written to memory: enrichment-as-primary-value, verify-don't-trust on links, first-occurrence-per-file link discipline, archival scope not capped by current spec.

**Key research-relevant decisions:**
- **Worldwide-sweep language scope confirmed:** EN + RU + ZH + FR + DE + ES + JA + KO. Hebrew + Persian/Farsi held back for round 2.
- **Subjective-characterization pattern** identified as a recurring voice problem: when a family member, employer, or official spokesperson's framing of a contested fact is presented as neutral fact rather than as an attributed claim. Concrete example flagged: McCasland case → "his wife characterizes it as brief, unpaid consulting for fiction writing" reads as fact, but is one party's framing of a contested connection. Phase 2 voice audit (next research-touching session) explicitly scoped to find more instances.
- **Hybrid triage** for Phase 6 update pass — surface what's new across all 11 cases at the same time as ranking by source weakness, so depth targets are picked from the union (most-weak ∪ most-new), not weakness alone.
- **Path B schema extension threshold** = ≥2 cases, with reader-facing methodology note documenting each extension.
- **Acronym sweep** = general (first-use expansion + glossary completeness + cross-file consistency + over-linking flag), not specific.

**Further work:**
- Session 2: Phase 1 audit (5 parallel read-only agents). Until that runs, no new research findings, no source-tier changes, nothing for this log to capture.

## 2026-04-21 — Harness-integration conformance check (read-only)

**What happened:**
- Executed `drafts/prompt-harness-integration.md` Phases 1–3 (discovery, gap analysis, install plan).
- Harness classified as **Mature, conforming** — all three required artifacts present, adapter table matches, no conflicts.
- No filesystem changes made; `APPROVED` gate not reached because nothing needed doing.

## 2026-04-21 — Agent harness install (tailored)

**What happened:**
- Committed [INSTALL-PROMPT.md](../INSTALL-PROMPT.md) and [AGENT-HARNESS.md](../AGENT-HARNESS.md) — generic, portable agent-harness tooling.
- Installed a **tailored** harness variant in this repo instead of running the generic install. Rationale: this repo's knowledge already has a domain-native taxonomy (`cases/`, `analysis/`, `appendices/`, `logs/`); the generic layer model (`knowledge/`, `workflows/`, `extractions/`) would force renames without adding value.
- Created [NAVIGATION.md](../NAVIGATION.md) — intent-keyed routing table covering dossier, research content, methodology, open threads, agent operation.
- Created [.claude/commands/end-session.md](../.claude/commands/end-session.md) — session-close ritual with 8 steps: research-content capture, integrity artifacts (contradictions, known-unknowns, dossier sync), tier consistency, navigation, actionables reconciliation, mandatory research-log append, status/changelog, final report.
- Edited [CLAUDE.md](../CLAUDE.md) — added a "Session structure" section pointing at NAVIGATION.md, `/end-session`, and AGENT-HARNESS.md.
- Existing artifacts preserved and integrated: `logs/research-log.md` is the session ledger (this entry is the first dogfood), `TODO-research.md` is the actionables file.

**Key decisions:**
- No `progress.md` created — `logs/research-log.md` already plays that role.
- No `knowledge/`, `workflows/`, `extractions/` directories created — current structure is sufficient.
- Rotation threshold intentionally deferred: research-log is structured by prompt-run, not per-session entries. Split to `logs/research-log-prompt-NNN.md` when a run section grows unwieldy.
- INSTALL-PROMPT.md is kept in-repo (untracked → tracked) for future reuse, not because we ran the generic install here.

## 2026-04-20 — Bootstrap (prompt 000)

- Initialized repository structure.
- No research performed in this prompt; plumbing only.

## 2026-04-20 — Prompt 001 research begins

### Orchestration approach
- **Lead orchestrator** reads the full prompt, spawns sub-agents, enforces source discipline, merges outputs.
- **Case-research agents** — one per case, 11 total, run in parallel. Each writes `cases/{slug}.md` and populates `appendices/primary-sources/{slug}/`.
- **Primary-source hunter** — separate agent, runs in parallel with case agents, focuses exclusively on Tier 1 documents.
- **Foreign-coverage agent** — searches foreign press, runs in parallel.
- **Named-expert-commentary agent** — locates on-the-record expert statements, runs in parallel.
- **Cross-case analysis agent** — runs after case files are complete.
- **Diagram-and-timeline agent** — runs after analysis is complete.
- Orchestrator writes dossier abstract and executive summary **last**.

### Cases included (initial list from prompt)
1. Anthony "Tony" Chavez — LANL, missing May 2025
2. Melissa Casias — LANL, missing June 2025
3. Monica Jacinto Reza — NASA JPL, missing June 2025
4. Steven Garcia — govt contractor (disputed), missing Aug 2025
5. William Neil McCasland — retired USAF Maj Gen, missing Feb 2026
6. Carl Grillmair — Caltech/IPAC, shot Feb 2026 (suspect arrested)
7. Nuno Loureiro — MIT PSFC, shot Dec 2025 (suspect linked)
8. Michael David Hicks — JPL, died July 2023
9. Frank Maiwald — JPL, died July 2024
10. Jason Thomas — Novartis, missing Dec 2025 / found Mar 2026 (weaker fit)
11. Amy Eskridge — exotic science researcher, died June 2022 (weaker fit)

### Decisions
- All 11 cases from the prompt are included initially. Inclusion rationale will be documented per case.
- Additional cases may be added if discovered during research. Exclusions documented here.

### Chavez case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Anthony Chavez Los Alamos missing 2025" -- 10 results, strong coverage
2. WebSearch: "Tony Chavez LANL missing New Mexico" -- 10 results, overlapping with #1
3. WebSearch: ""Anthony Chavez" "Los Alamos" missing" -- 10 results, overlapping
4. WebSearch: "Anthony Chavez Los Alamos police department missing person update 2025" -- 10 results
5. WebSearch: ""Anthony Chavez" LANL retired role job title Los Alamos National Laboratory" -- 10 results, no job title found
6. WebSearch: "Los Alamos National Laboratory statement Anthony Chavez missing employee" -- 10 results, no LANL-specific statement found
7. WebSearch: "Anthony Chavez Los Alamos Silver Alert Pueblo Canyon search cadaver dogs" -- 10 results

#### Pages fetched
1. NM DPS missing person record (T1) -- successful, key details extracted
2. Los Alamos Reporter LAPD notice (T1 via T3) -- successful
3. Los Alamos Reporter social media concern article (T3) -- successful, Carl Buckland friend details
4. CBS News broader pattern article (T4) -- successful but minimal Chavez-specific detail
5. KOB.com article (T3) -- content truncated, limited value
6. Boomtown Los Alamos article (T3) -- paywalled, only metadata extracted
7. michaelrcronin.com article (T5) -- successful but limited new detail
8. LA Daily Post LAPD search update (T3) -- successful, Deputy Chief Rodriguez quote
9. losalamosnm.gov county page (T1) -- returned HTTP 403
10. NewsNation article (T4) -- returned HTTP 403

#### Key findings
- **Tier 1 sources identified:** NM DPS missing person database entry; LAPD official statements (via local media and county website). County website returned 403.
- **No LANL institutional statement found.** Only the broader NNSA acknowledgment applies.
- **No Silver Alert found** despite Chavez being 78 years old.
- **Specific LANL role unknown.** No source identifies job title, division, or clearance status. This is a significant gap for inclusion assessment.
- **Case number:** #2025-0254 (from Los Alamos Reporter)
- **DOB confirmed:** January 7, 1947 (NM DPS)

#### Contradictions identified
- Height/weight discrepancy between NM DPS (5'7", 145 lbs) and LAPD notice (5'6", 135 lbs)
- Race listed as "Unknown/Other" in NM DPS vs. "White male" in LAPD notice
- Last seen date: NM DPS says 05/08 (report date), local media says May 4 (actual last sighting)
- NM DPS case entry date of 01/13/2023 is anomalous

#### Gaps remaining
- Specific LANL role/title/division
- Security clearance status
- Whether Silver Alert was issued
- Surveillance footage findings
- Medical history
- Who reported him missing
- Federal review status specific to this case
- Explanation for NM DPS 2023 case entry date

#### Files written
- `cases/chavez.md` -- full case file
- `appendices/primary-sources/chavez/nm-dps-missing-person-record.md`
- `appendices/primary-sources/chavez/lapd-missing-person-notices.md`

### Casias case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Melissa Casias LANL missing 2025" -- 10 results, strong coverage
2. WebSearch: "Melissa Casias Taos County missing" -- 10 results, overlapping with #1
3. WebSearch: "Melissa Casias Los Alamos missing person" -- 10 results, additional national outlets
4. WebSearch: "Melissa Casias phones factory reset wiped LANL" -- 10 results, confirmed family-sourced claim
5. WebSearch: "New Mexico State Police Melissa Casias press release missing endangered" -- found NamUs listing MP150628
6. WebSearch: "site:nmsp.dps.nm.gov OR site:namus.nij.ojp.gov Melissa Casias" -- confirmed NamUs entry
7. WebSearch: "Melissa Casias niece Jazmin McMillen phones wiped" -- traced phone-reset claim to McMillen

#### Pages fetched
1. ABQ Journal (Aug 26, 2025) -- most detailed single source; full timeline, phone detail, blue truck lead
2. Santa Fe New Mexican (early July 2025) -- strong early reporting; phone detail, family quotes
3. Taos News (July 9, July 23, Sept 3, 2025) -- local coverage, paywalled/JS-rendered (partial extraction only)
4. CBS News (2026) -- national aggregation; McMillen quote on clearance level
5. KOB (nuclear ties article) -- partial extraction only
6. NBC Dateline -- 403 error
7. NamUs MP150628 -- JS-rendered, confirmed via metadata only
8. KRQE -- 403 error
9. KOB (family one month) -- JS-rendered, minimal extraction

#### Key findings
- **Factory-reset phone claim is FAMILY-SOURCED (niece Jazmin McMillen), NOT confirmed by NMSP publicly.** Tier 3 provenance (via local media), not Tier 1.
- McMillen told CBS: "Melissa was an administrative assistant and did not have high-level clearance" -- pushes back on high-clearance framing.
- McMillen also told CBS she has not "seen any evidence linking her to any of the other cases."
- NMSP spokesperson Wilson Silver confirmed "no updates" in August 2025; notably restrained public posture.
- No standalone NMSP press release was found online.
- No LANL or DOE statement was found.
- Taos News reported "family divided" on July 9 -- details not fully accessible.
- Mark Casias (husband) repeatedly noted as "unavailable for comment."
- NamUs case MP150628 confirmed.

#### Contradictions identified
- Clearance level: task brief says "security clearance"; niece says "did not have high-level clearance" (not necessarily contradictory -- admin staff typically hold Q clearance for facility access)
- "Forgot badge" narrative vs. husband's account of her going to another LANL location
- Family division reported but not elaborated

#### Gaps remaining
- No Tier 1 confirmation of phone factory reset
- Taos News articles largely inaccessible (JS-rendered or paywalled)
- No LANL or DOE public statement located
- No information on investigation progress after September 2025
- Family division details unclear
- Foreign coverage not searched
- Surveillance footage details (alone? distressed? others visible?)
- Backpack contents unknown
- Post office errand purpose unknown

#### Files written
- `cases/casias.md` -- full case file
- `appendices/primary-sources/casias/namus-mp150628.md`
- `appendices/primary-sources/casias/nmsp-statements.md`

### Grillmair case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Carl Grillmair Caltech shot 2026" -- 10 results, strong coverage across major outlets
2. WebSearch: "Carl Grillmair IPAC astrophysicist killed" -- 10 results, overlapping; found Caltech memorial, Wikipedia, Newsweek congressional article
3. WebSearch: "Grillmair Llano California murder" -- 10 results, strong local and national coverage
4. WebSearch: "Freddy Snyder arraignment Lancaster Grillmair murder 2026" -- 10 results; confirmed postponement to April 29
5. WebSearch: ""Carl Grillmair" LA County Board honors resolution" -- 10 results; found Supervisor Barger adjournment
6. WebSearch: ""Freddy Snyder" Llano criminal history trespassing Grillmair property" -- 10 results; found LA Times deep dive via Yahoo syndication
7. WebSearch: ""Carl Grillmair" "Los Angeles Times" Llano porch desert compound" -- 10 results
8. WebSearch: "Grillmair LASD press release homicide Llano February 2026" -- 10 results; no direct LASD .gov URL found

#### Pages fetched
1. ABC7 Los Angeles -- charges and timeline (T3), successful
2. Caltech official memorial (T1) -- successful, comprehensive biographical data
3. FOX 11 Los Angeles -- suspect prior arrest details (T3), successful
4. Wikipedia -- Carl Grillmair biography (T5), successful, useful for cross-referencing
5. Pasadena Now -- prior arrest and release details (T3), successful
6. MyNewsLA -- initial LASD report details (T3), successful
7. MyNewsLA -- arraignment postponement (T3), successful
8. Yahoo News (LA Times syndication) -- December trespassing deep dive (T3), successful; most detailed source on Snyder's criminal history
9. CBS Los Angeles -- initial shooting report (T3), successful
10. Caltech student newspaper (The California Tech) -- colleague quotes (T3), successful
11. KTLA -- 403 error
12. LA Mag -- 403 error

#### Key findings
- **Named suspect Freddy Snyder, 29, charged with murder, carjacking, and burglary.** Strong criminal case.
- **Pattern of escalating criminal behavior by Snyder:** trespassing with loaded rifle (Dec 20) -> attempted jail escape (Dec 21) -> released on OR (Dec 23) -> neighbor burglary (Dec 28) -> weapons charges dismissed (Feb 5) -> fatal shooting (Feb 16) -> carjacked own mother (Feb 16).
- **System failure:** Felony weapons charges dismissed less than two weeks before the murder, reportedly due to lack of prior record.
- **No known motive disclosed.** Detectives say they found no prior connection between the men beyond the December trespassing.
- **Grillmair's work was entirely unclassified civilian research:** exoplanets, stellar streams, near-Earth object surveying. No known security clearances.
- **Caltech memorial (T1) provided comprehensive career details.** 147 publications, NASA medal, nearly 30 years at IPAC.
- **LA County Board of Supervisors honored Grillmair on March 3, 2026 (T1).**
- **No direct LASD press release found on lasd.org.** All LE-sourced facts come through media relay.

#### Contradictions identified
- Date of death: Feb 16 (consensus/most sources) vs. Feb 17 or Feb 21 in some outlets
- Bail amount: $2M (CBS) vs. $3.175M (Fox 11, MyNewsLA, Pasadena Now)
- 911 caller identity not disclosed

#### Gaps remaining
- No motive publicly disclosed
- No direct LASD press release located (only media relays of LE information)
- Arraignment outcome unknown (scheduled for April 29, 2026)
- Snyder's mental health status and whether evaluation ordered
- Identity of 911 caller
- Whether firearm used in shooting forensically matches the rifle from December
- No court filings directly accessed (no public docket link found)
- LA Times deep investigation was accessible only through Yahoo syndication

#### Assessment
This case has the strongest non-conspiracy explanation of any in the cluster. A local man with an escalating pattern of criminal behavior, who had previously trespassed on Grillmair's property while armed, returned and killed him. The primary systemic question is why the justice system failed to hold Snyder after the December arrest. This case supports hypothesis H8 (independent events misgrouped) most strongly. It does not support H4, H5, or H7.

#### Files written
- `cases/grillmair.md` -- full case file
- `appendices/primary-sources/grillmair/caltech-memorial.md`
- `appendices/primary-sources/grillmair/la-county-bos-adjournment.md`
- `appendices/primary-sources/grillmair/lasd-initial-report.md`

### Reza case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Monica Jacinto Reza JPL missing 2025" -- 10 results, strong coverage across T3/T4/T7 sources
2. WebSearch: "Monica Reza NASA JPL Angeles National Forest missing" -- 10 results, overlapping; House Oversight and Newsweek results
3. WebSearch: "Monica Reza nickel superalloy inventor patent JPL" -- 10 results; patent records confirmed via Google Patents and Justia
4. WebSearch: ""Monica Jacinto" OR "Monica Reza" LASD sheriff missing person statement 2025" -- 10 results; KTLA, Crescenta Valley Weekly, Websleuths
5. WebSearch: ""Monica Jacinto" patent US20100266442 "burn-resistant" nickel alloy" -- 10 results; patent details confirmed
6. WebSearch: ""Monica Reza" OR "Monica Jacinto" "Find a Grave" death declared 2025" -- 10 results; Sentinel Briefing investigation
7. WebSearch: ""Monica Jacinto" JPL "materials processing" director Aerojet Rocketdyne career" -- 10 results; LinkedIn profile located (not fetched), career timeline
8. WebSearch: ""Monica Reza" cell phone forensic data Angeles National Forest search evidence 2025" -- 10 results; Sentinel phone gap article
9. WebSearch: "House Oversight Committee missing scientists investigation Monica Reza 2026" -- 10 results; Comer/Burlison press release, Fortune, Newsweek
10. WebSearch: "NASA JPL statement Monica Reza missing scientist 2025 2026" -- 10 results; no JPL-specific statement found
11. WebSearch: ""Monica Reza" 911 call screaming woman Mount Waterman June 2025" -- 10 results; Sentinel and Websleuths

#### Pages fetched
1. Wikipedia - Monica Jacinto (T5) -- successful, comprehensive biography with reliability caveats noted on page
2. FOX 11 Los Angeles (T3) -- successful, LASD lead agency confirmed, federal probe details
3. Solve the Case / LASD listing (T1) -- successful, full physical description, case numbers, detective names
4. Google Patents US-20100266442-A1 (T1) -- successful, full patent details, inventors, composition, applications
5. Crescenta Valley Weekly / Vienna statement (T1 via T3) -- successful, key LASD quotes
6. The Sentinel Briefing "Green Burial" (T7) -- successful, Find a Grave anomaly, search evidence details
7. Yahoo News / Men's Journal (T4) -- successful, companion details, running claim, career details
8. The Sentinel Briefing "Phone Gap" (T7) -- successful, cell phone forensics claim, 911 call
9. Justia Patents (T1) -- returned 403
10. KTLA (T3) -- returned 403
11. NewsNation (T4) -- returned 403
12. House Oversight press release (T1) -- returned 403

#### Key findings
- **Patent claims CONFIRMED.** Three US patent applications (2003, 2004, 2010) for "Burn-resistant and high tensile strength metal alloys" list Monica A. Jacinto and Dallis Ann Hardwick as co-inventors. Alloy known commercially as Mondaloy. Used in AR1 engine components. Patent assigned to individuals, not corporate entity.
- **JPL title partially verified.** LASD listing on Solve the Case states "Director of the Materials Processing Group at NASA JPL" (T1). No JPL directory or NASA statement independently confirms. Wikipedia repeats title with reliability caveats.
- **Prior career at Aerojet Rocketdyne confirmed** (37+ years, Technical Fellow rank). Also worked at Boeing (2004, Associate Technical Fellow).
- **LASD is lead agency.** Case NIC: M668487735. Classified as "at-risk missing person." Assigned to Homicide Bureau Missing Persons Unit.
- **Find a Grave anomaly documented.** Memorial created June 26, 2025, listing death date June 22, 2025, with "green burial" -- while search was still active. Memorial removed ~March 27, 2026, after media reporting.
- **Cell phone forensic data was obtained but not publicly released** (per since-removed Montrose SAR Facebook post).
- **911 call same morning** from Mt. Waterman area reported woman screaming. Not publicly connected to or excluded from case.
- **No NASA/JPL institutional statement found** specifically about Reza.
- **No family public statements found** beyond privacy request conveyed through LASD.
- **Federal investigation confirmed** via House Oversight Committee (Comer/Burlison) and White House.

#### Contradictions identified
1. Find a Grave memorial with death date and "green burial" created while search active; no death certificate or remains located
2. Cell phone data obtained but never released; SAR post about it removed
3. Minor title discrepancies across sources (Director of Materials Processing vs. Director of Materials Processing Group vs. Fellow at Rocketdyne -- likely sequential roles)

#### Gaps remaining
- No JPL organizational confirmation of title
- No NASA/JPL public statement about Reza
- Hiking companions not publicly identified
- Cell phone forensic results unknown
- Find a Grave creator "lillian" not identified
- Security clearance level unspecified
- No family public statements beyond privacy request
- Connection to McCasland (also missing) alleged but unconfirmed
- Dallis Hardwick (co-inventor, d. 2015) death circumstances not examined
- House Oversight press release content not accessible (403)

#### Files written
- `cases/reza.md` -- full case file
- `appendices/primary-sources/reza/lasd-missing-person-listing.md`
- `appendices/primary-sources/reza/lasd-vienna-statement-2025-07-03.md`
- `appendices/primary-sources/reza/patent-us20100266442a1.md`

### Hicks case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Michael David Hicks JPL died 2023" -- 10 results, strong coverage (DPS memorial, LPL memorial, Newsweek, oversight.house.gov)
2. WebSearch: "Michael Hicks JPL DART Dawn scientist obituary" -- 10 results, overlapping; found LPL news article, multiple 2026 pattern articles
3. WebSearch: "Michael Hicks JPL cause of death autopsy Los Angeles coroner" -- 10 results, mostly Michael Jackson results; no coroner-specific Hicks data
4. WebSearch: ""Michael Hicks" JPL Sunland California death 2023 family" -- 10 results; found Forest Lawn obituary
5. WebSearch: ""Michael Hicks" asteroid NEAT DART publications JPL" -- 10 results; no direct publication list, confirmed 80+ papers
6. WebSearch: "Comer Burlison missing scientists JPL Hicks Maiwald investigation" -- 10 results; confirmed Congressional inquiry
7. WebSearch: "White House FBI investigation dead missing scientists NASA JPL 2026" -- 10 results; confirmed federal review
8. WebSearch: "missing dead NASA scientists Global Times Russia China coverage Hicks Maiwald" -- 10 results; found Global Times article

#### Pages fetched
1. AAS DPS obituary (T1) -- 403 Forbidden; confirmed via search snippets
2. U of Arizona LPL memorial (T1) -- successful; PhD 1997, JPL 1998-2022, 80+ papers, missions listed
3. U of Arizona LPL news (T1) -- successful; dissertation title confirmed
4. Forest Lawn obituary (T1) -- successful; full biographical and family details, memorial service, al-anon donation request
5. Newsweek "List of dead or missing scientists" (T4) -- successful; "no record of an autopsy" claim; colleague Dr. Joe Masiero quote
6. Newsweek "Obituaries shed light" (T4) -- successful; described as "astronomer, artist and father"
7. Fox 11 LA (T3) -- successful; LA County connection, federal review confirmed
8. CBS News (T4) -- successful; skeptical perspectives from CSIS, NTI, former DOE official
9. Global Times (T8) -- successful; Chinese state media framing with conspiracy amplification

#### Key findings
- **Cause of death not disclosed in any source.** Not in obituary, not in professional memorials, not in media reporting.
- **No autopsy record found** per Newsweek reporting; not confirmed by LA County Medical Examiner on record.
- **Left JPL in 2022, died 2023.** One-year gap unexplained. Possible retirement, layoff (JPL had budget cuts), health, or other reasons.
- **Obituary requests donations to al-anon.org** -- Al-Anon is a support organization for families of people with alcohol use disorders. This may provide biographical context.
- **No NASA/JPL institutional statement found** regarding his death.
- **Colleague Dr. Joe Masiero on record** with mentoring characterization.
- **CBS News review found no links between any of the deaths** in the broader pattern.

#### Contradictions identified
- Employment end (2022) vs. death (2023) gap unexplained
- "No autopsy record found" may reflect incomplete records search rather than confirmed no autopsy
- Pattern claims by Congress/media vs. skepticism from security analysts

#### Gaps remaining
- Cause of death
- Whether autopsy was conducted (no on-record statement from LACME)
- Reason for leaving JPL in 2022
- Security clearance level (planetary science work may not require high clearances)
- Federal agency response to Comer/Burlison inquiry
- Full publication list

#### Files written
- `cases/hicks.md` -- full case file
- `appendices/primary-sources/hicks/source-index.md`

### Maiwald case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Frank Maiwald JPL died 2024" -- 10 results, strong coverage (Legacy.com obituary, MSN, Newsweek, The Hill)
2. WebSearch: "Frank Maiwald JPL researcher obituary" -- 10 results, overlapping; confirmed Legacy.com as sole obituary source
3. WebSearch: "Frank Maiwald JPL cause of death autopsy Los Angeles" -- 10 results; X/social media claim of no autopsy; LiveNOW from FOX coverage
4. WebSearch: "Frank Maiwald SBG-VSWIR instrument JPL publications research" -- 10 results; found IEEE, SPIE publications, Google Scholar profile
5. WebSearch: "Frank Maiwald JPL HIFI Herschel space observatory publications" -- 10 results; found ResearchGate, JPL repository, 3,400+ citations
6. WebSearch: ""Frank Maiwald" OR "Michael Hicks" JPL scientist security clearance classified" -- 10 results; no specific clearance info found

#### Pages fetched
1. Legacy.com obituary (T1) -- successful; full biographical and family details, JPL projects listed, no cause of death
2. Google Scholar profile (T1) -- partially successful; rendered as code, confirmed PhD Applied Physics
3. Newsweek "List of dead or missing scientists" (T4) -- successful; "no record of an autopsy" claim; principal investigator description
4. Newsweek "Obituaries shed light" (T4) -- successful; no new details beyond obituary
5. Fox 11 LA (T3) -- successful; LA County connection, federal review confirmed
6. CBS News (T4) -- successful; skeptical perspectives (same as Hicks research)
7. The Hill (T4) -- 403 Forbidden
8. Global Times (T8) -- successful (shared fetch with Hicks); Maiwald listed among 11 cases

#### Key findings
- **Cause of death not disclosed in any source.** Obituary simply states he "passed away."
- **No autopsy reportedly performed** per multiple media outlets; original basis for claim unclear (possibly records search).
- **NASA never commented publicly on Maiwald's death.** Only public record is Legacy.com obituary.
- **Active researcher at time of death:** Co-authored SPIE paper published May 2024, died July 4, 2024.
- **JPL Principal designation** -- an honor for "outstanding individual contributions," distinct from PI role.
- **June 2023 astrobiology breakthrough claim** -- media report he led research relevant to detecting life on icy moons ~13 months before death. Specific publication not identified.
- **German-born** -- immigration/citizenship status and clearance eligibility implications unreported.
- **3,400+ citations** across career; research spanned THz technology, microwave radiometry, and imaging spectrometry.
- **CBS News review found no links** between any of the deaths.

#### Contradictions identified
- "Principal researcher" vs. "principal investigator" conflated in media; JPL "Principal" is a specific honor
- "No autopsy performed" -- source of claim unclear; not confirmed on-record by LACME
- Employment start date approximate (~1999 from media; obituary does not specify)
- Pattern claims vs. security analyst skepticism

#### Gaps remaining
- Cause of death
- Whether autopsy was conducted (no on-record LACME statement)
- Security clearance level
- Specific June 2023 astrobiology publication
- NASA/JPL internal communications about his death
- Immigration/citizenship status
- Federal agency response to Comer/Burlison inquiry

#### Files written
- `cases/maiwald.md` -- full case file
- `appendices/primary-sources/maiwald/source-index.md`

### Garcia case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Steven Garcia Albuquerque missing 2025" -- 10 results; NM DPS record, Newsweek, CBS, Fox, KOB 4, NewsNation, Cybernews, BroBible, aggregators
2. WebSearch: "Steven Garcia Kansas City National Security Campus" -- 10 results; NewsNation (Lauren Conlin), Newsweek, British Brief, Cybernews
3. WebSearch: "Steven Garcia missing scientist government contractor" -- 10 results; CBS, Newsweek, NewsNation, Fox, Daily Wire
4. WebSearch: "Steven Garcia Albuquerque missing August 2025 APD police report property custodian" -- 10 results; no APD press release found
5. WebSearch: ""Steven Garcia" "Daily Mail" Kansas City National Security Campus missing Albuquerque" -- confirmed Daily Mail as origin of KCNSC claim via anonymous source
6. WebSearch: "Steven Garcia Albuquerque Silver Alert APD missing person 2025" -- no Silver Alert found; NM DPS record confirmed
7. WebSearch: "Steven Garcia Albuquerque police department missing person endangered August 28" -- no APD press release found
8. WebSearch: "dailymail.co.uk Steven Garcia Kansas City National Security Campus missing" -- Daily Mail article confirmed as origin but not directly fetchable
9. WebSearch: "Kansas City National Security Campus statement Steven Garcia missing employee" -- no KCNSC statement; NNSA general statement located
10. WebSearch: ""Steven Garcia" "Cattail Court" Albuquerque missing" -- address detail confirmed from anonymous source
11. WebSearch: "Lauren Conlin Steven Garcia NewsNation investigation reporter" -- Conlin covers case, appears to relay anonymous-source claims
12. WebSearch: ""Steven Garcia" found body update 2026 Albuquerque" -- no resolution; still missing
13. WebSearch: "site:krqe.com OR site:koat.com OR site:kob.com Steven Garcia" -- KOB 4 found; no KRQE/KOAT coverage
14. WebSearch: "Honeywell Kansas City National Security Campus statement missing scientists employees" -- NNSA general statement found
15. WebSearch: "Lauren Conlin Daily Mail Steven Garcia KCNSC nuclear exclusive reporter" -- confirmed DailyMail.com as origin outlet

#### Pages fetched
1. NM DPS Missing Persons record M101688 (T1) -- successful; key biographical data extracted
2. Newsweek "Missing government security man compared to Neil McCasland case" (T4) -- successful; noted Newsweek did not independently verify KCNSC employment
3. CBS News cluster overview (T4) -- successful; used "reportedly" for KCNSC claim
4. LiveNOW from FOX overview (T4) -- successful; cited "Fox News" for KCNSC claim
5. British Brief article (T5) -- successful; explicitly attributed KCNSC claim to anonymous source via Daily Mail
6. Newsweek FBI investigation overview (T4) -- successful; Garcia listed with no sourcing detail
7. Daily Wire article (T5) -- successful; cited Economic Times India, not independent
8. NewsNation Lauren Conlin segment (T4) -- returned 403
9. Cybernews article (T5) -- returned 403
10. Colorado Springs Gazette (T4) -- returned 403
11. BroBible article (T5) -- JS-heavy, no article body rendered

#### Key findings: KCNSC employment sourcing chain
**The entire KCNSC employment claim traces to a single anonymous source speaking to DailyMail.com (~April 12, 2026).** No outlet has published independent confirmation:
- **Daily Mail:** Original outlet; anonymous source described Garcia as property custodian at KCNSC with top clearance
- **Newsweek:** Explicitly stated it "has not independently verified his employment details"; reached out to KCNSC (no response documented)
- **CBS News:** Used "reportedly" without attribution
- **Fox News Digital:** Appears to have repeated the claim; LiveNOW from FOX cited Fox News as source
- **NewsNation:** Reporter Lauren Conlin discussed Garcia on air, appears to relay the anonymous source's characterizations
- **British Brief:** Explicitly cited "anonymous source revealed to the Daily Mail"
- **Daily Wire:** Cited Economic Times India
- **KCNSC/Honeywell FM&T:** No public statement confirming or denying
- **NNSA:** General statement acknowledging awareness of reports; did not name Garcia

#### Contradictions identified
1. APD "danger to himself" warning vs. anonymous source's "very stable person" characterization
2. Employment claim from anonymous source vs. complete absence of official confirmation

#### Gaps remaining
- Was Garcia actually employed at KCNSC? No official confirmation exists
- APD basis for "danger to himself" warning
- Identity and credibility of the anonymous source
- No APD press release or Silver Alert located
- No family statements found
- No FBI/federal review status specific to Garcia
- Investigation updates since August 2025
- No NamUs entry found

#### Files written
- `cases/garcia.md` -- full case file
- `appendices/primary-sources/garcia/nm-dps-missing-persons.md`
- `appendices/primary-sources/garcia/nnsa-statement.md`

### Loureiro case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. "Nuno Loureiro MIT shot 2025 Brookline" -- 10 results
2. "Nuno Loureiro MIT Plasma Science Fusion Center director" -- 10 results
3. "Brookline shooting December 2025 Brown University connection" -- 10 results
4. "Claudio Valente video confession storage unit motive Brown MIT shooting" -- 10 results
5. "Nuno Loureiro MIT fusion research defense Department of Energy SPARC" -- 10 results
6. "Norfolk County DA Brookline police Nuno Loureiro murder investigation" -- 10 results
7. "MIT Plasma Science Fusion Center Department of Defense DARPA funding contracts" -- 10 results
8. "Claudio Valente Instituto Superior Tecnico grudge Loureiro classmate motive 2026" -- 10 results
9. "Claudio Valente Brown University PhD dropout Portugal top student career failure resentment" -- 10 results
10. "Nuno Loureiro wife family Brookline apartment shot foyer 9 Gibbs Street" -- 10 results

#### Pages fetched (10 successful, 3 failed)
MIT obituary, Wikipedia Brown shooting, WBUR timeline, ABC News grudge article, NextBigFuture fusion work, Boston 25 confession transcript, Wikipedia Loureiro, MIT Statement, CBS Boston police reports. Failed: Brookline.News (429), NBC News (403), Boston Globe (paywall).

#### Key findings
- Named suspect with ballistics, DNA, fingerprints, surveillance, rental car records, and video confession
- Motive: academic resentment/grudge (law enforcement sources); Valente did not explicitly state motive
- Brown was primary target (planned ~3 years); Loureiro murder was personal secondary attack
- No evidence of defense/national security motive
- Strongest candidate for reclassification from the pattern

#### Files written
- `cases/loureiro.md`
- `appendices/primary-sources/loureiro/mit-obituary.md`
- `appendices/primary-sources/loureiro/mit-statement-20251219.md`
- `appendices/primary-sources/loureiro/doj-confession-transcript-summary.md`
- `appendices/primary-sources/loureiro/brown-shooting-wikipedia-summary.md`

### Foreign coverage research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Search strategy
Searched for coverage in Russia, China, Iran, Israel, UK, France, Germany, India, Japan, Australia, and Qatar. Used outlet-specific searches (RT, TASS, Xinhua, Global Times, Press TV, Tehran Times, BBC, Guardian, Le Monde, Der Spiegel, WION, NHK, Haaretz, SCMP, Al Jazeera, Daily Mail, LBC, IBTimes UK, UnHerd, Sky News, Telegraph, Times of India, NDTV, ABC Australia, Sydney Morning Herald, Jerusalem Post, Times of Israel, Japan Times). Searched in English.

#### Countries with confirmed coverage (files written)

1. **Russia** -- RT (2 articles), Pravda UK (1 commentary). State-affiliated. Sensationalist framing; implicit U.S.-dysfunction narrative. See `appendices/foreign-coverage/russia.md`.
2. **China** -- Global Times (1 article). State-affiliated. UFO conspiracy angle foregrounded; omitted China-as-suspect framing from U.S. lawmakers. See `appendices/foreign-coverage/china.md`.
3. **Iran** -- Tehran Times (1 op-ed), Press TV (1 article). State-affiliated. Tehran Times advanced unique "knowledge sequestration" theory. See `appendices/foreign-coverage/iran.md`.
4. **United Kingdom** -- LBC (1), IBTimes UK (1), UnHerd (1). Independent outlets. Widest editorial range: LBC sensationalist, UnHerd skeptical. See `appendices/foreign-coverage/united-kingdom.md`.
5. **India** -- WION (5+ articles/videos), Northeast Live TV (1). Independent. Highest volume of any foreign outlet. Original Mondaloy angle. See `appendices/foreign-coverage/india.md`.

#### Countries with no meaningful coverage found
France, Germany, Japan, Israel (mainstream), Australia, Qatar/Al Jazeera.

#### Files written
- `appendices/foreign-coverage/russia.md`
- `appendices/foreign-coverage/china.md`
- `appendices/foreign-coverage/iran.md`
- `appendices/foreign-coverage/united-kingdom.md`
- `appendices/foreign-coverage/india.md`

### Named expert commentary research

**Date:** 2026-04-20
**Researcher:** Named-expert-commentary sub-agent (Claude)

Searched for on-the-record statements from identifiable experts on the missing/dead U.S. defense scientists cluster. Created 10 individual profile files in `appendices/named-expert-commentary/`.

#### Experts documented (10 total)

**High credibility / Direct expertise:**
1. Chris Swecker (former FBI Asst. Director) -- Espionage hypothesis, conditional framing. File: `chris-swecker.md`
2. Joseph Rodgers (CSIS, Deputy Dir. Nuclear Issues) -- Skeptical of pattern. File: `joseph-rodgers-csis.md`
3. Scott Roecker (NTI, VP Nuclear Materials Security) -- Skeptical; scale argument. File: `scott-roecker-nti.md`
4. Jennifer Coffindaffer (retired FBI agent) -- Rejected conspiracy framing. File: `jennifer-coffindaffer.md`

**Official government (direct authority):**
5. Kash Patel (FBI Director) -- Confirmed investigation, no conclusions yet. File: `kash-patel.md`
6. Chris Wright (Energy Secretary) -- Confirmed DOE review, nothing alarming yet. File: `chris-wright-doe.md`

**Adjacent expertise / Media:**
7. Ross Coulthart (journalist, NewsNation) -- "Grave national security crisis." File: `ross-coulthart.md`
8. Michio Kaku (physicist, CCNY) -- "Cause for national concern." File: `michio-kaku.md`
9. Luis Elizondo (former AATIP director) -- Restrained; deferred to law enforcement. File: `luis-elizondo.md`

**Low credibility:**
10. Steven Greer (Disclosure Project founder) -- UAP criminal-org narrative. File: `steven-greer.md`

#### Key finding: Expert opinion is divided
- Espionage-concerned: Swecker, Coulthart, Kaku
- Skeptical: Rodgers (CSIS), Roecker (NTI), Coffindaffer
- Official no-conclusions: Patel, Wright
- UAP-narrative: Coulthart, Greer; Elizondo restrained

#### Files written
- `appendices/named-expert-commentary/ross-coulthart.md`
- `appendices/named-expert-commentary/chris-swecker.md`
- `appendices/named-expert-commentary/michio-kaku.md`
- `appendices/named-expert-commentary/joseph-rodgers-csis.md`
- `appendices/named-expert-commentary/scott-roecker-nti.md`
- `appendices/named-expert-commentary/jennifer-coffindaffer.md`
- `appendices/named-expert-commentary/luis-elizondo.md`
- `appendices/named-expert-commentary/steven-greer.md`
- `appendices/named-expert-commentary/kash-patel.md`
- `appendices/named-expert-commentary/chris-wright-doe.md`

### Thomas case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Jason Thomas Novartis missing Wakefield Massachusetts 2025" -- 10 results
2. WebSearch: "Jason Thomas Lake Quannapowitt body found March 2026 cause of death" -- 10 results
3. WebSearch: "Jason Thomas Novartis chemical biology cancer research background education" -- 10 results
4. WebSearch: ""Jason Thomas" Wakefield wife "Kristen Bartoli" missing December 2025" -- 10 results
5. WebSearch: "Jason Thomas Novartis obituary funeral Burlington Massachusetts 2026" -- 10 results
6. WebSearch: ""Jason Thomas" Wakefield medical examiner cause manner death 2026" -- 10 results
7. WebSearch: ""Jason Thomas" Wakefield police chief Skory search canine drone December 2025" -- 10 results

#### Pages fetched
1. Wakefield town website / DA Marian Ryan statement (T1) -- successful
2. Legacy.com obituary (T1) -- successful
3. Boston 25 News wife interview (T3) -- successful
4. NBC Dateline (T4) -- 403 Forbidden
5. Middlesex DA press release (T1) -- 403 Forbidden
6. Boston.com March 17 (T3) -- partial extraction

#### Key findings
- DA Marian Ryan: no foul play suspected (T1)
- Cause/manner of death not yet publicly released by Chief Medical Examiner
- Both parents died within ~90 minutes of each other, November 2025
- Left home without phone/wallet; last seen near railroad tracks
- Body found March 17, 2026 in Lake Quannapowitt after ice melted
- No connection to defense/aerospace/classified work; Novartis pharma cancer research
- Weakest fit in repository

#### Contradictions
- Age 45 vs 46 (birthday between disappearance and obituary)

#### Gaps
- Official cause/manner of death
- Whether lake was searched in December
- Mental health context

#### Files written
- `cases/thomas.md`
- `appendices/primary-sources/thomas/sources.md`

### Eskridge case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
1. WebSearch: "Amy Eskridge Institute Exotic Science died 2022 Huntsville" -- 10 results
2. WebSearch: "Amy Eskridge Huntsville Alabama death ruled suicide gunshot 2022" -- 10 results
3. WebSearch: "Amy Eskridge "Richard Eskridge" NASA engineer father HoloChron" -- 10 results
4. WebSearch: "Amy Eskridge obituary Huntsville Alabama 2022" -- 10 results
5. WebSearch: "Amy Eskridge father Richard "nothing suspicious" death daughter statement" -- 10 results
6. WebSearch: "Amy Eskridge "Franc Milburn" investigation Congress report antigravity" -- 10 results
7. WebSearch: "Amy Eskridge 2020 interview Jeremy Rys threats directed energy weapon burns" -- 10 results
8. WebSearch: "Amy Eskridge Huntsville police department investigation 2022 coroner report Madison County" -- 10 results

#### Pages fetched
1. Newsweek "Who is Amy Eskridge?" (T4) -- successful
2. The Arab Tribune obituary (T1) -- successful
3. Fox News "11th scientist death" (T4) -- successful
4. Yahoo News / Fox News syndication (T4) -- successful
5. IBTimes UK father's statement (T4) -- rendering failure
6. NewsNation father interview (T4) -- 403 Forbidden

#### Key findings
- Death confirmed June 11, 2022, age 34, Huntsville, AL (T1 obituary)
- Reported as self-inflicted gunshot wound; no police/coroner report publicly released
- Father Richard Eskridge dismissed conspiracy theories: "nothing suspicious" (T4)
- Father is retired NASA MSFC engineer (plasma physics, fusion); co-founded organizations with Amy
- 2020 interview: threat claims, DEW claims, harassment -- all self-reported, unverified
- Franc Milburn claims not suicide; reportedly submitted to Congress 2023 (no record found)
- Shellenberger testified "murdered by private aerospace company" (no evidence documented)
- No peer-reviewed antigravity experimental publications found
- 2022 death predates 2025-2026 cluster by three years

#### Contradictions
1. Father says "nothing suspicious" vs Milburn/Shellenberger allege murder
2. Suicide ruling widespread in media but no official documentation located
3. Threat claims specific but entirely self-reported

#### Gaps
- Official police/coroner report
- Whether police reports were filed about threats
- Milburn investigation details
- Congressional submission documentation
- Shellenberger testimony evidence basis
- Circumstances of gunshot

#### Files written
- `cases/eskridge.md`
- `appendices/primary-sources/eskridge/sources.md`

### McCasland case research

**Date:** 2026-04-20
**Researcher:** Sub-agent (Claude)

#### Searches performed
19 web searches conducted covering: disappearance details, military career (AFRL, SAPOC, NRO, GPS, Office of Special Projects), post-retirement career (ATA/BlueHalo, Riverside Research), DeLonge/UAP connection (WikiLeaks emails, wife's statements, congressional interest), search efforts (BCSO, FBI), 911 call details, and political affiliations.

#### Pages fetched (successful)
10 pages successfully fetched: Wikipedia biography (T5), Newsweek (3 articles, T4), ABC News (T4), Fox News (T4), CBS News (T4), WikiLeaks emailid/3099 (T1), ABQ Journal (T3), Newsweek "Who is McCasland" (T4). 8 pages returned 403 or failed rendering, including the BCSO press release PDF (T1) and House Oversight press release (T1).

#### Key findings
- Military career comprehensively documented: 34-year USAF career spanning classified satellite reconnaissance, GPS, AFRL command, NRO, SAPOC executive secretary.
- Disappeared Feb 27, 2026 between 11:10 AM and 12:04 PM. Left phone/glasses/wearables. Took boots/wallet/.38 revolver/backpack.
- Wife's 911 call: "I have some indication that he must have planned not to be found." Also relayed statement about not wanting to live with deteriorating brain/body.
- Mental fog confirmed but not dementia per wife and BCSO.
- DeLonge/UAP: WikiLeaks email documents DeLonge's claims; wife confirms brief unpaid consulting for fiction; denies Roswell knowledge. McCasland silent.
- BCSO: no evidence of foul play, no classified-work connection, no link to other cases.
- Still missing as of April 20, 2026. No sightings. USAF sweatshirt found 1.25 mi east, unconfirmed as his.

#### Assessment
Highest-profile case in cluster. Current evidence more consistent with voluntary departure driven by medical/psychological distress than foul play. Supports H1/H8, H2, tangentially H6 (weaker than publicly perceived). Does not currently support H4 or H7.

#### Files written
- `cases/mccasland.md`
- `appendices/primary-sources/mccasland/wikileaks-podesta-email-3099.md`
- `appendices/primary-sources/mccasland/bcso-press-release-2026-03-12.md`
- `appendices/primary-sources/mccasland/house-oversight-press-release.md`
- `appendices/primary-sources/mccasland/riverside-research-appointment.md`

## Reconcile survey (2026-04-21)

### What was committed (31 commits, a0ab7ef through 4d2d916)
- All 11 case files: `cases/{casias,chavez,eskridge,garcia,grillmair,hicks,loureiro,maiwald,mccasland,reza,thomas}.md`
- `dossier.md` (112 lines, with abstract, executive summary, case index)
- `analysis/connection-analysis.md` (166 lines)
- `analysis/foreign-intel-layer.md` (169 lines)
- `analysis/hypotheses.md` (308 lines)
- `appendices/primary-sources/` — 11 per-case subdirectories, plus 4 government-wide documents
- `appendices/foreign-coverage/` — 5 country files (china, india, iran, russia, united-kingdom)
- `appendices/named-expert-commentary/` — 10 expert files
- `logs/research-log.md` — fully populated research log
- Skeleton versions of `data/diagram-data.json` (5 lines), `data/timeline-data.json` (4 lines), `logs/contradictions.md` (20 lines), `logs/known-unknowns.md` (45 lines)
- `data/schema/diagram-schema.json`, `data/schema/timeline-schema.json`

### Uncommitted modified files (rate-limit artifacts)
- `data/diagram-data.json` — 831 lines, fully populated with 11 person nodes, 10 institution nodes, 6 location nodes, 6 program nodes, 44 edges, 3 layer definitions. Valid JSON.
- `data/timeline-data.json` — 436 lines, fully populated with 29 case events, 14 context events. Valid JSON.
- `logs/contradictions.md` — 101 lines, expanded from 20-line skeleton; 12 within-case + 4 cross-case contradictions documented.
- `logs/known-unknowns.md` — 156 lines, expanded from 45-line skeleton; 16 case-specific + 7 cross-case analytical gaps.
- `run-all.log` — 58 new lines of pipeline transcript (not a research artifact).

### Untracked files
- `prompt-reconcile.md` — reconciliation prompt (operational, not a pipeline artifact)
- `prompt-resume.md` — resume prompt (operational, not a pipeline artifact)
- `reconcile.log` — reconciliation log (operational)

### Missing artifacts
- `STATUS.md` — required by prompt-001 spec as a final deliverable. Never created.

### Directory health
- `pdf-output/` — empty (expected; prompt-002 produces PDFs)
- No empty directories under `appendices/primary-sources/` — all 11 cases have files
- `.gitignore` does not cover `run-all.log` or `reconcile.log`

### Assessment
All four uncommitted modified files are complete, well-formed, and consistent with the spec. None are truncated. The rate limit hit after these files were written but before they could be committed. They should be committed as-is.

## Reconcile summary (2026-04-21)

### Uncommitted files at start and how each was handled
- `data/diagram-data.json` — Complete, 831 lines. Committed as-is (7c891e4).
- `data/timeline-data.json` — Complete, 436 lines. Committed as-is (7c891e4).
- `logs/contradictions.md` — Complete, 101 lines. Committed as-is (7c891e4). Later updated to add missing Hicks/Maiwald entries (525f3a2).
- `logs/known-unknowns.md` — Complete, 156 lines. Committed as-is (7c891e4).
- `run-all.log` — Pipeline transcript. Added to .gitignore; left untracked (7c891e4).
- `prompt-reconcile.md` — Operational prompt file. Left untracked.
- `prompt-resume.md` — Operational prompt file. Left untracked.
- `reconcile.log` — Operational log. Added to .gitignore; left untracked.

### Audit gaps fixed
- Created `STATUS.md` (required by spec, never generated due to rate limit).
- Updated `CHANGELOG.md` with prompt-001 completion and reconcile entries.
- Fixed H4 assessment discrepancy: dossier.md table now matches hypotheses.md ("Weak support").
- Added 4 missing contradiction entries for Hicks and Maiwald to `logs/contradictions.md`.

### Deferred gaps (NEEDS_RESEARCH)
- Non-English foreign coverage not searched (documented in known-unknowns.md).
- Base-rate actuarial analysis not performed (documented in known-unknowns.md).

### Full audit
See `logs/audit-report.md` for the complete per-case and top-level artifact audit.

READY_FOR_PROMPT_002

## 2026-04-21 — Tier migration inventory (prompt-retag-tiers)

### Scope
Migrating all source tier references from the old 7-tier system to the new 8-tier system per `prompts/build/prompt-retag-tiers.md`.

### Files already migrated (new-system tags confirmed)
- `cases/casias.md` — T1, T3 tags ✓
- `cases/chavez.md` — T1, T3, T4, T5, T8 tags ✓
- `cases/eskridge.md` — T1, T4, T5 tags ✓
- `cases/garcia.md` — T1, T3, T6 tags ✓
- `cases/hicks.md` — T1, T3, T4 tags ✓
- `cases/maiwald.md` — T1, T3, T4 tags ✓
- `cases/reza.md` — T1, T3, T4, T5, T7 tags ✓
- `cases/thomas.md` — T1, T3, T4, T7 tags ✓
- `analysis/connection-analysis.md` — T1, T3, T4 tags ✓
- `analysis/hypotheses.md` — T3, T6 tags ✓
- `appendices/foreign-coverage/china.md` — Tier 3 for SCMP ✓ (geographic proximity to HK/China story)
- `appendices/primary-sources/*` — all T1 ✓

### Files needing migration

**`cases/grillmair.md`** — ~40 old T2 tags. All sources are local LA media (ABC7, Fox 11 LA, CBS LA, MyNewsLA, Pasadena Now, LA Times/Yahoo, Caltech student paper). All T2 → T3.

**`cases/mccasland.md`** — ~35 old T2 tags. Mix of national outlets (CNN, ABC News, Fox News, Newsweek, NewsNation → T4), local (ABQ Journal → T3), and aggregator (Wikipedia → T5).

**`cases/loureiro.md`** — ~20 old T2 tags. Mix of local (CBS Boston, WBUR, Boston 25 → T3), national (NBC News, PBS, ABC News → T4), and aggregator (Wikipedia, NextBigFuture → T5). Also: Max Planck condolence statement reclassified T2 → T1 (institutional primary source); CNN Portugal → T3 (geographic proximity to Portuguese story).

**`logs/research-log.md`** — ~60 old tags across all tiers:
- Old T7 (Global Times, 2 occurrences) → T8
- Old T6 (Sentinel Briefing, 2 occurrences) → T7
- Old T3 (Wikipedia, aggregators, ~6 occurrences) → T5
- Old T2 (~50 occurrences) → T3 or T4 per outlet

**`logs/contradictions.md`** — 10 remaining old T2 tags (lines 75, 85, 90, 95, 104, 105, 109, 110, 114, 119). All are national outlets (Newsweek, Fox News, CBS News, NewsNation) → T4.

**`logs/audit-checklist.md`** — 2 old-system references in example/description text.

### Ambiguities logged

1. **Max Planck Institute condolence statement (loureiro.md line 159):** Tagged old T2 (media) but is actually an institutional statement → reclassified as T1. Not a media outlet.
2. **CNN Portugal (loureiro.md line 158):** Portuguese outlet covering a case involving two Portuguese nationals. Geographic/cultural proximity to the story → classified as T3 (beat reporting), not T4.
3. **NextBigFuture (loureiro.md line 92):** Tech blog/aggregator, not original reporting → classified as T5 (aggregator), not T4.
4. **British Brief (research-log.md line 413):** Small UK news/commentary site → classified as T5 (aggregator/tertiary), not T4. Lacks the reporting capacity of listed T4 international outlets.
5. **Colorado Springs Gazette (research-log.md line 418):** Covers military beat broadly but has no geographic proximity to the Garcia case (Albuquerque) → classified as T4.
6. **Daily Wire (research-log.md line 415):** Cited Economic Times India, not independent reporting → classified as T5 (aggregator/tertiary).

## 2026-04-21 — Tier migration complete (prompt-retag-tiers)

### Summary

Migration from 7-tier to 8-tier source classification system complete.

**Tags updated by new tier:**
| New Tier | Count (approx.) | Migration path |
|----------|-----------------|----------------|
| T1 | 0 changed | Unchanged (1 reclassification: Max Planck condolence → T1) |
| T3 (local/beat) | ~45 | From old T2: local NM outlets, local LA outlets, local Boston outlets, CNN Portugal |
| T4 (national) | ~65 | From old T2: Newsweek, CBS News, CNN, ABC News, Fox News, NBC News, NewsNation, The Hill, Fortune, PBS, IBTimes UK, Daily Mail |
| T5 (aggregator) | ~10 | From old T3: Wikipedia, BroBible, Cybernews, michaelrcronin.com; from old T2: NextBigFuture, British Brief, Daily Wire |
| T7 (independent) | 2 | From old T6: Sentinel Briefing (2 articles) |
| T8 (foreign state) | 2 | From old T7: Global Times (2 entries) |

**Files modified (22 total):**
- `cases/grillmair.md`, `cases/mccasland.md`, `cases/loureiro.md`
- `analysis/foreign-intel-layer.md`
- `logs/research-log.md`, `logs/contradictions.md`, `logs/audit-checklist.md`, `logs/audit-report.md`
- `appendices/primary-sources/eskridge/sources.md`, `appendices/primary-sources/thomas/sources.md`
- `appendices/primary-sources/garcia/nnsa-statement.md`, `appendices/primary-sources/casias/nmsp-statements.md`
- `appendices/primary-sources/grillmair/lasd-initial-report.md`
- `appendices/primary-sources/loureiro/brown-shooting-wikipedia-summary.md`
- `appendices/primary-sources/mccasland/bcso-press-release-2026-03-12.md`, `appendices/primary-sources/mccasland/house-oversight-press-release.md`
- `TODO-research.md` (marked migration tasks complete)
- 8 case files already migrated in prior pass (casias, chavez, eskridge, garcia, hicks, maiwald, reza, thomas)

**Files NOT modified (per exclusion list):**
- `README.md`, `CLAUDE.md`, `prompts/research/README.md`, `prompts/build/prompt-retag-tiers.md`

**Prompt specification files left unchanged:**
- `prompts/build/prompt-000.md`, `prompts/build/prompt-001.md`, `prompts/research/prompt-deep-*.md` — These define the OLD tier system as originally written. Updating them would rewrite historical specifications. They describe the system under which prompt-001 research was conducted.

**Quality checks passed:**
- No file in `cases/`, `analysis/`, `appendices/`, or `logs/` contains old-system `(T2)` tags
- `(T2)` grep returns only the excluded migration prompt file
- No news outlet is tagged T2 — T2 is reserved for named expert commentary
- Total tier references approximately equal before and after (tags remapped, not added or removed)

## 2026-05-06 — Planning session: rebalance, scope, and execution plan

### Summary

Pure planning session — no research conducted, no dossier prose edited. Captured a substantial set of methodology corrections from the user and codified them as durable rules + a phased execution plan.

### Artifacts created or modified

- **`SESSION-PLAN.md`** (new) — comprehensive phased plan with standing rules, Phase 0 decisions, agent strategy per phase, next-session execution ladder, snapshot tooling spec, X-Files posture, multi-angle analysis, geographic/domain clustering analysis (Phase 9), pattern-recognition framing layer (Phase 8). Cross-references TODO-research.md and scratch.txt.
- **`scratch.txt`** (expanded) — open items unfolded from terse one-liners to actionable items with `→` prompt-back questions. New sections added for: scope correction (global default), Tom DeLonge resolution (researched, ready), Amy Eskridge precursor statement, precursor-statement pattern category, Huntsville hotbed analysis, antigravity / zero-gravity research domain, industry-insider voices on TikTok, multi-angle analysis as standing rule, X-Files investigation posture, TikTok transcripts achievable via Phase 3 tooling, self-host primary-source materials, broken links pass with Playwright integration.
- **`TODO-research.md`** (modified) — added Tooling section for snapshot pipeline (Playwright, yt-dlp + Whisper, snapshot-reddit); added Methodology section for Weirwood Network pattern adoption (Path B categorizer extension, alias resolver, Option C re-emission, mechanical-vs-prose split); cross-ref to SESSION-PLAN.md.

### Memory updates (durable across sessions)

Five memory entries created or updated under `~/.claude/projects/-Users-mnoth-source-research-missing-scientists/memory/`:

- **`feedback_source_trust.md`** (updated) — extended to specify national mainstream = Tier 4 *regardless of country*; foreign outlets must not be downweighted on origin alone.
- **`feedback_conclusion_neutrality.md`** (new) — surface human-instinct patterns (factory-reset phones, walking out together, missing belongings, precursor statements) without verdicting; don't assert "no connection."
- **`feedback_global_scope.md`** (new) — dossier scope is worldwide; existing 11 U.S. cases are historical artifact, not principled scope; no "foreign case" downgrade.
- **`feedback_multi_angle_analysis.md`** (new) — apply geographic / industry-insider / "weird" / asymmetry / domain lenses *before* settling on a framing; TikTok is primary insider venue in 2026.
- **`feedback_xfiles_posture.md`** (new) — Mulder-side hypotheses get same investigative rigor as Scully-side; investigation ≠ endorsement.

### Next session

Session 1 per SESSION-PLAN.md: walk through Phase 0's 7 decisions one at a time, then launch Phase 1's 5 parallel read-only audit agents (both-links sweep, acronym audit, broken-links pass, foreign-source bias audit, alias-resolver scan). Hold all edits until session 2.

A copy-paste kickoff message was provided to the user for use in a fresh Claude Code session.
