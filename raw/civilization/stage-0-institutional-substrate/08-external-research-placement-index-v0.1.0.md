---
doc_id: CIV-V4.1-EPIC-015-EXTERNAL-RESEARCH-PLACEMENT-INDEX
title: Civilization v4.1 Event 15 External Research Placement Index
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
  - CIV-V4.1-EPIC-015-PLATFORM-MCP-BOUNDARY-INDEX
  - CIV-V4.1-EPIC-015-OPENBRAIN-WIKI-PIPELINE-INDEX
canonical: false
transpara:
  event: 15
  gate: Y
  stage: 0
  corpus_domain: external-research-placement
---

<!-- transpara:artifact id=CIV-V4.1-EPIC-015-EXTERNAL-RESEARCH-PLACEMENT-INDEX type=corpus-index version=0.1.0 status=proposal -->
<!-- transpara:scope project=civilization event-15 gate-y stage-0 external-research competitors adjacent-technologies complementary-technologies no-runtime no-production -->

# Civilization v4.1 Event 15 External Research Placement Index

## Purpose

This index places research into competitors, adjacent technologies, and
complementary technologies inside the proposed institutional hierarchy.

## Placement Rule

Use the institutional owner of the research question:

```text
commercial product, sales, partner, market, or competitor question
  -> /Transpara/llc/product/platform/knowledge/

Civilization capability, agent tooling, memory, governance, provenance,
workflow, or autonomous-development question
  -> /Transpara/civilization/knowledge/

cross-boundary decision, authority implication, handoff, or policy
  -> /Transpara/exchange/
```

## LLC Platform Research

Commercial research belongs here:

```text
/Transpara/llc/product/platform/knowledge/
|-- market-landscape/
|-- competitive-intelligence/
`-- complementary-technologies/
```

Examples:

```text
industrial software competitors
RTOI/operations-intelligence market maps
sales positioning
commercial product capability comparisons
partner and integration opportunities
demo-system positioning
customer-facing claims and proof packages
```

This branch is owned by the Transpara LLC product estate. It may inform
Transpara-AI, but it is not raw Civilization memory.

## Civilization Research

Civilization-adjacent research belongs here:

```text
/Transpara/civilization/knowledge/
|-- external-landscape/
`-- adjacent-technologies/
```

Examples:

```text
agent frameworks
multi-agent runtimes
LLM orchestration tools
memory systems
wiki/corpus generation methods
provenance and event-graph systems
workflow engines
review and adversarial-gate harnesses
autonomous software-development systems
OpenBrain-adjacent tools
MCP-adjacent tools
```

This branch is evidence and research until curated or accepted. It does not
become doctrine by being collected.

## Placed Stage 0 Research

| Research item | Placement | Reason |
| --- | --- | --- |
| `TAI-RES-2026-001-v1.0.0-Sakana-AI-Evaluation.md` | `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-001-v1.0.0-Sakana-AI-Evaluation.md` | Sakana AI is an adjacent AI research/product organization. The document evaluates strategic learning opportunities for the Transpara-AI Civilization, so its institutional owner is Civilization external landscape research rather than Platform commercial competitive intelligence. |
| `TAI-RES-2026-002-v1.0.0-Sakana-AI-Adjacent-Landscape.md` | `corpus/copied/civilization/knowledge/external-landscape/sakana-ai/TAI-RES-2026-002-v1.0.0-Sakana-AI-Adjacent-Landscape.md` | This report maps Sakana-adjacent research collaborators, recursive self-improvement work, autonomous research systems, evolutionary AI tooling, and collective-intelligence orchestration. It extends the same Civilization external-landscape research set as `TAI-RES-2026-001`; it is research evidence, not accepted doctrine or Platform competitive positioning. |
| `TAI-RES-2026-002-v1.0.0-Hermes-Agent-Self-Evolution-Evaluation.md` | `corpus/copied/civilization/knowledge/external-landscape/hermes-agent-self-evolution/TAI-RES-2026-002-v1.0.0-Hermes-Agent-Self-Evolution-Evaluation.md` | This report evaluates Hermes Agent, Hermes Self-Evolution, and the relationship between the Hermes optimizer pattern and the Civilization Capability Evolution chain. Its institutional owner is Civilization external landscape research because it concerns governed agent capability evolution, runtime adapters, plugin governance, and research-to-doctrine learning opportunities. It is research evidence, not activation authority, Platform competitive positioning, or accepted doctrine. |

## Exchange Research

Cross-boundary implications belong here:

```text
/Transpara/exchange/
|-- llc-to-civilization/
|-- civilization-to-llc/
|-- platform-demo-authority/
`-- customer-access-authority/
```

Examples:

```text
research that changes demo-system authority
research that changes customer-data claims
research that affects sales promises made by agents
research that changes what Transpara-AI may infer from Platform data
research that changes human approval or review requirements
```

## Wiki Rule

The wiki may publish curated research outputs. It should not be the raw landing
zone for competitor or adjacent-technology research.

The raw-to-published path should be:

```text
research branch
  -> normalized record
  -> curated finding
  -> wiki-input
  -> wiki presentation
```

## Stage 0 Non-Action

Stage 0 defines placement only. It does not migrate existing research files,
change current repo paths, or create live `/Transpara/llc` or
`/Transpara/civilization` filesystem branches.
