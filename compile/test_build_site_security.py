#!/usr/bin/env python3
"""Stdlib-assert tests for security-sensitive build_site helpers."""
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_site as site  # noqa: E402


def test_safe_source_path_rejects_escape_and_accepts_allowlisted_file():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        raw = root / "raw"
        raw.mkdir()
        ok = raw / "ok.md"
        ok.write_text("# ok\n")
        escape = raw / "escape.md"
        escape.symlink_to("/etc/passwd")

        old_root, old_allowed = site.ROOT, site.ALLOWED_SOURCE_ROOTS
        try:
            site.ROOT = root
            site.ALLOWED_SOURCE_ROOTS = [root]
            assert site.safe_source_path("raw/ok.md") == ok.resolve()
            assert site.safe_source_path("raw/escape.md") is None
            assert site.safe_source_path("/etc/passwd") is None
        finally:
            site.ROOT, site.ALLOWED_SOURCE_ROOTS = old_root, old_allowed
    print("ok test_safe_source_path_rejects_escape_and_accepts_allowlisted_file")


def test_markdown_source_rendering_escapes_raw_html():
    rendered = site.render_source_document(
        "raw/inbox/test.md",
        pathlib.Path("test.md"),
        "---\ntitle: Test\n---\n\n# Heading\n\n<script>alert(1)</script>\n",
    )
    assert '<h1 id="heading">Heading</h1>' in rendered
    assert "<script>" not in rendered
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in rendered
    print("ok test_markdown_source_rendering_escapes_raw_html")


def test_markdown_source_rendering_strips_unsafe_uri_schemes():
    rendered = site.render_source_document(
        "raw/inbox/test.md",
        pathlib.Path("test.md"),
        "# Links\n\n[x](javascript:alert(1))\n\n![pixel](data:text/html;base64,AAAA)\n\n[ok](https://example.com)\n",
    )
    assert "javascript:alert" not in rendered
    assert "data:text/html" not in rendered
    assert 'href="#" data-unsafe-uri="removed"' in rendered
    assert 'src="#" data-unsafe-uri="removed"' in rendered
    assert 'href="https://example.com"' in rendered
    print("ok test_markdown_source_rendering_strips_unsafe_uri_schemes")


def test_remote_url_helpers_redact_credentialed_or_noncanonical_remotes():
    credentialed = "https://x-access-token:secret-token@github.com/transpara-ai/wiki.git"
    assert site.github_web_url("git@github.com:transpara-ai/wiki.git") == "https://github.com/transpara-ai/wiki"
    assert site.github_web_url("https://github.com/transpara-ai/wiki.git") == "https://github.com/transpara-ai/wiki"
    assert site.github_web_url(credentialed) == ""
    rendered = site.remote_link(credentialed)
    assert "secret-token" not in rendered
    assert "Remote URL redacted" in rendered
    print("ok test_remote_url_helpers_redact_credentialed_or_noncanonical_remotes")


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
    print("\nall %d build-site security tests passed" % len(fns))
