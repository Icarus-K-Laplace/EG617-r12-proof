# EG617(r=12) — independent root dependency DAG

Date: 2026-10-29
Audit status: **FAIL-CLOSED / OPEN / NOT_CERTIFIED**

This is an independent branch-local audit. It does not promote the theorem while E408-Q32 remains open.

## 1. Shortest currently audited root chain

```text
balanced K145 counterexample
  |
  +--> contextual R(4,49) ------------------------------ X
  |       FRONTEND_BRIDGE_THEOREM + contextual R449 closure
  |
  `--> T61, 397 <= E <= 408
          |
          +--> h12 -------------------------------------- X
          `--> h13
                 |
                 +--> E397--E406 ------------------------ X
                 +--> E407
                 |      +--> Q31 ------------------------ X
                 |      `--> Q32 ------------------------ CONDITIONAL (29-point reserve contract; V12/parent bridge must remain explicit)
                 `--> E408
                        +--> Q31 ------------------------- X (conditional + replay-backed)
                        +--> Q33 ------------------------- CONDITIONAL (31-point/56-witness contract; support exhaustiveness must be source-linked)
                        `--> Q32 ------------------------- OPEN
```

Therefore the unique currently identified live **graph terminal** is

> **E408 / h13 / Qmax=32 / 47-core / 285 edges / excess 6.**

This statement is relative to the named retained front-end and lower-order inputs. It is not a claim that every publication dependency has been re-proved in this chat.

## 2. Front-end gate

The fail-closed root receipt freezes:

- `front_end/FRONTEND_BRIDGE_THEOREM.md`, blob `52b2f4af102ceba1671dc7d0e7ed36a512458e77`;
- line-A package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 1,752 recurrence nodes;
- 144 stopping comparisons;
- 73 manifest files, 0 errors;
- unique no-R449 stop `(11,6,5,61)` with `397<=E<=408`;
- independent replay PASS.

The receipt also freezes the contextual R449 exclusion, relative to its named extremal input.

Important scope point: the computation receipt certifies the enumerated recurrence/stopping package. External/analytic bridge statements retain their hypotheses.

## 3. V9/V10/V11 status

V9 is independently replayed relative to its retained seeds.

The newer `V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md` supersedes the older V11 `INDEPENDENT_REPLAY_PENDING` note. Its frozen replay records include:

- V10 archive SHA256 `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`;
- V11 archive SHA256 `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`;
- V11 certificate SHA256 `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`;
- 684 kernel weights, 349 outside-count states, 259 necessary shells, 252 Family-A + 7 Family-B states, zero completed graphs.

Hence E407/E408 Q31 may be imported only as **PROVED_CONDITIONAL + COMPUTATION_CERTIFIED** under their named analytic/lower-order contracts.

## 4. E407 Q32: replay coverage versus analytic contradiction

The latest fail-closed receipt records the V12 finite screen as computation-certified:

- archive SHA256 `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`;
- certificate SHA256 `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`;
- 8,677 kernel weights;
- 17,957 count states;
- 1,984 necessary shells;
- 554 survivors mapped to five templates.

This audit checked the exact read-only sibling freeze at commit

`b36538e27dce89dfcba2aa2bfdfc29d6611a96ec`.

The expected blobs match exactly:

- `FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md` = `8b95bbf59e7a9232eff6cc27c9f50177533e5e21`;
- `SUPPORT_BLOCK_ANCHOR_IDENTITY.md` = `50447a9931b9b51a21a979dc61d834389abd4e3a`;
- `PROOF_DEPENDENCY_AUDIT.md` = `4b6c8ef85dce38003591c1aa712b7f9b637a68cb`.

Crucial distinction: the frozen five-template file itself still says **OPEN**. Therefore `554 -> five templates` is not by itself a contradiction.

The later source-correct theorem `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` bypasses the individual template compatibility problem. It uses only their shared support contract:

- `|U|=29`;
- 49 selected independent four-blocks, seven in each of seven distinct exact colors;
- selected-component color identity;
- pairwise edge-disjointness of the 49 monochromatic K4 edge sets;
- `e(overline(H[U])) = 294+delta <=310`.

The selected blocks already own

`49*C(4,2)=294`

complement edges. One of the four unselected non-target colors has `alpha<=12` on 29 vertices, hence needs at least

`p_12(29)=22`

additional U-edges. Unique color ownership gives

`294+22=316>310`.

Thus E407-Q32 is closed **conditional on V12 exhaustiveness and the frozen 29-point/49-block support contract**, without the retracted KP degree-nine premise and without solving the five templates one by one.

The raw V12 archive is not re-executed in this chat; this audit verifies the replay receipt/hashes and the exact frozen analytic support files. Do not describe that as a fresh independent rerun by this workstream.

## 5. E408 Q33

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` excludes `m=10` under the registered 31-point/56-witness Q33 support contract.

`Q33_NONEXACT_U_RESERVE_CLOSURE.md` then uses:

