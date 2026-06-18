#!/usr/bin/env python3
"""Self-building auto-deploy poller for the Civilization Wiki.

Self-hosting: rebuilds only via the civilization's own refresh.py/build_site.py,
local git state, Python stdlib, air-gap. Fail-closed: deploy is the single
explicitly-proven branch; every unknown/missing/error path refuses. The script
NEVER commits, pushes, non-ff-merges, or forces — only `git fetch` and
`git merge --ff-only`. See docs/superpowers/specs/2026-06-15-wiki-autodeploy-design.md.
"""
import json
import sys
import subprocess
import pathlib
import datetime
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]

ALLOW_EXACT = {
    "index.md", "PROVENANCE.md",
    "compile/build_site.py", "compile/refresh.py",
    "compile/stats.py", "compile/inflight.py",
}
ALLOW_ASSET_PREFIX = "compile/assets/"


def sh(*a):
    return subprocess.run(list(a), capture_output=True, text=True)


def site_affecting(paths):
    """Pure. True if any path is site-affecting (allowlist), with the hits."""
    hits = []
    for p in paths:
        if p in ALLOW_EXACT:
            hits.append(p)
        elif p.startswith(ALLOW_ASSET_PREFIX):
            hits.append(p)
        elif p.startswith("wiki/") and p.endswith(".md"):
            hits.append(p)
    return (len(hits) > 0, hits)
