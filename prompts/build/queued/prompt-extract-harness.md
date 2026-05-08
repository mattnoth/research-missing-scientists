# Extract the agent harness into a standalone tooling repo

**How to run:**

1. Create the target directory (empty):

   ```bash
   mkdir -p /Users/mnoth/source/ai-infra-tooling
   cd /Users/mnoth/source/ai-infra-tooling
   ```

2. Launch Claude Code with permission prompts disabled:

   ```bash
   claude --dangerously-skip-permissions
   ```

3. Paste everything between the `<<<BEGIN PROMPT>>>` and `<<<END PROMPT>>>` fences (exclusive) as the first message.

This prompt is **one-shot**: it executes end-to-end without an approval gate. All writes land under `/Users/mnoth/source/ai-infra-tooling/`. The source repo at `/Users/mnoth/source/research-missing-scientists/` is **read-only** — do not modify it.

---

<<<BEGIN PROMPT>>>

You are extracting the portable agent-harness pattern out of a research dossier repo and into its own reusable tooling repo. The goal is that someone (me or anyone else) can pull in just the pieces they need — the full harness, or only the session-close ledger, or only the routing-file pattern — without dragging along the research-specific content the harness currently lives alongside.

## Boundaries (read carefully)

- **Target directory:** `/Users/mnoth/source/ai-infra-tooling/` — assumed to exist and be empty. All writes go here.
- **Source directory:** `/Users/mnoth/source/research-missing-scientists/` — **read-only**. Read files here but never write, edit, or delete anything in this tree.
- **No git init.** Don't run `git init` in the target. The user will decide repo boundaries after reviewing.
- **No contact with the network.** Everything needed is on the local filesystem.
- **If you are uncertain** about how to split a concept, prefer **keeping it in the assembled `harness/` spec** and leaving the standalone module lean, rather than fragmenting content across multiple files.

## What to read first

Before writing anything, read these source files in full:

1. `/Users/mnoth/source/research-missing-scientists/AGENT-HARNESS.md` — the current assembled spec.
2. `/Users/mnoth/source/research-missing-scientists/INSTALL-PROMPT.md` — the current installer prompt.
3. `/Users/mnoth/source/research-missing-scientists/.claude/commands/end-session.md` — an *instance* of the session-close command, specialized for the research dossier. Useful as a concrete example; do not copy it wholesale.
4. `/Users/mnoth/source/research-missing-scientists/NAVIGATION.md` — an instance of an intent-keyed routing file (what the harness spec calls a "hot-routing file"). Useful as a concrete example.
5. `/Users/mnoth/source/research-missing-scientists/CLAUDE.md` — shows how adapter slots get filled in for a real project.
6. `/Users/mnoth/source/research-missing-scientists/logs/research-log.md` (first ~100 lines) — an instance of a session ledger (`progress.md` in harness vocabulary). Useful as a concrete example.

## Target structure

Create this layout under `/Users/mnoth/source/ai-infra-tooling/`:

```
ai-infra-tooling/
├── README.md
├── harness/
│   ├── README.md
│   ├── AGENT-HARNESS.md        # The assembled portable spec
│   └── INSTALL-PROMPT.md       # The installer prompt
├── progress-tracking/
│   ├── README.md
│   ├── session-close-contract.md
│   ├── end-session-command.template.md
│   └── progress-log.md         # The ledger pattern + rotation rule
├── trigger-table/
│   ├── README.md
│   ├── trigger-table.md        # Intent-keyed routing file pattern
│   └── topic-tables.md         # Per-topic pointer-table variant
└── strategy/
    ├── README.md
    ├── layer-model.md          # Hot / warm / cold / supplementary
    ├── source-of-truth-boundaries.md  # Pre-install diagnostic questions
    └── content-pipeline.md     # Supplementary → extractions → cold
```

Each top-level subdir is a **self-contained module**. A reader who pulls only `progress-tracking/` should get a usable pattern without needing to read the full harness spec (though links back to `harness/AGENT-HARNESS.md` are welcome for the integrated view).

## What goes where

**`harness/`** — the assembled, composed spec. This is the entry point for someone who wants the whole pattern.

