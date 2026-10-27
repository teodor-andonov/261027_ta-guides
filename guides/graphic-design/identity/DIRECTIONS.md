# STAGE 02 — Visual Identity Directions

**Status:** v0.3 · 13 October 2026 · 03 / Soft Precision **selected for development**; board refinement pending  
**Decision inherited from Stage 01 (APPROVED), clarified against 27 September history:** **TA is the personal umbrella**; **Portfolio** and **Studio** have equal prominence alongside **Notes** and **Apps/Projects**. Ventures can begin under TA and later move to independent websites. **Method / Studio Method** is the leading provisional studio name; the final spelling is unapproved. See [SITE_ARCHITECTURE.md](SITE_ARCHITECTURE.md).

## Soft Precision v2 — HTML/CSS application board

**NEW primary working study:** **[Open Soft Precision v2](../../../studies/261013-0849_soft-precision-v2/soft-precision-v2.html)**.

After comparing SVG and HTML authoring, the current workflow uses **one standalone HTML/CSS file** as the visual design-board source. It is easier to evolve recursive Cards, reuse real components, tighten typography and add semantic icons than a manually positioned SVG illustration. The original SVG boards remain as dated design exploration; fixed-format SVG/PDF export is an optional downstream deliverable.

**What's new in v2:**
- Four typographic roles: **Display / Heading / Body / Metadata**; no per-card bespoke scales.
- A small shared spacing rhythm based on **u / 2u / 4u / 8u**, plus repeatable card padding and radii (all numeric values remain trial).
- Explicit, consistent nested Card/Object-inspired hierarchy and alignment across the website, three services, Portfolio/Studio entry routes, Notes, app UI and report.
- Functional outline icons: **official Lucide 1.55.0 loads when online**, with **self-contained line-icon fallbacks** if offline (the demo does not bundle fonts or icon binaries). For production, use a selected Lucide version and preserve its license notices.
- Interactive **Comfortable / Compact** spacing, **Light / Dark** grayscale and **Print / Save PDF** controls.
- Actual responsive HTML rather than static 1800px labels scaled down to mobile.
- No proprietary signature symbol, invented A/B image field or branded decorative SVG while those systems remain pending.

**How to view:** download `soft-precision-v2.html` from GitHub using its **Raw** or **Download raw** control, and open it in a browser. It runs from `file://` without a local server; the icons fall back gracefully without internet access. The GitHub code view does not execute HTML.

**Status:** v2 is a **working implementation study**, not the final approved website or a finished brand book. Direction 03 is selected; the exact token values, layout treatments and icon mappings remain available for visual review.

## Direction selected — 13 October 2026

**OWNER DECISION: 03 / Soft Precision is the selected base direction.** This closes the *which visual family?* comparison, **not** the entire identity or production system.

Feedback on the current 03 board:
- **Keep:** soft, rounded Card/Box nesting and the coherent monochrome feeling.
- **Fix:** too much variation in type sizes, insufficient rhythm, too many simultaneous hierarchy changes. Simplify to a four-role typography set, recurrent spacing, aligned padding, more editorial pauses.
- **Adopt:** consistent **Lucide functional icons** for features, services, tool navigation, notes and explanations instead of drawing arbitrary symbols each time.
- **Defer:** final A/B generative glyphs and diffused imagery. Don't fake a signature logo or fill every service card with unapproved bespoke art.
- **Keep grayscale neutral:** no warm saturation. Emphasize size, spacing, rounding, alignment and content rather than contrast tricks.

The next iteration should be **a disciplined refinement of 03** applied to a real website/portfolio/studio/report/app family. **01 is a source of typographic restraint**, not a co-equal competing identity. **02 remains a recorded experiment**.

See [ICONOGRAPHY.md](../ICONOGRAPHY.md) and the updated rhythm rules in [DESIGN.md](../DESIGN.md). Precise numeric values and final logo/imagery are still **TRIAL/OPEN**.

## Current deliverables — complete multi-application boards

