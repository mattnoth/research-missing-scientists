# Research Log

Chronological record of searches performed, sources consulted, and decisions made.

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
