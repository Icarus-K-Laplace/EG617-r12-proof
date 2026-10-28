# E408 Q32 high-support + root-audit canonical state

Updated: 2026-10-28
Branch: `workstream/r12-q32-highsupport-root-20261028`
Write scope: `r12_master/workstreams/q32-highsupport-root-chat-20261028/`

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Unique currently identified live root graph gate: **E408 / h13 / Qmax=32 / e(H)=285 / excess6**.

This workstream does not modify the sibling branch `workstream/r12-q32-caseII-v44-final-20261028`. Its latest canonical/dependency audit closes the full `|U|=44` support layer for m=8,9,10; this is a read-only import pending final root consolidation.

## Live Q32 contract

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- `sum_H(d_H-12)=6`;
- exact-color count `m in {8,9,10}`;
- source-correct exact Type-I factorization `10K5 dot-union G11`;
- no universal degree-nine exceptional vertex;
- every exact color has at least ten disjoint core K4 witnesses;
- witness union `U` has `|U|>=44`;
- for `W=H\U`, corrected multiplicity `n_w>=m-6`;
- latest nonexact pointwise floors:
  `L8=12`, `L9=7`, `L10=3`.

## Case I

- v=44 CLOSED;
- v=45 CLOSED;
- v=46,m=10 CLOSED;
- v=46,m=9 CLOSED;
- v=46,m=8 CLOSED by the 130-edge minimum-degree-four theorem;
- v=47 OPEN.

Hence Case I now has only v=47.

## Case II in this workstream

### v=45
- m=8: **CLOSED** by source-correct weighted special-incidence capacity;
- m=9: **CLOSED** by `Q32_130_NO_CORE_ONLY_DEG4.md`. The rigid shell count forces a core-only degree-four vertex in the 130-edge color at each W-point, which the direct local theorem forbids;
- m=10: **CLOSED** by the universal zero-shell multiplicity bound.

### v=46
- m=8: **CLOSED** by the same three-unit surplus contradiction;
- m=9: **CLOSED** by `Q32_130_NO_CORE_ONLY_DEG4.md`. The rigid shell count forces a core-only degree-four vertex in the 130-edge color at the unique W-point, which the direct local theorem forbids;
- m=10: **CLOSED** by the universal zero-shell multiplicity bound.

### v=47
Full support `U=H`, so W is empty. All m remain OPEN; the non-full-support zero-shell theorem does not apply.
 
## New direct closure of v45/v46 m=9 (2026-10-28)

`Q32_130_NO_CORE_ONLY_DEG4.md` proves that a 130-edge color cannot have even one core vertex of degree four with all four color-neighbors in H. The v45 and v46 m=9 zero-shell normal forms each force exactly such a vertex: the 130-edge color has degree four at W, no A-neighbor, and cannot own pw because the unique zero-shell special exact color owns pw.

Therefore Case-II v45,m=9 and v46,m=9 are now CLOSED. Together with the existing m=8/m=10 closures and the sibling v44 closure, **all non-full-support rows v=44,45,46 are closed for m=8,9,10**. Only full support v=47 remains in Q32.

This direct contradiction supersedes the older v45 pair-rigidity/e_H(W)=0 route. The new closure does not rely on that previously retracted inference.

## v=47 proved reductions

For an exact color C let

`g_C=e_C(H)-69`.

Source-correct Type-I placement gives

`0<=g_C<=6`.

More precisely:

- `x in O`: outside-count profile `(2,1^11)`, eleven witnesses, `69<=e_C(H)<=73`;
- `x in H`, two-double: `(2,2,1^10)`, ten witnesses, `69<=e_C(H)<=74`;
- `x in H`, triple: `(3,1^11)`, eleven witnesses, `69<=e_C(H)<=75`.

All eleven non-target colors partition `bar H`, so

`sum_C g_C = 37`.

The 69-edge layer is genuinely source-feasible for a single exact color; therefore a false universal strict reserve `e_C(H)>=70` must not be used.