**NEW — 12 October 2026.** These **1800 × 2975 px** editable SVG sheets replace the original homepage-sized explorations as the **primary Stage 02 comparison**. Every board shows:
- TA personal umbrella website with **Portfolio / Studio / Notes / Apps** in the navigation;
- **Portfolio** and provisional **Method Studio** with equal prominence and different duties;
- credited project/case-study design, separate studio services/CTA;
- reports/publication artboard, presentation system, notes and app UI examples;
- typography specimen (Latin + Bulgarian), grayscale palette, icons, component details.

A simple **[HTML review viewer](../../../studies/261012-2105_visual-identity-directions/compare.html)** lets you switch between the three boards and compare them after downloading/cloning the repo (open that HTML locally). Individual SVG links work in GitHub's file viewer too.

### Large boards — primary visual comparison

1. **[01 — Editorial Framework / full identity board](../../../studies/261012-2105_visual-identity-directions/01-editorial-framework-board.svg)** — disciplined layout, spacious white surfaces, fine rules, minimal corner radii.
2. **[02 — Modular Signal / full identity board](../../../studies/261012-2105_visual-identity-directions/02-modular-signal-board.svg)** — dark grayscale, strong typographic contrast and higher-density computational interface.
3. **[03 — Soft Precision / full identity board](../../../studies/261012-2105_visual-identity-directions/03-mineral-field-board.svg)** — **latest user favourite**; softly rounded monochrome surfaces, comfortable space, calm hierarchy. *No warm tint or saturation.*

All three demonstrate **the system in use across media** rather than just a homepage. They avoid pretending the A/B proprietary imagery system has been finalized; icons, restrained architectural linework and neutral placeholders are used where needed. Wordmarks, font metrics and final commercial copy are still conceptual.

### Older explorations — retained as first-pass sketches

The small 1600 × 1120 page-oriented SVGs below remain in the repo as **historical process**, not as the current target for Stage 02.

## View the three editable boards

- **[01 — Editorial Framework](../../../studies/261012-2105_visual-identity-directions/01-editorial-framework.svg)** — precise, calm, mostly white: an architectural publication with distinctive geometric punctuation.
- **[02 — Modular Signal](../../../studies/261012-2105_visual-identity-directions/02-modular-signal.svg)** — high contrast, denser, more explicitly computational: a recognizable visual toolset and strong symbol system.
- **[03 — Mineral Field (original sketch)](../../../studies/261012-2105_visual-identity-directions/03-mineral-field.svg)** — early soft-field sketch, since expanded into the neutral-gray **Soft Precision** full board.

The **original sketches** are editable SVGs at 1600 × 1120. The **new primary boards** are editable SVGs at 1800 × 2975. No fonts are bundled; Geist Mono displays where installed, otherwise a monospace fallback. Neither size is a finished responsive website. Copy, icons and numerical choices remain exploratory.

## Controlled comparison

Each new board deliberately tests **the same functional application set**, with more than a single website page:

- Identity: **TA / Teodor Andonov**.
- Existing descriptor: **Design / Architecture / Computation**.
- Hero headline: **Architecture and computation, in practice.**
- **Same TA navigation:** Portfolio / Studio / Notes / Apps / About.
- Two equally visible, distinct primary portals: **Portfolio** (personal work/credits) and **Method Studio** (independent practice/services).
- Separate sample pages/artefacts for notes and apps, not merely subfolders of Portfolio.
- Report, presentation, typography, grayscale palette, UI tokens and iconography.
- Signature **A / Glyph** and **B / Field** demonstrations.
- Basic type/layout/colour behaviour.

This means differences come from **compositional treatment**, not different brands or unequal business emphasis. The current headline and CTA terms are *specimens*, not approved public copy.

## Direction 01 — Editorial Framework

**Idea:** TA is an architectural publication with a practice attached as an equal pillar—not a corporate website. Geometry supports a calm hierarchy rather than monopolizing attention.

- Very light, spare surfaces and near-black type.
- Large measured mono headline; thin horizontal rules and careful whitespace.
- Crisp fused-rect glyphs appear as punctuation/signature.
- B fields stay secondary, in bounded imagery slots.
- Both primary routes read as two equivalent editorial chapters.

