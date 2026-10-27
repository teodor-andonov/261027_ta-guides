# IMAGERY — TA Generated Graphic Language

**Status:** consolidated visual brief, 12 October 2026  
**Current model:** two related families generated from the same modular source grammar. The concept is selected; particular outputs and diffusion settings are still under aesthetic development.

## 1. Why this system exists

TA imagery should feel like **computation made visible**, not generic algorithmic decoration. It represents architecture, geometry, making and systems through simple controlled forms. The core is **fused orthogonal modules**, described in earlier discussions as a *monochrome filleted raster abstraction*, *rounded rectilinear morphology* or *system glyphs*.

Desired tension: **modern / futuristic, yet faintly ancient or mineral**. Achieve that by form, negative space, quiet grain, erosion and controlled diffusion, not faux stone textures or historical pastiche.

**CORE visual DNA:**
- Mostly 2D, orthographic, flat; no perspective as the default.
- Clear square/pixel/grid relationship; rounded-square or rounded-rectangle vocabulary.
- Merge occupied modules into a connected shape with consistent, generous fillets.
- Asymmetrical but deliberate composition, enough negative space to read the form.
- Black/near-black, white/off-white and intermediate mineral grays.
- Minimal, local, fine grain / dither / halftone when warranted.
- Crisp edges in structural glyphs, with softness reserved for the field/texture layer.
- No text inside brand-art output. Text and labels are separate compositional Objects.
- Neither 3D sculpture nor liquid blobs, glows, glossy materials, shadow-driven volume, decorative gradients or random AI-art atmospherics.

## 2. The two image families

| Property | A / Vector glyphs | B / Soft abstract fields |
| --- | --- | --- |
| Role | Identity, icons, symbols, isolated elements | Backgrounds, atmosphere, hero/section fields |
| Geometry | Small rounded modules, connected/fused | Same underlying grammar, often larger units/denser or magnified |
| Edge | Crisp vector fillets | Selective blur/diffusion/soft edges |
| Texture | None or fine localized mineral grain/halftone | More grain, dither, threshold artefacts |
| Space | Strong figure/ground and silhouette | Spatial field, distribution and controlled abstraction |
| Typical output | SVG, optional rasterized export | Raster/canvas export, optional layered SVG source |
| Use together | A overlays B, with sufficient contrast and clear hierarchy | B supports A and editorial text without competing |

**CORE use examples:**
- **Service card:** B as restrained background, A as explicit icon/mark on top.
- **Landing hero:** B as atmospheric field, A as symbolic logo/glyph with text as separately typeset content.
- **Section marker / metadata:** often A alone, or no imagery at all.
- **Project image:** real project imagery should not be replaced wholesale by a generic B field.

The family distinction is a treatment continuum, **not two disconnected visual codes**.

## 3. Geometry and morphology

Start with an authored or seeded base **square grid**. An occupancy map selects cells. Each occupied cell contributes to a union of modules; merge contiguous regions so internal grid boundaries are not visible as arbitrary seams. Round exterior and appropriate internal corners consistently.

Geometry vocabulary:
- Rounded rectangles/squares, connected arms, stepped orthogonal edges.
- Aggregation of adjacent cells, holes/voids, local density transitions.
- Tangency, adjacency, proximity, deliberate gaps and edge relations.
- Grid orthogonality before any erosion/softening stage.
- Negative space may define the symbol as much as the occupied material.

Visual rule: **the silhouette should remain intelligible in flat monochrome before texture.** If texture is doing all the work, simplify the geometry.

Use distinguishable scales:
1. **Module:** one elementary cell/pixel.
2. **Morphology / Glyph:** a shape assembled from modules.
3. **Field:** a spatial arrangement or softened accumulation of morphologies.
4. **Atlas:** a coherent collection/systematic taxonomy of related forms.

This MODULE → MORPHOLOGY → FIELD → ATLAS sequence was accepted as a productive framework for a v0.1 imagery system. It is a creative taxonomy, not a claim that a finished software generator implements every level.

## 4. Texture / diffusion explorations

### Selected shortlist, not all final presets

- **A1 — Clean Mineral:** clear geometry, restrained slight grain; suitable baseline.
- **A2 — Rounded-square Halftone:** localized halftone/dither acting as signal/resolution, not wallpaper.
- **B2 — Diffused Fusion:** modules merge and soften selectively.
- **B3 — Threshold / Artefact:** subtle loss of fidelity, grain/threshold effects used as a visual transformation.

### Two competing diffusion behaviours

**Option 01 — Proximity Diffusion**

Diffusion appears where forms/edges are close or nearly touch. **Near = diffuse; isolated edges stay comparatively crisp.** This makes softness relational and gives the graphics a computational cause. Earlier recommendation favoured this as primary.

**Option 02 — Soft Field Diffusion**

A broader, ambient softening field affects areas across the composition. It should be diffuse but **must not look like a cast shadow, glow or photographic depth of field**.

**OPEN:** the final selection/ratio of Option 01 and Option 02. We compared them repeatedly; image-generation attempts did not reliably satisfy the prompt. Do not represent a poor generated moodboard as approved visual evidence or pretend the choice has been conclusively locked. A reasonable technical experiment is to expose both modes and compare them against the same underlying geometry.

### Comparative visual board

The repeatedly requested inspection matrix:

| | Light Object | Dark Object | Light Background | Dark Background | Hybrid |
| --- | --- | --- | --- | --- | --- |
| Option 01 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Option 02 | ✓ | ✓ | ✓ | ✓ | ✓ |

Use **identical geometry/seed, frame and layout** across variants; only change the tested diffusion, foreground/background and treatment. Present as a clean Swiss/editorial research board with legible labels **outside** the artwork. Comparing randomly different forms is not a valid test.