The 69/70 layers have the rigid `4^11,3` near-Turan normal form. At 70 edges there is exactly one cross-part color edge, so every monochromatic K4 still lies in one of the eleven four-parts.

For exact colors, with `mu_C=e_C(A)`, the valid tradeoff is

- x in H: `g_C<=mu_C+2`;
- x in O: `g_C<=mu_C+1`.

Every exact color pays at least two M-edges; x-in-H triple type pays at least three.

## m=8 source-correct rigidity

At every residual point z,

`(d_F(z)-13) + sum_non-target(d_C(z)-4) = 3`.

For every exact Type-I color this forces

`a in {2,3}`.

The two variable gadget surplus weights are therefore `{2,3}`. No residual point can be variable for two exact colors, so all sixteen points

`{x_C,y_C : C exact}`

are pairwise distinct.

This is the mechanism closing the v45/v46 Case-II m=8 rows.

## Root audit

Current source-safe chain:

- contextual R449: closed relative to named input;
- h12: closed;
- E397--E406: closed;
- E407 Q31: replay-backed conditional closure;
- E407 Q32: the 29-point U-reserve contradiction is valid under the frozen V12 support contract; parent-level use remains conditional on V12 exhaustiveness and branch-state reconciliation;
- E408 Q31: replay-backed conditional closure;
- E408 Q33: the 31-point/56-witness nonexact-U-reserve contradiction is valid under that contract; exhaustive support-lifting source was not located in this pass;
- E408 Q32: OPEN.

The old root promotion based on Q32 degree-nine/injectivity is withdrawn.

## Immediate mathematical frontier

1. Full-support v=47 for m=8,9,10: combine the exact 37-unit gap ledger, exact Type-I placement normal forms, pivot-neighborhood K4 packing, shell-edge ownership, and pointwise degree/excess-six constraints.
2. Root dependency reconciliation: keep E407 Q32 conditional on V12 exhaustiveness and E408 Q33 conditional on the 31-point/56-witness support-lifting contract until exact upstream source links are reconciled.

No root promotion before all of these plus sibling v44 are closed and replayed.

## New pivot-neighborhood packing result (2026-10-28)

`V47_PIVOT_NEIGHBORHOOD_PACKING.md` proves that each exact color has a pivot-neighborhood K4, and these m K4s are vertex-disjoint across exact colors. With Q their union and R=H\\Q:

- e_H(Q) >= 4*C(m,2);
- e_H(Q,R) >= m|R|;
- e_H(R) >= p_4(|R|);
- the three floors sum to 253 for m=8,9,10;
- if x,y,z are the respective edge slacks, x+y+z=32;
- the six-unit core-excess ledger gives 2x+y>=5m, y+2z>=D_m with D=(18,13,8), and x>=8,13,18 for m=8,9,10.

`verify_v47_pivot_packing.py` returned `V47_PIVOT_PACKING_ARITHMETIC_OK` and found 79,61,44 feasible scalar slack states. Thus this is a structural reduction, not a scalar UNSAT certificate.

## Root-audit caveat

The root DAG now distinguishes local U-reserve contradictions from parent-level exhaustiveness. E407 Q32 remains conditional on the frozen V12 29-point contract; Q33 remains conditional on the 31-point/56-witness support contract until the exact upstream exhaustive support-lifting theorem is linked. Neither caveat changes the headline: EG617(r=12) remains OPEN / NOT_CERTIFIED.
## Zero-shell multiplicity upgrade (2026-10-28)

For any nonempty W, the source-correct zero-shell lemma says at most one exact color special at w can have zero shell-A degree, because each such color must own the unique edge pw. Non-special exact colors use at least two of the thirteen w--A edges each. Let `t_w` be the number of target-colored edges from w to A. Reserving them explicitly gives `n_w>=2m-14+t_w`.

