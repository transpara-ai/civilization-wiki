---
doc_id: CIV-V4.1-EPIC-015-INSTITUTIONAL-SUBSTRATE-DOCTRINE
title: Civilization v4.1 Event 15 Gate Y Institutional Substrate Doctrine
doc_type: doctrine-plan
status: proposal
version: 0.1.0
created: 2026-06-24
updated: 2026-06-24
owner: Michael Saucier
steward: assistant
project: civilization
supersedes: []
related_docs:
  - CIV-README
  - CIV-V4.1-README
  - DF-V4.0-README
  - DF-V4.0-INTEGRATION-ARC
canonical: false
transpara:
  event: 15
  gate: Y
  semver: 0.1.0
  doctrine_scope: institutional-substrate
  naming_change: dark-factory-to-civilization
  dark_factory_policy: preserve-as-lineage
  mutation_policy: scaffold-only
  filesystem_migration: planned-not-executed
  customer_runtime_access: not-presumed
  demo_runtime_access: authorized-demo-and-simulation-estates
  openbrain_role: canonical-raw-memory-capture
  wiki_role: curated-knowledge-presentation
  transpara_mcp_role: live-platform-data-interface
  acceptance_required: true
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-INSTITUTIONAL-SUBSTRATE-DOCTRINE type=doctrine-plan version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y institutional-substrate transpara-llc transpara-platform transpara-ai docs operation wiki ob1 site hive eventgraph agent work openbrain transpara-mcp filesystem migration-tooling dark-factory-lineage no-runtime no-production no-deploy no-customer-data no-existing-tree-move -->
<!-- transpara:ingest mcp=true chunking=heading hidden_headers=true -->

# Civilization v4.1 Event 15 Gate Y Institutional Substrate Doctrine

## Purpose

This document opens the proposal scaffold for the institutional substrate
doctrine that should govern the next maturity step of the Transpara-AI
Civilization.

The work began as Dark Factory. That name still matters as lineage: it captured
the production doctrine that software work, agent work, review, evidence, and
authority should be treated as governed factory operations. The current system
has grown beyond that seed. It now includes the adjacent relationship between
Transpara LLC and Transpara-AI, the commercial Transpara Platform, the
Civilization repo family, OpenBrain memory, wiki curation, Transpara-MCP live
data access, and the filesystem/migration substrate that gives all of it a
physical shape.

This document is proposal-only. It creates naming and planning scaffolding. It
does not move the existing `dark-factory/` tree, alter runtime paths, authorize
production operation, grant customer data access, deploy services, or change
the accepted v4.0 doctrine.

## Core Thesis

The body of the system should match the ontology of the institution:

```text
Transpara LLC
  human company, commercial owner, legal actor, product steward

Transpara Platform
  commercial industrial software product and runtime estate

Transpara-AI Civilization
  adjacent agent civilization that augments the humans and operates under
  explicit authority, evidence, review, and memory constraints

Exchange boundary
  the formal handoff layer between human company authority, agent action,
  product knowledge, demo runtime data, and customer confidentiality

Machine substrate
  caches, containers, package stores, toolchains, and local runtime support

Archive
  retired material with provenance, manifests, and recovery notes
```

The filesystem, repo charters, wiki pipeline, OpenBrain capture path,
Transpara-MCP interface, and migration tooling are not incidental infrastructure.
They are the physical expression of this ontology.

## Naming Doctrine

`civilization/` should become the umbrella namespace.

`dark-factory/` should be preserved as a lineage and doctrine subset.

The intended relationship is:

```text
Civilization
|-- birth and founding records
|-- doctrine
|-- governance
|-- operations
|-- implementation
|-- events and gates
|-- knowledge and memory
|-- platform alignment
`-- dark-factory lineage
```

The old name is not wrong historically. It is now too narrow.

## Scope

This project includes the entire philosophy and operating substrate embodied in
the alignment of:

```text
Transpara LLC
Transpara Platform
Transpara-AI Civilization
docs
operation
wiki
OB1
site
hive
eventgraph
agent
work
filesystem layout
OpenBrain capture
transpara-MCP
migration tooling
governance and review gates
```

## Institutional Roles

### Transpara LLC

Transpara LLC is the human company. It owns the commercial product, sales
motion, customer relationships, legal obligations, and final human authority.

It is not dissolved into the Civilization. The Civilization augments it.

### Transpara Platform

The Transpara Platform is the commercial industrial software product. It is
constructed from the non-Civilization repo family forked from the Transpara org
and related implementation repos.

The Platform is used in industrial settings such as refineries, electric
generation, pharmaceutical plants, drilling platforms, telecommunications,
satellite monitoring, military weapons production, and adjacent high-criticality
environments.

Customer production runtime contents are customer secrets. Ordinary operation
does not presume physical access by Transpara LLC or Transpara-AI.

### Demo And Simulation Estates

For demonstration, sales, testing, and internal development, Transpara maintains
high-fidelity simulations across multiple industries. These systems are the
authorized live runtime substrate available to Transpara LLC and Transpara-AI.

The doctrine must distinguish:

```text
customer production runtime
  confidential customer asset data
  no presumed access
  requires explicit customer-specific authority

