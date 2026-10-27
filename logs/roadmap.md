# TA Guides — consolidation roadmap

Updated: 2026-10-27
Status: PLANNED — inventory complete, merger not yet performed

## Goal

Create **TA Guides**, a personal, informal, extensible collection of practical guides, conventions, examples, references, templates, and small tools. This is **not** a company/practice standards manual. Established rules can exist within a guide without making the entire collection prescriptive.

Destination: `teodor-andonov/261027_ta-guides` (public, renamed from the repo-guidance repository; preserves that repository's history).
Source: `teodor-andonov/ta-graphic-design-system` (private).
Do not automatically publish a site, deploy Pages, or manufacture screenshots.

## Verified current source inventory (2026-10-27)

- Destination contains `README.md`, `AGENTS.md`, and `template/` with copyable `AGENTS.md`, `logs/README.md`, `status.md`, `roadmap.md`, `decisions.md`, `knowledge.md`, and `.gitignore`.
- Source contains `README.md`, `DESIGN.md`, `IMAGERY.md`, `ICONOGRAPHY.md`, `APP_ICONS.md`, `BRAND.md`, `SITE_ARCHITECTURE.md`, `DIRECTIONS.md`, `DECISIONS.md`, `TOKENS.json`, several SVG and HTML studies in `directions/`, `presets/ta-app-icon-default.json`, `tools/app-icon-studio.html`, and an `index.html` redirect.
- Source revision inspected: `8401953fa587b4d5ccd5dbedf9279ddec6ad8c64`. Recheck the actual heads before importing because other agents may continue modifying it.

## Proposed v1 file organisation

```text
README.md                   # personal collection landing page / reading routes
AGENTS.md                   # how agents maintain this repo (not copied app instructions)
guides/
  repositories/
    agent-project-memory.md # canonical guide for logs, evidence, naming
  graphic-design/
    README.md                # index to active design guidance
    design.md
    imagery.md
    iconography.md
    app-icons.md
    tokens.json
    identity/                # TA-specific identity; not generic defaults
      brand.md
      site-architecture.md
      directions.md
      decisions.md
templates/
  repository/
    AGENTS.md
    .gitignore
    logs/README.md
    logs/status.md
    logs/roadmap.md
    logs/decisions.md
    logs/knowledge.md
tools/
  app-icon-studio.html
  presets/ta-app-icon-default.json
examples/
  graphic-design/
    directions/             # existing SVG and HTML explorations; retain
logs/
  status.md                 # state of TA Guides itself
  roadmap.md                # this living plan
  decisions.md              # decisions about the collection itself
  sessions/                 # dated development notes when useful
```

Do not create empty speculative domain directories. Add more guides/areas only when real material exists. Preserve useful source documents verbatim at first, then edit and cross-link in a separate verification pass. A guide may contain instructions, examples, references or status labels (core/preferred/trial/open/historical) without asserting universal TA practice rules.

## Consolidation cycle

### Phase A — Safety and mapping

- [x] Identify actual renamed destination and its contents.
- [x] Identify original Graphic Design System repository and its contents.
- [x] Identify visibility mismatch: destination PUBLIC, source PRIVATE.
- [ ] Recheck both branch heads immediately before migration.
- [ ] Check source content and history for anything unsuitable for public exposure; do **not** import the private repository's entire Git history into a public repository by default.
- [ ] Snapshot source and destination commit SHAs in the final migration record.

### Phase B — Single coherent structural merge

- [ ] Move existing repo-guidance content under `guides/repositories/` and `templates/repository/` without losing standalone copy/paste usability.
- [ ] Import the current, reviewed Graphic Design System docs to `guides/graphic-design/`; separate TA-specific identity decisions from reusable design guidance.
- [ ] Carry across SVG/HTML studies, App Icon Studio and its JSON preset to `examples/` and `tools/`.
- [ ] Replace obsolete root `README.md` and `AGENTS.md` with collection-level navigation and concise authoring rules.
- [ ] Replace the old design-only root `index.html` redirect with an appropriate local guide landing page **only if** retaining a web view is useful. Do not deploy it.
- [ ] Record migration source paths / commit SHAs, and explicitly distinguish imported decisions from newly approved ones.

### Phase C — Repair, validate, hand over

- [ ] Fix relative Markdown/HTML links, presets, examples and references after moving files.
- [ ] Check JSON validity and ensure the icon tool still loads its default, preview and exports.
- [ ] Check SVG/HTML study viewer assets and paths in their new location.
- [ ] Confirm project template is self-contained and can be copied into a fresh repo.
- [ ] Search for stale `ta-repo-guidance`, old `ta-graphic-design-system` relative paths and obsolete links; use redirects or source references where appropriate.
- [ ] Update `logs/status.md`, `logs/decisions.md` and a dated session record with actual validation results, unknowns and follow-up.
- [ ] Archive/retain the original private Graphic Design System repo after successful checks rather than deleting its separate history.

## Boundary rules

1. Personal guides, not a formal organisation/practice policy.
2. A guideline is a useful default unless explicitly marked as required by a particular task.
3. Project-specific implementation belongs to its own project; cross-project reusable lessons belong here.
4. One canonical document per topic; references and self-contained templates may intentionally duplicate a stable snapshot.
5. Keep original history and evidence, including historical and superseded approaches, discoverable.
6. Do not claim a migrated integration or screenshot was verified without actual testing.
7. No automatic Pages publishing, screenshots, or changes to consuming app repositories.
