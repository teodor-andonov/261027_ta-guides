# TA — Graphic Design System

**Owner:** TA / Teodor Andonov  
**Status:** Working design system — updated 27 October 2026  
**Scope:** Graphic identity, editorial composition, website/app visual grammar, imagery, diagrams and presentations.

A quiet, precise graphic language for **design, architecture and computation**: strict geometry and structured layouts, with controlled generative expression.

> **Working principle:** One small design grammar; many compositions. The system should generate consistency without making everything look like the same template.

## Read in this order

1. **[BRAND.md](identity/BRAND.md)** — brand foundation: TA as a **personal umbrella** with Portfolio and Studio at parity alongside Notes and Apps.
2. **[SITE_ARCHITECTURE.md](identity/SITE_ARCHITECTURE.md)** — recovered 27 September decision on Portfolio / Studio / Notes / Apps, provisional Method and future spin-off sites.
3. **[DIRECTIONS.md](identity/DIRECTIONS.md)** — Stage 02 boards; **03 / Soft Precision selected** 13 October 2026 (refinement pending).
4. **[ICONOGRAPHY.md](ICONOGRAPHY.md)** — Lucide for functional icons in services, UI and diagrams.
5. **[APP_ICONS.md](APP_ICONS.md)** — **per-app installed PWA launcher identity**, exact Sourcebook / Notebook / Objectbook icon choices and future deployment checklist.
6. **[DESIGN.md](DESIGN.md)** — current visual and compositional specification (main source of truth for visual execution).
7. **[IMAGERY.md](IMAGERY.md)** — the two generative graphic families, visual constraints, texture/diffusion and generator controls.
8. **[DECISIONS.md](identity/DECISIONS.md)** — chronological decision trail, superseded approaches, uncertainties and outstanding decisions.
9. **[TOKENS.json](TOKENS.json)** — small machine-readable draft. Explicit statuses distinguish a confirmed rule from a proposed numeric preset.

## App launcher icons — shared Lucide family

**Recovered 21 October decision, formalized 27 October:** every deployed TA app should have an **individual Lucide outline symbol**, used consistently for its in-app identity, favicon and installed PWA launcher assets. Current selections: **Sourcebook `library-big`**, **Notebook `notebook-pen`**, **Objectbook `blocks`**. Same monochrome rounded-outline family; each app gets a **distinct** symbol.

See **[APP_ICONS.md](APP_ICONS.md)** for packaging, safe zones and manifest requirements. The listed GitHub-hosted PWAs **have not been edited/deployed yet**; those changes follow once the user names the target repositories.

## Deployed PWA repository integrations — 27 October 2026

