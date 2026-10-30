# TA PWA update template

Local, dependency-free starting point for the [TA PWA standard](../../guides/pwa/ta-pwa-standard.md). Copy into the app; TA Guides is not a runtime dependency.

1. Copy `pwa-update.js` into the deployed app root. Load it once with `<script defer src="./pwa-update.js"></script>`. For a module service worker, add `data-worker-type="module"`.
2. Append `pwa-update-worker.js` to the app's `sw.js`. Keep its normal install, activate and fetch handlers; remove unconditional install-time `skipWaiting()` and call `clients.claim()` after activation cleanup.
3. Define `window.taPwaCanUpdate = () => ...` in the app. Return `true` only when no unsaved edits, incomplete dialogs or active operations would be interrupted. This must use actual product state. Missing or throwing hooks fail closed. Re-evaluate the hook whenever a feature introduces new drafts or async operations.
4. Cache `pwa-update.js` and the complete shell in a new per-app release cache. Read only from the active cache while updates wait. Remove old registration/reload logic so the app has one update owner.
5. Copy `pwa-update.test.mjs` to the app's `tests/` folder and run `node --test tests/pwa-update.test.mjs`. It expects `../sw.js`, `../pwa-update.js` and `../manifest.webmanifest`, and exercises activation consent, refusal, timeout and app scope. Add browser tests for the actual guard, UI and old/new workers.

The client discovers the concise app name and favicon from the main document. The update card lives in a shadow root so app CSS does not distort its controls. It leaves the editor interactive until the user requests an update. A short input shield protects prepared windows during activation; a timeout releases it if activation fails.

The worker asks same-scope windows to prepare using MessageChannels, refuses unknown/legacy clients and never contacts another app. Browsers suspend background pages; an unresponsive page deliberately blocks, and the user can close it. No push notification permission, external update service or account is required.

First migration: existing windows without the new client cannot show its prompt retroactively. Save work, close all app windows and reopen online once. Subsequent releases can use the new prompt.

Keep copies coordinated with a template version comment and regression tests. App-specific guards and hosting paths stay in the consuming repository. This is a small shared protocol, not a general autosave or data-migration framework.

All control IDs use the `ta-pwa-` prefix, even inside the shadow root. Browser automation can pierce shadow roots; generic IDs such as `status` can otherwise collide with the consuming app’s selectors.
