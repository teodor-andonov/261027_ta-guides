# DESIGN — TA Graphic Design System

**Version:** 27 October 2026 — app launcher icon family added to Soft Precision grammar  
**Authority:** current direction, not a verbatim snapshot of one prototype  
**Reading rule:** CORE > PREFERRED > TRIAL; OPEN remains genuinely unresolved.

## 1. Intent and character

**CORE** — This is one coherent visual grammar for websites, applications, diagrams, slide decks, reports, posters and other TA communication. Its purpose is to **make complex design/research legible and visually distinctive** without ornamental noise.

Desired character:

- **Architectural:** geometry, alignment, proportions, boundaries, composition, hierarchy.
- **Computational:** visibly generated structure, modularity, precise variation, traceable rules.
- **Editorial / Swiss:** disciplined grids, clear typographic hierarchy, asymmetry used with intention, useful whitespace.
- **Contemporary with quiet material depth:** flat forms at the structural layer; texture/diffusion only when deliberately authored within imagery.
- **Minimal but not generic:** restraint in interface chrome allows unusual compositions and research images to carry identity.
- **Adaptable:** a method for many formats, not one reusable page template.

Prefer a few strong relations—scale, position, grouping, contrast—over decoration. Do not imitate a default SaaS dashboard or an overly polished generic architecture portfolio.

### Layer separation

1. **System tokens and layout grammar:** stable, reusable rules.
2. **Components and templates:** common arrangements that consume those rules.
3. **Composition:** a particular arrangement of components and objects, sometimes bespoke.
4. **Graphics and imagery:** authored or generated visual content with internal logic.
5. **Publication/content:** the actual projects, articles, images, metadata and pages.

A graphic is not automatically a layout component; a component is not automatically a page; a project record is not styling.

## 2. Naming and identity

- **CORE:** public umbrella identity **TA / Teodor Andonov**.
- **Historical confirmed descriptor:** **Design, Architecture, Computation**, in that order, was explicitly accepted in February 2026. It remains a safe formal descriptor; later mockups also use **Architecture / Computation / Research** as contextual language, not necessarily a formal replacement.
- **CORE:** the brand is broader than any one service or product; it covers personal portfolio, independent practice, publishing, tools and research.
- **OPEN:** the final independent studio/offer name. METOD, SREDA, OSNOVA, REDIA, GRADIA and others have been explored; do not silently canonize any of them.
- **OPEN:** final standalone logomark. Earlier orbit/bear and wordmark trials are **historical**. The current rounded modular glyph language can be used to investigate a mark but is not itself an approved logo.

Use naming and labels as part of clear editorial information architecture, not as an excuse for heavily branded decoration.

## 3. Composition grammar: Card / Object

**CORE — latest working model:**

- **Card:** structural container. Owns layout/grid behavior, padding, gap, rounding, optional surface/background, and may contain Objects and nested Cards.
- **Object:** one atomic content payload, or intentional empty space. Owns its position/span within its parent composition, and its own content behavior.
- **Payload examples:** text, image/video, graphic/SVG, interactive control, data view, empty.
- **Root Card:** the page, screen, artboard or authored section's outermost composition. It is a **role**, not a third node type.
- **Group/nested Card:** starts its own local grid or layout context while inheriting shared visual tokens. Recursion should be possible without an arbitrary depth limit in the design model.

**One Object = one content payload.** If you need a headline, paragraph, image and caption placed independently, use multiple Objects inside a Card. A caption intrinsically inseparable from an illustration may remain part of one Graphic, but separately laid-out copy is another Object.

Schematic composition:

~~~text
ROOT CARD
├─ OBJECT: header / navigation
├─ CARD: hero (local grid)
│  ├─ OBJECT: headline
│  ├─ OBJECT: supporting copy
│  ├─ OBJECT: call to action
│  └─ OBJECT: generated graphic A or B
├─ CARD: selected projects
│  ├─ OBJECT: section heading
│  └─ CARD: repeated project items
│     ├─ OBJECT: project image
│     └─ OBJECT: project label
└─ OBJECT: footer
~~~

**Surfaces and styling boundary:**

- Cards are the principal regions carrying backgrounds, padding and rounding.
- Images/Graphics may have their own field/frame and independent media rounding.
- A Text Object should **not** acquire an arbitrary decorative rectangle; wrap it in a surfaced Card when necessary.
- Objects should not independently introduce layout padding, background and shadows that undermine this grammar.
- A transparent Card is still a useful grouping and layout context.
- The Root Card should not be mistaken for an extra full-page margin wrapper; its spacing is a parameter.

