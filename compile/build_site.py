#!/usr/bin/env python3
"""Build the served Civilization Wiki site (the Mission Control view) from wiki/*.md + index.md.

Deterministic: Python stdlib + python-markdown only. No network, no LLM, no push.
The wiki is the substrate; this renders a read-view onto it. Run by compile/refresh.py
(nightly cron) and on demand.
"""
import re
import json
import html
import pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
DIST = ROOT / "dist"
ASSETS = ROOT / "compile" / "assets"
STATUS = ROOT / "compile" / "refresh-status.json"
INDEX = ROOT / "index.md"

SLUGS = {p.stem for p in WIKI.glob("*.md")} | {"index"}

WL = re.compile(r"\[\[([a-z0-9][a-z0-9\-]*)(?:\|([^\]]+))?\]\]")
TOK = re.compile(r"@@WL\|([a-z0-9\-]+)\|([^@]*)@@")


def tokenize(t):
    return WL.sub(lambda m: "@@WL|%s|%s@@" % (m.group(1), m.group(2) or ""), t)


def detok(h):
    def repl(m):
        slug, alias = m.group(1), m.group(2)
        label = html.escape(alias or slug.replace("-", " "))
        if slug in SLUGS:
            return '<a class="wl" href="%s.html">%s</a>' % (slug, label)
        return '<span class="wl tbd" title="not yet compiled (TBD)">%s</span>' % label
    return TOK.sub(repl, h)


def split_fm(raw):
    if raw.startswith("---"):
        e = raw.find("\n---", 3)
        if e != -1:
            return raw[3:e].strip("\n"), raw[e + 4:].lstrip("\n")
    return "", raw


def fm_val(fm, key):
    m = re.search(r"^%s:[ \t]*(.+)$" % re.escape(key), fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


MD = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])


def to_html(body):
    MD.reset()
    return detok(MD.convert(tokenize(body)))


def load_status():
    if STATUS.exists():
        try:
            return json.loads(STATUS.read_text())
        except Exception:
            pass
    return {}


def page(title, body_html, *, is_home=False, tier="", status=None):
    status = status or {}
    stale = status.get("stale_articles", [])
    synced = status.get("synced", "")
    n = status.get("article_count", len([s for s in SLUGS if s != "index"]))
    if synced:
        fresh, fcls = "synced %s · %d stale" % (synced, len(stale)), ("warn" if stale else "ok")
    else:
        fresh, fcls = "not yet refreshed", "warn"
    nav = '<span class="here">arc index</span>' if is_home else '<a href="index.html">‹ arc index</a>'
    sub = "the arc, compiled from the corpus" if is_home else html.escape(title)
    strip = ""
    if is_home:
        scls = "warn" if stale else "ok"
        strip = (
            '<div class="strip">'
            '<div class="tile"><div class="k">articles</div><div class="v">%d</div></div>' % n +
            '<div class="tile"><div class="k">last synced</div><div class="v mono">%s</div></div>' % html.escape(synced or "—") +
            '<div class="tile"><div class="k">stale</div><div class="v %s">%d</div></div>' % (scls, len(stale)) +
            '<div class="tile"><div class="k">substrate</div><div class="v">LLM wiki</div></div>'
            '</div>'
        )
    arthead = "" if is_home else (
        '<div class="arthead"><span class="tier %s">%s</span><h1>%s</h1></div>'
        % (html.escape(tier), html.escape(tier or "article"), html.escape(title))
    )
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s — Civilization Wiki</title>' % html.escape(title) +
        '<link rel="stylesheet" href="style.css"></head><body>'
        '<div class="topbar"><div class="brand"><span class="mark">CIVILIZATION&nbsp;WIKI</span>'
        '<span class="sub">%s</span></div>' % sub +
        '<div class="meta"><span class="pill %s">%s</span>%s</div></div>' % (fcls, html.escape(fresh), nav) +
        '<main class="wrap%s">%s%s' % (" home" if is_home else "", strip, arthead) +
        '<article class="md">%s</article></main>' % body_html +
        '<footer class="wrap">Generated from <code>wiki/</code> + <code>index.md</code> · '
        'Karpathy-style LLM wiki · fail-legible: gaps are TBD, conflicts stated.</footer>'
        '</body></html>'
    )


def build():
    DIST.mkdir(exist_ok=True)
    status = load_status()
    (DIST / "style.css").write_text((ASSETS / "style.css").read_text())
    count = 0
    for p in sorted(WIKI.glob("*.md")):
        fm, body = split_fm(p.read_text())
        title = fm_val(fm, "entity") or p.stem.replace("-", " ")
        tier = fm_val(fm, "tier")
        body = re.sub(r"^#\s+.*\n", "", body, count=1)
        (DIST / ("%s.html" % p.stem)).write_text(page(title, to_html(body), tier=tier, status=status))
        count += 1
    fm, body = split_fm(INDEX.read_text())
    body = re.sub(r"^#\s+.*\n", "", body, count=1)
    (DIST / "index.html").write_text(page("Civilization Wiki", to_html(body), is_home=True, status=status))
    print("built %d articles + index -> %s" % (count, DIST))


if __name__ == "__main__":
    build()
