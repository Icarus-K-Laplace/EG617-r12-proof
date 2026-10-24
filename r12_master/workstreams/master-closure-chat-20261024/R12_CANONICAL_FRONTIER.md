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

For a legal 49-point residual F and every degree-13 pivot, the exact identity is `E = 91 + q + e(H)`, with a 35-point core H. The new `R12_UNIVERSAL_CORE214_THEOREM.md` proves that the full legal-core contract itself forces `e(H)>=214`: if a core had excess K<=6, at least29 vertices would have degree12; `omega(H)<=11` gives a nonadjacent degree-12 pair, whose at least nine common nonneighbours include a third degree-12 vertex. The registered three-anchor theorem then contradicts K<=6. Therefore every legal pivot, without separately extracting anchors, satisfies `q<=E-305`.

| Layer | Evidence-based status | Contract / evidence | Exact remaining gap |
|---|---|---|---|
| E329--E332 | `PROVED_RELATIVE_TO_REGISTERED_DEPENDENCIES` | `backend/E329_E332_CLOSURE.md`, `backend/E332_FULL_CLOSURE.md`, CORE211 and the q27/q28/q29 assets. | Keep inherited CORE211/q27/topology assumptions explicit for a self-contained manuscript; do not reopen the layer casework. |
| E333 | `PROVED_CONDITIONAL` | `R12_E333_E334_REPIVOT_CLOSURE.md`: universal legal-core floor gives q<=28; q27 is excluded by the registered q27 shell theorem, and q28 repivots to q'>=30. | Retain the q27 inherited shell-floor and boundary-sublemma dependencies; V5 package replay is not needed for this edge-layer contradiction. |
| E334 | `PROVED_CONDITIONAL` | `R12_E333_E334_REPIVOT_CLOSURE.md`: universal legal-core floor gives q<=29; q27 is excluded and q28/q29 repivot to q'>=30. | Same registered q27 shell dependencies plus q28/q29 repivot theorems; V7/V8 package replay is not needed for this edge-layer contradiction. |
| E335--E340 | `OPEN`, with sharpened pivot ceilings | Universal legal-core floor gives q<=E-305, i.e. E335..E340 ceilings 30,31,32,33,34,35. Existing support/allowance machinery remains conditional on exhaustive extraction. | Prove the forcing bridge for the reduced q<=30..35 range and close the remaining higher-slack d2/d3 residues. |

## 2A. New backend results from this workstream

`R12_UNIVERSAL_CORE214_THEOREM.md` upgrades the legal-core floor from e(H)>=211 to e(H)>=214 under the full alpha<=3, omega<=11, minimum-degree-12 contract. `R12_E333_E334_REPIVOT_CLOSURE.md` then independently closes E333 and E334 relative to the registered q27 shell dependencies and q28/q29 repivot theorems.

`r12_master/workstreams/master-closure-chat-20261024/R12_D3_MULTIS_EXTRACTION_BOUND.md` proves an allowance-localization theorem for every regular d3 owner family through q=38. For N=9, it forces a single common missing triple through q=34, at most two common-S classes at q=35, and gives class-size-dependent subcritical/first-high-slack bounds through q=38. This is a genuine extraction advance, but does not cover d2 multi-S systems, lower-owner d3 systems, or every fully-decorated/shallow-loss class.

### Independent-triple extension through total excess four

`R12_INDEPENDENT_TRIPLE_H4_EXTENSION.md` and `R12_INDEPENDENT_TRIPLE_H5_EXTENSION.md` prove that any independent triple in a 35-core with alpha<=3, omega<=11, and minimum degree12, whose total excess above12 is at most5, forces K>=8 (e(H)>=214). This extends the common-S independent-triple anchor envelope through the full d3 allowance ceiling a<=8. The independent-triple branch no longer contributes an open d3 shallow-loss case.

### d3 disjoint-support compatibility through q=38

`R12_D3_DISJOINT_SUPPORT_COMPATIBILITY.md` proves that disjoint d3 core supports have missing triples intersecting in at least two vertices. If the triples differ, their core cross-edge count is at most `q-36`. The block-transversal theorem then bounds the number of distinct missing-triple types in any disjoint-support family by 1 for q<=35, 3 for q=36,37, and 6 for q=38. This strengthens the old q<=32 extraction interface, but does not bound repeated-common-S support multiplicity or intersecting supports.

## 3. Overall theorem and proof-body status

The required final chain remains:

`K145 counterexample -> certified front-end dichotomy -> legal R(4,49) or T61 -> every backend/T61 terminal excluded -> contradiction`.

The inspected repository itself states `NOT_CERTIFIED` in `CANONICAL_STATE.md` and `PROOF_DAG.md`. The present evidence supports keeping that status. No closed local lemma or finite recurrence certificate substitutes for the missing exhaustive front-end/backend bridge.

## 4. Working priorities

1. Extend the new d3 multi-S extraction bound to the remaining owner counts / decorated branches, and prove the missing d2 extraction or finite kernel under the maximal-pivot contract; avoid re-running E-layer trees.
2. Audit the retained q27 shell-floor/boundary dependencies and use the new q<=E-305 ceilings to reorganize E335--E340 without reopening E329--E332.
3. Integrate E407's five common-K11 templates with the same 284-edge core, once their actual template data are independently available.
4. Integrate E408 Q32/Q33 local constraints with the seven-block global color system; do not infer contradiction from necessary inequalities alone.
