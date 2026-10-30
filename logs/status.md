# TA Guides — current status

Updated 2026-10-29

## Current

Personal guide collection, navigated directly through GitHub or the local filesystem. No generated website, dedicated homepage, site build or publication workflow.

The Repo Guidance and Graphic Design System consolidation remains complete ([PR #1](https://github.com/teodor-andonov/261027_ta-guides/pull/1)); its content is unchanged by the website rollback.

## Structure

- `guides/` — graphic design, TA identity history and repository conventions.
- `templates/` — copyable agent instructions, logs and tracker files.
- `tools/` — timestamped tool folders, currently `261027-1116_app-icon-studio/` with the Icon Studio and its JSON preset.
- `studies/` — WIP SVG/HTML explorations and comparison boards; **not** a website.
- `logs/` — roadmap, decisions, handover history.

## Website rollback

The experimental GitHub Pages website introduced by [PR #2](https://github.com/teodor-andonov/261027_ta-guides/pull/2) was intentionally removed at the owner's request. Website-only files, generated site tooling, deployment workflow and root HTML homepage were removed. Historical commits remain available through Git.

**GitHub Pages repository setting:** disabling Pages under Settings → Pages remains an owner-side administrative action; deleting the workflow does not guarantee that GitHub will unpublish an already deployed site.

## Previous checks

Design tokens/preset JSON and original local asset links passed structural checks during consolidation. Interactive browser tooling and export behaviour were not retested during this cleanup.

## Next

Keep the collection file-first. Add or edit guides only as needed; do not reinstate a website without a new explicit decision.

## History housekeeping — 2026-10-27

- Only active branch: `main` (both temporary merger/site branches deleted).
- Pre-merge snapshot: [`pre-merge-2026-10-27`](https://github.com/teodor-andonov/261027_ta-guides/tree/pre-merge-2026-10-27) pointing to original commit `23384fdafa8439f8c93945c6de1e6c247247ad88`.
- The one-time GitHub Actions cleanup workflow was removed after tagging and branch deletion.

## Folder organisation update — 2026-10-27

The WIP design boards live in `studies/261012-2105_visual-identity-directions/`. App Icon Studio and its companion preset live together in `tools/261027-1116_app-icon-studio/`. All cross-references were updated. See `logs/decisions.md` for rationale.

## Flat studies — 2026-10-27

The studies now live in two direct, dated folders: `studies/261012-2105_visual-identity-directions/` and `studies/261013-0849_soft-precision-v2/`. The date/time prefixes use each study's initial Git-recorded creation time (UTC). No thematic nesting is used.

## 2026-10-27 — New repository workflow guide

Added [GitHub development and publishing](../guides/repositories/github-development-and-publishing.md) as a reusable convention for website/PWA repositories: side-branch development → reviewed squash merge to `main` → GitHub Actions publishes, with optional manual dispatch. TA Guides remains files-only and has no publication workflow. Existing application workflows are unchanged by this guide.

## 29 October 2026 — TA PWA standards and update templates

Separated [PWA runtime guidance](../guides/pwa/README.md) from [publishing](../guides/publishing/README.md) and [visual icon identity](../guides/graphic-design/APP_ICONS.md). The old repository publishing URL remains a pointer. Added local copyable update client/worker templates and activation-consent regression tests.

The owner authorized changes and publication for TaGraphicpad, TaSourcebook, TaMindmap, TaViewsvg and TaCodegraph only. Their app-specific integration lives in each repo's PWA.md and TA_APP_ICON.md. See the dated [session](sessions/261029-2355_pwa-icons-and-update-standard.md) for validation and release evidence. TA Guides remains files-only; no website was introduced.
