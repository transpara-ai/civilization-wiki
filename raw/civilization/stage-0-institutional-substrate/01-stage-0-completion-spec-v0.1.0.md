---
doc_id: CIV-V4.1-EPIC-015-STAGE-0-COMPLETION-SPEC
title: Civilization v4.1 Event 15 Stage 0 Completion Spec
doc_type: completion-spec
status: proposal
version: 0.1.0
created: 2026-06-24
updated: 2026-06-24
owner: Michael Saucier
steward: assistant
project: civilization
supersedes: []
related_docs:
  - CIV-V4.1-EPIC-015-INSTITUTIONAL-SUBSTRATE-DOCTRINE
canonical: false
transpara:
  event: 15
  gate: Y
  stage: 0
  mutation_policy: scaffold-only
  done_contract: true
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-STAGE-0-COMPLETION-SPEC type=completion-spec version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 completion-spec no-runtime no-production no-deploy no-existing-tree-move -->

# Civilization v4.1 Event 15 Stage 0 Completion Spec

## Purpose

This document is the Stage 0 "done" contract for the Civilization institutional
substrate migration arc.

Stage 0 is preparation only. It creates the scaffold, copies or indexes
historical material, records provenance, and stops before any action that would
alter the accepted live structure or steer adjacent in-flight Civilization
development.

## Stage 0 Definition

Stage 0 is complete when all of the following are true:

```text
scaffold exists
historical docs copied or indexed
provenance manifest complete
birth-era philosophy indexed
Dark Factory lineage indexed
Platform/transpara-MCP boundary indexed
OpenBrain/wiki pipeline indexed
no live canonical paths altered
no active development steered
verification passed
```

## Required Deliverables

| Deliverable | Required path |
| --- | --- |
| Migration arc README | `README.md` |
| Stage 0 completion spec | `01-stage-0-completion-spec-v0.1.0.md` |
| Provenance manifest | `02-stage-0-provenance-manifest-v0.1.0.md` |
| Birth-era philosophy index | `03-birth-era-philosophy-index-v0.1.0.md` |
| Dark Factory lineage index | `04-dark-factory-lineage-index-v0.1.0.md` |
| Platform/transpara-MCP boundary index | `05-platform-transpara-mcp-boundary-index-v0.1.0.md` |
| OpenBrain/wiki pipeline index | `06-openbrain-wiki-pipeline-index-v0.1.0.md` |
| External research placement index | `08-external-research-placement-index-v0.1.0.md` |
| Corpus index | `corpus/README.md` |
| Copied corpus | `corpus/copied/` |
| Stage 0 closeout report | `07-stage-0-closeout-report-v0.1.0.md` |

## Completion Rules

### Scaffold

The `civilization/` namespace must exist under the docs repo, with Event 15 /
Gate Y rooted at:

```text
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/
```

### Historical Corpus

Historical material may be copied, indexed, or deferred.

Copy when the document is compact, stable, and load-bearing for the birth,
lineage, accepted doctrine, Platform boundary, OpenBrain/wiki pipeline, or
migration arc.

Index when the corpus is large, volatile, generated, or already has a stronger
source-of-truth path.

Defer only when the material is outside Stage 0, inaccessible, binary, too broad
to classify safely, or would risk steering active development.

### Provenance

Every copied or indexed corpus group must record:

```text
source repo
source path
source repo head observed during Stage 0
Stage 0 action: copied, indexed, summarized, or deferred
reason for inclusion
canonicality classification
customer-data risk classification
```

### Birth-Era Philosophy

Birth-era philosophy must be separate from accepted doctrine. It may be raw,
reconstructed, curated, or historical, but it must not be presented as accepted
current authority unless the source already has that status.

### Dark Factory Lineage

Dark Factory must be preserved as the formative production doctrine and
historical lineage inside the larger Civilization umbrella.

Stage 0 must not rename `dark-factory/`.

### Platform And Transpara-MCP Boundary

The Platform boundary must distinguish:

```text
commercial Transpara Platform product knowledge
authorized demo/simulation runtime access
customer production runtime contents
```

Stage 0 must not claim customer production visibility.

### External Research Placement

Competitor and adjacent-technology research must have an explicit home.

Commercial product and market research belongs under the LLC Platform product
knowledge branch. Civilization-adjacent technical research belongs under the
Civilization knowledge branch. Cross-cutting authority or handoff implications
belong under the exchange boundary.

### OpenBrain And Wiki Pipeline

OpenBrain must be treated as raw memory capture. The wiki must be treated as
curated knowledge presentation. Stage 0 may copy or index representative
material, but it must not activate a new ingestion pipeline.

### Non-Interference

Stage 0 must not:

```text
move docs/dark-factory
rename live repo paths
rewrite systemd units
alter production/runtime behavior
modify active Civilization development branches
steer in-flight PRs
change customer/demo access policy
make the new scaffold canonical
claim Test 001 GREEN
commit, push, open PRs, or mark ready
```

## Verification Requirements

At minimum:

```text
git diff --check
find civilization -path "*/corpus/copied/*" -prune -o -type f -name "*.md" -print0 | xargs -0 -r env LC_ALL=C rg -n "[^\\x00-\\x7F]"
npm run verify
```

The copied historical corpus is excluded from the ASCII hygiene check because
Stage 0 preserves source bytes for copied evidence.

If `npm run verify` cannot run, Stage 0 may still close only if the blocker is
recorded with exact command output and the narrower checks pass.

## Stage 1 Preconditions

Stage 1 may not begin until Stage 0 is complete and human approval explicitly
authorizes the next scope.

Stage 1 must name whether it authorizes:

```text
doctrine refinement only
additional corpus copying
dry-run tooling
filesystem migration
repo migration
service binding migration
wiki pipeline activation
OpenBrain capture policy changes
Transpara-MCP access policy changes
```
