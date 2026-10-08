# Changelog

All notable changes to this research repository will be documented in this file.

## v0.2.0 — 2026-10-07/08 — General refresh

First general refresh since 2026-05-08 (window 2026-05-08 → 2026-10-07). Minor bump: one case status change plus new video tooling.

- **Tooling:** `scripts/snapshot-video.py` (yt-dlp + faster-whisper; ingest / search / channel; media gitignored, SHA-256 in manifest); RUNBOOK "Video snapshots". First captures: six Eskridge TikToks and the 2020 Rys/Sokol interview (archive.org, 3 h 15 m transcript). YouTube single-video ingest is blocked on the maintainer's network (open decision in TODO).
- **Research bundles:** `logs/news-refresh-2026-10-07-cross-case.md`, eleven `logs/{case}-news-refresh-2026-10-07.md`, `logs/eskridge-rys-sokol-transcript-notes-2026-10-07.md`, `logs/w1-video-discovery-2026-10-07.md`.
- **Status change:** Casias Missing → Deceased (remains found 2026-05-28; OMI manner undetermined).
- **Case files:** `## Update — 2026-10-07` blocks on all 11 (full blocks on casias, chavez, eskridge, grillmair, hicks, loureiro, mccasland; short blocks on garcia, maiwald, reza, thomas), with inline markers where earlier prose is superseded.
- **dossier.md:** markers on the abstract / executive-summary counts, the April 2026 "ongoing" and briefing-deadline lines, and the Casias / Hicks case-index rows; new Update block with restated counts.
- **Integrity logs:** new within-case and cross-case entries in `logs/contradictions.md`; case-specific re-check lines in `logs/known-unknowns.md` (cross-case section updated 2026-10-07).
- **Snapshot:** `archive/snapshots/2026-10-07-pre-refresh/` + tag `dossier-2026-10-07-pre-refresh`.

## v0.1.1 — 2026-04-21 — PDFs generated

- Generated main dossier PDF (`pdf-output/missing-scientists-dossier.pdf`) with cover page, TOC, all 11 case files, 3 analysis files, appendices, and methodology logs
- Generated 11 individual case PDFs (`pdf-output/cases/{slug}.pdf`) with per-case primary-source appendices
- Generated 3 connection diagram PDFs (`pdf-output/diagrams/`) at tight, medium, and corkboard layer levels
- Generated timeline PDF (`pdf-output/timeline.pdf`) with all case and context events
- Created `pdf-config/` with print CSS, metadata YAML, and build script
- Created `pdf-output/README.md` documenting all outputs

## 2026-04-21

- Reconciled interrupted prompt-001 artifacts (diagram-data.json, timeline-data.json, contradictions.md, known-unknowns.md)
- Created STATUS.md summarizing prompt-001 outputs and flags for prompt-002
- Added missing contradictions entries for Hicks and Maiwald to central contradictions log
- Fixed H4 assessment discrepancy between dossier.md and hypotheses.md
- Full completeness audit (see logs/audit-report.md)

## 2026-04-20

- Completed all prompt-001 research: 11 case files, 3 analysis files, dossier, appendices, data JSON
- Bootstrapped repository structure (prompt 000)
