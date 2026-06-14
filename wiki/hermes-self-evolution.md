---
entity: Hermes Self-Evolution
aliases: [hermes-agent-self-evolution, hermes evolution, DSPy GEPA evolution, hermes optimizer]
tier: investigation
status: compiled
last_compiled: "2026-06-14"
sources:
  - gh:transpara-ai/hermes-agent-self-evolution README.md  # root README, fetched 2026-06-14
  - gh:transpara-ai/hermes-agent-self-evolution PLAN.md    # architecture and phased plan, fetched 2026-06-14
confidence:
  sources: primary
  claims: grounded
---

# Hermes self-evolution

A forked evolutionary optimization pipeline that applies **DSPy + GEPA** (Genetic-Pareto Prompt Evolution) to automatically improve [[hermes-agent]]'s skills, tool descriptions, system prompt sections, and agent code — producing measurably better variants through reflective evolutionary search. Forked into `transpara-ai/hermes-agent-self-evolution` as a reference artifact; **not integrated into any active transpara-ai system** as of 2026-06-14.

## What it is

`hermes-agent-self-evolution` is a standalone optimization pipeline that operates *on* [[hermes-agent]], not inside it. It reads execution traces, proposes targeted textual mutations, evaluates variants against test tasks, and selects winners under Pareto constraints. It was originally published as `NousResearch/hermes-agent-self-evolution`; the transpara-ai fork captures it as a reference for future [[capability-evolution]] work.

The pipeline runs entirely via API calls — no GPU training, no weight updates. All three engines evolve and select text (skill files, tool descriptions, system prompt sections, code files), not model weights. The DSPy `BootstrapFinetune` component (the one that does train weights) is explicitly excluded from the plan.

## Engines

Three engines are unified under one workflow:

| Engine | Targets | License | Status in plan |
|--------|---------|---------|----------------|
| **DSPy + GEPA** | Skill files, tool descriptions, system prompt sections | MIT | Primary — fully integrated |
| **DSPy MIPROv2** | Few-shot examples, instruction text | MIT | Fallback optimizer |
| **Darwinian Evolver** (imbue-ai) | Code files, algorithms, tool implementations | AGPL v3 | External CLI only — Phase 4 |

GEPA (ICLR 2026 Oral) is the leading engine. It integrates into DSPy, reads execution traces to understand *why* things fail rather than merely that they failed, and converges with as few as three examples. The README claims it outperforms both RL and prior DSPy optimizers on prompt-optimization benchmarks.

## What it optimizes (phased plan)

The PLAN.md describes five ordered phases, with only Phase 1 implemented at the time of the last commit (2026-03-29):

| Phase | Target | Engine | Impl status |
|-------|--------|--------|-------------|
| 1 | Skill files (SKILL.md) | DSPy + GEPA | Implemented |
| 2 | Tool descriptions | DSPy + GEPA | Planned |
| 3 | System prompt sections | DSPy + GEPA | Planned |
| 4 | Tool implementation code | Darwinian Evolver | Planned |
| 5 | Continuous improvement loop | Automated pipeline | Planned |

Skill files (Phase 1) are the lowest-risk entry point: pure text, directly measurable, easily mutated. The evaluation harness wraps a skill as a DSPy module, runs it against a test-task dataset via `batch_runner`, and ranks candidate mutations under the five guardrails below.

## Guardrails

Every evolved variant must pass all five gates before a PR is opened:

1. Full test suite — `pytest tests/ -q` must pass 100%
2. Size limits — skills ≤ 15 KB, tool descriptions ≤ 500 chars
3. Caching compatibility — no mid-conversation changes
4. Semantic preservation — must not drift from original purpose
5. PR review — all changes go through human review; no direct commits

The pipeline opens a PR against hermes-agent; it never writes directly to the branch.

## Evaluation data strategy

Two modes are supported:

- `--eval-source synthetic` — dataset generated from the skill/prompt under test; requires no prior history
- `--eval-source sessiondb` — real session history imported from Claude Code, Copilot, or Hermes; produces higher-signal evals

A session importer was added in the final commit (2026-03-29, commit `feat: add Hermes session importer`), confirming the `sessiondb` path is implemented for Phase 1.

## Estimated cost

README quotes **~$2–10 per optimization run** at Phase 1 scope (skill evolution, 10 iterations). Costs scale with phase depth and iteration count.

## Relationship to transpara-ai

The fork lives at `transpara-ai/hermes-agent-self-evolution`. It is referenced but not integrated:

> ⚠ **Deferred per v3.9 Decision 15.** This system was evaluated during the v3.9 planning cycle and deferred — it is a reference artifact, not a dependency or scheduled integration. Any activation requires a new architectural decision. The AGPL v3 license on the Darwinian Evolver component (Phase 4) is a dependency constraint that must be reviewed before integration into any transpara-ai product.

The broader [[capability-evolution]] article covers the institutional question of how and when the arc adopts automated self-improvement loops.

## Sources & provenance

- `transpara-ai/hermes-agent-self-evolution` README.md — fetched via GitHub API 2026-06-14; repo description, engine table, guardrails, quick-start commands, cost estimate
- `transpara-ai/hermes-agent-self-evolution` PLAN.md — fetched via GitHub API 2026-06-14 (first ~3 000 chars); vision, engine comparison table, five-phase plan with tier descriptions, GEPA characterization, BootstrapFinetune exclusion, evaluation data strategy
- Commit log — fetched via GitHub API 2026-06-14; last commit 2026-03-29; rebrand commit 2026-03-09 (`refactor: rebrand to Hermes Agent Self-Evolution`)

**Conflicts / thin spots:** The PLAN.md excerpt covered through Phase 3 detail; Phases 4–5 descriptions are from the README table only. The claim that GEPA "outperforms both RL and previous DSPy optimizers" is sourced from the README (asserted, not independently verified here). The "ICLR 2026 Oral" claim for GEPA is from the README. License status of NousResearch upstream is not confirmed independently.