## 5. Suggested generative pipeline

The October 2026 single-HTML generator exploration arrived at a shared sequence:

~~~text
INPUT / SOURCE
    ↓
GRID + DETERMINISTIC SEED
    ↓
CELL OCCUPANCY / DISTRIBUTION
    ↓
BASIC MODULE GEOMETRY + PER-CELL ROUNDING
    ↓
MERGE ADJACENT MODULES
    ↓
POST-MERGE CORNER ROUNDING
    ↓
PROXIMITY / SOFT-FIELD TRANSFORMATION
    ↓
LOCAL DITHER + MINERAL GRAIN / THRESHOLD
    ↓
COLOUR / INVERSION / CROP
    ↓
SVG / PNG OUTPUT
~~~

Treat source geometry as the common dependency. A is a more crisp/vector outcome; B increases module scale, field softening and textural treatment. Avoid implementing two unrelated random shape generators.

**Geometry caveat:** earlier one-file prototypes approximated true merging / post-union rounding. Any production implementation must distinguish mathematically clean unions and fillets from visually acceptable approximations. A visually convincing raster output is not proof of correct vector topology.

## 6. Generator parameter inventory

The user's directly requested parameters were:

| Parameter | Meaning |
| --- | --- |
| Canvas width, height (px) | Composition dimensions |
| Pixel/cell size (px) | Base grid resolution |
| Pixel density (%) | Occupied portion / density control |
| Pixel corner rounding (%) | 0 = square, 100% = circular/dot-like |
| Pixel scale | Module size relative to nominal pixel size; 1 = equal |
| Post-merge rounding (%) | Radius treatment on combined silhouette |
| Blur circles count | Number of local field-softening regions |
| Blur circles XY position seed | Reproducible field positions |
| Blur radius scale (%) | Relative softening region size |
| Blur strength | Softening intensity |

Additional controls discussed during the v0.1 generator:
- Overall seed and alternate seed values for source vs treatment
- Blur falloff / mode (relational or ambient)
- Grain strength/scale; dithering/threshold
- Foreground/background inversion and grayscale mapping
- A/B preset and image type
- Export dimension/format; preserve/reload parameter preset

**PREFERRED:** deterministic, repeatable outputs. Same inputs + seed should produce the same result. Store parameters with the output, not just exported PNGs. Keep control ranges in a future implementation explicitly **TRIAL** until visually tested.

### Generator UX

A **single-file HTML prototype** was explicitly requested and a v0.1 version was explored. It used live sliders, numeric values, basic presets, seeded states and export concepts. The UI itself should be extremely minimal: black/white, mono labels, fine separators, canvas dominant; no elaborate app shell to obscure the experiment.

This repo does **not** yet contain that generator. The existence of an earlier experimental HTML artifact elsewhere is not a claim of current source or visual fidelity here.

## 7. Image production roles

### Symbol / isolated foreground A

- Transparent or quiet field.
- Clearly legible silhouette, generous free space.
- Avoid pseudorandomly tangled grids and arbitrary protrusions.
- Should work both inverted (light on dark) and normal (dark on light).
- Test reduction to icon scale; complex symbols may need simplified variants.

### Background B

- Text contrast and safe area come first.
- Texture should have spatial hierarchy, not uniform coarse noise.
- Blur must feel like an authored field property, not a Photoshop drop shadow.
- Monochrome light and dark variants.
- Can be cropped to cards or hero aspect ratios; preserve the important morphology.

### Hybrid

- A and B must be distinguishable as figure and field.
- Use an explicit separation principle: contrast, scale, placement, local clearing or density reduction.
- Typography always belongs to the page composition; do not bake headlines into raster assets.

### Architectural photos and renders

Different class of media. Retain native colour, credits and truthful visual content. Choose crop, placement and nearby fields in accordance with the graphic system, but do not unnecessarily recolor all real work to monochrome.

### Diagrams

Diagrammatic SVGs are first-class Graphic Objects but not automatically part of the generative A/B family. Allow informative coloured linework, fills, legends and labels. An October palette trial used HSL 60 / 150 / 240 / 330°, S=50%, L=50%, with lighter related tones; it is **trial diagram color**, not a mandate to colour the identity artworks.

## 8. Quality criteria

Evaluate every output at three scales: overview/thumb, normal presentation size and enlarged crop.

**Pass:**
- The underlying grid/fused geometry is legible.
- The frame feels intentional, with useful negative space.
- Rounding appears consistent and deliberate.
- The softness belongs to the field, not a shadow behind objects.
- The grain seems intrinsic/material and not a noisy overlay.
- There is strong figure/ground hierarchy in both light and dark modes.
- B remains suitable behind actual editorial text.
- Two outputs from one family look related without appearing duplicated.

**Fail:**
- Soft, colourful, organic blobs.
- Inflated 3D clay, glass, liquid or glossy material.
- Literal ruins/stone textures; fake 'ancient' ornament.
- Uncontrolled gray smudge or Gaussian blur on everything.
- Decorative halftone spread evenly across the whole image.
- Random geometric wallpaper with no form hierarchy.
- Pixel cells whose seams remain visible when the stated intention is fused geometry.
- Heavy outlines or faux depth replacing the geometric logic.

## 9. Practical next experiment

Use the same seed and a small reproducible set of 3–5 morphologies. Make crisp A glyphs; make two versions of B (Option 01 and Option 02); test the five light/dark/hybrid compositions. Inspect at 1600px reference width and at intended card/icon sizes. Only then lock numeric presets or produce a large identity atlas.

No generated image examples have been committed to this repository yet; this file is the specification against which they should be judged.