The **repository-side** icon integration is complete for [Sourcebook](https://github.com/teodor-andonov/261025-2132_sourcebook) (`library-big`), [Mindmap](https://github.com/teodor-andonov/261019-1740_pwa-mindmap) (`network`), [SVG Viewer](https://github.com/teodor-andonov/ta-svg-viewer-261012) (`scan-eye`), and [CAD Graph](https://github.com/teodor-andonov/ta-cad-graph-261012) (`workflow`). Each has proper 192/512 regular and maskable assets, favicon, manifest and service-worker cache updates. See [APP_ICONS.md](APP_ICONS.md) for the full audit. Live publishing and installed-OS icon refresh have not yet been verified; Sourcebook uses deliberate nightly/manual Pages publishing.

## Approved TA app icon preset — 27 October 2026

**Shared for now:** 2.0 Lucide stroke, **60%** icon scale, **25%** launcher rounding, **`#333333` icon on `#E6E6E6` background**, X/Y offset 0%, no transparency. Individual apps keep their own Lucide symbols. App-specific icon or background colours are a possible **later** refinement, not current.

Use the exact [TA app icon default preset](../../tools/261027-1116_app-icon-studio/ta-app-icon-default.json) in [TA Icon Studio](../../tools/261027-1116_app-icon-studio/app-icon-studio.html). The studio has these values as its default, and **TA Default** restores the shared style without changing the selected symbol. Maskable Android exports use safety-adjusted scaling and OS masking, documented in [APP_ICONS.md](APP_ICONS.md).

Four named PWA repositories have now been updated; any further apps require an explicit target list.

## Interactive app icon design tool

**[TA Icon Studio — HTML](../../tools/261027-1116_app-icon-studio/app-icon-studio.html)** lets you test any Lucide icon, thickness, icon scale, position, foreground/background colours and tile rounding. Includes live app/favicons previews, maskable Android-safe exports, regular SVG/PNG exports, and save/load settings JSON.

To use, open the GitHub file → **Download raw** → open the resulting HTML locally. The editor fetches official Lucide icon paths from a pinned CDN; first-time icons need an internet connection. Exports are self-contained. The Icon Studio doesn't directly edit other repositories; the four named PWAs were integrated separately on 27 October.

## Current direction, in one minute

- **Identity:** TA / Teodor Andonov is the **personal parent website**, with **Portfolio and Studio** equally prominent and **Notes, Apps/Projects** as additional independent sections. **Method / Studio Method** is a leading *provisional* studio name. Ventures may later get their own domains.
- **Visual mood:** grayscale first; warm/off-white or white ground; near-black ink; whitespace, proportion and alignment do the work.
- **Typography:** one monospace family; **Geist Mono** is the latest preferred direction, with readable English and Bulgarian Cyrillic.
- **Layout:** one shared proportional design unit; recursively nested **Cards** contain **Objects**. Objects hold one atomic payload.
- **Responsive geometry:** container-based scaling (cqw), a modular column system and powers-of-two options (1/2/4/8/16); exact breakpoints and numerical presets still require visual tests.
- **Images:** **A / Glyphs** = crisp fused rounded-rectangle modules; **B / Fields** = softer, grainier fields generated from the same grammar.
- **Colour:** restrained accents are possible where meaningful, but the core identity and generated image families are monochrome. Photography/rendered work keeps its own native colour.
- **Format:** same underlying rules should work for a web page, app, diagram, poster, slide and report; do not force identical page layouts across formats.

## Boundaries

This is the **graphic design system**, not the website content repository or a finished website implementation. The TA website / content studio should consume these rules and tokens; its JSON content and page-composition records belong with that product. The system may later provide shared components or generative tooling, but those are not implemented here.

**Important:** Prior history includes real changes of direction. The latest explicit choices take precedence over old prototypes. Numbers recorded as examples or trials are not silently promoted to immutable standards. See [DECISIONS.md](identity/DECISIONS.md).

## Status legend

- **CORE** — direct, repeated or latest accepted requirement; use as the default rule.
- **PREFERRED** — current favourite, but subject to practical testing.
- **TRIAL** — example value or experimental rendering to validate visually.
- **OPEN** — not yet decided; do not invent a final answer.
- **HISTORICAL** — earlier exploration, kept for context and not a current instruction.

## Using this with a coding agent

1. Read these documents **before** changing the TA website or visual editor.
2. Respect **CORE** rules, expose **TRIAL** parameters instead of hiding them, and explicitly flag **OPEN** choices.
3. Use shared source definitions for the website and authoring tool — no second, subtly different layout engine.
4. Start with one small, inspectable end-to-end proof, not a large framework.
5. Keep the source file-first and readable; prefer JSON for website content/composition and normal CSS/JS/SVG for rendering.

The **personal umbrella + equal Portfolio/Studio** structure and **03 / Soft Precision base visual direction** are approved. Notes and Apps/Projects stay first-class TA sections. **Lucide** is the preferred functional icon family. The Studio Method / Method spelling, final tagline, logo, proprietary imagery, precise typography and layout tokens are not yet finalized.

## Current working board — Soft Precision v2

**[View/download Soft Precision v2 HTML](../../studies/261013-0849_soft-precision-v2/soft-precision-v2.html)** — our new single-file, responsive, interactive design-board prototype. It supersedes the SVG sketches as the **current iteration**, not as a final identity approval.

The board demonstrates four recurring type roles, a shared spacing vocabulary, calmer nested cards and surfaces, service icons, the TA umbrella structure, report/notes/app specimens, and **light/dark + density controls**. Online it upgrades local fallback line icons to **Lucide 1.55.0**. Offline it remains usable without a build step; font is an explicit system fallback unless Geist Mono is installed.

For actual viewing, **download the raw HTML file and open it in a browser**; GitHub's code page typically displays source rather than the live design. The static SVGs remain below as research history.

## Stage 02 — Review the expanded identity application boards

These are **large 1800 × 2975 SVG concept sheets**, not single homepage mockups.

For a side-by-side browser review after cloning/downloading the repo, open **[directions/compare.html](../../studies/261012-2105_visual-identity-directions/compare.html)** locally. The GitHub web UI may display its source rather than run the HTML; the SVG links below open directly. Each includes a personal TA website, Portfolio, provisional Method Studio, a report, presentation, app/notes example, grayscale palette, type and icons.

- **[01 / Editorial Framework — full board](../../studies/261012-2105_visual-identity-directions/01-editorial-framework-board.svg)** — spare and architectural.
- **[02 / Modular Signal — full board](../../studies/261012-2105_visual-identity-directions/02-modular-signal-board.svg)** — dark and computational.
- **[03 / Soft Precision — original vector board](../../studies/261012-2105_visual-identity-directions/03-mineral-field-board.svg)** — selected direction's *earlier* study; see HTML v2 above for the current typography/rhythm refinement.

The earlier small SVG sketches remain as design-history references. Read [DIRECTIONS.md](identity/DIRECTIONS.md) for comparison and decision criteria. These boards show **proposals**, not approved final marks, commercial claims or published webpages.

This repository is documentation-first. No sample artwork, font binaries, components or rendering engine are claimed to be finished.