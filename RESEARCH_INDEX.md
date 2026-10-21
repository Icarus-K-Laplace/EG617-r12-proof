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
- `front_end/FRONTEND_DEPENDENCY_DAG.md` — original clean front-end DAG
- `front_end/ASSUMPTION_LEDGER.md` — exact hypotheses and status
- `front_end/RECURRENCE_PROOF.md` — mathematical recurrence proof
- `front_end/BRIDGE_STATE.md` — architecture notes
- `front_end/T61_NEW_LEMMAS.md` — alpha=5, z=0 and early T61 tightening
- `front_end/R448_FLOOR310.md` — generic `R(4,48)>=310`
- `front_end/T61_H12_CLOSURE.md` — complete minimum-degree12 T61 closure
- `front_end/T61_H13_LOW_LAYER.md` — canonical h13 layer ledger
- `front_end/E398_Q23_SHELL.md` — exact q23 shell classification and E398 closure
- `front_end/E399_Q24_SHELL.md` — exact q24 shell cells and E399 closure
- `front_end/E400_Q25_SHELL.md` — uniform q25 shell theorem and E400 closure
- `front_end/S30_S31.md` — local S30/S31 scope
- `front_end/S30_REMAINING_BRANCHES.md` — labelled S30 residual scalar cases

Current front-end terminal:

`T61: delta=13, 401<=E<=408`.

Next target: q26 / E401 and a parameterized `q=22+r` shell-stability theorem.

## Backend

- `backend/CORE211.md`
- `backend/Q28_Q29_REPIVOT.md`
- `backend/E332_Q30_211.md`

The backend canonical state excludes E329–E331, reduces E332 to q30+211, and leaves E333–E340 to the high-layer line.

## Audits

- `audits/2026-10-21_FRONTIER_AUDIT.md`
- `audits/2026-10-21_Q29_SCOPE_CORRECTION.md`

## Certified computation

Directory `certificates/frontend_line_a_v1/` contains the immutable V1 recurrence replay:

- recurrence implementations A/B;
- verifier;
- verification receipt;
- exact outer-stop table;
- local S30 arithmetic assets.

The V1 certificate is retained as historical evidence. Any recurrence using stronger modern seeds such as CORE211 and R448>=310 must be emitted as a new certificate version rather than overwriting V1.

## Agent prompts

- `prompts/ASTRA_A_FRONTEND.md` — current V5 T61/E401 prompt
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

These large binary sources are **not** duplicated wholesale in this text-oriented proof repository. Their accepted mathematical content, status, proof dependencies, and replayable small certificates are reconstructed here.

## Current certification condition

The full theorem remains OPEN until:

1. T61 h13 E401–E408 is excluded or always yields a legal R449;
2. E332 and E333–E340 are all eliminated for every legal R449 residual.
