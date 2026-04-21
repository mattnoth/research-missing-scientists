# Research TODO

Items deferred from the prompt-001 cycle. Revisit before or after PDF/website generation.

## Actionable now (web search could fill)

- [ ] **House Oversight briefing results** — Comer/Burlison requested briefing by April 27, 2026. Check for public statements, press releases, or news coverage of what was disclosed.
- [ ] **FBI investigation updates** — Patel said they'd "produce information to the White House and the world." Search for any findings released since April 20, 2026.
- [ ] **Daily Mail articles** — Original source for Garcia KCNSC employment claim and a key narrative originator for international coverage. Prior searches returned nothing; retry with fresh queries.
- [ ] **BBC coverage** — Absence noted but unconfirmed. One more targeted search to close the gap or confirm the absence.
- [ ] **T1 sources that returned HTTP 403** — BCSO press release PDF, House Oversight press release page. May now be accessible. Retry fetches.

## Formatting fixes (no research needed)

- [ ] **Reza case file** — Add missing section headers: inclusion rationale, named expert commentary, foreign coverage (WION India covered this case).
- [ ] **Hicks case file** — Add inline tier/confidence tags to narrative prose.
- [ ] **Maiwald case file** — Same as Hicks.
- [ ] **Grillmair case file** — Add explicit Documented/Reported/Alleged/Speculated section header (substance already inline).

## Significant gaps (harder to fill)

- [ ] **Base-rate actuarial analysis** — Compare observed rate (11 events, ~4-year window) against expected rate for the combined defense/aerospace workforce (~30k+ across LANL, JPL, Sandia, KCNSC, etc.). Most important analytical gap. May require workforce demographic data that isn't freely public.
- [ ] **Non-English foreign coverage** — Search TASS, Xinhua, Press TV, NHK, Al Jazeera, Le Monde, Der Spiegel, Haaretz in native languages. Only English-language editions were searched in prompt-001.
- [ ] **Reza-McCasland professional connection** — WION flagged a "Mondaloy connection." Both touched the AFRL ecosystem. No documented link found yet. Patent co-author networks, conference proceedings, or AFRL contract records might surface something.

## Cannot fill with open-source research

- Classified program overlap between subjects (only FBI/DOE/DOD can address)
- Inter-case social network analysis from phone/email records
- Cell phone forensic results for Reza (LASD has not released)
- McCasland USAF sweatshirt forensic results (pending)
- Hicks and Maiwald autopsy status (LA County ME has not confirmed or denied)




- can we get around the above?
- make the prompt resuable in such a way as to update the research. also ask if i can put that on an automatic clock to the deployed website for updated research every day?

## Automated Trigger
- [ ] **Set up a scheduled Claude Code trigger** to run prompt-004 (maintenance/update) on a daily or weekly cron. Should: check for new developments (House Oversight findings, FBI updates, new cases, case resolutions), update research artifacts, bump version, and flag if PDFs/website need regeneration. Needs: a trigger prompt adapted from prompt-004 that runs non-interactively and commits results. Consider whether to also auto-rebuild the website (`npm run build` in mattnoth-dev) or just flag it for manual rebuild.

## Website — Timeline Improvement
- [ ] Better layout and spacing — current visualization is too basic
- [ ] More readable event labels and descriptions
- [ ] Improved zoom/scroll UX
- [ ] Better mobile experience (consider vertical layout for mobile)
- [ ] Group overlapping events more clearly
- [ ] Add more context events (media milestones, congressional actions)

## Website — Diagram Enrichment
The connection diagram needs significantly more data to match the richness of the research:
- [ ] Add more specific locations (Los Alamos neighborhoods, specific trails, specific addresses)
- [ ] Add specific projects/programs (DART, NEAT, Dawn for Hicks; Mondaloy for Reza; PSFC fusion programs for Loureiro; SAPs for McCasland)
- [ ] Expand speculative/corkboard layer — research contains extensive speculation analysis not yet visualized
- [ ] Add behavioral pattern nodes (left without belongings, undisclosed cause of death)
- [ ] Consider temporal proximity edges (events close in time)
- [ ] Current: 34 nodes / 44 edges — research supports significantly more

## Website — Diagram Interactivity & Animations
- [ ] Make graph nodes clickable (navigate to relevant case or detail)
- [ ] Add more cool animations to the diagram (transitions, hover effects, edge pulses, etc.)

## Website — UFO/UAP Section
- [ ] Create a dedicated page or section focused on UFO/UAP/alien theories and these scientists' connections to that world
- [ ] Make it prominent in the site navigation (not buried)
- [ ] Collect and link evidence tying cases to UAP-related programs, congressional hearings, whistleblower claims, etc.
- [ ] Include outbound links to key UAP sources (congressional testimony, AARO reports, Grusch claims, etc.)

## Website — Diagram Styles
- [ ] Experiment with a traditional corkboard-style diagram (straight lines, pinned cards, string connections) as an additional view alongside the existing force-directed graph
- [ ] Try other diagram layout styles (hierarchical, radial, etc.) to see what communicates the connections best

## Website — UI Polish
- [ ] Change the question mark icon
