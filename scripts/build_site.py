#!/usr/bin/env python3
"""Turn Markdown source into readable static HTML for GitHub Pages."""
from __future__ import annotations

from html import escape
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

import mistune

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
INCLUDE = ("index.html", "README.md", "AGENTS.md", "guides",
           "templates", "tools", "examples", "logs")
markdown = mistune.create_markdown(escape=True, plugins=["table", "strikethrough", "task_lists", "url"])
links = re.compile(r'\b(href|src)=(["\'])([^"\']+)\2')


def rel(to, start):
    return os.path.relpath(to, start).replace(os.sep, "/")


def fix_links(content):
    """Rewrite relative Markdown links to generated HTML documents."""
    def sub(m):
        attr, q, url = m.group(1, 2, 3)
        parsed = urlsplit(url)
        if parsed.scheme or url.startswith(("/", "#", "//")) or not parsed.path.endswith(".md"):
            return m.group(0)
        new = parsed.path[:-3] + ".html"
        if parsed.query:
            new += "?" + parsed.query
        if parsed.fragment:
            new += "#" + parsed.fragment
        return f"{attr}={q}{escape(new, quote=True)}{q}"
    return links.sub(sub, content)


def wrap(content, title, output):
    current = output.parent
    nav = (("Home", "index.html"), ("Graphic design", "guides/graphic-design/README.html"),
           ("Repositories", "guides/repositories/README.html"),
           ("Templates", "templates/repository/index.html"), ("Tools", "tools/index.html"),
           ("Examples", "examples/graphic-design/directions/index.html"))
    menu = "".join(f'<a href="{rel(OUT / path, current)}">{escape(label)}</a>'
                   for label, path in nav)
    home = rel(OUT / "index.html", current)
    css = rel(OUT / "assets/site.css", current)
    source = escape(str(output.relative_to(OUT)))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · TA Guides</title><link rel="stylesheet" href="{css}"></head>
<body><header class="bar"><a class="logo" href="{home}">TA / Guides</a><span>Personal collection</span></header>
<div class="layout"><nav aria-label="Site navigation">{menu}</nav>
<main class="paper"><div class="path">{source}</div>{content}
<footer>TA Guides · Personal, evolving guides and examples</footer></main></div></body></html>"""


def source_files():
    for name in INCLUDE:
        item = ROOT / name
        if item.is_file():
            yield item
        elif item.is_dir():
            for path in item.rglob("*"):
                if path.is_file() and not any(part in ("__pycache__", ".git") for part in path.parts):
                    yield path


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    count = 0
    for source in source_files():
        count += 1
        target = OUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == ".md":
            target = target.with_suffix(".html")
            html_content = fix_links(markdown(source.read_text(encoding="utf-8")))
            target.write_text(wrap(html_content, source.stem, target), encoding="utf-8")
        elif source.suffix in (".html", ".htm"):
            target.write_text(fix_links(source.read_text(encoding="utf-8")), encoding="utf-8")
        else:
            shutil.copy2(source, target)

    folders = {p.parent for p in OUT.rglob("*") if p.is_file()}
    for folder in sorted(folders):
        if folder == OUT or (folder / "index.html").exists():
            continue
        entries = []
        for item in sorted(folder.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            if item.name == "index.html":
                continue
            href = item.name + ("/index.html" if item.is_dir() else "")
            label = item.name + ("/" if item.is_dir() else "")
            entries.append(f'<li><a href="{escape(href, quote=True)}">{escape(label)}</a></li>')
        title = str(folder.relative_to(OUT))
        body = f'<h1>{escape(title)}</h1>'
        if (folder / "README.html").exists():
            body += '<p><a href="README.html">Section overview</a></p>'
        body += '<ul class="file-list">' + "".join(entries) + '</ul>'
        (folder / "index.html").write_text(wrap(body, title, folder / "index.html"), encoding="utf-8")

    (OUT / "assets").mkdir()
    shutil.copy2(ROOT / "site/site.css", OUT / "assets/site.css")
    (OUT / ".nojekyll").touch()

    errors = []
    class Auditor(HTMLParser):
        def __init__(self, source):
            super().__init__()
            self.source = source
        def handle_starttag(self, tag, attrs):
            for key, value in attrs:
                if key not in ("href", "src") or not value:
                    continue
                parsed = urlsplit(value)
                if parsed.scheme or value.startswith(("/", "#", "//")) or not parsed.path:
                    continue
                if "YYMMDD-HHmm" in parsed.path:  # Example placeholder screenshot
                    continue
                dest = (self.source.parent / parsed.path).resolve()
                if not dest.is_relative_to(OUT.resolve()) or not dest.exists():
                    errors.append(f"{self.source.relative_to(OUT)} -> {value}")
    for html_file in OUT.rglob("*.html"):
        Auditor(html_file).feed(html_file.read_text(encoding="utf-8"))
    if errors:
        raise SystemExit("Broken links:\n" + "\n".join(errors))
    print(f"Built {count} source files; all actual local HTML links validated.")


if __name__ == "__main__":
    main()
