# APP_ICONS — TA Application Launcher Identity

**Status:** family rule recovered from 21 October 2026 conversation; practical PWA packaging guidance added 27 October 2026.  
**Scope:** independent TA apps, Windows/Android-installed PWAs, favicon/browser tabs, launchers and app listings.  
**Related:** [ICONOGRAPHY.md](ICONOGRAPHY.md) covers ordinary action/interface icons. An in-app **product identity mark** must use the same canonical geometry as its installed PWA icon. Packaging, caching and update requirements live in the separate [TA PWA guide](../pwa/README.md).

## Interactive design tool — TA Icon Studio

**[Open/download the HTML Icon Studio](../../tools/261027-1116_app-icon-studio/app-icon-studio.html)** — standalone editable-browser experiment, created 27 October 2026. Open the **downloaded HTML file** in a modern browser; GitHub's file view shows source rather than running the app.

The tool lets you select the family icons or search/load other Lucide names, adjust **stroke weight, icon scale, X/Y offsets, icon/background colours, background corner radius and transparent background**, inspect **desktop, circular Android-maskable and favicon-size previews**, and export **SVG, 192/512 PNG, maskable 192/512 PNG, 64px favicon**, plus a JSON settings preset.

The editor loads authentic Lucide geometry from a **pinned `lucide-static@1.61.0` CDN**, so an internet connection is needed when first selecting an icon. After that, **downloaded icons are self-contained SVG/PNG files**. This tool uses localStorage for convenience and JSON import/export for portable, reproducible settings. It is an **experiment/asset-export tool**, not an automatic modification of the actual app manifests or service workers.

**Preview/export behavior:** regular exports honour adjustable tile corner radius/transparency, while **maskable PNGs always use a solid square background with a centred glyph at no more than 54% of the square** to protect the guaranteed central safe zone. Maskable exports intentionally ignore custom X/Y offsets. The latter behaviour is an implementation safety choice, not an established brand-token standard.

## Selected shared launcher preset — approved 27 October 2026

**Source of truth:** the owner's uploaded [TA Icon Studio configuration](../../tools/261027-1116_app-icon-studio/ta-app-icon-default.json). These are **approved current defaults** for all TA app launcher icons, while each app's Lucide glyph remains distinct.

| Property | Shared value |
| --- | --- |
| Lucide symbol | App-specific — Sourcebook `library-big`, Notebook `notebook-pen`, Objectbook `blocks` |
| Stroke width | **2.0** on Lucide 24×24 coordinate system |
| Icon scale | **60%** of launcher square (regular export) |
| Launcher background rounding | **25%** of tile width, used as CSS/SVG corner-radius percentage |
| Icon/stroke colour | **`#333333`** |
| Background/tile colour | **`#E6E6E6`** |
| Icon offsets | **0% X / 0% Y** |
| Transparency | **Off** — opaque tile |
| Safe-area guide | Off by default; available for checking |
| Lucide version recorded by preset | `1.61.0` |

**Current rule:** use the **same monochrome style across the app family** for now. Later, individual apps *may* get a unique colour either on the icon or the background—but this is a **future option, not an active style variation**. Do not apply app-specific colours until selected.

**Android maskable assets differ from regular preview tiles:** the export tool uses a **solid square** background, OS-controlled rounding, and a centred glyph clamped to **54% of the square** for safer masking (so a selected regular 60% scale becomes 54% on that export). The adjustable offsets do not carry into the maskable export. This is tool behaviour, not a contradiction of the 60% shared regular-launcher choice.

**Icon Studio behaviour:** the HTML tool now opens with these values as a new local default (`v2` preference namespace), and its **TA Default** action reapplies this shared style while keeping the selected Lucide symbol. Older experiments can still be re-imported from their JSON. Exported PNG/SVG files still require separate deployment and manifest updates in the target PWA repos.

## Current five-app registry — 29 October 2026