- `e(overline(H[U]))=336+delta`, `delta<=17`;
- at most `h<=4` selected gadget witnesses (the stronger sibling result is `h<=3`, not needed);
- every non-target color on 31 vertices has at least `p_12(31)=26` U-edges;
- the selected component witnesses leave at most `delta+6h<=41` slots for all nonexact colors.

For `m=9` two nonexact colors need `52>41`; for `m=8` three need `78>41`. Therefore the registered Q33 minimum-support terminal is impossible.

The root receipt asserts that the upstream E408 reduction enters this 31-point/56-witness terminal, but the exact exhaustive support-lifting theorem was not identified in the source paths inspected during this pass. Until that theorem and its coverage of every Q33 completion are linked, treat this premise as an explicit unresolved dependency. The Q33 contradiction itself does not use the Q32 285-edge identity or the false degree-nine claim.

## 6. E408 Q32 — only live graph gate

Valid source-correct interface currently retained:

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- core excess `sum_H(d_H-12)=6`;
- `m in {8,9,10}` exact-129 non-target colors;
- exact Type-I factorization `10K5 dot-union G11`;
- each exact color supplies at least ten disjoint core K4 witnesses;
- cross-color witness family pairwise linear;
- witness union `|U|>=44`;
- corrected non-full-support multiplicity `n_w>=m-6`;
- latest nonexact pointwise floors `L8=12`, `L9=7`, `L10=3`;
- Case I closed for v=44,45 and all v=46 rows;
- this workstream closes Case-II v=45,46 for m=8,9,10 using weighted surplus, zero-shell multiplicity, and the direct 130-edge no-core-only degree-four theorem;
- sibling branch `workstream/r12-q32-caseII-v44-final-20261028` closes v=44 for m=8,9,10.

Still open in this workstream at this snapshot:

- full support v=47, m=8,9,10.

The universal zero-shell bound now closes m=10 for every non-full-support branch. The sibling branch `workstream/r12-q32-caseII-v44-final-20261028` closes the full v=44 support layer for m=8,9,10; final merge/root consolidation remains pending.

## 7. Promotion rule

Root promotion is forbidden until **all** source-correct E408-Q32 rows are eliminated and the sibling v=44 result is merged/audited.

Even after Q32 closes, promotion requires a final replay/source-freeze pass over every retained root dependency. Until then:

> **EG617(r=12) = OPEN / NOT_CERTIFIED.**


## 8. Independent audit addendum — support contracts and branch reconciliation

This addendum controls any broader wording above if the statements conflict.

### 8.1 E407 Q32 U-reserve