**Strength:** credible across reports, architecture and academic writing; best for enduring legibility and content.  
**Risk:** too neutral without a sufficiently distinctive glyph/photographic language.  
**Best case:** technically literate, highly restrained portfolio and practice.

## Direction 02 — Modular Signal

**Idea:** the identity behaves like a precise digital instrument, using repetition, stark inversion, graphic modules and indexed taxonomy.

- Deep monochrome shell and aggressive light/dark blocks.
- Larger, more prominent A glyph assembly and denser graphic cadence.
- Labels, coordinates, numbering and modular blocks are part of the visual voice.
- Equal primary entry points use deliberately identical formal weight.
- B texture remains extremely subordinate so the concept does not become noisy.

**Strength:** highly recognizable, generative, strong in apps/tools and diagrams.  
**Risk:** can become a cold developer-tool aesthetic or obscure architecture and people; needs restraint.  
**Best case:** computational research, software, identity atlas, technical interfaces.

## Direction 03 — Mineral Field

**Idea:** mathematical precision meets calm and soft interface surfaces. Sharply defined type sits against grayscale panels with more generous radii. The generative field treatment is **deferred**, not simulated as a finalized brand asset.

- True achromatic grayscale surfaces; **no warm tint or intentional colour saturation**.
- Sharply defined editorial type remains the primary information layer.
- Simple line icons and neutral geometric/architectural placeholders for now; proprietary A/B imagery is a separate future refinement.
- Both primary routes have equal area, salience and call-to-action treatment.
- Soft cards and rigorous proportion make application layouts cohesive without relying on a final logo or distinctive imagery system.

**Strength:** most ownable synthesis of the recent A/B image-language research.  
**Risk:** field can become arbitrary blur, poor contrast or decorative texture if not tightly constrained.  
**Best case:** coherent brand artwork, hero images, research publications and visual tools.

## My provisional judgement

**First choice to develop: 03 / Soft Precision**, supported by **01 / Editorial Framework** as the structural spine. Treat **02 / Modular Signal** as a high-energy application mode for tools, diagrams or special campaigns, not necessarily the default TA homepage.

**Direction selection is now approved:** 03 / Soft Precision (13 October 2026). Its exact treatment and the current full board are **not** approved production assets. Borrowing 01's editorial discipline is a focused refinement, not choosing a fourth direction. Avoid a mash-up of all three without constraints.

## What we need to approve

1. **Underlying stance:** should the base feel primarily **01 editorial**, **02 high-contrast computational**, or **03 soft precision / rounded editorial**?
2. **Graphic A / symbol:** does the orthogonal fused-module signature feel right at icon and hero sizes? None of the board specimens is a final approved logo.
3. **Graphic B / treatment:** defer texture/diffusion design and approval; at this stage approve monochrome surface layout, icons and typography independently.
4. **Typographic tone:** acceptable weight and size hierarchy for Geist Mono in English and Bulgarian (these boards use fallback until the font is available).
5. **Umbrella presentation:** do Portfolio and Studio feel equally accessible, with Notes and Apps properly represented and all under one clearly personal TA identity?

## Tests before selecting a direction

- Review the boards at normal desktop width **and at 50% scale**.
- Repeat the selected treatment on a real project case study, practice service page, technical report and a short post.
- Set the same test copy in English and Bulgarian using actual Geist Mono.
- Replace experimental glyphs with deliberately designed vector forms that work at favicon size and on A4.
- Test a light and dark variant, accessible text/focus contrast and crop behaviour.
- Decide which elements are **identity-wide defaults** and which are **section-/media-specific treatments**.

## Completion of Stage 02

**Stage 02 direction selection is complete (03 / Soft Precision).** The current board requires a refinement pass to address typography, spacing rhythm and Lucide icon use; the full brand identity remains unfinished. Stage 03 should validate repeatable design tokens and typography before producing final logo, components and media templates.

**Related:** [BRAND.md](BRAND.md), [DESIGN.md](../DESIGN.md), [IMAGERY.md](../IMAGERY.md), [DECISIONS.md](DECISIONS.md).