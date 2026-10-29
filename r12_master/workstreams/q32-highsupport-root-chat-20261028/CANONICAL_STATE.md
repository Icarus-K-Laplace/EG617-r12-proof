# E408 Q32 high-support + root-audit canonical state

Updated: 2026-10-29
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


## RETRACTION: small-to-outer matching rigidity (2026-10-29)

The earlier section claiming global constancy of the small-to-outer matching permutations is **RETRACTED**. Audit file: `V47_37_SMALL_OUTER_MATCHING_RIGIDITY_RETRACTION.md`; the original proof file is now marked RETRACTED.

The 4,5,5 switch theorem's two extra edges hit the two distinct moved small-side labels, not one common small label. Thus the former cut-endpoint charging to one set S_s was invalid, and neither global constancy of p_D nor the resulting matching-type dichotomy is established. `verify_v47_37_matching_cut_bound.py` certifies only the cut-endpoint lower bound.

The small-block degree ledger remains valid: `epsilon_s=e_A(s)+n_s-3>=0`, `sum epsilon_s=2`, `e_A(s)=3-n_s+epsilon_s`, and `sum e_A(s)=7`. The separate `V47_Z01_TRACK_ALIGNMENT.md` proof is not based on the retracted cut-charge argument and remains separately scoped.

## New z=0,1 small/outer track alignment theorem (2026-10-28)

Added `V47_Z01_TRACK_ALIGNMENT.md`. In the 3+7 m=10 cell, z=0,1 have `alpha(H[R])=4), hence no double-track vertices. Let F_s be the common small-triangle map fibers and G_g the unique complete outer-K7-track fibers. For every outer block D, the exact mismatch inequality is
`y_D >= sum_{q in D}|F_{s(q)} \\ G_{g(q)}|`,
because q is adjacent to both F_{s(q)} and G_{g(q)}, while `sum_{q in D}d_R(q)=7+y_D`.

For z=0, e(R)=3 forces H[R]=3K2 dot-union K1, whose partition into four clique fibers is unique, so F=G. For z=1, all four F and G fibers are nonempty. If their unlabelled partitions differed, every outer block (aligned or switch) would incur mismatch at least one, forcing `y>=7`; but y=6. Thus F=G. Once the partitions coincide, a synchronized switch is impossible: the q receiving two small-side extra edges is adjacent to both disjoint nonempty fibers F_s and F_j, so d_R(q)>=2, while its two extra Q-Q incidences force d_R(q)<=1. Therefore every outer block is aligned for z=0,1.

This eliminates all switch/double-track escape mechanisms in the two lowest residual-excess cells. It does not close the aligned z=0 or z=1 graph completions. Root remains OPEN / NOT_CERTIFIED.


## z=4 empty-fiber arithmetic replay restored (2026-10-28)

The referenced `verify_v47_z4_empty_fiber_escape.py` was absent at the start of this audit. Added the missing arithmetic-only replay script and executed the same 1,000 slack-profile check in-session. Result: `V47_Z4_EMPTY_FIBER_ESCAPE_ARITHMETIC_OK`; it verifies `E_0>=9), at most 12 nonzero-label endpoints, 21 required empty-track extra incidences, and the contradiction `9> x_T=7). The script explicitly does not certify the graph-theoretic premise or global Q32 UNSAT.


### z=1 triple-fiber subcase closed by balanced-coloring K13 (2026-10-28)

The z=0,1 alignment theorem plus the `(3,2,1,1)` fiber profile would create a fully aligned track with `10+3=13) vertices forming a target-color K13. This contradicts the original balanced-coloring premise that every 13-set contains every color (equivalently, each non-target color has alpha at most12). Thus z=1, profile (3,2,1,1), is CLOSED. Remaining low-z cells are z=0 profile (2,2,2,1) and z=1 profile (2,2,2,1) with one cross-fiber residual edge. More generally, any aligned 3+7 completion with a size-three residual fiber is impossible; this does not close z=2,3,4 where alignment is not established.


