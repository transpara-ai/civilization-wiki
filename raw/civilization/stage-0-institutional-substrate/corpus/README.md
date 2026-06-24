---
doc_id: CIV-V4.1-EPIC-015-CORPUS-README
title: Civilization v4.1 Event 15 Stage 0 Corpus
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
  corpus_policy: copies-and-indexes
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-CORPUS-README type=corpus-index version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 corpus copied-indexed no-runtime no-production -->

# Civilization v4.1 Event 15 Stage 0 Corpus

This directory holds Stage 0 source material for the institutional substrate
doctrine arc.

## Layout

```text
corpus/
|-- README.md
`-- copied/
    |-- docs/
    |-- wiki/
    |-- operation/
    |-- platform/
    |-- transpara-mcp/
    `-- OB1/
```

## Policy

Copied files are historical evidence snapshots for this Stage 0 scaffold. They
do not become canonical by being copied here.

The original repo path remains the source of truth unless a later governed
acceptance packet says otherwise.

Large or volatile corpora are indexed rather than copied wholesale. See:

```text
02-stage-0-provenance-manifest-v0.1.0.md
03-birth-era-philosophy-index-v0.1.0.md
04-dark-factory-lineage-index-v0.1.0.md
05-platform-transpara-mcp-boundary-index-v0.1.0.md
06-openbrain-wiki-pipeline-index-v0.1.0.md
```