The exact file `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` is present on the global workstream branch and proves the local contradiction under its frozen contract:
- `|U|=29`;
- 49 selected K4 support blocks, seven in each of seven exact colors;
- `e(\overline{H[U]})=294+delta<=310);
- one unselected non-target color needs at least `p_12(29)=22) U-edges;
- hence `294+22=316>310).

The arithmetic is valid and does not use the retracted degree-nine claim. Its **scope** is the frozen 29-point/49-block V12 terminal contract. The V12 replay receipt reports 8,677 kernel weights, 17,957 count states, 1,984 necessary shells, and 554 survivors mapped to five templates; the raw archive was not re-executed by this workstream in this turn.

There is a branch-state discrepancy: the dedicated E407 closure branch's `CANONICAL_STATE.md` and `PROOF_DEPENDENCY_AUDIT.md` still say the five-template same-core problem is OPEN. The global workstream's U-reserve theorem bypasses template-by-template compatibility **if** the frozen V12 terminal contract is exhaustive. Until that premise and the branch promotion are reconciled, record E407 Q32 as **PROVED_CONDITIONAL on the frozen V12 contract**, not as an unconditional root closure.

### 8.2 E408 Q33 support-contract exhaustiveness

`Q33_NONEXACT_U_RESERVE_CLOSURE.md` proves a valid contradiction on the registered `|U|=31`, 56-witness contract: `26(11-m) <= delta+6h <= 41`, while m=8 or9 requires at least78 or52.

However, the theorem's own scope firewall conditions promotion on an upstream proof that every Q33 completion enters this contract. The inspected witness-packing theorem gives a **lower bound** on support size (`|U|>=31`), and the Q33 local theorem takes `|U|=31` as a frozen input. The separate exhaustive support-lifting theorem was not located among the inspected source files in this pass. The root DAG's earlier statement that upstream exhaustiveness is explicit therefore remains an unresolved citation/dependency question here.

Until the exact support-lifting source and its parameter coverage are linked and checked, record Q33 as **PROVED_CONDITIONAL on the 31-point terminal contract**, with full Q33 exhaustion **NOT INDEPENDENTLY RE-CERTIFIED** in this workstream.

### 8.3 Current v=47 Q32 addition

`V47_PIVOT_NEIGHBORHOOD_PACKING.md` proves m vertex-disjoint independent K4s selected from exact-color pivot neighborhoods. The common edge baseline is 253; the 285-edge core leaves 32 slack units. The arithmetic verifier `verify_v47_pivot_packing.py` returned `V47_PIVOT_PACKING_ARITHMETIC_OK`, with 79, 61, and 44 feasible scalar slack states for m=8,9,10. This is a graph-structure reduction, not an UNSAT certificate.

### 8.4 Final root gate

- E408 Q32 remains the live graph terminal in the audited shortest chain.
- The source-correct Q32 support-44 result is in a sibling branch and has not been merged into this workstream.
- E407 Q32 and E408 Q33 reserve contradictions remain conditional on their named support contracts and parent exhaustiveness.
- No root promotion is allowed while any of those contract/exhaustiveness dependencies is unresolved.

[
\boxed{\text{EG617}(r=12)=\text{OPEN / NOT\_CERTIFIED}.}
]

## 9. New universal zero-shell multiplicity bound

For any nonempty W-point w, the source-correct Type-I K5 shows that a special exact color with zero shell-A degree must own pw; at most one special exact color at w can therefore have zero shell degree. The m-n_w non-special exact colors each use at least two distinct w--A edges. If t_w is the number of target-colored edges from w to A, the exact inequality is

`n_w-1 <= 13-t_w-2(m-n_w)`, hence `n_w >= 2m-14+t_w`.

The pointwise special-surplus budgets are `n_w<=r_m`, with `r_8=3`, `r_9=4`, `r_10=4`. Thus m=10 is impossible whenever W is nonempty; m=9 forces `n_w=4`, all special parameters `a=4`, and `t_w=0` at every W-point; m=8 remains closed by its two-unit special-incidence cost against budget3. For m=9, the shell count saturates exactly: five non-special exact colors use 10 A-edges, three special colors use one each, and one special color uses zero and owns pw. Both nonexact colors have no A-shell neighbors; the target degree is13, so each W-point has core excess1. This makes the 130-edge color degree four at w with all neighbors in H. The direct theorem `Q32_130_NO_CORE_ONLY_DEG4.md` rules out even one such vertex, closing both v=45,m=9 and v=46,m=9. Do not use the older unsupported W-pair/e_H(W)=0 inference; the direct contradiction is independent of it.

Thus, together with the weighted m=8 closure and zero-shell m=10 closure, every non-full-support row v=45,46 is closed. The sibling branch closes v=44. Full support v=47, where W is empty, is the sole live Q32 support terminal.

### 8.5 Direct no-core-only degree-four theorem closes v45/v46 m=9

The local source-correct file `Q32_130_NO_CORE_ONLY_DEG4.md` proves:
> For a 130-edge non-target color D with alpha(D)<=12, omega(D)<=5 and delta(D)>=4, no core vertex u in H can have d_D(u)=4 with all four D-neighbors in H.

The proof uses Kang–Pikhurko Theorem 1 at (56,11) to show every degree-four vertex has at least five edges induced by its neighborhood. If u is core-only degree four, the 130-edge budget and alpha(H)<=4 force D[N_D(u)]=K4-e with the two cross edges attached to the missing-edge endpoints. An endpoint then has a four-neighbor graph consisting of a triangle plus an isolated vertex, contradiction.

The v45 and v46 m=9 shell normal forms each force a 130-edge color vertex of degree four at W, with no A-neighbor and no pw edge (the unique zero-shell special exact color owns pw). Thus both rows are closed directly. This theorem supersedes the earlier unsupported v45 W-pair rigidity inference and does not use exceptional-vertex injectivity.

The source-safe Q32 frontier after this addition is:
- v44,m=8,9,10: closed by the sibling branch;
- v45,m=8,9,10: closed;
- v46,m=8,9,10: closed;
- v47,m=8,9,10: open.


## 10. Zero-slack map alignment / transversal-capacity refinement

New proof asset: `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md`.

For the m=10 disconnected light-block cases 2+8 and 3+7, the small-component blocks have zero Q-R incidence slack. Their unique-neighbor maps on R therefore coincide after matching alignment. In the 3+7 light triangle, all three maps agree.

For each outer vertex q in the 3+7 cell, the local 4,5,5 switch theorem plus the independent-transversal argument yields:
- singleton common track h: q is adjacent to every residual vertex in fiber F_h, so `k(q)<=3-|F_h|`;
- double common tracks: q uses all three extra edges to the small component and has no R-neighbor or other extra Q-Q incidence;
- per outer block, `sum_q k(q)=3`.

The exact normalized verifier `verify_v47_three_small_block_transversal.py` checks 1,728 aligned and 36 switch configurations, covering 7,056 vertex records, and returns `V47_ZERO_SLACK_TRANSVERSAL_LOCAL_OK`.

This tightens the disconnected m=10 cells but does not eliminate them. It is a structural reduction, not an UNSAT certificate. Full-support v47 remains open, so the root status remains EG617(r=12) OPEN / NOT_CERTIFIED.


### 10.1 Endpoint-load ledger and switch-count cap

The same theorem file now records the exact small-block endpoint load. For each small block label h, `e_i(h)>=3-n_h), and the excess above these floors sums to exactly 3 units in 2+8 and 2 units in 3+7. The only fiber-size partitions are `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, `(2,2,2,1)`.

In 3+7, every switch block sends all three extra endpoints to the same small-block label s; its duplicated common track has `n_s<=1). If `n_s=1), the singleton residual vertex spends one extra-incidence unit per such switch, so there are at most `2-d_R(r_s)` switches of that label. This is an exact cross-link between local matching switches, the endpoint floors, and residual degree. It does not yet close the 2+8/3+7 cells.


## 11. Full-support m=10 matching-holonomy refinement

New local theorem: `V47_TWO_LIGHT_MATCHING_COMPOSITION.md`.

For three independent 4-sets with two light matching pairs and a third pair of at most seven edges, the third pair must contain the composed matching. The exact local verifier covers all 25,636 bipartite edge sets with 4..7 edges and returns `V47_TWO_LIGHT_MATCHING_COMPOSITION_EXHAUSTIVE_OK`.

In the m=10 disconnected 2+8 and 3+7 cells, this forces every actual length-two light-path composition in the outer component (8 blocks for 2+8; 7 for 3+7) into the endpoint pair graph. The outer light graph has minimum degree at least 3 in 2+8 and at least 4 in 3+7; the all-nonadjacent-pairs common-neighbor conclusion is used only for 3+7. A 5-edge pair forces a unique composition; a 6-/7-edge pair can support at most two perfect matchings. At most six endpoint pairs can have 6 or 7 edges in 2+8 under x_T<=12, and at most three in 3+7 under x_T<=7.

This is a conditional local reduction only. It does not close either component-size cell or the full-support m=10 branch; root status remains EG617(r=12) OPEN / NOT_CERTIFIED.


### Matching-holonomy scope correction (2026-10-28)

The correct light-graph degree bounds are: 2+8 has eight outer blocks and minimum light degree at least 3; 3+7 has seven outer blocks and minimum light degree at least 4. Therefore the statement that every nonadjacent pair has a common light neighbor applies only to 3+7. In 2+8, the matching-composition theorem is used only on length-two light paths that actually exist. The local theorem and its finite verification remain valid; only this application scope is corrected.


## 12. Four-light-cycle holonomy restriction

Added `V47_LIGHT_CYCLE_HOLONOMY.md`. The two-light composition theorem forces both diagonals of a light 4-cycle to contain the two path matchings. The seven-edge cap rules out derangements; a 3-cycle is ruled out by an explicit independent 5-set. Thus only identity or transposition holonomy survives, and transposition holonomy requires both diagonals to be 6/7-edge pairs.

The normalized exact verifier checked 726 transposition cases and all eight 3-cycle cases, returning `V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK`. This is a local reduction only. The m=10 disconnected cells and all full-support Q32 rows remain OPEN.


## 13. m=10 disconnected 3+7: globally aligned outer tracks

New proof: `V47_37_OUTER_LIGHT_HOLONOMY.md`.

Under the 3+7 cell contract, the outer light graph has seven vertices, minimum degree four, weighted heavy degree at most two, and total heavy weight at most seven. Triangle consistency and the four-light-cycle theorem force identity holonomy on every cycle: chordless five-cycles have a common light hub, and six-/seven-cycles must have chords. Thus light-edge matchings globally align. Since any heavy pair has at least three common light neighbors, the same matching is contained in every pair graph.

This yields four aligned K7 tracks on the 28 outer-block vertices and at most seven additional cross-track edges. The finite weighted-graph verifier covers 22,054 outer heavy graphs and 5,803,387 light cycles. This is a local structural reduction only; it does not close the m=10 3+7 cell or any full-support Q32 row.


### 8.3 Current high-support continuation — m=10 disconnected cells

The latest branch-local additions are `V47_TWO_BLOCK_TRANSVERSAL_BLOCKER.md` (2+8) and the strengthened double-track part of `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md` (3+7). They impose exact fiber-neighborhood and endpoint-load restrictions but do not eliminate the disconnected cells. The only live graph terminal remains E408/Q32 full-support v=47, with m=8,9,10 OPEN. No root promotion is permitted.


## 14. m=10 3+7 residual-track domination

Added `V47_37_RESIDUAL_TRACK_TRANSVERSAL.md`.

After global alignment, the seven outer blocks form four K7 tracks with at most seven cross-track edges and cross-track maximum degree two. For any residual vertex r, `d_R(r)+b_r=2), so at least 19 of the 28 outer vertices are nonneighbors of r. If r missed at least one vertex on every track, the four nonneighbor part sizes would sum to at least19. A strict union-bound theorem, exhaustively checked over all 64 part-size profiles and all relaxed six-variable edge-count allocations, guarantees an independent transversal avoiding r. That would give an independent 5-set, so r must be complete to one entire K7 track.

