# DECISIONS — Evolution, Reconciliation and Open Work

**Compiled:** 12 October 2026  
**Purpose:** record *why* the TA design system looks the way it does; prevent a future agent from reviving an attractive but explicitly abandoned prototype.

This is a synthesis of accessible prior conversations and saved project artifacts (including the **1 October 2026 shared-unit DESIGN.md**), not a claim to have exported an exhaustive, line-by-line transcript of every chat. Where a decision was not clearly ratified, it stays **OPEN** or **TRIAL**.

## 1. Current decisions at a glance

| Topic | Current position | Status |
| --- | --- | --- |
| Umbrella brand | TA / Teodor Andonov — personal website with Portfolio, Studio, Notes and Apps/Projects | CORE, Sept 27 clarified Oct 12 |
| Formal descriptor previously accepted | Design, Architecture, Computation | CORE historical wording; contextual variants allowed |
| General look | Computational editorial minimalism, Swiss/architectural, grayscale-first | CORE |
| Design premise | One consistent graphic grammar for multiple media | CORE |
| Structure | Recursive Card + Object; one atomic payload per Object | CORE latest model |
| Page boundary | Special root Card; nested Cards can restart local grid | CORE |
| Spacing/scaling | Shared unit, proportional layout and controlled local overrides | CORE |
| Desktop reference | Approx. 1600px canvas | PREFERRED / reference, not maximum |
| Grid column family | 1 / 2 / 4 / 8 / 16, with eight-column emphasis | PREFERRED |
| Precise breakpoints | Not defined | OPEN |
| Typography | Geist Mono after Latin/Bulgarian comparisons | PREFERRED |
| Surface/palette | Whites, mineral greys, near-black, rare semantic accent | CORE direction |
| Numeric tokens/radii | Four type roles and simplified spacing proposed for Soft Precision | TRIAL values; role simplification preferred |
| Brand-generated imagery | Fused rounded modular A glyphs + related softer B fields | CORE direction, generation deferred |
| Functional icons | Lucide outline icons for UI, services and explanatory graphics | PREFERRED, selected 13 Oct |
| App launcher icons | Distinct Lucide glyph per TA PWA: Sourcebook library-big, Notebook notebook-pen, Objectbook blocks | SELECTED 21 Oct, extended 27 Oct |
| Visual direction | 03 Soft Precision, grayscale and rounded recursive Cards | SELECTED 13 Oct; implementation not final |
| Diffusion choice | Proximity vs ambient soft field | OPEN |
| Photography | Native color, not compulsory desaturation | CORE |
| Website content authoring | JSON-first; a few grouped JSON files are sufficient | CORE latest website decision |
| Technology | Lightweight HTML/CSS/JS/SVG renderer and shared components | PREFERRED current |
| Separate studio sub-brand | Method / Studio Method preferred provisional name; earlier METOD shortlisted | OPEN final naming |
| Final logo | No conclusive approved mark | OPEN |

## Decision — 12 October 2026: equal dual emphasis (APPROVED)

**User selection:** **C — Both equally.** The TA brand must give **Portfolio / Research** and **Practice / Collaboration** equivalent prominence. This supersedes the Stage 01 draft proposal of *author/portfolio first, practice second*. It does **not** oblige equal amounts of content, treating speculative work as commissions, or presenting a personal author as an established large firm.

Practical implications:
- Two clear and comparably weighted entry points in navigation, first-screen messaging and identity applications.
- Unified typographic, layout, naming and A/B image grammar across both expressions.
- Distinct content and calls to action appropriate to each function.
- Neither route is a nested afterthought nor a separate competing sub-brand.

**Stage 02 opened:** [DIRECTIONS.md](DIRECTIONS.md) documents three **concept studies**, with editable vector boards in [directions/](../../../studies/261012-2105_visual-identity-directions):
**01 / Editorial Framework**, **02 / Modular Signal**, **03 / Mineral Field**.
All use equal primary channels so differences in treatment can be judged fairly. No visual direction, logomark, diffusion algorithm or numeric type scale has been approved yet.

## Clarification — 12 October 2026: recovered 27 September umbrella decision