demo and simulation runtime
  Transpara-controlled high-fidelity estates
  authorized for sales and demonstration
  appropriate live-data substrate for Transpara-AI

synthetic fixtures
  local, generated, or static test data
  safe for deterministic tests and public examples
```

### Transpara-AI Civilization

Transpara-AI is the adjacent agent Civilization: a memory-bearing,
review-gated, increasingly capable operating body that augments the humans in
Transpara LLC. It must remain bounded by explicit authority, evidence,
provenance, and review gates.

## Repo Charters

| Repo | Charter |
| --- | --- |
| `docs` | Constitutional and doctrine authority, including Civilization and Dark Factory lineage. |
| `operation` | Living operating model, test plans, incidents, runbooks, surface contracts, and operational status. |
| `wiki` | Curated Civilization knowledge presentation, compiled from accepted and provenance-labeled sources. |
| `OB1` | OpenBrain implementation, capture substrate, memory access, and recall tooling. |
| `site` | Public and operator-facing command surfaces, Civilization views, observability, and live-reader correction surfaces. |
| `hive` | Agent runtime, roles, factory/civilization operation, autonomy barriers, and execution envelopes. |
| `eventgraph` | Causality, authority, provenance, trace semantics, and evidence graph contracts. |
| `agent` | Agent primitives, capabilities, worker substrate, and local execution support. |
| `work` | Task/order model, work lifecycle, readiness, completion semantics, and factory order interfaces. |
| `platform` | Commercial Transpara Platform product knowledge root and repo-family map. |
| `tinstaller` | Platform bundle/distribution, image pinning, install/upgrade paths, and airgap packaging. |
| `tsystem-api` | Platform API and runtime configuration rendering, including TStore/CNPG paths. |
| `tstore-interface` | Platform data-store interface and database capability expectations. |
| `tview` | Platform visualization/user-facing product surface. |
| `deployment` | Historical and current deployment examples, treated as context unless superseded by active runtime code. |
| `timescale` | Platform data-layer artifact work and Timescale/CNPG extension packaging. |
| `transpara-py-sdk` | Programmatic Platform access and integration client surface. |
| `transpara-mcp` | MCP interface that presents authorized live Platform data, especially demo/simulation estates, to Transpara-AI. |

## Transpara-MCP Doctrine

`transpara-mcp` is the live-data interface to the runtime Transpara Platform.
Its job is to present executing Platform state as a source of live data from
assets under management.

It is not a blanket authorization channel into customer systems. Its default
authorized substrate is the Transpara-controlled demo and simulation estate.

Required invariant:

```text
Transpara-AI must not imply access to customer production runtime contents.
Live Platform data access means authorized demo/simulation access unless a
separate customer-specific authority path is recorded.
```

## OpenBrain Capture Doctrine

OpenBrain is canonical raw memory capture for Civilization work.

The capture path should record commits, reviews, pushes, checkpoints, durable
decisions, and operational transitions. Manual duplicate exports into the wiki
should not be the normal path when OpenBrain capture is working.

OpenBrain is not itself published doctrine. It is raw and recallable memory with
provenance.

## Wiki And LLM Artifact Pipeline

The wiki should not be a raw LLM dump. It should render curated knowledge.

The target pipeline is:

```text
OpenBrain / Codex sessions / GitHub / reviews / imports
  -> raw capture
  -> normalized records
  -> curated Civilization knowledge
  -> wiki-input package
  -> wiki repo render
```

Target staging structure:

```text
/Transpara/civilization/knowledge/
|-- raw/
|   |-- openbrain/
|   |-- codex-sessions/
|   |-- github/
|   |-- pr-reviews/
|   |-- issue-events/
|   `-- imports/
|-- normalized/
|-- curated/
|-- wiki-input/
|-- rejected/
`-- quarantine/
```

The wiki repo consumes `wiki-input`. It should not own the whole ingestion and
interpretation pipeline.

## Target Filesystem Doctrine

The proposed mature filesystem shape is:

```text
/Transpara
|-- llc/
|   `-- product/
|       `-- platform/
|           |-- repos/
|           |-- knowledge/
|           |   |-- product-architecture/
|           |   |-- market-landscape/
|           |   |-- competitive-intelligence/
|           |   `-- complementary-technologies/
|           |-- live-data/
|           `-- evidence/
|-- civilization/
|   |-- repos/
|   |-- work/
|   |-- knowledge/
|   |   |-- raw/
|   |   |-- normalized/
|   |   |-- curated/
|   |   |-- external-landscape/
|   |   |-- adjacent-technologies/
|   |   `-- wiki-input/
|   |-- governance/
|   |-- evidence/
|   `-- runtime/
|-- exchange/
|   |-- llc-to-civilization/
|   |-- civilization-to-llc/
|   |-- platform-demo-authority/
|   `-- customer-access-authority/
|-- machine-substrate/
|   |-- caches/
|   |-- containers/
|   |-- package-stores/
|   `-- toolchains/
`-- archive/
    |-- legacy-layouts/
    |-- retired-repos/
    |-- dirty-patch-bundles/
    |-- manifests/
    `-- dated/