The verifier returns `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK` with minimum count margin63. This is a conditional structural consequence of the 3+7 cell; it does not close that cell or promote the root theorem.


### 8.4 3+7 double-track refinement

The 3+7 local blocker now adds the exact residual edge floor for any double-track vertex. In particular, the z=0,1 residual cells have only singleton-track vertices. The arithmetic verifier is replayed and passes. This is a local branch reduction only; full-support v47,m=10 remains OPEN and the root theorem stays OPEN / NOT_CERTIFIED.


### 14a. 3+7 track fibers are cliques

The residual-track theorem is strengthened: the unique track complete to r defines a fiber, and two nonadjacent residual vertices cannot share a fiber. Each of the other three tracks would provide at least three vertices nonadjacent to both; with at most seven cross-track edges, the three-part union bound guarantees an independent transversal. Hence the track assignment partitions R into at most four cliques, with size profile one of `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, `(2,2,2,1)`. This matches the possible small-block map fiber profiles but does not yet prove the two partitions coincide.


### 8.5 3+7 z=4 empty-fiber escape

The exact source-correct lemma `V47_Z4_EMPTY_FIBER_ESCAPE_CLASSIFICATION.md` excludes the all-aligned singleton-track cell for fiber profile (3,2,2,0). A remaining local completion must contain a switch whose duplicated label is empty, or a double-track block involving the empty fiber. The Q32 full-support graph terminal remains OPEN; no root promotion.


### 8.6 Double-track alpha blocker

The 3+7 double-track branch is further restricted by `alpha(H[R])<=3), because a double-track vertex has no R-neighbors. The exact residual-type list leaves six types at z=2,3,4 and none at z=0,1. This remains a local reduction; the root stays OPEN / NOT_CERTIFIED.


