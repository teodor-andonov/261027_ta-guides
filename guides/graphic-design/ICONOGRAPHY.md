# ICONOGRAPHY — TA / Functional Illustration

**Status:** Updated 27 October 2026 — UI iconography + the separate approved PWA application-icon family. Numeric presets remain trials.

## Why icons belong in the system

Icons provide a **fourth practical visual vocabulary** between typography and unique artwork: familiar, repeatable, low-effort illustrations for information design. We should not custom-design a symbolic SVG for every service, feature or note. The visual grammar must remain understandable even when the original A/B imagery generator is unfinished.

**Default library:** [Lucide](https://lucide.dev/) — consistent line-based SVG icons, open source and usable commercially. Lucide icons are licensed under **ISC**, with some Feather-derived icons under **MIT**; preserve applicable notices if distributing icon files. See [license](https://lucide.dev/license). This is a third-party library, **not a proprietary TA logo**. Do not assume every icon seen in ChatGPT uses Lucide; the local conversational UI can use Lucide and platform-specific equivalents.

## Installed applications: app-launcher icon family (approved 21 October 2026)

**Canonical deployment rule:** use **distinct Lucide outline symbols** as the **installed icon identity for individual TA PWAs** (Sourcebook `library-big`, Notebook `notebook-pen`, Objectbook `blocks`). The same family approach applies to newly deployed apps; record each app's actual chosen symbol instead of giving every app the general `app-window` icon.

**Separate contexts:** An in-app UI icon inherits `currentColor`. A PWA **launcher icon** requires self-contained local SVG/PNG exports, manifest `any` and `maskable` assets where appropriate, OS safe-zone testing and favicon treatment. These share design logic but are **not the same asset**. The 21 October discussion selected the icons and outline treatment; it did not approve one launcher-tile colour or corner treatment. Any launcher packaging parameters below are a new implementation proposal.

**Read [APP_ICONS.md](APP_ICONS.md) for the central icon registry, exact Lucide mappings, maskable asset guidance and later cross-repository rollout checklist.** This distinction is particularly important because the general website `Apps` section uses `app-window`, while the apps themselves need distinctive symbols.

## Graphic layers — three distinct responsibilities

| Layer | Library/source | Role | Example |
| --- | --- | --- | --- |
| **Functional icons** | Lucide | Semantic explanation, navigation, UI, services and small feature cards | Layers, blocks, notebook, panel, chart |
| **A — TA glyphs** | Future original authored/generative system | Recognisable brand identity, signatures and bespoke symbolic work | Cover graphic, signature identity mark |
| **B — TA fields** | Future original authored/generative system | Atmospheric background artwork and hero/service fields | Subtle background with an icon overlaid |

**Do not force A/B graphic work to supply routine interface icons.** Iconography must remain useful independently of bespoke brand imagery.

## Style contract

**PREFERRED core behaviour**
- Use Lucide **outline** icons with default round caps/joins.
- One family in the same composition: don't mix outline Lucide with filled Material, emojis, duotone or bespoke pseudo-Lucide symbols without a clear exception.
- Same size, stroke and alignment for icons used in one component class.
- Color from existing grayscale tokens; inherit foreground color where possible (`currentColor`).
- A functional icon should convey a specific concept. Decorative duplication of the same point adds no information.
- Avoid making all icons look like corporate clip art or a row of identical squares. Their **containers and placement** can give identity.
- Brand logo/wordmark is **not** Lucide. The distinctive symbol remains separately designed.

**TRIAL default implementation**
- SVG coordinate box: `viewBox="0 0 24 24"`.
- Stroke width: **1.75** in the 24-unit coordinate system. Lucide's default is 2; 1.75 is a slightly quieter **trial** for TA.
- Icon sizes by job: **16px** small inline, **20px** navigation/control, **24px** standard feature, **32px** prominent service icon. Avoid endless intermediate sizes.
- Feature icon container: optionally a neutral surfaced Card, not an Object background; trial outer **48–64px** with shared card rounding.
- Don't resize the SVG to fake hierarchy when typography/placement can do the job.
- Icons in a repeated row share one optical baseline and identical frames.
- Test real icon silhouettes for visual weight; consistent stroke numbers alone don't guarantee equal optical density.

## Suggested semantic icon registry

Use explicit semantic mappings and reuse them, rather than selecting a random similar icon at each appearance:

| Domain | Lucide icon name | Reason |
| --- | --- | --- |
| Portfolio / work | `layers-3` | Stacked design output |
| Studio / architecture | `drafting-compass` | Drawing / technical craft |
| Computation | `workflow` | Connected procedural logic |
| Façades / systems | `panels-top-left` or `grid-3x3` | Components and systemization |
| Research | `book-open` | Knowledge and exploration |
| Notes | `notebook-pen` | Writing and observation |
| Apps | `app-window` | Digital tools |
| Generative systems | `blocks` | Modular construction |
| Performance | `chart-no-axes-combined` | Measurement and evaluation |
| Collaboration | `users` | Work with others |
| Contact / inquiry | `arrow-up-right` | Next action (pair with an explicit text label) |

These are **recommended mappings**, not universal truth. Confirm icon names exist in the version actually installed.

### Where icons help

**Service cards:** place a 24 or 32px monochrome semantic icon above/alongside a short descriptive title. Later a subtle **B-field image can sit behind** while the icon remains crisp on top, provided contrast is tested.

**Three-point explanation:** repeat a single `icon + title + body` component three times with identical typography, spacing and bounds.

**Information diagrams:** mix clear arrows, numbers and simple symbols. Use SVG for structural connections and grids; use Lucide for familiar semantic endpoints. Do not stretch icons as a substitute for a real drawing.

**Navigation:** small icons may help scan, but labels remain visible, especially for primary website navigation (Portfolio, Studio, Notes, Apps).

**Reports and presentations:** use the same line icons with the same optical and baseline rules; no special report-only pseudo-icons.

### Examples with the Card/Object grammar

```text
CARD / Service Grid (3 equal children, uniform gap/pad/radius)
├── CARD / Service
│   ├── OBJECT / icon (Lucide drafting-compass)
│   ├── OBJECT / heading ("Architecture")
│   └── OBJECT / description
├── CARD / Service
│   ├── OBJECT / icon (Lucide workflow)
│   ├── OBJECT / heading ("Computation")
│   └── OBJECT / description
└── CARD / Service
    ├── OBJECT / icon (Lucide blocks)
    ├── OBJECT / heading ("Design Systems")
    └── OBJECT / description
```

An Icon is **one Object payload**, not a new structural kind or a permanently surfaced square. The Card controls optional background, padding, gap, grouping and rounding. Within a complex SVG diagram, icons are embedded graphic elements rather than separate layout Objects.

## Component rhythm (trial — see DESIGN.md)

For **Soft Precision**, cut the default typography to four roles: **Display / Heading / Body / Metadata**. Default example at a 1600px reference with `u=10px`:

| Role | Size | Scale | Usage |
| --- | --- | --- | --- |
| Display | 48px | 4.8u | Large hero or section display |
| Heading | 28px | 2.8u | Card/section title |
| Body | 16px | 1.6u | Normal prose |
| Metadata | 12px | 1.2u | Labels/captions |

**These values are tests, not canon.** Optical fit and legibility in English/Bulgarian override arbitrary adherence to numeric ratios.

**Spacing vocabulary:** `1u / 2u / 4u / 8u`, with fine `0.5u` adjustments as needed. Default card padding `3u` (trial), gap `2u` (trial), softened radius `2.4u` (trial). Keep media radius as a separate token. Prefer repeated layout dimensions and deliberate whitespace over dozens of individually tuned offsets.

## Implementation notes

- In vanilla JS/HTML a small central icon registry can emit named Lucide SVGs, or use the official `lucide` package/runtime. Do not manually paste divergent path data across every component.
- Keep source SVG assets as an option for export and print; don't require a network call to show core navigation icons in production.
- Keep icon names/semantic assignments in **data**, style in CSS tokens, and component layout in Card/Object.
- For real interactive controls, icons alone require accessible text/labels, title/tooltip as appropriate, keyboard focus and sufficient targets.
- Protect the legal notices when bundling Lucide SVG assets.

**Decision boundary:** Lucide remains the preferred functional UI icon family **and** the selected shared visual vocabulary for per-app PWA launch symbols. It does **not** approve a single universal launcher glyph, a final bespoke TA umbrella logo, A/B imagery generator, finished type ramp or production UI kit. See [APP_ICONS.md](APP_ICONS.md).