#!/usr/bin/env python3
"""Stdlib-assert tests for compile/ingest_server.py."""
import io
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import ingest_server as srv  # noqa: E402


class DummyHandler:
    def __init__(self, content_type, body):
        self.headers = {
            "Content-Type": content_type,
            "Content-Length": str(len(body)),
        }
        self.rfile = io.BytesIO(body)


def test_parse_post_form_accepts_browser_multipart_uploads():
    boundary = "----codex-form-boundary"
    body = (
        "--%s\r\n"
        'Content-Disposition: form-data; name="target_slug"\r\n\r\n'
        "sakana-ai-evaluation\r\n"
        "--%s\r\n"
        'Content-Disposition: form-data; name="note"\r\n\r\n'
        "citation upgrade\r\n"
        "--%s\r\n"
        'Content-Disposition: form-data; name="documents"; filename="TAI-RES-2026-001.md"\r\n'
        "Content-Type: text/markdown\r\n\r\n"
        "# Sakana update\n\nBody.\r\n"
        "--%s--\r\n"
    ) % (boundary, boundary, boundary, boundary)
    form = srv.parse_post_form(DummyHandler(
        "multipart/form-data; boundary=%s" % boundary,
        body.encode("utf-8"),
    ))
    assert srv.first_value(form, "target_slug") == "sakana-ai-evaluation"
    assert srv.first_value(form, "note") == "citation upgrade"
    docs = srv.field_values(form, "documents")
    assert len(docs) == 1
    assert docs[0].filename == "TAI-RES-2026-001.md"
    assert docs[0].file.read() == b"# Sakana update\n\nBody."
    print("ok test_parse_post_form_accepts_browser_multipart_uploads")


def test_authoring_policy_requires_token_for_remote_clients():
    assert srv.authoring_allowed("127.0.0.1", "", "") is True
    assert srv.authoring_allowed("::1", "", "") is True
    assert srv.authoring_allowed("192.168.20.22", "", "") is False
    assert srv.authoring_allowed("192.168.20.22", "wrong", "secret") is False
    assert srv.authoring_allowed("192.168.20.22", "secret", "secret") is True
    print("ok test_authoring_policy_requires_token_for_remote_clients")


def test_host_header_policy_blocks_rebinding_hosts():
    old_allowed = os.environ.pop(srv.ALLOWED_HOSTS_ENV, None)
    try:
        assert srv.host_header_allowed("127.0.0.1:8787", 8787) is True
        assert srv.host_header_allowed("localhost:8787", 8787) is True
        assert srv.host_header_allowed("[::1]:8787", 8787) is True
        assert srv.host_header_allowed("evil.test:8787", 8787) is False
        assert srv.host_header_allowed("127.0.0.1:notaport", 8787) is False
        os.environ[srv.ALLOWED_HOSTS_ENV] = "wiki.internal:8787"
        assert srv.host_header_allowed("wiki.internal:8787", 8787) is True
        assert srv.host_header_allowed("wiki.internal:9999", 8787) is False
    finally:
        if old_allowed is None:
            os.environ.pop(srv.ALLOWED_HOSTS_ENV, None)
        else:
            os.environ[srv.ALLOWED_HOSTS_ENV] = old_allowed
    print("ok test_host_header_policy_blocks_rebinding_hosts")


def test_same_origin_authoring_policy_blocks_browser_csrf():
    assert srv.same_origin_authoring_request({
        "Host": "127.0.0.1:8787",
        "Origin": "http://127.0.0.1:8787",
        "Sec-Fetch-Site": "same-origin",
    }, 8787) is True
    assert srv.same_origin_authoring_request({
        "Host": "127.0.0.1:8787",
        "Origin": "http://evil.test",
        "Sec-Fetch-Site": "cross-site",
    }, 8787) is False
    assert srv.same_origin_authoring_request({
        "Host": "127.0.0.1:8787",
        "Sec-Fetch-Site": "cross-site",
    }, 8787) is False
    assert srv.same_origin_authoring_request({
        "Host": "127.0.0.1:8787",
        "Origin": "http://127.0.0.1:notaport",
    }, 8787) is False
    assert srv.same_origin_authoring_request({
        "Host": "127.0.0.1:8787",
    }, 8787) is True
    print("ok test_same_origin_authoring_policy_blocks_browser_csrf")


