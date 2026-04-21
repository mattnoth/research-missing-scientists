# Harness Install Prompt

**How to use this file:**

1. Drop `AGENT-HARNESS.md` into the target repo's root (or be ready to paste its contents inline when the prompt asks).

2. **Work in an isolated copy.** Run the install inside a fresh git worktree or a disposable container, so any surprise edits are trivially reversible:

   ```bash
   git worktree add ../<repo>-harness-install
   cd ../<repo>-harness-install
   ```

   This is the seatbelt for step 3. If the plan goes sideways, `git worktree remove` and you're back to where you started.

3. From the isolated copy, launch the Claude Code CLI with permission prompts disabled:

   ```bash
   claude --dangerously-skip-permissions
   ```

   This skips per-tool permission prompts so execution can run end-to-end without interruption. It is safe here because **Phases 1–3 are read-only** and **Phase 4 blocks on the literal token `APPROVED`** before any filesystem changes. The flag does not bypass the in-prompt approval gate.

   Do not run as root (the flag refuses).

4. Paste the entire prompt below — everything between the `<<<BEGIN PROMPT>>>` and `<<<END PROMPT>>>` fences, exclusive of the fences themselves — as your first message.

---

<<<BEGIN PROMPT>>>

You are installing the **Agent Harness** in this repo. The harness is a portable context-engineering pattern: a layer model, a session-close contract, and a bounded session ledger. The full spec is in `AGENT-HARNESS.md` (either already at the repo root, or provided alongside this prompt). **Read it now before proceeding.**

## Ground rules for this installation

1. **Preserve existing work.** If this repo already has any piece of the harness — a progress log, a rules directory, a `CLAUDE.md`, a session-close workflow, a knowledge folder, anything — the existing version is **authoritative**. Adapt the harness to match the vocabulary, paths, and formats already in use. Do not rename, do not restructure, do not "standardize" unless I explicitly approve it.

2. **Propose before editing.** Your job in this session is to **classify the repo state, produce a plan, and wait for my approval before making any filesystem changes.** Do not invoke Edit, Write, or any file-modifying Bash command until I reply with the literal token `APPROVED`. "Go", "yes", "ok", or a paraphrase do **not** count. If my reply is ambiguous, ask — do not assume.