The user correctly recalled a specific **27 September 2026** conversation: **TA / teodorandonov.com is the personal umbrella** with **Portfolio, independent Studio, Notes/blog and separate Apps/Projects (e.g. Balkan House)**. These may start as TA-hosted portals/subsites; mature ventures can migrate to independently named domains while TA remains the parent/link source.

The earlier 12 October **C = both equally** decision refers to **Portfolio and Studio prominence**, **not** a two-destination brand architecture that swallows Notes and Apps. The repo's first BRAND.md draft was therefore incomplete; v0.3 corrects it. Historical employer projects may be shown in personal Portfolio **with clear credits, roles and employers**, not marketed as the Studio's completed contracts.

**Studio name:** September discussion favoured **METOD** among Bulgarian/international names, but it was not finally chosen. The latest user wording is **Method / Studio Method**, a preferred **working name**, still not legally or visually locked.

**Stage 02 visual feedback:** The first set of sketches looked too much like webpages. The user wanted **much bigger identity/application boards** across website, reports, presentation, apps etc. The soft rounded feel of Direction 03 is preferred; **strict grayscale without warm saturation**; proprietary A/B image system is deferred; use simple icons and placeholder linework meanwhile. Large application boards are stored in `studies/261012-2105_visual-identity-directions/*-board.svg`; see [DIRECTIONS.md](DIRECTIONS.md) and [SITE_ARCHITECTURE.md](SITE_ARCHITECTURE.md). Visual approval remains pending.

## Selection — 13 October 2026: Soft Precision + functional icons

**Selected direction:** the owner explicitly judged **03 / Soft Precision** best and aligned with the nested Card/Box compositional system. This is now the **preferred design family to implement**, not just one of three equally weighted directions.

**Critique of first 03 board:** too many type sizes/variants, weak rhythm, excessive simultaneous hierarchy gestures. Do **not** copy every numeric size and decorative panel from the current 1800 × 2975 concept board into the real component library. Apply a limited four-role type hierarchy, repeatable unit spacing, consistent radii/alignments, deliberate empty space, less gratuitous decoration.

**New graphic separation:** adopt **Lucide** as preferred third-party **functional icon** system for services, navigation, explanatory cards, reports and apps. It must not be confused with (or replace) the distinctive TA signature mark, the future **A / glyph** artwork or **B / abstract field** imagery. Icons can overlay B in future service panels, provided contrast is sufficient.

**Surface confirmation:** grayscale only (no deliberate warm hue/saturation), with softly rounded surfaces. Exact role sizes, spacing multipliers, icon thickness and approved compositions remain trials. Documented in [ICONOGRAPHY.md](../ICONOGRAPHY.md), [DESIGN.md](../DESIGN.md) and [DIRECTIONS.md](DIRECTIONS.md).

## Decision recovered — 21 October 2026: Lucide app family; standardized 27 October

The 21 October app-design conversation **established a shared Lucide icon family for individually named apps**, with explicit assignments:

- **Sourcebook** → `library-big`
- **Sketchbook / now Notebook** → `notebook-pen`
- **Objectbook** → `blocks`

The accepted style was **monochrome outline**, no fill, round caps/joins, approximately **2px stroke** in the standard 24×24 viewBox, with the icon inheriting its UI theme colour. A Lucide v0.456.0 / XL-preset (about 24px UI specimen) was discussed. This was **a family decision**, not conclusive approval of a fixed Android/Windows launcher tile design.

On 27 October the user specifically asked to formalize using **Lucide as the installed PWA icon family for all deployed TA apps** and to prepare for updating a selected set of existing GitHub-hosted PWAs **later**. This establishes the wider launcher policy without falsely claiming those deployments were already changed.

**Clarification:** each PWA gets its **own distinct Lucide glyph**, not a single reused `app-window` / TA glyph. The common treatment provides a recognizable family. Masks, backgrounds, exported PNGs, favicon variants and manifest links are deployment requirements/implementation trials, not earlier approved visual details.

**Central standard:** [APP_ICONS.md](../APP_ICONS.md). **UI iconography:** [ICONOGRAPHY.md](../ICONOGRAPHY.md). **Current status:** design-system docs updated; **no other app repository changed** pending the owner's specific list.

## Approved current app icon styling — 27 October 2026