**Historical clarification:** a detailed 1 October file used **Box → Object → Content** (where a Box could be nested as Content) and explicitly retired Card terminology at that time. Subsequent website/editor decisions returned to **Card/Object** semantics. Treat these as versions of the same underlying idea; use the latest terms in new website work. Do not introduce both systems as separate competing APIs.

## 4. Grid, scale and layout

### Shared design unit

**CORE:** dimensions derive from a design reference width and a chosen number of divisions:

~~~text
u = reference_design_width / unit_divisions
~~~

For a proportional web canvas, calculate the live unit from the same root/viewer width. Typography, internal spacing, gaps, padding, rounding and placement should be expressed as clear multiples of a **single shared unit** where appropriate. Hairline rules, optical corrections and font-relative line heights are permitted exceptions.

**TRIAL, not locked:** at a 1600px desktop reference, 160 divisions produce u = 10px. Earlier studies also used 1440 / 200 = 7.2px, a 15px base, and fixed 10px base. Those are **not interchangeable defaults**. The formula and consistency are the durable principles.

**PREFERRED:** a reference desktop width around **1600px**, with a 4:3 reference sheet (1600 × 1200) in some explorations. **1600px is the authored reference size, not automatically the site's CSS max-width or content width.** Content margins and usable columns still need their own design.

A global scale should not silently reset inside nested Cards; nested Cards may change local grid divisions but should inherit the same fundamental visual unit. For web, container query length units (cqw) were explicitly explored to make dimensions follow the chosen viewer/container instead of arbitrary viewport percentages.

### Tracks and subdivisions

**CORE:**
- Column/row counts are authored grid controls, not inferred from a desired nominal cell size.
- Use equal bounded tracks when explicit grid assignment is intended.
- Support per-Card local overrides for columns, rows, padding, gap, alignment and rounding without implicitly altering descendants.
- Objects can occupy explicit x/y positions and width/height spans inside their immediate Card, or take an ordered flow position where that is the appropriate component.
- Do not smuggle visual spacing into unrelated margin overrides.
- Composition can be nested and asymmetric; global consistency does **not** require visually symmetrical results.

**PREFERRED:** an eight-column design vocabulary with scale variants **1 / 2 / 4 / 8 / 16** as a responsive/modular family. The 1/2/4/8/16 sequence is a **column-count strategy**, not a list of pixel breakpoint values. The exact mapping from available widths to variants is **OPEN**. Four columns/rows were used as a practical default in the 1 October composition experiments, not a final mandate for every Card.

**TRIAL:** some older web studies used root-width-based section heights (e.g. 0.625 × root width), independent of their inner row count, with 16:9 = 0.5625 and 4:3 = 0.75 as examples. This creates a fixed visual artboard effect. Keep the technique available for authored visual sections but **do not assume every content-heavy page must clip to a fixed ratio**.

### Responsive behavior

**CORE:** preserve predictable, explicitly authored relations rather than generating arbitrary fractional paddings and radii. A web card and its editor representation should obey the **same layout rules**.

**OPEN / needs testing:** whether the entire web page remains a fully proportional miniature at narrow widths (1 October experiment) or selectively reflows to maintain touch targets, readable body type and accessible controls. The current website aims at real public mobile use, so do not silently impose the earlier “miniature / zoom to read” behavior globally. Use explicit mobile overrides where real usability needs them and record them as variants of the same grammar.

A viewer-sizing wrapper can expose an inherited root width with 100cqw; prevent nested query containers from accidentally reinterpreting that unit. CSS Grid / Flex are implementation mechanisms; neither changes the design semantics.

### Negative space and density

Let some regions stay genuinely empty. Use transitions between dense and quiet regions, deliberate asymmetry and readable blocks. Space is a design element, not leftover area.

## 5. Typography

**PREFERRED, latest (October 2026):** **Geist Mono** as the working TA mono family, with English and Bulgarian/Cyrillic checked visually. Typography should be legible enough for substantial reading, not merely technical annotation.

