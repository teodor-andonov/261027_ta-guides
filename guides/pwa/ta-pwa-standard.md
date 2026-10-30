# TA PWA standard

Adopted for TaGraphicpad, TaSourcebook, TaMindmap, TaViewsvg and TaCodegraph on 29 October 2026. Keep the installed app predictable, distinguishable from its neighbors and safe to update during real work.

## 1. Name and identity

- Use the exact concise `TaAppname` everywhere the product is named: manifest `name`, `short_name`, HTML title, dynamic `document.title`, `application-name` and `apple-mobile-web-app-title`. Do not add descriptions, version numbers or filenames to window titles. Keep document names in the interface.
- Give every application a stable, explicit manifest `id`: the full repository path with leading/trailing slash, such as `/261028_gaphic-pad/`.
- On GitHub project Pages use `start_url: "./"` and `scope: "./"`. Register `./sw.js` with the same app scope. Include a manifest link in the **main document head**, outside bundled JavaScript strings, drawing frames or imported SVG content.
- A manifest ID is an identity, not a request path. Relative IDs resolve against the start URL's **origin**; `id: "./"` therefore identifies the domain root. Never copy it between apps on a shared domain.
- Preserve an established correct identity when changing names, icons or release versions. Changing identity can create a separate installation. Record any intentional identity migration and test existing installations.
- Preserve unrelated manifest capabilities such as `file_handlers`, `share_target`, accepted MIME types and parameter field names. Renaming the app must not rename a nested share field called `name`.

| Exact name | Stable ID | Canonical Lucide symbol |
| --- | --- | --- |
| TaGraphicpad | `/261028_gaphic-pad/` | `pen-tool` |
| TaSourcebook | `/261025-2132_sourcebook/` | `library-big` |
| TaMindmap | `/261019-1740_pwa-mindmap/` | `network` |
| TaViewsvg | `/ta-svg-viewer-261012/` | `scan-eye` |
| TaCodegraph | `/ta-cad-graph-261012/` | `workflow` |

## 2. Icons and assets

The visual source of truth is [APP_ICONS.md](../graphic-design/APP_ICONS.md), not a second PWA-specific design preset.

- Keep one canonical, pinned Lucide SVG in `branding/icon-source.svg`. Derive the launcher, favicon, touch icon and every **in-app product identity mark** from that same geometry. Ordinary action icons can use their own appropriate symbols.
- The current preset is Lucide 1.61.0, stroke 2 on 24×24 coordinates, regular glyph 60%, tile radius 25%, foreground `#333333`, background `#E6E6E6`, centered offsets. Maskable exports use a fully opaque square and a centered 54% glyph.
- Supply separate regular (`purpose: "any"`) and maskable (`purpose: "maskable"`) PNGs at 192×192 and 512×512, plus the self-contained SVG/favicon. Do not label one rounded regular tile as both any and maskable.
- A touch icon may use the regular PNG; add a 180px Apple-specific export when Apple installation is a verified target. Optional 64px favicon/ICO exports can be added for supported consumers.
- Pin source geometry and retain Lucide/Feather license notices. Keep reproducible generation in the app's repository; no runtime icon CDN.
- Verify PNG dimensions, both mask shapes, small icon clarity and agreement between launcher and in-app mark. If filenames change, update every HTML/manifest/cache path together. Exact query-string versions of icon URLs must also work offline.

## 3. Shared-origin isolation

GitHub Pages project paths share an origin. Service worker **scope does not partition Cache Storage, IndexedDB or localStorage**.

- Cache keys must identify the application, ideally including its scope and a release identifier. Enumerate/delete only caches owned by this app. Never delete every key except the current cache.
- Read from the active app's named cache, not global `caches.match()` across all app caches. A waiting worker's new cache must not leak new files into the running older version.
- Restrict fetch interception to the correct origin and repository path; allow explicitly documented external runtime dependencies separately. POST share handlers must match only their own app's action URL.
- Namespace browser data stores and localStorage keys. Shared cross-tab locks are deliberate app-specific decisions; do not clear another app's stores, file handles or share inbox.
- Cleanup is for superseded **app shell caches**, never user documents, recovery drafts or a persistent incoming-share cache.
- Regression-test activation with several foreign shell and inbox cache names present.

## 4. Offline shell and versions

