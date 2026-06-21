# Civilization Arc — Date Ownership & Backfill Feasibility (scoping)

**Date:** 2026-06-21 · **Branch:** `claude/elegant-jang-3373f3` · **Status:** scoping only, no code changed
**Question (Michael):** "once 2,3,4,5 are done we'll revisit who precisely OWNS the dates" — and whether
that unblocks #1 (dates on tooltip/detail), #6 (date-based x-axis + duration-proportional widths), and
real Actor attribution.

---

## TL;DR / Recommendation

- **Real dates ARE recoverable** for the items that cite a PR/issue — **proven**, not theoretical. The arc
  items are effectively a foreign-key table; `gh api repos/transpara-ai/<repo>/issues/<n>` resolves each
  cited ref to a real `merged_at` (and they corroborate the labels — docs#138 *is* "revise Gate K pre-live
  closeout").
- **Coverage is partial by design.** Of 116 items: **25 are datable now** (cite a ref), **70 have no
  datable event** (reconstructed narrative / design-principle beats), **21 are future/planned** (haven't
  happened — no date possible).
- **Who owns the dates:** the **source-of-truth repos' GitHub PR/issue history** — overwhelmingly
  `transpara-ai/docs` (governance/gates), plus `work`/`hive`/`site`/`eventgraph` for implementation.
  `civilization-wiki` owns only the *reconstructed pre-history*, which is "not commit-derived" by its own
  honesty note and therefore **ownerless for dating**.
- **Do:** #1 (tooltip/detail dates) for the 25 datable items — cheap, honest, graceful blanks elsewhere
  (the `item.date` hook already renders this way). ~½ day.
- **Don't:** #6 (date x-axis / duration-proportional widths) — too sparse; a date axis with ~¾ of dots
  unplaceable forces fabricated positions, contradicting the accuracy-first redesign. The ordinal-`seq`
  axis is the *honest* representation. (Optional later: a "dated-only" sparse lens.)
- **Actor:** low value. GitHub author/merger collapses to `MichaelSaucier` (single-human-operator model);
  real agent attribution lives only in `[codex]`/`[claude]` title prefixes (fragile/partial). Not worth a
  primary feature; it would *misrepresent* the documented single-authority operating model.
- **Air-gap constraint:** dates must be **baked into the data file at rest** (one-time human-run deref
  script), **not** fetched during `build_site.py` (runs air-gapped on nucbuntu; network-at-build breaks the
  air gap and makes builds nondeterministic).

---

## Evidence

### Data model (elegant-jang `compile/assets/civilizationArcData.js`, 116 items)

- Per-item fields: `id, code, type, label, status, blocked, blocked_reason, provenance, seq, repo[],
  sprint, gate, goal, deps[], href, note`. **No `date` field.** `href` points to *wiki article pages*
  (`the-20-primitives.html`), **not** to PRs — it is not a date source.
- A tooltip hook is already reserved and renders gracefully when absent:
  `civilizationArcNav.js:314 → if (item.date) … "date · " + item.date  // reserved for date-backfill`.

### Coverage audit (programmatic load of the data; `/tmp/arc_date_audit.js`)

| Population | Count | Datable? |
|---|---:|---|
| **Total items** | 116 | — |
| Historical (`done`/`active`) | 95 | a date *can* exist |
| Future (`planned`/`future`) | 21 | **no** — hasn't happened |
| Historical **with** deref-able `#ref` | **25** | **yes, now** (Tier 1) |
| Historical **without** a `#ref` | 70 | mostly no (see tiers) |
| provenance `derived` / `reconstructed` | 17 / 99 | — |

### Recoverability — proven by dereference (read-only `gh`, all transpara-ai)

| Ref | Kind | Real date (`closed/merged_at`) | Title corroborates label |
|---|---|---|---|
| eventgraph#34 | PR | 2026-05-14 | Stage 5 — TraceCompletenessGate … |
| work#41 | PR | 2026-06-02 | Implement Gate I capability monitoring fixture |
| hive#148 | PR | 2026-06-10 | feat(loop): … keepalive reviewer (closes F8) |
| docs#127 | PR | 2026-06-12 | accept the v4.0 seed doctrine | (matches inline prose `(2026-06-12)`) |
| docs#132 | PR | 2026-06-15 | record Event-1 Gate K authority grant |
| docs#138 | PR | 2026-06-17 | **revise Gate K pre-live closeout** |
| docs#142 | PR | 2026-06-18 | Accept v4.0 canonical docs baseline |

The recoverable timeline spans **~5 weeks (mid-May → mid-June 2026)**. Everything before is the
reconstructed Feb-genesis pre-history with no commit dates.

---

## Who owns the dates

| Owner | Items | Date source | Quality |
|---|---|---|---|
| `transpara-ai/docs` PR/issue history | 62 docs-owned (governance/gates/events) | `merged_at` of the cited PR | real, precise (for the 25 that cite a ref) |
| `work`/`hive`/`site`/`eventgraph` history | implementation items | `merged_at` of the cited PR | real, precise |
| `civilization-wiki` (reconstructed narrative) | origin story + design-principle beats | **none** — "not commit-derived" by its own note | n/a (undatable by design) |

---

## Feasibility per deferred feature

### #1 — dates on tooltip / detail panel  →  **DO (Tier 1)**
- 25 items get a real, sourced date immediately. Hook already renders; undated items simply show no date
  line (already-wired graceful fallback). Low risk, honest, partial-by-design.

### #6 — date-based x-axis + duration-proportional widths  →  **DON'T**
- Even Tier 1 + Tier 2 (below) dates well under half the items; ~¾ have no real position. A date axis then
  either drops most of the chart or fabricates positions — the exact "decorative axis that encodes nothing"
  failure the Direction-C rebuild was meant to kill. Ordinal-`seq` is the accurate choice.
- *Optional future:* a separate "dated-only" sparse timeline lens showing just the 25 real events.

### Actor attribution  →  **SKIP (low value)**
- PR `author`/`merged_by` ≈ `MichaelSaucier` for nearly all (single-human-operator model). Agent-level
  actor exists only as `[codex]`/`[claude]` title prefixes — fragile, partial, and attributing distinct
  "actors" would misrepresent the documented single-authority posture.

---

## Datability tiers (the 116, precisely)

- **Tier 1 — date now, by deref (25):** items citing a PR/issue. One script. Reliable.
- **Tier 2 — date with PR-hunting research (~30–40):** real-but-uncited gates (Gate-A..D, security gates,
  several `G-x.x` docs gates) + worklist `C*/N*` items. Moderate–high manual effort, variable reliability.
- **Tier 3 — undatable by design:** reconstructed origin-story + design-principle beats (MEM "memory
  remains advisory", PROMPT, RITUAL, D15, RO, LENS, …) + all 21 future/planned. No real date exists.

---

## Concrete next step IF greenlit (Tier-1 only)

1. Lift the cited ref into a structured field on the 25 items (e.g. `ref: "docs#138"`), out of prose.
2. One-time **human-run** deref script (`gh api … merged_at`) writes `date` (ISO) into the data file as a
   **committed value** — no network at build time.
3. Render: tooltip hook already exists; add a detail-panel "date" line.
4. Tests: data-integrity guard — refs well-formed, dates ISO, **date ≤ today**, dated ⇒ historical status
   (fail-closed allowlist style).
5. `npm run verify` + build.

**Effort:** ~½ day. **Risk:** low (additive; graceful fallback already wired). **Reversible:** yes.

---

## What I did NOT do / caveats

- No arc code changed; the fragile 9-file uncommitted diff on this branch is untouched. This note is a new,
  **untracked** file — keep, commit, or `rm` at will.
- Did not exhaustively map every Tier-2 ref to a PR (that *is* the moderate-effort work, deferred to a
  greenlight).
- `gh` deref reflects state as queried 2026-06-21; baked dates would be a point-in-time snapshot,
  refreshable by re-running the script.
