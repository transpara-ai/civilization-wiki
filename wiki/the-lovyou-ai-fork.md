---
entity: The lovyou.ai Fork
aliases: [the lovyou-ai fork, lovyou.ai fork, the fork, lovyou-ai → transpara-ai]
tier: arc
status: compiled
last_compiled: 2026-06-13
sources:
  - raw/searles/all-posts-1.md  # post 2, "From 44 to 200", 2026-02-28 [Searles-P2] — hive0/LovYou origin: ~70-agent run, 44 primitives, 200/14-layers
  - Open Brain  # fork chronology and spawn-lifecycle: lovyou-ai-hive/work/agent/eventgraph/site captured thoughts (earliest 2026-03-03; spawn-lifecycle 2026-04-08/09)
  - https://github.com/transpara-ai  # the fork org (repos: agent, eventgraph, hive, site, work + docs) — cited as the downstream we own
  - https://github.com/lovyou-ai  # the upstream project — cited as CONTEXT ONLY per org rules; never re-published, never a PR/push target
confidence:
  fork_date_2026_03_30: asserted by task framing — NOT corroborated by an Open Brain capture or a GitHub record read this run. The earliest Open Brain thoughts that name the forked repos are 2026-04-08/09 (`lovyou-ai-hive`, `lovyou-ai/work`, `lovyou-ai/agent`); Open Brain's earliest capture of any kind is 2026-03-03. Treated as reconstructed, not proven. See "When the fork happened."
  feb_2026_first_fork_and_build: reconstructed — explicitly NOT in the org GitHub history or Open Brain read this run, both of which begin after the fact. Labelled fail-legibly throughout.
  hive0_origin: single-author testimony (Searles post 2), no run log or repro read this run; the ~70-agent / two-day / 44-primitive derivation is asserted, not independently proven (the source corpus itself classes it "research input").
  upstream_provenance: high for the *fact* of a lovyou-ai → transpara-ai fork relationship (multiple Open Brain thoughts name `upstream = lovyou-ai/*`, push-disabled); the per-repo first-commit dates are not established here.
---

# The lovyou.ai Fork

**The point where an external project became internal infrastructure.** "The lovyou.ai fork" is the act and the result of forking Matt Searles' open-source LovYou / mind-zero work out of the `lovyou-ai` GitHub org and into the `transpara-ai` org, where it became the codebase the [[hive-governance]] and the broader [[dark-factory]] arc are built on. The downstream set named in the org's [[dark-factory]] topic is **agent, eventgraph, hive, site, work** (plus a **docs** repo) — six repos, five of which carry the runtime; the prompt-supplied fork date for those is **2026-03-30**, with the caveats below.

This article is the umbrella for that relationship: where the code came from, what it became under our ownership, and — non-negotiably — which parts of that story are reconstructed rather than recorded. The upstream project (`lovyou-ai`) is cited here **as context only**. Per organization rules it is never re-published, never pushed to, and never a PR target; `upstream` in this setup is the public project we read from, `origin` is the `transpara-ai` fork we own.

## Where it came from: hive0 and LovYou

The upstream's own origin story is told in Searles' second post, *"From 44 to 200"* (**2026-02-28**, [Searles-P2]). It frames LovYou as the project that grew out of the late-night failure-tracing question behind [[the-20-primitives]]: those 20 primitives "became a hive of seventy autonomous agents, and … that hive — left running accidentally for two days — derived 44 foundation primitives on its own." That ~70-agent run is the object the wider corpus calls **hive0**; it is the seed the current [[hive-governance]] descends from in lineage, if not in literal code.

The post then describes feeding those 44 primitives to Claude Opus as "Layer 0" and asking, layer by layer, "what's the gap?" — yielding "156 additional primitives across 13 new layers," i.e. the **200 primitives across 14 layers** ([[the-20-primitives]] → 44 → 200). The 44 are grouped into eleven clusters (Foundation, Causality, Identity, Expectations, Trust, Confidence, Instrumentation, Query, Integrity, Deception, Health), and the post is explicit that "no human designed these."