def test_article_records_hide_sources_when_not_authorized():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        wiki.mkdir()
        (wiki / "example.md").write_text(
            "---\n"
            "entity: Example\n"
            "tier: investigation\n"
            "sources:\n"
            "  - /Transpara/transpara-ai/repos/docs/private.md\n"
            "---\n\n"
            "# Example\n"
        )
        old_wiki = srv.WIKI
        try:
            srv.WIKI = wiki
            hidden = srv.article_records(include_sources=False)
            visible = srv.article_records(include_sources=True)
            assert hidden[0]["sources"] == []
            assert visible[0]["sources"] == ["/Transpara/transpara-ai/repos/docs/private.md"]
        finally:
            srv.WIKI = old_wiki
    print("ok test_article_records_hide_sources_when_not_authorized")


def test_save_uploads_rejects_target_slug_traversal_before_write():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        old_root, old_raw, old_manifest = srv.ROOT, srv.RAW_INBOX, srv.MANIFEST
        try:
            srv.ROOT = root
            srv.RAW_INBOX = root / "raw" / "inbox"
            srv.MANIFEST = srv.RAW_INBOX / "manifest.jsonl"
            form = {
                "documents": srv.FormField(
                    "documents",
                    filename="escape.md",
                    data=b"# should not be written\n",
                )
            }
            try:
                srv.save_uploads(form, "../escape", "", "")
            except ValueError:
                assert not list(root.rglob("escape*"))
                print("ok test_save_uploads_rejects_target_slug_traversal_before_write")
                return
            raise AssertionError("traversal slug should be rejected")
        finally:
            srv.ROOT, srv.RAW_INBOX, srv.MANIFEST = old_root, old_raw, old_manifest


def test_append_sources_quotes_urls_and_preserves_fragments():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        wiki.mkdir()
        article = wiki / "sakana-ai-evaluation.md"
        article.write_text(
            "---\n"
            "entity: Sakana AI Capability Evaluation\n"
            "tier: investigation\n"
            "sources:\n"
            "  - raw/existing.md\n"
            "confidence:\n"
            "  sources: test\n"
            "---\n\n"
            "# Body\n"
        )
        old_wiki = srv.WIKI
        try:
            srv.WIKI = wiki
            added = srv.append_sources_to_article(
                "sakana-ai-evaluation",
                ["raw/inbox/2026-06-24/sakana/update.md", "https://example.com/paper#section-2"],
                note="better citation",
                supersedes="raw/existing.md",
            )
            assert "https://example.com/paper#section-2" in added
            fm, _, _ = srv.split_fm(article.read_text())
            sources = srv.fm_list(fm, "sources")
            assert "raw/existing.md" in sources
            assert "raw/inbox/2026-06-24/sakana/update.md" in sources
            assert "https://example.com/paper#section-2" in sources
            assert article.read_text().count("confidence:") == 1
        finally:
            srv.WIKI = old_wiki
    print("ok test_append_sources_quotes_urls_and_preserves_fragments")


def test_append_sources_collapses_supersedes_before_frontmatter_comment():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        wiki.mkdir()
        article = wiki / "example.md"
        article.write_text(
            "---\n"
            "entity: Example\n"
            "tier: investigation\n"
            "sources:\n"
            "  - raw/existing.md\n"
            "---\n\n"
            "# Body\n"
        )
        old_wiki = srv.WIKI
        try:
            srv.WIKI = wiki
            srv.append_sources_to_article(
                "example",
                ["raw/new.md"],
                note="note\nwith break",
                supersedes="raw/existing.md\ninjected_key: bad",
            )
            text = article.read_text()
            assert "note: note with break" in text
            assert "supersedes: raw/existing.md injected_key: bad" in text
            assert "\ninjected_key: bad" not in text
        finally:
            srv.WIKI = old_wiki
    print("ok test_append_sources_collapses_supersedes_before_frontmatter_comment")


