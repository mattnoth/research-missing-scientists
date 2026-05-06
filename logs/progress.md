# Session Progress

Every agent session appends here — research, website, tooling, whatever. This is the single durable record of what happened across sessions. The research log (`research-log.md`) tracks research-specific detail; this file tracks everything at session level.

## 2026-05-06 — Session 1: Phase 0 decisions + multi-session plan

**What changed:**
- Walked through all 7 Phase 0 decisions in `SESSION-PLAN.md` one at a time; resolved values now encoded in the plan's Phase 0 table (replaced the "Default if unanswered" column with "Resolved value").
- No agents launched. No research-content edits. User explicitly scoped this session as decisions + planning only.
- Revised `SESSION-PLAN.md`:
  - Phase 0 table → resolved values + new "Standing rules captured during this session" subsection
  - Phase 1 Agent A → added verify-don't-trust on every proposed URL + first-occurrence-only link discipline + redundant-link flagging
  - Phase 1 Agent B → expanded scope to 4 specific checks including over-linking flag
  - Phase 2 (Agent F) → added subjective-characterization-from-interested-parties pattern with the wife/McCasland concrete example
  - Phase 3 → added "design scope" caveat encouraging richer-than-baseline options
  - Phase 4 worldwide sweep → added W-6 (Japanese) and W-7 (Korean); W-8 is now the indie/aggregator thread
  - Phase 6 Step A → restructured as hybrid triage (source-weakness + new-material density in single pass)
  - "Next-session execution order" → expanded from 5 sessions to 8+, splitting audit/cleanup, voice-audit/voice-commit, and acknowledging tooling likely takes 2 sessions
- Captured 4 new standing rules to memory (`~/.claude/projects/-Users-mnoth-source-research-missing-scientists/memory/`):
  - `feedback_enrichment_priority.md` — enrichment of names/sources/acronyms is editorial baseline, not cleanup
  - `feedback_link_verification.md` — every URL must be loaded and confirmed before adding (no plausible-looking guesses)
  - `feedback_link_discipline.md` — first-mention-per-file gets the link; subsequent mentions are bare acronym
  - `feedback_archival_scope.md` — Phase 3 archival tooling not capped by scratch.txt's baseline; surface richer options
- `MEMORY.md` index updated with 4 new entries.
- No commits yet — held pending user direction (pre-existing prompts/build reorganization in working tree predates this session and is untouched).

**Further work:**
- Session 2: launch Phase 1's 5 parallel read-only agents (A–E). Findings only, no edits.
- Session 3: review Phase 1 findings, tag `pre-rebalance-2026-05-06`, single cleanup commit, push tag.
- Decision 1 (timeline alternation bug) and Decision 7 (abstract scroll-up) → mattnoth-dev session, separate from research repo work.
- `scratch.txt` open items section is now partially obsolete (most `→` prompts resolved). Worth a tidy pass to mark resolved items with pointers to where decisions landed — deferred unless user prioritizes.

## 2026-04-21 — Mobile timeline + abbreviation tooltips

**What changed:**
- `mattnoth-dev`: Replaced native browser `<abbr title>` tooltips with custom CSS tooltips (`data-tooltip` + `::after`). Accent-colored underline, no more question-mark cursor.
- `mattnoth-dev`: Added mobile-responsive timeline — single-column layout for screens < 600px, left-aligned axis, full-width cards, touch tap-to-reveal tooltips.
- Files: `build/missing-scientists.ts`, `src/styles/missing-scientists.css`, `src/ts/modules/ms-timeline.ts`
- Committed and pushed as `42d3ea7` on mattnoth-dev main.

**Further work:**
- Mobile diagram view still needs attention (deferred — harder problem).
- Should visually test the timeline on actual mobile devices / browser devtools to confirm touch interactions work as expected.
- The abbreviation tooltip `white-space: nowrap` may clip long expansions on narrow screens — monitor and adjust if needed.
