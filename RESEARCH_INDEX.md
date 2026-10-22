# EG617 r=12 — research index

This repository is the canonical record of reconstructed mathematical results, proof status, dependencies, and reproducible certificates for the EG617 r=12 project. Agent prompts are intentionally kept outside the repository.

## Canonical human-readable status

- `README.md` — project warning and current research frontier
- `CANONICAL_STATE.md` — current mathematical state
- `PROOF_DAG.md` — dependency graph
- `ASSET_LEDGER.md` — theorem/status registry
- `OPEN_FRONTIERS.md` — active mathematical frontiers
- `STATUS_POLICY.md` — proof-status semantics
- `PROOF_COMPLETENESS_AUDIT.md` — repository self-containment audit

## Machine-readable status

- `machine/CANONICAL_STATE.json`
- `machine/THEOREM_REGISTRY.json`
- `machine/OPEN_FRONTIERS.json`

These JSON files contain results/state only, never working prompts.

## Front-end

- `front_end/FRONTEND_BRIDGE_THEOREM.md` — proved `K145 -> R(4,49) OR T61` dichotomy
- `front_end/FRONTEND_DEPENDENCY_DAG.md`
- `front_end/ASSUMPTION_LEDGER.md`
- `front_end/RECURRENCE_PROOF.md`
- `front_end/BRIDGE_STATE.md`
- `front_end/T61_NEW_LEMMAS.md`
- `front_end/R448_FLOOR310.md`
- `front_end/T61_H12_CLOSURE.md`
- `front_end/T61_H13_LOW_LAYER.md` — canonical h13 layer ledger
- `front_end/E398_Q23_SHELL.md` — q23 theorem / E398
- `front_end/E399_Q24_SHELL.md` — q24 theorem / E399
- `front_end/E400_Q25_SHELL.md` — uniform q25 theorem / E400
- `front_end/S30_S31.md`
- `front_end/S30_REMAINING_BRANCHES.md`

Current front-end terminal:

`T61: delta=13, 401<=E<=408`.

Next target: E401, including q26 cells `(26,25,1),(26,24,2),(26,23,3),(26,22,4)` and q25 extension `(25,21,4)`, preferably by a parameterized `q=22+r` stability theorem.

## Backend

- `backend/CORE211.md` — canonical theorem statement/equality structure
- `consolidation/INTEGRATED1_CORE211_AUDIT.md` — recovered 210-edge AES contradiction and remaining minimum-degree provenance gap
- `backend/Q28_Q29_REPIVOT.md` — compact repivot interface
- `backend/Q29_GOOD_REPIVOT_FULL_PROOF.md` — reconstructed three-branch standalone q29 proof
- `backend/E329_E332_CLOSURE.md` — standalone E329/E330/E331 closures and E332 q30+211 reduction
- `backend/E332_Q30_211.md`
- `backend/E332_D10_CLOSURE_D3_NORMAL_FORM.md`

Current backend state:

- E329, E330, E331 closed;
- E332 reduces to q30 over a 211-edge core;
- undecorated missing degrees 3 through10 eliminated;
- remaining E332 undecorated degrees lie in `{0,1,2,11,12}` with total decoration `G in {4,5,6,7,8}`;
- exact G=4 support count `(h,k,l)=(2,4,7)`;
- E333–E340 remain open.

## Audits / consolidation

- `audits/2026-10-21_FRONTIER_AUDIT.md`
- `audits/2026-10-21_Q29_SCOPE_CORRECTION.md`
- `consolidation/Q27_ANALYTIC_EQUALITY_CLOSURE.md`
- `consolidation/I_Q29_RECOVERY_AUDIT.md`
- `consolidation/INTEGRATED1_CORE211_AUDIT.md`

## Certified computation

`certificates/frontend_line_a_v1/` contains the immutable contextual recurrence replay and local S30 arithmetic assets. New stronger seeds must generate new certificate versions rather than overwrite V1.

## Historical reconstruction

- `history/CANONICAL_TIMELINE.md`
- `history/LEGACY_ASSET_MAP.md`
- `history/RETRACTIONS_AND_SCOPE_CORRECTIONS.md`
- `history/INTEGRATED1_SOURCE_MAP.md` — source map from the complete 636-page Integration 1 bundle to current proofs
- A--J source/audit maps under `history/` and `consolidation/`

## Raw source bundles outside GitHub

Integration 1/2 PDFs, A--J PDFs and large audit ZIPs are retained as provenance outside GitHub; accepted mathematical content is reconstructed into human/machine-readable proof assets here.

## Current certification condition

The full theorem remains OPEN until:

1. T61 h13 E401–E408 is excluded or always yields a legal induced R(4,49);
2. E332 and E333–E340 are eliminated for every legal R(4,49) residual.
