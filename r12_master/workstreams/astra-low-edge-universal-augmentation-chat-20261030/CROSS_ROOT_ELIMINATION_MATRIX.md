# Cross-root elimination and supersession matrix

Date: 2026-10-30.

## Fully mapped charge layers

All rows below use the actual h13 T61 parent P0 and the independently proved generic hereditary minimum-degree gate. CLOSED means impossible under that explicit parent contract; it does not assert that the complete global reduction has been re-certified.

| Parent layer | Core edges | Parent mapping | Terminal result | Precise status |
|---|---:|---|---|---|
|E407 / q_p=31, including Q_max=31|285|PROVED from P0|directly excluded by low-edge theorem|CLOSED / PROVED_CONDITIONAL on P0|
|E407 / q_p=32, including Q_max=32|284|PROVED from P0|directly excluded|CLOSED / PROVED_CONDITIONAL on P0|
|E408 / q_p=32, including Q_max=32|285|PROVED from P0|directly excluded for m=8,9,10 and every selected support size|CLOSED / PROVED_CONDITIONAL on P0|
|E408 / q_p=33, including Q_max=33|284|PROVED from P0|directly excluded for every source/profile/support placement|CLOSED / PROVED_CONDITIONAL on P0|
|Any R(4,47) graph with at most285 edges|<=285|generic gate supplies delta>=12|directly excluded|PROVED|
|All E407 regular pivots|>=286 core edges|PROVED from P0|q_p<=30|PROVED_CONDITIONAL on P0|
|All E408 regular pivots|>=286 core edges|PROVED from P0|q_p<=31|PROVED_CONDITIONAL on P0|

## V12 and support work that becomes unnecessary for these layers

The E407 V12 branch reports554 necessary-shell survivors assigned to A--E (30,54,24,226,220). These are finite shell objects, not completed61-vertex parents. The new theorem does not claim those combinatorial shell objects cease to exist.

For ANY legal E407/Q32 completion of ANY of those shells:

    actual P0 parent + regular q=32 pivot
       => induced H in R(4,47), e(H)=284
       => Theorem M: delta(H)>=12
       => low-edge theorem: contradiction.

Therefore every legal parent completion of all five template families is impossible. This route has no MS-29 assumption, no need to produce a29-point union, no use of the49 selected blocks, and no dependence on V12 finite enumeration being exhaustive. The V12/MS-29 route can be removed from the dependency path to THIS E407/Q32 contradiction after root review. No assertion that MS-29 itself is proved is made.

Likewise E408/Q33 requires no promotion of a56-witness union from31 to larger support sizes. E408/Q32 requires no m-specific residual grid enumeration and no distinction between selected supports of size44,45,46 or47. The induced antineighborhood H always has47 vertices; its order is not the selected witness-union size v.

## Still OPEN in this workstream

| Object | Reason it is not closed here |
|---|---|
|E408 / q_p=31|Core has286 edges, outside the <=285 theorem; existing V11 closure retains its own dependencies|
|E407 / q_p<=30|Core has at least286 edges; exclusion needs other arguments|
|E407 or E408 as entire energy layers|Requires audited coverage or charge-lower-bound theorems, not merely the upper bounds proved here|
|Non-h13 pivots/parents|The47-point identity uses a degree13 pivot; h12 leaves48 vertices|
|Bare47-point graphs without delta>=12 and without inherited caps|Neither the universal core theorem nor Theorem M applies|
|Contextual R(4,49), original K145 bridge and remaining root dependencies|Not re-proved by these terminal obstructions|
|Global root promotion|Not applied; all writes remain in this isolated workstream|

Old sibling status files remain unchanged. This matrix is an importable replacement route, not a silent edit of their proof claims.