Earlier testing:
- **PT Mono:** particularly liked for Bulgarian.
- **Noto Sans Mono:** considered strong for English.
- **IBM Plex Mono:** explicitly rejected.
- **JetBrains Mono:** main earlier working font; remains a fallback/reference, not the latest first choice.
- **Source Code Pro:** tested.
- **Atkinson Hyperlegible Mono:** investigated, but Cyrillic coverage was a blocker for this use.
- **Arial:** appeared in a medium-specific 1 October composition experiment and a 2026 presentation deck; not the current website font decision.

**CORE:** the visual system should work in both Latin and Bulgarian Cyrillic. Test the **same typography specimen** in both languages, including headings, long paragraphs, numerals, metadata, and a logo/wordmark. Avoid a family that looks elegant in English but compromised in Bulgarian.

Hierarchy is by large, intentional differences in **size, weight, position and whitespace**, not many minor font-style tricks. A single type family across a composition is the preferred baseline. Uppercase tiny metadata, labels, numbering and restrained tracking belong to the editorial vocabulary, but do not make paragraphs artificially tracked.

- Titles/hero: clear large typographic gestures.
- Section headings: visibly secondary but structural.
- Body: actual reading comfort, moderate line lengths.
- Captions and metadata: quiet, precise, linkable to the evidence/image.
- Numerical labels: useful systems language, not meaningless “01 / 02 / 03” garnish.

**OPEN:** final numeric type ramp, body size at mobile, line height, weight mapping and font-loading strategy. Historical ramps (40/20/10px or 44/16/13px) are not current automatic tokens.

## 5A. Soft Precision — selected visual foundation (13 October 2026)

**SELECTED DIRECTION:** **03 / Soft Precision** has been chosen over 01 and 02 as the TA visual starting point. Keep it consistent with the recursive **Card/Object** grammar and true neutral grayscale. The owner specifically likes softened, rounded panels, but found the initial board **too busy, with too many unrelated type sizes and weak rhythm**.

**CORE feedback:**
- Reduce typography variants. Prioritize four recurring roles: **Display**, **Heading**, **Body**, **Metadata**; only override when content/medium genuinely requires it.
- Reuse a small series of spacing steps and one calm, consistent corner system. Don't tune every nested panel independently.
- Use comparable Card padding, repeated vertical intervals, measured proportions, clear alignments and intentional whitespace.
- Keep **strict achromatic grayscale** (no intentional warm hue/saturation) in authored UI and brand surface treatments. Photos and project material retain native color.
- Use **Lucide-style functional line icons** for routine semantic illustrations (services, features, UI, navigational explanation). Brand glyphs and abstract field graphics remain separate and unfinished.
- Avoid large bespoke SVG illustrations just to explain an ordinary feature. Keep SVG for diagrams, technical drawings and distinctive authored image compositions.

**TRIAL numeric rhythm at 1600px reference, u=10px (not signed-off production tokens):**

| Role | Size | Example |
| --- | --- | --- |
| Display | 4.8u / 48px | Hero |
| Heading | 2.8u / 28px | Section/card heading |
| Body | 1.6u / 16px | Paragraph |
| Metadata | 1.2u / 12px | Caption/index |
| Spacing | 1u / 2u / 4u / 8u | Repeated rhythm |
| Card padding | 3u / 30px | Structural panel |
| Card gap | 2u / 20px | Siblings |
| Card radius | 2.4u / 24px | Soft surface |
| Icon standard | 24px, 1.75 stroke (trial) | Semantic illustration |

The chosen direction is **not** proof that those exact numbers work across web, print, desktop and mobile. Validate them on real English/Bulgarian copy and multiple formats. Icon sources, semantic mapping and integration guidance are in [ICONOGRAPHY.md](ICONOGRAPHY.md).

### App launcher identity — separate from interface iconography

**CORE (21 October 2026, reiterated 27 October):** standalone TA apps use **individual Lucide outline symbols** as a coordinated family of app/installed-PWA icons: Sourcebook `library-big`, Notebook `notebook-pen`, Objectbook `blocks`. Use the same system for future PWAs, assigning each its own readable Lucide symbol.

This is **not** one Lucide icon reused for every app; nor is it a proposal to replace the personal TA brand logo. A user-facing icon inside a Card, the installed PWA launcher, and the favicon share an icon identity but require **different actual assets and platform treatment**. Preserve the Soft Precision grayscale language; PWA launcher background/padding/masking remain implementation trials. The icon set must be locally available for installed apps, not dependent on a runtime CDN.

For actual app-icon names, sample manifest entries, maskable safe zones, file formats and rollout guidance, see [APP_ICONS.md](APP_ICONS.md).

