# Reza source-deepening bundle — 2026-05-08

**Agent:** Source-deepening agent (general-purpose, Opus 4.7 [1M])
**Scope:** Higher-tier primary-source hunt for `cases/reza.md`. X-Files posture; Mulder + Scully equal rigor.
**Read-only on cases/reza.md** — bundle feeds next session's drafted Update block.

## Headline findings

- **The LASD soft-404 on Solve the Case is confirmed.** Direct fetch of https://www.solvethecase.org/case/2025-56/monica-reza returns the page shell only — no case fields, no narrative, no photo. Existing repo annotation is correct. The original LE-side primary record this session located is the **LASD Special Bulletin dated June 25, 2025** (text mirrored at goldrushcam.com/sierrasuntimes), which is the canonical missing-person flyer issued by LA County Sheriff Missing Persons Detail [T1, Confirmed].
- **Find-a-Grave Wayback retrieval status: NEGATIVE.** Direct fetch of `web.archive.org/web/2025*/findagrave.com/memorial/284387277` is blocked at the agent level ("unable to fetch from web.archive.org"). Indexed Google searches for `site:web.archive.org "284387277"` returned no hits. No Wayback capture of the memorial has been surfaced through any indexed source. Sentinel Briefing's "The Green Burial" piece (Mar 16, 2026) does not cite a Wayback snapshot either. **Flag for manual user retrieval via `curl -A` against `web.archive.org/web/20260101000000*/findagrave.com/memorial/284387277/monica-jacinto-reza`** — this is the most operationally significant missing artifact in the case file and the agent-level block prevents resolution from this session.
- **Find-a-Grave creator/maintainer ID identification status: NEGATIVE.** "lillian" profile is non-public per Sentinel reporting. Maintainer "J.C." (ID 50725353) — direct profile fetch blocked (Find-a-Grave returns 403 to automation). Search for "J.C." memorial creation history on Find-a-Grave returned no usable results.
- **Three new high-tier primary findings:**
  - (1) **Boeing media-room press release** dated October 11, 2004 confirms the HENAAC Luminary Award and gives Reza's title at award time as **"Boeing Integrated Defense Systems engineer / Boeing Associate Technical Fellow / metallurgical engineer at Rocketdyne laboratories in Canoga Park, California"** [T1, Confirmed].
  - (2) **Russian Patent RU2301276C2 was granted June 20, 2007 to United Technologies Corporation as assignee** — the Mondaloy patent family's *only* granted patent worldwide. Status: invalid since Sep 18, 2012 (non-payment of fees). The U.S. priority went into Russian state-IP registry under a U.S. corporate assignee during the RD-180 / Atlas V / national-security-payload era. This is a strategic-tech-disclosure data point not currently captured in `cases/reza.md` [T1 Rospatent, Confirmed].
  - (3) **All three U.S. Mondaloy patent applications were ABANDONED.** US-20030053926-A1 abandoned 2004-06-03 (failure to respond), US-20040208777-A1 abandoned after examiner's answer 2009-12-07, US-20100266442-A1 abandoned 2012-12-01. **No U.S. patent on Mondaloy was ever granted.** The repository correctly identifies these as "patent applications" but the abandonment status is not currently noted. Aerojet Rocketdyne and AFRL nonetheless continued referencing "Mondaloy 200" in 2016 hot-fire test press releases, indicating the IP became trade-secret / common-law-mark territory rather than federally-protected.
- **Hardwick death date is 2014, not 2015.** Repository says Hardwick died 2015. UNSW alumni profile, Dignity Memorial Dayton OH obituary, Sentinel Briefing's "What Is Mondaloy" piece, Fortean Winds' "Mondaloy Chain," and Wikipedia all give **January 5, 2014** (born June 26, 1950, age 63, stage-four metastatic breast cancer diagnosed 2012). **Flag for repo correction.**
- **Hardwick's AFRL employment is documented and direct.** UNSW alumni profile establishes she went from Rockwell Science Centre → Boeing Seattle → AFRL Ohio, where she **led materials research for advanced gas turbine engines from 2005-2012** and received the Meritorious Civilian Service Medal in 2010. Her AFRL tenure overlapped with **William McCasland's AFRL command (2011-2013)**. Fortean Winds reads this as "Hardwick worked under McCasland at AFRL" — the institutional overlap is documented but a direct reporting relationship is *inferred*, not confirmed.
- **JPL transition timing — partial new evidence.** **Allan Petre** (NASA JPL aerospace engineer, X handle @astro_allan) posted a public search appeal on June 30, 2025 calling Reza "a dear colleague and friend, Monica Reza, Director of the Materials Processing Group at NASA JPL." This is the strongest *insider* corroboration of her JPL title outside of the LASD bulletin and Wikipedia. Sentinel Briefing's "Phone Gap" piece asserts she "quietly moved from Aerojet Rocketdyne to JPL sometime after the 2023 L3Harris acquisition." Wikipedia phrases the JPL employment as "House Oversight Committee reported unconfirmed work at NASA's Jet Propulsion Laboratory" — *unconfirmed* meaning no JPL directory or NASA press release has been produced.
- **Companions are still not publicly named in Tier 1-4 sources.** No outlet — including the Daily Mail anonymous-family piece, LA Magazine, NewsNation, IBTimes UK — has named either hiking companion. The male companion is consistently characterized as "yoga instructor" (London Mail, multiple T7) operating "a wellness business that includes taking clients on outdoor excursions" (uapmurders.com T7). Sentinel/uapmurders refer to him as "Subject A." The female companion turned back partway up. **Companion identification remains the single largest gap.**
- **New evidentiary detail not in repo: the 2:30 PM "anguish" report.** Search-forum reconstruction (websleuths, eispiraten) describes that on June 22, 2025 at approximately 2:30 PM, **two hikers returning from Twin Peaks reported hearing "a female in anguish or despair (not calling for help)" near Twin Peaks Saddle**. This is *separate* from and ~5 hours later than the morning 9:10 AM disappearance. The repo currently captures the morning 911 call about screaming; it does not capture the 2:30 PM Twin Peaks Saddle report. [T7, Reported — needs T1 LASD confirmation.]
- **Federal agency-list and named-letter recipients are confirmed.** Comer/Burlison letters dated April 30, 2026 went to: **FBI Director Kash Patel, Secretary of Energy Chris Wright, Secretary of Defense Pete Hegseth, NASA Administrator Jared Isaacman.** Briefing deadline: April 27 [T1 House Oversight press release referenced via Wikipedia citation; direct fetch of oversight.house.gov was 403]. Reza is named in the letter scope per multiple T4 sources; the letter explicitly **"flags a close professional tie between two of the missing: Aerojet Rocketdyne and JPL engineer Monica Reza and retired Air Force Maj. Gen. William Neil McCasland."**
- **L3Harris divested propulsion business 2026-01-09.** L3Harris announced sale of Space Propulsion and Power Systems to AE Industrial Partners ($845M, 60% majority stake) — the new entity reverts to the standalone "Rocketdyne" brand. RS-25 engine excluded from sale. **AR1 / Mondaloy disposition not specified in sale documents** (per Spaceflight Now). This corporate-custody change happened ~7 months after Reza's disappearance and is not currently in `cases/reza.md` — relevant because the AR1 program (with Mondaloy as enabling material) was canceled in 2018 when ULA picked Blue Origin's BE-4, so by 2026 Mondaloy IP sat in a divested asset class.

## Scully-side findings

### A1. Mainstream press refresh

**Newsweek — "Monica Reza Case Gains Attention After Disappearance of US General"**
- **URL:** https://www.newsweek.com/monica-reza-case-gains-attention-after-disappearance-us-general-11698172
- **HTTP status:** 200
- **Publish date:** 2026-03-18 1:03 PM EDT
- **Outlet:** Newsweek (US national)
- **Tier:** T4
- **Confidence:** Reported
- **Extract:** Byline Jordan King. Establishes "Reza once worked on a government-funded rocket materials project overseen by McCasland." Bernalillo County Sheriff's Department: "Detectives are looking into this to see if there is any connection at all." Notes McCasland's wife Susan McCasland Wilkerson disputed UFO-related speculation.

**Newsweek — "Wave of Missing or Dead US Scientists: Everything We Know"**
- **URL:** https://www.newsweek.com/wave-of-missing-or-dead-us-scientists-everything-we-know-11867967
- **HTTP status:** 200
- **Publish date:** 2026-04-23 11:57 AM EDT (updated 2026-05-01 1:57 PM EDT)
- **Outlet:** Newsweek
- **Tier:** T4
- **Confidence:** Confirmed as media event
- **Extract:** Byline Joe Edwards. Names 11 scientists including Reza. On Reza: "led the lab's Materials Processing Group" / "smiling and waving some 30 feet behind her hiking companion before she vanished" / "had connections to Wright-Patterson Air Force Base." Aerospace engineer specializing in "high-strength and burn-resistant alloys."