### 14b. RETRACTED — global small-to-outer matching permutations

The former claim that every small block has a fixed matching permutation to all seven outer blocks is **RETRACTED**. The proof incorrectly charged both endpoints of a switch edge to the same small-side label. The exact 4,5,5 switch theorem places the two extra edges at distinct moved labels. See `V47_37_SMALL_OUTER_MATCHING_RIGIDITY_RETRACTION.md`.

The seven-vertex cut-endpoint lemma remains valid, but it does not imply the claimed matching constancy. The independent z=0,1 track-partition alignment proof remains a separate dependency. The 3+7 cell remains OPEN.

### 8.7 New m=10, 3+7 low-z alignment

`V47_Z01_TRACK_ALIGNMENT.md` proves that z=0,1 have no double-track vertices, that the common small-triangle clique partition and the outer-track clique partition coincide, and that every outer block is aligned (no synchronized switch). This is a strict reduction only: the fully aligned z=0 and z=1 completions remain open. It does not alter the root promotion gate.


### 8.8 Replay-gap repair: z=4 empty-fiber arithmetic

The previously referenced `verify_v47_z4_empty_fiber_escape.py` was not present in the audited branch directory. It has now been added. The arithmetic was executed in-session over all 1,000 slack-vector profiles and confirms the bound `T_0>=9>x_T=7). This repairs the missing arithmetic artifact only; the analytic premise remains conditional on the registered z=4, (3,2,2,0), all-aligned singleton contract. It does not promote Q32.


### 8.9 Balanced-coloring K13 closure inside z=1

Within the already-aligned z=1, (3,2,1,1) cell, a size-three fiber plus its ten aligned pivot-track vertices forms a target-color K13. This contradicts the balanced-coloring condition that every 13-set contains all colors. Thus this residual profile is closed; z=1, (2,2,2,1), and z=0, (2,2,2,1), remain open. No root promotion.


### 14c. Balanced-coloring cross-track ledger for aligned z=0,1

Added `V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md`. The aligned target-color tracks have sizes 12,12,12,11. Every pair of K12 tracks has H-edges forming a matching, because a K12 plus any outside vertex is a 13-set that must contain all eleven non-target colors. For the K11--K12 pairs, the same bound is only asserted on the K11 side.

The exact degree ledger forces `22+E_0` H edges incident to the K11 track and `10-E_0` among the three K12 tracks, where `E_0 in {0,1,2,3}`. The arithmetic verifier checked 729 excess triples and 28,107 necessary aggregate states. This does not close either aligned low-z cell.


### 8.11 Aligned low-z Type-I placement reduction

`V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` eliminates the triple-outside Type-I K5 placement in the fully aligned m=10, 3+7, z=0,1 profile (2,2,2,1). The reason is the balanced-coloring degree floor `d_C(v,H)>=2` on each of the three K12 parts and `>=3` on the K11 part, while a triple-outside K5 gives its H vertices only one same-color H-neighbor.

The surviving exact-color types are x_C in O (one double/nine single K5s) and x_C in H two-double (two double/eight single K5s). Their G11 H-H edge counts are `12+g_C` and `15+g_C`. This reduces the local color-placement state space but does not close either low-z cell; the root gate remains OPEN.


The cross-track theorem also gives pairwise color-repeat conservation: for each K12--K12 pair and each non-target color C, the surplus `e_C(T_i,T_j)-12` equals the number of unmatched vertices on either side that repeat C. The two sides must have identical repeat-color counts. For a K11--K12 pair, the surplus over 11 is the repeated-color count among unmatched K11-side vertices. This is an additional finite color-assignment constraint; no closure is inferred.


The aligned z=0,1 cross-track ledger further gives `e_H(T_i,T_j)<=9-E_0-E_k<=9` for each pair of K12 tracks, where k is the third K12 label. Thus each such pair has at least three unmatched vertices on both sides, and the color-repeat counts on that pair have total deficit at least `3+E_0+E_k). This is a necessary restriction only.