The retraction is backed by `verify_v47_37_switch_endpoint_counterexample.py`, which reconstructs the normalized 12-vertex switch witness and exhaustively checks its independence number: `alpha=4), 63 maximum independent sets, output `V47_37_SWITCH_ENDPOINT_COUNTEREXAMPLE_REPRODUCED`. This verifies the counterexample to the old inference, not any global Q32 conclusion.


## New balanced-coloring cross-track ledger for aligned z=0,1 (2026-10-29)

Added `V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md` and `verify_v47_z01_cross_track_ledger.py`.

After the independent z=0,1 alignment theorem, the target-color graph H is partitioned into cliques of sizes 12,12,12,11. The 13-set balanced-coloring premise implies that between any two K12 tracks, H-edges form a matching: for each outside vertex, its 12 edges into the K12 track must contain all eleven non-target colors, leaving at most one H-edge. For a K11--K12 pair, the same argument bounds the H-degree by one on the K11 side; no symmetric matching claim is made.

The within-track edge count is 253, so the 32 remaining H-edges are cross-track edges. The exact degree ledger gives:
- total H edges between the K11 track and the three K12 tracks: `22+E_0`;
- total H edges among the three K12 tracks: `10-E_0`;
- `E_0` is the sum of small-block degree-excess units on the singleton-fiber label and lies in `{0,1,2,3}`.

Thus 7–10 H edges lie among the three large tracks and 22–25 join the K11 track to a K12 track. The six track-pair deficits sum exactly to 37. The verifier enumerated all 729 small-block excess triples and found 28,107 feasible necessary aggregate track-count states; output `V47_Z01_CROSS_TRACK_ARITHMETIC_OK`. This is a sharper structural normal form, not a closure of z=0 or z=1.


## Aligned low-z Type-I component normal form (2026-10-29)

Added `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` and arithmetic replay `verify_v47_aligned_typei_component_normal_form.py`. In the surviving aligned z=0,1 profile (2,2,2,1), H partitions into three target K12 cliques and one target K11 clique. Balanced coloring implies every non-target color C has `d_C(v,H)>=2` at every H vertex and `d_C(v,H)>=3` on the K11 part.

The registered triple-outside K5 placement gives its two H vertices only one C-neighbor in H, so it is impossible in this cell. A double-outside K5 must use one H vertex from each of the three K12 parts and none from K11; every single-outside K5 uses one H vertex from each of the four parts. Therefore exact colors have only two remaining Type-I placement types: x_C in O with one double/nine single K5s, or x_C in H with two doubles/eight singles.

The gadget H-H edge count is tied exactly to the near-Turan gap:
- x_C in O: `e_C(H intersect G11)=12+g_C`, with `0<=g_C<=4`;
- x_C in H, two-double: `e_C(H intersect G11)=15+g_C`, with `0<=g_C<=5`.

The arithmetic verifier was executed and returned `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM_ARITHMETIC_OK`. This eliminates only the triple-placement row and sharpens the color-gap decomposition; the aligned z=0,1 cells remain OPEN.


The cross-track ledger now also has a color-repeat conservation lemma. On each K12--K12 pair, every unmatched vertex repeats exactly one non-target color among its 12 cross edges; for every color C, the surplus `e_C(T_i,T_j)-12` equals the number of repeat-C vertices on either side, so the repeat-color counts must match across both sides. On a K11--K12 pair, the analogous surplus over 11 counts repeated colors among unmatched vertices on the K11 side only. This is a color-level constraint for any future exact completion search, not a closure.


A further exact consequence is now recorded: each pair of the three K12 tracks has at most nine H-edges. For distinct large labels i,j,k,
`e_H(T_i,T_j)=y_k-2-E_0-E_k<=9-E_0-E_k`,
because `y_k<=11). Hence each K12--K12 pair has at least three unmatched vertices on each side, with a sharper deficit lower bound `12-e_H(T_i,T_j)>=3+E_0+E_k). The aggregate verifier now asserts these identities in every retained state.


## Type-I accounting correction — special K5s belong to G11 (2026-10-29)

**Correction / supersession:** the immediately preceding `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` revision incorrectly treated all twelve K5 factors as if they were ten isolated components plus two additional independent pieces. The actual Type-I factorization has twelve K5 factors: ten isolated K5 components plus the two special K5 cliques `N_s,N_t` inside the 11-point gadget G11. The previous claim that triple placement is impossible, and its fixed G11 H/O counts, are withdrawn.

The file and verifier have been corrected. The balanced-coloring degree floor remains valid: every non-target color has H-degree at least two at every vertex of a K12 track, and at least three at every vertex of the K11 track. Therefore a triple-outside K5 cannot be one of the ten isolated K5 components. In the registered triple placement it must be one of the special K5s; the other special K5 is single-outside, so `b_s+b_t=4` and G11 has four O vertices and seven H vertices. This is a necessary condition only.

Correct K5-interior H-edge counts over all twelve factors are:
- x_C in O, profile (2,1^11): 69;
- x_C in H, two-double (2,2,1^10): 66;
- x_C in H, triple (3,1^11): 67.

Writing G_H for the nine additional non-K5 gadget edges with both endpoints in H gives `G_H=g_C`, `3+g_C`, or `2+g_C`, respectively. The corrected verifier returned `V47_CORRECTED_TYPEI_PLACEMENT_ARITHMETIC_OK`. No triple-placement closure is claimed; full-support Q32 remains OPEN.


### Valid refinement after the Type-I correction: triple placement geometry and exact gap

The corrected `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` now further proves that any surviving triple placement in the aligned low-z cell has a fixed local geometry. The triple special K5 has three O and two H vertices; the other special K5 is single-outside. The distinguished `y` must be in H, otherwise `x union (N_t minus {y})` would be a C-colored K5 wholly in H. The four H vertices of N_t occupy one each of X_0,X_1,X_2,X_3, and x lies in the same K12 part as y. The two H vertices of N_s lie in the other two K12 parts. This forces `b_s+b_t=4), G11=(7 H,4 O), `G_H=5), and `g_C=3). The corrected arithmetic replay passed. Triple placement remains OPEN, but is now constrained to this exact local configuration and consumes three units of the global gap budget.


### New aligned-cell gap-cap theorem and nonexact-color budget (2026-10-29)