Together with the pointwise budgets `n_w<=r_m=(3,4,5)`, this closes m=10 for every non-full-support Q32 branch and sharpens m=9 to `n_w=4`, all `a=4`. The refined bound forces `t_w=0`, so each m=9 W-point has core excess1; shell ownership is exactly ten edges from the five non-special exact colors plus three from the special exact colors. The detailed proof is recorded in `V45_SOURCE_CORRECT_MULTIPLICITY.md` and `V46_CASEII_CLOSURE.md`.

`verify_zero_shell_multiplicity.py` returned `ZERO_SHELL_MULTIPLICITY_ARITHMETIC_OK`; it checks the multiplicity budgets and m=9 shell saturation only, not the graph lemma.

## New local 130-color degree-four audit (2026-10-28)

Added `V45_M9_130_COLOR_DEGREE4_LOCAL_STRUCTURE.md`. For a 130-edge nonexact color D and a vertex v of degree4, the 56-point non-neighborhood has at least119 D-edges by the source-checked KP second-Turan bound at (56,11). The neighborhood S has either 5 edges with exactly2 S-to-N edges, or 6 edges with 0 or1 S-to-N edges. This local classification does not force the v45 W-pair edge; the earlier unsupported pair-rigidity inference is withdrawn. The same file now also proves the stronger no-core-only degree-four theorem: if all four neighbors lie in H, the local K4-e equality pattern makes a neighbor itself have a triangle-plus-isolate neighborhood, contradicting the same KP lower bound. Thus v45,m9 can be closed by the core-only obstruction, independently of the unresolved W-pair edge. The arithmetic verifier returned `130_COLOR_DEG4_LEDGER_OK`.

## New v47 residual incidence-cover lemma

Added `V47_RESIDUAL_INCIDENCE_COVER.md`: for every independent k-set S in R, k<=4, and every pivot block Q_i, the union of H-neighborhoods from S into Q_i has size at least k. If a block has zero cross-edge slack (every r has exactly one neighbor in Q_i), its neighbor map partitions R into at most four cliques. For m=10, z<=5 forces an independent triple in R, activating the triple-cover constraint; z=6,7 remains a separate high-z cell. No v47 closure is claimed.

## 132-edge minimum-degree upgrade (2026-10-28)