## 6. Colour and surfaces

**CORE:** a primarily **monochrome / grayscale** identity, with light and dark inversion supported. Quiet off-whites, mineral greys and near-black are preferred. Contrast should be created through hierarchy and substance—not generic gradients.

**TRIAL neutral mapping from October studies:**
- White: #FFFFFF
- Soft/light: #F2F2F2 (also warm mineral #F2F2F0 in imagery work)
- Light-middle: #CCCCCC
- Mid: #999999
- Ink: #333333
- Deep image dark: approximately #080808 in some artwork studies

These are useful known examples, **not an approved final colorimetry standard**. Light text, muted labels and focus indications must be contrast-tested on their real surfaces.

**Historical accent palette** (from May, still usable sparingly for system/index semantics rather than the core artwork):
- Blue #3F55C0
- Green #40BD6A
- Magenta #C04196
- Gold #C0AA3F

**October diagram/illustration palette experiment:** HSL hues 60°, 150°, 240° and 330°, with 50% saturation / 50% lightness plus lighter variants. This applied to **drawn/diagrammatic imagery**, not photographs and renderings. It does not supersede the grayscale-first brand identity.

**CORE distinction:** authored UI surfaces, labels, symbols and graphic diagrams use deliberate system colors; photographs and architectural renderings normally **retain native color**. Colour can carry a semantic category or project identity; it should not make a random collection of unrelated bright shapes.

Avoid heavy borders, glowing surfaces, ornamental shadows and false depth. Fine neutral separators/hairlines can clarify an interface; structural Cards need not all be outlined. In some early studies touching boxes and faint boundaries were useful; in later studies surface differentiation and whitespace often did more.

## 7. Corners, outlines and depth

**CORE:** rounding is a real and **independently controllable** parameter, not hardcoded incidental styling. Cards and media may use different radii. Explicitly retain this in any future visual authoring UI.

**TRIAL:** 2u Card radius and 2u media radius were recommended in October 1 study; ~14px cards appeared in a later mockup; older versions tested 5px/10px. No one radius has been universally locked.

- **Structural regions:** quiet rectangles, possibly rounded by one consistent system parameter.
- **Image/video fields:** crop or contain with their own radius.
- **Generated fused modules:** deliberate corner morphology is a different control from a Card corner.
- **Graphic lines:** useful for real diagrams/annotations; not heavy decorative outlines around the identity glyphs.
- **Depth:** flat editorial base. Avoid permanent drop shadows, shiny/neumorphic effects, strong glassmorphism, extrusions and glossy 3D.

The image family's localized blur and grain are **not** permission to blur ordinary UI controls.

## 8. Graphics vs images

**CORE:** a **Graphic** is one authored drawing—SVG diagram, plot, annotation, map, schematic, logo or generative 2D illustration—placed as a single Object in a Card. Its internal geometry uses its own local coordinate system/viewBox and **does not inherit the parent's Card grid**.

- Use SVG when geometry, precise linework, symbols and authored compositions benefit from vectors.
- Keep internal graphic text only if labels are intrinsic to the drawing.
- Use separate Text Objects for independently laid-out titles, captions, legends, metadata and calls to action.
- Compose a multi-object explanatory section in a Card; do not overstuff one enormous SVG with normal page UI.
- When imagery fills a fixed frame, use cover/crop intentionally; when detail/labels must remain visible, choose contain.
- Author a safe subject area in cropped images. Test all intended aspect ratios.

**Image brief:** define **Content → Treatment → Composition**. Clarify whether an image is a photograph/render, project drawing, explanatory diagram, texture field or brand glyph; do not treat these classes as interchangeable.

**PREFERRED presentation pairing:** HTML/CSS handles readable/responsive interfaces and repeated content; SVG can handle very deliberate fixed artboard-like graphic sections. The user explored both hybrid HTML/SVG sections and all-HTML reconstructions. Neither obliges the design system to be “SVG-only.”

Full specifications for A/B image families live in [IMAGERY.md](IMAGERY.md).

## 9. Components and visual patterns

The grammar is intentionally more fundamental than a giant component catalogue. Common compositions may be promoted to named reusable components once justified by repetition:

- Page shell / header / navigation / footer
- Hero (headline + image field or symbolic glyph)
- Text group, section label, metadata cluster
- Project card, project grid, image grid, gallery
- Article/post card and index (posts include articles, notes, news and shorter records)
- Services / modes of work
- Graphic panel / captioned diagram / annotated study
- Form controls, primary/secondary action and 15-minute-call CTA

