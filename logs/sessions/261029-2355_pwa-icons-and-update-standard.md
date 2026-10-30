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

## Local-source clarification and checkout setup — 30 October

The owner identified Sourcebook’s existing authoritative local checkout and requested local repos for missing apps. Inventory also identified Graphicpad’s existing local source checkout. Their source models and release policies supersede this session’s earlier clean-public-clone approach. Reconciled the scoped PWA changes into each local main-local source, preserving Sourcebook V0.0.66 media/theme/menu features and Graphicpad’s portable HTML/build path. Runtime-only releases retain the earlier public ancestry; local source branches and logs are not uploaded.

Sourcebook local gate: 480 Node tests, all syntax checks and 21 Chromium scenarios pass. Graphicpad local gate: 98 tests, TypeScript/Vite build and generated PWA checks pass; no local-source browser interaction was requested, so none was performed. Prior cross-app distribution-browser evidence remains separate. The manual-update-check race was separately exercised with a deliberately held update request: the click displays Checking and then the result.

Created full local checkouts for Mindmap, Viewsvg, Codegraph and TA Guides under T/Repos, reusing the existing Sourcebook and Graphicpad checkouts. New clones track existing remotes, disable implicit pushes and retain existing publication policies. Source location and release ownership are now explicit in the guides.

## Final publication verification — 30 October 2026

| App | Final public runtime/source commit | Successful release Action |
| --- | --- | --- |
| TaGraphicpad | e5a7c0fcb803 (local-source runtime snapshot) | 40978410630 |
| TaSourcebook | d0b5ef26e17b (local V0.0.66 runtime snapshot) | 40978052039 |
| TaMindmap | f1c8587478c6 | 40978053205 |
| TaViewsvg | b4e872933916 | 40978055591 |
| TaCodegraph | 7fc0049aa2e2 | 40978058169 |

All five live pages have the exact concise name, separate stable identity, a real main-head manifest, the final matching updater client and working SVG/PNG icon URLs with true 192/512 dimensions. Sourcebook’s live app module matches authoritative local V0.0.66 source, and its installed-client update/then offline reload was exercised in a separate browser profile with zero installability errors. Final Graphicpad source was checked by its automated build/PWA verifier and live HTTP asset checks, without opting into local editor browser use. Earlier four-app distribution installability/offline and two-version browser tests are recorded above.

Local source and runtime snapshots are now in sync for Sourcebook and Graphicpad. The three new application clones are clean on main and track the existing remotes; TA Guides’ new local checkout is synchronized after this documentation merge. No other application repositories were changed.
