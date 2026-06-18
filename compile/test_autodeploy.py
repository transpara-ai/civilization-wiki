#!/usr/bin/env python3
"""Stdlib-assert tests for compile/autodeploy.py. Run: python3 compile/test_autodeploy.py"""
import sys
import json
import pathlib
import tempfile
import datetime
import subprocess

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import autodeploy as ad  # noqa: E402

UTC = datetime.timezone.utc


def test_site_affecting():
    yes, hits = ad.site_affecting(["wiki/x.md", "docs/y.md"])
    assert yes and hits == ["wiki/x.md"]
    assert ad.site_affecting(["index.md"])[0] is True
    assert ad.site_affecting(["compile/assets/style.css"])[0] is True
    assert ad.site_affecting(["compile/inflight.py"])[0] is True
    # excluded-only -> skip
    assert ad.site_affecting(["docs/a.md", ".github/ci.yml",
                              "compile/test_stats.py",
                              "compile/deploy-authorization.json"])[0] is False
    # wiki/ non-markdown does not count
    assert ad.site_affecting(["wiki/img.png"])[0] is False
    # mixed -> affecting
    assert ad.site_affecting(["docs/a.md", "wiki/b.md"])[0] is True
    print("ok test_site_affecting")


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
    print("\nall %d tests passed" % len(fns))
