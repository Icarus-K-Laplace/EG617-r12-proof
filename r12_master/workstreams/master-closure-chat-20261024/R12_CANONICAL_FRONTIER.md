# R12 canonical frontier (evidence-first)

Audit date: 2026-10-24  
Working branch: `workstream/r12-master-closure-20261024`  
Base HEAD rechecked at start: `b98bea36e36a033100b8bf09a599897cb5afd7de`  
Global theorem status: **OPEN / NOT_CERTIFIED**.

This file assigns status from proof bodies, contracts, source-audit notes, and replay evidence. A filename or an upstream label `CLOSED` is not by itself evidence that all dependencies are certified.

## 1. Front-end T61 frontier

| Case / theorem | Current evidence-based status | Contract and evidence | Exact remaining gap |
|---|---|---|---|
| T61 h12 | `PROVED_RELATIVE_TO_CANONICAL_ASSETS` | Root `CANONICAL_STATE.md`, `PROOF_DAG.md`, and the canonical h12 closure assets. | Publication-grade dependency/citation consolidation remains part of the repository-wide proof-body audit; this is not the active mathematical frontier. |
| E397--E406 | `PROVED_RELATIVE_TO_CANONICAL_ASSETS` | `front_end/E401_E404_CANONICAL_CLOSURE.md`, `E405_FULL_CLOSURE_CANONICAL.md`, `E406_FULL_CLOSURE.md`, and their cited bridges. | Preserve their exact inherited contracts; do not reopen or treat them as unconditional outside those contracts. |
| E407, Q=27 | `PROVED` under the canonical E407/T61 contract | Recorded as closed in `OPEN_FRONTIERS.md`; earlier low-Q closure chain applies. | No new gap identified at this layer in the inspected assets. |
| E407, Q=31 | `SOURCE_REPORTED / CONDITIONAL` | `front_end/T61_H13_V11_SOURCE_AUDIT.md`: delivered V11 reports exclusion relative to retained lower-order seeds; package replay remains pending. | Independent replay/re-certification of the retained seeds and V11 package. |
| E407, Q=32 | `OPEN`; reduction is source-reported | `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md` reports five `rho=0` templates with a common regular K11, conditional on retained seeds. `front_end/E407_CELL_B_FULL_CLOSURE.md` excludes the separate sharp `|W|=23` Cell-B form only. | Prove that none of the five common-K11 templates can coexist with one and the same 284-edge core, or provide a certified legal completion (which would contradict the intended result). V12 replay remains pending. |
| E408, Q=27,28 | `PROVED` under the canonical E408/T61 contract | Recorded closed in `OPEN_FRONTIERS.md`. | No new gap identified at these layers in the inspected assets. |
| E408, Q=31 | `SOURCE_REPORTED / CONDITIONAL` | `front_end/T61_H13_V11_SOURCE_AUDIT.md`. | Independent replay/re-certification of retained seeds and package. |
| E408, Q=32 | `OPEN` | `OPEN_FRONTIERS.md`, V11/V12 source-audit notes. | Full shell/core and global-color compatibility; E407 Q32 eliminations do not transfer automatically. |
| E408, Q=33 | `OPEN`; several conditional necessary conditions proved | `front_end/E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md`; `E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.md`; `E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md`; `E408_Q33_D3_EXACT_BUDGET.md`. | Exclude all legal Q33 shell types, including the d3 four-case allowance budget, against the same 284-edge core and seven-block global near-Latin system. The exact budget is necessary, not contradictory by itself. |

### E407/E408 cross-cutting facts

- The `|W|=23` Cell-B normal form is excluded for both E407 and E408 by the proof bodies in `front_end/E407_CELL_B_FULL_CLOSURE.md` and `front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md`, relative to their stated extremal inputs.
- This does **not** close the remaining E407 Q32 templates or E408 Q32/Q33.
- E408 Q33's exact d3 identity `beta + X + G_B = 3` is conditional on the retained V11 Q33 interface. It does not establish nonexistence of any of its four `beta` cases.

## 2. Backend R(4,49) frontier

For a legal 49-point residual F and a degree-13 pivot, the exact identity is

`E = 91 + q + e(H)`,

with a 35-point core H. The three-anchor theorem is now stronger than CORE211: under `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`, three independent degree-12 anchors force `e(H)>=214`, hence `q<=E-305`. This is a conditional envelope: a survivor must first be shown to have the anchors.

| Layer | Evidence-based status | Contract / evidence | Exact remaining gap |
|---|---|---|---|
| E329--E332 | `PROVED_RELATIVE_TO_REGISTERED_DEPENDENCIES` | `backend/E329_E332_CLOSURE.md`, `backend/E332_FULL_CLOSURE.md`, CORE211 and the q27/q28/q29 assets. | Keep inherited CORE211/q27/topology assumptions explicit for a self-contained manuscript; do not reopen the layer casework. |
| E333 | `PROVED_RELATIVE_TO_CANONICAL_V4` | `backend/E333_V5_CANONICAL_CLOSURE.md`; the V5 arithmetic verifier is reported as independently rerun and its 12 endpoint inequalities passed. | The upstream legal-backend certification, all-pivot core-minimum-degree contract, and V4 forcing theorem remain retained dependencies; this is not a proof from the raw K145 assumption alone. |
| E334 | `SOURCE_REPORTED / CONDITIONAL` | `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md` reports E334 empty relative to retained backend/V7 forcing. The independent graph-theoretic K>=8 theorem is in `backend/GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`. | Independently replay/certify the V7/V8 forcing/extraction package that puts every E334 survivor into the three-anchor contract. Do not promote the source report itself to unconditional PROVED. |
| E335--E340 | `OPEN` | `backend/GLOBAL_FORCING_TO_MASTER_V3_SYNTHESIS.md`, `GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md`, and `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md` provide a strong conditional structural stack. | Exhaustive extraction from an arbitrary legal maximal-pivot shell to the master contract, plus the finite higher-slack residues described in the companion forcing document. |

## 2A. New backend result from this workstream

`r12_master/workstreams/master-closure-chat-20261024/R12_D3_MULTIS_EXTRACTION_BOUND.md` proves an allowance-localization theorem for every regular d3 owner family through q=38. For N=9, it forces a single common missing triple through q=34, at most two common-S classes at q=35, and gives class-size-dependent subcritical/first-high-slack bounds through q=38. This is a genuine extraction advance, but does not cover d2 multi-S systems, lower-owner d3 systems, or every fully-decorated/shallow-loss class.

## 3. Overall theorem and proof-body status

The required final chain remains:

`K145 counterexample -> certified front-end dichotomy -> legal R(4,49) or T61 -> every backend/T61 terminal excluded -> contradiction`.

The inspected repository itself states `NOT_CERTIFIED` in `CANONICAL_STATE.md` and `PROOF_DAG.md`. The present evidence supports keeping that status. No closed local lemma or finite recurrence certificate substitutes for the missing exhaustive front-end/backend bridge.

## 4. Working priorities

1. Extend the new d3 multi-S extraction bound to the remaining owner counts / decorated branches, and prove the missing d2 extraction or finite kernel under the maximal-pivot contract; avoid re-running E-layer trees.
2. Keep E333 and E334 at their evidence-qualified statuses.
3. Integrate E407's five common-K11 templates with the same 284-edge core, once their actual template data are independently available.
4. Integrate E408 Q32/Q33 local constraints with the seven-block global color system; do not infer contradiction from necessary inequalities alone.
