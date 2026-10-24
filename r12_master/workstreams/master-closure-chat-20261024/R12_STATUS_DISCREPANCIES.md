# R12 status discrepancies and resolution policy

Audit date: 2026-10-24  
Working branch: `workstream/r12-master-closure-20261024`.

This document records discrepancies between repository snapshots and explains which status is used for the present workstream. It does not mutate the root canonical files.

## 1. Root canonical state versus newer live frontier

### Discrepancy

- `CANONICAL_STATE.md` is dated 2026-10-22 and still lists `E333..E340` as the complete open backend obligation.
- `LIVE_THREE_LINE_STATE.md` and `OPEN_FRONTIERS.md` include later work: E333 has a V5 canonical closure, E334 has a V8 source-reported closure, and the global three-anchor theorem has advanced.
- Newer E407/E408 assets include the seven-block equality system, exact-129 blocker theorem, and E408 Q33 d3 exact budget.

### Resolution

Use the newer proof bodies and audit notes, but do not infer certification solely from recency:

- E333: `PROVED_CONDITIONAL` via the new independent `R12_E333_E334_REPIVOT_CLOSURE.md`, relative to the registered q27 shell dependencies and q28 repivot theorem. The V5 route is no longer needed for this edge-layer contradiction.
- E334: `PROVED_CONDITIONAL` via the same new repivot closure, relative to q27/q28/q29 dependencies. The V7/V8 package replay is not needed to exclude E334 under the full legal-core contract, although the source-reported V8 argument remains a separate route.
- E335--E340: OPEN.
- E407/E408: use the later T61/V11/V12 source audit and the explicit Cell-B proof bodies, but preserve the source-reported boundary for unreplayed packages.

## 2. Three-anchor excess: K>=4 versus K>=8

### Apparent discrepancy

`backend/GLOBAL_THREE_ANCHOR_EXCESS_LOWER_BOUND.md` proves the baseline `K>=4`. Other live-state files state `K>=8`.

### Resolution

These are successive theorem layers, not contradictory statements:

1. The lower-bound file rules out `K<=2` and establishes `K>=4`.
2. `backend/GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md` closes the K=4 equality layer.
3. `backend/GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md` closes the exhaustive K=6 connector partition.
4. Since `K=2e(H)-420` is even, the combined theorem yields `K>=8`, hence `e(H)>=214`.

The valid K>=8 envelope is therefore conditional on the complete chain, especially the K=4 and K=6 closures; it must not be attributed to the K>=4 file alone.

## 3. E334: “empty” versus “source-reported”

### Apparent discrepancy

`OPEN_FRONTIERS.md` summarizes E334 as empty under retained assumptions, while `LIVE_THREE_LINE_STATE.md` and `V12_V8_SOURCE_REPORTED_AUDIT.md` state that package replay remains pending.

### Resolution

The new `R12_UNIVERSAL_CORE214_THEOREM.md` proves that every legal 35-core has e(H)>=214, hence every E334 pivot has q<=29. The registered q27 shell theorem excludes q=27, while the q28 and q29 repivot theorems force q'>=30, contradicting the same-residual ceiling. Therefore E334 is now `PROVED_CONDITIONAL` on the registered q27 shell dependencies and q28/q29 repivot theorems. The V7/V8 package remains source-reported, but its replay is not needed for this alternative E334 closure.

## 4. Universal core floor versus CORE211 equality channels

The legal-core contract is stronger than the standalone CORE211 contract. If alpha(H)<=3, omega(H)<=11, delta(H)>=12 on 35 vertices, then K<=6 would give at least29 degree-12 vertices; a nonadjacent pair among them has at least nine common nonneighbours, including a third degree-12 vertex. The three-anchor theorem then contradicts K<=6. Thus every legal core has e(H)>=214. This does not strengthen CORE211 for graphs without omega(H)<=11, but it invalidates any q32/e(H)=211 state if it is presented as a fully legal E334 core.

## 5. E407 Q31: V10 open versus V11 source-reported exclusion

### Apparent discrepancy

`front_end/T61_H13_V10_CANONICAL_AUDIT.md` leaves Q31 coverage/completion open, whereas `front_end/T61_H13_V11_SOURCE_AUDIT.md` reports E407 and E408 Q31 exclusion under retained lower-order seeds.

### Resolution

V11 is the later claimed mathematical advance, but its package replay is still pending. Thus Q31 is not treated as unconditionally proved in this workstream; it is `SOURCE_REPORTED / CONDITIONAL` relative to V11's retained-seed contract. V10 remains useful evidence that the earlier shell inequalities alone did not close Q31.

## 6. E407 Cell-B closure versus full E407

### Apparent discrepancy

`front_end/E407_CELL_B_FULL_CLOSURE.md` proves no E407 `|W|=23` Cell-B completion, while the global frontier still lists E407 Q32 open.

### Resolution

These statements concern different scopes. The Cell-B theorem excludes one sharp common-antineighbourhood normal form. V12 reports five remaining Q32 common-K11 templates, whose simultaneous compatibility with one 284-edge core remains open. No conflict exists once the scope is made explicit.

## 7. E408 Q33 exact budget versus Q33 closure

### Apparent discrepancy

`front_end/E408_Q33_D3_EXACT_BUDGET.md` proves `beta+X+G_B=3`, but E408 Q33 remains open.

### Resolution

The exact identity is conditional on the retained V11 Q33 interface and only classifies a necessary integer budget. It does not eliminate `beta=0,1,2,3`, prove the core graph exists, or extend the local shell to the global seven-block near-Latin coloring. E408 Q33 remains OPEN.

## 8. General status policy for this workstream

Use these labels consistently:

- `PROVED`: a proof body and all dependencies needed for the stated theorem are available and the stated contract is met.
- `PROVED_RELATIVE_TO(contract)`: the theorem body is present, but named upstream assumptions are retained.
- `SOURCE_REPORTED / CONDITIONAL`: a delivered result is described in a source audit, but its package or retained-seed bridge has not been independently replayed.
- `OPEN`: no complete contradiction or certified completion exclusion is established for the full stated case.

The root theorem remains `OPEN / NOT_CERTIFIED`. No local closure or source-reported package changes that verdict by itself.
