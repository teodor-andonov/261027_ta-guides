# TA Guides — current status

Updated 2026-10-27

## Completed

Repo Guidance and Graphic Design System have been consolidated into the personal TA Guides repository on `main` through [PR #1](https://github.com/teodor-andonov/261027_ta-guides/pull/1).
Original Repo Guidance ancestry is retained through the renamed destination, and the private Graphic Design System remains intact as a record of its own Git history.

## Content

- `guides/` — graphic design, identity history and repository memory.
- `templates/` — copyable repository `AGENTS.md`, logging trackers and ignored test-artifact convention.
- `tools/` — app icon utility and approved launcher JSON preset.
- `examples/` — SVG and interactive HTML design studies.
- `logs/` — decisions, roadmap and handover history.
- `index.html` — standalone visual directory, replacing the old study redirect.

## Verified

- Both JSON files parse successfully.
- 92 actual relative Markdown links resolve; one illustrative example screenshot filename isn't a real asset.
- 24 local HTML links resolve.
- The migrated App Icon Studio points to its moved guide, and the copyable project template is present.

## Not tested / out of scope

- No interactive browser regression test of the example boards, Icon Studio controls or asset exports.
- No screenshots captured, no Pages deployment triggered by us, and no consuming app repositories modified.

## Next

Future cycles can refine individual guides, test visual tools in a real browser, and improve the lookbook without further restructuring by default.