def test_append_raw_documents_updates_article_nav_inputs():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        wiki.mkdir()
        article = wiki / "sakana-ai-evaluation.md"
        article.write_text(
            "---\n"
            "entity: Sakana AI Capability Evaluation\n"
            "tier: investigation\n"
            "sources:\n"
            "  - raw/existing.md\n"
            "---\n\n"
            "# Body\n"
        )
        old_wiki = srv.WIKI
        try:
            srv.WIKI = wiki
            added = srv.append_raw_documents_to_article(
                "sakana-ai-evaluation",
                ["raw/inbox/2026-06-24/sakana/update.md", "https://example.com/paper"],
            )
            assert added == ["raw/inbox/2026-06-24/sakana/update.md"]
            fm, _, _ = srv.split_fm(article.read_text())
            assert srv.fm_list(fm, "raw_documents") == ["raw/inbox/2026-06-24/sakana/update.md"]
            assert "https://example.com/paper" not in article.read_text()
        finally:
            srv.WIKI = old_wiki
    print("ok test_append_raw_documents_updates_article_nav_inputs")


def test_create_article_from_source_for_unassigned_ingest():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        raw = root / "raw" / "inbox" / "2026-06-24" / "unassigned"
        wiki.mkdir(parents=True)
        raw.mkdir(parents=True)
        source = raw / "TAI-RES-2026-003-v1.0.0-Google-Open-Knowledge-Format-Evaluation.md"
        source.write_text(
            "---\n"
            "document_id: TAI-RES-2026-003\n"
            "title: Google Open Knowledge Format (OKF) Capability Evaluation\n"
            "version: 1.0.0\n"
            "---\n\n"
            "## Abstract\n\n"
            "OKF standardizes the envelope; the Civilization governs the contents.\n"
        )
        old_root, old_wiki = srv.ROOT, srv.WIKI
        try:
            srv.ROOT = root
            srv.WIKI = wiki
            rel = str(source.relative_to(root))
            slug, created = srv.create_article_from_source(rel, note="new research")
            assert created is True
            assert slug == "google-open-knowledge-format-capability-evaluation"
            article = wiki / ("%s.md" % slug)
            assert article.exists()
            fm, _, _ = srv.split_fm(article.read_text())
            assert srv.fm_list(fm, "raw_documents") == [rel]
            assert srv.fm_list(fm, "sources") == [rel]
        finally:
            srv.ROOT = old_root
            srv.WIKI = old_wiki
    print("ok test_create_article_from_source_for_unassigned_ingest")


def test_create_article_from_source_escapes_untrusted_title_markdown():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        wiki = root / "wiki"
        raw = root / "raw" / "inbox" / "2026-06-24" / "unassigned"
        wiki.mkdir(parents=True)
        raw.mkdir(parents=True)
        source = raw / "malicious-title.md"
        source.write_text(
            "---\n"
            "title: \"<script>alert(1)</script> [x](javascript:alert(1))\"\n"
            "---\n\n"
            "Body.\n"
        )
        old_root, old_wiki = srv.ROOT, srv.WIKI
        try:
            srv.ROOT = root
            srv.WIKI = wiki
            rel = str(source.relative_to(root))
            slug, created = srv.create_article_from_source(rel)
            assert created is True
            article = wiki / ("%s.md" % slug)
            _, body, _ = srv.split_fm(article.read_text())
            assert "<script" not in body.lower()
            assert "](javascript:" not in body.lower()
        finally:
            srv.ROOT = old_root
            srv.WIKI = old_wiki
    print("ok test_create_article_from_source_escapes_untrusted_title_markdown")


def test_external_url_validation_rejects_unsafe_scheme():
    try:
        srv.valid_external_urls("javascript:alert(1)")
    except ValueError:
        print("ok test_external_url_validation_rejects_unsafe_scheme")
        return
    raise AssertionError("javascript: URL must be rejected")


def test_source_href_matches_build_site_source_viewer_ids():
    source = "raw/inbox/2026-06-24/sakana/update.md"
    assert srv.source_href(source) == "source/29d1acbe353cb797.html"
    assert srv.source_href("https://example.com/paper#section-2") == "https://example.com/paper#section-2"
    print("ok test_source_href_matches_build_site_source_viewer_ids")


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    for fn in fns:
        fn()
    print("\nall %d ingest-server tests passed" % len(fns))
