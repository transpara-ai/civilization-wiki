---
doc_id: CIV-V4.1-EPIC-015-STAGE-0-CLOSEOUT
title: Civilization v4.1 Event 15 Stage 0 Closeout Report
doc_type: closeout-report
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
  - CIV-V4.1-EPIC-015-STAGE-0-PROVENANCE-MANIFEST
canonical: false
transpara:
  event: 15
  gate: Y
  stage: 0
  closeout: true
  mutation_policy: scaffold-only
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-STAGE-0-CLOSEOUT type=closeout-report version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 closeout verified no-runtime no-production no-deploy no-existing-tree-move no-commit no-pr -->

# Civilization v4.1 Event 15 Stage 0 Closeout Report

## Result

Stage 0 is complete.

The Civilization institutional substrate scaffold exists, historical material is
copied or indexed, provenance is recorded, and verification passed.

This closeout does not make the scaffold canonical. It does not authorize Stage
1. It stops before any action that would alter live canonical structure, active
development, service bindings, runtime behavior, customer/demo access policy, or
accepted doctrine.

## Completion Against Stage 0 Definition

| Requirement | Status | Evidence |
| --- | --- | --- |
| scaffold exists | complete | `civilization/`, `civilization/v4.1/`, and Event 15 epic path exist. |
| historical docs copied or indexed | complete | `corpus/copied/` contains 58 copied files; indexed groups recorded in provenance/index docs. |
| provenance manifest complete | complete | `02-stage-0-provenance-manifest-v0.1.0.md`. |
| birth-era philosophy indexed | complete | `03-birth-era-philosophy-index-v0.1.0.md`. |
| Dark Factory lineage indexed | complete | `04-dark-factory-lineage-index-v0.1.0.md`. |
| Platform/transpara-MCP boundary indexed | complete | `05-platform-transpara-mcp-boundary-index-v0.1.0.md`. |
| OpenBrain/wiki pipeline indexed | complete | `06-openbrain-wiki-pipeline-index-v0.1.0.md`. |
| external research placement indexed | complete | `08-external-research-placement-index-v0.1.0.md`. |
| no live canonical paths altered | complete | No existing `dark-factory/` files were moved or renamed. |
| no active development steered | complete | No PRs, branches, service configs, or runtime repos were changed. |
| verification passed | complete | `git diff --check`, authored-doc ASCII check, and `npm run verify` passed. |

## Files Created

Authored Stage 0 docs:

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
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/08-external-research-placement-index-v0.1.0.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/corpus/README.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/inventory/README.md
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/manifests/README.md
```

Copied corpus:

```text
civilization/v4.1/implementation/epics/epic-15-institutional-substrate-doctrine/corpus/copied/
```

The copied corpus contains 60 files.

Fail-legible count note: this copied closeout source carries two source-era
counts, 58 in the completion table and 60 in this section. The wiki mirror has
not revalidated the originating `docs` checkout corpus count; treat the mismatch
as preserved provenance drift, not as a live wiki count.

## Files Copied

Copied groups:

```text
docs/dark-factory seed files
docs/dark-factory phase-record kernel/audit/SOP files
docs/dark-factory v3 lineage files
docs/dark-factory v3.8 acceptance files
docs/dark-factory v3.9 doctrine files
docs/dark-factory v4.0 doctrine and integration arc files
docs/dark-factory v4.0 birth/research files
wiki raw Searles source corpus
wiki raw Transpara Dark Factory source mirror
wiki README, DESIGN, PROVENANCE
wiki representative curated Civilization/Dark Factory pages
operation README and existential test plan
platform README and product/specification anchors
transpara-mcp README, STATUS, infrastructure anchor
OB1 README and safe memory provenance anchor
Sakana AI external-landscape research set
Hermes Agent self-evolution external-landscape evaluation
```

Detailed source/destination provenance is recorded in:

```text
02-stage-0-provenance-manifest-v0.1.0.md
```

## Files Referenced Or Indexed

Indexed groups:

```text
wiki/raw/open-brain/2026-03.md through 2026-06.md
wiki/wiki/*.md full curated article corpus
docs/dark-factory/archive/v2
docs/dark-factory/archive/v3.1 through v3.7
docs/dark-factory/v3.9/implementation
docs/dark-factory/v4.0/implementation/epics/epic-*
site
hive
eventgraph
agent
work
tinstaller
tsystem-api
tstore-interface
tview
deployment
timescale
transpara-py-sdk
```

These were indexed rather than copied wholesale to avoid unnecessary churn and
to avoid steering active development.

## Verification Run

Commands:

```text
git diff --check
find civilization -path "*/corpus/copied/*" -prune -o -type f -name "*.md" -print0 | xargs -0 -r env LC_ALL=C rg -n "[^\\x00-\\x7F]"
npm run verify
```

Result:

```text
git diff --check: passed
authored-doc ASCII hygiene excluding copied corpus: passed
npm run verify: passed
```

`npm run verify` included:

```text
gate-n:test
gate-n:check
canonical-repo-names:test
canonical-repo-names:check
exact-head-approval:test
openbrain-capture:test
typecheck
docusaurus build
```

The Docusaurus build completed successfully. It emitted the existing Rspack
deprecation and `vscode-languageserver-types` dynamic-require warning; those
were not introduced as blocking Stage 0 failures.

## What Was Not Changed

Stage 0 did not:

```text
move docs/dark-factory
rename any live repo path
rewrite systemd units
alter production/runtime behavior
modify active Civilization development branches
steer in-flight PRs
change customer/demo access policy
make the new scaffold canonical
claim Test 001 GREEN
commit
push
open a PR
mark anything ready
```

## Stage 1 Boundary

The next stage requires explicit human authorization. Stage 1 must name whether
it is authorizing doctrine refinement, additional corpus copying, dry-run
tooling, filesystem migration, repo migration, service binding migration, wiki
pipeline activation, OpenBrain capture policy changes, or Transpara-MCP access
policy changes.
