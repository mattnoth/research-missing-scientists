# Agent Harness — Portable Context-Engineering Spec

A reusable pattern for giving a Claude Code agent durable memory, bounded context, and a repeatable session-close ritual across any project.

This file is the **specification**. It does not auto-load. `CLAUDE.md` references it and the agent reads it on demand (at session close, during installation, or when asked).

Live rules and commands that implement this spec live elsewhere:

- `CLAUDE.md` (repo root) — always loaded; small; points to this file and names the project's adapter values.
- `.claude/commands/end-session.md` — the `/end-session` slash command; implements the session-close contract below.
- `.claude/rules/*.md` — path-scoped warm rules (conventions, workflows).
- `progress.md` — append-only session ledger. `progress/archive-NNN.md` for rotated chunks.

---

## 1. Layer model

Every piece of context lives in one of four layers. The layer determines when it loads into the agent's context window.

| Layer | Load model | Typical location | Role |
|-------|------------|------------------|------|
| **Hot** | Every session, in full | `CLAUDE.md`; a small hot-routing file if needed | Conventions, "always do X," "where do I look for topic Y" |
| **Warm** | On demand (path-scoped, slash-command, or agent-triggered) | `.claude/rules/*.md`, `.claude/commands/*.md` | Workflows, query patterns, session-close checklist |
| **Cold** | Read when task demands it | `knowledge/`, `extractions/`, `workflows/`, `docs/` | Facts, procedures, reference material |
| **Supplementary** | Last resort, often gitignored | `inbox/`, `digests/`, raw dumps | Unverified input awaiting promotion to cold |

**Rules of thumb:**

- Keep `CLAUDE.md` under ~200 lines. It loads on every message; bloat costs tokens on every call and hurts instruction adherence.
- "Always do X" → hot. "When working on X, do Y" → warm, path-scoped. "Sometimes I need to know Z" → cold.
- The session-close contract is warm (it loads when `/end-session` fires), not hot.

---

## 2. Session-close contract

Every session must complete these checks before closing. They are **not optional**. Implemented by `/end-session`.

Checks are written as **roles**, not filenames. Each project's `CLAUDE.md` names the specific files that play each role (see section 6, Adapter).

### 2.1 Knowledge extraction

Decide whether the session produced durable value: confirmed behavior, root causes, gotchas, corrections, working queries, reusable snippets. If yes, extract to cold storage using the project's extraction format.

**Exclude** meta-discussion about the harness/repo itself — that's check 2.5.

### 2.2 Hot-routing maintenance

Update the hot-routing file(s) **only when meaning changed** — a new article to list, a new key concept, a broken pointer, a principle confirmed, contradicted, or refined. Bump `updated` when you do.

If nothing meaningful changed, do nothing. Do **not** bump dates "because a session happened."

### 2.3 Rule and command sync

If any `.claude/rules/*.md` or `.claude/commands/*.md` was created, updated, or deleted during the session, verify the change is consistent with `CLAUDE.md` (no duplication, no contradiction, references still valid).

### 2.4 Navigational files

If cold-storage articles were created, updated, or deleted, check index files for needed updates. Indexes rot silently; catch them at session close.

### 2.5 Harness meta

If the session produced insights about **how the harness itself** works or should evolve (layer model, routing, orchestration, token budgets, agent design), capture them in the harness-meta location — not mixed in with product/project knowledge.

This is the complement to 2.1: 2.1 excludes repo-meta chat; 2.5 captures it.

### 2.6 Operational patterns

Repeatable procedures, config, or environment setup not yet documented → workflows directory.

Routing question: *"Is this about the **project**, or about the **system that documents the project**?"* Project → cold knowledge. Harness/agent ops → workflows.

If a pattern is automatable, flag it as a candidate for a future slash command or subagent.

### 2.7 Progress log (mandatory)

**Append** a session summary to `progress.md`. Do not skip.

Format:

```
## YYYY-MM-DD — <brief description>

**What happened:**
- <specific bullet with file paths, ticket numbers, decisions>
- ...

**Key discoveries / decisions:** (optional)
- ...
```

Rules: concise but specific; include file paths and ticket numbers; skip meta-discussion unless it caused structural change; trivial sessions can be one line.

`progress.md` is the **append-only session ledger**. Continuity must not depend on vendor chat history retention.

### 2.8 Actionables hygiene

If any actionable/working-list files were touched:

- All items done → delete the file. No empty shells.
- Partial → remove completed checkboxes, leave open items, bump `updated`.
- Absorbed by another doc → delete the actionable, add a one-line pointer in the absorbing doc.

Actionables are **working material**, not permanent backlog.

---

## 3. Progress log rotation (hard gate)

**Problem this prevents:** Soft language ("when it gets long") leads to deferred rotation and bloated logs.

**Mandatory trigger:** At `/end-session`, count session entries in `progress.md`. If **more than 15**, rotate **immediately** before closing — not "next time."

**Rotation procedure:**

