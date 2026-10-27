# TA Guides static website

Source documents are Markdown under `guides/`, `templates/`, and `logs/`. The existing root `index.html` is the visual landing page.

The script `scripts/build_site.py` renders the Markdown into readable HTML, rewrites local Markdown links to HTML, preserves existing HTML and SVG examples/tools, creates indexes for folders, and validates relative links. It builds to `_site/`, which is ignored by Git.

To preview locally:

    python -m pip install 'mistune>=3.0,<4.0'
    python scripts/build_site.py
    python -m http.server 8000 --directory _site

Then visit http://localhost:8000.

GitHub Actions workflow `.github/workflows/pages.yml` builds/deploys on pushes to `main` and can be run manually. GitHub Pages must first be enabled in **Settings → Pages → Source → GitHub Actions**. Our connected GitHub tooling cannot make that administration setting. After changing the setting, go to Actions → Publish TA Guides → Run workflow if needed.

Expected URL after successful deployment: https://teodor-andonov.github.io/261027_ta-guides/

Publishing changes nothing in other application repos. Existing App Icon Studio external Lucide CDN dependency remains unchanged.
