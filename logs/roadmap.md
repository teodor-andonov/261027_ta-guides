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
- [x] Build a small standalone HTML guide landing page.
- [x] Verify moved Markdown links (92 resolved; one intentionally illustrative sample screenshot link in the repository-memory guide).
- [x] Parse design tokens and icon preset JSON; confirm the repository template is self-contained and present.
- [ ] Run interactive browser checks for the visual boards and Icon Studio (not performed in this migration; source paths and JSON statically validated).
- [ ] Merge migration branch and confirm `main` content.

### Validation performed on 27 Oct 2026

- Markdown: 92 valid relative links; one illustrative placeholder screenshot link is intentionally absent.
- HTML: 24 local href/src targets checked, none broken.
- TOKENS.json and launcher preset parse as JSON.
- Old auto-redirect replaced with the visual index.
- Icon Studio documentation href points to the migrated guide.
- Interactive browser controls, exports and installed PWA behaviour were NOT tested.

## After the merge

- New guide domains are added **only** when useful content exists, not proactively.
- Refine individual guides and visual examples in later cycles without losing the original provenance.
- Keep source Graphic Design System repo available as historical archive.
- Consider a richer lookbook interface later, only if actually useful. Publishing remains manual/explicit.