### 8.12 Source correction: Type-I special K5 accounting

The prior entry asserting that the triple-outside Type-I placement is eliminated in the aligned z=0,1 cell is **superseded**. The Type-I profile has twelve K5 factors, comprising ten isolated components and two special K5 cliques inside G11. A triple-outside K5 is ruled out only if it is isolated. If triple placement occurs, it must be one of the two special K5s; the other special K5 is single-outside, forcing `b_s+b_t=4` and G11 composition (7 H,4 O). The source-correct gap ledger is `G_H=g_C`, `3+g_C`, `2+g_C` for x-in-O, two-double, and triple placements respectively. This correction removes the claimed closure; Q32 remains OPEN.


### 8.13 Aligned triple-special local normal form

The corrected Type-I audit now pins any triple placement in the aligned low-z cell to: `b_s+b_t=4), G11 with seven H and four O vertices, y in H, x and y in the same K12 part, the two H vertices of the triple special K5 in the other two K12 parts, and `g_C=3). The source arithmetic replay passes. This does not close the triple row or either low-z cell; root remains OPEN / NOT_CERTIFIED.


### 8.14 Aligned low-z exact-gap budget

In the fully aligned z=0,1 cell, the corrected Type-I component analysis caps every exact-color gap at three. Hence the unique nonexact color must have `g_D>=7). Its 132-edge total and the balanced-coloring lower bound of at least42 H-O edges imply `g_D<=21). Therefore `e_D(H) in [76,90]`, `mu_D<=21-g_D<=14`, and at least six exact colors have positive gap. This is a new global necessary condition for the low-z branch; it is not a closure and does not alter the root status.


### 8.15 Nonexact-color shell-floor tightening

For the aligned low-z cell, the unique nonexact color D has `g_D in [7,19]`, `e_D(H) in [76,88]`, and `mu_D in [2,14]). The lower shell bound `mu_D>=2) follows because p is D-nonadjacent to A and alpha(D)<=12, forcing alpha(D[A])<=11 on 13 vertices. Thus the ten exact colors contribute 18–30 gap units, with at least six positive-gap exact colors. This is a necessary aggregate budget only.


### 8.16 Type-I factor occupancy across target parts

The twelve Type-I K5 factors partition the 60 vertices other than x_C. Matching their H vertices to the part sizes (12,12,12,11) forces the double/triple occupancy vectors recorded in Section 8 of `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md`. In particular, x_C-in-K12 two-double placement requires a special double K5 containing X_0, and triple placement forces x_C outside X_0 with the triple H pair in the other two K12 parts. Arithmetic replay passes; this is a necessary reduction only.


### 14d. Residual 1-factorization in aligned z=0,1 (audit-corrected)

See `V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION.md`. **Correction:** the residual perfect matching P is not intrinsically canonical. Choose one Hall perfect matching for each non-target color on a K12--K12 pair; the eleven edge-disjoint matchings leave a perfect matching P. It contains all H-edges and all unselected color edges. Its color-C edge count is `e_C(T_i,T_j)-12`, and it contains at least three H-edges and three repeated-color edges by the nine-edge cap. For a K11--K12 pair, each color has a matching saturating T0; the residual set has one edge per T0 vertex but is not asserted to be a matching on the larger side.

The same file derives the 69/70 low-gap orientation using the registered near-Turan normal form. This is a structural refinement only; no Q32 closure is claimed.


### 8.12 T0 pointwise color-degree saturation

**V47_T0_POINTWISE_COLOR_SATURATION.md** adds an exact vertexwise ledger to the aligned z=0,1 cells. At each T0 vertex v, the eleven non-target colors have H-degrees all equal to 3 if epsilon_v=1; if epsilon_v=0, exactly one color has degree 4 and ten have degree 3. Thus \(\sum_C t_C=11-E_0\).

For each exact Type-I color C, a degree-four T0 vertex must lie in G11(C). The initial occupancy count gives the coarse bound t_C<=2, but the later placement-sensitive case split proves the global bound t_C<=1 for every exact color. This is a source-correct capacity restriction for future simultaneous color packing. It does not close the aligned cells; root status remains OPEN / NOT_CERTIFIED.


### 8.12 T0 pointwise color-degree saturation

**V47_T0_POINTWISE_COLOR_SATURATION.md** adds an exact vertexwise ledger to the aligned z=0,1 cells. At each T0 vertex v, the eleven non-target colors have H-degrees all equal to 3 if epsilon_v=1; if epsilon_v=0, exactly one color has degree 4 and ten have degree 3. Thus \(\sum_C t_C=11-E_0\).

For each exact Type-I color C, a degree-four T0 vertex must lie in G11(C). The placement-sensitive case split gives t_C<=1 globally, and the T0-pair surplus identity gives t_C<=g_C; hence t_C<=min(1,g_C). The residual K12-pair surplus is 26+E0. This is a source-correct capacity restriction for future simultaneous color packing. It does not close the aligned cells; root status remains OPEN / NOT_CERTIFIED.