`Q32_132_MINDEG3.md` proves `delta(D)>=3` for the unique132-edge nonexact color by excluding degrees0,1,2 with the (60,59,58)-point second-Turan bounds and the Kang–Pikhurko equality classification at (58,11). Therefore `L_10=3) and the pointwise surplus budget becomes `r_10=4), improving the full-support gadget quota to `q_z<=4). This strengthens the existing non-full-support m=10 contradictions but does not itself close full support v47.

### v=47, m=10 high-chromatic residual subcase CLOSED

From `V47_RESIDUAL_INCIDENCE_COVER.md`, if `chi(bar(H[R]))>=5`, the residual is forced to `H[R]=C5 dot-union 2K1`, and the scalar ledger forces `(x,y,z)=(20,10,2)` with one extra Q-R incidence in each of the ten blocks. Both isolated residual vertices need at least two such incidences, but Lemma 7.1 proves no block's extra-incidence vertex can be either isolated vertex: the C5 nonedge-pair labels force its two-neighbor set to contain three distinct Q_i labels. Contradiction.

Therefore the remaining v=47,m=10 branch has `chi(bar(H[R]))<=4`, equivalently R admits a partition into at most four cliques. The full m=10 branch remains OPEN.

## New m=10 light-block graph reduction (2026-10-28)

Added `V47_LIGHT_BLOCK_GRAPH_DISCONNECTED_REDUCTION.md`. On the ten pivot blocks, define L by `e_H(Q_i,Q_j)=4`. With block excesses `s_i=t_i+y_i-5`, one has `s_i>=0` and `sum s_i=2x+y-50<=6`. If L is disconnected, it has exactly two components, of sizes 1+9, 2+8, 3+7, 4+6, or 5+5.

The 2+8 and 3+7 cases saturate all six Q-excess units, force `s_R=0`, and force every cross pair to have exactly five H-edges. The 2+8 case has `x_T=8+z, y=8-2z, z<=4`; the 3+7 case has `x_T=3+z, y=8-2z, z<=4`. In both, every block in the large component has weighted internal-heavy degree at most3 or2, respectively, and degree at least4 in its light graph.

For 4+6, `y+2z<=10`, `z<=5`, and at most two units remain for internal-heavy weight, cross-pair multiplicity beyond one, and shell-incidence slack on the four-block component. For 5+5, `x>=25, y+z<=7, z>=1`, with at most three weighted extra units beyond the mandatory cross-pair baseline. This is a finite structural split, not an UNSAT certificate.


## New zero-slack map alignment and transversal blocker (2026-10-28)

Added `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md` and `verify_v47_three_small_block_transversal.py`.

For the disconnected m=10 light-block components 2+8 and 3+7, every small-component block has y_i=0. The new zero-slack alignment lemma proves that if A,B are small light blocks, then after aligning their perfect matching, the unique residual-neighbor maps coincide: f_A(r)=f_B(r) for every r in R. The proof uses alpha(H)<=4 to force equality of the unordered label pairs for every independent pair r,s in R, then Delta(H[R])<=2 to find two suitably nonadjacent witnesses for each r. In the 3+7 light triangle, triangle matching consistency aligns all three maps, so every residual vertex has a matched neighbor pair/triple across the small component.

For each outer block D in the 3+7 cell, the 4,5,5 switch classification gives every q in D a common neighbor track across A,B,C. If the common track intersection is a singleton {h}, a Hall argument gives an independent transversal on the other three labels, forcing q adjacent to the entire residual fiber F_h; hence k(q)<=3-|F_h|, where k(q) counts q's incidences among the three extra edges from D to A,B,C. If the intersection has size two, q consumes all three extra edges, has no R-neighbor, and has no other extra Q-Q incidence. Per block, sum_q k(q)=3.

The normalized local verifier checked 1,728 aligned configurations plus 36 synchronized-switch configurations, or 7,056 vertex records. It returned `V47_ZERO_SLACK_TRANSVERSAL_LOCAL_OK` (7,044 singleton-track records, 12 double-track records). This verifies the local label/transversal classification only, not global Q32 infeasibility.

No full-support row is closed by this result. v47,m=8,9 remain open; v47,m=10 remains open in the chi(complement residual)<=4 cell. EG617(r=12) remains OPEN / NOT_CERTIFIED.


### Exact small-block endpoint-load refinement

The zero-slack alignment file now also records `e_i(h)), the number of outer extra-edge endpoints at label h in a small block. In either 2+8 or 3+7, `d_H(q_h)=9+e_i(h)+n_h), so `e_i(h)>=3-n_h). The exact endpoint slack is `sum_h(e_i(h)-(3-n_h))=3) for 2+8 and 2 for 3+7. The only possible sorted fiber-size partitions are `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, and `(2,2,2,1)`.