Section 6–7 of the corrected `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` proves that every exact color in the aligned z=0,1 cell has `g_C<=3`, stronger than the source-level caps 4/5/6. For x_C in O, only y--A_0 edges can contribute H-H gadget edges, and at most three N_s H vertices can be placed in A_0 away from y's target part. For x_C in H two-double, the b_s+b_t=2 case is impossible; y in H gives `g_C=6-(b_s+b_t)<=3), while y in O forces N_t double and gives `g_C<=3). Triple placement has `g_C=3).

Since the total gap is 37 over eleven non-target colors, the unique nonexact color D must have `g_D>=7`, hence `e_D(H)>=76`. Conversely each of the 14 O vertices has at least one D edge into each of the three K12 parts, so `e_D(H,O)>=42); with `e(D)=132`, this yields `g_D<=21`, `e_D(H)<=90`, and `mu_D<=21-g_D<=14`. Therefore exact colors contribute 16–30 units of the gap and at least six exact colors have positive gap. Arithmetic replay passed; the interval is a necessary budget, not a contradiction.


### Further nonexact-color shell-floor tightening (2026-10-29)

The final section of `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` now strengthens the nonexact gap range. Besides `e_D(H,O)>=42`, the nonexact color D must have `mu_D=e_D(A)>=2): the pivot p has no D-edges to A, so if D[A] had an independent 12-set, adding p would produce a D-independent 13-set. Thus `alpha(D[A])<=11), requiring at least `p_11(13)=2` edges on the 13-point shell. Consequently `7<=g_D<=19`, `76<=e_D(H)<=88`, and `2<=mu_D<=14). The exact colors contribute 18–30 gap units, so at least six exact colors have positive gap. The arithmetic verifier passed.


### Exact K5-factor occupancy ledger (2026-10-29)

Added Section 8 to `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md`. The twelve K5 factors partition all 60 vertices other than x_C, so their H-vertex counts can be matched exactly to the four target clique sizes (12,12,12,11):
- x_C in O: eleven single factors plus one double force the double factor to use one H vertex from each K12 part and none from X_0;
- x_C in H, two-double: if x_C lies in X_0, both double factors use all three K12 parts; if x_C lies in a K12 part, one double factor uses X_0 plus the other two K12 parts, and the other uses all three K12 parts. The double factor containing X_0 must be special, not isolated;
- x_C in H, triple: x_C cannot lie in X_0; the triple factor's two H vertices lie in the other two K12 parts.

The exact occupancy arithmetic verifier passed. This sharpens the allowed placement geometry but does not close the remaining color types.


## Residual 1-factorization across K12 tracks (audit-corrected 2026-10-29)

Added `V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION.md`. Its title is historical: **the residual factor is choice-dependent, not canonical**. A repeated color occurs on two edges at a vertex, so no single edge is intrinsically distinguished as “the repeated edge.” The proof now chooses one perfect matching for each non-target color via Hall; their edge-disjoint union has degree 11 at every vertex, and its complement is a perfect matching P. Every H-edge lies in P, and every unselected non-target edge lies in P. Thus each K12xK12 pair has a 1-factorization into P and eleven color-specific perfect matchings. Different choices may yield different P.

The number of C-colored edges in P is the surplus `e_C(T_i,T_j)-12`; these edges pair the repeat-C vertices on the two sides. Since `e_H(T_i,T_j)<=9`, P contains at least three H-edges and at least three non-target repeat edges.

For a K11--K12 pair, Hall gives a matching saturating T0 for each non-target color. Choosing those matchings leaves a residual set with one edge per T0 vertex, but no matching claim on the larger side. The corrected low-gap corollary in the same file uses the registered 69/70 near-Turan forms to align the base matchings when `g_C<=1`.

This is a structural reduction only; it does not close z=0,1. E408/Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## T0 pointwise color-degree saturation (2026-10-29)

Added **V47_T0_POINTWISE_COLOR_SATURATION.md** and its arithmetic replay. In the aligned z=0,1 profile, each vertex v of the K11 track T0 has exactly \(34-\epsilon_v\) non-target-colored H-edges to the other three tracks, with \(\epsilon_v\in\{0,1\}\). Each of the eleven non-target colors must occur at least once from v into each K12 track, so every color has T0 H-degree at least 3.

Therefore:
- if \(\epsilon_v=1\), all eleven non-target colors have H-degree exactly 3 at v;
- if \(\epsilon_v=0\), exactly one color has H-degree 4 and the other ten have degree 3.

Writing \(t_C\) for the number of T0 vertices where color C has H-degree 4 gives \(\sum_C t_C=11-E_0\). For every exact Type-I color, all such degree-four T0 vertices must lie in G11(C), because an isolated single-outside K5 gives degree 3, while an isolated double/triple factor at T0 would violate the degree floor. The source-correct factor occupancy first gives the coarse bound \(t_C\le2\); the later placement-sensitive case split in Section 5 of V47_T0_POINTWISE_COLOR_SATURATION.md sharpens this to the global exact-color bound \(t_C\le1\).

This is an exact vertexwise saturation/capacity constraint for future packing or SAT/ILP work, not a contradiction. The nonexact color may own some of the repeated-color T0 vertices; the aligned cells and root remain OPEN / NOT_CERTIFIED.


## T0 pointwise color-degree saturation (2026-10-29)