3. **Be specific.** Every gap, conflict, and proposed change must cite actual paths that exist (or don't) in this repo. No generic advice.

4. **Don't invent structure.** If the spec suggests `workflows/` but this repo already uses `ops/` for the same role, keep `ops/`. Record the mapping in the adapter section of `CLAUDE.md`.

## Phase 1 — Discovery

Scan the repo and classify its state as one of:

- **Greenfield** — no `CLAUDE.md`, no `.claude/` directory, no `progress.md`, no harness-like structure. The repo might have a `README.md` and code, but nothing resembling agent scaffolding.

- **Partial / needs reconciliation** — some pieces exist with different names, locations, or formats. Examples: a `CLAUDE.md` that's too long or inlines stuff that should be path-scoped; a progress log with a different entry format; rules in a non-standard location like `.cursor/rules/` or `docs/agent/`; a knowledge folder that mixes cold reference with working notes.

- **Mature** — `CLAUDE.md`, `.claude/commands/end-session.md`, `progress.md`, and adapter values are already present and roughly conform to the spec. Minor gaps possible but the harness is clearly installed.

Report your classification with evidence. Look for (but don't limit yourself to) these signals:

- `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `AGENTS-PORTABLE.md` at the root.
- `.claude/` directory and its subdirs (`commands/`, `rules/`, `skills/`, `agents/`).
- `.cursor/rules/` or any other tool's rule directory.
- `progress.md`, `CHANGELOG.md`, `journal.md`, `sessions/`, or anything that smells like a session ledger.
- Folders that look like layer candidates: `knowledge/`, `docs/`, `notes/`, `extractions/`, `workflows/`, `ops/`, `inbox/`, `digests/`, `actionable/`, `todo/`, `meta/`.
- A `CONTEXT.md` or similar orientation file.

Output the classification as a short table: signal found → what layer/role it plays → whether it matches the spec.

## Phase 2 — Gap and conflict analysis

For the three required artifacts (`CLAUDE.md`, `.claude/commands/end-session.md`, `progress.md`), report:

- **Present and conforming** — exists and roughly matches the spec. No action needed.
- **Present but divergent** — exists but format/location/content differs from the spec. Describe the divergence specifically. Do **not** propose normalizing it unless the divergence causes a real problem (e.g. the existing progress log has no rotation mechanism, so it's unbounded). Preservation is the default.
- **Missing** — does not exist. Will need to be created.

For the optional extras (hot-routing file, `.claude/rules/`, knowledge/extractions/workflows/harness-meta directories), report the same three categories but treat "missing" as "not needed yet" unless the repo has content that's clearly homeless.

For the adapter slots (section 6 of the spec), report which slots already have a natural home in this repo and which don't. If the repo uses `ops/` where the spec says `workflows/`, call that out — the fix is an adapter-table entry, not a rename.

Flag any **conflicts**: places where the existing structure and the spec disagree in ways that matter (not just naming). Examples: a `progress.md` with 40 entries and no rotation; a `CLAUDE.md` that's 800 lines and slow to load; rules scoped to wrong paths.

## Phase 3 — Installation plan

Based on classification and gaps, produce a concrete plan:

**If greenfield:**

- Create `CLAUDE.md` at root (stub with adapter slots filled in based on what little you could infer from the repo; ask me to fill the rest).
- Create `.claude/commands/end-session.md` implementing sections 2 and 3 of the spec.
- Create `progress.md` at root with an empty Archives table header.
- Optionally create `AGENT-HARNESS.md` at root if it's not already there.
- List any directories you'd create lazily on first use (don't create them now).

**If partial / needs reconciliation:**

- For each existing piece: keep-as-is, or adapt-in-place (small additive changes only, preserving existing vocabulary).
- For each missing piece: create per the spec, using the existing repo's naming conventions.
- For each conflict that matters: describe the problem, propose a minimal fix, note the alternative of leaving it alone.
- Build the adapter table (section 6 of spec) using this repo's actual paths.

**If mature:**

- Report conformance.
- List any small gaps (e.g. "rotation threshold not documented in `CLAUDE.md`").
- Probably do nothing.

## Phase 4 — Wait

Stop here. Present the classification, the gap/conflict analysis, and the plan. Do not touch the filesystem. Do not call Edit, Write, or any file-modifying Bash command.

I will either:

- Reply with the literal token `APPROVED` → you execute the plan exactly as presented.
- Modify specific items → you update the plan and re-present, then wait again for `APPROVED`.
- Reject and iterate.

**Any reply that is not the literal token `APPROVED` keeps you in wait state.** "Go", "yes", "ok", "sounds good", or a paraphrase do not authorize execution. If you are unsure whether a reply counts, ask.

## After approval

Once I approve, execute the plan. For each file created or edited, show a brief diff or summary. When done, append the first `progress.md` entry documenting the harness installation itself — this is the first use of the session-close contract, and it should work.

Finally, recommend running `/end-session` at the close of this session to exercise the new command once.

## Guardrails

- **Never overwrite.** If a file exists and you need to change it, show me the change first.
- **Never delete** anything in Phase 3 — that's a Phase 4 action, and only after approval.
- **Never "clean up" the repo** beyond what's explicitly needed for the harness. If you see a mess in `src/` or stale files in `docs/`, leave them alone. The harness install is not a refactoring pass.
- **Never assume** a path exists because the spec mentions it. Verify with the filesystem.
- **Never collapse adapter slots to defaults** if the repo has its own answer. Map, don't rename.
- **When in doubt, ask** rather than guess.

Begin with Phase 1. Report what you find.

<<<END PROMPT>>>
