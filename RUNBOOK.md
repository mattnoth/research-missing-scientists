# Runbook — Missing Scientists Research Pipeline

This is a living-artifact research project. The pipeline is composed of five prompts (000–004), executed via Claude Code CLI.

## Prompts at a glance

### Build prompts (`prompts/build/`)

| Prompt | Purpose | Runs in chain? | Typical duration |
|---|---|---|---|
| `prompts/build/prompt-000.md` | Bootstrap: initialize git repo, create skeleton, write README stub | Yes | ~1 min |
| `prompts/build/prompt-001.md` | Main research: spawn sub-agents, populate case files, appendices, analysis, data JSON | Yes | ~1–2 hours |
| `prompts/build/prompt-002.md` | PDF generation (dossier, cases, diagrams, timeline) | Yes | ~10–20 min |
| `prompts/build/prompt-003.md` | Website integration in `/Users/mnoth/source/mattnoth-dev/` | Yes | ~30–60 min |
| `prompts/build/prompt-resume.md` | Resume after rate-limit interruption | Manual | Variable |
| `prompts/build/prompt-reconcile.md` | Audit interrupted prompt-001 for completeness | Manual | ~10 min |

### News update prompt (top-level)

| Prompt | Purpose | Runs in chain? | Typical duration |
|---|---|---|---|
| `prompt-004.md` | Maintenance / update — run manually when news surfaces | No (manual) | Variable |

### Deep research prompts (`prompts/research/`)

| Prompt | Purpose | Depends on | Typical duration |
|---|---|---|---|
| `prompt-deep-001.md` | Public records & primary source deep dive (11 sub-agents, 1 per case) | — | ~1–2 hours |
| `prompt-deep-002.md` | Professional networks: patents, publications, grants, associations (4 sub-agents) | — | ~1 hour |
| `prompt-deep-003.md` | Foreign-language & international source expansion (5 regional sub-agents) | — | ~1 hour |
| `prompt-deep-004.md` | Historical precedent & base-rate statistical analysis (3 sub-agents) | — | ~1 hour |
| `prompt-deep-005.md` | Integration, comparison & gap audit — updates analysis, data, dossier | 001–004 | ~30–60 min |

See `prompts/research/README.md` for alignment rules and execution details.

## Running the chain

### Full pipeline (fresh run)

```bash
cd /Users/mnoth/source/research-missing-scientists/
chmod +x run-all.sh    # first time only
./run-all.sh 2>&1 | tee run-all.log
```

### Output model

The script uses `claude -p --output-format=stream-json --verbose`, which emits every event — assistant text, thinking blocks, tool calls, tool results — as JSON. A `jq` filter in the script pretty-prints these to your terminal in real time with color coding:

- `[thinking]` (grey) — the agent's reasoning
- `[assistant]` (cyan) — text the agent generated
- `[tool: name]` (yellow) — tool invocations (web_search, bash, create_file, etc.)
- `[tool result]` (green) — what the tool returned (truncated to 500 chars for readability)
- `[done]` (magenta) — end-of-prompt summary

The **raw JSON** is always captured in `run-all-raw.log` regardless of terminal output. Useful for later analysis, debugging, or re-running the jq filter:

```bash
cat run-all-raw.log | jq -r 'select(.type=="assistant") | .message.content[] | select(.type=="text").text'
```

### Dependencies

- **`jq`** — strongly recommended for readable output. `brew install jq`. If missing, the script warns and falls back to raw JSON (still captured, just noisier in the terminal).
- **`claude`** — Claude Code CLI. `claude --version` should report a current version.

### One-liner equivalent (manual, no script)

```bash
cd /Users/mnoth/source/research-missing-scientists/ && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-000.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-002.md)" && \
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-003.md)"
```

(Without `jq` piping, you get raw JSON. Use the script for the filtered view.)

### Running a single prompt

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)"
```

Or with the same pretty-printing the script uses:

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/build/prompt-001.md)" | jq -r '
  select(.type != "system") |
  if .type == "assistant" then
    (.message.content // [])[] |
    if .type == "text" then "\n[assistant] " + .text
    elif .type == "thinking" then "\n[thinking] " + (.thinking // "")
    elif .type == "tool_use" then "\n[tool: " + .name + "] " + ((.input // {}) | tostring)
    else empty end
  elif .type == "user" then
    (.message.content // [])[] |
    if .type == "tool_result" then "\n[tool result] " + ((.content // "") | tostring)
    else empty end
  elif .type == "result" then "\n[done] " + (.result // "")
  else empty end
'
```