Added **V47_T0_POINTWISE_COLOR_SATURATION.md** and its arithmetic replay. In the aligned z=0,1 profile, each vertex v of the K11 track T0 has exactly \(34-\epsilon_v\) non-target-colored H-edges to the other three tracks, with \(\epsilon_v\in\{0,1\}\). Each of the eleven non-target colors must occur at least once from v into each K12 track, so every color has T0 H-degree at least 3.

Therefore:
- if \(\epsilon_v=1\), all eleven non-target colors have H-degree exactly 3 at v;
- if \(\epsilon_v=0\), exactly one color has H-degree 4 and the other ten have degree 3.

Writing \(t_C\) for the number of T0 vertices where color C has H-degree 4 gives \(\sum_C t_C=11-E_0\). For every exact Type-I color, all such degree-four T0 vertices must lie in G11(C), because an isolated single-outside K5 gives degree 3, while an isolated double/triple factor at T0 would violate the degree floor. The source-correct factor occupancy first gives the coarse bound \(t_C\le2\); the later placement-sensitive case split in Section 5 of V47_T0_POINTWISE_COLOR_SATURATION.md sharpens this to the global exact-color bound \(t_C\le1\).

Moreover, the T0-pair surplus identity gives \(t_C=\sum_{i=1}^3(e_C(T_0,T_i)-11)\), while every K12-pair has at least 12 C-edges. Hence \(g_C=e_C(H)-69\ge t_C\), and the placement-sensitive bound gives \(t_C\le\min(1,g_C)\) for exact colors. Summing gives \(\sum_C(g_C-t_C)=26+E_0\), the exact surplus on the three K12--K12 pairs.

This is an exact vertexwise saturation/capacity constraint for future packing or SAT/ILP work, not a contradiction. The nonexact color may own some of the repeated-color T0 vertices; the aligned cells and root remain OPEN / NOT_CERTIFIED.


## New exact residual holonomy-cost theorem (2026-10-29)

Added `V47_Z01_RESIDUAL_HOLONOMY_COST.md` and `verify_v47_z01_residual_holonomy_cost.py`.

In the subcase where all ten isolated Type-I K5 components are single-outside, they leave ten transversal K4s and a seven-vertex residual of profile (2,2,2,1), with a nine-edge baseline and at most three matching-constrained extra edges. This is not universal: the registered source-correct isolated-double placement leaves nine isolated K4s plus an isolated K3 and an eight-vertex G11 residual of profile (2,2,2,2), with 12+g_C edges. See V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md.

There are exactly 64 possible baselines. Exhaustive enumeration classifies them into four types:
- A: large-part matchings form two triangles and T0 attaches to one triangle; 8 baselines, alpha=2, minimum gap 0.
- B: large-part matchings form two triangles but T0 attachments are mixed; 24 baselines, alpha=3, minimum gap 1.
- C: large-part matchings form a six-cycle with alpha 3; 24 baselines, minimum gap 2.
- D: six-cycle with alpha 4; 8 baselines, minimum gap 3.

The exact verifier checked every admissible extra-edge set of size at most three. Thus a nonaligned large-part matching composition costs at least two repeat edges; the most obstructive six-cycle/T0 pattern costs all three. In particular, any exact color with `g_C<=1` must have aligned large-part matching composition. The local enumeration returned `V47_Z01_RESIDUAL_HOLONOMY_COST_OK`; it does not close the global z=0,1 cell.


## Residual holonomy repair shapes (2026-10-29)

The updated verifier checks two sharper local patterns. In class C, each baseline has exactly three independent triples: two share a pair of large-track vertices and the third is a disjoint transversal triple. Every minimum two-edge repair contains the shared-pair edge plus one of the three edges within the disjoint triple, so the shared-pair edge is mandatory.

In class D, the unique independent 4-set consists of the T0 residual singleton and a transversal triple V. The baseline T0 edges attach to the complementary triple U. Every minimum three-edge repair consists of one edge within U, one edge from T0 to a vertex w in V, and the edge between the other two vertices of V. The updated verifier checks these edge-level patterns in addition to the aggregate repair counts.


## Conditional seven-vertex residual graph catalog (2026-10-29)

Added `V47_Z01_EXACT_COLOR_RESIDUAL_GRAPH_CATALOG.md` and its verifier for the conditional subcase where all ten isolated K5 components are single-outside. Its seven-vertex relaxation has profile (2,2,2,1), edge count 9+g_C, alpha at most 2, and corrected counts 8,72,360,1,000 at gaps 0,1,2,3. The catalog is not universal: the source-correct isolated-double placement has an eight-vertex G11 residual, corrected in `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md`. The 7-vertex holonomy table is conditional too; the global g=0,1 orientation remains justified separately by the near-Turan classification.

## Residual-placement audit correction — isolated-double branch (2026-10-29)

A source audit found that the seven-vertex residual graph catalog and the 64-class holonomy-cost table were overstated as universal. The Type-I outside-count profile alone does not force all ten isolated K5 components to be single-outside. HIGH_SUPPORT_NEAR_TURAN.md, Section 3, contains a source-correct placement with the unique double-outside K5 among the isolated components.