### 14e. Conditional seven-vertex residual holonomy-cost theorem

Added `V47_Z01_RESIDUAL_HOLONOMY_COST.md` for the subcase where all ten isolated K5 components are single-outside. There the seven-vertex residual has profile (2,2,2,1), a nine-edge baseline, and 64 matching-compatible baseline classes. The minimum costs 0,1,2,3 correspond to aligned/aligned, aligned/mixed, six-cycle-alpha-3, and six-cycle-alpha-4 classes. This local table is conditional and must not be used for isolated-double placements, which have a separate eight-vertex residual audit.


### Minimum-repair edge patterns for classes C and D

The holonomy verifier checks the exact minimum repairs. Class C has three independent triples: two share a pair of large-track vertices, and the third is a disjoint transversal triple. Each minimum two-edge repair includes the shared-pair edge and one edge within the disjoint triple. Class D has a unique independent 4-set T0 plus a transversal triple V; the baseline T0 edges attach to the complementary triple U. Each minimum three-edge repair consists of one edge within U, one T0-to-V edge, and the edge between the other two vertices of V. These are local constraints only.

### 14f. Conditional seven-vertex residual graph catalog

Added `V47_Z01_EXACT_COLOR_RESIDUAL_GRAPH_CATALOG.md` and its verifier for the all-isolated-single-outside subcase only. The 7-vertex necessary relaxation has profile (2,2,2,1), e=9+g_C, alpha at most 2, and corrected counts 8,72,360,1,000 at gaps 0,1,2,3. The source-correct isolated-double branch instead has an 8-vertex G11 residual; see `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md`. Neither catalog closes the aligned cells.

### 14g. Isolated-double residual branch and catalog scope correction

The seven-vertex residual catalog and 64-class holonomy theorem are conditional on all ten isolated Type-I K5 components being single-outside. The source-correct 69-edge placement registered in HIGH_SUPPORT_NEAR_TURAN.md, Section 3, has one double-outside isolated component, so its residual accounting is different: the isolated H-subgraph is 9K4 plus K3 (57 edges), while G11 contributes an 8-vertex residual of profile (2,2,2,2) with 12+g_C edges.

This correction is documented in V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md and checked by verify_v47_z01_isolated_double_residual.py. In the low-gap isolated-double subcases, the residual contains two disjoint transversal K4s; the exceptional x_C in H, y in H placement has g_C=3. The global g=0,1 alignment result is still supplied by the independent 69/70 near-Turan classification, not by applying the 7-vertex holonomy table to every color. No dependency to a Q32 UNSAT certificate is created.


### 14g. Conditional scope and T0-cap correction for residual enumerators

The seven-vertex residual catalog and holonomy-cost theorem apply only when all ten isolated Type-I K5s are single-outside. `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` handles the separate source-correct isolated-double branch: nine isolated H-K4s, one isolated H-K3, and an eight-vertex gadget residual with profile (2,2,2,2). The two local enumerators must not be used as a universal Type-I reduction.

Within the seven-vertex branch, the residual T0 singleton has three baseline C-edges. The pointwise degree saturation caps its C-degree at four, hence at most one surplus C-edge may touch T0 across all three T0--Ti pairs. The verifiers now enforce this cap. Corrected graph counts by gap are 8,72,360,1000; K4+K3-base counts 8,72,264,520; non-base counts 0,0,96,480. Corrected holonomy repair counts are A=(8,72,264,520) at gaps 0–3, B=(24,216,696) at gaps 1–3, C=(72,720) at gaps 2–3, D=72 at gap 3. The minimum repair costs and class-C/D forced-edge patterns survive the cap. The placement-sensitive Type-I case split proves the global exact-color bound t_C<=1. In the exceptional isolated-double x_C in H, y in H two-double branch, x_C and y cannot be in T0 (a single T0 endpoint creates a forbidden same-track edge; both in T0 would force degrees 3+(3-k) and 3+k, both <=4, which is impossible). Thus the T0 vertex in the special K3 has degree 3 and the T0 vertex in the special K4 has degree 4; g_C=3 but t_C=1. Therefore the total one-extra-edge cap across all three T0--Ti pairs is global for exact colors, and t_D>=max(0,1-E0) for the nonexact color.

### 14h. T0-capped isolated-double two-K4 residual enumeration

`V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` now incorporates the global exact-color bound t_C<=1 in the two-K4 residual subcases. At most one of the 12 cross-K4 extra edges may be T0-incident in total; six edges are T0-incident and six join large tracks. The exact per-base counts for gaps 0,1,2,3 are 1,12,51,110, yielding 8,96,408,880 across eight unordered bases. This supersedes the per-T0-vertex-cap counts 8,96,480,1312 and the uncapped counts 8,96,528,1760. If the source-derived extra-edge star is centered at a T0 vertex, g_C<=1. These remain necessary local counts, not a full Q32 certificate.

### 14i. Narrow exclusion in isolated-double exceptional geometry