- `AGENT-HARNESS.md`: copy `research-missing-scientists/AGENT-HARNESS.md` as-is. It is already written as a portable spec. If you notice any lingering project-specific assumptions while copying (there shouldn't be many — verify), note them in the subdir README rather than editing the spec in this pass.
- `INSTALL-PROMPT.md`: copy `research-missing-scientists/INSTALL-PROMPT.md` as-is. Same verification rule.
- `README.md`: one short page. State what the harness is, who it's for, how to install it (point at `INSTALL-PROMPT.md`), and how it relates to the other modules in this repo (each sibling module is a standalone extraction of one piece of the assembled spec).

**`progress-tracking/`** — the session-close contract plus the append-only ledger and rotation rule. This is the module someone pulls if they want durable session memory without adopting the full layer model.

- `session-close-contract.md`: extract sections 2.1 through 2.8 from the harness spec. Rewrite the preamble so it reads as a standalone document — don't reference "this spec" or "section X" of anything else. Keep the eight numbered checks. Make clear that each check is role-based (what the project's file plays the role, not a hardcoded filename).
- `end-session-command.template.md`: a genericized template for `.claude/commands/end-session.md`. Use the research repo's `end-session.md` as a *reference example* (not a template) — strip all research-domain vocabulary (cases, tiers, source tiering, appendices, etc.) and replace with role-based placeholders in `{braces}` that an installer fills in. Include a short "how to specialize this template" note at the top.
- `progress-log.md`: extract section 3 (rotation) plus 2.7 (append format) into one coherent document about the append-only ledger — what goes in it, format, rotation threshold and procedure, anti-patterns. Framed as a standalone pattern.
- `README.md`: what progress-tracking is, what problem it solves (continuity that doesn't depend on chat history retention), the three artifacts in this module and how they relate.

**`trigger-table/`** — the hot-routing-file pattern. The idea that a small top-level file can dispatch the agent to the right cold-storage location by intent keyword.

- `trigger-table.md`: describe the intent-keyed routing file pattern in the abstract. A trigger table maps "when the agent needs X, go to Y". Use `research-missing-scientists/NAVIGATION.md` as a concrete example (quote or summarize its shape; don't copy it verbatim — it's full of research-specific entries). Include guidance on when a trigger table is needed vs. when `CLAUDE.md` alone suffices.
- `topic-tables.md`: describe the per-topic variant — where trigger-table dispatches by *intent* ("where do I record a contradiction?"), a topic table dispatches by *subject* ("everything about Topic X lives here"). If the current harness spec doesn't distinguish these, do the distinction cleanly here and note it. Again, use concrete examples.
- `README.md`: explains the routing problem these files solve (keeping `CLAUDE.md` small while still making cold knowledge discoverable), when you want a trigger table, when you want topic tables, when you want both.

**`strategy/`** — the pre-install and ongoing diagnostic reasoning. This module is about the questions you answer to decide what belongs in the harness at all.

- `layer-model.md`: extract section 1 of the harness spec. Hot/warm/cold/supplementary, load model, rules of thumb. Frame as the foundational mental model for the whole kit.
- `source-of-truth-boundaries.md`: extract section 4. The four diagnostic questions (live source for code, data, tickets, tribal knowledge). The anti-pattern about static snapshots. What "allowed to go stale" means.
- `content-pipeline.md`: extract section 5. Supplementary → extractions → cold knowledge, with the 2.1 session-close step as the checkpoint. Frame as a pattern that stands alone.
- `README.md`: what strategy is for — these are the documents an installer reads *before* adopting the harness, and the mental models a maintainer returns to when deciding how to evolve it.

## Top-level `ai-infra-tooling/README.md`

One page. Includes:

- What this repo is (a kit of reusable AI-agent context-engineering patterns).
- The four modules and a one-sentence hook for each.
- How to install the full kit (→ `harness/INSTALL-PROMPT.md`).
- How to pull just one module (copy the subdir, follow its README).
- A note that each module originated as part of the assembled `harness/` spec, decomposed so downstream consumers can mix and match.
- A short "origins" line: extracted from a research-dossier project where this pattern was iterated in production. No link to the research repo — keep this kit content-neutral.

## Style rules

- **No emojis** anywhere.
- Match the existing harness voice: plain, declarative, specific. Not marketing copy.
- Prefer short sentences. No hedging filler ("it's worth noting that...").
- Code fences for file layouts, commands, and format templates. Tables where the harness spec already uses them.
- Do not add author names, dates, or version strings — this is a pattern library, not a publication.
- When a module's document duplicates text that also lives in `harness/AGENT-HARNESS.md`, that is **fine and expected**. Each module stands alone. Cross-link, don't deduplicate.

## Execution order

1. Read the six source files listed above.
2. Create the four subdirs under `/Users/mnoth/source/ai-infra-tooling/`.
3. Write the nine module files plus the five READMEs plus the top-level README (15 files total).
4. After all files are written, list the target tree with `find /Users/mnoth/source/ai-infra-tooling -type f | sort` and show it in the final report.
5. Final report: one paragraph summarizing what was created, any verification notes (e.g. "confirmed AGENT-HARNESS.md has no project-specific references"), and any recommendations for the user's next step (e.g. "after reviewing, consider removing `AGENT-HARNESS.md` and `INSTALL-PROMPT.md` from the research repo and replacing with a pointer to this kit").

Do not modify `/Users/mnoth/source/research-missing-scientists/` under any circumstance. Do not `git init` the target. Do not install dependencies. Do not create files outside the target tree.

Begin.

<<<END PROMPT>>>