Correct split:
- **All isolated components single-outside:** ten isolated transversal K4s leave a seven-vertex G11 residual with profile (2,2,2,1), e=9+g_C. The existing 7-vertex graph catalog and 64-baseline holonomy theorem apply only here.
- **One isolated component double-outside:** the isolated H-subgraph is 9K4 disjoint union K3, with 57 edges. The remaining G11 H-vertices have profile (2,2,2,2), and their induced graph has 8 vertices and 12+g_C edges. The new V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md records the exact accounting and the two-K4 low-gap subcases.

The initial uncapped two-K4 relaxation gave 8,96,528,1760; the per-T0-vertex cap then gave 8,96,480,1312. Both are superseded by the global exact-color bound t_C<=1, which allows at most one T0-incident extra edge in total and gives the stronger necessary-relaxation counts 8,96,408,880. These are not source-realizable completion counts. The exceptional isolated-double placement with x_C in H and y in H has g_C=3 and is now shown to have t_C=1.

The global g_C=0,1 alignment conclusion remains supported independently by the 69/70 near-Turan classification recorded in V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION.md. The T0 pointwise saturation and its identity g_C>=t_C do not depend on the seven-vertex assumption. No root status changes: E408/Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Audit correction: conditional seven-vertex residual model (2026-10-29)

The seven-vertex catalog and holonomy-cost theorem apply **only when all ten isolated Type-I K5 components are single-outside**. `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` establishes a separate source-correct branch: one isolated component is double-outside, giving nine isolated H-K4s plus one isolated H-K3 and an eight-vertex gadget residual of profile (2,2,2,2). Do not apply the seven-vertex counts to that branch.

Within the seven-vertex subcase, the T0 singleton has three baseline C-edges, one into each large track. Pointwise balanced-coloring saturation limits its total C-degree to 3 or 4, so at most one surplus C-edge may touch T0 across all three T0--Ti pairs combined. Both local enumerators now enforce this cap. The corrected exact seven-vertex catalog counts are 8, 72, 360, 1,000 graphs at gaps 0,1,2,3, with K4+K3-base counts 8,72,264,520 and non-base counts 0,0,96,480. The corrected holonomy repair counts are A: (8,72,264,520) for gaps 0–3; B: (gap1,2,3)=(24,216,696); C: (gap2,3)=(72,720); D: (gap3)=72. Minimum repair costs A/B/C/D remain 0/1/2/3 and minimum-repair counts remain 8/24/72/72. An independent reimplementation of both enumerations reproduced these corrected counts and the class-C/D mandatory-edge patterns.

The placement-sensitive case split now proves the global exact-color bound t_C<=1, including the isolated-double exceptional branch x_C in H, y in H. In that exceptional two-double placement, x_C and y are forced into large tracks; the T0 vertex in the special K3 has degree 3 and the T0 vertex in the special K4 has degree 4, so t_C=1. Therefore the total surplus across all three T0--Ti pairs is at most one for every exact color, not just the seven-vertex branch. The global identity then forces t_D>=max(0,1-E0) for the nonexact color D. In the unresolved g_D<=17 branch with no exact gap 0/1, if k exact colors have gap 3, the ten exact colors must contribute at least 10+k large-pair surplus edges and the nonexact color at most 16+E0-k. Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

## Isolated-double residual branch: T0-capped two-K4 enumeration (2026-10-29)

Extended `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` and its verifier. In the isolated-double placements with a two-transversal-K4 residual base, the global exact-color bound t_C<=1 allows at most one T0-incident extra edge in total. Of the 12 possible cross-K4 edges, six are T0-incident and six join large-track vertices, giving 1,12,51,110 allowed extra sets per base at gaps 0,1,2,3. Across eight unordered bases, the corrected necessary-relaxation counts are 8,96,408,880. These supersede both the per-T0-vertex-cap counts 8,96,480,1312 and the uncapped counts 8,96,528,1760. Source gadget star restrictions are stricter; if the star center x_C or y is in T0, then g_C<=1. This still does not close the isolated-double branch.

## Isolated-double exceptional branch: audit correction (2026-10-29)

The attempted full closure of the `x_C in H, y in H` isolated-double branch was retracted after re-reading the cross-track ledger. For a vertex in a large track, the H cross-track degree is **one in total across all other tracks**, not one into each other large track. Therefore the proposed contradiction for a large-track center was invalid.

The valid local lemma is narrower: if `x_C,y` lie in `T0`, each already has three C-neighbors in H from the special K5 geometry and can receive at most one further C-edge by T0 pointwise saturation. The three required gadget edges to the H-part of `N_s` cannot be assigned to two centers, so the T0-centered subcase is CLOSED. The case `x_C,y in T_i` for a large track remains OPEN. See Section 3.3 of `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md`; no Q32 closure is claimed.

## Exact surplus-location constraints by holonomy class (2026-10-29)

The updated `verify_v47_z01_residual_holonomy_cost.py` now checks the full split of every valid repair into T0--Ti surplus edges and large-track-pair surplus edges. In the seven-vertex single-outside subcase: class B at its minimum g_C=1 must use its only surplus edge on a T0--Ti pair; class C at its minimum g_C=2 uses both surplus edges on large-track pairs and has no T0 surplus; class D at g_C=3 uses exactly one T0 surplus and two large-track surpluses. Full split counts are recorded in `V47_Z01_RESIDUAL_HOLONOMY_COST.md`; they sum to the corrected capped totals. These are conditional local constraints, not a global contradiction.

