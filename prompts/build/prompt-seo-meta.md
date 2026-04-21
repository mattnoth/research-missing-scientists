# Prompt SEO-Meta — Per-Page Meta Tags, FAQ Page, Structured Data, and Sitemap Prep

## Non-interactive execution (read first)

This prompt runs via `claude -p --output-format=stream-json` — print mode. There is no stdin. Make decisions autonomously per the spec. Log ambiguities in `logs/research-log.md` and proceed.

You are Claude Code. For this prompt only, you may operate in **both**:
- `/Users/mnoth/source/research-missing-scientists/` (read-only — research source of truth)
- `/Users/mnoth/source/mattnoth-dev/` (read/write — the website)

## Hard Safety Rules

- **Working directories are the two listed above. Nothing else.**
- **Research repo is read-only.** Do not modify it.
- **No sudo. No system-wide installs.**
- **No framework installs.** Vanilla TypeScript and CSS only. The project uses esbuild, marked, and gray-matter.
- **Branch workflow:** Create a feature branch (`feature/seo-meta`) in the website repo. Commit there. Merge to `main` locally when verified. **Do not push** — the user pushes.
- **No git remote operations. No authentication.**
- **No contacting anyone.**

## Alignment (read `prompts/research/README.md` § "Alignment rules" before starting)

This prompt does not change research content. It changes how the website presents metadata to search engines and social sharing. All factual claims in meta descriptions, FAQ answers, and structured data must accurately reflect the research artifacts — do not editorialize, sensationalize, or overstate conclusions.

## Current State

The website's missing-scientists section (`/unpublished/missing-scientists/`) already has:
- ✅ `<title>` tags on every page
- ✅ `<meta name="description">` on every page
- ✅ Open Graph tags (og:title, og:description, og:type, og:url, og:image, og:site_name)
- ✅ Twitter Card tags (twitter:card, twitter:title, twitter:description, twitter:image)
- ✅ JSON-LD on content pages (WebSite schema on landing, Article schema on case/analysis pages)
- ✅ Canonical URLs on every page
- ✅ `noindex, follow` robots directive (section is unpublished)
- ✅ Breadcrumb HTML navigation on case and analysis pages

