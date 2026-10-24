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

- E333: `PROVED_RELATIVE_TO_CANONICAL_V4`, supported by `backend/E333_V5_CANONICAL_CLOSURE.md` and its reported arithmetic replay. The V4 forcing and upstream legal-backend contracts remain dependencies.
- E334: `SOURCE_REPORTED / CONDITIONAL`, not unconditional PROVED, because the V7/V8 package replay is explicitly pending in `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`.
- E335--E340: OPEN.
- E407/E408: use the later T61/V11/V12 source audit and the explicit Cell-B proof bodies, but preserve the source-reported boundary for unreplayed packages.

## 2. Three-anchor excess: K>=4 versus K>=8

### Apparent discrepancy

`backend/GLOBAL_THREE_ANCHOR_EXCESS_LOWER_BOUND.md` proves the baseline `K>=4`. Other live-state files state `K>=8`.

### Resolution

These are successive theorem layers, not contradictory statements:

1. The lower-bound file rules out `K<=2) and establishes `K>=4).
2. `backend/GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md` closes the K=4 equality layer.
3. `backend/GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md` closes the exhaustive K=6 connector partition.
4. Since `K=2e(H)-420` is even, the combined theorem yields `K>=8), hence `e(H)>=214).

The valid K>=8 envelope is therefore conditional on the complete chain, especially the K=4 and K=6 closures; it must not be attributed to the K>=4 file alone.

## 3. E334: “empty” versus “source-reported”

### Apparent discrepancy

`OPEN_FRONTIERS.md` summarizes E334 as empty under retained assumptions, while `LIVE_THREE_LINE_STATE.md` and `V12_V8_SOURCE_REPORTED_AUDIT.md` state that package replay remains pending.

### Resolution

The mathematical graph theorem behind the three-anchor contradiction is analytically represented. The E334-specific implication that every legal E334 survivor enters that contract is imported from V7/V8 and has not been independently replayed in this session.

Therefore the evidence-based status is:

> `E334 = SOURCE_REPORTED / CONDITIONAL on retained backend + V7/V8 forcing`.

This preserves the conditional theorem while avoiding an unjustified promotion to fully independently audited closure.

## 4. E407 Q31: V10 open versus V11 source-reported exclusion

### Apparent discrepancy

`front_end/T61_H13_V10_CANONICAL_AUDIT.md` leaves Q31 coverage/completion open, whereas `front_end/T61_H13_V11_SOURCE_AUDIT.md` reports E407 and E408 Q31 exclusion under retained lower-order seeds.

### Resolution

V11 is the later claimed mathematical advance, but its package replay is still pending. Thus Q31 is not treated as unconditionally proved in this workstream; it is `SOURCE_REPORTED / CONDITIONAL` relative to V11's retained-seed contract. V10 remains useful evidence that the earlier shell inequalities alone did not close Q31.

## 5. E407 Cell-B closure versus full E407

### Apparent discrepancy

`front_end/E407_CELL_B_FULL_CLOSURE.md` proves no E407 `|W|=23) Cell-B completion, while the global frontier still lists E407 Q32 open.

### Resolution

These statements concern different scopes. The Cell-B theorem excludes one sharp common-antineighbourhood normal form. V12 reports five remaining Q32 common-K11 templates, whose simultaneous compatibility with one 284-edge core remains open. No conflict exists once the scope is made explicit.

## 6. E408 Q33 exact budget versus Q33 closure

### Apparent discrepancy

`front_end/E408_Q33_D3_EXACT_BUDGET.md` proves `beta+X+G_B=3`, but E408 Q33 remains open.

### Resolution

The exact identity is conditional on the retained V11 Q33 interface and only classifies a necessary integer budget. It does not eliminate `beta=0,1,2,3), prove the core graph exists, or extend the local shell to the global seven-block near-Latin coloring. E408 Q33 remains OPEN.

## 7. General status policy for this workstream

Use these labels consistently:

- `PROVED`: a proof body and all dependencies needed for the stated theorem are available and the stated contract is met.
- `PROVED_RELATIVE_TO(contract)`: the theorem body is present, but named upstream assumptions are retained.
- `SOURCE_REPORTED / CONDITIONAL`: a delivered result is described in a source audit, but its package or retained-seed bridge has not been independently replayed.
- `OPEN`: no complete contradiction or certified completion exclusion is established for the full stated case.

The root theorem remains `OPEN / NOT_CERTIFIED`. No local closure or source-reported package changes that verdict by itself.