## Aggregate lower bound on exact-color large-pair surplus (2026-10-29)

Added Section 6 to `V47_T0_POINTWISE_COLOR_SATURATION.md`. Define `L_exact=sum_{C exact}(g_C-t_C)`, the surplus on the three K12--K12 pairs carried by the ten exact colors. The global identity gives `L_exact=26+E0-(g_D-t_D)`. Using `g_D<=19` and `t_D>=max(0,1-E0)` yields `L_exact>=8,8,9,10` for `E0=0,1,2,3`, respectively. Hence exact colors must carry at least eight large-pair surplus edges in every aligned cell; E0=2,3 strengthen this to nine and ten. This is a necessary global budget constraint, not a contradiction.

The aggregate budget is sharpened by conditioning on g_D: since `sum_exact g_C=37-g_D` and `sum_exact t_C<=10`, `L_exact>=27-g_D`. Combined with the E0-based bound, `L_exact>=max(27-g_D,8,7+E0)`. In particular, g_D=7 forces at least 20 exact-color large-pair surplus edges, while g_D=19 gives lower bounds 8,8,9,10 for E0=0,1,2,3.

## Shell-bound notation audit — 2026-10-29

The nonexact-color shell lower bound e_D(A)>=2 remains valid. Its proof is now stated directly from alpha(D)<=12 and the fact that p has no D-edges to A; the equivalent ordinary Turán calculation is 78-t_11(13)=2. The previous label p_11(13) was misleading because p_r(n) is reserved for the Kang–Pikhurko second-Turán extremal quantity, whose theorem is not being applied at n=13. This correction changes no numerical result and does not close the aligned z=0,1 cell.


## Shared residual-factor packing audit (2026-10-29)

Added V47_Z01_SHARED_P_FACTOR_PACKING.md and its arithmetic verifier. A subsequent source-baseline audit corrected the earlier classification: the x_C-in-O, N_s-single, N_t-double construction has actual K4+K3 baseline and is Class A, with extras yw and ys_j. It is a valid shared-track pattern, but it does not refute the Class-B-specific complement law. In the seven-vertex Class-B mode, x_C lies in T0 and both special factors are double-outside; for g_C=2,t_C=1, the T0 repeat is on T0-T_k and the large-pair repeat on complementary T_i-T_j. The scalar witness remains source-local by using Class-A patterns: E0=0, E=(2,2,2), e_H=(4,3,3), y=(7,7,8), r=(8,9,9), q=(4,4,3); exact surplus (7,0,3;4,3,3), D surplus (1,9,6;0,1,0), g_D=17. It still omits shared endpoint labels and is not a Q32 coloring.

The labelled six-cycle construction is now explicitly classified as an OWNER-ONLY relaxation, not a feasible common-P color-matching packing. It satisfies P_ij matching counts, pairwise H/exact/D counts, T0 owner counts, and ten individually valid Class-A K4+K3 gadgets, but assigns three colors to each of three residual cycles. Each repeated residual signature forces the same six baseline edges on the same pairwise 2x2 blocks, causing 9 colliding color pairs and 36 duplicate baseline-edge claims. Added the valid pair-projection injectivity lemma: if an exact color owns an S_ij edge, no other exact color may have the same pair of residual subsets (R_i,R_j), because P_ij leaves at most one perfect matching on that 2x2 block. The next model must enforce this injectivity and full cross-color matching edge-disjointness, not just endpoint ownership. Full-support v=47 z=0 and z=1 profile (2,2,2,1) remain OPEN / NOT_CERTIFIED.

## Source-mode local verifier and common-P witness retraction (2026-10-29)

Added `V47_Z01_TWO_DOUBLE_SOURCE_PATTERN_AUDIT.md` and `verify_v47_z01_two_double_source_pattern_audit.py` for the all-ten-isolated-single-outside, both-special-factors-double-outside, x-in-T0 subcase. The exact 7-vertex verifier passes all 19 labeled cases: y outside/a=3 (1), y outside/a=2 (3), y in H/a=2 (3), y in H/a=1 (12). The last row has one T0 repeat on the third track and one large-pair repeat on the other two tracks; this complement relation is valid only in that Class-B source mode. The verifier's unordered track-pair assertion was corrected and the independent replay passed.

Correction to the prior audit: the claimed 20 direct P_0i/K4-baseline overlaps were false. In the source Class-A construction, the K4 baseline uses w-s_i,w-s_j,w-s_k, whereas the candidate P_0i edges use w-y_i,w-y_j,w-y_k, with y_j,y_k in the separate K3. A direct endpoint replay gives zero such overlaps; the verifier asserts zero. Two genuine independent failures remain. First, the candidate H endpoints on T0-T3 have support size 5 for 8 H edges, with three T3 vertices each receiving two H edges from T0; this violates the frozen aligned zero-slack requirement that each large-track vertex has total H cross-track degree exactly one. Second, the owner-only construction has 9 residual-signature collision pairs / 36 duplicate baseline-edge claims. No valid common-P packing or Q32 closure is established.

## T0--Ti omitted-vertex conservation — small-block excess audit (2026-10-29)