> ⚠ **Fail-legible note (hive0 is testimony, not proof).** The ~70-agent, two-day, self-derived-44 claim is **single-author testimony** with no run log or reproduction read this run. The first-party Dark Factory synthesis classes hive0 and the 44/200 ladder as **"research input, not independently proven,"** and Searles' own later guardrail ([[the-cult-test]]) concedes the run "could be repeated, might produce different results." Carried here because the source carries it, and labelled as such. The detail of the 44 and the 14 layers belongs to [[primitive-basis]] / [[the-20-primitives]]; it is summarized here only to anchor *what was forked from*.

A second source-internal subtlety to keep straight: the upstream code Searles writes about is named **mind-zero-five** (`github.com/mattxo/mind-zero-five` in the post footers), while the repos the `transpara-ai` fork actually carries are named **eventgraph / hive / work / agent / site**. The sources do **not** assert these are the same codebase — see [[event-graph]] for the repo-identity conflict, which this article does not resolve.

## What it became: the transpara-ai fork

Under `transpara-ai` ownership the forked code is the substrate of the live [[hive-governance]] runtime. Open Brain's operational record (the durable part of this story) shows the fork repos wired together and exercised:

- **The repos are co-dependent via local `replace` directives.** The hive, eventgraph, agent, and work repos link through go.mod `replace ../<repo>` paths; because they are not co-built in CI, cross-repo type drift only surfaces on a local `go build`. A concrete instance: a 2026-04-17 build break where `eventgraph` tightened `SiteOpTranslatedContent.BusEventID` from `string` to a typed `EventID`, but the hive caller still unwrapped it via `.Value()`. This is also why a dependency repo must be pulled before building the one above it.
- **The runtime boots from chain replay and hosts the [[civic-roles|nine civic agents]].** A representative boot: the hive cold-started 9 static agents from chain replay and spawned 2 dynamic agents (task-curator, researcher), with the webhook on :8081 and work-server on :8080.
- **The growth loop runs on the fork.** The first dynamically-spawned agent in the hive's history — the **researcher**, 2026-04-08 — went through the full Spawner → Guardian → Allocator → runtime lifecycle, the first end-to-end proof of the SELF-EVOLVE invariant. See [[hive-governance]] and [[agent]] for the spawn machinery and the agent definition itself.
- **A site↔hive webhook bridge** was wired across `lovyou-ai-site` and `lovyou-ai-hive` (2026-04-08), translating site ops into eventgraph bus events — the first reactive coupling between the fork's web surface and its runtime.

Over April 2026 the fork was also progressively **rebranded** from `lovyou-ai` to `transpara-ai` in code: a mechanical rename across all 212 tracked files of `eventgraph` (Go module path, npm package, URLs) landed as `transpara-ai/eventgraph#8`, and `work` was renamed `lovyou-ai-work → work` in `transpara-ai/work#20`. Crucially, **the git remotes were not touched** by these renames — `upstream` still points at `lovyou-ai/*` per Michael's convention.

## When the fork happened

The prompt frames the fork of **agent, eventgraph, hive, site, work** out of `lovyou-ai` as occurring on **2026-03-30**. This article carries that date but must be honest about its evidentiary status.

> ⚠ **Fail-legible note (the 2026-03-30 fork date is reconstructed, not recorded).** No Open Brain capture read this run is dated 2026-03-30, and none records the act of forking five repos. Open Brain's **earliest capture of any kind is 2026-03-03** (confirmed by the 2026-06-13 export audit, which also corrects the tool's reported start date of "3/5/2026" as approximate). The earliest captured **spawn-lifecycle and repo-operational** thoughts that name the forked repos are **2026-04-08/09**, and they name them under their pre-rebrand identities — `lovyou-ai-hive`, `lovyou-ai/work`, `lovyou-ai/agent`, `lovyou-ai-site`. So the *fact* of a `lovyou-ai → transpara-ai` fork is well corroborated (the `upstream = lovyou-ai/*`, push-disabled convention appears across many thoughts); the specific **3/30 date is asserted by the task framing**, not independently verified here.

> ⚠ **Fail-legible note (the Feb-2026 first-fork-and-build is reconstructed).** Any account of an earlier February 2026 first fork and initial build sits **before both records available to this article**: it is not in the `transpara-ai` org GitHub history read this run, and it predates Open Brain (which begins 2026-03-03). It is **reconstruction, not documentation** — stated as such, with no claimed commit, PR, or capture behind it. What *is* grounded for February 2026 is upstream-side only: Searles' posts (including [Searles-P2]) are dated 2026-02-28 and describe hive0 and mind-zero-five as already running.