| App | Repository | Canonical Lucide 1.61.0 glyph |
| --- | --- | --- |
| TaGraphicpad | [261028_gaphic-pad](https://github.com/teodor-andonov/261028_gaphic-pad) | `pen-tool` |
| TaSourcebook | [261025-2132_sourcebook](https://github.com/teodor-andonov/261025-2132_sourcebook) | `library-big` |
| TaMindmap | [261019-1740_pwa-mindmap](https://github.com/teodor-andonov/261019-1740_pwa-mindmap) | `network` |
| TaViewsvg | [ta-svg-viewer-261012](https://github.com/teodor-andonov/ta-svg-viewer-261012) | `scan-eye` |
| TaCodegraph | [ta-cad-graph-261012](https://github.com/teodor-andonov/ta-cad-graph-261012) | `workflow` |

The four pre-existing symbols and their 27 October launcher assets already follow the approved preset. Graphicpad now joins the family with `pen-tool`, selected for its vector drawing purpose. App identity marks inside the UI, launchers and favicons use the same per-app artwork; ordinary action icons remain functional controls. Each authoritative source checkout retains its canonical geometry and export method. Graphicpad and Sourcebook use their local-source release policies rather than hosted icon automation; source-hosted apps retain their existing asset workflows.

**Historical rollout:** on 27 October four repositories received their source SVG, regular/maskable PNGs, manifests and generation workflows. Live publication and OS icon refresh were not confirmed by that earlier audit. Release policies have since evolved; consult each repository, rather than inferring its current policy from that dated rollout.

## 1. Decision and provenance

The **21 October 2026** app-family discussion established a **shared Lucide outline icon language** for three independently named products. The then-current family was Sourcebook / Sketchbook / Objectbook; Sketchbook was subsequently called **Notebook**. The associated selected icons remained the same:

| Application | Lucide name | Identity | Status |
| --- | --- | --- | --- |
| **Sourcebook** | [library-big](https://lucide.dev/icons/library-big) | Indexing, sources, libraries | **SELECTED** 21 Oct |
| **Notebook** | [notebook-pen](https://lucide.dev/icons/notebook-pen) | Writing, notebooks and sketching | **SELECTED** for former Sketchbook, carried into Notebook |
| **Objectbook** | [blocks](https://lucide.dev/icons/blocks) | Objects, relationships and composition | **SELECTED** 21 Oct |

**Family rule — APPROVED:** TA apps should have **distinct per-app symbols from one consistent Lucide vocabulary**, rather than three copies of a single TA mark or three unrelated decorative designs. Follow the same approach by default for newly deployed TA PWAs; choose each new symbol deliberately and record it here.

The previous discussion referenced **Lucide v0.456.0** and an in-interface **\`xl\` / approximately 24 px** presentation. Those are evidence of the **UI icons** as chosen; they do **not** lock the scale of a 512px launcher asset or prove that the original conversation approved a particular launcher background, mask shape or raster export format. All three named icon identifiers have been confirmed in the official Lucide catalogue. Pin whichever compatible Lucide version is used **per app** for repeatable exports. Do not automatically upgrade or change icon geometry across a family without visual comparison.

**Prior related decisions:**
- **13 October:** Lucide preferred for ordinary interface/service/diagram icons, distinct from future bespoke **TA A/glyph** and **B/field** artwork.
- **September PWA workflow:** each deployed app can be an independently installable PWA with its own manifest, name, URL/scope, start URL and icon assets; the portable single-HTML content/editor may remain separate from that deployment layer.
- **27 October:** explicitly extend the per-app Lucide symbol approach as the **default installed PWA launcher identity** for future TA deployments. The export/manifest specification below is *new implementation guidance*, not recovered wording from 21 October.

## 2. The visual contract

### A / Symbol (approved family approach)

- Use the **selected, canonical Lucide SVG path**, never a loose hand-drawn lookalike.
- **Outline**, **no fill** *on the glyph itself*, **rounded line caps and joins**, visual **stroke-width ≈ 2** on a 24×24 Lucide viewBox. Earlier family discussions used about 2; the Soft Precision UI experiment used 1.75 as a separate **trial**. Treat these as different contexts; do not silently overwrite app-icon strokes with a universal 1.75.
- Achromatic/monochrome. In normal UI usage the icon can inherit the application's theme text colour via \`currentColor\`. Exported PWA assets must use actual **resolved colors**, because manifest PNG/SVG cannot depend on another document's CSS \`currentColor\`.
- Keep the symbol recognisable at 16–32px, and optically centred within the launcher icon.
- Avoid arbitrary hand-added badges, product initials, coloured gradients, drop shadows or different outline families unless deliberately approved for a particular product.

### B / Tile, background and platform treatment (new **TRIAL**, not a recovered choice)

The **21 October** icon-selection decision **did not yet establish** a tile or padding specification. The owner's **27 October uploaded Icon Studio preset has now approved** the shared regular-launcher colour, scale and rounding above. The notes below concern remaining platform-specific export choices.

For implementation, **retain** these platform guidelines alongside the approved colour/style preset:
- Use the **confirmed monochrome `#E6E6E6` field and `#333333` glyph** for the current regular app icon family. Alternate app-specific colours remain **open/future**.
- Round corners via **OS masking** when installed; do not bake a strong rounded-corner crop into the full exported square and then let Android round it a second time.
- Keep the full glyph inside a **maskable safe area**. For a 512px square, a centrally located circle of radius 204.8px (40% of width) is guaranteed visible; important strokes and extremities must not cross this boundary.
- A maskable icon should have a fully **opaque field**; a normal \`any\` icon may be separately optimized for desktop or transparent use. Do not assume a transparent SVG alone is a sufficient Android launcher asset.
- Keep all app tiles recognisably related. Distinct names and icons remain legible if devices use themed icons or system-defined adaptive shapes.

### C / Separate design roles

1. **UI icon**: scalable Lucide SVG, using \`currentColor\`, 16/20/24/32px controls, accessibility label from surrounding button text.
2. **App launcher icon**: **self-contained exported artwork**, defined by that app's manifest and installed by Android/desktop.
3. **Favicon/tab icon**: small, often simplified SVG/PNG/ICO derivative of the same app symbol.
4. **Optional product logo/wordmark**: separate identity task; do not assume a Lucide icon is a registered product logo.
5. **TA brand artwork**: future A/B generative visual system, distinct from the functional app-symbol family.

**Do not confuse the Lucide library icon named \`app-window\` used to illustrate the general _Apps_ navigation section with the distinctive Sourcebook/Notebook/Objectbook launcher symbols above.**

## 3. PWA packaging and runtime behavior

The [TA PWA standard](../pwa/ta-pwa-standard.md) is now the canonical home for asset deliverables, manifest identity/scope, same-origin cache isolation, offline checks and update prompts. Do not maintain a second technical checklist here.

## 4. Publishing and rollout

The separate [publishing guide](../publishing/README.md) covers branches, review, authorization, Actions and live deployment evidence. Each named app records its actual icon paths and generator in `TA_APP_ICON.md` and its runtime integration in `PWA.md`.

Visual acceptance remains here: recognizable and distinct glyphs, one monochrome family, canonical geometry across in-app and installed identity, clean small-size rendering and no clipping under OS masks. Test actual Windows/Android icon refresh separately before claiming device acceptance.

## 5. Licences and source authority

The [Lucide library](https://lucide.dev/) uses an ISC license, and some icons derived from Feather may also require their applicable MIT notices. Preserve copyright/license notices if redistributing the icons or source files. See [Lucide licensing](https://lucide.dev/license).

Source of truth for the *family decision*: 21 October 2026 conversation, not a claim of a complete technical rollout at that date. Source of truth for PWA packaging: implementation recommendations informed by browser/platform manifest standards.

**Status boundary:** shared Lucide symbols and the monochrome preset are approved current defaults. The current five-app registry records this implementation; publication and browser checks belong in the dated session log. Actual installed OS icon refresh remains device-specific. Optional per-app colors remain open.
