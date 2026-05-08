# Prompt — Mobile TOC overlay and vertical spacing tightening

Run this in the parent website repo:

```bash
cd /Users/mnoth/source/mattnoth-dev && claude "$(cat /Users/mnoth/source/research-missing-scientists/prompts/build/queued/prompt-mobile-toc-overlay.md)"
```

---

## Context

The missing-scientists pages (`/unpublished/missing-scientists/`) use a `<details open>` element for the Table of Contents. On desktop (≥64rem) this sits in a sticky sidebar via `.ms-toc` and works fine. On mobile it appears inline between the header and the prose, occupying significant vertical space and pushing the first content heading (e.g. "Abstract") far from the page title.

Additionally, the current `<details>` disclosure triangle doesn't align well and the expanded list just pushes content down rather than overlaying it.

## Goals

1. **Contents becomes a compact overlay trigger on mobile.** On viewports below 64rem:
   - The `<details>` summary ("Contents") should render as a compact inline element positioned directly beneath the page title / subtitle area, visually tucked under the header — not floating in whitespace.
   - The disclosure triangle should align cleanly with the summary text.
   - When opened, the TOC list should render as a **floating overlay / dropdown** that sits on top of page content (using `position: absolute` or `position: fixed` with appropriate z-index), not pushing content down.
   - The overlay should dismiss on: (a) clicking/tapping outside it, (b) selecting a TOC link, (c) tapping the summary again to close.
   - The overlay should have a subtle background (surface color + border), constrained to a reasonable max-height with overflow-y scroll if needed.

2. **Tighten vertical spacing between header and first content.** The gap between the page `<h1>` and the first prose heading (e.g. "Abstract") is too large on mobile. Reduce `margin-block-end` on `.ms-header` and any gap introduced by `.ms-toc` or `.ms-layout` so the first content heading sits closer to the title.

3. **Desktop behavior unchanged.** At ≥64rem the TOC remains a sticky sidebar in `.ms-layout` grid, always visible, `<details open>` with no overlay behavior.

## Implementation approach

### CSS changes (`src/styles/missing-scientists.css`)

Inside `@layer components`:

- On mobile (below 64rem), `.ms-toc` should:
  - Use `position: relative` as the positioning anchor for the dropdown.
  - Have minimal `margin-block` so it doesn't create a vertical gap.
- On mobile, `.ms-toc details[open] > ol` (or equivalent content container) should:
  - `position: absolute`
  - `z-index: 100` (or appropriate layer)
  - `background: var(--color-surface)` with border and border-radius
  - `max-block-size: 60vh` with `overflow-y: auto`
  - `inline-size: max(16rem, 80vw)` or similar to be readable but not full-width
  - `box-shadow` for depth
- `.ms-header` `margin-block-end` should be reduced (try `var(--space-sm)` instead of `var(--space-xl)`)
- `.ms-toc summary` should have clear, compact styling — consider aligning the disclosure triangle and text on a single tight line with `display: flex` or `list-style` adjustments.

### JS changes (light-dismiss behavior)

The overlay needs to close when clicking outside. Options:

**Option A — Minimal inline script in `build/missing-scientists.ts`:**
Add a small `<script>` block to the TOC HTML that adds a click-outside listener on the document. When `<details>` is open and a click lands outside `.ms-toc`, remove the `open` attribute. Also close on link click within the TOC.

**Option B — Module in `src/ts/`:**
If there's an existing MS interactive module, add the behavior there. Check `src/ts/` for any missing-scientists module before deciding.

Prefer Option A if the logic is under ~15 lines. This is a progressive enhancement — if JS fails, the `<details>` still works as a normal disclosure, just without light-dismiss.

### Build changes (`build/missing-scientists.ts`)

- The `toc` template string may need structural adjustments (e.g., wrapping the `<ol>` in an additional container div for positioning).
- Keep `<details open>` in the HTML — CSS and JS handle the mobile behavior.

## Verification

1. `npm run build` — must pass cleanly including lint-classes.
2. Dev server at `http://localhost:3001/unpublished/missing-scientists/` in Chrome DevTools device mode:
   - **375px (iPhone SE):** Contents appears as a compact trigger below the title. Tapping it opens a floating overlay with TOC links. Tapping a link scrolls to the section and closes the overlay. Tapping outside closes it. "Abstract" heading is close to the page title.
   - **393px (iPhone 14 Pro):** Same behavior.
   - **≥1024px desktop:** TOC is a sticky sidebar, always visible, no overlay behavior.
3. Dark mode: overlay background and borders render correctly.
4. Reduced motion: no transitions break.

## Out of scope

- Nav strip layout changes (already fixed to horizontal scroll in the mobile-tables branch).
- Page-level prose overflow (separate layout bug).
- Diagram or timeline mobile layout.