Section 3.3 of `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` excludes only the subcase `x_C,y in T0`: both centers have three C-neighbors in H and T0 pointwise saturation permits at most one additional C-edge per center, but three gadget edges must be assigned to them. An attempted extension to centers in a large track was retracted: the cross-track degree of a large-track vertex is one in total, not one per other track, so that argument does not apply. The large-track-centered exceptional case remains OPEN.

### 14i. Placement-sensitive T0 repeat-owner cap

V47_T0_POINTWISE_COLOR_SATURATION.md now proves the global exact-color bound \(t_C\le1\). The all-isolated-single and isolated-double two-K4 branches follow from residual support and star-edge geometry. In the exceptional isolated-double two-double case \(x_C\in H,y\in H\), the pointwise cap rules out either x_C or y alone in T0, and rules out both in T0 because their degrees would be \(3+(3-k)\) and \(3+k\) for \(k=|A_0\cap H|\). Thus the two T0 vertices lie in the special K3 and K4, with degrees 3 and 4 respectively; here \(g_C=3\) but \(t_C=1\). Consequently the one-extra-edge cap across all three T0--Ti pairs is global for exact colors. The updated arithmetic/source-interface verifier checks the case-split arithmetic. Combined with the no-low-gap alternative g_D<=17, the bound t_C<=1 yields at least 10+k exact-color surplus edges on the three K12--K12 pairs, where k exact colors have gap 3; the nonexact color has at most 16+E0-k such edges. This is a placement restriction and budget cut, not a contradiction.


### 14j. Holonomy-class surplus-location constraints

The capped holonomy verifier now checks the exact distribution of surplus edges between the three T0--Ti pairs and the three K12--K12 pairs. At minimum cost, class B (g_C=1) requires its only surplus on a T0--Ti pair; class C (g_C=2) has both surplus edges on large-track pairs; class D (g_C=3) has one T0 surplus and two large-track surpluses. Full counts by class, gap, and split are in `V47_Z01_RESIDUAL_HOLONOMY_COST.md`. These are conditional single-outside constraints.

### 14k. Aggregate exact-color large-pair surplus lower bound

Section 6 of `V47_T0_POINTWISE_COLOR_SATURATION.md` derives `L_exact=26+E0-(g_D-t_D)` for the total exact-color surplus on the three K12--K12 pairs. Since `g_D<=19` and `t_D>=max(0,1-E0)`, the lower bounds for `E0=0,1,2,3` are respectively 8,8,9,10. This gives a global necessary budget to combine with local holonomy surplus-location constraints; it does not close Q32.

The large-pair budget also has the conditional form `L_exact>=27-g_D`, because the ten exact colors contribute at most 10 T0 surpluses. Combined with the E0 bound, `L_exact>=max(27-g_D,8,7+E0)`. This is most restrictive when g_D is small (e.g. g_D=7 forces L_exact>=20).

### 14l. Shared residual-factor packing and aggregate feasibility witness

`V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md`, Section 7, records the common factor theorem: after choosing Hall matchings, each large-pair complement P_ij is a perfect matching containing all H edges. The repeated-color graph S=P\\H over the three large-pair factors has `d_S(v)=2-d_H^large(v)<=2` and `|S|=26+E0`. Each edge has a unique repeat-color owner; exact-color-owned edges must have endpoints in the owner's Type-I residual set.

`verify_v47_z01_aggregate_budget_witness.py` independently verifies that scalar capacities and local pattern counts admit a relaxed witness (E0=0, E_i=2, e_H=(4,3,3), ten exact gaps of 2, g_D=17). This is not a graph completion; it establishes that aggregate budget inequalities cannot close the branch. The next dependency is the vertex-labelled packing of exact-color residual sets into the common S graph, while preserving the separate single-outside and isolated-double source modes. Q32 remains OPEN / NOT_CERTIFIED.

### 14j. Mode-sensitive pair-location constraints; correction to the prior retraction

The purported counterexample to the Class-B complement law used the wrong baseline. For \(x_C\in O\), \(N_s\) single-outside and \(N_t\) double-outside, the actual source baseline is the K4 H-part of \(N_s\) plus the K3 H-part of \(N_t\), which is Class A. The edges \(yw\) and \(ys_j\) are the two extras; \(ws_i\) is already a K4 baseline edge. Hence Class A legitimately permits a T0 repeat on \(T_0T_i\) and a large-pair repeat on \(T_iT_j\), sharing track \(i\).

The Class-B-specific law remains: in the seven-vertex Class-B mode, \(x_C\in T_0\), both special K5s are double-outside, \(y\in H\), and for \(g_C=2,t_C=1\) the T0 repeat is on \(T_0T_k\) while the large-pair repeat is on \(T_iT_j\), with \(\{i,j,k\}=\{1,2,3\}\). The aggregate witness uses Class-A source patterns (exact surplus \((7,0,3;4,3,3)\), D surplus \((1,9,6;0,1,0)\), \(g_D=17\)); it remains only scalar/locally realizable feasibility, not a vertex-labelled common-P completion.
