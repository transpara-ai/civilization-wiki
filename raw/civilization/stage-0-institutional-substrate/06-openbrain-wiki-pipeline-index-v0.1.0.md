---
doc_id: CIV-V4.1-EPIC-015-OPENBRAIN-WIKI-PIPELINE-INDEX
title: Civilization v4.1 Event 15 OpenBrain and Wiki Pipeline Index
doc_type: corpus-index
status: proposal
version: 0.1.0
created: 2026-06-24
updated: 2026-06-24
owner: Michael Saucier
steward: assistant
project: civilization
supersedes: []
related_docs:
  - CIV-V4.1-EPIC-015-STAGE-0-COMPLETION-SPEC
canonical: false
transpara:
  event: 15
  gate: Y
  stage: 0
  corpus_domain: openbrain-wiki-pipeline
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-OPENBRAIN-WIKI-PIPELINE-INDEX type=corpus-index version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 openbrain wiki knowledge-pipeline no-runtime no-production -->

# Civilization v4.1 Event 15 OpenBrain and Wiki Pipeline Index

## Purpose

This index separates raw memory capture from curated knowledge presentation.

OpenBrain is canonical raw memory capture. The wiki is curated Civilization
knowledge presentation.

## Copied OpenBrain/Wiki Material

| Source | Stage 0 path | Role |
| --- | --- | --- |
| `OB1/README.md` | `corpus/copied/OB1/README.md` | OpenBrain project anchor. |
| `OB1/docs/safe-agent-memory-provenance.md` | `corpus/copied/OB1/safe-agent-memory-provenance.md` | Memory provenance and safety anchor. |
| `wiki/README.md` | `corpus/copied/wiki/README.md` | Wiki project anchor. |
| `wiki/PROVENANCE.md` | `corpus/copied/wiki/PROVENANCE.md` | Wiki source provenance contract. |
| `wiki/DESIGN.md` | `corpus/copied/wiki/DESIGN.md` | Wiki design and genesis framing. |
| `wiki/wiki/the-civilization.md` | `corpus/copied/wiki/wiki/the-civilization.md` | Representative curated Civilization page. |
| `wiki/wiki/dark-factory.md` | `corpus/copied/wiki/wiki/dark-factory.md` | Representative curated lineage page. |
| `wiki/wiki/v3-9.md` | `corpus/copied/wiki/wiki/v3-9.md` | Representative curated v3.9 page. |
| `wiki/wiki/v4-0.md` | `corpus/copied/wiki/wiki/v4-0.md` | Representative curated v4.0 page. |

## Indexed Raw Memory

| Source | Action | Reason |
| --- | --- | --- |
| `wiki/raw/open-brain/2026-03.md` | indexed | Large raw memory export; should remain governed by OpenBrain/wiki curation path. |
| `wiki/raw/open-brain/2026-04.md` | indexed | Large raw memory export; should remain governed by OpenBrain/wiki curation path. |
| `wiki/raw/open-brain/2026-05.md` | indexed | Raw memory export; not copied in Stage 0. |
| `wiki/raw/open-brain/2026-06.md` | indexed | Large raw memory export; should remain governed by OpenBrain/wiki curation path. |

## Target Pipeline

```text
OpenBrain / Codex sessions / GitHub / reviews / imports
  -> raw capture
  -> normalized records
  -> curated Civilization knowledge
  -> wiki-input package
  -> wiki repo render
```

## Stage 0 Non-Action

Stage 0 does not activate a new ingestion pipeline, write OpenBrain thoughts,
rewrite wiki raw exports, or alter the wiki build.