In a 3+7 switch block, all three extra endpoints have the same small-block label s; the duplicated common track is s and has `n_s<=1). If `n_s=1), that residual vertex gets one extra Q-R incidence in every such switch block, so the number of switches using s is at most `2-d_R(r_s)). These are further necessary constraints, not a global closure.


## New two-light matching composition theorem (2026-10-28)

Added `V47_TWO_LIGHT_MATCHING_COMPOSITION.md` and `verify_two_light_matching_composition.py`.

For three independent 4-sets A,B,C with alpha<=4, if A-C and B-C each consist of exactly four matching edges and e(A,B)<=7, then the composed A-B matching must be contained in H[A,B]. The analytic proof uses a missing-diagonal contradiction and the seven-edge cap. Exact enumeration checked all 25,636 possible A-B edge sets of sizes 4..7; the alpha<=4 counts are 1,12,66,220, exactly all edge sets containing the composed matching. The verifier returned `V47_TWO_LIGHT_MATCHING_COMPOSITION_EXHAUSTIVE_OK`.

In the m=10 disconnected 2+8 and 3+7 cells, every outer pair has at most seven edges, so matching composition applies along each actual length-two light path. The 2+8 outer light graph has eight vertices and minimum degree at least 3; the 3+7 outer light graph has seven vertices and minimum degree at least 4. Only in 3+7 does every nonadjacent pair necessarily have common light neighbors. A five-edge pair forces a unique composition; six-/seven-edge pairs support at most two perfect matchings. Matching disagreements are charged to pairs with at least six edges, at most six in 2+8 and at most three in 3+7.

This is a new matching-holonomy restriction to combine with the zero-slack residual-neighbor map and the residual path/cycle types. It does not close the 2+8 or 3+7 cells. Full-support v47,m=8,9,10 remains open; EG617(r=12) remains OPEN / NOT_CERTIFIED.


### Matching-holonomy scope correction (2026-10-28)

The correct light-graph degree bounds are: 2+8 has eight outer blocks and minimum light degree at least 3; 3+7 has seven outer blocks and minimum light degree at least 4. Therefore the statement that every nonadjacent pair has a common light neighbor applies only to 3+7. In 2+8, the matching-composition theorem is used only on length-two light paths that actually exist. The local theorem and its finite verification remain valid; only this application scope is corrected.


## New four-light-cycle holonomy theorem (2026-10-28)

Added `V47_LIGHT_CYCLE_HOLONOMY.md` and `verify_v47_light_cycle_holonomy.py`.

For a four-cycle of light pivot-block pairs, the two diagonals contain both path-composed matchings by the two-light composition theorem. With at most seven edges per diagonal, holonomy cannot be a derangement (would require eight edges); a 3-cycle gives a forced normalized 16-vertex graph with an independent 5-set. Thus only identity or transposition holonomy is possible. A transposition requires both diagonals to have at least six edges.

Exact local regression: 726 transposition/diagonal-extra configurations checked, 8 forced 3-cycle configurations rejected, result `V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK`.

For the 3+7 disconnected cell, every six-edge outer pair consumes the full internal-heavy budget of two at each endpoint, so its endpoints have no other internal-heavy incidences. Nontrivial four-cycle holonomy is therefore supported only on two disjoint high-weight diagonal pairs. This is a local structural restriction, not a Q32 closure.


## New 3+7 global light-holonomy rigidity (2026-10-28)

Added `V47_37_OUTER_LIGHT_HOLONOMY.md` and `verify_v47_37_light_graph_cycles.py`.

In the m=10 disconnected 3+7 cell, the outer light graph has seven vertices, minimum degree four, weighted heavy degree at most two, and total heavy weight `x_T=3+z<=7`. Using triangle matching consistency, the four-light-cycle theorem, and the heavy-degree cap, every light cycle has identity holonomy:
- a transposition four-cycle would saturate both diagonals and leave a common light hub, forcing identity;
- a chordless five-cycle likewise has a common light hub;
- every six-/seven-cycle has a chord and reduces inductively.

Therefore all outer light-edge matchings globally align. Every heavy pair has at least three common light neighbors, so the two-light composition theorem forces the same matching into that pair too. The 28 outer-block vertices consequently contain four aligned K7 tracks, with at most seven additional cross-track edges.

The exact weighted graph verifier checked 22,054 heavy graphs and 5,803,387 light cycles, returning `V47_37_LIGHT_GRAPH_CYCLE_DECOMPOSITION_OK`. This is a stronger normal form for the 3+7 subcase, not a contradiction. Full-support m=10 remains OPEN; m=8 and m=9 remain OPEN; EG617(r=12) remains OPEN / NOT_CERTIFIED.


## New 2+8 outer-vertex blocker and corrected double-track exception (2026-10-28)

Added `V47_TWO_BLOCK_TRANSVERSAL_BLOCKER.md`. In the disconnected m=10 2+8 cell, for each outer vertex q the two five-edge pair-neighborhoods into the small blocks A,B have nonempty common-track intersection I(q).

- If I(q)={h}, then q must be adjacent to every residual vertex in the fiber F_h. Hence `d_R(q)>=n_h` and `k(q)<=3-n_h).
- If I(q)={h,j}, q uses both extra A/B edges, so `k(q)=2` and `d_R(q)<=1). The correct sharp consequence is: if `d_R(q)=0), then `n_h+n_j<=3); if `d_R(q)=1), the same bound holds except for the explicit case `{n_h,n_j}={1,3}) where the unique R-neighbor is the singleton-fiber vertex. This exception is retained rather than overclaimed away.
- Each outer block has `sum_q k(q)=2); each small block has endpoint loads `e_i(h)=3-n_h+u_i(h)), `sum_h u_i(h)=3), so `e_i(h)<=6-n_h). Synchronized switch blocks with extra endpoint label h are bounded in number by `6-n_h).

