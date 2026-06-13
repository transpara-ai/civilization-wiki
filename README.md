# Civilization Wiki

A [Karpathy-style LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — a self-maintaining, interlinked knowledge **substrate** for the Transpara-AI Civilization arc, compiled from the source corpus (Matt Searles' lovyou.ai posts + the first-party dark-factory docs + Open Brain).

**Start here: [`index.md`](index.md)** — the arc spine from day one (2026-02-28) to the present, with the future marked TBD.

## Layout

- `index.md` — the arc spine + article index (read this first)
- `wiki/` — interlinked entity articles (foundational philosophy · architecture · dark-factory arc · investigations)
- `raw/` — source material: `searles/` (the posts), `open-brain/` (exported thoughts). First-party dark-factory docs are read in place and recorded in `PROVENANCE.md`.
- `DESIGN.md` — substrate design, compile pipeline, keep-current plan
- `PROVENANCE.md` — source manifest

## Principles

- **Ingest broadly, synthesize at compile** — curation happens in `wiki/`, not at the door.
- **Fail-legible** — articles state source conflicts and mark asserted-vs-proven claims; gaps are `TBD`, never invented.
- **Compounding** — pre-compiled, cross-linked entity pages re-derived from sources (not RAG-per-query).

## Status

Run 1 + Run 2 core: **61 articles**, links canonicalized, secret-scan clean. ~58 long-tail entities deferred to later runs. Downstream visualization (a Mission Control board, the spine/story view) renders onto this wiki; it is not the wiki.
