# Decisions — TA Guides

## 2026-10-27 — Informal personal collection

- The chosen name is **TA Guides**, hosted in `teodor-andonov/261027_ta-guides`.
- It is personal and organically expandable, **not** a manual for a company/practice.
- Guides may contain specific rules, but need not be formal standards.
- Use `guides/` for instruction, `templates/` for copyable structures, `tools/` for utilities, `examples/` for specimens and `logs/` for project memory.
- Keep TA identity decisions visibly separate from generic design guidance.
- Preserve the existing design status vocabulary; never silently treat a trial as settled.
- No automatic publication, screenshots or changes to other app repositories.

## Source preservation

- **Repo Guidance**: this destination is the renamed original, so its existing Git commit ancestry is preserved.
- **Graphic Design System**: imported content as of `8401953fa587b4d5ccd5dbedf9279ddec6ad8c64`. The original [repository](https://github.com/teodor-andonov/ta-graphic-design-system) remains, preserving its previous commit history without rewriting public Git history.
- Existing source material, including original lengthy overview, visual boards, HTML studies, tokens, app icon studio and preset, is retained. Historical outcomes remain historical.
- Public visibility of the destination was explicitly accepted by the owner.

## 2026-10-27 — Return to files-only navigation

The owner decided that the short-lived GitHub Pages website introduced in [PR #2](https://github.com/teodor-andonov/261027_ta-guides/pull/2) added unnecessary complexity. **Current decision:** maintain and navigate TA Guides directly as GitHub Markdown and local folders, not as a generated documentation website. Remove the website build, workflow, CSS, HTML homepage and corresponding build-only files. Keep the standalone HTML design experiments and App Icon Studio as useful *tools/examples*, not as part of any website. Preserve historic Git commits rather than rewriting history. Pages itself still needs to be turned off through GitHub repository settings.

## 2026-10-27 — Preserve the pre-merge state as an annotated tag

- Saved the original Repo Guidance at commit `23384fdafa8439f8c93945c6de1e6c247247ad88` as the annotated tag [`pre-merge-2026-10-27`](https://github.com/teodor-andonov/261027_ta-guides/tree/pre-merge-2026-10-27). This predates the TA Guides planning and file-merger commits.
- Deleted only the two verified temporary branches: `refactor/consolidate-guides-261027` and `site/github-pages-261027`.
- Continue active work on `main`; tags are historical snapshots rather than ongoing branches. Original TA Graphic Design System remains separately available in its own repository.
- One-time branch maintenance workflow removed immediately after the successful run; no standing workflow is needed.
