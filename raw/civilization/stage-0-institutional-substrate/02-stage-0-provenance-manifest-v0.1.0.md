---
doc_id: CIV-V4.1-EPIC-015-STAGE-0-PROVENANCE-MANIFEST
title: Civilization v4.1 Event 15 Stage 0 Provenance Manifest
doc_type: provenance-manifest
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
  manifest_scope: copied-and-indexed-corpus
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-STAGE-0-PROVENANCE-MANIFEST type=provenance-manifest version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 provenance no-runtime no-production no-customer-data -->

# Civilization v4.1 Event 15 Stage 0 Provenance Manifest

## Observed Repo Heads

| Repo | Observed HEAD | Dirty entries at inventory |
| --- | --- | ---: |
| `docs` | `16d08d6f3c41a48f8fa5ccd15e5a8c5953522986` | 1 |
| `operation` | `3cc71edba561f70209043f237d9a8ff61969d243` | 0 |
| `wiki` | `8ddbd3cb33743fb6d120e1935ba620a76d5551e7` | 0 |
| `OB1` | `1c4c9069fba06f82411005c77dafac8711805bdc` | 3 |
| `site` | `185ff54ce87511b1fed25b9eb53810882ba8c6ba` | 0 |
| `hive` | `b5e630e31b62823b1e4fe200c88aae6f82495426` | 6 |
| `eventgraph` | `80c5531cb698c4f1bd13e62fb9aade474428e95c` | 0 |
| `agent` | `cc343a86085dccedc8641b37a688019142d70b9d` | 1 |
| `work` | `12c03eacec4723ea735b2fee32b19ef6a2d7d331` | 0 |
| `platform` | `4341d9031806d53d000e8150876aa64d47f80cd7` | 0 |
| `transpara-mcp` | `125181b6285a8f23842dc30ddac42a522aa8b028` | 2 |
| `tinstaller` | `1ccf7dbb84926a5e6a3851c57937531e8b1e950e` | 2 |
| `tsystem-api` | `ed7337ddfbfb3b98635e4f4d7574403f1ca26c0d` | 0 |
| `tstore-interface` | `fbbd5e47e1fee4f8f1095334d59d0f18c907aa52` | 0 |
| `tview` | `7a6af0ba7f5d83904b5e8bbe4477151b2b58878c` | 0 |
| `deployment` | `83df58b9e5792776073f78399cd5f415df274888` | 0 |
| `timescale` | `a5d61d54588c2a8ffc8ba97aac24414b193fcdc3` | 0 |
| `transpara-py-sdk` | `0a8daf6ad56902cae04f5268271b617c467498cc` | 9 |

Dirty entries were observed but not modified. Stage 0 did not clean or steer
those repos.

## Copied Corpus Groups

