# Civilization Wiki — substrate design

**Status:** draft v0.1 · **Date:** 2026-06-13 · **Owner:** Michael Saucier · **Authority:** planning (proposal)

## Purpose

A [Karpathy-style LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): the single, self-maintaining, interlinked knowledge **substrate** for the Transpara-AI Civilization arc. Compiled from the full corpus — 8,783 markdown files across 73 repos + 1,175 Open Brain thoughts + the Matt Searles lovyou.ai posts — and kept current as the work progresses.

Everything downstream (the Mission Control board, the spine/story view) becomes a **read view onto this wiki**. The wiki is the source of truth for the narrative; the visualization is a lens, built later.

## Pattern

Karpathy's three-part loop — knowledge **compounds** instead of being re-discovered per query (the anti-RAG bet):

```
raw/   → sources, verbatim, never hand-edited
wiki/  → LLM compiles raw into encyclopedia articles: synthesize, resolve
         conflicts, cross-link [[related]]
index.md → the arc spine + article index
```

## Layout

```
civilization-wiki/
  raw/
    searles/            day-1 provocation: the ~45–50 lovyou.ai posts
    transpara/          first-party: docs, df-impl-v11..v16, dark-factory, design iterations
    open-brain/         the 1,175 thoughts, exported as dated markdown
    investigations/<x>/ forked-upstream context, one dir per investigated project
  wiki/                 LLM-compiled, interlinked entity articles
  index.md              spine + index, with a fail-loud freshness header
  PROVENANCE.md         source manifest: each raw item → origin, date, tier
  compile/              the compiler: prompts, manifest, scripts
  DESIGN.md             this file
```

## Ingestion — "ingest all, sort at compile"

Per Karpathy (and Michael's call): mirror the **whole** corpus into `raw/`, nothing dropped. Curation is a compile-time concern, not a gate at the door.

- **Provenance tiers** (recorded in `PROVENANCE.md` + each file's frontmatter), so the compiler knows what's load-bearing without anything being excluded:
  - `first_party` — Transpara-authored (docs, df-impl-v*, dark-factory, Open Brain)
  - `searles` — the foundational philosophy
  - `upstream_context` — a forked project's own docs (context for its investigation article, **not** the subject of the wiki)
- **Phased to manage token cost** (not to filter): Phase 1 = `searles` + `first_party` + `open_brain` (the arc itself); Phase 2 = `investigations/*`.
- **Open Brain export**: dump all 1,175 thoughts to `raw/open-brain/` as dated markdown.
- **Secret-scrub before any commit** — the corpus includes config-laden repos and the platform has a known hardcoded-credentials finding (F-01). `raw/` runs a secret scanner; nothing with live secrets is committed. Non-negotiable.

## Compilation — wiki/

- **Engine:** Claude Code, multi-agent (subagents / a workflow) to cover the corpus at scale. Each agent owns a source cluster and proposes/updates entity articles.
- **The article set EMERGES from the sources** — it is *not* pre-authored by me (the lesson from getting the narrative wrong by assumption). A first pass derives the entity list from `raw/`, seeded by the grounded fork-chronology + the Searles philosophy; later passes refine.
- **Per article:** frontmatter (`entity`, `status`, `last_compiled`, `sources[]`), body that synthesizes the sources, a "Sources & provenance" footer listing the `raw/` files it was built from, and `[[wikilinks]]` to related entities.
- **Fail-legible / anti-confabulation:** when sources conflict or a fact is unverified, the article **states the disagreement and cites both** rather than silently picking a winner. Thin evidence is labeled thin. (Mirrors the platform's fail-safe-by-default doctrine.)

## Keep-current — cron

- **Nightly:** re-export Open Brain + re-sync first-party repos into `raw/` → **incremental** re-compile of only the entities whose source set changed (a manifest tracks `raw → article` dependencies) → commit.
- **Fail-loud freshness:** `index.md` header shows `last_compiled` + which sources are synced/stale — same honesty signal as Mission Control. Never looks-current-while-stale.

## The Feb genesis (the gap we must fill by hand)

Day one — the Searles reading + the first lovyou.ai fork/build (~Feb 2026) — is **not in the digital record** (org forks start 3/30, personal GitHub has no Feb-2026 forks, Open Brain starts 3/4). It is reconstructed from `raw/searles/` + a short `raw/transpara/genesis.md` captured from Michael's account + the Substack post dates. The wiki's origin article will say so explicitly — reconstructed, not derived from commit history.

## Boundaries

- **Repo:** new `transpara-ai/civilization-wiki`, **private** (internal substrate). Created when we're ready to push, with confirmation first.
- transpara-ai only; never touch `lovyou-ai`/upstream. `upstream_context` quotes public docs as cited context, never re-publishes wholesale.
- Air-gap friendly: compile runs locally on nucbuntu; only dependency is the LLM.

## Open questions (for your review)

1. **Wiki readership, v1:** markdown-in-repo (read on GitHub / in an editor) is enough to start; a served browsable renderer on nucbuntu can come with the visualization phase. Agree, or do you want it served from day one?
2. **Compile engine:** greenlight a multi-agent **workflow** for the Phase-1 compile (real token cost across thousands of sources), or start incremental/manual and scale up?
3. **Secret-scrub:** confirm `raw/` ingestion must pass a secret scan before any commit (strongly recommended).