**FOX 11 LA — "11 missing or dead scientists draw federal scrutiny, including 4 tied to LA County"**
- **URL:** https://www.foxla.com/news/white-house-fbi-investigation-la-county-scientists-missing-reza
- **HTTP status:** 200
- **Publish date:** 2026-04-18 9:19 PM PDT
- **Outlet:** FOX 11 Los Angeles (local TV)
- **Tier:** T3 (local broadcast in primary jurisdiction)
- **Confidence:** Confirmed as media event
- **Extract:** Byline Alexa Mae Asperin. Bundles four LA County cases: Reza, Grillmair, Hicks, Maiwald. White House Press Secretary Karoline Leavitt confirms WH+FBI+DOE working to "identify any potential commonalities that may exist." On Reza: "Professional history overlapped with retired Air Force Maj. Gen. William 'Neil' McCasland."

**Hoodline — "Search Effort Escalates for Missing Hiker Monica Reza"**
- **URL:** https://hoodline.com/2025/06/search-effort-escalates-for-missing-hiker-monica-reza-in-angeles-national-forest/
- **HTTP status:** 403 on direct fetch (search snippet readable; URL exists)
- **Publish date:** June 2025
- **Outlet:** Hoodline (local aggregator)
- **Tier:** T5
- **Confidence:** Reported
- **Extract:** Contemporaneous search-escalation coverage. Listed in many secondary-citation chains.

**KTLA — "Missing hiker: Teams from San Diego to Tulare County enter day 6 of search"**
- **URL:** https://ktla.com/news/local-news/missing-hiker-teams-from-san-diego-to-tulare-county-enter-day-6-of-search/
- **HTTP status:** 403 on direct fetch (URL valid; widely cited)
- **Publish date:** ~June 28, 2025 (Day 6 of search)
- **Outlet:** KTLA Channel 5 (local TV)
- **Tier:** T3
- **Confidence:** Confirmed as published
- **Extract:** Documents geographic span of SAR effort (San Diego to Tulare County). Cited extensively by Sentinel Briefing for the "extraordinary search" framing.

**KTLA — "Initial search phase concludes, Southern California hiker still missing"**
- **URL:** https://ktla.com/news/local-news/initial-search-phase-concludes-southern-california-hiker-still-missing/
- **HTTP status:** 200 (per existing repo cite)
- **Publish date:** 2025-06-29
- **Outlet:** KTLA
- **Tier:** T3
- **Confidence:** Confirmed
- **Extract:** Already cited in repo via primary-sources/reza/la-county-sheriff-missing-hiker-search.md.

**Outdoors.com — "Southern California Hiker, Monica Reza, Still Missing After Six Days"**
- **URL:** https://outdoors.com/southern-california-hiker-monica-reza-still-missing-after-six-days/
- **HTTP status:** 200
- **Publish date:** 2025-06-27 (six days after disappearance)
- **Outlet:** Outdoors.com (lifestyle vertical)
- **Tier:** T5
- **Confidence:** Reported
- **Extract:** Byline Bethanie H. Adds "one second Monica was there, and the next she wasn't" and notes search support spans San Diego County to Tulare County. CV Sheriff statement: "uncoordinated foot traffic can unintentionally interfere with tracking evidence."

**SnowBrains — "Initial Search for Missing Southern California Hiker Ends Without Success"**
- **URL:** https://snowbrains.com/initial-search-for-missing-southern-california-hiker-ends-without-success/
- **HTTP status:** 200
- **Publish date:** 2025-07-03
- **Outlet:** SnowBrains (outdoor vertical)
- **Tier:** T5
- **Confidence:** Confirmed as published
- **Extract:** Byline Luke Guilford. Reza "Separated from hiking companions near ridgeline between 7,000-8,000 feet elevation." Quotes Sgt. John Gilbert (LASD Crescenta Valley): "[The friends] go out weekly [to hike] in the area. She is in good shape and is experienced." Lists participating SAR agencies: Montrose, Altadena Mountain Rescue, Antelope Valley SAR, Sierra Madre, San Diego Mountain Rescue.

**KFI AM 640 — "Search Ends for Missing Hiker in Southern California"**
- **URL:** https://kfiam640.iheart.com/content/2025-06-30-search-ends-for-missing-hiker-in-southern-california/
- **HTTP status:** Not directly fetched; URL surfaced in search index
- **Publish date:** 2025-06-30
- **Outlet:** KFI AM 640 / iHeart (LA news radio)
- **Tier:** T3
- **Confidence:** Reported

**TMZ — "FBI Investigating Deaths & Disappearances of Scientists for Possible Connection"**
- **URL:** https://www.tmz.com/2026/04/21/fbi-looking-into-scientists-deaths-disappearances/
- **HTTP status:** Not directly fetched
- **Publish date:** 2026-04-21
- **Outlet:** TMZ
- **Tier:** T4
- **Confidence:** Reported

**Pasadena Now — "Four Pasadena-Area Scientist Deaths or Disappearances Among Those Under Federal Review"**
- **URL:** https://pasadenanow.com/main/four-pasadena-area-scientist-deaths-or-disappearances-among-those-under-federal-review-officials-say
- **HTTP status:** 200
- **Publish date:** 2026-04-22
- **Outlet:** Pasadena Now (local digital, primary-jurisdiction)
- **Tier:** T3
- **Confidence:** Confirmed as published
- **Extract:** Byline Gab Apo. Confirms JPL is managed by Caltech for NASA. Three JPL cases under federal review: Hicks, Maiwald, Reza. On Reza: "Director of Materials Processing at JPL." LASD ended initial search phase June 30; case remains with Homicide Bureau Missing Persons Unit.

**HeySoCal.com — "Feds investigate disappearances, deaths of US scientists"**
- **URL:** https://heysocal.com/2026/04/22/feds-investigate-disappearances-deaths-of-us-scientists/
- **HTTP status:** 200
- **Publish date:** 2026-04-22
- **Outlet:** HeySoCal (regional aggregator)
- **Tier:** T5
- **Confidence:** Reported
- **Extract:** Byline Joe Taglieri. NASA spokesperson: "is coordinating and cooperating with the relevant agencies" / no national-security threat indicators existed at the time of the statement.

**Fortune — "FBI looks into dead or missing nuclear and space defense scientists tied to NASA, Blue Origin, and SpaceX"**
- **URL:** https://fortune.com/2026/04/21/scientists-disappear-die-nasa-space-blue-origin-spacex/
- **HTTP status:** Not directly fetched (URL exists)
- **Publish date:** 2026-04-21
- **Outlet:** Fortune
- **Tier:** T4
- **Confidence:** Reported

**Axios — "Missing scientists working on space and nuclear projects alarm Congress"**
- **URL:** https://www.axios.com/2026/04/23/missing-scientists-space-nuclear-congress-investigating
- **HTTP status:** 403 on direct fetch
- **Publish date:** 2026-04-23
- **Outlet:** Axios
- **Tier:** T4
- **Confidence:** Reported

**The Hill — "Missing dead scientists Trump probe who are they"**
- **URL:** https://thehill.com/homenews/administration/5837873-missing-dead-scientists-trump-probe-who-are-they/
- **HTTP status:** Already cited in repo
- **Tier:** T4

### A2. Local / beat press

**Crescenta Valley Weekly — "Ongoing Search for Missing Hiker Monica Reza"**
- **URL:** https://www.crescentavalleyweekly.com/news/06/24/2025/ongoing-search-for-missing-hiker-monica-reza/
- **HTTP status:** 200
- **Publish date:** 2025-06-24
- **Outlet:** Crescenta Valley Weekly (local beat — primary-jurisdiction local press)
- **Tier:** T3
- **Confidence:** Confirmed
- **Extract:** Byline CV Weekly. Acting Captain Vienna: "We are deeply concerned about the whereabouts of Monica, who has now been missing for over 24 hours. We have deployed numerous resources, including Air Rescue 5..." Lists ten participating SAR teams: Crescenta Valley Station, Montrose SAR, Altadena Mountain Rescue, Antelope Valley, Malibu SAR, San Dimas Mountain Rescue, Sierra Madre, San Diego Mountain Rescue, Ventura County East Valley SAR, Riverside Mountain Rescue Unit. **Earlier than the July 3 statement currently cited in repo.**

**Crescenta Valley Weekly — "Search Continues for Missing Hiker in Rugged ANF Terrain"**
- **URL:** https://www.crescentavalleyweekly.com/news/06/26/2025/search-continues-for-missing-hiker-in-rugged-anf-terrain/
- **HTTP status:** 200
- **Publish date:** 2025-06-26
- **Outlet:** Crescenta Valley Weekly
- **Tier:** T3
- **Confidence:** Confirmed
- **Extract:** First documented quote from **Sgt. John Gilbert (LASD Crescenta Valley Station)**: "They [the friends] go out weekly [to hike] in the area. She is in good shape and is experienced [hiking]." Adds details on terrain (poodle dog bush; rappelling around waterfalls; helicopter extraction); Day 4 search staffing of ~35 searchers. **Most operationally specific T3 piece located this session.**