### Maintenance updates

```bash
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompt-004.md)"
```

### Deep research prompts

Run any of prompts deep-001 through deep-004 independently (any order), then run deep-005 to integrate:

```bash
# Example: run primary source deep dive
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/research/prompt-deep-001.md)"

# After all deep dives complete, integrate
claude -p --output-format=stream-json --verbose --dangerously-skip-permissions "$(cat prompts/research/prompt-deep-005.md)"
```

Pipe through `jq` as above if you want pretty output.

### Monitoring progress from another terminal

While the chain runs, a second terminal can watch progress directly via the repo filesystem — often more useful than scrolling output:

```bash
cd /Users/mnoth/source/research-missing-scientists

# Commits as they land
watch -n 5 'git log --oneline | head -15'

# The agent's own research log as it grows
tail -f logs/research-log.md

# Case files appearing
watch -n 10 'ls -la cases/'

# Everything at once (if you have `watch` and a wide terminal)
watch -n 5 'git log --oneline | head -5; echo; ls cases/ 2>/dev/null | wc -l | xargs echo "cases written:"; echo; tail -5 logs/research-log.md 2>/dev/null'
```

### Background run (close terminal, return later)

```bash
nohup ./run-all.sh > run-all.log 2>&1 &
echo "Started as PID $!"

# Watch anytime:
tail -f run-all.log
```

The `say "Research pipeline complete"` at the end speaks through your Mac speakers when done regardless of whether you're watching.

## Safety model

Every prompt follows the same hard rules:

- **Scope:** only the research repo (and `mattnoth-dev/` in prompt 003 only).
- **Pre-approved silent installs:** pandoc, weasyprint (via `brew`), d3 + @types/d3 and markdown-it (via `npm` local to `mattnoth-dev/`). Any other install requires the agent to stop and ask.
- **No `sudo`. Never.**
- **No git push.** Agents commit locally only. You push.
- **No contact attempts.** Agents do not email, message, submit forms, or reach out to any person, family, agency, or reporter.
- **No arbitrary network access** beyond Claude Code's web search/fetch tools, `git` local operations, and the pre-approved package managers.

If an agent is unsure whether an action is in scope, it stops and asks. In practice this should be rare — the prompts are designed to run unattended end-to-end.

## Prompt authoring permissions

Every prompt in the series may:
- **Alter downstream prompts** for correctness (missing context, structural conflicts, incorrect state assumptions). Never for stylistic preference.
- **Create new prompts** if a task decomposes better than the current structure. New prompts use logical numbering (e.g., `prompt-001a.md` for insertions, `prompt-005.md` for additions).

Every alteration and creation is logged in `logs/prompt-alterations.md` with filename, what changed, why, and date. When a new prompt enters the chain, the agent updates `run-all.sh` and this RUNBOOK to reflect the change. Review `logs/prompt-alterations.md` after every run to see what the agent decided.

## Reviewing the output

After the chain completes:

1. **`STATUS.md`** at the research repo root — read first. Summarizes what was produced, what was skipped, any flags for review.
2. **`CHANGELOG.md`** — version history.
3. **`logs/research-log.md`** — chronological log of what sub-agents searched and found, including dead ends.
4. **`logs/contradictions.md`** — tracked source-to-source disagreements.
5. **`logs/known-unknowns.md`** — gaps the research could not resolve, with specificity.
6. **`dossier.md`** — the main artifact. Start with the abstract and executive summary.
7. **`pdf-output/`** — generated PDFs (dossier, per-case, diagrams, timeline).
8. **Website:** check out the `feature/missing-scientists` branch in `mattnoth-dev/` (now merged to main, not pushed). Build and view locally.

## Pushing the website

Prompts do not push. When you're satisfied with the website:

```bash
cd /Users/mnoth/source/mattnoth-dev/
git status              # confirm you're on main with the merge
git log --oneline -5    # confirm the feature branch merge is there
git push origin main    # push when ready
```

