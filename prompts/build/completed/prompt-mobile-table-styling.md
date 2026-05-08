# Prompt — Mobile table styling for the research dossier

Run this in the parent website repo:

```bash
cd /Users/mnoth/source/mattnoth-dev && claude "$(cat /Users/mnoth/source/research-missing-scientists/prompts/build/prompt-mobile-table-styling.md)"
```

---

## Task

Fix mobile rendering of wide markdown tables on `mattnoth.com/unpublished/missing-scientists/`. The rendered research pages (Connection Analysis, Hypothesis Summary, Case Index) overflow the viewport on phones because `src/styles/missing-scientists.css` has no `<table>` rules at all — tables inherit browser defaults and push past the 75ch prose width.

Plan file (for reference, not to be modified): `/Users/mnoth/.claude/plans/i-counted-incorrectly-the-nested-donut.md`.

## Branch

```bash
git checkout -b feat/ms-mobile-tables
```

## Change 1 — Wrap tables in a scroll container

File: `build/missing-scientists.ts`

Near the top of the file, after the `import { marked } from "marked"` line, add a renderer override so every `<table>` emitted from markdown is wrapped in `<div class="ms-table-wrap">`:

```ts
const msRenderer = new marked.Renderer();
const defaultTable = msRenderer.table.bind(msRenderer);
msRenderer.table = (header, body) =>
  `<div class="ms-table-wrap">${defaultTable(header, body)}</div>`;
marked.use({ renderer: msRenderer });
```

Check the `marked` version in `package.json` — the renderer API differs between marked v4 (positional args) and marked v5+ (single token arg). Adjust the signature to match. If marked ≥5, use:

```ts
msRenderer.table = ({ header, rows }) => {
  const inner = defaultTable.call(msRenderer, { header, rows });
  return `<div class="ms-table-wrap">${inner}</div>`;
};
```

Verify after build: `dist/unpublished/missing-scientists/analysis/connections/index.html` should contain `<div class="ms-table-wrap"><table>…</table></div>`.

## Change 2 — Add table CSS

File: `src/styles/missing-scientists.css`

Append inside the `@layer components { … }` block, before its closing brace (around line 847):

```css
  /* ── Tables (wrapped by renderer in build/missing-scientists.ts) ──── */
  .ms-table-wrap {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin-block: var(--space-md);
    border: 0.0625rem solid var(--color-border);
    border-radius: var(--radius-md);
  }

  .ms-prose .ms-table-wrap > table {
    inline-size: 100%;
    min-inline-size: max-content;
    border-collapse: collapse;
    font-size: var(--text-sm);
  }

  .ms-prose .ms-table-wrap :is(th, td) {
    padding: var(--space-xs) var(--space-sm);
    border-block-end: 0.0625rem solid var(--color-border);
    vertical-align: top;
    text-align: start;
    overflow-wrap: anywhere;
  }

  .ms-prose .ms-table-wrap th {
    font-weight: 600;
    background-color: color-mix(in oklch, var(--color-surface) 60%, transparent);
  }

  /* Case Index is the only 7-column table (dossier.md:68-80).
     Hide the "Case File" column under narrow viewports — the Name
     column already links to the case page. */
  @media (max-width: 37.5rem) {
    .ms-prose .ms-table-wrap table:has(th:nth-child(7)) :is(th, td):nth-child(7) {
      display: none;
    }
  }
```

## Verification

1. Build: `npm run build`
2. Grep the generated HTML for the wrapper to confirm the renderer fires:
   ```bash
   grep -l ms-table-wrap dist/unpublished/missing-scientists -r
   ```
3. Serve locally (check `package.json` scripts for `preview`/`serve`/`dev`).
4. Chrome DevTools → device mode → test at 375px (iPhone SE) and 393px (iPhone 14 Pro).
5. Visit and confirm on each page:
   - `/unpublished/missing-scientists/` — Case Index renders 6 columns on mobile (no "Case File"); Hypothesis Summary fits or scrolls internally.
   - `/unpublished/missing-scientists/analysis/connections/` — Institutional + Geographic tables scroll inside their wrappers, not at page level.
   - `/unpublished/missing-scientists/analysis/hypotheses/` — Hypothesis table scrolls cleanly.
6. At desktop widths (≥1024px), tables should render at normal width without triggering internal scroll.
7. Toggle dark mode — `color-mix` header background should still render correctly.

## Out of scope

- Timeline mobile polish (tracked in `research-missing-scientists/TODO-research.md:53-59`).
- Menu/hamburger overlap with page content — separate layout bug.
- Diagram mobile layout (deferred per `research-missing-scientists/logs/progress.md:13`).

## Commit & PR

Commit in two logical commits if clean:
1. `feat(ms): wrap rendered tables in scroll container`
2. `feat(ms): style wrapped tables and hide case-file column on mobile`

Then open a PR against `main` with screenshots at 375px and ≥1024px for each affected page.