**CORE:** share components between an authoring interface and rendered website, rather than maintaining a separate “looks similar” editor version. The special root Card and nested Cards should keep their controls for grid, gap, padding and radius. A specific page may use reusable patterns or a freely authored tree of Cards/Objects.

**CORE:** no compulsory decorative background on each component. A completely flat surface and whitespace often yield stronger editorial structure than multiple nested cards with borders.

**OPEN:** canonical naming of component variants, numeric component spacing, component catalogue, interaction visual tokens and any dedicated component authoring UI. Earlier use of data-* attributes for settings is a sensible implementation precedent, not a mandated public JSON schema.

## 10. Interaction and accessibility

The design should not fail when used rather than viewed.

- Use semantic HTML for navigation, controls, headings and reading order.
- Keep focus visible; dark/light monochrome styling must not obscure keyboard affordances.
- Do not encode status by color alone.
- Make controls and type usable on smaller screens even if the initial layout study used scale-to-miniature behavior.
- Expose meaningful alt text and appropriate captions/credits for media.
- Animation belongs to content/illustration and should be restrained, with reduced-motion handling.
- Selected, hover, disabled, expanded and focus are **states**, not new visual object kinds.
- Check text wrapping/overflow; hiding overflow may hide errors rather than solve them.

## 11. Formats beyond the website

**CORE:** the same token logic and Card/Object composition should inform websites, app UIs, slides, posters and design reports. The actual medium changes readability, dimensions, scale and cropping.

### Websites / content studio

- The website and editor should consume the **same component/layout logic**.
- The latest **website authoring** decision is **JSON as source of truth** for pages, projects, posts/articles, assets and compositions.
- A small number of broad JSON files is fine; do not require one file per item.
- Content is edited through a polished table/visual editor when built; it must persist valid JSON, not a disconnected visual mockup.
- Support templated pages, reusable collections and genuinely custom layouts using the same renderer.
- Standard project and post pages should be generated from records, not manually copied HTML.
- Native HTML/CSS/JS, JSON and SVG are the favoured simple web stack. Do not add a framework, a CMS or unnecessary build tooling just to express this grammar.
- This repository owns **design rules**; the website repository owns **content data and publishing code**.

### Presentations / reports / graphics

- Compose a page/slide as a fixed artboard with known width/height, and export it proportionally. 16:9 and 4:3 are formats, not new grammars.
- Favor large imagery, short specific text, calm metadata/footers and one principal message per slide.
- Reports may be denser than presentation slides without changing their editorial DNA.
- An earlier independent presentation deck used Arial and a neutral monochrome system; that medium-specific implementation is a reference, not an override of the later mono website direction.
- Respect safe reading distances, page boundaries, print scaling and color reproduction rather than relying blindly on CSS px.

## 12. Authoring / review checks

Before accepting any mockup or new reusable component:

1. Is the Card/Object hierarchy visible and unambiguous?
2. Does each Object have one content payload?
3. Are grid, pad, gap and radii consistent and locally overrideable?
4. Are the root dimensions, shared unit and local grids used consistently?
5. Does the composition work in both English and Bulgarian?
6. Are photographs still photographic, diagrams still diagrammatic, and brand art still brand art?
7. Are crop, contrast, alt text, reading order, focus and motion handled?
8. Does the typography create hierarchy through proportion, not decoration?
9. Are unusual choices genuinely authored rather than arbitrary one-off CSS?
10. Have **TRIAL** numbers and imagery modes been visually inspected instead of prematurely ratified?

## 13. Explicit non-goals and anti-patterns

- Not a complete web framework, CMS, component generator or implementation library.
- Not a system of colorful organic gradient blobs or generic futuristic 3D.
- Not permanently “no diffusion”: targeted diffusion belongs **inside image family B**, not UI chrome.
- Not one universal fixed grid or fixed web section ratio regardless of content.
- Not automatic forced borders around every Card.
- Not a typographic system that only works in English.
- Not one-page-per-JSON-item bureaucratic overhead.
- Not separate, incompatible renderer rules for website and content editor.
- Not invented numeric certainty: unanswered presets and breakpoints remain **OPEN**.

**Design test:** if the same simple rules cannot produce both a sober architectural report and a distinctive computational hero, the system is either too decorative or too restrictive.