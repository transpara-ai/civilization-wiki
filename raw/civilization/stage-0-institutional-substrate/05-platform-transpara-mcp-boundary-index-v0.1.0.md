---
doc_id: CIV-V4.1-EPIC-015-PLATFORM-MCP-BOUNDARY-INDEX
title: Civilization v4.1 Event 15 Platform and Transpara-MCP Boundary Index
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
  corpus_domain: platform-transpara-mcp-boundary
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-PLATFORM-MCP-BOUNDARY-INDEX type=corpus-index version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 platform transpara-mcp demo-simulation customer-data-boundary no-runtime no-production -->

# Civilization v4.1 Event 15 Platform and Transpara-MCP Boundary Index

## Purpose

This index records the Platform boundary correction.

The Transpara Platform is the commercial product. `transpara-mcp` is the
interface that presents authorized live Platform data to Transpara-AI.

Customer production runtime contents are not presumed accessible. Demo and
simulation estates are the authorized live-data substrate available for
demonstration, sales, testing, and Civilization-facing analysis.

## Copied Platform Boundary Material

| Source | Stage 0 path | Why included |
| --- | --- | --- |
| `platform/README.md` | `corpus/copied/platform/README.md` | Product repo anchor. |
| `platform/docs/platform-readme.md` | `corpus/copied/platform/platform-readme.md` | Platform product description anchor. |
| `platform/docs/product-context.md` | `corpus/copied/platform/product-context.md` | Product context and customer/problem framing. |
| `platform/docs/platform-specification.md` | `corpus/copied/platform/platform-specification.md` | Platform capability and specification anchor. |
| `transpara-mcp/README.md` | `corpus/copied/transpara-mcp/README.md` | MCP interface anchor. |
| `transpara-mcp/STATUS.md` | `corpus/copied/transpara-mcp/STATUS.md` | Current MCP status anchor. |
| `transpara-mcp/docs/infrastructure.md` | `corpus/copied/transpara-mcp/infrastructure.md` | Infrastructure and integration boundary anchor. |

## Indexed Platform Repo Family

| Repo | Role in product knowledge |
| --- | --- |
| `platform` | Product knowledge root and repo-family map. |
| `tinstaller` | Bundle, distribution, install/upgrade, image pinning, airgap model. |
| `tsystem-api` | API and runtime configuration rendering. |
| `tstore-interface` | Data-store interface and database capability expectations. |
| `tview` | Product visualization and user-facing surfaces. |
| `deployment` | Deployment examples and historical operational context. |
| `timescale` | Data-layer packaging, CNPG/Timescale extension artifact work. |
| `transpara-py-sdk` | Programmatic Platform access and integration client surface. |
| `transpara-mcp` | Live Platform data interface for authorized demo/simulation estates. |

## Boundary Invariants

```text
commercial Platform product knowledge belongs to the Transpara LLC side
Transpara-AI may reason over authorized product knowledge
Transpara-AI may consume authorized demo/simulation live data
Transpara-AI must not presume customer production data access
customer-specific runtime access requires a separate authority path
```

## Stage 0 Non-Action

Stage 0 does not change Platform access policy, MCP deployment, customer
connectivity, demo connectivity, or runtime credentials.