1. If ≤ 15 entries, skip.
2. Find the **10 oldest** entries by embedded date (not necessarily file order).
3. Create `progress/archive-NNN.md` (increment NNN from the highest existing archive).
4. Header: archive id, session range, date range, separator.
5. Move those 10 sessions into the archive.
6. Update the Archives table in `progress.md` header.
7. Verify the active file holds only the newer sessions and count is ≤ 16.

**Intent:** bounded file size, predictable archival structure, no silent drift.

---

## 4. Source-of-truth boundaries

Before you start using the harness, answer these questions for the project. The answers shape what belongs in cold storage vs. what should be fetched live.

1. **What is the live source of truth for code?** (this repo? sibling repos? a monorepo elsewhere?)
2. **What is the live source of truth for data?** (a warehouse? a MongoDB? none?)
3. **What is the live source of truth for tickets/specs?** (Jira? Linear? GitHub Issues? none?)
4. **What tribal knowledge does NOT live in any of the above?** → that's what the harness exists to hold.

**Anti-pattern:** maintaining huge static snapshots of things that live elsewhere (per-class dumps, per-table schemas frozen in markdown). They drift. Prefer live access + narrow cross-stack architectural docs.

**What's allowed to go stale:** nothing critical. If it's in the harness, it's curated and the session-close contract is what keeps it fresh.

---

## 5. Content pipeline

Rough flow for knowledge: **supplementary → extractions → cold knowledge** (with validation against live sources where applicable).

- **Supplementary** (inbox, digests): raw, unverified.
- **Extractions**: session-derived, extracted at 2.1, still somewhat raw but structured.
- **Cold knowledge**: validated, reviewed, indexed, referenced from the hot-routing file.

The session-close extraction step is the checkpoint that moves value from ephemeral chat → tracked repo artifact.

---

## 6. Adapter — project-specific values

Every project fills in these slots. The values live in `CLAUDE.md` so the agent sees them every session. The harness spec above stays generic.

| Slot | Example values | Notes |
|------|----------------|-------|
| **Hot-routing file(s)** | `meta-trigger-table.md`, `strategy.md`, or none if `CLAUDE.md` is enough | Optional for small projects |
| **Cold knowledge root** | `knowledge/`, `docs/`, `notes/` | Where validated facts live |
| **Extractions dir** | `extractions/`, `session-notes/` | Where 2.1 output goes |
| **Workflows dir** | `workflows/`, `ops/` | Where 2.6 output goes |
| **Harness-meta location** | `meta/`, root `HARNESS-NOTES.md`, or a `CONTEXT.md` section | Where 2.5 output goes |
| **Actionables dir** | `actionable/`, `todo/`, or skip if not used | Working lists |
| **Session ledger** | `progress.md` | Convention; don't rename without reason |
| **Archive dir** | `progress/` containing `archive-NNN.md` | Convention; don't rename without reason |
| **Rotation threshold** | 15 entries (archive 10) | Defaults shown; tune if needed |
| **Live sources** | (from section 4) | List in `CLAUDE.md` as a short bullet list |

---

## 7. The three artifacts that implement this spec

A correctly installed harness has these three things. The install prompt creates whichever are missing.

### 7.1 `CLAUDE.md` (repo root)

Always loaded. Small. Contains:

- One-line project description.
- Live sources (from section 4).
- Adapter slot values (from section 6).
- A pointer to `AGENT-HARNESS.md` for the full spec.
- A pointer to `.claude/commands/end-session.md` for the session-close checklist.
- Any project-specific conventions that truly need to load every session (style, language, "always use X").

Target length: under 200 lines. Shorter is better.

### 7.2 `.claude/commands/end-session.md`

The `/end-session` slash command. Implements the contract in section 2 and the rotation in section 3. Written as direct instructions to the agent — natural language, no YAML required beyond an optional `description:` frontmatter.

### 7.3 `progress.md` (repo root)

The session ledger. Starts with a header including an Archives table (empty initially). Entries appended at 2.7. Rotated per section 3.

**Optional extras** depending on project size:

- A hot-routing file (if `CLAUDE.md` alone doesn't cover routing).
- `.claude/rules/*.md` for path-scoped conventions.
- Cold knowledge, extractions, workflows, harness-meta directories (created lazily as content demands).

---

## 8. Failure modes to watch for

- **Deferred rotation.** Tighten language to "mandatory, before close." Don't say "when it feels long."
- **`CLAUDE.md` bloat.** Every line costs tokens on every message. Move path-specific stuff to `.claude/rules/`.
- **Indexes rotting.** The 2.4 check exists because indexes silently fall out of sync with the corpus.
- **Static snapshots of live data.** See section 4. Prefer live access + narrow curated docs.
- **Actionable files as permanent backlog.** 2.8 forces retirement.
- **Harness-meta mixed with project knowledge.** 2.5 separates them on purpose.
- **Relying on chat history for continuity.** The mandatory `progress.md` append exists specifically so this isn't needed.

---

*End of spec. Install via the install prompt; adapt per section 6; keep `CLAUDE.md` small; run `/end-session` religiously.*