Also strengthened the 3+7 double-track blocker in `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md`: its vertex has no R-neighbors, so the two track fibers must be completely joined in H[R], forcing `n_h+n_j<=3). These are local structural constraints only. Full-support v47,m=8,9,10 remains OPEN / NOT_CERTIFIED.


## New 3+7 residual-track transversal theorem (2026-10-28)

Added `V47_37_RESIDUAL_TRACK_TRANSVERSAL.md` and `verify_v47_37_residual_track_transversal.py`.

The preceding global holonomy theorem gives four aligned K7 tracks on the 28 outer vertices, with at most seven cross-track edges and maximum cross-track degree at most two. For each residual vertex r, `d_R(r)+b_r=2), so it has at most nine neighbors among the 28 outer vertices and at least 19 nonneighbors. If every track had a nonneighbor, the four nonneighbor-part sizes would be in `{1,...,7}` and sum to at least19.

A strict union bound proves an independent transversal exists for any four such parts with at most seven cross-part edges and maximum degree two. The exact integer verifier checks all 64 sorted part-size profiles and all relaxed edge-count allocations under total-edge and part-degree caps. The worst profile is `(7,7,4,1)`: 196 transversals, at most133 forbidden, margin63. It returned `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`.

Therefore every residual vertex is adjacent to all seven vertices of at least one outer K7 track, extending that track to a K8. At least five of the seven outer-block neighbors lie in that same track as unique neighbors; if `d_R(r)=2`, all seven do. This is a stronger necessary condition, not a contradiction. Full-support m=10 remains OPEN, as do m=8 and m=9.


## 3+7 double-track residual edge floor (2026-10-28)

Strengthened `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md`. In 3+7, a double-track outer vertex has `d_R=0), so its two track fibers must be completely joined in H[R]. Therefore
`e(H[R]) >= sum_h binom(n_h,2) + n_h*n_j`,
and since `e(H[R])=3+z), the four fiber-size patterns give:
- (3,3,1,0): allowed track-size pair (3,0) or (1,0), requiring z>=3;
- (3,2,2,0): (3,0) or (2,0), requiring z>=2;
- (3,2,1,1): (2,1) requires z>=3; (1,1) requires z>=2;
- (2,2,2,1): (2,1), requiring z>=2.

Hence **z<=1 rules out all double-track vertices** in the 3+7 cell. Added `verify_v47_3plus7_double_track_edge_floor.py`; executed arithmetic regression returned `V47_3PLUS7_DOUBLE_TRACK_EDGE_FLOOR_OK`. This is a necessary local condition only; 3+7 remains OPEN.


### Further 3+7 residual partition rigidity

The same file now proves that the complete outer track assigned to each residual vertex is unique and that any two residual vertices assigned to the same track must be adjacent. If two such vertices were nonadjacent, each of the other three tracks would contain at least three vertices nonadjacent to both; a three-part union bound (at most seven cross-track edges, each blocking at most the largest part size, while the transversal count is at least nine times that size) yields an independent transversal. Adding the two residual vertices would create an independent 5-set.

