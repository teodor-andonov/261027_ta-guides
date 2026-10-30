# TA Guides

**A personal, evolving collection of practical guides, conventions, visual references, examples and small tools.**

TA Guides helps me remember and reuse useful approaches to design, development and other recurring topics. It is informal and personal—not a practice/company standards manual. Browse the Markdown directly on GitHub or in a local folder. Areas are added when real material exists.

## Guides

- [Graphic design](guides/graphic-design/README.md) — design grammar, images, icons, tokens, brand/identity thinking, historic decisions.
- [Repositories](guides/repositories/README.md) — agent project memory, logs, documentation, handovers, [GitHub development and publishing](guides/publishing/github-development-and-publishing.md).
- [PWAs](guides/pwa/README.md) — TA app identity, shared icons, isolated offline storage and safe update prompts.
- [Publishing](guides/publishing/README.md) — development/review/release policy and GitHub Actions, separate from runtime PWA behavior.

## Reusable material

- [PWA update template](templates/pwa/README.md) — local update UI, worker protocol and regression tests.
- [Repository template](templates/repository/) — copyable agent instructions, logs and tracker files.
- [App Icon Studio](tools/261027-1116_app-icon-studio/app-icon-studio.html) — interactive Lucide icon styling and exports.
- [TA app icon preset](tools/261027-1116_app-icon-studio/ta-app-icon-default.json) — approved current launcher default.
- [Soft Precision v2](studies/261013-0849_soft-precision-v2/soft-precision-v2.html) — work-in-progress design study.
- [Comparison of visual directions](studies/261012-2105_visual-identity-directions/compare.html) — earlier work-in-progress SVG studies.

## Organisation

| Location | Intended content |
| --- | --- |
| `guides/` | Practical advice, decisions and explanations |
| `templates/` | Self-contained files and structures to reuse |
| `tools/` | Functional utilities and presets |
| `studies/` | Flat list of timestamped work-in-progress study folders |
| `logs/` | Development roadmap, handovers and decisions about this repository |

Status labels from the design materials (**Core / Preferred / Trial / Open / Historical**) remain scoped to those documents. A reusable guide is not automatically a mandatory standard; project-specific decisions live in the project repo.

## History

Created 27 October 2026 by consolidating the renamed **TA Repo Guidance** repository (this repository, preserving its Git commits) and the original [TA Graphic Design System](https://github.com/teodor-andonov/ta-graphic-design-system), imported from commit `8401953fa587b4d5ccd5dbedf9279ddec6ad8c64`. The source repository retains its own separate full Git history. To browse **Repo Guidance exactly as it stood before the merger**, use the [pre-merge-2026-10-27 snapshot](https://github.com/teodor-andonov/261027_ta-guides/tree/pre-merge-2026-10-27) (original commit `23384fd`). Details: [decisions](logs/decisions.md) and [roadmap](logs/roadmap.md).

This repo does not impose runtime dependencies on other apps. For agents maintaining **this** repository read [AGENTS.md](AGENTS.md); for the copyable agent instructions for **other** projects use [templates/repository/AGENTS.md](templates/repository/AGENTS.md).