For each non-target color C, its selected matching M_C,0i saturates T0 and misses one vertex z_i(C) in T_i. Since the 11 selected matchings and P_0i partition K11,12, d_P0i(v)=#{C:z_i(C)=v}. In the single-T0-residual seven-vertex Type-I mode, an exact color's own T0 repeat edge ending at v forces its omitted vertex to be v. Cancelling those repeat owners gives
n_i(v)+1[z_i(D)=v]=h_i(v)+r_i^D(v),
where h_i(v) is the H degree from v∈T_i to T0 and r_i^D(v) is D-repeat endpoint multiplicity.

**Degree correction:** the aligned degree ledger does not say every T_i vertex has total cross-track H degree exactly one. The nine non-small vertices in T_i do; the three small-block vertices A_i,B_i,C_i have cross-track degrees 1+epsilon and total excess E_i=2 in the current scalar row. Therefore h_i(v)≤1 at non-small vertices and sum_v max(h_i(v)-1,0)≤E_i=2. Repeated H endpoints can occur at small-block vertices, so the earlier binary-profile assumption and blanket injectivity claim are withdrawn.

The D omitted vertex is not known to equal a D-repeat endpoint: D is the nonexact color, and no source lemma currently identifies these. If D has no repeat on T0-T_i, then r_D=0, its omitted vertex must be an H endpoint, and n_i=h_i-delta_D. If D has a repeat, keep delta_D and r_D independent subject to n_i+delta_D=h_i+r_D and nonnegativity.

Updated verify_v47_z01_t0_omission_conservation.py to enumerate endpoint profiles with overage allowed only at the three small-block vertices and total overage at most E_i=2. For y=(7,7,8), exact repeats=(4,3,3), D repeats=(0,1,0), E=(2,2,2), the exact endpoint-only replay gives 3,528 / 3,528 / 3,897 allowed H profiles and 20,610 / 42,336 / 25,758 D-omission assignments for T1/T2/T3. Maximum exact nonrepeat omission multiplicity is 3 on each track. A further exact local degree audit sets \ell_i(v)=d_H(v,T_j)+d_H(v,T_k), u_i=\sum_v max(h_i(v)-1,0), k_i=\sum_v max(\ell_i(v)-1,0), and omega_i=#{v:h_i(v)>0, ell_i(v)>0}. The pointwise equation h_i(v)+ell_i(v)=1+epsilon_i(v) yields the exact decomposition E_i=u_i+k_i+omega_i=2. Here k_i is overlap between the two large-pair H endpoint sets at T_i, and omega_i is overlap between T0-H and large-pair H endpoints. The verifier enumerates 9,270 / 9,270 / 8,649 local degree states on T1/T2/T3 and checks this identity in every state. This is still only a necessary endpoint relaxation, not a full common-P completion. The eight-vertex isolated-double mode is outside the exact-repeat cancellation lemma. Q32 remains OPEN / NOT_CERTIFIED.

## Forced Class-A repeat allocation in the E0=0 scalar row (2026-10-29)

Added verify_v47_z01_class_a_repeat_allocation.py. Conditional on all ten exact colors being Class A, the scalar counts exact large-pair repeats (7,0,3) and T0 repeats (4,3,3) force a unique allocation: four colors repeat on T0-T1 and T1-T2; three on T0-T2 and T1-T2; three on T0-T3 and T2-T3. The verifier enumerates all nonnegative allocations and finds exactly one. Since P12 and P23 are perfect matchings, their seven and three exact-repeat edges are pairwise vertex-disjoint within each pair, forcing the corresponding track endpoints to be distinct. This is a local CSP constraint only; mixed Class-A/Class-B and isolated-double modes are not covered.

## Residual six-set injectivity — all source modes (2026-10-29)

Added V47_Z01_RESIDUAL_SIGNATURE_INJECTIVITY.md and its finite parity replay. The theorem now rules out two exact colors sharing the same six residual vertices across all source modes. If two colors share that set, their matching restrictions on each of the three K2,2 blocks must be complementary, which toggles triangle/six-cycle parity; one color must have a six-cycle. The source-mode split shows any such color has at least one large-pair repeat: single-outside six-cycle costs g_C>=2; isolated-double two-K4 subcases cannot realize a six-cycle because extras form a star and cannot supply both disjoint cross edges of an alternate matching; the exceptional isolated-double branch has g_C=3,t_C=1. Pair-projection injectivity then forbids any other color sharing the residual pair on the repeated-edge track pair.

This rules out repeated residual six-sets globally, but not distinct signatures with overlapping pair projections, and it does not solve the common-P packing. Full-support v=47 z=0 and z=1 profile (2,2,2,1) remain OPEN / NOT_CERTIFIED.

## Owner-only P0 overlap audit correction (2026-10-29)

The previous claim of 20 direct P_0i/K4-baseline overlaps was false and is withdrawn. In the explicit source Class-A construction, the K4 baseline uses w-s_i,w-s_j,w-s_k, while the candidate P_0i edges use w-y_i,w-y_j,w-y_k with y_j,y_k in the separate K3. A direct endpoint replay gives zero overlaps. Two actual failures remain: the candidate's T0-T3 H endpoint profile has 8 edges on 5 vertices, giving endpoint excess sum_v max(h_3(v)-1,0)=3>E_3=2; and the owner-only construction has 9 residual-signature collision pairs / 36 duplicate baseline-edge claims. The first is a track-excess-budget violation, not a claim that every T3 vertex has degree one. No complete common-P packing is certified.