| Group | Source | Destination | Action | Reason | Canonicality | Customer-data risk |
| --- | --- | --- | --- | --- | --- | --- |
| Dark Factory seed | `docs:dark-factory/{README.md,Dark Factory - Motive, Goal, Approach.md,civic-roles.md}` | `corpus/copied/docs/dark-factory/seed/` | copied | Birth-era production-doctrine seed from docs | historical / source-derived | none expected |
| Phase-record kernel | `docs:dark-factory/phase-record/{DF-SPEC-0001,DF-AUDIT-0001,DF-SOP-0001}` | `corpus/copied/docs/dark-factory/phase-record/` | copied | Early kernel, audit, and authority-gated side-effect doctrine | historical / source-derived | none expected |
| v3 lineage | `docs:dark-factory/archive/v3/{README.md,dark-factory-v3-manifesto.md}` | `corpus/copied/docs/dark-factory/v3/` | copied | Manifesto and archived v3 lineage | historical | none expected |
| v3.8 acceptance | `docs:dark-factory/archive/v3.8/{README.md,checkpoint-2026-05-12-v3.8-acceptance.md}` | `corpus/copied/docs/dark-factory/v3.8/` | copied | Accepted pre-v3.9 baseline and acceptance proof | accepted historical | none expected |
| v3.9 doctrine | `docs:dark-factory/v3.9/*.md` | `corpus/copied/docs/dark-factory/v3.9/` | copied | Accepted canonical pre-v4 line and implementation state | accepted historical | none expected |
| v4.0 doctrine | `docs:dark-factory/v4.0/*.md` plus integration arc | `corpus/copied/docs/dark-factory/v4.0/` | copied | Current accepted doctrine and integration arc | accepted current source snapshot | none expected |
| v4.0 review/research | `docs:dark-factory/research/checkpoints/2026-06-01-01-development-process-adversarial-review.md` | `corpus/copied/docs/dark-factory/research/` | copied | Birth of v4 doctrine shift | historical evidence | none expected |
| Civilization landscape | `docs:dark-factory/research/civilization-landscape-progress.md` | `corpus/copied/docs/dark-factory/research/` | copied | Landscape and adjacent project lineage | historical evidence | none expected |
| Reunification | `docs:dark-factory/reunification/README.md` | `corpus/copied/docs/dark-factory/reunification/` | copied | Reunification workstream index | historical evidence | none expected |
| Searles raw corpus | `wiki:raw/searles/all-posts-1.md` | `corpus/copied/wiki/raw/searles/all-posts-1.md` | copied | Birth-era philosophical source corpus | raw historical / not accepted doctrine | none expected |
| Wiki raw Transpara seed | `wiki:raw/transpara/dark-factory/*` | `corpus/copied/wiki/raw/transpara/dark-factory/` | copied | Wiki source mirror of Dark Factory seed material | raw historical / not accepted doctrine | none expected |
| Wiki design/provenance | `wiki:{README.md,PROVENANCE.md,DESIGN.md}` | `corpus/copied/wiki/` | copied | Wiki knowledge-substrate design and provenance contract | current source snapshot | none expected |
| Wiki curated pages | `wiki:wiki/{the-civilization.md,dark-factory.md,v3-9.md,v4-0.md}` | `corpus/copied/wiki/wiki/` | copied | Representative curated wiki outputs for Civilization and Dark Factory | curated presentation | none expected |
| Operation baseline | `operation:{README.md,docs/001-existential-test-plan.md}` | `corpus/copied/operation/` | copied | Operating model and existential test boundary | current source snapshot | none expected |
| Platform product docs | `platform:{README.md,docs/platform-readme.md,docs/product-context.md,docs/platform-specification.md}` | `corpus/copied/platform/` | copied | Commercial Platform product knowledge anchor | current source snapshot | product-sensitive but no customer runtime data expected |
| Transpara-MCP boundary | `transpara-mcp:{README.md,STATUS.md,docs/infrastructure.md}` | `corpus/copied/transpara-mcp/` | copied | Live Platform data interface anchor | current source snapshot | product-sensitive; customer data not copied |
| OpenBrain provenance | `OB1:{README.md,docs/safe-agent-memory-provenance.md}` | `corpus/copied/OB1/` | copied | OpenBrain capture and provenance boundary | current source snapshot | none expected |
| Sakana AI evaluation | attachment:`TAI-RES-2026-001-v1.0.0-Sakana-AI-Evaluation.md` | `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-001-v1.0.0-Sakana-AI-Evaluation.md` | copied | Civilization external-landscape and adjacent-technology evaluation | released internal research / not accepted doctrine | confidential internal; no customer runtime data expected |
| Sakana AI adjacent landscape | attachment:`TAI-RES-2026-002-v1.0.0-Sakana-AI-Adjacent-Landscape.md` | `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-002-v1.0.0-Sakana-AI-Adjacent-Landscape.md` | copied | Civilization external-landscape research on Sakana-adjacent technologies and organizations | released internal research / not accepted doctrine | confidential internal; no customer runtime data expected |
| Hermes Agent self-evolution evaluation | attachment:`TAI-RES-2026-002-v1.0.0-Hermes-Agent-Self-Evolution-Evaluation.md` | `corpus/copied/civilization/knowledge/external-landscape/hermes-agent-self-evolution/TAI-RES-2026-002-v1.0.0-Hermes-Agent-Self-Evolution-Evaluation.md` | copied | Civilization external-landscape research on Hermes Agent, Hermes Self-Evolution, and governed capability evolution | released internal research / not accepted doctrine | confidential internal; no customer runtime data expected |

## Indexed Or Deferred Corpus Groups

| Group | Source | Action | Reason |
| --- | --- | --- | --- |
| OpenBrain monthly raw exports | `wiki:raw/open-brain/2026-03.md` through `2026-06.md` | indexed | Large raw memory corpus; better tracked by OpenBrain and wiki provenance until a curation pass is authorized. |
| Full wiki article corpus | `wiki:wiki/*.md` | indexed | Curated presentation layer is broad; representative pages copied and full corpus indexed. |
| Full v3.1-v3.7 archive | `docs:dark-factory/archive/v3.1` through `v3.7` | indexed | Historical lineage is large and superseded; representative v3/v3.8/v3.9/v4.0 line copied. |
| Active event packets beyond integration arc | `docs:dark-factory/v4.0/implementation/epics/epic-*` | indexed | Accepted current work is broad and in-flight adjacent; copying all event packets risks unnecessary churn. |
| Runtime source repos | `site`, `hive`, `eventgraph`, `agent`, `work` | indexed | Stage 0 documents charters only; it does not steer active development. |
| Platform implementation repos | `tinstaller`, `tsystem-api`, `tstore-interface`, `tview`, `deployment`, `timescale`, `transpara-py-sdk` | indexed | Product family is broad; Stage 0 records repo heads and boundary docs without copying all implementation docs. |

## Representative Checksums

| Copied file | SHA-256 |
| --- | --- |
| `corpus/copied/wiki/raw/searles/all-posts-1.md` | `f5f25567b7469abc581736230a00581ef60b1f8321e80856c62f1c60b11bd512` |
| `corpus/copied/docs/dark-factory/v4.0/README.md` | `f6a3bb939a3f68280601c8caca832896f0e424d956090b948fd4bf83526021cd` |
| `corpus/copied/docs/dark-factory/v3.9/README.md` | `5000cfe8aece9da4670dde842f5f427a6b0235738206024391d92d4181400951` |
| `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-001-v1.0.0-Sakana-AI-Evaluation.md` | `d619454f68dced587dce9d8c38b0cd333ac8875ccecf96321e8ebd506e83c2d0` |
| `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-002-v1.0.0-Sakana-AI-Adjacent-Landscape.md` | `7e4c149494c7d9b79b8d1f4c19f8a55d0bdabedb6216182b23105527b6118447` |
| `corpus/copied/civilization/knowledge/external-landscape/hermes-agent-self-evolution/TAI-RES-2026-002-v1.0.0-Hermes-Agent-Self-Evolution-Evaluation.md` | `a7b119333702225f2be4a54a95357de4560da4ff179b8c8e7667f5648a62a7f9` |