## Regenerating after updates

If you run `prompt-004.md` and it changes the research:

- **PDFs are out of date:** run `prompt-002.md`.
- **Website is out of date:** run `prompt-003.md`.

Prompt 004 will ask whether to regenerate these. You can say yes/no case by case.

## Historical preservation

Readers without git skills should be able to see what the dossier said at past points in time and how its framing evolved. Two layers handle this:

- **Inline preservation** (per-file): top-of-file `*Last revised: YYYY-MM-DD*` line + inline `*(updated YYYY-MM-DD — see GitHub for details)*` markers + `## Update — YYYY-MM-DD` blocks. Original prose is never deleted. See SESSION-PLAN.md "Append, don't overwrite" for the full convention.
- **Whole-dossier snapshots** (this section): a date-stamped copy of the synthesis files at major-revision moments, plus a git tag and an entry in [archive/HISTORY.md](archive/HISTORY.md).

### Tag-and-push convention

Any session that ships a substantive content or framing change tags HEAD before the change-set commit and pushes the tag:

```bash
git tag dossier-YYYY-MM-DD-<short-label>
git push origin dossier-YYYY-MM-DD-<short-label>
```

`<short-label>`: 1–3 hyphenated lowercase words (`pre-rebalance`, `xfiles-reframe`, `eskridge-update`, `phase1-cleanup`, `huntsville-pass`). The tag captures the state *before* the change lands, so the named version recovers cleanly with `git checkout dossier-YYYY-MM-DD-<short-label>`.

### When to take a full snapshot

Snapshot — i.e., copy synthesis files into `archive/snapshots/<date-label>/` *and* tag — at moments like:

- Banner / project-purpose / disclosure changes that alter how a reader interprets the whole dossier.
- Voice or framing rewrites (e.g., conclusion-neutrality pass, X-Files / Evidence-for-against rebalance).
- Phase-completion commits that ship a coherent revised state (Phase 1 cleanup, Phase 2 voice, Phase 3 tooling integration, etc.).
- Any time the editorial frame of `dossier.md` or `analysis/*.md` shifts in a way that future readers should be able to compare to.

Do **not** snapshot for: typo fixes, single-source updates, log-only commits, mechanical reformatting, ephemeral session-state changes.

### Snapshot file scope

Each snapshot directory contains four files only:

- `dossier.md`
- `analysis/hypotheses.md`
- `analysis/connection-analysis.md`
- `analysis/foreign-intel-layer.md`

**Not** the 11 case files — they have their own inline-history markers and snapshotting all of them on every checkpoint bloats the repo. **Not** the JSON data — git history covers those.

Each copied file gets a one-line banner prepended (above the H1):

```markdown
*Snapshot YYYY-MM-DD. Current: [<filename>](<relative-path-to-live>). Tag: [<tag-name>](<github-tag-url>).*

---
```

Relative paths from the snapshot location to the live file:
- `archive/snapshots/<date>/dossier.md` → `../../../dossier.md` (3 levels up)
- `archive/snapshots/<date>/analysis/<file>.md` → `../../../../analysis/<file>.md` (4 levels up)

Snapshots are **read-only after creation**. Never edit a snapshot file. If you want a different captured state, take a new snapshot under a new date-label directory.

### `archive/HISTORY.md` maintenance

Newest at top. One section per checkpoint: H2 with `YYYY-MM-DD — <short-label>`, one descriptive (not editorial) sentence, snapshot link if applicable, tag link. Format is descriptive (what changed substantively) — never editorial ("we used to do X but realized X was wrong"). Retroactive entries link the tag only and note `(No snapshot — recoverable via git tag.)`.

### Commit / tag / push ordering for snapshot sessions

The tag must point at HEAD *before* the snapshot commit lands, otherwise the tag captures the state-with-archive-tooling rather than the genuinely-pre-change state.

```bash
# 1. Tag HEAD before any new commits
git tag dossier-YYYY-MM-DD-<label>

# 2. Take the snapshot (copy synthesis files, prepend banners), update HISTORY.md
# 3. Commit the archive changes
git add archive/ NAVIGATION.md RUNBOOK.md   # plus any other files touched in the session
git commit -m "..."

# 4. Push tag and commit
git push origin dossier-YYYY-MM-DD-<label>
git push origin main
```