The net chronology, with confidence flagged:

| When | Event | Evidence status |
|---|---|---|
| 2026-02-28 | Upstream LovYou / mind-zero / hive0 described as live (Searles post 2) | Grounded (source post), but hive0 itself is testimony |
| Feb 2026 (claimed) | First fork-and-build of the upstream into our hands | **Reconstructed** — not in GitHub or Open Brain read this run |
| 2026-03-03 | Earliest Open Brain capture of any kind | Grounded (export audit) |
| 2026-03-30 (claimed) | Fork of agent/eventgraph/hive/site/work from `lovyou-ai` | **Asserted by task framing** — no 3/30 capture found |
| 2026-04-08/09 | Earliest captured spawn-lifecycle & repo work; repos named `lovyou-ai-*` | Grounded (Open Brain) |
| April 2026 | Mechanical rebrand `lovyou-ai → transpara-ai` in code (eventgraph#8, work#20); remotes untouched | Grounded (Open Brain) |

## Why it entered the arc

The fork is the hinge between **[[primitive-basis]]** (the philosophy and vocabulary we are permitted to consume) and the **[[dark-factory]]** machinery we actually build and run. The upstream supplied the accountability premise and the running shape — an append-only, hash-chained [[event-graph]]; a [[hive-governance]] of governed agents; a growth loop — and the fork is where that became code we own, can modify, can gate, and can hold to our own fail-closed standards. The downstream arc (reunification, the [[dark-factory]] production loop, the civic-role runs) all sit on top of this forked substrate.

What the fork is **not**: it is not a license to touch upstream. The corpus is consumed as motive and pattern only; `lovyou-ai` is read, never written. See [[primitive-basis]] for the boundary on how much of the upstream philosophy is load-bearing (only the 20 primitives are accepted as basis; 44/200/hive0/mind-zero are "research input" or "prior pattern"), and [[the-20-primitives]] for the seed itself.

## Sources & provenance

- `raw/searles/all-posts-1.md` — post 2, *"From 44 to 200"*, 2026-02-28 · [Searles-P2] · https://mattsearles2.substack.com/p/from-44-to-200 — the hive0/LovYou origin (the ~70-agent run, the self-derived 44, the 200-across-14-layers derivation). Read in full this run for the origin sections.
- **Open Brain** — fork chronology and spawn-lifecycle facts: the co-dependent `replace`-directive structure and the 2026-04-17 `eventgraph`/hive type-drift break; the 9-static-/2-dynamic-agent boot; the **researcher** as the first dynamic spawn (2026-04-08, first SELF-EVOLVE proof); the site↔hive webhook bridge (2026-04-08); the April-2026 rebrand PRs (`transpara-ai/eventgraph#8`, `transpara-ai/work#20`) with remotes left pointing at `lovyou-ai`; the `upstream = lovyou-ai/*`, push-disabled convention; and the export-audit fact that Open Brain's earliest capture is 2026-03-03.
- **https://github.com/transpara-ai** — the fork org we own (repos `agent`, `eventgraph`, `hive`, `site`, `work`, `docs`). Cited as the downstream; not browsed for first-commit dates this run.
- **https://github.com/lovyou-ai** — the upstream project. **Cited as context only.** Per org rules it is never re-published, pushed to, or PR'd against; it appears here solely to name where the code originated.

**What is contested or unproven, stated not resolved:** (1) the **2026-03-30 fork date** — asserted by the task framing, with no corroborating capture or GitHub record read this run; the earliest captured repo work is 2026-04-08/09. (2) The **February-2026 first-fork-and-build** — reconstructed, predating both the org GitHub history and Open Brain. (3) **hive0** (the ~70-agent two-day self-derivation of the 44) — single-author testimony, classed "research input, not independently proven" by the first-party synthesis. (4) **Repo identity** — the upstream Searles code is named `mind-zero-five`; the fork repos are `eventgraph`/`hive`/etc.; the sources do not assert they are the same codebase (carried to [[event-graph]]). `[[wikilinks]]` are forward references where targets are not yet compiled.