- Cache the entire runnable shell: main HTML, styles, update client, runtime/transitive modules, icons, required workers, manifest and local examples needed at launch.
- Treat a shell as a release snapshot. Install into a new versioned cache and fail installation if a required asset is unavailable. Keep the previous working worker when a download fails.
- Advance the shell version whenever web assets change, including icons or the updater itself. An HTML release must not silently pair with old modules or CSS.
- Serve the active shell consistently while an update waits. Network-first navigation that loads new HTML before approval defeats the update prompt.
- A first-time install activates normally without a fake “update available” message. An update to an existing installation waits for explicit user choice, or activates naturally after all old windows close.
- Test a fresh online load followed by offline restart, including direct `index.html`, query navigation, relevant share handoff and every imported module. Checking the title alone does not establish that the app rendered.

## 5. Visible, safe browser updates

Use [the update templates](../../templates/pwa/README.md) as a starting point, with app-specific state guards.

- Check on app launch, return to a visible window, restored connectivity and hourly while visible. Offer an always-available **Updates → Check for updates** control.
- A fully downloaded waiting release shows a nonmodal **Update available** card naming the app, explaining the reload, and offering **Update now** and **Later**. Announce it accessibly; do not steal focus when it arrives during work. Use readable contrast, keyboard controls and reduced-motion support.
- **Later** closes the card without activating or reloading. Keep a visible update badge so the user can return. Manual checks report current, waiting, offline or failed status accurately.
- Remove unconditional `skipWaiting()` from the worker's install handler. Also remove reload-on-focus and unconditional reload-on-`controllerchange` logic.
- **Update now** requests readiness from **every open window belonging to this app**. Each checks its own unsaved work, dialogs, pending file writes, imports, saves and long-running operations through a synchronous guard. A missing/throwing guard or an old/unresponsive window blocks activation.
- Prepare ready windows against new user input during activation; cancel/release them if another window refuses. The user should save/finish work or close the other windows, then retry. Do not offer “discard anyway” as the default path.
- Only after all same-app windows agree, send `skipWaiting()`, claim clients on activation and reload the prepared windows once. Unprepared windows must never silently reload. Guard results are not proof of durable saves: integrate actual app state and verify the save path separately.
- Test user choice, active writing, dirty state, multiple windows, unresponsive legacy windows, failed downloads and offline checks. Do not repeatedly prompt on initial installation or loop on reload.
- Browser updates do not guarantee immediate OS launcher icon/name refresh. Test Windows/Android separately when claiming device acceptance. Avoid clearing origin-wide site data to refresh one shortcut.

## 6. Publishing is separate

[Publishing guidance](../publishing/README.md) owns branch/review/release policy and GitHub Actions. This guide owns the behavior of an installed browser client.

Each app should keep a short `PWA.md` describing its IDs, asset locations, updater hooks and verification results. Its README/release instructions identify the actual workflow and staging folder. Do not duplicate shared standards in every repository, replace product architecture docs with deployment instructions, or silently enable automatic releases for a manually published app.

For this rollout the owner explicitly authorized implementation and publication. For future work, obtain the release authorization required by the consuming project.

## 7. Acceptance record

Before saying “published,” record the commit, successful release Action and live URL. Check:

1. Five distinct app IDs, correct main-document manifest links, exact concise names and valid scopes/start URLs.
2. Local PNG/SVG URLs, real 192/512 dimensions, separate maskable artwork, matching in-app symbol and license notices.
3. All required offline assets including transitive imports; offline UI actually renders.
4. Old release → waiting update → Later leaves the old controller/session intact → Update now activates once and renders the new release.
5. Dirty work and active operations block; ready windows reload together; another app's controller and caches are untouched.
6. Existing file/share handlers still work. Browser installability diagnostics contain no app-related errors.
7. Device tests and limitations are stated honestly. An automated browser check is not an actual Windows/Android install.

## Why these rules exist

The 29 October audit found a manifest link embedded inside Graphicpad's drawing iframe, a root-relative identity collision risk, Codegraph deleting foreign caches, a missing Sourcebook offline module, inconsistent interface marks and unclear updates. Separate identity/visual/runtime/publishing contracts prevent those problems from being reintroduced.

Primary references: [manifest identity](https://developer.chrome.com/docs/capabilities/pwa-manifest-id), [manifest icons](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/icons), [service worker lifecycle](https://web.dev/articles/service-worker-lifecycle), [update prompts](https://developer.chrome.com/docs/workbox/handling-service-worker-updates), [registration updates](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/update).