### Submodule note

This research repo is a submodule of the `mattnoth-dev` website repo. Tracked content here flows through to the rendered site automatically. Snapshots are committed to git (not gitignored) so they appear on the website. Untracked snapshots disappear at session end — always `git add archive/snapshots/<date>/`.

## Video snapshots (Phase 3 — video leg)

[`scripts/snapshot-video.py`](scripts/snapshot-video.py) archives a TikTok / YouTube / archive.org / other yt-dlp-supported video as a research artifact and provides cookie-free discovery. First proof-of-concept 2026-07-05; built, documented and re-verified 2026-10-07. The web-page (Playwright) and Reddit legs of Phase 3 are **not** built yet — see `TODO-research.md` "Tooling".

### Setup (user site-packages, no sudo)

```bash
pip3 install --user -U --pre "yt-dlp[default,curl-cffi]" faster-whisper
brew install ffmpeg        # already present on the maintainer's machine
```

- Use the **nightly** (`--pre`). The 2026.08 stable release failed on TikTok ("Unexpected response from webpage request"); nightly 2026.09.27 works, with `curl_cffi` providing Chrome TLS impersonation.
- The `yt-dlp` CLI lands in `~/Library/Python/3.14/bin`, which is not on `PATH` by default. The script imports the module directly, so `PATH` does not matter; for ad-hoc use run `python3 -m yt_dlp …`.
- First Whisper run downloads the model into `~/.cache/huggingface/hub/` (`base.en` ≈ 141 MB).

### Commands

```bash
# Archive known URLs for a case (metadata + captions/Whisper transcript + thumbnail + audio + manifest)
python3 scripts/snapshot-video.py ingest --case eskridge "https://www.tiktok.com/@user/video/123" [URL …] --note "why it matters"

# Discover candidates on YouTube — any language, no API key, no login
python3 scripts/snapshot-video.py search "Amy Eskridge scientist" --n 15
python3 scripts/snapshot-video.py search "美国 科学家 失踪 死亡 2026" --n 15

# Enumerate a creator's catalogue
python3 scripts/snapshot-video.py channel "https://www.youtube.com/@PopCrimeTV/videos" --n 50
```

Options: `--model small|medium|large-v3` (default `base.en`), `--no-transcribe`, `--audio-only`, `--max-height 720`, `--refetch-media`, `--force` (re-capture), `--cookies-from-browser brave|chrome|safari`, `--extractor-args …`.

### Layout and what is committed

```
appendices/primary-sources/<case>/snapshots/video/
  INDEX.md                                 one row per snapshot (committed)
  <upload-date>-<platform>-<id>/
    manifest.json                          provenance: URLs, uploader, dates, duration, counts,
                                           capture time, yt-dlp version, media SHA-256, transcript method
    info.json                              trimmed yt-dlp metadata
    transcript.txt                         from platform captions when present, else Whisper
    transcript.segments.json               timestamped segments (Whisper path)
    captions.<lang>.vtt                    platform captions when present
    thumbnail.*                            when available
    media.mp4 | media.m4a                  LOCAL ONLY — gitignored; hash recorded in manifest
```

**The footage is kept by default** (≤720p mp4; `--audio-only` for long audio-centric items; `--refetch-media` upgrades an existing audio-only snapshot to video without re-transcribing). Media stays out of git because a few dozen videos would bloat the repo and the public site copy; the committed manifest carries the SHA-256 so a re-fetched or restored file can be verified against the archived transcript. Until a durable off-repo store is chosen (TODO-research.md "Durable video storage"), the local disk is the archive — back it up.

### Platform status (verified 2026-10-07)

