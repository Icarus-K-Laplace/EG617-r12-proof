# EG617 r=12 — research index

This repository is the canonical record of reconstructed mathematical results, proof status, dependencies, and reproducible certificates for the EG617 r=12 project. Agent prompts are intentionally kept outside the repository.

## Canonical human-readable status

- `README.md` — project warning and current research frontier
- `CANONICAL_STATE.md` — current mathematical state
- `PROOF_DAG.md` — dependency graph
- `ASSET_LEDGER.md` — theorem/status registry
- `OPEN_FRONTIERS.md` — active mathematical frontiers
- `STATUS_POLICY.md` — proof-status semantics

## Machine-readable status

- `machine/CANONICAL_STATE.json` — current global state and exact frontier constraints
- `machine/THEOREM_REGISTRY.json` — theorem/result registry with status and source files
- `machine/OPEN_FRONTIERS.json` — active research objects and next exact targets

These JSON files are intended for other research agents, scripts, and automated audits. They contain results and state only, not working prompts.

## Front-end

- `front_end/FRONTEND_BRIDGE_THEOREM.md` — proved `K145 -> R(4,49) OR T61` dichotomy
- `front_end/FRONTEND_DEPENDENCY_DAG.md` — clean front-end dependency DAG
- `front_end/ASSUMPTION_LEDGER.md` — exact hypotheses and status
- `front_end/RECURRENCE_PROOF.md` — mathematical recurrence proof
- `front_end/BRIDGE_STATE.md` — bridge architecture and scope
- `front_end/T61_NEW_LEMMAS.md` — `alpha(R)=5`, anchor defect `z=0`, and early T61 tightening
- `front_end/R448_FLOOR310.md` — generic `R(4,48) >= 310`
- `front_end/T61_H12_CLOSURE.md` — complete minimum-degree-12 T61 closure
- `front_end/T61_H13_LOW_LAYER.md` — canonical h13 layer ledger
- `front_end/E398_Q23_SHELL.md` — exact q23 shell classification and E398 closure
- `front_end/E399_Q24_SHELL.md` — exact q24 shell cells and E399 closure
- `front_end/E400_Q25_SHELL.md` — uniform q25 shell theorem and E400 closure
- `front_end/S30_S31.md` — exact scope of local S30/S31 assets
- `front_end/S30_REMAINING_BRANCHES.md` — remaining labelled S30 scalar cases

Current front-end terminal:

`T61: delta=13, 401<=E<=408`.

Current next mathematical target: E401, including q26 cells `(26,25,1),(26,24,2),(26,23,3),(26,22,4)` and q25 extension `(25,21,4)`, preferably through a parameterized `q=22+r` stability theorem.

## Backend

- `backend/CORE211.md` — clean 35-core lower bound
- `backend/Q28_Q29_REPIVOT.md` — q28/q29 repivot theorems with corrected scope
- `backend/E332_Q30_211.md` — canonical E332 frontier
- `backend/E332_D10_CLOSURE_D3_NORMAL_FORM.md` — d10 closure and the equality-row reductions used in the E332 analysis

Current backend state:

- E329, E330, E331 are closed;
- E332 reduces to q30 over a 211-edge core;
- all undecorated missing degrees 3 through 10 are now eliminated;
- any remaining E332 shell has undecorated missing degree in `{0,1,2,11,12}`, at most two degree-11/12 regular vertices, and total decoration `G in {4,5,6,7,8}`;
- the exact G=4 support count is `(h,k,l)=(2,4,7)`;
- E333–E340 remain open as the high-layer stability problem.

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

The V1 certificate is retained as historical evidence. Stronger modern seeds must generate a new certificate version rather than overwrite V1.

## Historical reconstruction

- `history/CANONICAL_TIMELINE.md` — phase-by-phase progress
- `history/LEGACY_ASSET_MAP.md` — integration/source bundle provenance
- `history/RETRACTIONS_AND_SCOPE_CORRECTIONS.md` — unsafe old claims and corrected theorem scopes

## Raw source bundles outside GitHub

The source archive includes Integration 1/2 PDFs, the large A–J work archive, and audit ZIPs. These large binaries are not duplicated wholesale here. Their accepted mathematical content, proof dependencies, and small replayable certificates are reconstructed in this repository.

## Current certification condition

The full theorem remains OPEN until both conditions hold:

1. the T61 h13 window E401–E408 is excluded or always yields a legal induced R(4,49);
2. E332 and E333–E340 are eliminated for every legal R(4,49) residual.
