# EG617 r=12 — research index

This is the top-level map of all currently reconstructed progress.

## Canonical status

- `README.md` — project warning and three-line split
- `CANONICAL_STATE.md` — current mathematical frontier
- `PROOF_DAG.md` — dependency graph
- `ASSET_LEDGER.md` — theorem/status table
- `OPEN_FRONTIERS.md` — active research tasks
- `STATUS_POLICY.md` — proof-status semantics
- `TEAM_SPLIT.md` — Astra A / Astra B / central line ownership

## Front-end

- `front_end/FRONTEND_BRIDGE_THEOREM.md` — proved K145 -> R449 OR T61 dichotomy
- `front_end/FRONTEND_DEPENDENCY_DAG.md` — clean front-end DAG
- `front_end/ASSUMPTION_LEDGER.md` — exact hypotheses and status
- `front_end/RECURRENCE_PROOF.md` — mathematical recurrence proof
- `front_end/BRIDGE_STATE.md` — architecture notes
- `front_end/S30_S31.md` — local S30/S31 scope
- `front_end/S30_REMAINING_BRANCHES.md` — labelled S30 residual scalar cases
- `front_end/T61_NEW_LEMMAS.md` — z=0, R448>=309, h12 equality classification and row overlap

## Backend

- `backend/CORE211.md`
- `backend/Q28_Q29_REPIVOT.md`
- `backend/E332_Q30_211.md`

The backend canonical state currently excludes E329–E331, reduces E332 to q30+211, and leaves E333–E340 to the high-layer line.

## Audits

- `audits/2026-10-21_FRONTIER_AUDIT.md`
- `audits/2026-10-21_Q29_SCOPE_CORRECTION.md`

## Certified computation

Directory `certificates/frontend_line_a_v1/` contains:

- recurrence implementations A/B;
- verifier;
- verification receipt;
- exact 144-row outer stop table;
- exact 192-entry S30 scalar table.

The V1 certificate remains immutable historical evidence. Any recurrence using modern seed upgrades 211/309 must be emitted as a separate V2 certificate.

## Agent prompts

- `prompts/ASTRA_A_FRONTEND.md` — current T61-only prompt
- `prompts/ASTRA_B_HIGH_LAYER.md` — E333–E340 high-layer prompt

## Historical reconstruction

- `history/CANONICAL_TIMELINE.md` — phase-by-phase progress
- `history/LEGACY_ASSET_MAP.md` — integration/source bundle provenance
- `history/RETRACTIONS_AND_SCOPE_CORRECTIONS.md` — unsafe old claims and corrected theorem scopes

## Raw source bundles supplied outside GitHub

The conversation/source archive includes:

- Integration 1 PDFs (636 pages)
- Integration 2 PDFs (287 pages)
- large A–J/raw work archive
- 2026-10-21 frontier audit ZIP
- 2026-10-21 Line A V1 ZIP

These large binary sources are not duplicated in this text-oriented proof repository. Their mathematically accepted content is reconstructed above.

## Current completion interpretation

Structural understanding is substantially ahead of final certification. The full theorem remains OPEN until:

1. T61 is excluded or always yields a legal R449;
2. E332 and E333–E340 are all eliminated for every legal R449 residual.