| Platform | Discovery | Ingest | Notes |
|---|---|---|---|
| TikTok | No search extractor. Use `WebSearch site:tiktok.com <terms>`, hashtag/discover pages, cross-posts on Reddit/X, creator enumeration, and user-curated URLs from in-app search. | **Works** (nightly + impersonation). | No platform captions → Whisper path. 78 s clip ≈ 6 s wall-clock on `base.en`. |
| YouTube | `search` (ytsearch) and `channel` **work**. | **Blocked on the maintainer's network** — "Sign in to confirm you're not a bot" for every player client, with the bgutil PO-token provider, and even in the desktop app's own browser pane on an unrelated video. This is IP-level, not a tooling gap. | Workarounds are a **user decision**: (a) `--cookies-from-browser brave|chrome|safari` (uses your own Google session; yt-dlp warns accounts can be rate-limited), (b) run from another network, (c) third-party caption relays are **not** a fallback right now — youtubetranscript.com returned a "YouTube is currently blocking us from fetching subtitles" stub on 2026-10-07. Already-captured KATV transcript (2026-07-05) predates the block. |
| archive.org | n/a | **Works.** | Preferred mirror for privated / removed YouTube uploads (e.g. `archive.org/details/youtube-HOtsZSzpnhI`). |
| Reddit-hosted (v.redd.it) | via Reddit thread URLs | Supported by yt-dlp; untested here. | |

### Relevance gate (mandatory before Whisper)

Whisper is the compute-heavy step: `base.en` runs ≈ 12× real time on the M4 Max CPU (a 3 h 15 m interview ≈ 15 min). Discover first, then gate on uploader, title, upload date, view count and whether the clip is a re-upload of outlet footage already in the dossier. Ingest only likely-relevant items; use `--no-transcribe` to archive metadata-only for marginal ones. **Non-English speech needs a multilingual model**: `--model small --language es` (the default `base.en` is English-only and emits noise on other languages — the Spanish @anderciencia clip had to be re-run).

### Citing a snapshot

Cite the original URL inline, then the local transcript: `[@newsnationnow TikTok](https://www.tiktok.com/@newsnationnow/video/7629859059788713229) ([local transcript](../appendices/primary-sources/eskridge/snapshots/video/20260417-tiktok-7629859059788713229/transcript.txt))`. Tier is assigned at citation time: independent creators T7; outlet-run accounts inherit the outlet's tier (a NewsNation TikTok is T4). Whisper output is a machine transcription — quote sparingly, tag `[Whisper transcript]`, and expect proper-noun misspellings (it renders Eskridge as "Escridge"). Uploader identifiers are kept as captured, including archive.org account e-mails (maintainer decision 2026-10-07: they are already public on the platform and are the mirror's provenance); use `--redact-uploader-email` only for a capture that needs it.

## Known limitations

- **Paywalled foreign coverage** (e.g., some major international outlets behind subscription walls): documented in `logs/known-unknowns.md`. The research does not bypass paywalls; it looks for syndicated reposts and notes when those are not available.
- **Claims requiring comment from named individuals or agencies:** never solicited. The research works only from already-public material.
- **Evolving investigations:** cases resolve, new cases surface, House Oversight will likely release findings. The `prompt-004.md` workflow handles updates; rerun it when material new information surfaces.

## Tips

- The `run-all.sh` script writes `run-all-raw.log` unconditionally — the raw stream-json from every prompt in the chain. This is your authoritative transcript. Add it to `.gitignore` if you don't want it tracked (it can get large).
- If running overnight, redirect pretty output to a log and run in background:
  ```bash
  nohup ./run-all.sh > run-all.log 2>&1 &
  ```
  Then `tail -f run-all.log` when you want to peek.
- If prompt 001 fails partway through, you can often re-invoke it — the prompt is designed to be idempotent for completed case files (sub-agents will see existing files and not redo them). Check `logs/research-log.md` first to confirm state. Alternatively, use `prompts/build/prompt-resume.md` or `prompts/build/prompt-reconcile.md`.
- **Re-reading the reasoning after a run:** the raw log preserves every thinking block, tool call, and tool result. You can grep it freely. For example, to see every `web_search` query the agent ran:
  ```bash
  jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use" and .name=="web_search") | .input.query' run-all-raw.log
  ```
  Or every file created:
  ```bash
  jq -r 'select(.type=="assistant") | .message.content[]? | select(.type=="tool_use" and .name=="create_file") | .input.path' run-all-raw.log
  ```
- The research repo is the source of truth. Website and PDFs are renderings. If you want to edit content, edit the markdown in the research repo, then regenerate — don't edit the PDFs or the website HTML directly.