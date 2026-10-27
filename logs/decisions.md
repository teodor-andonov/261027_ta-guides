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

## 2026-10-27 — Rename WIP examples as studies; package tools by original creation timestamp

- Renamed `examples/` to `studies/` because the existing visual directions and HTML boards are still explorations, not polished reusable examples.
- Each reusable tool should have its own folder named `YYMMDD-HHmm_short-name/`, using the tool's **original creation time** (not today's refactoring time).
- Consolidated `app-icon-studio.html` and its approved JSON preset into `tools/261027-1116_app-icon-studio/` (original Icon Studio creation: 27 October 2026 at approximately 11:16 UTC).
- This is a filesystem change only: no new website, no publishing, no change to the pre-merge Git tag, and no changes to the underlying design decisions.

## 2026-10-27 — Flat dated studies

The owner clarified that studies are WIP explorations and should form a **simple flat list** of directly nested `studies/YYMMDD-HHmm_short-title/` folders, not folders organised by discipline. Keep multiple source files together when they form one coherent study.

- `studies/261012-2105_visual-identity-directions/` — SVG direction explorations, application boards and comparison viewer; first original asset 12 Oct 2026 at 21:05 UTC.
- `studies/261013-0849_soft-precision-v2/` — responsive HTML study, originally created 13 Oct 2026 at 08:49 UTC.

The matching App Icon Studio tool folder remains untouched. All prior project decisions and original Git history are preserved.

## 2026-10-27 — GitHub development and publishing convention

For website/PWA repositories, the owner chose side-branch development and approved PR **squash merges** to `main`. GitHub Actions is the only publishing mechanism: publish **automatically on pushes to `main`** and **manually through `workflow_dispatch`**, with production deployment guarded to `main`. Block accidental direct pushes through branch protection/rules where available. Develop and validate off `main`; an agent must not silently merge or publish. This reusable convention is documented in [GitHub development and publishing](../guides/repositories/github-development-and-publishing.md).

This **does not** reinstate a website or publishing workflow for TA Guides itself. Existing application repositories are not altered by documenting the convention; their workflows must be migrated separately when requested.