The owner supplied a **TA Icon Studio settings JSON** and explicitly selected its parameters as the **shared monochrome family preset for now**. Exact values: Lucide `2.0` stroke; regular icon `60%` scale; tile `25%` corner rounding; offsets `0%/0%`; icon `#333333`; tile `#E6E6E6`; transparency `false`; guide `false`. Source/preset: [presets/ta-app-icon-default.json](../../../tools/261027-1116_app-icon-studio/ta-app-icon-default.json).

These values are **approved current defaults**, superseding the earlier OPEN launcher palette and trial defaults of 67% scale / 24% rounding / #242424 on #EEEEEE. Each application still has its own Lucide glyph. Different app-specific icon/background colours may be explored later, but **are not selected** now.

Maskable Android exports intentionally clamp glyph scale to 54%, use solid square background and OS-controlled cropping for safe rendering. This is a separate export implementation, not a change to the approved regular 60% design.

TA Icon Studio now embeds the approved values and provides a **TA Default** style reset. The four owner-selected PWA repositories and their manifests were subsequently updated on 27 October 2026.

## Implementation — 27 October 2026: four PWA icon integrations

The owner explicitly selected four existing GitHub PWA repositories for the approved monochrome icon family: **Sourcebook (`library-big`)**, **Mindmap (`network`)**, **SVG Viewer (`scan-eye`)**, and **CAD Graph (`workflow`)**. Distinct icons from canonical Lucide 1.61.0 were combined with stroke 2, regular 60% scale, rounded tile at 25%, foreground `#333333`, background `#E6E6E6`, centred offsets, and maskable square icons with 54% safe glyph scale. Four repos received regular/maskable PNG icons in 192/512 sizes, SVG icon/favicons, webmanifest icon references, cache updates and repeatable GitHub Actions asset generation.

The four updated manifests and service-worker JavaScript were verified on GitHub; **live deployment and Android/Windows installed icon refresh were not confirmed at the time of this repository update**. Sourcebook's Pages publishing is nightly/manual by established release policy. The other apps have push-triggered Pages deployment workflows. Per-app icon/background colours remain a future experiment.

## 2. Development timeline and supersessions

### February 2026 — TA identity and early typography

**Confirmed:** TA / Teodor Andonov; phrase **“Design, Architecture, Computation”** in that order. A relatively severe mono editorial hierarchy was proposed, often using JetBrains Mono, large size jumps, thin alignment rules, restrained metadata and a black/white/gray structure.

**Still useful:** clarity, distinct hierarchy, mono character.  
**Not final:** orbit/logomark tests or early typographic numeric ladders.

### May 2026 — Computation + Swiss matrix + UI grammar

A sequence of experiments moved from brand-graphic comparisons toward strict modular layout. The user chose the computational / monochrome rounded-pixel option **A** over colorful organic gradient blob alternatives. Swiss grids, grayscale surfaces, nested translucent neutral regions and sparing color were explored.

A minimal web/app/graphics design system experimented with:
- 10px grid unit; body 10px; H2 20px; H1 40px.
- 0.5–1px faint structural outlines.
- Minimal/square grouping; small media radii, black primary controls.
- Later 10px radius / 600px reading width and wireframe-like regions.
- Token name “--ta” and in other iterations a 15px base.
- Accent palette #3F55C0 blue, #40BD6A green, #C04196 magenta, #C0AA3F gold.

**Survives:** structural rigor, minimalism, grayscale identity, modular glyphs, occasional purposeful accents.  
**Superseded as global prescriptions:** 10px body text, compulsory hairline boxes, mandatory 10px unit, one universal radius or all interface areas styled like wireframes. Good real-world readability overrides the tiny-body prototype.

### September 2026 — Studio framing, presentation system and reference scale

The website was framed as a personal/public platform plus independent design work. Arrangement types separated from subject matter: fixed packages, subscription, bespoke contracts; architecture/computation/façades/parametric work as areas, not necessarily the hero proposition. Primary contact action: book a 15-minute call. Brand sub-names were considered, **not selected**.

A minimal TA presentation/report deck explored a quiet off-white/ink/gray language, strong imagery, technical metadata and clean hierarchy. Some slides used **Arial**. That is a *presentation-specific experiment* and evidence that the language should be portable, not a later decision to replace mono on the website.

