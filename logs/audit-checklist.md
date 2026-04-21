# Audit Checklist — Derived from prompt-001.md

Extracted 2026-04-21 during reconcile session. This defines what "complete" means for each artifact.

---

## 1. Required sections in each `cases/<case>.md`

Per prompt-001 "Artifact specifications → `cases/{slug}.md`":

1. **Slug and title**
2. **Status** (Missing / Deceased — circumstances / Deceased — suspect apprehended / etc.)
3. **Key dates** (last seen, reported missing, body found, death date, etc.)
4. **Location(s)**
5. **Affiliation and role** (with confidence ratings per claim)
6. **Inclusion rationale** (why this case is in the repository; strong / weak fit)
7. **Narrative of known facts** (paragraph prose, every factual claim tagged with tier and confidence rating)
8. **What is documented vs. reported vs. alleged vs. speculated** (clearly separated sections or inline labels)
9. **Primary sources** (links to Tier 1 documents in `appendices/primary-sources/{slug}/`)
10. **Secondary sources** (links only)
11. **Named expert commentary** (if any, with link to `appendices/named-expert-commentary/`)
12. **Foreign coverage** (if any, with link and origin/orientation note)
13. **Contradictions** (source-to-source disagreements, cross-ref to `logs/contradictions.md`)
14. **Open questions** (what the case research could not resolve)

**Interpretation notes:**
- "Tier and confidence rating" means inline markers like `(T1, confirmed)` or `[Tier 3, reported]` on factual claims in the narrative.
- "Clearly separated sections or inline labels" for documented/reported/alleged/speculated — either discrete headings or consistent inline tagging satisfies this.
- Not every case will have named expert commentary or foreign coverage; their absence is acceptable if noted.

## 2. Required sections in `dossier.md`

Per prompt-001 "Artifact specifications → `dossier.md`":

1. **Abstract** (200–400 words) — written last, summarizes findings, neutral register
2. **Executive summary** (800–1500 words) — written last, main findings, hypothesis evaluations, open questions
3. **Methodology reference** — short, points to README
4. **Case index** — table with: name, status, date of incident, location, affiliation, inclusion rationale, link to `cases/{slug}.md`
5. **Connection analysis summary** — short version, points to `analysis/connection-analysis.md`
6. **Hypothesis evaluation summary** — short version, points to `analysis/hypotheses.md`
7. **Open questions and known unknowns** — points to `logs/known-unknowns.md`

## 3. Required contents of analysis files

### `analysis/connection-analysis.md`
- Three layers clearly labeled: **Tight**, **Medium**, **Corkboard**
- Every connection cited to a specific source
- Every connection carries a confidence rating
- Explicit about what is documented / inferred / speculated

### `analysis/hypotheses.md`
- Each hypothesis (H1–H9 minimum) gets:
  - Statement of the hypothesis
  - Evidence that would support it
  - Evidence that would contradict it
  - What the research found (evidence for, evidence against)
  - Current assessment (supported / partially supported / not supported / indeterminate — with reasoning)

### `analysis/foreign-intel-layer.md`
- Historical precedent for state-actor targeting of defense scientists
- Specific case evidence for each relevant state actor
- Assessment by named experts with credential context
- Open questions
- Explicit neutrality statement

## 4. Required schema, fields, and coverage in data JSON files

### `data/diagram-data.json`
- **Nodes**: people (all 11 cases), institutions, programs, events, locations. Each with: id, label, type, metadata (affiliations, dates, URLs).
- **Edges**: connections. Each with: source id, target id, edge_type (employment / funding / research-domain / geography / speculative-UAP / speculative-intel / other), layer (tight / medium / corkboard), confidence rating, evidence pointer, label.
- **Layer metadata**: what each layer contains and how it's rendered.
- Schema defined in `data/schema/diagram-schema.json`.

### `data/timeline-data.json`
- **Events**: each with: id, date, type (disappearance / death / investigation_milestone / institutional_statement / political_event), subject (case slug), description, source_pointer, confidence_rating.
- **Context events**: non-case events providing context.
- Schema defined in `data/schema/timeline-schema.json`.

## 5. Required appendix coverage

### Per-case primary sources (`appendices/primary-sources/<case>/`)
- Each file: source URL, access date, publisher/author, document type, date of document, text/excerpt
- **Minimum threshold**: prompt-001 does not set an explicit numeric minimum. Interpretation: at least 1 Tier 1 source per case, or documented explanation of why none exists. Cases with 0 files are a gap.

### `appendices/foreign-coverage/`
- One file per country with meaningful coverage
- Each file: country, outlet(s), outlet orientation, coverage summary, how it differs from U.S. reporting

### `appendices/named-expert-commentary/`
- One file per named expert
- Each file: name, credentials, professional history, on-the-record statements (with source/date), relevance assessment, documented conflicts of interest

## 6. Minimum evidence thresholds

Prompt-001 does not set explicit numeric thresholds. Interpretations:
- **Primary sources per case**: ≥1 Tier 1 source per case, or documented explanation. No hard numeric minimum.
- **Foreign-language sources**: the spec says "where relevant" for foreign coverage. English-language foreign coverage satisfies the spec; non-English is flagged as a known unknown.
- **Search budget**: "roughly 8–12 attempts at Tier 1 sources, 5–10 at Tier 3/4" per case. This is guidance, not a hard minimum. Under-sourcing should be "reported honestly."

## 7. Additional required artifacts

- `STATUS.md` — "A final STATUS.md file at the repo root summarizes: what was produced, what was skipped and why, how long it took, and any flags for the user to review before running prompt 002"
- `CHANGELOG.md` — "Initial entry: v0.1.0 — Initial research complete. Dated."
- `README.md` — expanded from prompt-000 skeleton with navigation guide, source tier legend, confidence rating legend, repository structure
