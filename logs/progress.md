# Session Progress

Every agent session appends here — research, website, tooling, whatever. This is the single durable record of what happened across sessions. The research log (`research-log.md`) tracks research-specific detail; this file tracks everything at session level.

## 2026-05-08 — Historical preservation mechanism (design + implement)

**What changed:**
- New `archive/` tree with the first checkpoint snapshot under `archive/snapshots/2026-05-08-pre-rebalance/`. Contents: copies of `dossier.md`, `analysis/hypotheses.md`, `analysis/connection-analysis.md`, `analysis/foreign-intel-layer.md`, each with a verdict-free banner pointing back to the live file and the matching git tag. Snapshots are read-only after creation.
- `archive/HISTORY.md` — chronological index of dossier checkpoints, newest-at-top. Today's entry plus 5 retroactive entries: `repo-bootstrap` (2026-04-20), `dossier-complete` (2026-04-20), `tier8-migration` (2026-04-21), `crosslink-pass` (2026-04-21), `session-plan` (2026-05-06). Retroactive entries link the tag only — recoverable via `git checkout`.
- `NAVIGATION.md` — new "Historical snapshots" section pointing at `archive/HISTORY.md`.
- `RUNBOOK.md` — new "Historical preservation" section documenting the tag-and-push convention, when to take snapshots, snapshot file scope (synthesis files only — not the 11 case files, not the JSON), banner format, relative-path math, HISTORY.md maintenance, and commit/tag/push ordering.
- 6 git tags pushed under `dossier-YYYY-MM-DD-<label>` convention. The pre-rebalance tag points at the genuinely pre-archive HEAD so `git checkout dossier-2026-05-08-pre-rebalance` recovers the dossier without the archive infrastructure.
- One subagent fired: Sonnet Explore pass enumerating retroactive checkpoint candidates. Returned 8; trimmed to 5 after review (dropped same-day-as-bootstrap framework commit, mid-step case-research-start, and the renderer-only PDF pipeline commit).
- Push handling: encountered a non-fast-forward rejection — origin had `6846fc4` (authorship-clarification edit to `PROJECT-HISTORY.md` from 2026-04-22) that was not local. Rebased local 3 commits onto `6846fc4`, re-applied the 2 affected tags (`session-plan` and `pre-rebalance`) on the new SHAs. Other 4 retroactive tags unaffected (below the merge-base). Pushed main + 6 tags successfully.

**Further work:**
- Website-side rendering of the archive index (browseable HISTORY.md page, snapshot viewers) — separate `mattnoth-dev` session.
- Future substantive-revision sessions: follow the documented tag-and-snapshot convention. Next likely checkpoint: post-rebalance after the X-Files / Evidence-for-against framing pass lands.
- Pre-existing WIP in working tree (TODO-research.md modification + prompts/build/ reorganization into `completed/` and `queued/`) was untouched this session — those are the user's pre-existing in-progress work.

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