Late September explicitly established **u = design width / divisions**, with typographic and spatial values related to u. The user distinguished design reference width from actual CSS viewport and content width. A **1600px** desktop reference was favored, while values like 160 divisions (=10px) were examples.

### 1 October 2026 — Shared-unit WIP DESIGN.md

A substantial saved specification defined:
- **Box → Object → Content**, one content per Object, nested Box as Content.
- A shared unit, named design width and divisions.
- Independently chosen local column/row counts and x/y/w/h assignments.
- Root vs nested layout contexts, explicit web section height ratios and fixed print/artboard sizes.
- Card/Media rounding separated; content-fit checks and export discipline.
- Trial neutral palette #FFF / #F2F2F2 / #CCC / #999 / #333.
- A 1440/200 = 7.2px trial and a 2u pad/gap/radius trial.
- Fixed authored page heights, not intrinsic content flow.
- Arial as an experiment, alongside an IBM Plex Mono trial.

At that moment it explicitly retired **Card** terminology. This was a point-in-time version, not eternal instruction. Later October conversations adopted a direct **Card/Object** grammar for the actual website/editor.

**Carry forward:** one shared unit, recursive containment, one payload per Object, local grid controls, consistent rounding tokens, format awareness, visual-content separation.  
**Do not force as universal current rules:** the precise 1440/200 preset, Arial default, automatically clipped fixed-height web copy, no mobile reflow, “Card retired” assertion, or a hard 4×4 inside every container.

### 1–3 October 2026 — Graphic composition and SVG/HTML research

Developed the highly specific visual direction often called **monochrome filleted raster abstraction**: strict orthogonal occupied modules merged into a smooth continuous shape with generous fillets, negative space and no generic glossy treatment. Explored an authored computational hero/animated SVG.

Graphics were treated as one atomic placed drawing with their own internal coordinate system; captions/headings often separate from the drawing. The user distinguished colors for explanatory diagrams from native photographs/renders. Diagrammatic HSL hues 60 / 150 / 240 / 330 at S/L 50% were a specific exploration.

Research compared pure SVG composition, HTML/CSS composition and hybrids. A hybrid used HTML for shell/project cards/footers and SVG for distinctive services/how-we-work/hero sections. Later a pure HTML alternative was tested. **No requirement emerged that all pages must be SVG.**

### 3 October 2026 — Fonts and UI refinements

Font tests compared PT Mono, Noto Sans Mono, IBM Plex Mono, Geist Mono, Source Code Pro and others in English/Bulgarian. PT Mono was liked in Bulgarian, Noto in English, IBM Plex Mono rejected. **Geist Mono** emerged as the latest strongest practical overall preference. Do not mistake the earlier generator prototype's JetBrains Mono UI or the older Arial report as a later reversal.

### 5 October 2026 — Generative A/B families and diffusion

Two families established:
- **A:** vector/system glyphs: rounded rectangular modular pixelated/fused geometry.
- **B:** softer, grainier abstract image fields generated by the same script, varying module scale, distribution, blur and grain.

Visual directions combined **fused modules + system glyphs**, minimal mineral materiality and a subtle ancient-future tension. Shortlisted texture variants: **A1 Clean Mineral**, **A2 Rounded-square Halftone**, **B2 Diffused Fusion**, **B3 Threshold/Artefact**.

Two diffusion behaviours were compared: **01 Proximity Diffusion** (near forms soften, isolated edges remain sharp) and **02 Soft Field Diffusion** (wider ambient field with no drop-shadow/glow look). A comparison board was requested across Light Object, Dark Object, Light Background, Dark Background and Hybrid. Repeated revisions suggest **the final render/choice was not fully approved**.

A one-file HTML generator concept and v0.1 experiment covered deterministic seeds, module size/density, rounding, merging, field circles, blur and grain. Geometry-merging refinements remain future work.

**Resolution of apparent contradiction:** early “no blur” refers to the crisp core identity / UI / A glyphs. Later selective blur is intentional **inside B and selected treatment layers**, not a global invitation to add glowing shadows.

### 10–12 October 2026 — Website/editor architecture and latest grammar

Website content/composition switched decisively from HTML-first / Markdown / Astro explorations to **JSON-first**. This is a meaningful **supersession**, not an optional file-format footnote.