## E0=0 endpoint multiplicity constraints — corrected (2026-10-29)

The H endpoint multiset on T0-T_i is not necessarily a set. In the aligned zero-slack contract, h_i(v)≤1 for each of the nine non-small vertices, while the three small-block vertices may have multiplicity above one with total excess sum_v max(h_i(v)-1,0)≤E_i=2. In the E0=0 scalar row, the allowed H endpoint profile counts are 3,528 / 3,528 / 3,897 for T1/T2/T3.

If D has no T0 repeat on a pair (T1,T3), its omitted vertex must be an H endpoint and n_i=h_i-δ_D. If D has the T0 repeat on T0-T2, the omitted vertex is the endpoint of that repeat, so δ_D=r_D and n_i=h_i. The earlier claim that all omissions were injective, the binary-profile counts 5,544 / 70,488 / 3,960, and the P0 endpoint-degree caps (2,3,2) are withdrawn.

Under the all-Class-A allocation, exact T0-repeat endpoints are distinct within each track (a_i(v)≤1), but may overlap H endpoints. With h_i(v)≤3 and the D-repeat vector (0,1,0), the conservative endpoint-only bounds are max degree of P0i at most (4,5,4) for T1/T2/T3. These are necessary local constraints only; the full vertex-labelled common-P packing remains OPEN / NOT_CERTIFIED.

## Class-B zero-T0-surplus star-center incidence (2026-10-29)

In the Class-B source mode with x_C in T0 and both special factors double-outside, the y-in-H, a=2 row has g_C=2,t_C=0 and two surplus edges forming a star y-s_j,y-s_k into the other two large tracks. These are y's unique P edges on those pairs, so y has no H-neighbor in the other large tracks. Under the aligned zero-slack ledger, y is a residual vertex with total cross-track H-degree exactly one; therefore it must have exactly one H-neighbor in T0. This is a necessary source-incidence filter, not a contradiction.


## Class-B zero-T0-surplus star-center incidence (2026-10-29)

In the Class-B source mode with x_C in T0, both special factors double-outside, y in H and a=2, the two surplus edges form a star ys_j, ys_k into the other two large tracks. These are the unique P edges incident to y on those pairs, so y has no H-neighbor in the other large tracks. Under the aligned zero-slack ledger y has total cross-track H-degree exactly one; therefore it must have exactly one H-neighbor in T0. This is a necessary source-incidence filter, not a contradiction.


## Partial pair-projection packing (2026-10-29)

Added V47_Z01_PARTIAL_PROJECTION_PACKING.md and verify_v47_z01_partial_projection_packing.py. For any fixed residual pair key (A,B) on tracks i,j, the block A×B is K2,2 with two internal perfect matchings. If common P_ij contains any edge of the block, one internal matching is forbidden and only the other can be used; edge-disjointness makes the key unique. Thus a duplicated pair projection is possible only if the entire four-edge block is P-free. In that case exactly two colors may share the key, using complementary matchings and covering all four block edges. No two colors can share two pair projections, since that forces identical full residual six-sets, already excluded by the all-mode injectivity theorem. The verifier checks all seven possible matching intersections of P_ij with a K2,2 block. This is a necessary CSP constraint, not a Q32 closure.


## Exact projection-block CSP encoding (2026-10-29)

Added a solver-ready binary encoding to V47_Z01_SHARED_P_FACTOR_PACKING.md, Section 4.3.2. Variables choose each color's residual 2-set per track, its pair projection, one of the two K2,2 matching orientations, and the common P_ij edges. Linking constraints enforce one residual set per track and a consistent pair projection; orientation-wise occupancy is at most one color; any P_ij edge forbids the matching orientation containing it. Because P_ij is a matching, each residual block is either P-free (allowing at most two colors, one per orientation) or P-hit (allowing at most one). This exactly encodes the partial projection lemma locally, while source-mode, alpha, repeat ownership, T0, and global degree constraints remain necessary. No Q32 closure claimed.


### Projection encoding edge-conflict audit (2026-10-29)

A follow-up audit caught an incompleteness in the first solver-ready encoding: key-local orientation occupancy alone does not prevent two different residual pair blocks from overlapping in an actual edge. Section 4.3.2 of V47_Z01_SHARED_P_FACTOR_PACKING.md now adds the required edge-level constraint, for every actual edge e in T_i×T_j, summing all selected orientations across every color and every pair key containing e to at most one. Keep both constraints: key-local occupancy handles duplicate projections; edge-level occupancy handles overlapping but nonidentical blocks. The encoding is still a local projection layer, not a complete CSP or Q32 closure.


### Cross-key edge-overlap regression (2026-10-29)

Extended verify_v47_z01_partial_projection_packing.py with a concrete 3×3 toy regression: two distinct residual K2,2 blocks can each choose a matching orientation disjoint from the same global P perfect matching, yet those chosen orientations share an actual edge. The example passes all key-local checks but violates cross-color edge-disjointness, confirming that the newly added edge-level occupancy inequality is essential. The toy replay passed independently; it is a model-audit check, not a Q32 graph witness.