```

`machine-substrate/` is deliberately not named `platform/`, because Platform is
the commercial Transpara product.

## External Research Placement Doctrine

Research into competitors, adjacent technologies, and complementary
technologies belongs in different places depending on what the research is for.

Commercial product and market research belongs under the LLC Platform product
knowledge branch:

```text
/Transpara/llc/product/platform/knowledge/
|-- market-landscape/
|-- competitive-intelligence/
`-- complementary-technologies/
```

This includes competitors to the Transpara Platform, industrial software market
maps, sales positioning, partner/complement analysis, product capability
comparisons, and evidence that informs commercial strategy.

Civilization research belongs under the Civilization knowledge branch:

```text
/Transpara/civilization/knowledge/
|-- external-landscape/
`-- adjacent-technologies/
```

This includes agent frameworks, LLM tooling, memory systems, governance systems,
workflow engines, provenance systems, wiki/corpus technologies, autonomous
development tools, and other systems that may inform how the Civilization
evolves.

When a research item affects both the commercial Platform and the Civilization,
the source research should stay in its owning research branch and the shared
decision, handoff, or authority implication should be recorded under:

```text
/Transpara/exchange/
```

The wiki may publish curated research results. It should not be the raw research
landing zone.

## Migration Tooling Doctrine

Migration tooling must be manifest-driven and rollback-aware.

Every planned move should carry:

```text
source_path
target_path
classification
institutional_owner
repo_owner
runtime_owner
authority_required
customer_data_risk
service_impact
rollback_path
validation_command
status
```

Allowed migration verbs:

```text
inventory
classify
map
dry-run
validate
migrate
verify
rollback
archive
```

No tooling should rewrite live service paths, move source repos, or replace
compatibility shims without an accepted migration packet and a rollback plan.

## Project Phases

### Phase 0: Scaffold

Create the `civilization/` namespace and this proposal packet. No existing
canonical tree is moved.

### Phase 1: Doctrine Completion

Expand this packet into accepted doctrine candidates covering repo charters,
filesystem invariants, OpenBrain capture, wiki curation, Transpara-MCP live data
boundaries, and Platform repo-family knowledge.

### Phase 2: Inventory

Generate current-state manifests for repos, worktrees, services, caches,
symlinks, archives, OpenBrain paths, wiki raw inputs, and Platform demo access.

### Phase 3: Mapping

Map current paths to the target institutional layout. Classify each path as
source truth, generated evidence, runtime state, cache, archive, product
knowledge, customer-risk material, or migration tooling.

### Phase 4: Dry Run

Build dry-run tooling that reports all intended changes without mutating paths.

### Phase 5: Review

Run exact-head cross-family adversarial review on the doctrine and dry-run
outputs. Findings must be classified, fixed, or explicitly rejected with
evidence.

### Phase 6: Acceptance

Human acceptance must state exactly what is accepted:

```text
doctrine only
dry-run only
filesystem migration
repo migration
service migration
wiki pipeline activation
OpenBrain capture policy
Transpara-MCP access policy
```

### Phase 7: Physical Migration

Execute in small PRs or host-local operations with manifests, compatibility
links, service checks, and rollback paths.

## Non-Interference Rules

This scaffold does not authorize:

```text
moving docs/dark-factory
renaming live repo paths
rewriting systemd units
touching customer Platform runtime data
deploying services
changing production posture
claiming Test 001 GREEN
claiming customer data visibility
removing compatibility paths
```

## Acceptance Criteria

The Event 15 / Gate Y doctrine is ready for acceptance only when:

```text
the Civilization namespace is documented
the Dark Factory lineage is preserved
the repo charters cover the full repo family
the Platform and transpara-MCP roles are corrected
external research placement is defined
customer production data access is explicitly constrained
demo/simulation access is explicitly named
OpenBrain and wiki roles are separated
the target filesystem has a rollback-aware migration plan
dry-run tooling exists or is explicitly deferred
cross-family review returns zero blockers
human acceptance text names the authorized scope
```

## Initial Deliverables In This Scaffold

```text
civilization/README.md
civilization/v4.1/README.md
civilization/v4.1/implementation/epics/README.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/README.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/01-stage-0-completion-spec-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/02-stage-0-provenance-manifest-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/03-birth-era-philosophy-index-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/04-dark-factory-lineage-index-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/05-platform-transpara-mcp-boundary-index-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/06-openbrain-wiki-pipeline-index-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/07-stage-0-closeout-report-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/corpus/README.md
```

## Current Status

Status: Stage 0 scaffold created, proposal only.

The next practical step is to add inventory and mapping artifacts under this
same epic, then run review against the exact head before any physical migration
is attempted.
