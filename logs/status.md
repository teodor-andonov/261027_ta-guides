# TA Guides — current status

Updated 2026-10-27

## Current

Personal guide collection, navigated directly through GitHub or the local filesystem. No generated website, dedicated homepage, site build or publication workflow.

The Repo Guidance and Graphic Design System consolidation remains complete ([PR #1](https://github.com/teodor-andonov/261027_ta-guides/pull/1)); its content is unchanged by the website rollback.

## Structure

- `guides/` — graphic design, TA identity history and repository conventions.
- `templates/` — copyable agent instructions, logs and tracker files.
- `tools/` — standalone App Icon Studio and JSON presets.
- `examples/` — standalone SVG/HTML design references; **not** a website.
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
