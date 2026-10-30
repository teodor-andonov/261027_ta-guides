# TA Guides — consolidation roadmap

Updated 2026-10-27

## Objective

Merge the former Repo Guidance and Graphic Design System into an informal, expanding personal guides collection, while preserving meaningful source documents and working examples. No automatic deployment.

## Migration checklist

- [x] Confirm destination is renamed Repo Guidance and preserve its existing history.
- [x] Inventory Graphic Design System and establish exact source revision `8401953fa587b4d5ccd5dbedf9279ddec6ad8c64`.
- [x] Import design guide documents, historic brand and direction decisions, source overview and JSON tokens.
- [x] Move copyable repository template into `templates/repository/` and add the agent project memory guide.
- [x] Bring across HTML/SVG design boards, app icon editor and JSON preset.
- [x] Replace repository README and AGENTS with TA Guides-wide entry points.
- [x] Originally built a standalone HTML landing page; **reversed 27 Oct 2026** to keep files-only navigation.
- [x] Verify moved Markdown links (92 resolved; one intentionally illustrative sample screenshot link in the repository-memory guide).
- [x] Parse design tokens and icon preset JSON; confirm the repository template is self-contained and present.
- [ ] Run interactive browser checks for the visual boards and Icon Studio (not performed in this migration; source paths and JSON statically validated).
- [x] Merge migration branch and confirm `main` content: [PR #1](https://github.com/teodor-andonov/261027_ta-guides/pull/1), merge commit `f40edf857d24ef5dfd641f614b0b04154074898c`.

### Validation performed on 27 Oct 2026

- Markdown: 92 valid relative links; one illustrative placeholder screenshot link is intentionally absent.
- HTML: 24 local href/src targets checked, none broken.
- TOKENS.json and launcher preset parse as JSON.
- Historical: replaced the old redirect with a visual index, subsequently removed in the website rollback.
- Icon Studio documentation href points to the migrated guide.
- Interactive browser controls, exports and installed PWA behaviour were NOT tested.

## 27 Oct 2026 — files-only simplification

- [x] Remove the generated-site build script, GitHub Pages workflow, website stylesheet and website-specific README.
- [x] Remove the root HTML homepage and its now-unnecessary root `.gitignore`.
- [x] Restore README to GitHub/local-folder navigation.
- [ ] Disable GitHub Pages in repository Settings to unpublish the previously deployed website (requires owner administration; not possible via the available connector).

## After the merge

- New guide domains are added **only** when useful content exists, not proactively.
- Refine individual guides and visual examples in later cycles without losing the original provenance.
- Keep source Graphic Design System repo available as historical archive.
- Keep TA Guides file-first; website generation and publishing were explicitly rolled back on 27 Oct 2026.

## 2026-10-27 — Flat studies

- [x] Flatten `studies/` into dated study folders without category nesting.
- [x] Preserve all original SVG/HTML study assets and move relative references.
- [x] Keep the App Icon Studio timestamped tool folder unchanged.

## 29 October 2026 — Shared PWA/runtime and publishing separation

- [x] Add dedicated PWA identity, icon integration, offline isolation and update UX guidance.
- [x] Move publishing into its own guide area, retain the old link as a pointer, and connect repository/visual/PWA guides.
- [x] Add reusable local update templates and app-aware activation tests.
- [x] Apply the icon family and update UX to the five owner-selected apps; preserve their release policy.
- [x] Validate all 20 PNG dimensions, all five offline launches, installability and two-version update behavior locally.
- [ ] Record final live release verification in the session log.
- Actual Windows/Android installed-icon refresh remains a separate device check; no physical device acceptance is claimed.
