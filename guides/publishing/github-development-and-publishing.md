# GitHub development and publishing

**Default for actively developed websites and PWAs.** Keep development separate from production, and use GitHub Actions as the sole publisher. Project-specific requirements can be stricter; a files-only repo such as TA Guides does **not** need Pages or a publish workflow.

## Core convention

- **Side branches are for development.** Work on `feature/<scope>`, `fix/<scope>`, or a coherent milestone branch (e.g. `feature/v2-studio`). Agents, scheduled tasks and local coding sessions commit here, **not to `main`**. A long-running milestone may use a single rolling branch; a permanent `dev` branch is optional, not required.
- **`main` is the production/release branch.** Keep it stable. A pull request and **squash merge** turn an approved development cycle into one clear production commit.
- **GitHub Actions does all publishing.** A single Pages workflow has **both** `push` to `main` (automatic release) and `workflow_dispatch` (manual publish/re-publish). The manual run deploys **`main` only**, never a feature branch.
- **No side-branch publishing.** Pull requests may run checks or local previews, but they must not deploy to the production Pages site.
- **A green build is not release approval.** Complete the project-relevant tests, screenshots and visual review; merge only when the owner explicitly approves that release. Agents should not self-merge simply because code compiles.

## Development-to-release cycle

1. Branch from the latest `main`; develop and commit in manageable chunks. Keep decisions and work status in the project's own logs.
2. Run relevant local tests, build and visual checks. Follow the [agent project memory guide](../repositories/agent-project-memory.md) for per-prompt screenshots of visual work. PR checks are optional additional automation; don't make GitHub-hosted testing mandatory for projects that validate locally.
3. Open a PR into `main`. Review the diff and release evidence; resolve issues **on the side branch**.
4. When approved, **squash and merge** the PR. Do not push unfinished work directly to `main`. Retain milestone branches or make a tag when a useful historical snapshot is wanted; deleting merged feature branches is not mandatory.
5. The merge creates a push to `main`, which triggers the GitHub Actions publish job. Verify the successful run **and** the live URL before reporting the release as published.

**Manual release path:** On GitHub, open **Actions → Publish → Run workflow** and select `main`. Use this to re-run or republish the current approved release without needing an empty commit. To roll back, revert the relevant change on `main` (using the normal review process) and let the workflow deploy the resulting commit; do not publish a development branch as a shortcut.

## Minimal GitHub Pages workflow pattern

If a workflow skips releases with unchanged app files, remember that packaging/workflow-only fixes may need a manual publication. Include packaging configuration in the release comparison, or explicitly dispatch the corrected workflow on main. A successful run with a skipped publish job is not a published release.

Verify that every locally linked runtime file and every precached asset is actually included in the staged artifact; a new root-level script must be added to a copy allowlist. Validate the staged output as well as the source checkout.

Use project-specific build and validation steps; publish only the **built public app/site**, not development logs, secrets or source workspaces. For static files this may be a staged `_site/` folder; for built projects it may be `dist/`.

```yaml
name: Publish

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: github-pages
  cancel-in-progress: false

jobs:
  publish:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      # Run project-specific validation and build here.
      # Ensure dist/ contains ONLY the intended public site.
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v4
        with:
          path: dist
      - id: deployment
        uses: actions/deploy-pages@v4
```

The `github.ref` guard means a manual dispatch on a development branch **cannot deploy**; choose `main` when running it manually. The default checkout uses the triggering commit, not whatever code happens to be newest when the runner starts. Configure **Settings → Pages → Build and deployment → Source: GitHub Actions**, not **Deploy from a branch**.

## Safety and ownership

- Configure a `main` branch rule/ruleset to **require a pull request** for changes. Optionally require checks and approvals that are practical for the project. A solo developer should not set an approval rule they cannot satisfy. Avoid bypassing your own release gate with direct pushes.
- Restrict the GitHub Pages deployment environment to `main` where supported. Keep production publishing out of `pull_request`, `schedule` and development-branch push triggers.
- PWA identity, offline storage and installed-client updates belong to the separate [TA PWA guide](../pwa/README.md). Deployment success and browser update adoption are different checks.
- Pin a supported runner OS when the toolchain requires it. A pinned older Playwright harness may not support the next `ubuntu-latest` image; retain the browser check and select a supported runner rather than disabling validation.
- Publishing workflows should request the minimum necessary permissions; never place application credentials or personal source files in the published artifact.
- **Existing exceptions are explicit.** A paused repo need not be migrated; a files-only repo needs no website; a project with a deliberately manual release policy must be consciously changed before enabling `push` publishing.

## Agent handoff rule

Before editing a website/PWA repository, check its current branch and publishing workflow. **Develop on a side branch, do not silently change release policy, do not merge into `main` without authorization, and report separately:** code committed, PR merged, Action succeeded, public site checked. These are four different states.