The new system has:
- JSON as source of truth for pages, projects, posts/articles, image properties and page compositions.
- A few grouped files (pages, projects, posts/articles, images) instead of pointless one-record-per-file scattering.
- Reusable templates/components and data-driven collections plus exceptional fully authored pages.
- The **recursive Card/Object** authoring grammar; Cards own spacing/grid/surfaces; Objects are atomic content payloads.
- A special root Card, nesting/grouping and layout controls.
- One renderer/component model shared between the public site and visual Content Studio.
- An editor that can author properties in table form **and** visually edit pages/templates/components, persisting real JSON.
- Broad classes of posts: news, short notes, articles and other editorial updates, distinct from projects.

**Important boundary:** JSON is a website **authoring/source-of-truth decision**. CSS and SVG are still appropriate implementations/asset formats; not every graphic must be expressed as JSON. This repository stores design specifications, while the separate website repo implements the JSON renderer.

## 3. Contradiction-resolution rules

1. **Latest explicit user choice wins** when it concerns the same question; do not treat a prototype as immutable because it was once documented.
2. **Aesthetic constraints are context-specific:** crisp A glyph ≠ soft B background; diagram colors ≠ photo colors.
3. **Formula ≠ numeric preset:** u=width/divisions can be agreed while the final divisions remain unknown.
4. **Reference viewport ≠ CSS max-width:** a 1600px authored reference does not mean a mandatory 1600px max-width.
5. **A mockup is evidence, not automatically approval:** output quality and exact radius/colors remain testable.
6. **Brand identity ≠ studio business name:** TA is stable while the independent-practice naming search remains open.
7. **Design system ≠ website codebase:** the same rules inform both, but page data belongs to the website.

## 4. Still-open decisions — suitable for future tests

| Question | What to evaluate |
| --- | --- |
| Exact global unit/divisions | Compare 1600/160=10px against alternatives at real desktop and mobile scales |
| Responsive transitions | Choose column counts and explicit breakpoints that preserve legibility and composition |
| Default Card/media radius | Visually test independently; keep override controls |
| Definitive neutral palette | Compare cold #F2F2F2 and warmer mineral #F2F2F0, contrast on both themes |
| Sparse accent usage | Decide whether categorical accents belong in general UI or only diagrams/system states |
| Final typography ramp | Validate Geist Mono Cyrillic/Bulgarian, readability and mobile sizes |
| Final logo/symbol | Create/approve wordmark or A-family-derived mark; don't imply historic symbols are chosen |
| Option 01 vs 02 diffusion | Matched-seed comparison using the 5-state board; judge real outputs |
| Generator union/fillet method | Exact geometry versus raster approximations and export quality |
| Motion language | If animated SVG hero is useful, define restraint, timing and reduced-motion fallback |
| Responsive fixed artboards | Decide where scaling, cropping and content reflow are actually appropriate |
| Editor component controls | Map JSON fields to consistent Card/Object design props without duplicating renderer logic |
| Final independent-practice name | Separate strategic choice, not a design-system prerequisite |

## 5. Anti-revival checklist for agents

**Do not silently reintroduce:**
- Markdown as the website's required content source after JSON-only choice.
- Astro/React/Next or a mandatory build pipeline as if the user had selected one for v1.
- A separate React/HTML visual editor whose rendering differs from the public website.
- IBM Plex Mono or an all-Arial web typography system as the newly chosen primary.
- Colorful generative blobs, glossy 3D, faux stone materials, glowing gradient artwork.
- Hardcoded 10px body text or uniform tiny print from the May experiments.
- A mandatory 1440px width, fixed web section ratio, or 4×4 grid everywhere.
- A locked METOD/SREDA/etc brand name that was only explored.
- A claim that the two diffusion directions or exact generator presets are finalized.
- The old “Card retired” language as a prohibition against the latest Card/Object grammar.

## 6. How to continue

This is a **living decision log**. When making an actual choice:
1. Update the corresponding **CORE/PREFERRED/TRIAL/OPEN** status in DESIGN.md or IMAGERY.md.
2. Record what changed and why here, with date.
3. Update machine-readable TOKENS.json only when it expresses the same truth.
4. Validate with real visual output—not only code review.
5. Keep history without polluting the current specification with competing defaults.

Do not flatten the history into a faux consensus. The system evolved. That's normal and useful.