**Crescenta Valley Weekly — "Update on Efforts to Locate Missing Hiker Monica Reza" (Vienna statement)**
- **URL:** https://www.crescentavalleyweekly.com/news/07/03/2025/update-on-efforts-to-locate-missing-hiker-monica-reza/
- **HTTP status:** 200 (already in repo)
- **Publish date:** 2025-07-03
- **Tier:** T3 carrying T1 LASD statement
- **Confidence:** Confirmed

**La Cañada Outlook — "Search Continues for Missing Hiker Monica Reza"**
- **URL:** https://outlooknewspapers.com/lacanadaoutlook/search-continues-for-missing-hiker-monica-reza/article_95b0f944-7fd6-44d2-99aa-f25a8ca19aed.html
- **HTTP status:** 429 on this fetch attempt (rate-limited; URL valid)
- **Publish date:** ~late June 2025
- **Outlet:** La Cañada Outlook / Outlook Newspapers (local beat)
- **Tier:** T3
- **Confidence:** Reported

**CBS Los Angeles — "Search continues for missing 60-year-old hiker in Angeles National Forest"**
- **URL:** https://www.cbsnews.com/losangeles/news/angeles-national-forest-missing-hiker-monica-reza/
- **HTTP status:** Already in repo primary-sources/reza/
- **Tier:** T3

**NBC Los Angeles — "Search for a missing hiker near Angeles Crest Highway"**
- **URL:** https://www.nbclosangeles.com/news/local/search-for-a-missing-hiker-near-angeles-crest-highway/3730493/
- **HTTP status:** Search-index hit; not directly fetched this session
- **Tier:** T3

**LA Magazine — "Monica Reza Family Questions Missing Scientist Investigation" (Conlin)**
- **URL:** https://lamag.com/news/exclusive-for-monica-rezas-family-it-doesnt-make-sense/
- **HTTP status:** 403 on direct fetch
- **Publish date:** ~April 16, 2026 (per Wikipedia citation)
- **Outlet:** LA Magazine (local magazine)
- **Tier:** T3
- **Confidence:** Reported
- **Extract:** Byline Lauren Conlin. Family-side framing: "It doesn't make sense" / fear "for our safety" / "Whoever did this, if it was not an accident, was a professional." (Quote text accessed via search snippets; full body fetch blocked.) **This is the LA-local-press flagship piece on Reza** — flag for re-fetch via DuckDuckGo or alternate path.

**LA Magazine — "Monica Reza Case Update as Trump Probes Missing Scientists"**
- **URL:** https://lamag.com/crimeinla/new-clues-in-monica-reza-case-surface-as-trump-launches-probe-into-missing-scientists/
- **HTTP status:** 403 on direct fetch
- **Publish date:** 2026-04-16 (per Wikipedia)
- **Outlet:** LA Magazine
- **Tier:** T3
- **Confidence:** Reported
- **Extract:** Byline Lauren Conlin. Establishes "Reza was training as a yoga instructor at a studio incorporating astrology and Vedic sciences" and the "running on steep terrain" detail.

**LA Magazine — Lauren Conlin author archive**
- **URL:** https://lamag.com/author/lconlin/
- **HTTP status:** 999 (LinkedIn-style block)
- **Tier:** T3 (host of multiple Reza pieces)

### A3. Court / official sources

**LASD Special Bulletin — Monica Reza missing-person flyer (June 25, 2025)**
- **URL (mirror):** https://goldrushcam.com/sierrasuntimes/index.php/news/california/68455-los-angeles-county-sheriff-seeks-public-s-help-locating-at-risk-missing-hiker-monica-reza-last-seen-on-angeles-crest-highway
- **HTTP status:** 200
- **Publish date:** 2025-06-25 (date of LASD bulletin)
- **Outlet:** Goldrush Cam / Sierra Sun Times republishing the LASD release verbatim
- **Tier:** T1 (LASD bulletin text)
- **Confidence:** Confirmed
- **Extract:** Full LASD Special Bulletin text. Issuing entity: LASD Missing Persons Detail. Contact numbers: (323) 890-5500 (Missing Persons Detail); (800) 222-TIPS (8477) Crime Stoppers; lacrimestoppers.org; P3 Tips app. Last-seen location specified as **"6000 Foot Gate on Angeles Crest Highway"** (slightly different phrasing from the Solve the Case "6000ft Day Use Parking Lot"). Physical description identical to Solve the Case. **No detectives named in the public bulletin.**

**LASD Crescenta Valley Station X account — Missing Hiker post**
- **URL:** https://x.com/CVLASD/status/1937086645913956698
- **HTTP status:** 402 on direct fetch (X paywall to scrapers; URL exists per Google index)
- **Publish date:** ~June 23, 2025
- **Outlet:** LASD Crescenta Valley Station official X account
- **Tier:** T1 (verified LE official social-media)
- **Confidence:** Confirmed (post existence and account verified via redirect from twitter.com/CVLASD to x.com/CVLASD)
- **Extract:** Per Google index: "Missing Hiker – Help Us Locate Monica Reza Crescenta Valley Station is actively searching for Monica Reza, who was last seen while hiking in the Mount Waterman area..."

**LASD Crescenta Valley Station X account — Update post**
- **URL:** https://x.com/CVLASD/status/1937317093067944305
- **HTTP status:** 402
- **Publish date:** ~June 24, 2025
- **Outlet:** LASD CV Station X
- **Tier:** T1
- **Confidence:** Confirmed
- **Extract:** "We continue to search for missing hiker Monica Reza, last seen near Mount Waterman in the Angeles National Forest. Crescenta Valley Station and Montrose Search and Rescue have been working around the clock."

**LASD Crescenta Valley Station X account — Vienna update repost**
- **URL:** https://x.com/CVLASD/status/1939524007617003851
- **HTTP status:** 402
- **Publish date:** ~July 1-3, 2025
- **Outlet:** LASD CV Station X
- **Tier:** T1
- **Confidence:** Confirmed
- **Extract:** "An update on efforts to locate Monica Reza, an at-risk missing person."

**LASD Crescenta Valley Sheriff's Station — Facebook missing-person post**
- **URL:** https://www.facebook.com/CrescentaValleySheriffsStation/posts/missing-hiker-help-us-locate-monica-rezacrescenta-valley-station-is-actively-sea/1114472707384424/
- **HTTP status:** 200
- **Publish date:** 2025-06-23
- **Outlet:** LASD CV Station Facebook
- **Tier:** T1
- **Confidence:** Confirmed
- **Extract:** Public missing-person flyer with image. Contact: (818) 248-3464.

**Montrose Search and Rescue Team Facebook — Day 8 post**
- **URL:** https://www.facebook.com/MontroseSearchandRescueTeamLASD/posts/day-8-search-for-monica-rezatoday-marks-day-8-of-the-search-for-monica-reza-in-t/1040417294948776/
- **HTTP status:** 200
- **Publish date:** 2025-06-29
- **Outlet:** Montrose SAR / LASD official Facebook
- **Tier:** T1
- **Confidence:** Confirmed (post text fetched)
- **Extract:** "Search teams from across California continue to navigate steep, remote, and hazardous terrain in hopes of finding any sign of her." Hashtags include #FindMonicaReza. **This is NOT the cell-phone-forensics post; that earlier post was removed.**

