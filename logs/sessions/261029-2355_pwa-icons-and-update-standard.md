# TA PWA icon and update standard — 29 October 2026

## Request and scope

Apply the approved TA icon family to TaGraphicpad, TaSourcebook, TaMindmap, TaViewsvg and TaCodegraph; use matching in-app identity icons; make browser updates visible and safe; separate PWA standards from publishing/repository guidance; publish the five apps. No other application repositories were changed. TA Guides remains files-only.

## Changes

- Graphicpad: canonical Lucide 1.61.0 pen-tool, same grayscale preset as the family, regular/maskable SVG and 192/512 PNG exports, preserved license, repeatable GitHub asset generator.
- The four existing canonical symbols remain library-big/network/scan-eye/workflow. In-app identity marks use the actual matching SVG, replacing old approximations. All five TA_APP_ICON.md files point to the consolidated guide.
- Local pwa-update.js copies plus matching worker message protocol: launch/resume/online/hourly/manual checks, downloaded-update card, Update now / Later, app-aware readiness across all same-scope windows, timed-out/legacy clients fail closed. No install-time unconditional takeover or reload-on-focus. Complete active-shell snapshots and per-app cache reads prevent mixing releases.
- Product guards cover actual editor dirty state, gestures, dialogs, file picker/save/export/autosave operations and Sourcebook write/import/index/backup state. Guards must evolve with product features.
- Dedicated guides/pwa and guides/publishing, linked from README and repository guides; old publishing path retained as a pointer. Visual styling stays in APP_ICONS; technical packaging/runtime requirements now have one PWA home. Added templates/pwa without introducing a hosted dependency.

## Verification

- 504 Node tests pass across the five apps (474 Sourcebook, 30 across the others), including scope/identity/cache isolation and the new update protocol tests.
- Twenty PNG files checked at true 192/512 dimensions; five-glyph family sheet visually reviewed. Regular and maskable variants remain separate.
- Local Chrome persistent test profiles: all five manifests installable, no app-related installability errors, all five render offline with the updater and no page errors, all five current caches survive together.
- Real two-version browser tests: Later keeps the current page/controller; Update now activates and reloads all five; dirty Graphicpad/Mindmap edits refuse; pending Mindmap Save As refuses; Sourcebook dialog refuses; a second dirty Mindmap window blocks and releases the prepared clean window, then both clean windows update successfully.
- Update card checked on desktop and a 390px-wide viewport; no horizontal overflow. These are browser checks, not physical device installation acceptance.
- Sourcebook CI initially caught an updater #status selector colliding through an open shadow root. All IDs were namespaced ta-pwa- in every app and the shared template, with regression coverage. Sourcebook PR CI subsequently passed, including its full pinned Linux Chromium browser smoke.
- A local attempt to run that Linux-oriented smoke with installed Windows Chrome encountered Windows renaming a .url download to .download; its Linux CI result is the applicable unchanged harness acceptance. No unrelated download behavior was modified.
- Live verification caught Sourcebook’s existing root-file staging allowlist omitting the new pwa-update.js. The Pages staging command and a release-artifact regression test were added before final publication. Recreated the staged artifact locally and checked all 63 precache paths exist.
- All new guide links resolve. Two pre-existing example screenshot placeholders remain intentionally absent. All inline app scripts parse. Template copies match each other; service worker/cache versions advance for this release.

## Release evidence

Implementation PRs: Graphicpad #1/#2; Sourcebook #45/#46; Mindmap #2/#3; Viewsvg #1/#2; Codegraph #1/#2. All were squash merged after local validation; Sourcebook after its required CI passed (including the artifact-packaging follow-up). The owner’s explicit publish request authorizes these releases. Sourcebook’s app-diff gate skipped the packaging-only correction, so its corrected workflow was explicitly dispatched on main. A skipped publish job was not counted as publication. Existing manual release workflows were dispatched on main; automatic policies remain intact.

Final live verification is recorded below after publication.

## Upgrade note

This is the first introduction of the update UI: older open windows cannot show code they have not loaded. Save work, close all windows for each app, then reopen online once. Future releases can use Update now / Later. Browser/OS icon caches may still need time or reinstall; never clear shared-origin site data merely to refresh one shortcut. No actual Windows/Android installed-icon refresh is claimed.