Thus the track assignment partitions R into four clique fibers of size at most three. The only sorted profiles are `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, and `(2,2,2,1)`, matching the four possible profiles of the common small-block map. The verifier now checks all 35 sorted three-part profiles in addition to the 64 four-part profiles and retains `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`.

The two clique partitions have not yet been proved identical; the 3+7 cell remains OPEN.


## 3+7 switch duplicate-fiber budget and z=4 escape classification

For a synchronized transposition switch, the common-track intersections have one singleton label s duplicated and one label missing. Both vertices with intersection {s} hit all of F_s, so the outer block's residual-incidence slack obeys `n_s<=y_D). Hence in 3+7, where `y_D<=2), a switch cannot duplicate a size-three fiber; when z=4, `y_D=0) and the duplicated fiber must be empty.

Added `V47_Z4_EMPTY_FIBER_ESCAPE_CLASSIFICATION.md`. In the 3+7,z=4 cell with fiber sizes (3,2,2,0), the all-aligned/singleton-track configuration is impossible: the empty-label endpoint floor gives at least nine small-to-outer endpoints, none of which can land at the empty-track vertex in an aligned block. Since there are only seven units of total outer-heavy weight, the empty-track vertices cannot fill their 21 units of degree surplus. Therefore every completion of this cell must contain at least one switch or double-track block involving the empty label. This is still a necessary local reduction, not a closure.


## Double-track alpha(R) blocker (3+7, m=10)

Added `V47_DOUBLE_TRACK_ALPHA_BLOCKER.md` and `verify_v47_double_track_alpha_pruning.py`. Any 3+7 double-track vertex has no R-neighbors, so it immediately forces `alpha(H[R])<=3). The registered 18 residual path/cycle types then prune double-track configurations to:
- z=2: only `C3 dot-union 2P2`;
- z=3: only `2C3 dot-union K1`, `C3 dot-union P4`, `C5 dot-union P2`;
- z=4: only `C7`, `C3 dot-union C4`;
- z=0,1: no double tracks.

The residual-type alpha arithmetic was executed and returned `V47_DOUBLE_TRACK_ALPHA_PRUNING_OK`. Combined with the double-track fiber-size cap and switch duplicate-fiber budget, this further narrows 3+7; it does not close the terminal.


## New 3+7 small-to-outer matching rigidity (2026-10-28)

Added `V47_37_SMALL_OUTER_MATCHING_RIGIDITY.md` and `verify_v47_37_matching_cut_bound.py`.

For each small block A,B,C and each outer block D, the 5-edge pair has a unique perfect-matching permutation to the globally aligned outer tracks. Across a light outer edge DE, the 4,5,5 switch theorem says that if this permutation changes at label s, both endpoint blocks D,E must place their A-D/A-E extra edge at the same small vertex A_s. Thus all vertices on the cut of the partition by matching-image p_D(s) are charged to e_A(s).

Any nontrivial cut in a seven-vertex graph of minimum degree four has at least five crossing-edge endpoints. For every nonempty residual fiber, the small-block degree ledger gives e_A(s)<=5-n_s<=4, so p_D(s) is constant across all seven outer blocks. Since at most one fiber is empty, three permutation coordinates are constant and the fourth is forced. The same proof applies to B and C.

Therefore the three small blocks each have a fixed matching permutation to the outer tracks, independent of the outer block. The global type is either all three permutations equal, or exactly one differs from the other two by a fixed transposition. In the transposition regime, every outer block's three extra-edge endpoints share a moved label s_D with n_{s_D}<=1; both moved labels must have fiber size at most one. This restricts that regime to residual profiles `(3,3,1,0)` or `(3,2,1,1)`.

The cut verifier checks all 63 distinct nontrivial cuts by size and returns `V47_37_MATCHING_CUT_BOUND_OK`. This is a global matching normal form, not closure of the 3+7 cell.
