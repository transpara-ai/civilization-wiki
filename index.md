---
title: Civilization Wiki — index
last_compiled: 2026-06-13
run: Run-2 (arc spine + landscape survey + investigation entities)
status: partial — arc spine, architecture, and the investigated-landscape entities compiled; full corpus sweep still deferred
article_count: 61
---

# Civilization Wiki — index

The arc spine and article index for the Transpara-AI Civilization wiki. This is a
[Karpathy-style LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
a self-maintaining, interlinked knowledge substrate compiled from the corpus
(see `DESIGN.md`). The wiki is the source of truth for the narrative; every
downstream view (Mission Control, the spine/story view) is a read lens onto it.

---

## ⚠ Freshness — read this first (fail-loud)

| Field | Value |
|---|---|
| **last_compiled** | **2026-06-13** |
| **run** | **Run-2 (arc spine + landscape survey + investigation entities)** |
| **articles compiled** | **61** (12 foundational · 14 architecture · 8 arc · 15 investigation · 12 concept) |
| **completeness** | **PARTIAL — this is the arc plus the investigated landscape, not the whole corpus** |

**This is Run-2, not the finished wiki.** Run-1 compiled the core spine the
grounded record supported (the Searles source philosophy, the architecture
entities, and the dark-factory arc through the 2026-06-05 reunification). Run-2
extends that: the three formerly-TBD arc nodes now have their own articles (the
lovyou.ai fork, the Civilization Landscape Investigation, and a single
dark-factory umbrella), the Searles thirteen-graphs / cognitive-grammar
philosophy is filled in, and the **fifteen landscape entities** the 2026-05-13
investigation surveyed (gStack, Paperclip, Symphony, Multica, Hermes, OpenClaw,
PageIndex, MemPalace, OB1, the Miro stack, the Agent Governance Toolkit, and the
rest) are compiled as `investigation`-tier articles. **The full corpus is still
not swept** — the ~8,783-file / ~73-repo / ~1,175-thought substrate named in
`DESIGN.md` has not been exhausted, and two of the four `raw/` source tiers
(`open_brain`, `upstream_context`) are still **declared but unmirrored** (see
`PROVENANCE.md`). Treat any concept not in the article index below as
**not-yet-compiled**, not as absent from the project.

**Fail-legible by construction.** Where this index would otherwise emit a link to
an article that does not exist, it instead writes **TBD** and says why. No
wikilink below points at a missing file; gaps are marked, never invented. Every
`[[...]]` link in this index resolves to a real file in `wiki/`.

**Known compile-time tensions carried up from the articles** (stated, not
silently resolved):
- **Nine vs ten civic roles.** The code-grounded count is **nine**
  (`[[civic-roles]]`, `[[the-civilization]]`, and the canonical roles catalog
  all enumerate nine `StarterAgents()`). `[[the-drift]]` previously said "ten
  bootstrap civic roles" while listing only nine names; Run-2 corrected its
  wording to **nine**, consistent with its own list. This index uses **nine**.
- **v4.0 status.** Seed doctrine **accepted 2026-06-12**; the v4.0 folder is
  **candidate / proposal-only and not canonical**. v3.9 remains operative. See
  `[[v4-0]]` and `[[v3-9]]`.
- **Repo identity (event graph).** The Searles posts name `mind-zero-five`; the
  dark-factory docs and Open Brain name `transpara-ai/eventgraph` (and
  `lovyou-ai/eventgraph`). They are **not asserted to be the same repo**. See
  `[[event-graph]]` and `[[the-lovyou-ai-fork]]`.
- **The Feb genesis is reconstructed, not derived from commits.** Day one is not
  in the digital record (org forks start 3/30; Open Brain starts 3/3). It is
  reconstructed from `raw/searles/` and the Substack post dates. See
  `[[the-20-primitives]]`, `[[the-lovyou-ai-fork]]`, and `DESIGN.md` §"The Feb
  genesis."
- **"Civilization" the survey vs the operative concept.** The 2026-05-13
  **Civilization Landscape Investigation** was the *name of a one-time survey*;
  the drift diagnosis later found "civilization" appeared only ×8 in the v3.9
  folder, all referring to that survey, not a living civilization. See
  `[[civilization-landscape-investigation]]` and `[[the-drift]]`.

---

## The arc

A chronological spine from day one to the present. Each `[[...]]` link is a
compiled article; **TBD** marks a node the grounded record names but the wiki has
not yet given its own article.

### 1 — Day one: the 20 primitives (2026-02-28)

The whole arc starts on **2026-02-28** with Matt Searles' post *"20 Primitives
and a Late Night."* The origin was a narrow engineering question — *how do you
trace a bad outcome back to the thing that caused it, and where exactly did the
chain break?* — answered with an event graph where every node has an input, an
operation, and an output, and everything is traceable to its source. The seed was
produced by **incremental specification loading** (feed the model the vision one
message at a time, each ending "Respond ok," before asking for synthesis), the
method that outlived the post. → **`[[the-20-primitives]]`**

> Genesis caveat: this day predates the first fork and the runtime, and survives
> only in the source corpus — reconstructed from `raw/searles/` and post dates,
> not from commit history.

### 2 — The philosophy: the derivation ladder and the irreducibles

From the seed, Searles (working with Claude) built out a philosophy across the
2026-02-28 → early-March posts. The primitives climb a **derivation ladder —
20 → 44 → 200** — across fourteen layers (`[[the-primitives]]`,
`[[fourteen-layers]]`, `[[the-20-primitives]]`), reachable by a small
**cognitive grammar** of operations (`[[the-cognitive-grammar]]`,
`[[derivation-method]]`, `[[higher-order-operations]]`). The ontology is
**self-referential** — a **strange loop**, Return-to-Event (`[[strange-loop]]`).
The framework names **three things it explicitly cannot derive** — moral status,
consciousness, being — and an is-ought bridge offered as hypothesis, not proof
(`[[three-irreducibles]]`, `[[second-derivation-convergence]]`,
`[[the-moral-ledger]]`). The philosophy guards itself against being a closed
system (`[[the-cult-test]]`, `[[the-permanent-tensions]]`,
`[[three-evaluative-axes]]`), and reads the node's-eye view of all this as lived
experience (`[[node-phenomenology]]`, `[[religion-as-paths-from-being]]`).

Three load-bearing architectural ideas fall out of the philosophy and carry
forward into every later build:
- **The event graph** — append-only, hash-chained, causally linked; "the moral
  ledger at scale." → `[[event-graph]]`
- **Intelligence is just another operation type** — the AI stays *inside* the
  accountability graph as a node, never above it. → `[[intelligence-is-an-operation-type]]`
- **The authority layer** — graduated consent (Required / Recommended /
  Notification). → `[[authority-layer]]`

These are demonstrated, not just argued, in **mind-zero-five** — the running Go
code Searles published as *"The Architecture of Accountable AI"* (the operational
"it runs right now" claim is the author's testimony; the wiki read the prose and
quoted excerpts, not the repo). → `[[accountable-ai-architecture]]`,
`[[crash-recovery-as-ethics]]`

The product horizon Searles sketches on top of the same substrate — one event
graph, thirteen lenses — is `[[thirteen-graphs]]`, with the first two layers
compiled as `[[the-market-graph]]` and `[[the-social-graph]]`, and the
edges-over-nodes proposal as `[[edge-weights-as-personality]]` and
`[[the-four-strategies]]`. The corpus is taken into the Transpara work as the
**Searles primitive basis** — **motive, vocabulary, and accountability premise
only**, never as proven metaphysics or implementation authority. →
`[[primitive-basis]]`

### 3 — The lovyou.ai fork (Feb–March 2026)

Searles' own first system was **hive0 / LovYou** — a multi-agent system on the 20
primitives that grew to "roughly seventy agents," most of which he says he did not
design ("the hive had decided it needed them"). That LovYou / `lovyou-ai` lineage
is the upstream the Transpara runtime was **forked** from: the earliest captured
spawn-lifecycle thoughts name the repo `lovyou-ai-hive` before the `transpara-ai`
fork convention took hold, and an early guardian-governance fix landed on the
`lovyou-ai`/upstream hive. Under `transpara-ai` ownership the forked repos
(`agent`, `eventgraph`, `hive`, `site`, `work`, plus `docs`) became the substrate
the live `[[hive-governance]]` runtime and the whole `[[dark-factory]]` arc are
built on. → **`[[the-lovyou-ai-fork]]`**

> Fail-legible: the **2026-03-30 fork date** of those five repos is asserted by
> the task framing, not corroborated by a capture (earliest captured repo work is
> 2026-04-08/09); the **Feb-2026 first fork-and-build** predates both the org
> GitHub history and Open Brain (which starts 2026-03-03) and is reconstructed,
> not recorded. The fork's philosophy is `[[primitive-basis]]`; upstream is cited
> as context only, never re-published. See also `[[agent]]`, `[[hive-governance]]`.

### 4 — The Civilization Landscape Investigation (2026-05-13)

On **2026-05-13** a **Civilization Landscape Investigation** was run: a single
multi-phase research session that surveyed a fixed 22-item candidate list (native
Dark Factory core, prior in-house research, and a wide cut of the external
agent-tooling landscape) and asked of each — *is this already in the design; if
not, what is its exact marginal contribution, and what would it replace,
strengthen, or make possible?* Its headline conclusion was that **no surveyed
tool beats the native kernel**; its lasting product was the eight gaps it found
and the U1–U10 update set that defines the v3.8 → v3.9 delta. Concretely,
**v3.9 = the accepted v3.8 baseline + this investigation**, with external
frameworks routed to references / optional adapters / patterns and kept out of
all control roles (v3.9 Decision 15). →
**`[[civilization-landscape-investigation]]`**, **`[[v3-9]]`**

> The fifteen surveyed tools that now have their own `investigation`-tier
> articles — `[[gstack]]`, `[[paperclip]]`, `[[symphony]]`, `[[multica]]`,
> `[[hermes-agent]]`, `[[openclaw]]`, `[[pageindex]]`, `[[mempalace]]`,
> `[[ob1]]`, `[[miro-stack]]`, `[[agent-governance-toolkit]]`,
> `[[solo-orchestrator]]`, `[[graphify]]`, `[[claw-code]]`,
> `[[bitsandpieces]]` — were compiled from the first-party survey checkpoints
> and Open Brain, **not** from `raw/investigations/*`, which is still empty
> (Phase 2, per `PROVENANCE.md`). They are the landscape *as Transpara
> evaluated it*, not a re-publication of each upstream project.

### 5 — The nine-agent civilization design

The Transpara design names a **society of nine civic roles** — strategist,
planner, implementer, reviewer, guardian, cto, spawner, allocator, sysmon — the
`AgentDef` structs registered by `StarterAgents()` in `pkg/hive/agentdef.go`.
They coordinate **only through the shared append-only event graph** (the
"hive-mind property, obtained for free"), with the human as the top authority
tier. Only `implementer` has filesystem access; `guardian` sits outside the
hierarchy and reports to the human; `spawner` + a growth loop can add new
trust-gated members (`CanOperate=false`) at runtime. → **`[[civic-roles]]`**

This society is the engine of the **north-star model: "one civilization, one
business"** — the civic roles and growth loop *perform and govern* the factory.
→ **`[[the-civilization]]`**

> Fail-legible: this is the **Transpara nine**, distinct from Searles' ~70-agent
> hive0 (`[[primitive-basis]]`, `[[the-lovyou-ai-fork]]`). `[[the-drift]]`'s
> wording was corrected from "ten" to **nine** in Run-2.

### 6 — The drift, then the reunification (2026-06-05)

By **2026-06-05** the build had **drifted**: it had grown **two systems on one
event-graph substrate that never connected** — a living `[[hive-governance]]`
civilization with a working growth loop, and a standalone dark-factory
accountability pipeline (the `work/epic*.go` Gate A–J fixtures) running *beside*
it, not *through* it. The diagnosis is reproducible from source
(`grep -rnE 'guardian|cto|spawner|strategist' work/epic*.go` returns no
civic-role references) and summarized as **"the cage was perfected; the
inhabitants never moved in."** → **`[[the-drift]]`**

The same day, the **reunification workstream** opened (`authority: planning`,
demonstration-first) to pull the program back onto "one civilization, one
business": prove the reunion with one real `FactoryOrder` run before rewriting
doctrine. The civilization's **first reunified act was to document its own
society** (it wrote `civic-roles.md`). → **`[[the-reunification]]`**,
**`[[the-civilization]]`**

### 7 — The present (as of 2026-06-13)

The governed-production effort now has a single umbrella article,
**`[[dark-factory]]`**, synthesizing the orientation doc and the version lineage
(v2 2026-05-10 → v3.0 2026-05-11 → v3.9 accepted 2026-06-05 → v4.0 doctrine
accepted 2026-06-12). Within it:

- **`[[v3-9]]` is the operative baseline** — accepted by Michael Saucier on
  **2026-06-05**; the canonical doc/spec baseline for all current
  implementation. Its gate completions are real but **bounded-fixture**, not
  general production proofs.
- **`[[v4-0]]` is candidate doctrine** — seed folder opened **2026-06-01**, seed
  ADR (*the development process is itself a governed Civilization function — the
  factory builds the factory*) **accepted 2026-06-12**. The v4.0 folder remains
  **proposal-only and not canonical**; it does **not** supersede v3.9 and
  authorizes no implementation.
- **`[[base-slice-0]]` is the control-plane proof** — the minimal end-to-end
  slice the local-deterministic runtime must pass before anything else is
  eligible. Whether it has actually run green is **asserted-as-target, not
  proven-as-done** in the sources read this run.
- **The reunification remains demonstration-first and unaccepted as v4.0
  doctrine.** The Civilization is the model the program is converging toward and
  actively demonstrating slice by slice — not yet accepted doctrine.

> **TBD (deferred to a later run): "the present" beyond the reunification
> frontier.** Later artifacts (the 2026-06-09 deployment arc, the 2026-06-10
> execution plan) carry the model forward toward a continuously operated factory,
> proposal-only; the wiki captures them only as they surface inside `[[v4-0]]`,
> `[[dark-factory]]`, `[[hive-governance]]`, `[[site]]`, and `[[work]]`, not as
> their own arc articles.

---

## Article index

61 articles compiled, grouped by tier. Tier is taken verbatim from each article's
frontmatter.

### Foundational — the Searles source philosophy (12)

The accepted philosophical basis (motive and vocabulary only, never proven
metaphysics or implementation authority).

| Article | Entity |
|---|---|
| `[[the-20-primitives]]` | The 20 Primitives — day one of the arc (2026-02-28) |
| `[[the-primitives]]` | The Primitives — derivation ladder: 20 → 44 → 200 |
| `[[fourteen-layers]]` | The Fourteen Layers — the Layer 0–13 vertical stack |
| `[[the-cognitive-grammar]]` | The Cognitive Grammar — Derive / Traverse / Need |
| `[[derivation-method]]` | The Derivation Method — how the primitives were derived |
| `[[strange-loop]]` | The Strange Loop — the self-referential ontology (Return-to-Event) |
| `[[three-irreducibles]]` | The Three Irreducibles — is-ought / the moral-ledger argument |
| `[[event-graph]]` | The Event Graph — append-only, hash-chained "moral ledger" / kernel |
| `[[intelligence-is-an-operation-type]]` | Intelligence Is Just Another Operation Type — the AI stays in the graph |
| `[[authority-layer]]` | The Authority Layer — graduated consent (Required / Recommended / Notification) |
| `[[accountable-ai-architecture]]` | The Architecture of Accountable AI (mind-zero-five) — the running-code proof |
| `[[the-permanent-tensions]]` | The Permanent Tensions — the four unresolvable axes (anti-utopian feature) |

### Architecture — the entities the system is built from (14)

The standing components and design objects of the platform/runtime, including the
basis and north-star entities.

| Article | Entity |
|---|---|
| `[[primitive-basis]]` | Searles Primitive Basis — source philosophy, as motive/vocabulary only |
| `[[agent]]` | Agent — identity and lifecycle core (`transpara-ai/agent`) |
| `[[hive-governance]]` | Hive / Governance Layer — the civilization runtime (`transpara-ai/hive`) |
| `[[civic-roles]]` | Hive Civic Roles — the nine bootstrap agents (`StarterAgents()`) |
| `[[the-civilization]]` | The Civilization — "one civilization, one business" (north star) |
| `[[factory-order]]` | FactoryOrder — the durable unit of work / unit of cooperation |
| `[[work]]` | Work — the production DAG and task lifecycle (`transpara-ai/work`) |
| `[[gates]]` | Gates — verification, trace, and release gates (A–J; K/L are v4.0) |
| `[[runtime-broker]]` | RuntimeBroker — the bounded execution envelope |
| `[[the-mind-loop]]` | The Mind Loop — the bounded autonomous self-improvement loop (mind-zero-five) |
| `[[capability-evolution]]` | Capability Evolution — governed self-improvement as production work |
| `[[memory-knowledge-advisory]]` | Memory and Knowledge — the advisory-only layer (incl. this LLM wiki) |
| `[[edge-weights-as-personality]]` | Edge Weights as Personality — the (proposed) weighted-graph extension |
| `[[site]]` | Site — the governed operator console (Gate-E surface, society view) |

### Arc — the dark-factory chronology and turning points (8)

The dated stations of the narrative: the upstream fork, the landscape survey, the
umbrella, the operative baseline, the candidate doctrine shift, the control-plane
proof, the diagnosed drift, and its correction.

| Article | Entity |
|---|---|
| `[[the-lovyou-ai-fork]]` | The lovyou.ai Fork — upstream → `transpara-ai` (Feb–Mar 2026) |
| `[[civilization-landscape-investigation]]` | The Civilization Landscape Investigation — the 22-item survey (2026-05-13) |
| `[[dark-factory]]` | Dark Factory — the umbrella over the governed-production effort |
| `[[v3-9]]` | Dark Factory v3.9 — operative baseline (accepted 2026-06-05) |
| `[[v4-0]]` | Dark Factory v4.0 — candidate doctrine shift (seed accepted 2026-06-12) |
| `[[base-slice-0]]` | Base Slice 0 — the control-plane proof |
| `[[the-drift]]` | The Drift — two systems on one substrate (diagnosed 2026-06-05) |
| `[[the-reunification]]` | The Reunification Workstream — "one civilization, one business" (opened 2026-06-05) |

### Investigation — the surveyed agent-tooling landscape (15)

The external tools, frameworks, and prior research the 2026-05-13 landscape
investigation evaluated — compiled from the first-party survey checkpoints and
Open Brain, **not** from `raw/investigations/*` (still empty, Phase 2). Each was
admitted only as a reference / optional adapter / pattern, never as a control
role (v3.9 Decision 15).

| Article | Entity |
|---|---|
| `[[agent-governance-toolkit]]` | Agent Governance Toolkit — `PolicyEngineAdapter` candidate (Microsoft) |
| `[[gstack]]` | gStack — software-factory workflow/skill pattern (Garry Tan) |
| `[[paperclip]]` | Paperclip — org / budget / approval UX pattern only |
| `[[symphony]]` | Symphony — trials / proof-of-work packaging pattern |
| `[[multica]]` | Multica — managed-agent / teammate-board UX pattern |
| `[[hermes-agent]]` | Hermes Agent — governed self-evolution optimizer pattern (deferred) |
| `[[openclaw]]` | OpenClaw — deferred gateway/session adapter & UX candidate |
| `[[pageindex]]` | PageIndex — vectorless `DocumentEvidenceRetriever` (augment, not replace) |
| `[[mempalace]]` | MemPalace — advisory memory candidate (no truth authority) |
| `[[ob1]]` | OB1 (Open Brain) — optional cognitive-planning pattern, advisory only |
| `[[miro-stack]]` | The Miro Stack — MiroThinker / MiroFlow, deferred research/eval references |
| `[[solo-orchestrator]]` | Solo Orchestrator — single-orchestrator agent-execution reference |
| `[[graphify]]` | Graphify — graph-construction reference |
| `[[claw-code]]` | claw-code — agent-execution reference |
| `[[bitsandpieces]]` | bitsandpieces — landscape reference |

### Concept — recurring ideas, lenses, and proposals (12)

Cross-cutting philosophical and architectural concepts that recur across the arc
without being a single standing component — including the Searles thirteen-graphs
product horizon and the node's-eye readings of the framework.

| Article | Entity |
|---|---|
| `[[thirteen-graphs]]` | Thirteen Graphs, One Infrastructure — one event graph, thirteen lenses |
| `[[the-market-graph]]` | The Market Graph — Layer 2, the exchange lens |
| `[[the-social-graph]]` | The Social Graph — Layer 3, the relationship-and-governance lens |
| `[[the-moral-ledger]]` | The Moral Ledger — the event graph reread as ethics at scale |
| `[[the-four-strategies]]` | The Four Strategies — the cognitive quartet (Agentic / Communal / Structural / Emergent) |
| `[[second-derivation-convergence]]` | The Second Derivation — primitives-up meets physics-up |
| `[[three-evaluative-axes]]` | Three Independent Evaluative Axes — how the framework is judged |
| `[[the-cult-test]]` | The Cult Test — the framework's self-falsifiability defences |
| `[[higher-order-operations]]` | Higher-Order Operations — operations on the cognitive grammar itself |
| `[[crash-recovery-as-ethics]]` | Crash Recovery as Ethics — integrity-under-failure as a moral property |
| `[[node-phenomenology]]` | What It's Like to Be a Node — the inside-view of an event-graph node |
| `[[religion-as-paths-from-being]]` | Six Paths from Being — religion in primitive terms |

---

## Deferred to later runs (not-yet-compiled)

Stated so the gaps are legible, per `DESIGN.md` and `PROVENANCE.md`. None of these
has an article yet; do not read their absence as absence from the project.

- **The full corpus sweep.** Per `DESIGN.md`, the substrate is meant to compile
  from ~8,783 markdown files across ~73 repos + ~1,175 Open Brain thoughts.
  Run-2 covered the arc spine, the Searles philosophy, the architecture entities,
  and the 2026-05-13 landscape survey — not the whole corpus.
- **Two `raw/` source tiers remain unmirrored** (`PROVENANCE.md`): `open_brain`
  (`raw/open-brain/` is empty but for `.gitkeep` — Open Brain was queried live,
  not dumped to disk) and `upstream_context` (`raw/investigations/<project>/` is
  empty by design, Phase 2). The `investigation`-tier articles above exist
  *despite* this — they were compiled from the first-party survey, not from a
  mirror of each upstream project's own docs. A future run that mirrors
  `raw/investigations/*` can deepen them with upstream-sourced detail (cited as
  context, never re-published).
- **Granular forward-referenced entities.** Article bodies link several entities
  that are real in the sources but have no article yet — e.g. the standalone
  **44-primitives** and **200-primitives** set articles (distinct from the
  compiled `[[the-primitives]]` ladder and `[[fourteen-layers]]` stack), the
  remaining individual graphs of `[[thirteen-graphs]]` (justice, ethics,
  knowledge, identity, relationship, community, governance, …), and runtime
  objects named in passing (`authority-request`, `execution-receipt`,
  `roles-catalog`, `bounded-runtime`, `slice-1-first-reunified-order`). These
  are left as legitimate forward-refs, not aliases.
- **The `mind-zero` / `mind-zero-five` repo entity and the `eventgraph` repo.**
  Referenced as the upstream Go system and repo, deliberately **not** merged into
  `[[event-graph]]` or `[[the-mind-loop]]` because the repo-identity tension (see
  the freshness header) is unresolved.

---

*Compiled by Run-2 on 2026-06-13. Fail-legible: gaps are marked TBD, conflicts
are stated rather than resolved, and every `[[...]]` link above resolves to a real
file in `wiki/`. Re-run the compiler to refresh `last_compiled` and fold in the
deferred entities.*
