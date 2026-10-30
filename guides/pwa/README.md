# TA PWA guide

Runtime standards for independently installed TA apps: identity, icons, offline storage and clear, safe updates. These apply to the five apps updated on 29 October 2026; they are useful defaults for future TA PWAs.

- [TA PWA standard](ta-pwa-standard.md) — implementation requirements and release acceptance checks.
- [Reusable update client and worker](../../templates/pwa/README.md) — local, dependency-free templates and tests.
- [App icon visual standard](../graphic-design/APP_ICONS.md) — approved glyph assignments, colors, scale and provenance.
- [Publishing](../publishing/README.md) — GitHub branches, review, merging and deployment. Publishing is a separate concern from browser updates.

Project-specific data models, product architecture and release policies stay in each application's repository. TA Guides supplies reusable guidance and copyable assets; apps must not require it at runtime.

## Local source locations

Before editing or cloning, check existing saved projects and Git remotes. Under `~/T/Repos/`:

| App / guide | Authoritative local folder | Publication model |
| --- | --- | --- |
| TaGraphicpad | `20261002-2342_graphic-pad_05` | Local source on main-local; tested runtime-only child snapshots to public main; portable HTML stays local |
| TaSourcebook | `261025-2132_sourcebook` | Local source on main-local; complete local check gate; runtime-only snapshots to public main |
| TaMindmap | `261019-1740_pwa-mindmap` | Full static-app checkout; existing manual Pages release |
| TaViewsvg | `ta-svg-viewer-261012` | Full static-app checkout; existing manual Pages release |
| TaCodegraph | `ta-cad-graph-261012` | Full static-app checkout; existing manual Pages release |
| TA Guides | `261027_ta-guides` | File-only documentation, no site deployment |

Graphicpad and Sourcebook already had local source repos. The other four folders were cloned in this rollout. New clones track their existing GitHub repository and disable implicit pushes. Do not clone a public runtime distribution and treat it as authoritative source when a richer local checkout exists. Read that checkout’s AGENTS.md and release instructions first. Local-only source policies override the generic source-PR publishing example.