What's missing or generic:
- ❌ Case page meta descriptions are all identical boilerplate ("Case file: {Name}. Part of the research dossier...")
- ❌ No FAQ page (high value for question-based search queries)
- ❌ No BreadcrumbList JSON-LD structured data (HTML breadcrumbs exist but aren't machine-readable)
- ❌ Missing-scientists pages excluded from sitemap.xml (by design, but needs prep for publication)
- ❌ All pages share one default OG image — no per-page or per-section images

The build system lives in `build/missing-scientists.ts` (~830 lines). Page templates are in `src/templates/`. SEO metadata is generated in TypeScript at build time, not in markdown frontmatter.

## Step 1 — Unique, Compelling Meta Descriptions

Replace the generic case page descriptions with unique, keyword-rich summaries for each of the 11 case pages. Each description should:
- Be under 160 characters
- Include the person's full name, their employer/role, and a distinguishing detail
- Use natural language that would match search queries
- Accurately reflect the case file content (read each case from the research repo)

**Examples of the target quality:**

| Page | Current | Target |
|------|---------|--------|
| Reza case | "Case file: Monica Reza. Part of the research dossier on deaths and disappearances of U.S. defense scientists." | "Monica Reza, JPL materials scientist and Mondaloy superalloy co-inventor, vanished hiking near Mt. Waterman in June 2025." |
| McCasland case | "Case file: William McCasland. Part of the research dossier on deaths and disappearances of U.S. defense scientists." | "Retired Air Force Maj. Gen. William McCasland, former AFRL commander, disappeared from his Albuquerque home in February 2026." |
| Grillmair case | "Case file: Carl Grillmair. Part of the research dossier on deaths and disappearances of U.S. defense scientists." | "Caltech astrophysicist Carl Grillmair was shot outside his Llano, CA home in February 2026. A suspect has been charged." |

Do the same for the analysis pages (connections, hypotheses, foreign-intel), sources, methodology, and transparency pages. The landing page description is already good.

Also update the `<title>` tags for case pages to include more context. Current format is `"{Name} — Research — Matt Noth"`. Target format: `"{Name} | {Role/Employer} — Missing Scientists Research"`. Keep under 60 characters where possible.

Implementation: modify `build/missing-scientists.ts` where `generateCasePages()` and other generators set the title/description slots. You'll likely need to add a metadata map keyed by slug.

## Step 2 — FAQ Page

Create a new FAQ page at `/unpublished/missing-scientists/faq/index.html`.

**Target search queries** (from TODO-research.md):
- "Why are so many scientists dying?"
- "What happened to scientists at Los Alamos?"
- "Missing scientists 2024 2025"
- "Dead scientists government labs"
- "Scientists disappearing"

**Structure the FAQ using the research repo's actual findings.** Each Q&A must be factually grounded in the dossier — do not speculate or sensationalize. The FAQ should:

1. **What is this research about?** — Brief overview of the 11 cases and the federal review.
2. **Who are the missing and dead scientists?** — Summary table linking to each case page.
3. **Are these deaths and disappearances connected?** — Summarize the connection analysis findings: no documented inter-case connections, no common method, geographic/temporal clustering explained by institutional geography.
4. **What did the FBI investigation find?** — Summarize known status: investigation confirmed, no public findings yet, DOE Secretary said "not alarming yet."
5. **Is this a foreign intelligence operation?** — Summarize the foreign-intel analysis: experts divided, nuclear security analysts say strategic rationale is weak, no agency has indicated foreign involvement.
6. **What is the UAP/UFO connection?** — Only McCasland has a documented connection (DeLonge email); it's narrower than public perception. Be precise.
7. **Which cases have been solved?** — Grillmair (named suspect), Loureiro (named suspect + confession), Thomas (no foul play), Eskridge (ruled suicide).
8. **Which cases remain unexplained?** — McCasland, Reza, Chavez, Casias, Garcia. Briefly note what makes each unusual.
9. **What is the source methodology?** — Brief explanation of the tier system and confidence ratings, linking to the methodology page.
10. **How can I contribute?** — Point to the research repo (when public) and note the no-contact policy.

**Add FAQPage JSON-LD structured data** to this page using the [schema.org/FAQPage](https://schema.org/FAQPage) spec. Each Question/Answer pair should be a separate `mainEntity` item.

**Navigation:** Add the FAQ to the section navigation alongside the existing pages (between "Methodology" and "Transparency" seems natural, or wherever the existing nav ordering makes sense).

**Style:** Match the existing page styles. Use `<details>/<summary>` for the accordions if other pages use them, otherwise use the same content-block pattern as the methodology page.

## Step 3 — BreadcrumbList Structured Data

Add [BreadcrumbList](https://schema.org/BreadcrumbList) JSON-LD to every missing-scientists page that has breadcrumb HTML navigation. The structured data should match the visible breadcrumb trail.

**Example for a case page:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://mattnoth.dev/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Missing Scientists Research",
      "item": "https://mattnoth.dev/unpublished/missing-scientists/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Monica Reza",
      "item": "https://mattnoth.dev/unpublished/missing-scientists/cases/reza/"
    }
  ]
}
```

Implementation: extend the existing breadcrumb generation logic in `build/missing-scientists.ts` to also emit a `<script type="application/ld+json">` block alongside the breadcrumb HTML.

## Step 4 — Sitemap Preparation

The missing-scientists pages are currently excluded from `sitemap.xml` because they're `noindex`. Prepare for publication by:

1. **Add a conditional sitemap generator** in `build/sitemap.ts` (or `build/missing-scientists.ts`) that can include missing-scientists URLs when a flag/env variable is set. Don't flip it on yet — just wire it up so the user can enable it later.
2. **Add `lastmod` dates** derived from the research repo's CHANGELOG.md or git history.
3. **Set appropriate `changefreq` and `priority`** — the landing page and case pages are highest priority; FAQ and methodology are lower.

## Step 5 — robots.txt Prep (Optional)

If the site has a `robots.txt`, check that it doesn't block the missing-scientists section from crawlers once the `noindex` is removed. If there's a `Disallow: /unpublished/` rule, note it in the commit message so the user knows to update it at publication time.

## Step 6 — Verify and Commit

1. Run the build (`npm run build` or equivalent).
2. Spot-check the generated HTML for at least 3 case pages, the landing page, the FAQ page, and one analysis page. Verify:
   - Unique title and description per page
   - Valid JSON-LD (paste into a JSON validator or just eyeball the structure)
   - BreadcrumbList JSON-LD present alongside breadcrumb HTML
   - FAQ page renders correctly with FAQPage JSON-LD
   - No broken navigation links
3. Commit to the feature branch with a clear message.
4. Merge to `main` locally. **Do not push.**

## Step 7 — Update Research Repo TODO

After verifying the website changes, note in `/Users/mnoth/source/research-missing-scientists/logs/research-log.md` that the SEO-meta prompt was run, what it produced, and any issues encountered. (This is the only write permitted to the research repo.)

**Exception to read-only rule:** You may also update `TODO-research.md` to check off completed items under "Head / Meta Tags" and "Keywords & Search Visibility".