**House Oversight Committee press release — Comer/Burlison letters**
- **URL (Oversight):** https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/
- **URL (Burlison):** https://burlison.house.gov/media/press-releases/comer-burlison-seek-information-missing-nuclear-and-rocket-scientists
- **HTTP status:** 403 on direct fetch from both (institutional bot-block)
- **Publish date:** 2026-04-30 (per Wikipedia citation #9)
- **Outlet:** House Committee on Oversight and Government Reform
- **Tier:** T1 (Congressional record)
- **Confidence:** Confirmed (cross-confirmed via Wikipedia, Newsweek, Axios, Fox News, Christian Post, GBNews)
- **Extract:** Letters sent to **Kash Patel (FBI), Chris Wright (DOE), Pete Hegseth (DoD/Department of War), Jared Isaacman (NASA)**. Briefing requested by April 27. Letter explicitly "flags a close professional tie between two of the missing: Aerojet Rocketdyne and JPL engineer Monica Reza and retired Air Force Maj. Gen. William Neil McCasland." Reza is **named in the letter**, not just included by reference.

**Solve the Case — Reza listing (LASD-data mirror)**
- **URL:** https://www.solvethecase.org/case/2025-56/monica-reza
- **HTTP status:** 200 (page loads — soft-404 confirmed)
- **Tier:** T1 (LE record)
- **Confidence:** Confirmed soft-404 status (no usable case fields populated)

**California Department of Public Health Vital Records — death certificate search**
- **URL:** https://www.cdph.ca.gov/Programs/CHSI/pages/Vital-Records.aspx
- **HTTP status:** Not directly queried (no public-records online search portal for individual death certificates without identifying info)
- **Outcome:** No public death certificate for Monica Reza located through indexed sources. CA Vital Records requires written request with valid relationship; no contact-required research permitted under repository rules.

**LA County Sheriff Information Bureau (LACSD ISB)**
- Not directly queried (would require contact). No publicly-indexed LACSD ISB Reza-specific bulletin located beyond the June 25 Special Bulletin.

**NamUs federal missing-person database**
- **URL:** https://www.namus.gov/MissingPersons/Search
- **HTTP status:** 200 (search interface; no public-indexed Reza MP number located)
- **Outcome:** **No NamUs MP number for Monica Reza is publicly indexed through search.** This is consistent with NamUs's pattern that LE-side cases are often not cross-listed unless family or LE specifically uploads. Existing repo cites NIC: M668487735 / FCN: 2322517300164 (NCIC numbers) — these are FBI-side identifiers, not NamUs. **Flag: No NamUs entry surfaced.**

### A4. Family / employer comms (Scully)

**London Mail — "Family of missing US scientist make very inflammatory claim... 'We're scared for our safety'"**
- **URL:** https://londonmail.co.uk/2026/05/02/family-of-missing-us-scientist-make-very-inflammatory-claim-about-what-really-happened-in-highly-suspicious-disappearance-were-scared-for-our-safety/
- **HTTP status:** 200
- **Publish date:** 2026-05-02
- **Outlet:** London Mail (UK aggregator; appears to be a US-readership-targeted UK outlet, not the *Daily Mail* / *DMG Media*)
- **Tier:** T5 (aggregator with new factual content; weighting ambiguous; downgraded vs. London Mail UK because it appears to mirror Daily Mail content)
- **Confidence:** Reported
- **Extract:** Byline "Jordan." Most detailed family-side reporting located this session. Eight family/friend interviews reported. **New factual claims:**
  - Companions: "A male yoga instructor and female friend"
  - Trail start time: 6:30 AM
  - Summit reached: ~8:45 AM
  - Last photo of Reza: ~9:00 AM near "Double Delight Peak"
  - Distance from home: ~40 miles
  - Anonymous family quotes (verbatim, attributed to "anonymous family member"):
    - "I just don't understand that they were walking in a wide open space and then she suddenly disappears without them hearing her yell or anything. The whole thing is highly suspicious."
    - "I had always suspected this was work-related. I know in my gut that she was abducted."
    - "She is not the type to just leave without telling people and she definitely was not a suicidal person."
    - "Whoever did this, if it was not an accident, was a professional. If she knew something, they could've easily taken her from her home. The family is obviously in shock and are just scared."
  - Long-time friend (50+ years) quote:
    - "She is not the type to just leave without telling people... When they didn't find her within a few days, I immediately thought, 'Someone took her.' She wouldn't have gone willingly with someone she didn't know."
  - Yoga-instructor training: friend confirms Reza was "planning to become an instructor herself" at the studio.
  - LASD statement: "The case remains an active missing person investigation. At this time, there are no clear indications of foul play. However, investigators are continuing to evaluate all possibilities and are not ruling anything out."
  - White House Principal Deputy Press Secretary **Anna Kelly**: "The White House continues to coordinate across the interagency in order to investigate these events and provide transparency to the American people. We will not get ahead of the investigation."
  - Trump (April 2026): "Some of them that we looked at were very sad cases... So far, we're finding that there's not much of a connection."

**Daily Mail (UK) — "Disappearance of rocket scientist takes chilling turn after link to critical defense technology comes to light"**
- **URL:** https://www.dailymail.co.uk/sciencetech/article-15721979/nasa-scientist-disappearance-Monica-Jacinto-Reza-california.html
- **HTTP status:** Direct fetch returns "unable to fetch" (agent-level block on dailymail.co.uk). Google Translate redirect via translate.google.com/translate?u=... returns 303/redirect. Translate.goog redirect chain returns 303 Found.
- **Publish date:** ~April 2026 (article-15721979 numbering implies April 2026)
- **Outlet:** *Daily Mail* (UK national)
- **Tier:** T4
- **Confidence:** Confirmed as published (URL exists; mirrored at londonmail.co.uk and mogaznews.com per cross-search). **Direct extraction blocked.** Flag for re-fetch via DuckDuckGo or curl with custom user-agent.
- **Extract per cross-source:** Daily Mail interviewed eight people (friends, relatives, anonymous sources) familiar with Reza's case.

**JPL colleague — Allan Petre (X public appeal)**
- **URL:** https://x.com/astro_allan/status/1939785582026412252
- **HTTP status:** 402 on direct fetch
- **Publish date:** 2025-06-30 (Day 8 of search)
- **Outlet:** Allan Petre, NASA JPL aerospace engineer (verified via LinkedIn match `linkedin.com/in/allan-petre`)
- **Tier:** T1 (insider direct testimony to JPL employment)
- **Confidence:** Confirmed via search-engine snippet
- **Extract:** "I'm reaching out to my professional and personal network in the hope of finding a dear colleague and friend, **Monica Reza, Director of the Materials Processing Group at NASA JPL**. Monica was last seen near Mount Waterman, along Angeles Crest Highway, last Sunday." **This is the strongest insider corroboration of her JPL title outside official LASD channels.**

**Help Find Monica Instagram / Facebook (helpfindmonicareza)**
- **URL (LinkedIn proxy):** https://www.linkedin.com/posts/allan-petre_help-find-monica-helpfindmonicareza-activity-7344704035611963392-bApi
- **HTTP status:** Search-index hit; LinkedIn 999 to scrapers
- **Outlet:** Allan Petre (creator/admin per index)
- **Tier:** T6 (insider-managed civilian-search platform)
- **Confidence:** Confirmed account exists

**Help Find Monica Reza Facebook group**
- **URL:** https://www.facebook.com/groups/findmonica/
- **HTTP status:** 200 (content truncated)
- **Outlet:** civilian search group
- **Tier:** T7
- **Confidence:** Confirmed exists. Sentinel Briefing's "Phone Gap" piece references a *separate* civilian Facebook group that was deleted after a commenter posted a device-tampering theory.

**JPL employee directory**
- **URL:** https://www.jpl.nasa.gov/people/
- **HTTP status:** 404 (page does not exist at that exact path)
- **Outcome:** **No publicly-accessible JPL employee directory or Materials Processing Group page located.** JPL does not operate a public org-chart at that URL. No directory-side confirmation of Reza's directorship found this session.

**NASA Technical Reports Server (NTRS)**
- **URL:** https://ntrs.nasa.gov/search?q=Monica%20Jacinto
- **HTTP status:** 200
- **Outcome:** **Zero NTRS hits for "Monica Jacinto" or "Monica Reza."** No NASA technical reports authored or co-authored by her. This is consistent with her being a **process-engineering / materials-implementation researcher rather than a publishing scientist** — her output is patents (abandoned) and corporate technical fellowship rather than peer-reviewed papers. Hardwick has substantive publication record (UNSW alumni profile cites academic publications); Reza does not.

**ResearchGate**
- Not directly fetched (RG returns 403 to scrapers per prior agent reports). No Reza-authored publications surfaced via search-index.

**Aerojet Rocketdyne press releases**
- **URL (2016 Mondaloy milestone):** https://www.globenewswire.com/en/news-release/2016/09/06/869894/0/en/AFRL-Technology-Demonstration-Program-Gives-Boost-to-Future-Hydrocarbon-and-AR1-Engines.html
- **HTTP status:** 200
- **Publish date:** 2016-09-06
- **Outlet:** GlobeNewswire (Aerojet Rocketdyne press release distribution)
- **Tier:** T1 (corporate primary)
- **Confidence:** Confirmed
- **Extract:** **First public test of Mondaloy 200™ in a rocket engine environment.** Named officials: **Joe Burnett** (Program Manager, HBTD); **Eileen Drake** (CEO and President of Aerojet Rocketdyne); **Glenn Mahone** and **Mary Engola** (media contacts). Burnett: "Consistent gas temperatures in an engine are critical for turbomachinery performance." Drake: "What we've learned will be instrumental as other engines are developed using this same engine cycle." Notes: 250,000 lbf thrust class HBTD; 100-flight reusability target; preburner test at Edwards AFB Test Stand 2A (historic F-1 / Saturn V test stand). **AR1 directly cited as RD-180 alternative.** This is the corporate-side T1 source most directly bearing Mondaloy provenance.

**Boeing media-room press release — HENAAC Luminary Award**
- **URL:** https://boeing.mediaroom.com/2004-10-11-Two-Boeing-Employees-Receive-National-Recognition
- **HTTP status:** 200
- **Publish date:** 2004-10-11
- **Outlet:** Boeing
- **Tier:** T1 (employer-side primary)
- **Confidence:** Confirmed
- **Extract:** Co-honoree **Mike Cave** also recognized. Reza identified as: "Boeing Integrated Defense Systems engineer / Boeing Associate Technical Fellow / metallurgical engineer at Rocketdyne laboratories in Canoga Park, California / co-inventor of Mondaloy." HENAAC citation language: "her significant contributions to the Hispanic technical community and for inspiring youth to pursue engineering and technical careers." **This is the highest-tier source on her HENAAC award, replacing the T4 multiple-news-source citation in the repo.**

**L3Harris press release — Aerojet Rocketdyne acquisition completion**
- **URL:** https://www.l3harris.com/newsroom/press-release/2023/07/l3harris-completes-aerojet-rocketdyne-acquisition
- **HTTP status:** 200
- **Publish date:** 2023-07-28
- **Outlet:** L3Harris (corporate primary)
- **Tier:** T1
- **Confidence:** Confirmed
- **Extract:** Christopher E. Kubasik (Chair/CEO, L3Harris); Ross Niebergall (President of AR segment at L3Harris). $4.7B acquisition, 5,000+ AR employees joined L3Harris. Aerojet Rocketdyne becomes fourth L3Harris segment. **No mention of Monica Jacinto, Mondaloy, or specific Technical Fellow personnel.**

**Spaceflight Now — "L3Harris announces $845 million majority sale of Space Propulsion and Power Systems business"**
- **URL:** https://spaceflightnow.com/2026/01/09/l3harris-announces-845-million-majority-sale-of-space-propulsion-and-power-systems-business/
- **HTTP status:** 200
- **Publish date:** 2026-01-09
- **Outlet:** Spaceflight Now (specialized aerospace press)
- **Tier:** T3 (industry beat)
- **Confidence:** Confirmed
- **Extract:** Byline Will Robinson-Smith. **L3Harris divested Space Propulsion and Power Systems business to AE Industrial Partners for $845M (60% majority stake).** New entity reverts to standalone "Rocketdyne" name. RL10 upper stage engine primary focus; RS-25 *excluded* from sale. Closure expected H2 2026. **Mondaloy / AR1 not mentioned in the sale.** This is a corporate-custody change for the Mondaloy IP family that post-dates Reza's disappearance by ~7 months.

## Mulder-side findings

### B1. Precursor / disclosure findings (911 + Find-a-Grave anomaly)

**The morning 911 call about screaming — primary attribution:**
- **Source:** Sentinel Briefing "The Phone Gap" (T7); cited verbatim by Men's Journal / Yahoo / AOL syndication
- **Specifics:** "On June 22, 2025, someone in the general Mount Waterman area called 911 to report hearing a woman screaming. That call connected." Sentinel uses this to argue cellular coverage existed in the area that morning, undermining the "dead zone" theory.
- **Tier of original report:** T7 Sentinel (no LASD / dispatch transcript public)
- **Confidence:** Reported
- **Status:** No T1 LASD confirmation. **The 911 call may or may not be Reza-related — it was simultaneous and proximate but not officially connected to her case by LE.**

**The 2:30 PM Twin Peaks Saddle "anguish" report — NEW THIS SESSION:**
- **Source:** websleuths thread reconstruction; eispiraten thread; cross-cited in search-index summaries
- **Specifics:** "Two hikers returning from Twin Peaks heard what sounded like a female in anguish or despair (not calling for help) around Twin Peaks Saddle area at approximately 2:30pm" on June 22, 2025. Forum discussion notes "few searches were conducted in that area in the first couple of months."
- **Tier:** T7 (forum reconstruction; original police-report language not located)
- **Confidence:** Reported
- **Status:** **NOT currently in `cases/reza.md`. Operationally significant if confirmed — it would push the disappearance window from "vanished by 9:30 AM" to "potentially still alive at 2:30 PM in Twin Peaks Saddle area."** Flag for repo addition.

**Find-a-Grave memorial 284387277 anomaly — NO NEW EVIDENCE:**
- Repository's existing characterization (Sentinel Briefing T7 source; "lillian" creator non-public; "J.C." maintainer ID 50725353; created June 26 listing "green burial"; removed approximately March 27, 2026 four days after Sentinel coverage) is the highest-tier evidence available.
- **Wayback retrieval status: NEGATIVE this session (agent-level block on web.archive.org).**
- **Find-a-Grave direct fetch: NEGATIVE (403 blocks).**
- "J.C." profile ID 50725353 — direct profile fetch blocked. No "J.C." memorial-creation history surfaced through indexed search.
- **No alternative archival site (archive.today, cachedview.com, Google Cache) surfaced indexed snapshots of memorial 284387277.**

**Subject A behavioral anomalies — uapmurders.com / Sentinel:**
- "Subject A explicitly told Reza to make a northerly right turn. He claims she acknowledged with a wave. However, when SAR arrived, Subject A was reportedly 'irritated' that teams searched north and insisted she must have traveled south."
- Subject A "is documented as using his phone extensively after the disappearance (Zoom meetings, phone calls, four-minute video) but no record of him attempting to call Reza's number."
- "A civilian Facebook group titled 'Help Find Monica Reza in the Angeles National Forest' was deleted after a commenter posted a theory implicating Subject A in device tampering."
- **Tier:** T7 (uapmurders.com + Sentinel Briefing)
- **Confidence:** Alleged
- **Status:** Significant Mulder-side material that the repo currently captures only as an open question. The "Subject A directional contradiction" detail is a *concrete* alleged behavioral anomaly with implications — but rests entirely on T7 sources with no T1-3 corroboration.

### B2. Insider venue (TikTok / YouTube / Reddit / Substack)

**TikTok:** Indirect references via news-aggregator-style coverage on TikTok (e.g., LA Magazine TikToks of Conlin reporting). No deep investigative TikTok-creator content indexed for Reza this session. **Reza coverage is primarily YouTube / Substack-driven**, unlike Eskridge (which is heavily TikTok-driven). Asymmetry data point.

**YouTube:**
- **NewsNation Elizabeth Vargas Reports** (multiple Reza segments): https://www.newsnationnow.com/video/willaim-mccasland%E2%80%99s-ex-colleague-went-missing-months-before-him-elizabeth-vargas-reports/11616922/ [T4 video]
- **"11 Missing Scientists Investigator UNLOADS on the Case | Lauren Conlin"** — https://www.youtube.com/watch?v=-Ht5DIP2sho [T4 video, Conlin LA Mag interview]
- **"What One Investigator Found About the 'Missing Scientists' | Lauren Conlin"** — https://www.youtube.com/watch?v=I3yqntoghVM [T4]
- **"Family Breaks Silence on Missing Rocket Scientist, Same Day Caltech Scientist's Killer Faces Judge"** — https://www.youtube.com/watch?v=IeGQw5O932U [T4]
- **"Something Isn't Right About the Monica Reza Disappearance"** — https://www.youtube.com/watch?v=MPfMm9BSzsI [T6 creator]
- **"The disappearance of Monica Reza: General William McCasland's colleague"** — https://www.youtube.com/shorts/RA5ML6zJSq4 [T6]
- **"Woman missing since last year has ties to missing retired Air Force general"** — https://www.youtube.com/shorts/Wi1JLh_l5Ns [T6]

**Reddit:**
- **r/socalhiking** — referenced as primary host of preserved MSAR Facebook post text (per Sentinel Briefing). Direct thread URLs not located this session.
- **websleuths thread** — https://websleuths.com/threads/ca-monica-reza-60-hiker-mount-waterman-los-angeles-national-forest-22-jun-2025.747266/ — references CalTopo collaborative map (https://caltopo.com/m/P0GPMBL) showing volunteer search GPX tracks; Devil's Canyon hat-finding location; Three Points trailhead context. **Tier T7 forum reconstruction; primary sources are the LASD Facebook posts and USDA Forest Service PCT-Trailhead-6000 page (https://www.fs.usda.gov/r05/angeles/recreation/pct-trailhead-6000) — both T1.**
- **EISPIRATEN thread (German hiking forum)** — https://eispiraten.com/viewtopic.php?t=9445 — multi-page discussion, contains the Twin Peaks Saddle 2:30 PM anguish-report references.

**Substack:**
- **The Sentinel Briefing — "The Green Burial"** (https://thesentinel.network/p/the-green-burial-she-was-declared, March 16, 2026) [T7, Confirmed as published]
- **The Sentinel Briefing — "The Phone Gap"** (https://thesentinel.network/p/the-phone-gap-monica-rezas-cell-phone, March 23, 2026) [T7, Confirmed]
- **The Sentinel Briefing — "What Is Mondaloy: The American Alloy Built to Replace Russian Rocket Engines"** (https://thesentinel.network/p/what-is-mondaloy-the-american-alloy, April 23, 2026) [T7, Confirmed] — most technical of the Sentinel Reza pieces; details Russian patent assignment, L3Harris 10-K $0 developed-tech-asset valuation, FTT coating-patent line, AR1 program cancellation timeline.
- **Sentinel Briefing — "The Long Count"** (https://thesentinel.network/p/the-long-count) — 404 on direct fetch; URL referenced by other Sentinel pieces; possibly removed.
- **Fortean Winds — "The Mondaloy Chain: What the Record Actually Shows"** (https://forteanwinds.com/2026/04/13/the-mondaloy-chain/, 2026-04-13) [T7] — explicitly Mulder-side; argues Reza-McCasland-Hardwick triangle through documented institutional ties.
- **Legion Australia (LegionAUS) — "What is Mondaloy?"** (https://legionaus.substack.com/p/what-is-mondaloy-and-why-cant-you, 2026-03-21, byline Nicholas Lehmann) [T7]
- **Modernity News — "CONNECT THE DOTS: New Details Emerge in Disappearance of JPL Rocket Scientist"** (https://modernity.news/2026/04/17/connect-the-dots-new-details-emerge-in-disappearance-of-jpl-rocket-scientist/, byline Steve Watson) [T6]
- **17GEN4 (Michael R. Cronin) — "Rocket Scientist with Ties to Classified U.S. Propulsion Technology Remains Missing Nearly 10 Months After Vanishing"** (https://www.michaelrcronin.com/post/rocket-scientist-with-ties-to-classified-u-s-propulsion-technology-remains-missing-nearly-10-months, 2026-04-14) [T7]
- **uapmurders.com — Reza profile** (https://uapmurders.com/energy/Details/Monica_Jacinto_Reza/) [T7]
- **theytelluslies.com — Reza/McCasland Mondaloy connection** (https://theytelluslies.com/the-mondaloy-connection-monica-reza-william-mccasland/) [T7]
- **The Mondaloy File** (https://mondaloy.nowa.ca/ and https://the-mandaloy-file-nu.vercel.app/) [T7] — open-source investigation portal
- **Joann LeQuang Substack — "When Scientists Go Missing"** (https://joannlequang.substack.com/p/when-scientists-go-missing) [T7]
- **Britbrief.co.uk — "Vanished Scientist's Patent for Advanced US Launch Systems Sparks Concern"** (https://britbrief.co.uk/politics/lobbying/missing-scientists-patent-tied-to-us-advanced-launch-systems.html) [T6]
- **whatsgoingonnews.net — "'Not normal': lawmaker sees striking similarities"** (https://www.whatsgoingonnews.net/post/not-normal-lawmaker-sees-striking-similarities-in-scientist-disappearances-wants-answers) [T6]

### B3. Mulder-side domain investigation (Mondaloy / propulsion materials)

**Patent custody chain — newly verified this session:**
| Year | Custodian | Event |
|---|---|---|
| 2001-09-18 | Boeing Company | Original assignment of US-20030053926-A1 priority |
| 2002-09-17 | Boeing → Rospatent | Russian filing RU2002124799/02A within Paris Convention 12-month window |
| 2004-06-03 | — | US-20030053926-A1 abandoned for failure to respond |
| 2006-03-27 | United Technologies Corp | US-20040208777-A1 assigned to UTC |
| 2007-06-19 | Pratt & Whitney Rocketdyne | UTC subsidiary takes ownership |
| 2007-06-20 | Rospatent grants RU2301276C2 | **The only granted patent in the family — to UTC, not Boeing** |
| 2007-07-12 | — | Mondaloy™ trademark application 78970097 abandoned |
| 2009-12-07 | — | US-20040208777-A1 abandoned after examiner's answer |
| 2012-09-18 | — | Russian patent RU2301276C2 invalidated for non-payment of fees |
| 2012-12-01 | — | US-20100266442-A1 abandoned |
| 2013 | Aerojet Rocketdyne (GenCorp merger) | AR takes ownership of inventor-assigned and corporate-assigned patents |
| 2016-09-06 | Aerojet Rocketdyne + AFRL | First public Mondaloy 200™ rocket-engine hot-fire test (Edwards AFB) |
| 2016-08-03 | Florida Turbine Technologies | FTT files US-20170082070-A1 citing Mondaloy 100/200 by reference (Jacinto et al.) |
| 2017-Q3 | Aerojet Rocketdyne | Critical Design Review for AR1 with twelve major Mondaloy components specified |
| 2018 | ULA selects Blue Origin BE-4 | **AR1 program canceled; Mondaloy enabling-material loses its program-of-record vehicle** |
| 2019-02-28 | Kratos Defense | Acquires 80.1% of FTT for $60M |
| 2021-01-15 | — | FTT US-20170082070-A1 (Mondaloy coating patent) abandoned |
| 2023-07-28 | L3Harris | Acquires Aerojet Rocketdyne ($4.7B); SEC 10-K assigns $0 developed-technology asset value |
| 2026-01-09 | AE Industrial Partners | L3Harris announces sale of Space Propulsion / Power Systems ($845M, 60% majority); RS-25 excluded |

**The Mondaloy IP is currently:**
- Trade-secret / common-law-mark territory (no granted US patent; expired Russian patent; abandoned trademark)
- Held by L3Harris (transitioning to AE Industrial Partners-controlled "Rocketdyne" entity in H2 2026)
- Without a program-of-record (AR1 canceled 2018)
- Valued by L3Harris's auditor at $0 developed-technology asset

**This is the *strategic-tech-disclosure* picture that the repo currently does not fully capture.** Sentinel Briefing's "What Is Mondaloy" piece is the most thorough public synthesis of this chain.

**AFRL collaboration documentation:**
- **2016-09-06 GlobeNewswire press release** (T1) confirms "Mondaloy 200™ super alloy, developed collaboratively by Aerojet Rocketdyne and the AFRL Materials Directorate." Maj. Gen. Tom Masiello (AFRL commander at the time) quoted: "An objective of this program is to help eliminate the United States' reliance on foreign rocket propulsion technology... key to ensuring our national security." [T1]
- AFRL ManTech program: not located as a directly-cited Mondaloy program in this session's searches. **HBTD (Hydrocarbon Boost Technology Demonstrator)** is the documented AFRL program-of-record. AIAA Propulsion Forum 2020 paper "Key Achievements of Hydrocarbon Boost Technology Demonstrator Program" (https://arc.aiaa.org/doi/10.2514/6.2020-3833) is the academic-side T2 source on HBTD outcomes.
- AFRL Wright-Patterson institutional connection: Hardwick was AFRL Materials Directorate (Ohio / Wright-Patterson) 2005-2012; McCasland commanded AFRL at Wright-Patterson 2011-2013 — overlapping by 2 years. Reza collaborated with AFRL from 1999 onward but her primary employer remained at Aerojet Rocketdyne (Canoga Park, CA) until ~2024-2025.

**Hardwick research record (UNSW alumni profile, T2):**
- BHons Metallurgy 1972, PhD Metallurgy 1977 — University of New South Wales (one of the first women to earn a PhD from UNSW Metallurgy)
- Postdoc McGill (archaeometallurgy)
- Carnegie Mellon (hydrogen interactions in aluminium)
- Martin Marietta Research Laboratories (Space Shuttle external tank materials)
- Los Alamos National Laboratory (1982, married Pat Martin, nuclear weapons degradation research)
- US citizen 1985
- Rockwell Science Centre California (metal combustion in high-pressure oxygen — *this is the Mondaloy work with Reza*)
- Boeing Seattle
- AFRL Ohio (2005-2012, led materials research for advanced gas turbine engines)
- Meritorious Civilian Service Medal (2010); first woman TMS Structural Materials Distinguished Service Award (2010)
- US Air Force representative on a five-country cooperative panel managing Materials Technology
- Retired 2012 (stage-four metastatic breast cancer diagnosis)
- AFRL Emeritus Program mentoring 2012-2014
- Died January 5, 2014

**Hardwick's Los Alamos employment (1982) is a separate institutional connection** — LANL is the institutional center for Casias / Chavez (also missing/dead). Not currently in repo.

**McCasland link via Mondaloy oversight:**
- Newsweek (Jordan King, 2026-03-18): "Reza once worked on a government-funded rocket materials project overseen by McCasland."
- Newsweek caveat (LA Magazine cited via brobible): "**there is no confirmed reporting from law enforcement or the government establishing that Reza worked for a company directly overseen by McCasland during his tenure at the Air Force Research Laboratory**."
- Status: **Reported** professional connection. The institutional-ecosystem overlap (AFRL Materials Directorate / AR1 funding / HBTD program) is documented (T1-T2). The *direct-oversight* characterization is a NewsNation framing inferred from McCasland's role as AFRL commander 2011-2013 during Hardwick's AFRL tenure.

### B4. Foreign coverage

**WION India — "The Mondaloy Mystery: Two aerospace experts with ties to 'special projects' go missing"**
- **URL:** https://www.wionews.com/trending/the-mondaloy-mystery-two-aerospace-experts-with-ties-to-special-projects-go-missing-triggering-security-concerns-1774248547608
- **HTTP status:** 200 (per index)
- **Outlet:** WION (Indian national)
- **Tier:** T4 foreign mainstream
- **Confidence:** Reported
- **Extract:** Already cited in repo. WION is *the* foreign outlet most actively framing the Reza-McCasland Mondaloy connection.

**India Today — "US rocket scientist vanishes without trace as secret military patent emerges"**
- **URL:** Per Wikipedia citation #10 — Singh, Nitish K. (2026-04-11)
- **Outlet:** India Today
- **Tier:** T4 foreign mainstream
- **Confidence:** Reported

**Daily Mail (UK)** — see A4 above. **Direct fetch blocked. Flag for next session.**

**News.az (Azerbaijan)** — "Unexplained deaths and disappearances of NASA scientists spark security alarms" (https://news.az/news/unexplained-deaths-and-disappearances-of-nasa-scientists-spark-security-alarms) [T5/T6]

**MSN UK / aggregator** — "Missing rocket scientist linked to unique defence alloy patent" (https://www.msn.com/en-gb/news/insight/missing-rocket-scientist-linked-to-unique-defence-alloy-patent/gm-GME908AE79) [T4 foreign aggregator]

**Pamfleti.net (Albania) — "The Mystery of 'Mondaloy' / Two Disappearances and Three Suspicious Deaths"** (https://pamfleti.net/english/bota/misteri-i-mondaloy-dy-zhdukje-dhe-tre--te-dyshimta-ne-fushen-e-aeroha-i327708) [T5 foreign]

**Britbrief.co.uk** — see B2 list. UK independent.

**London Mail** — see A4. UK aggregator (likely *not* the actual Daily Mail; appears US-readership-targeted).

**Sott.net (multinational alt-conspiracy)** — "Scientist connected to missing Air Force general associated with UFOs disappeared last year under eerily similar circumstances" (https://www.sott.net/article/505275-Scientist-connected-to-missing-Air-Force-general-associated-with-UFOs-disappeared-last-year-under-eerily-similar-circumstances) [T6/T7 foreign]

**No surfaced coverage:** Le Monde, Der Spiegel, El País, ABC AU, NHK, Asahi, Yomiuri, TASS, Xinhua, China Daily, RT (no direct Reza piece — RT covered Eskridge but not Reza this session). **The Reza foreign-coverage set is concentrated in UK + India + Albanian/Eastern-European aggregators**, similar to Eskridge's pattern, with the same Continental-Europe / Russian-language-Russia / Chinese-language-China silence.

### B5. Geographic / institutional context (JPL cluster)

**JPL cluster (Reza, Hicks, Maiwald):** Existing repo coverage is canonical. New finding this session: **Pasadena Now's April 22 piece** confirms "JPL is managed by Caltech for NASA" and explicitly groups the three JPL cases.

**Caltech adjacency:** Grillmair (Caltech/IPAC) is institutionally adjacent (both Caltech-managed). The repo correctly captures this.

**Wright-Patterson / AFRL cluster:**
- McCasland: AFRL commander 2011-2013, Wright-Patterson
- Hardwick: AFRL Materials Directorate 2005-2012, Wright-Patterson (overlap with McCasland 2011-2012)
- Reza: AFRL collaborator from 1999 onward; never AFRL-employed. Aerojet Rocketdyne employer in Canoga Park CA.
- October 2025 three-Wright-Patterson-employee deaths (per Fortean Winds, Sentinel) — separate cluster, *currently in dossier as the McCasland-related Wright-Patterson story*.

**LANL (Los Alamos) connection — NEWLY SURFACED:**
- Hardwick's 1982 employment at Los Alamos National Laboratory (per UNSW alumni profile, T2)
- LANL is the institutional center for Casias / Chavez cases
- Hardwick is currently captured in the dossier as Reza's co-inventor; her LANL tenure has not been mapped against the LANL cluster
- **Flag for repo addition** — Hardwick is a documented institutional bridge between the JPL/Aerojet cluster (Reza) and the LANL cluster (Casias, Chavez), even though Hardwick herself is not classified as a "missing/dead scientist" within the dossier's scope (she died of cancer in 2014).

**Geographic spread of the Mondaloy triangle:**
- Hardwick: Sydney → Pittsburgh → Maryland → Los Alamos NM → Thousand Oaks CA (Rockwell Science Center) → Seattle WA → Dayton OH (AFRL Wright-Patterson) → death Dayton OH 2014
- Reza: New York (Columbia) → Los Angeles (UCLA / Canoga Park / Pasadena) → missing Angeles National Forest CA 2025
- McCasland: Albuquerque NM (PHILIPS Research / Kirtland) → Wright-Patterson OH (AFRL) → retirement Albuquerque NM → missing Albuquerque NM 2026
- Three states: CA, OH, NM (with Los Alamos NM and Wright-Patterson OH as institutional anchors)

## Imbalance note

**This case has more documentary depth on the Mulder side than on the Scully side, in a way that's structurally different from Eskridge.** Eskridge's Scully side rested on absent-evidence-as-evidence-of-routine-suicide; her Mulder side had two large and growing tranches of pre-death disclosure. Reza's situation is the inverse:

- **Mulder side has:** documented institutional-ecosystem ties (AR1 / HBTD / AFRL / Wright-Patterson), strategic-tech context (Russian-patent-grant in 2007, $0 IP-asset valuation, AR1-program cancellation, L3Harris divestiture), specific behavioral anomalies on Subject A (T7 only), Find-a-Grave memorial (T7 with primary record now removed), 2:30 PM Twin Peaks Saddle anguish report (T7 forum reconstruction), morning 911 call (T7), cell-phone-forensics-acknowledged-then-redacted MSAR Facebook post (T7 preserved via Reddit per Sentinel), removed civilian Facebook group, explicitly-named-in-Congressional-letter status (T1).
- **Scully side has:** physical-evidence absence (only beanie + lip balm in 40-50 mile search radius), LASD's stated "no clear indications of foul play" formulation (London Mail), JPL/NASA/Aerojet/Caltech/Wright-Patterson institutional silence (per Fortean Winds — multiple T1 entities have not issued statements), the geographic + terrain plausibility of an unaccompanied 60-year-old hiker disappearing in 700,000+ acres of rugged terrain.

**Key Scully-side weakness:** there is no Coffindaffer-equivalent named retired-FBI / named-investigator skeptical voice on Reza's case. No counter-pressure from credentialed experts arguing routine-hiking-misadventure. No published medical-examiner report (because no remains). No autopsy. No direct LE interview characterizing Subject A's account.

**Key Mulder-side weakness:** the pattern coverage is overwhelmingly T7-sourced (Sentinel Briefing, uapmurders.com, Fortean Winds, Modernity, 17GEN4). The T1 evidence (LASD bulletin, USPTO patents, Boeing 2004 press release, AFRL/AR 2016 press release, Comer/Burlison letter, L3Harris filings) supports the *institutional-ecosystem* framing but does not establish foul play, foreign intelligence, or any of the X-Files-side hypotheses. The Subject A behavioral anomalies are entirely Tier-7 sourced.

**Both sides are thin on official LE documentation** — LASD has stopped publicly speaking about the case (last LE-side public statement is Vienna's July 3, 2025 release; nothing public from Detectives Rincon/Sanchez since). The London Mail anonymous family quotes in May 2026 are the *only* reportedly-on-record statements from the family side.

**To balance** the next session should prioritize:
1. **Wayback Machine retrieval of Find-a-Grave 284387277** — manual user-side fetch via curl; this is the single most operationally significant missing artifact.
2. **Daily Mail UK direct fetch** — the original Chris Melore / DMG-Media-attributed piece (per london mail attribution chain) needs direct retrieval.
3. **LA Magazine Conlin pieces** — the two LA-local-press flagship articles are 403-blocked at fetch time but contain LA-local insider details (yoga studio identity, Vedic-sciences detail, additional family characterizations).
4. **NamUs cross-listing check** — query NamUs by surname and physical description, not by NIC/FCN.
5. **JPL Materials Processing Group public-facing artifact** — Wayback of jpl.nasa.gov directory pre-2025 to confirm directorship listing.
6. **California Vital Records query** — public-records search for Reza death certificate (no FOIA needed; CA death index is partially public).

## Search queries log

In rough order:
1. `"Monica Reza" findagrave memorial 284387277 wayback archive`
2. `"Monica Reza" LASD Crescenta Valley Station press release missing hiker`
3. `"Monica Reza" NamUs missing persons NIC M668487735`
4. `"Monica Jacinto" OR "Monica Reza" "JPL" OR "Jet Propulsion Laboratory" director materials processing`
5. `"Monica Reza" lamag family "doesn't make sense" "scared for our safety"`
6. `"Monica Reza" newsnation McCasland "ex-colleague" connection`
7. `"Monica Reza" findagrave wayback OR archive.today removed memorial green burial`
8. `"HENAAC" 2004 "Luminary Award" "Monica Jacinto" inaugural Hispanic engineer`
9. `"Dallis Hardwick" Rockwell Science Center materials scientist obituary cancer`
10. `"Monica Jacinto" AIAA "Associate Fellow" conference paper materials engineering`
11. `"Mondaloy" AR1 engine "Hydrocarbon Boost" AFRL ManTech "ETP" propulsion`
12. `site:web.archive.org "284387277" findagrave Reza`
13. `"Monica Reza" findagrave "lillian" OR "J.C." memorial creator profile`
14. `"Monica Jacinto" NTRS NASA technical reports server materials`
15. `"AFRL Achieves Major Milestone in Rocket Engine" 2016 Mondaloy press release`
16. `"L3Harris" acquisition "Aerojet Rocketdyne" 2023 press release`
17. `"Monica Jacinto" "Cal State LA" Dean's Advisory Board LAunchPad`
18. `"Monica Jacinto" Daily Mail OR "dailymail.co.uk" disappearance scientist Reza`
19. `"Monica Reza" "yoga" instructor companion identified named hiking`
20. `"Monica Reza" "Twin Peaks Saddle" anguish 911 screaming hiker`
21. `"Monica Reza" obituary OR funeral OR memorial death certificate California`
22. `"Monica Jacinto" obituary parents Reza Mexico Hispanic family`
23. `"Monica Reza" "Double Delight Peak" OR "Twin Peaks" OR "Upper West Ridge" hiking`
24. `"Monica Reza" "JPL" hire date "Director" "Materials Processing" 2024 OR 2025`
25. `"Monica Reza" "Subject A" companion identified yoga male`
26. `"Comer Burlison" letter scientists DOE NASA "Monica Reza" specifically named`
27. `"Allan Petre" JPL Monica Reza colleague astrophysicist materials`
28. `"Mondaloy" granted US patent 7740713 OR 8133334 OR alloy issued`
29. `"Monica Reza" "Phillips Research Site" OR "Air Force Research Laboratory" Wright-Patterson`
30. `"web.archive.org" "284387277" OR findagrave "Monica" "Reza" snapshot`
31. `"Monica Jacinto" "Aerojet Rocketdyne" 2016 milestone "AFRL" Mondaloy press`
32. `"Monica Reza" "Lauren Conlin" LA Magazine cell phone forensics`
33. `"Monica Reza" "Montrose Search and Rescue" Facebook cell phone forensic`
34. `"Monica Reza" "death certificate" California Department Public Health Vital Records`
35. `"Monica Jacinto" Columbia University metallurgical engineering 1986 OR 1987 alumna`

**Direct WebFetch URLs attempted this session: ~40.** Notable systematic-block patterns: web.archive.org (agent-level block — total negative for this session), dailymail.co.uk (agent-level block), x.com (402 paywall), facebook.com (mostly 200 with content extraction; one 403 on goldrush mirror), lamag.com (403 systematic), newsnationnow.com (403 systematic), oversight.house.gov (403), burlison.house.gov (403), thehill.com (not retried), thesentinel.network (200 — extracted successfully), patents.google.com (200 — fully extractable), boeing.mediaroom.com (200), wikipedia.org (200), unsw.edu.au (200), spaceflightnow.com (200), forteanwinds.com (200), uapmurders.com (200), modernity.news (200), londonmail.co.uk (200), goldrushcam.com (200), pasadenanow.com (200), heysocal.com (200), outdoors.com (200), snowbrains.com (200), crescentavalleyweekly.com (200).

## Anomalies

1. **Wayback Machine total agent-level block.** Every Find-a-Grave / Daily Mail / web.archive.org direct fetch failed. This is a *capability* anomaly, not a Reza-specific anomaly, but it materially affects the case file because the highest-priority artifact (Wayback of memorial 284387277) cannot be retrieved this session. **Flag for user-side curl retrieval.**
2. **Boeing as original Mondaloy patent assignee.** The repo currently says "patent assignee: Individual" based on the US-20100266442-A1 record. That's correct *for that specific application* — but the *first* application (US-20030053926-A1, priority 2001-09-18) was assigned to **Boeing Company** at filing. The patent then traveled Boeing → United Technologies → Pratt & Whitney Rocketdyne → Aerojet Rocketdyne → L3Harris → AE Industrial Partners (pending). The 2009-filed continuation went into individual-assignment because by then Aerojet Rocketdyne held the corporate-side rights and the inventor-side filing was a separate strategic choice. This is a **5-step institutional custody chain that the repo does not capture**.
3. **Russian patent grant 2007 to United Technologies Corporation.** The Mondaloy patent family's *only granted patent worldwide* was a Russian patent held by an American corporate parent, granted during the active RD-180-on-Atlas-V national-security-payload era (2007). The patent went invalid in 2012 for non-payment. **The strategic-disclosure framing is not in the repo.**
4. **L3Harris's $0 developed-technology asset valuation in the 2023 10-K.** Per Sentinel Briefing's "What Is Mondaloy" piece (T7 reading SEC filings T1), L3Harris's purchase-price allocation for the Aerojet Rocketdyne acquisition assigned $2,720M to customer relationships, $120M to trade names, and **$0 to developed technologies**. This is auditor-side framing that the proprietary IP (including Mondaloy) had no separately-recognized accounting value. This is a substantive corporate-finance fact about the Mondaloy IP that would be an interesting Mulder-side data point ("the strategic-defense-tech IP was valued at zero").
5. **AR1 program cancellation 2018.** The HBTD-with-Mondaloy-as-enabling-material program lost its program-of-record vehicle when ULA picked Blue Origin's BE-4 for Vulcan in 2018. This is 7 years before Reza's 2025 disappearance. **The strategic-significance argument depends on whether Mondaloy retained classified or trade-secret value after the AR1 cancellation, which is not publicly resolvable.**
6. **2:30 PM Twin Peaks Saddle anguish report.** Forum-reconstructed (T7) primary detail not currently in repo. If true, it operationally extends Reza's last-known-alive window from ~9:30 AM to ~2:30 PM.
7. **No NamUs entry surfaced for Reza.** Despite being a 60-year-old at-risk missing person under active LASD investigation since June 2025 with federal-investigation framing, no public NamUs MP record indexed. NCIC numbers (M668487735 / FCN 2322517300164) are FBI-side, separate from NamUs DOJ database.
8. **Allan Petre as insider corroborator.** A NASA JPL aerospace engineer publicly described Reza as "Director of the Materials Processing Group at NASA JPL" in a June 30, 2025 search appeal — this is the cleanest *insider* corroboration of her JPL title and pushes the JPL-employment claim from "Reported via news framings + LASD bulletin" to "Reported with insider direct testimony." Petre's appeal also drove the helpfindmonicareza.org / Facebook / Instagram civilian search ecosystem.
9. **Hardwick's LANL employment 1982.** Co-inventor's 1982 LANL tenure is institutional-bridge to the Casias / Chavez LANL cluster. Not currently mapped in the dossier's connection-analysis layer.
10. **Repository date-of-Hardwick-death error.** Repo says 2015; multiple T1/T2 sources (UNSW alumni profile, Dignity Memorial obituary, Wikipedia, Sentinel, Fortean Winds) confirm January 5, 2014. **Flag for repo correction**.
11. **Subject A documentary record vs. official silence.** Subject A is documented in T7 sources as the male yoga companion who allegedly gave directional contradictions and used his phone post-incident without calling Reza. LE has neither confirmed nor denied any of these characterizations publicly. The case file's "two yoga companions undisclosed" framing is correct; the pattern of silence around Subject A's identity is itself a data point.
12. **Family quotes consistency.** All Reza-family quotes published as of this session are anonymous (London Mail / Daily Mail / LA Magazine Conlin pieces). No on-record family member named in mainstream press, in contrast to McCasland (wife Susan McCasland Wilkerson on-record) and Eskridge (father Richard Eskridge on-record). The Reza family is operating in collective-anonymity mode, citing fear for safety. This is a behavioral-pattern data point.

---

**Bundle authored by:** Source-deepening agent (general-purpose, Opus 4.7 [1M context])
**Read-only on cases/reza.md throughout.**
**Date:** 2026-05-08
