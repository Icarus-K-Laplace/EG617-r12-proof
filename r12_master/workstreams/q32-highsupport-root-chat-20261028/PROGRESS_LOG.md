# Progress log — Q32 high support + root audit

## 2026-10-28

### Branch isolation

Created `workstream/r12-q32-highsupport-root-20261028` from the latest E408-global source state. All writes are confined to `r12_master/workstreams/q32-highsupport-root-chat-20261028/`.

### v=47 near-Turan attack

Proved the source-correct exact-color placement trichotomy relative to `H` and `O={p} union A`:

- x outside H -> `(2,1^11)`, 11 witnesses, H-edge range 69--73;
- x in H / two-double -> `(2,2,1^10)`, 10 witnesses, H-edge range 69--74;
- x in H / triple -> `(3,1^11)`, 11 witnesses, H-edge range 69--75.

Derived exact-color gap cap `0<=g_C<=6` and global all-color identity `sum g_C=37`.

Classified the 69/70 near-Turan layers: common `4^11,3` partition; at 70 edges exactly one cross-part color edge; no K4 can cross parts.

Audited and corrected the explicit 69-edge Type-I placement example so it respects the rule that every p--A edge has target color. This confirms that a universal per-exact-color `+1` reserve is false.

Derived source-correct shell/core tradeoffs `g<=mu+2` (x in H), `g<=mu+1` (x outside H), and minimum exact M-edge payment at least2 (triple x-in-H at least3).

### New m=8 weighted-surplus theorem

Using the newest 130-edge minimum-degree-four theorem, proved the exact pointwise identity

`(d_F(z)-13) + sum_non-target(d_C(z)-4)=3`.

Hence every exact Type-I source parameter satisfies `a in {2,3}`. Its variable weights are `{2,3}`, so no point can host two variable occurrences. Therefore all sixteen `x_C,y_C` points of the eight exact colors are pairwise distinct.

Consequences:

- Case-II v=45,m=8 CLOSED;
- Case-II v=46,m=8 CLOSED.

This is a new source-correct replacement for the historical injectivity-style argument and does not use the withdrawn degree-nine premise.

### v=45/v=46 rigidification

For m=9 and m=10, converted corrected multiplicity `n_w>=m-6` plus the pointwise surplus budget into high-a normal forms.

m=9 at a W-point:

- `n in {3,4}`;
- n=4 -> `(a)=(4,4,4,4)`;
- n=3 -> `(4,4,4)` or `(4,4,3)`.

m=10:

- `n in {4,5}`;
- n=5 -> all a=4;
- n=4 -> `(4,4,4,4)` or `(4,4,4,3)`.

For v=46, every non-special exact color through the unique W point uses at least two distinct shell neighbours, giving the valid Case-II matching lower bound `nu(M)>=m-n_w`.

### Root audit

Verified the fail-closed root receipt and source-frozen E407 sibling hashes.

The exact frozen E407 files at commit `b36538e27dce89dfcba2aa2bfdfc29d6611a96ec` match the receipt hashes. The five-template file itself was still OPEN; therefore finite reduction to five templates is not itself a contradiction.

Verified that the later `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` genuinely bypasses template-by-template closure using the common 29-point/49-block contract:

`294 selected edges + p_12(29)=22 > 310`.

Verified that the newer V10/V11 audit supersedes the older V11 replay-pending note.

Verified the Q33 global bypass: m=10 excluded by component capacity; m=8,9 excluded by the 31-point nonexact-U reserve (`78,52 > 41`).

Installed `ROOT_DEPENDENCY_DAG.md` and `RETRACTION_FIREWALL.md`.

### Current status

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

This workstream's remaining high-support frontier:

- v=47, m=8,9,10;
- Case-II v=45,m=9,10;
- Case-II v=46,m=9,10.

Sibling workstream retains sole ownership of Case-II v=44,m=8,9.

### New pivot-neighborhood packing theorem (this turn)

Added `V47_PIVOT_NEIGHBORHOOD_PACKING.md`.

Proof spine:
- every exact color C has a C-colored K4 `Q_C` contained in `N_C(p) cap H`, using the source-correct Type-I factorization;
- the sets `Q_C` are pairwise vertex-disjoint because the color-neighborhoods of p partition H;
- `alpha(H)<=4` and Konig imply at least four H-edges between each pair of Q-blocks;
- every point of R=H\\Q has at least one H-neighbor in each Q-block;
- Turan gives `e(H[R])>=p_4(|R|)`.

For m=8,9,10, the three floors sum to253. Defining edge slacks x,y,z gives `x+y+z=32`, `2x+y>=5m`, `y+2z>=D_m` with D=(18,13,8), and `x>=8,13,18` respectively. Added `verify_v47_pivot_packing.py`; local execution returned `V47_PIVOT_PACKING_ARITHMETIC_OK` with 79,61,44 scalar slack states. This confirms the scalar relaxation is feasible and must not be advertised as UNSAT.

### Independent root-dependency audit

Read the branch-local `ROOT_PROMOTION_RECEIPT.md`, the current E407 V12 reserve file, the dedicated E407 proof dependency audit, the V10/V11 independent replay audit, the Q33 capacity/reserve files, and the current Q32 core terminal.

Audit conclusions:
- The E407 four-color U-reserve arithmetic is valid under the frozen V12 `|U|=29`, 49-block contract (`294+22>310`). Parent-level closure remains conditional on V12 exhaustiveness and branch-state reconciliation; the dedicated E407 canonical still carries a stale OPEN same-core snapshot.
- The Q33 31-point nonexact-U-reserve arithmetic is valid under its contract (`m=9`: 52>41; `m=8`: 78>41). The closure file itself makes parent promotion conditional on the upstream reduction exhausting all Q33 completions through that contract. The precise exhaustive support-lifting theorem path was not identified in this pass, so the root DAG now records this as an unresolved dependency rather than silently assuming equality from a support lower bound.
- V9 replay is recorded relative to retained seeds; the newer V10/V11 replay audit supersedes the older V11 pending note and reports package-hash/replay success under retained analytic/lower-order inputs; V12 replay is source-reported by the root receipt and was not re-executed in this turn.
- The old root promotion remains withdrawn because of the KP degree-nine retraction. Root state remains OPEN / NOT_CERTIFIED.

Updated `ROOT_DEPENDENCY_DAG.md`, `RETRACTION_FIREWALL.md`, and `CANONICAL_STATE.md` to keep these contract boundaries explicit.
### Pivot-block triangle consistency (same sprint)

Added Lemma 8.1 to `V47_PIVOT_NEIGHBORHOOD_PACKING.md`: if two block-pairs incident to Q_i each have exactly four H-edges, their perfect matchings force the composed matching on the closing pair Q_j,Q_k. Otherwise Q_i minus one vertex together with the two unmatched endpoints would be an independent 5-set.

Thus every all-light triangle in the block-label graph aligns into four disjoint H-triangles; a heavy closing pair must still contain the composed matching. Since x is the number of extra Q-Q edges, the light-pair graph has at least 5,11,17 edges for m=8,9,10. These counts do not force a triangle by themselves, so the lemma is recorded as a finite compatibility constraint, not a contradiction.
### Universal zero-shell multiplicity theorem — new closure (2026-10-28)

Derived and committed the source-correct inequality `n_w >= 2m-14` for every nonempty W-point. Proof: each non-special exact color consumes at least two distinct w--A edges; at most one special exact color can have zero shell degree because any such color must own the unique edge pw.

Combined with pointwise special-surplus budgets `n_w<=r_m`, `r=(3,4,4)`:
- m=8: still closed by `n_w>=2` and each special incidence costing at least2 against budget3;
- m=9: sharpened from `n_w in {3,4}` to `n_w=4`, and all four special parameters are a=4 at each W-point;
- m=10: `n_w>=6` contradicts `n_w<=4`, so every non-full-support m=10 branch is CLOSED.

Consequences: v=45 m=10 and v=46 Case-II m=10 are now closed; the v=45 m=9 branch spends at least8 global exact-color gap units across the two disjoint special sets, and v=46 m=9 spends at least4. Full support v=47 remains unaffected because W is empty.

Updated `V45_SOURCE_CORRECT_MULTIPLICITY.md`, `V46_CASEII_CLOSURE.md`, `CANONICAL_STATE.md`, and `ROOT_DEPENDENCY_DAG.md`. No retracted KP degree-nine or exceptional-injectivity claim was used.
### Target-shell correction and m=9 shell saturation

Strengthened the universal inequality by explicitly reserving target-colored shell edges. If `t_w` is the target degree from w into A, then `n_w >= 2m-14+t_w` (not merely `2m-14`). For m=9 the pointwise budget forces `n_w=4`; therefore `t_w=0` and the core excess at each W-point is exactly1.

Exact shell ownership at each m=9 W-point is now rigid: the five non-special exact colors use exactly two A-edges each (10 total), three of four special exact colors use one A-edge each, and the remaining special color uses no A-edge and owns pw. The target color and both nonexact colors have no A-shell edge at w. Accounting for p correctly, every special exact color has exactly one outside neighbor and H-degree4; hence each spends `g_C>=1`, not `g_C>=2`. This correction preserves the rigorous total gap floor of 8 across the two disjoint W-point special sets.

For v=45,m=9, both W-points have degree4 in the 130-edge color, with all those neighbors in H. Audit found no source-correct theorem forcing the W-W edge to have that color: the isolated-K4 equality result is for degree-three vertices, not degree four. Retracted the unsupported pair-rigidity claim. The valid ledger is `E_W=2`, `E_U=4`, `e_H(W) in {0,1}`, and `e(bar(H[U]))=731-e_H(W)` (730 or731).

Updated the V45/V46 source-correct files, the zero-shell arithmetic verifier (rerun: `ZERO_SHELL_MULTIPLICITY_ARITHMETIC_OK`), the canonical state, and root dependency DAG.

### Direct 130-edge no-core-only degree-four theorem and v45/v46 m=9 closure

Files:
- `Q32_130_NO_CORE_ONLY_DEG4.md`
- `V45_V46_M9_CLOSURE.md`

The new theorem proves that no vertex in H can have degree four in a 130-edge non-target color while all four color-neighbors lie in H. The proof:
1. For any degree-four vertex, the (56,11) Kang–Pikhurko bound gives at least119 edges on its 56-point non-neighborhood.
2. The 130-edge budget and minimum degree four force at least five edges inside its four-neighbor set.
3. For a core-only degree-four vertex, alpha(H)<=4 forces the neighborhood to be K4-e; the two S–N edges attach one to each missing-edge endpoint.
4. An endpoint's own four-neighbor set then induces a triangle plus an isolated vertex (three edges), contradicting Step 2.

This is a direct analytic theorem and does not use exceptional-vertex injectivity or the retracted degree-nine claim.

The v45,m=9 and v46,m=9 source-correct shell profiles each force the 130-edge color to have degree four at a W-point, no A-neighbor, and no pw edge because the unique zero-shell special exact color owns pw. Thus the direct theorem closes both rows, bypassing the earlier unsupported W-pair/e_H(W)=0 inference.

Updated frontier:
- v44,m=8,9,10: closed by the sibling branch (read-only import);
- v45,m=8,9,10: closed;
- v46,m=8,9,10: closed;
- v47,m=8,9,10: **OPEN**.

The root dependency DAG now records v47 as the sole remaining Q32 support terminal. EG617(r=12) remains OPEN / NOT_CERTIFIED because v47 and the upstream dependency-reconciliation gates remain open.

### 130-edge degree-four local audit and correction

Audited the 130-edge color at each v45,m9 W-point. The source-correct local lemma is: if d_D(v)=4, the 56-point non-neighborhood has at least119 edges by KP at (56,11); writing S=N_D(v), a=e_D(S), b=e_D(S,N), the exact ledger gives a+b<=7 and 2a+b>=12. Thus only (a,b,e(D[N]))=(5,2,119),(6,0,120),(6,1,119) are possible. This yields a K4-minus-edge neighborhood with two outgoing edges, or a K4 neighborhood with at most one outgoing edge. It does not imply degree-four vertices are adjacent. Committed the local lemma and `verify_130_color_degree4_local.py`; the arithmetic check returned `130_COLOR_DEG4_LEDGER_OK`.

### v47 independent-set incidence-cover lemma

For every independent S subset R with |S|=k<=4 and every pivot block Q_i, proved that the union of N_H(r) intersect Q_i over r in S has size at least k; otherwise S plus 5-k vertices of the independent block is an independent 5-set. If y_i=0, every r has a unique neighbor in Q_i, and the independent-pair case forces each fiber to be a clique in H[R], so R is partitioned into at most four cliques. For m=10, the scalar ledger gives 8<=y+2z<=14 and z<=7. When z<=5, e(H[R])<=8, so Mantel implies alpha(H[R])>=3 and the independent-triple cover condition applies to every block. z=6,7 is kept as a separate high-z cell. Added `V47_RESIDUAL_INCIDENCE_COVER.md`.
### v47,m10 high-chromatic residual cell closed

Used the independent-set incidence-cover lemma to close the `chi(bar(H[R]))>=5` subcase. A 5-critical complement on seven vertices forces `H[R]=C5 dot-union 2K1`, hence z=2. No block can have zero y_i, so y>=10; the degree ledger gives y+2z<=14, hence y=10 and x=20. Thus each of ten blocks has exactly one extra Q-R incidence, and every Q-vertex has degree12.

Both isolated R vertices have d_R=0 and therefore each needs at least two extra incidences across blocks. Lemma 7.1 shows no block's extra-incidence vertex can be an isolated R vertex: if it were u, the other isolate v and all C5 vertices have unique Q_i neighbors; independent-pair constraints force the five C5 vertices to 3-color the C5 nonedge graph, using all three labels; each independent four-set {u,v,a,b} then forces N(u) in Q_i to contain the omitted third label for every pair of labels, impossible with only two neighbors. Same for v. Contradiction.

Therefore `chi(bar(H[R]))<=4` in the remaining v47,m10 cell. This closes only the high-chromatic residual subcase; the 4-colorable residual cell and v47 m=8,9 remain OPEN.

### v47,m10 light-block graph disconnected reduction

Added `V47_LIGHT_BLOCK_GRAPH_DISCONNECTED_REDUCTION.md`. Let L connect block labels whose Q-pair has exactly four H-edges. For each block, `s_i=t_i+y_i-5=sum_{q in Q_i}(d_H(q)-12)>=0`; `sum s_i=2x+y-50<=6`. A component of size k<=5 forces `s_Q>=k(5-k)+Y_S`. Hence L cannot have three or more components, and the only disconnected component-size splits are 1+9, 2+8, 3+7, 4+6, 5+5.

The 2+8 split forces `s_Q=6,s_R=0,y+2z=8); its two-block component is a light edge, all 16 cross pairs have exactly five edges, and `x_T=8+z,y=8-2z,z<=4`. The 3+7 split similarly forces a light triangle, all 21 cross pairs have exactly five edges, and `x_T=3+z,y=8-2z,z<=4`. In both cases `d_R(r)+b_r=2` pointwise, so `Delta(H[R])<=2`.

The 4+6 split has `y+2z<=10,z<=5` and at most two units for internal heavy pairs/cross multiplicity/shell incidence in the four-block component. The 5+5 split has `x>=25,y+z<=7,z>=1`, and at most three weighted extra units beyond the 25 mandatory cross-pair units.

Added `verify_v47_m10_residual_path_cycle_types.py`; an independent in-session enumeration verified exactly 18 possible 7-vertex path/cycle types under `Delta(H[R])<=2, alpha(H[R])<=4, clique_cover(H[R])<=4, e(R)=3+z`, for z=0,...,4. Scope is residual graph-type enumeration only, not the full Q32 contradiction.


### v47 m=10: zero-slack map alignment and three-block transversal blocker

Added `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md`.

**Zero-slack map alignment.** For two small blocks A,B with a light perfect matching and y_A=y_B=0, every r in R has unique labels f_A(r),f_B(r). For each independent pair r,s, alpha(H)<=4 forces `{f_A(r),f_A(s)}={f_B(r),f_B(s)}`; otherwise two A-vertices, r,s, and a B-vertex form an independent 5-set. Since |R|=7 and Delta(H[R])<=2, every r has two nonneighbors s,t that are themselves nonadjacent, which forces f_A(r)=f_B(r). Therefore the two maps coincide in the 2+8 cell, and all three maps coincide in the 3+7 light-triangle cell after matching consistency.

**Outer-block transversal obstruction in 3+7.** For each outer vertex q, the three label-neighborhood sets in the small blocks have a nonempty common intersection. If it is singleton {h}, there exists an independent transversal of the three labels other than h avoiding q. Thus q must be adjacent to every r in F_h; using d(q)=12 yields `k(q)<=3-|F_h|`. If the intersection has size two, q must own all three small-component extra edges and has no R-neighbor or other extra Q-Q incidence. The per-outer-block exact budget is `sum_q k(q)=3`.

Added `verify_v47_three_small_block_transversal.py`. Exact normalized enumeration:
- aligned matching maps: 1,728 configurations;
- synchronized transposition-switch configurations: 36;
- vertex records checked: 7,056;
- singleton-track: 7,044; double-track: 12.

The exact verifier returned `V47_ZERO_SLACK_TRANSVERSAL_LOCAL_OK`. It checks the finite local label/transversal theorem only. It does not solve the global Q32 graph or close the disconnected component cells.


### Endpoint-load refinement for the 2+8 and 3+7 cells

The small-block part of `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md` now has an exact endpoint ledger. If `e_i(h)) counts extra Q-Q endpoints at small-block label h and `n_h=|F_h|), then `d_H(q_h)=9+e_i(h)+n_h), hence `e_i(h)>=3-n_h). Summing gives only three slack units per small block in 2+8 and two in 3+7. The four possible sorted fiber profiles are `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, and `(2,2,2,1)`.

For 3+7, a switch block uses the same extra-edge endpoint label s in all three small blocks; its common track s is duplicated and must have fiber size at most one. If that fiber is a singleton r, each such switch gives r an extra Q-R incidence, so at most `2-d_R(r)` such switch blocks can occur. This creates an exact coupling between the 4,5,5 switch patterns and the residual degree ledger. Still a necessary-condition reduction, not an UNSAT proof.


### New m=10 two-light matching composition theorem

Added `V47_TWO_LIGHT_MATCHING_COMPOSITION.md` and its exhaustive verifier `verify_two_light_matching_composition.py`.

The theorem: if A-C and B-C are light perfect matchings, e(A,B)<=7, and alpha(A union B union C)<=4, then A-B must contain the composed matching. If a composed edge A_iB_i is missing, alpha<=4 forces all three off-diagonal edges in row i; the edge cap then forces the other diagonal edges and yields a second independent 5-set. The proof is analytic and uses no external extremal theorem.

The exact verifier enumerated all 25,636 A-B graphs with 4..7 edges and all 792 five-vertex subsets per graph. It returned:
- e=4: 1 alpha<=4 graph;
- e=5: 12;
- e=6: 66;
- e=7: 220;
- `V47_TWO_LIGHT_MATCHING_COMPOSITION_EXHAUSTIVE_OK`.

Application to the disconnected m=10 cells: every outer pair has at most 7 edges, so each actual length-two light path forces the composed matching into its endpoint pair. The 2+8 outer light graph has 8 vertices and minimum degree at least 3; the 3+7 outer light graph has 7 vertices and minimum degree at least 4. Thus every nonadjacent pair has common light neighbors only in the 3+7 cell. Five-edge pairs have a unique matching; six-/seven-edge pairs have at most two. Matching disagreements charge to at most six pairs with e>=6 in 2+8 (x_T<=12), or at most three in 3+7 (x_T<=7).

This narrows the matching system but does not close either disconnected cell. Full support remains OPEN / NOT_CERTIFIED.


### Matching-holonomy scope correction (2026-10-28)

The correct light-graph degree bounds are: 2+8 has eight outer blocks and minimum light degree at least 3; 3+7 has seven outer blocks and minimum light degree at least 4. Therefore the statement that every nonadjacent pair has a common light neighbor applies only to 3+7. In 2+8, the matching-composition theorem is used only on length-two light paths that actually exist. The local theorem and its finite verification remain valid; only this application scope is corrected.


### Four-light-cycle holonomy theorem for m=10 disconnected cells

Added `V47_LIGHT_CYCLE_HOLONOMY.md` and `verify_v47_light_cycle_holonomy.py`.

In a four-cycle of light matching pairs, the two diagonals must contain both length-two path matchings. If the holonomy moves four labels, each diagonal would need eight edges, over the cap seven. If it moves three labels, each diagonal is forced to exactly seven edges and the normalized graph contains the independent 5-set `{A_0,A_3,B_2,C_1,D_0}`. Therefore holonomy is identity or a transposition. A transposition requires both diagonal pairs to have at least six edges.

The exact local verifier checked 726 transposition cases (six transpositions times 11 choices for each diagonal) and rejected all eight 3-cycle cases:
`V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK`.

Application: in 3+7, a six-edge pair has weight k=2 and uses the full internal-heavy budget at both endpoints, so no other heavy pair can touch either endpoint. Any nontrivial four-cycle holonomy is supported on two disjoint high-weight diagonals. This tightens the matching-holonomy ledger but does not close the m=10 2+8/3+7 cells.


### New m=10 3+7 global light-holonomy theorem

Added `V47_37_OUTER_LIGHT_HOLONOMY.md` and `verify_v47_37_light_graph_cycles.py`.

In the 3+7 cell, the outer light graph L has seven vertices, minimum degree four, weighted heavy degree at most two per vertex, and total heavy weight `x_T=3+z<=7`. The new proof upgrades local cycle constraints to global matching alignment:
- triangles have identity holonomy by two-light composition;
- a transposition four-cycle would force both diagonals to weight two, saturating all four vertices and creating an outside common light hub, which forces identity;
- a chordless five-cycle similarly has an outside common light hub;
- every six-/seven-cycle has a light chord and reduces to shorter cycles.

All cycles therefore have identity holonomy. Since L is connected, its light-edge matchings can be globally relabeled as identity. Every heavy pair has at least three common light neighbors, so matching composition forces the same aligned matching into every heavy pair. The 28 outer vertices contain four aligned K7 tracks; all other Q-Q edges within T are cross-track edges, with total at most seven.

The exact verifier enumerated 22,054 weighted heavy graphs and checked 5,803,387 light cycles. Output:
`V47_37_LIGHT_GRAPH_CYCLE_DECOMPOSITION_OK`.

This is a genuine structural advance, not a global contradiction. It leaves m=10's 3+7 cell open, as well as m=10's other cells and full-support m=8,9.


### 2+8 two-block transversal blocker; 3+7 double-track fiber cap

Added `V47_TWO_BLOCK_TRANSVERSAL_BLOCKER.md` with a source-correct proof for the 2+8 cell. For an outer vertex q with singleton common track h, if q missed some r in F_h, its at least four R-nonneighbors and Delta(H[R])<=2 yield an independent pair r,s in distinct fibers; the two remaining labels can be chosen distinctly outside S_A(q),S_B(q), creating an independent 5-set. Thus q must hit all of F_h and `k(q)<=3-n_h).

For a double track {h,j}, q consumes both extra A/B edges and has at most one R-neighbor. Every cross-fiber nonedge between F_h,F_j must meet that unique neighbor. Corrected the exact case split: with zero R-neighbors, or one neighbor outside both fibers, or one neighbor in a fiber of size at least two, the degree cap gives `n_h+n_j<=3). The only exceptional pattern is `{n_h,n_j}={1,3}) with the unique R-neighbor being the singleton-fiber vertex. This exception is explicit and must not be omitted.

Each outer block has `sum k(q)=2); each small block's endpoint loads satisfy `e_i(h)=3-n_h+u_i(h)), `sum u_i=3), hence `e_i(h)<=6-n_h). Synchronized switch blocks with endpoint label h are therefore at most `6-n_h).

Strengthened the 3+7 file: a double-track vertex has d_R=0, so every cross-pair between its two track fibers must be an H-edge, forcing `n_h+n_j<=3). This is not yet a global contradiction; the 2+8 and 3+7 cells remain OPEN.


### New m=10 3+7 residual-track domination theorem

Added `V47_37_RESIDUAL_TRACK_TRANSVERSAL.md` and `verify_v47_37_residual_track_transversal.py`.

Combining the four globally aligned outer K7 tracks with the residual degree ledger gives each r in R at most nine neighbors among the 28 outer vertices, hence at least19 nonneighbors. The cross-track graph has at most seven edges and maximum degree two. If r missed at least one vertex in each of the four tracks, the four part sizes would be in `[1,7]` with sum at least19.

A strict union bound proves such a four-part graph always has an independent transversal. The verifier enumerates all 64 sorted profiles and the full relaxed six-pair edge-count allocation space under total-edge and per-part degree caps. Exact result:
- worst profile: `(7,7,4,1)`;
- total transversals:196;
- maximum forbidden-transversal upper bound:133;
- strict margin:63;
- output `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`.

Therefore each residual vertex is adjacent to every vertex of at least one outer K7 track, giving a K8 with that residual vertex. Since b_r<=2, at least five outer blocks have the track vertex as the unique r-neighbor; if d_R(r)=2, all seven do.

This is a new necessary structural condition. It does not yet close 3+7; m=10's other component cells and full-support m=8,9 remain open.


### 3+7 double-track fiber/edge floor

A double-track vertex in the 3+7 cell has no R-neighbors. The two fibers indexed by its common tracks must therefore be completely joined, so `e(R)>=sum binom(n_h,2)+n_h*n_j`. Applying this to the only four possible fiber-size partitions yields the exact thresholds: (3,3,1,0) permits (3,0)/(1,0) only at z>=3; (3,2,2,0) permits (3,0)/(2,0) only at z>=2; (3,2,1,1) permits (2,1) at z>=3 or (1,1) at z>=2; (2,2,2,1) permits (2,1) at z>=2. Therefore z=0,1 has no double-track vertex. Added and executed `verify_v47_3plus7_double_track_edge_floor.py`; result `V47_3PLUS7_DOUBLE_TRACK_EDGE_FLOOR_OK`. No global contradiction is claimed.


### 3+7 residual track fibers are cliques

Extended `V47_37_RESIDUAL_TRACK_TRANSVERSAL.md`: the complete track assigned to each residual vertex is unique, and two nonadjacent residual vertices cannot share a track. For two vertices r,s on the same track, each of the other three tracks has at least three vertices nonadjacent to both. With at most seven cross-track edges, the number of three-part transversals is at least `9*max(a,b,c)`, while each edge blocks at most `max(a,b,c)`; an independent transversal exists, giving an independent 5-set with r,s.

Thus the track assignment partitions R into clique fibers of size at most three, with profiles `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, or `(2,2,2,1)`. These match the possible profiles for the small-block map, but alignment of the two partitions remains open.

The exact verifier now checks the 64 four-part profiles and 35 three-part profiles. Output: `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`.


### Switch duplicate-fiber budget and z=4 empty-fiber escape theorem

A switch block duplicates one singleton common-track label s. Both vertices with common track s meet all of F_s, so the block must spend at least `n_s` residual-incidence slack: `n_s<=y_D). In 3+7 this rules out duplicate size-three fibers; at z=4, where every y_D=0, any switch must duplicate an empty fiber.

Added `V47_Z4_EMPTY_FIBER_ESCAPE_CLASSIFICATION.md`. In the 3+7,z=4 fiber pattern (3,2,2,0), an all-aligned singleton-track completion is impossible. The empty-label source contributes at least 9 extra endpoints over the three small blocks, and none can land at the empty-track vertex in an aligned block. That leaves at most 12 small endpoints to fill the 21 surplus units of the seven empty-track vertices, so the outer-heavy incidence at track0 must be at least9. But total outer-heavy weight is x_T=7 and every extra edge is off the base matching, so track0 can receive at most7. Therefore any surviving completion must contain a switch duplicating the empty label or an aligned double-track pair involving empty label (only (3,0) or (2,0) are allowed). Still OPEN.


### Double-track alpha(R) obstruction and residual-type pruning

A 3+7 double-track outer vertex has `d_R=0), so any independent 4-set in R plus that vertex would be an independent 5-set in H. Hence double tracks require `alpha(R)<=3). Among the 18 registered residual path/cycle types, only `C3+P2+P2` at z=2; `2C3+K1`, `C3+P4`, `C5+P2` at z=3; and `C7`, `C3+C4` at z=4 have alpha3. All z=0,1 cells and all other residual types forbid double tracks. Added `V47_DOUBLE_TRACK_ALPHA_BLOCKER.md` and `verify_v47_double_track_alpha_pruning.py`; replayed arithmetic returned `V47_DOUBLE_TRACK_ALPHA_PRUNING_OK`.


### RETRACTION — small-to-outer matching rigidity (2026-10-29)

Audit found an invalid switch-label inference in `V47_37_SMALL_OUTER_MATCHING_RIGIDITY.md`. In the normalized 4,5,5 switch with `sigma=(0 1)), `extra_ac=(0,1)`, and `extra_bc=(0,0)`, the two extra edges hit distinct small-side labels. Therefore crossing endpoints cannot both be charged to one label, and the claimed global constancy of `p_D`, aligned/single-transposition dichotomy, and fiber-profile exclusions are withdrawn.

Added `V47_37_SMALL_OUTER_MATCHING_RIGIDITY_RETRACTION.md`; the original theorem file is now marked RETRACTED. The cut-endpoint lemma and its arithmetic verifier remain valid as standalone graph facts. The separate z=0,1 alignment proof is not based on the retracted argument.

### z=0,1 track-partition alignment and switch elimination

Added `V47_Z01_TRACK_ALIGNMENT.md`. The per-block mismatch identity is `y_D >= eta_D := sum_q |F_{s(q)} minus G_{g(q)}|). It follows by lower-bounding each q's residual degree by the union of its small-map fiber and its complete outer-track fiber; summing the four q vertices gives at least `7+eta_D), while the exact residual incidence count is `7+y_D).

- z=0: e(R)=3 forces three disjoint K2 fibers plus a singleton, and this clique partition is unique, so the small and outer partitions agree.
- z=1: e(R)=4 forces all four fibers on both sides nonempty. If the partitions differed, every outer block would have eta_D>=1 (including switch normal form), so y>=7, contradicting y=6. Hence the partitions agree.
- With F=G and all fibers nonempty, a switch is impossible: its two-extra-edge endpoint q_j must meet both F_s and F_j, giving d_R(q_j)>=2 while e_Q(q_j)>=2 forces d_R(q_j)<=1.

Therefore z=0,1 reduce to all-aligned singleton outer blocks. The aligned completions remain OPEN; no global Q32 closure is claimed.


### Restore missing z=4 arithmetic replay

The z=4 empty-fiber classification referenced a verifier that was absent from the branch directory. Added `verify_v47_z4_empty_fiber_escape.py`. The 1,000 possible three-block slack-vector profiles were checked in-session: `min E_0=9), `max(21-E_0)=12), so the seven q_0 vertices require 21 extra incidences, at least 9 of which would have to come from outer-heavy edges, exceeding `x_T=7). Result `V47_Z4_EMPTY_FIBER_ESCAPE_ARITHMETIC_OK`. Scope remains arithmetic-only.


### Close z=1 profile (3,2,1,1) via forbidden K13

After the z=1 small/outer partition alignment and switch elimination, the profile (3,2,1,1) makes the 10 pivot vertices of the size-three track plus its three residual vertices a target-color K13. This is forbidden because every 13-set in the balanced coloring must contain every color. Hence this profile is CLOSED. Only the z=0 and z=1 profiles (2,2,2,1) remain in the low-z 3+7 branch; z=1 has one extra residual cross edge, z=0 has none.


The counterexample was made reproducible in `verify_v47_37_switch_endpoint_counterexample.py`: exact enumeration of all 4096 subsets gives `alpha=4) and 63 maximum independent sets, output `V47_37_SWITCH_ENDPOINT_COUNTEREXAMPLE_REPRODUCED`. The global matching-rigidity claim remains retracted.


### Balanced-coloring cross-track ledger for aligned z=0,1 (2026-10-29)

Added `V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md` and `verify_v47_z01_cross_track_ledger.py`.

In the remaining aligned z=0,1 profile (2,2,2,1), the target-color tracks are K12,K12,K12,K11. For any outside vertex and a K12 track, the 13-set formed by the track plus that vertex must contain all eleven non-target colors among twelve cross edges; hence at most one edge can be H-colored. Therefore H[T_i,T_j] is a matching for each pair of K12 tracks. For a K11--K12 pair, only the K11-side degree-one bound is asserted.

Within-track edges contribute 253 of the 285 H-edges; cross-track H edges total 32. If E_0 is the aggregate small-block degree excess on the singleton-fiber label, then E_0 is 0,1,2,3 and the exact track degree sums force:
- K11-to-K12 edge total = 22+E_0;
- K12-to-K12 edge total = 10-E_0.

The six track-pair deficits sum to 37, matching the global reserve budget. Exact arithmetic checked 729 small-block excess triples and 28,107 necessary aggregate track-count states; output `V47_Z01_CROSS_TRACK_ARITHMETIC_OK`. The aggregate relaxation remains feasible and is not a closure.


### Aligned low-z Type-I component normal form — 2026-10-29

Added `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` and `verify_v47_aligned_typei_component_normal_form.py`.

The aligned z=0,1 residual profile (2,2,2,1) gives three target K12 parts and one K11 part. Every non-target color appears on edges from any vertex to each external K12 part, so its H-degree is at least two on K12 parts and at least three on K11. A triple-outside K5 has only one H-neighbor per H vertex, contradicting that floor. Double-outside K5s must have one H vertex in each K12 part and none in K11; single-outside K5s are transversals of all four parts.

This leaves x_C in O with one double/nine single components, or x_C in H with two doubles/eight singles. Exact gadget H-H edge counts become `12+g_C` and `15+g_C`, respectively. Arithmetic replay passed. This is a genuine Type-I placement reduction, not closure of z=0 or z=1.


Further refinement in `V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md`: on each K12--K12 pair, an H-matched vertex has exactly one edge of each non-target color into the opposite track; an unmatched vertex has 12 non-target edges, with exactly one color repeated. For every color C, `e_C(T_i,T_j)-12` equals the repeat-C count on either side, so the repeat-color counts must agree. On each K11--K12 pair, the analogous surplus over 11 counts repeats on the K11 side only. This records pairwise color-level constraints beyond the aggregate 37-unit gap.


Tightened the aligned z=0,1 cross-track ledger: for each pair of large tracks T_i,T_j, with k the remaining large label,
`e_H(T_i,T_j)=y_k-2-E_0-E_k<=9-E_0-E_k<=9`.
Thus every K12--K12 pair has at least three unmatched vertices on each side. The arithmetic verifier now asserts the exact identities and pairwise caps in all 28,107 aggregate states.


### Audit correction: Type-I K5 factor count and triple-placement status (2026-10-29)

A source audit found that the previous local write-up incorrectly counted the two special K5 cliques N_s,N_t inside G11 as if they were isolated components. The true placement profile covers twelve K5 factors: ten isolated K5s plus the two special K5s within G11. Therefore the previous conclusion “triple placement impossible” was too strong and is withdrawn.

The valid balanced-coloring floor shows that an isolated triple-outside K5 is impossible. Thus, if triple placement occurs, its triple K5 must be one of N_s,N_t; the other special K5 is single-outside, forcing `b_s+b_t=4` and G11's composition to be four O vertices and seven H vertices. The corrected exact H-edge accounting is: K5 interiors 69/66/67 in x-in-O/two-double/triple cases, with extra H-H gadget edges `G_H=g_C`, `3+g_C`, `2+g_C` respectively. The corrected arithmetic replay passed. This is a necessary restriction, not a triple-placement closure.


### Triple-special geometry and exact gap — 2026-10-29

Within the corrected source accounting, the aligned triple-placement case is sharpened further. The triple K5 must be special; its companion special K5 is single-outside. The distinguished y must be H, or x together with the four H vertices of N_t\{y} forms a forbidden C-colored K5 in H. The four H vertices of N_t then occupy all four clique parts; x must be in y's K12 part. The two H vertices of the triple N_s occupy the other two K12 parts. Counting the nine extra gadget edges gives exactly five H-H edges, so `e_C(H)=67+5=72) and `g_C=3). Arithmetic replay returned `V47_CORRECTED_TYPEI_PLACEMENT_ARITHMETIC_OK`. This is a strict local normal form, not exclusion of the triple placement.


### All exact-color gaps capped at 3; nonexact color forced to 76–90 H-edges

The corrected aligned-cell analysis now gives `g_C<=3) for every exact color. In the x_C-in-O case only y--A_0 edges can be H-H; in the two-double x_C-in-H case the both-special-single subcase is impossible, while all surviving subcases have `g_C<=3); triple placement has exact `g_C=3).

With ten exact colors and total gap 37, the unique nonexact color has `7<=g_D<=21), so `76<=e_D(H)<=90). The upper bound uses the 14 O vertices: each must have at least one D edge into each of the three K12 cliques, giving at least42 H-O D-edges; the 132-edge total then yields `g_D<=21). Thus at least six exact colors have positive gap. The updated arithmetic replay passed. The remaining nonexact interval is still feasible on these counts alone.


### Nonexact color: sharpened to g_D in [7,19], e_D(H) in [76,88]

Added the shell-independent-set argument for the unique 132-edge color D. Since p has no D-edge to the 13-point shell A and alpha(D)<=12, alpha(D[A])<=11; therefore D[A] has at least p_11(13)=2 edges. Combined with e_D(H,O)>=42 and e(D)=132, this improves the previous necessary range to `7<=g_D<=19`, `76<=e_D(H)<=88`, `2<=mu_D<=14). The ten exact colors must contribute at least18 of the 37 gap units, so at least six have positive gap. Arithmetic replay passed; no contradiction yet.


### Exact factor-occupancy equations across (12,12,12,11) parts

The corrected Type-I file now uses the fact that twelve K5 factors partition all vertices other than x_C. Counting H vertices in each target part gives exact occupancy vectors:
- x_C in O: double factor = (1,1,1,0);
- x_C in H two-double with x_C in X_0: the two doubles total (2,2,2,0);
- x_C in H two-double with x_C in a K12: the two doubles total (1,2,2,1), forcing the X_0-containing double to be special;
- x_C in H triple: x_C cannot be in X_0, and the triple H pair lies in the other two K12 parts.

These are source-correct counting identities; the updated verifier passed. They leave the aligned cell OPEN.


### Residual 1-factorization across the K12 tracks — audit correction (2026-10-29)

Added `V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION.md`. The first draft incorrectly called the residual factor canonical and described a repeated-color edge as uniquely determined. A vertex with a repeated color has two edges of that color, so the distinguished edge depends on the selected baseline matching.

The corrected proof chooses one perfect matching for each non-target color by Hall. These eleven matchings are edge-disjoint and leave a perfect matching P. P contains all H edges and all color edges not selected in their color's baseline matching. Hence each K12xK12 pair has a valid 1-factorization, but P may depend on the choices. The color-C edges in P number `e_C(T_i,T_j)-12`; each P has at least three H-edges and three repeat-color edges because `e_H(T_i,T_j)<=9`.

For each K11--K12 pair, every color has a matching saturating T0; the residual set has one edge per T0 vertex but is not asserted to be a matching on the larger side. The file also records the aligned 69/70 low-gap orientation. These are exact structural constraints, not a Q32 closure.


### T0 pointwise color-degree saturation — 2026-10-29

Added **V47_T0_POINTWISE_COLOR_SATURATION.md** and **verify_v47_t0_pointwise_color_saturation.py**.

For each vertex v in the K11 track T0, the exact non-target H-degree sum is \(34-\epsilon_v\), while each of the eleven non-target colors must contribute at least one edge to each of the three K12 tracks. Hence a vertex with epsilon=1 has color degrees exactly 3 across all eleven colors; a vertex with epsilon=0 has exactly one color degree 4 and ten color degrees 3. Summing yields \(\sum_C t_C=11-E_0\).

For an exact Type-I color, any degree-four T0 vertex must lie in its 11-vertex gadget G11(C); isolated single factors contribute degree 3, and isolated double/triple factors at T0 are forbidden by the degree floor. The corrected factor occupancy bounds \(|G11(C)\cap T_0|\le2\), hence \(t_C\le2\) per exact color. The arithmetic replay passed (**V47_T0_POINTWISE_COLOR_SATURATION_ARITHMETIC_OK**). This is a local capacity constraint, not Q32 closure.


### T0 pointwise color-degree saturation — 2026-10-29

Added **V47_T0_POINTWISE_COLOR_SATURATION.md** and **verify_v47_t0_pointwise_color_saturation.py**.

For each vertex v in the K11 track T0, the exact non-target H-degree sum is \(34-\epsilon_v\), while each of the eleven non-target colors must contribute at least one edge to each of the three K12 tracks. Hence a vertex with epsilon=1 has color degrees exactly 3 across all eleven colors; a vertex with epsilon=0 has exactly one color degree 4 and ten color degrees 3. Summing yields \(\sum_C t_C=11-E_0\).

For an exact Type-I color, any degree-four T0 vertex must lie in its 11-vertex gadget G11(C); isolated single factors contribute degree 3, and isolated double/triple factors at T0 are forbidden by the degree floor. The corrected factor occupancy bounds \(|G11(C)\cap T_0|\le2\), hence \(t_C\le2\) per exact color. In addition, \(t_C\) is exactly the sum of the three T0--K12 pair surpluses, so \(t_C\le g_C\); therefore \(t_C\le\min(2,g_C)\) for exact colors. The aggregate big-pair surplus is exactly \(26+E_0\). The arithmetic replay passed (**V47_T0_POINTWISE_COLOR_SATURATION_ARITHMETIC_OK**). This is a local capacity constraint, not Q32 closure.


### Exact residual holonomy-cost theorem (2026-10-29)

Added `V47_Z01_RESIDUAL_HOLONOMY_COST.md` and `verify_v47_z01_residual_holonomy_cost.py`.

When all ten isolated K5 components are single-outside, they yield ten transversal K4s and a seven-vertex residual of profile (2,2,2,1), with a nine-edge baseline and at most three matching-constrained extras. This condition is not automatic: an isolated double-outside factor is source-correct and leaves nine isolated K4s plus an isolated K3, with an eight-vertex G11 residual of profile (2,2,2,2) and 12+g_C edges. See V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md.

Exhaustive enumeration classified 8 baselines as aligned K4+K3 (alpha2), 24 as aligned-large-pair but T0-misaligned (alpha3), 24 as six-cycle holonomy with alpha3, and 8 as six-cycle holonomy with alpha4. The minimum extra-edge costs to reach alpha<=2 are respectively 0,1,2,3. Repair counts at minimum cost are 8,24,72,72. Full repair counts were also checked for gaps 0..3. The equivalent Python enumeration returned `V47_Z01_RESIDUAL_HOLONOMY_COST_OK`.

New consequence: for every exact color, nontrivial six-cycle holonomy requires g_C>=2; the worst six-cycle attachment requires g_C=3. Hence g_C<=1 forces aligned large-part matching composition. This remains a local result, not a full Q32 contradiction.


The residual holonomy verifier now checks the exact repair shapes. In class C, every minimum two-edge repair includes a mandatory edge joining the common pair of two independent triples, plus one of three edges in the disjoint large-track triple. In class D, the unique independent 4-set is T0 plus a transversal triple V; T0 is attached in the baseline to the complementary triple U. Each of the nine minimum repairs uses one edge inside U, one T0-to-V edge, and the edge joining the other two vertices of V.

Added `V47_Z01_EXACT_COLOR_RESIDUAL_GRAPH_CATALOG.md` and its verifier for the all-isolated-single-outside subcase only. The first seven-vertex catalog counts were 8,72,384,1,148; after enforcing the T0 degree cap, the corrected counts are 8,72,360,1,000. The source-correct isolated-double branch is now separated in `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md`; therefore neither the 7-vertex counts nor the 64-baseline holonomy classes may be applied to every exact color without first checking its placement.

### Residual-placement audit correction — 2026-10-29

A source-correct 69-edge placement in HIGH_SUPPORT_NEAR_TURAN.md, Section 3, places the unique double-outside K5 in an isolated component. This contradicts the earlier unqualified assertion that every exact color's ten isolated K5s yield ten H-K4s. The 7-vertex residual graph catalog and 64-baseline holonomy table are therefore conditional on all ten isolated components being single-outside.

Added V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md and its verifiers. If one isolated component is double-outside, the ten isolated H-components are 9K4 plus K3 (57 edges), the G11 H-residual has profile (2,2,2,2), and its edge count is 12+g_C. In the two-K4 low-gap placements, the global t_C<=1 theorem limits the relaxation to at most one T0-incident extra edge total, yielding counts 8,96,408,880. These supersede the per-T0-vertex-cap counts 8,96,480,1312 and the uncapped counts 8,96,528,1760. The x_C-in-H, y-in-H exceptional subcase has g_C=3 and is now shown to have t_C=1.

Updated the residual catalog, holonomy theorem, their verifiers' scope notes, canonical state, dependency DAG, and retraction firewall. The global g=0,1 orientation still follows from the separate near-Turan theorem. Root remains OPEN / NOT_CERTIFIED.


### Residual-enumerator audit correction: T0 degree cap and placement scope (2026-10-29)

The seven-vertex catalog and holonomy-cost theorem are conditional on all ten isolated Type-I K5 components being single-outside. The separate source-correct isolated-double placement leaves nine isolated H-K4s plus one isolated H-K3 and an eight-vertex residual (2,2,2,2); that branch is not covered by the seven-vertex enumerators.

A further pointwise cap was missing from the first enumerator versions. In the seven-vertex subcase, the T0 residual singleton has three baseline C-edges, and every T0 vertex has C-degree exactly 3 or 4 by balanced-coloring saturation. Therefore at most one extra C-edge can touch T0 across all three T0--Ti pairs. Both verifiers now enforce this. Independent re-enumeration confirms corrected seven-vertex graph counts 8,72,360,1000 for gaps 0–3, with K4+K3-base counts 8,72,264,520 and non-base counts 0,0,96,480. Corrected holonomy repair counts: A=(8,72,264,520), B=(24,216,696), C=(72,720), D=72 at their respective allowed gaps. The minimum costs 0/1/2/3 and the class-C/D mandatory-edge repair patterns are unchanged. This is a conditional local correction, not Q32 closure; the isolated-double branch remains open.

### Isolated-double residual enumeration tightened by T0 saturation (2026-10-29)

Updated `V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md` and its graph verifier. The global t_C<=1 theorem permits at most one T0-incident extra edge across the two-K4 residual, not one per T0 vertex. Of the 12 cross-K4 edges, six are T0-incident and six join large tracks; the per-base counts are 1,12,51,110, giving 8,96,408,880 across eight unordered bases. This supersedes both the previous per-T0-vertex-cap counts 8,96,480,1312 and the uncapped counts 8,96,528,1760. The source star restriction further implies g_C<=1 if its center is in T0. Independent Python enumeration reproduced the counts; no global Q32 closure is claimed.

### Audit correction: isolated-double exceptional branch (2026-10-29)

A proposed closure of the entire `x_C in H, y in H` isolated-double branch was retracted. The cross-track ledger gives each large-track vertex one H-neighbor total outside its own track, not one H-neighbor into every other track. The argument relying on a per-pair degree-one condition was invalid.

The sound conclusion is limited to the T0-centered subcase: if `x_C,y in T0`, each already has three C-neighbors in H, so pointwise saturation allows at most one extra C-edge per center; the three required gadget edges cannot fit into total capacity two. This subcase is CLOSED; the large-track-centered exceptional subcase remains OPEN.

### Placement-sensitive T0 repeat-owner bound — 2026-10-29

The T0 saturation identity plus the full Type-I placement split now proves t_C<=1 for every exact color. This holds in the all-isolated-single seven-vertex branch and the isolated-double two-K4 branches, where the gadget extras form a star centered at y or x_C. It also holds in the exceptional isolated-double two-double placement x_C in H, y in H: if exactly one of x_C,y lies in T0, an x_C--(N_t minus {y}) edge would lie inside a target clique; if both lie in T0, their degrees would be 3+(3-k) and 3+k for k=|A0 intersect H|, impossible to keep both at most four. Hence x_C,y lie in large tracks, the T0 vertex in the special K3 has degree 3, and the T0 vertex in the special K4 has degree 4. This exceptional case has b_s+b_t=3 and g_C=3, but t_C=1, not 2. The total one-extra-edge cap across all three T0--Ti pairs is therefore global for exact colors. The verifier now checks the case-split arithmetic; no contradiction or Q32 closure is claimed.


### Exact surplus-location split by residual holonomy class (2026-10-29)

Extended the capped holonomy verifier to count valid repairs by `(class, g_C, T0-pair surplus, large-pair surplus)`. This yields additional forced placements: class B at minimum gap 1 must use a T0-pair edge; class C at minimum gap 2 has no T0 surplus and places both edges on large-track pairs; class D at gap 3 has one T0 surplus and two large-pair surpluses. The full table is in `V47_Z01_RESIDUAL_HOLONOMY_COST.md`; independent enumeration reproduced the split counts. These are local constraints only.

### Aggregate exact-color large-pair surplus budget (2026-10-29)

Derived and recorded in `V47_T0_POINTWISE_COLOR_SATURATION.md` the identity `L_exact=26+E0-(g_D-t_D)` for exact-color surplus on large-track pairs. The global bounds `g_D<=19` and `t_D>=max(0,1-E0)` imply `L_exact>=8,8,9,10` for `E0=0,1,2,3`. This is a small but exact cross-track budget constraint that can be combined with the per-color residual surplus splits; no global contradiction follows yet.

Sharpened the aggregate budget by conditioning on the nonexact gap: `L_exact>=27-g_D`, since exact-color gaps sum to `37-g_D` and exact colors own at most ten T0 surplus vertices. Combined with the E0-only bound, `L_exact>=max(27-g_D,8,7+E0)`. Thus g_D=7 forces at least 20 large-pair surplus edges on exact colors; g_D=19 leaves the E0-specific bounds 8,8,9,10.

### Large-pair surplus budget in the unresolved g_D<=17 branch — 2026-10-29

Combining the global exact-color T0 cap t_C<=1 with the existing gap split gives a new exact budget cut. If no exact color has gap 0 or 1, the ten exact gaps are 2 or 3. If k colors have gap 3, then g_D=17-k and the exact colors must contribute at least 10+k surplus edges across the three K12--K12 pairs. Since the total large-pair surplus is 26+E0, the nonexact color is limited to at most 16+E0-k such edges. This forces at least one large-pair repeat edge from every exact color, and at least two from each gap-three exact color. It narrows the next packing search but is not a contradiction.


### Clarify the shell-edge lower-bound theorem label — 2026-10-29

Audited the upper bound on the unique nonexact color D in V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md. The conclusion e_D(A)>=2 is correct, but the previous label p_11(13)=2 was a notation collision: p_r(n) denotes the Kang–Pikhurko second-Turán maximum in the external theorem, and its stated range does not include n=13. Replaced it with the direct independence argument (at most one edge in A would leave an independent 12-set, which together with p is a D-independent 13-set) and, equivalently, the ordinary Turán complement calculation C(13,2)-t_11(13)=78-76=2. No numeric bound or root status changes.


### Common P-factor packing and scalar-relaxation witness (2026-10-29)

Derived and documented the common large-track repeated-color graph S: each pair complement P_ij is a perfect matching containing H_ij, so S_ij=P_ij\\H_ij and `d_S(v)=2-d_H^large(v)<=2`; total |S|=26+E0. Exact-color-owned S edges must have both endpoints in that color's residual gadget set. This is the vertexwise edge-packing constraint absent from the scalar ledger.

Added a self-contained aggregate witness verifier. It confirms all nine class-B local vectors occur among 192 abstract repaired graphs, then filters them by the source complement law for (g,t0)=(2,1), leaving the three complementary pair-location patterns. At E0=0, E=(2,2,2), e_H=(4,3,3), capacities r=(8,9,9), q=(4,4,3), a source-aware aggregate witness uses exact surplus (2,4,4;4,4,2) and leaves D surplus (6,5,5;0,0,1), hence g_D=17. This still does not realize the shared P endpoint labels and is not a Q32 coloring.

### Source complement law for the class-B minimum-gap pattern — 2026-10-29

For a source-realizable single-outside class-B residual with g_C=2 and t_C=1, the special point x_C must lie in T0 and both special K5 factors are double-outside. The y-in-H placement forces A0 to contain exactly one H vertex; if y lies in T_i and that H vertex lies in T_j, then i≠j, the T0 repeat is on T0-T_k, and the large-pair repeat is on T_i-T_j, where {i,j,k}={1,2,3}. Thus the two repeat pairs are complementary.

Updated the shared-P packing note and aggregate verifier to impose this source-derived location law. The revised aggregate witness remains feasible: exact surplus (2,4,4;4,4,2), D surplus (6,5,5;0,0,1), g_D=17. This rules out only the previous pair-location assignment as source-compatible; it does not close the shared-endpoint packing problem.


### Retraction and replacement of the proposed class-B pair law — 2026-10-29

The previously logged universal complement law was too strong and is withdrawn. A source-correct counterexample exists with x_C outside H, N_s single-outside, N_t double-outside, and A_0={w,s_j}, where w is the T0 vertex and y lies in T_i: the two H-H gadget edges yw and ys_j yield g_C=2,t_C=1, and the valid class-B baseline can leave extras ws_i on T0-T_i and ys_j on T_i-T_j. These pair types share track i, so no universal complementary-pair rule holds.

The packing note and verifier now use an explicit source-compatible local mode and a corrected aggregate witness: exact surplus (7,0,3;4,3,3), D surplus (1,9,6;0,1,0), g_D=17. The verifier passed the independent Python replay with SOURCE_LOCAL_AGGREGATE_BUDGET_WITNESS_OK. This still omits common-P endpoint labels and does not close Q32.


### Audit correction: the purported Class-B counterexample is actually Class A — 2026-10-29

A fresh source-baseline audit found that the prior retraction of the Class-B complement law was based on misclassifying the local graph. In the \(x_C\in O\), \(N_s\)-single, \(N_t\)-double mode, the true nine-edge baseline is the K4 H-part of \(N_s\) plus the K3 H-part of \(N_t\). Its three T0 attachments all go to the K4 triangle (Class A). The gadget edges \(yw\) and \(ys_j\) are the two extras; \(ws_i\) is already a K4 edge. The graph has \(\alpha=2\), \(g_C=2,t_C=1\), and the shared-track pattern is genuinely source-realizable in Class A.

The Class-B-specific complementary-pair law remains valid under its own source contract: \(x_C\in T_0\), both special factors double-outside, \(y\in H\); then the T0 repeat is on \(T_0T_k\) and the large-pair repeat on complementary \(T_iT_j\). Updated the packing note and verifier to distinguish these modes. A clean local replay checked all six Class-A source patterns, each with \(\alpha=2\), and rechecked the aggregate witness: exact surplus (7,0,3;4,3,3), D surplus (1,9,6;0,1,0), \(g_D=17\). The common endpoint-labelled packing remains OPEN.


### Vertex-labelled common-P relaxation witness — 2026-10-29

Added verify_v47_z01_vertex_labelled_common_p_witness.py. It constructs six labelled 6-cycles on the 36 large-track vertices, giving shared perfect matchings P_ij; labels all large-pair P edges as H, exact-repeat, or D-repeat with counts H=(4,3,3), exact=(7,0,3), D=(1,9,6); and labels all 33 T0 complement edges with H counts (7,7,8) and repeat counts (4,4,3). Ten distinct T0 vertices own the ten exact repeats, each with a source Class-A K4+K3 residual gadget and one large repeat edge on the same track, giving g_C=2,t_C=1, alpha=2. The remaining T0 vertex owns D's repeat; D has 16 large repeats and g_D=17. A clean independent replay of the construction passed.

This is a vertex-labelled witness for the common-P and source-local residual relaxation, not a Q32 coloring. It does not construct the eleven simultaneous M_C,ij perfect matchings on the full 12x12 bipartite graphs or prove that their unions form the required triangle factors and ten isolated K4 components. The next attack must impose that global simultaneous triangle-factorization constraint.


### Owner-only relaxation collision audit and pair-projection injectivity — 2026-10-29

The six-cycle labelled witness was re-audited against the cross-color matching requirement. It is only an owner-only relaxation: cycle-owner multiplicities are (3,3,3,1), yielding 9 pairs of colors with identical residual six-sets and 36 duplicate claims on the same six baseline edges. Therefore it is not a feasible common-P color-matching packing; its value is to expose the exact missing constraint.

Proved the pair-projection injectivity lemma: if exact color C owns a large repeat edge in S_ij, P_ij has an edge inside R_i(C) x R_j(C). Since the two perfect matchings on this K2,2 block partition all four edges, at most one perfect matching on the block is disjoint from P_ij. Thus M_C,ij is forced on this block; any other exact color with the same residual subsets on tracks i,j would have the same M_C,ij edges, contradicting color edge-disjointness. The next solver must enforce this pair-projection injectivity and full cross-color matching disjointness. No global Q32 claim changes.


### Source-mode local audit and common-P construction retraction — 2026-10-29

Added `V47_Z01_TWO_DOUBLE_SOURCE_PATTERN_AUDIT.md` and its exact verifier. After fixing an unordered track-pair assertion, the independent replay passed 19 labeled cases: counts `{yO_a3:1, yO_a2:3, yH_a2:3, yH_a1:12}`. This certifies the local source incidence only for the subcase with all ten isolated K5s single-outside, both special K5 factors double-outside, and x in T0; it is not a global Q32 result.

Audit correction: the claimed 20 direct P_0i / own-K4-baseline overlaps were false; the candidate P edges use K3-side y vertices while the K4 baseline uses distinct s vertices. The verifier now asserts zero such overlaps. The owner-only construction is still invalid for two independent reasons: its T0-T3 H endpoint multiplicities are (8 edges, 5 distinct endpoints), with three T3 vertices receiving two H edges each, contrary to the aligned zero-slack cross-track degree-one contract; and it has 9 residual-signature collision pairs / 36 duplicate baseline-edge claims. The witness script remains a retraction audit, not a success certificate. Q32 remains OPEN / NOT_CERTIFIED.

### T0--Ti omitted-vertex conservation — degree-source correction (2026-10-29)

The universal identity d_P0i(v)=#{C:z_i(C)=v} remains exact. In the single-T0-residual seven-vertex Type-I mode, cancelling each exact color's own T0 repeat owner gives n_i(v)+1[z_i(D)=v]=h_i(v)+r_i^D(v).

The generic 13-set lemma does not bound H degree at a T_i vertex. However, the frozen aligned 3+7 zero-slack degree ledger gives each T_i vertex total H cross-track degree exactly one, so h_i(v)≤1 is valid under this contract. Accordingly, exact nonrepeat omissions are injective away from D-repeat endpoints; at a D-repeat endpoint multiplicity up to 1+r_i^D(v) is allowed. The earlier blanket withdrawal of this consequence was too broad; the unsupported step was its attribution to the asymmetric lemma alone.

Updated verify_v47_z01_t0_omission_conservation.py to enumerate binary H endpoint profiles and reran independently: 5,544 / 70,488 / 3,960 profiles for T1/T2/T3, with maximum omission multiplicities 1,2,1. The two-omission case occurs only on T2 at the D-repeat endpoint if it also has an H edge. The source-repeat cancellation is still not asserted for the isolated-double eight-vertex mode, and this does not close Q32.

### Forced Class-A repeat allocation — 2026-10-29

Enumerated the exact source allocation equations for the E0=0 scalar row under the all-Class-A source contract. With large-pair exact repeat totals (7,0,3) and T0 repeat totals (4,3,3), the unique solution is x12=4, x21=3, x32=3, all other xij=0. This forces the 7 P12 exact-repeat edges and 3 P23 exact-repeat edges to be vertex-disjoint within their respective perfect matchings. The corresponding T0-repeat endpoints are distinct within each track. Added verifier verify_v47_z01_class_a_repeat_allocation.py. This is a necessary local restriction, not a root contradiction.

### Residual six-set injectivity and P0 audit correction — 2026-10-29

Proved a conditional residual-signature injectivity lemma for the single-outside mode. If two colors shared the same six residual vertices, edge-disjointness would force opposite perfect matchings on all three K2,2 blocks; complementing all three toggles parity, so one color has a six-cycle. The local holonomy theorem gives that color g_C>=2, and t_C<=1 forces a large-pair repeat edge. Pair-projection injectivity then forbids the second color from sharing the residual pair. A six-cycle single-outside color's residual signature is therefore unique even against colors in other source modes. Added V47_Z01_RESIDUAL_SIGNATURE_INJECTIVITY.md and an 8-case parity verifier.

Corrected the separate owner-only witness audit: the previously reported 20 P_0i/K4-baseline overlaps do not occur. The source baseline edges are w-s_i,w-s_j,w-s_k; candidate complement edges are w-y_i,w-y_j,w-y_k, with y_j,y_k in the separate K3. The exact endpoint replay gives zero overlaps. The owner-only witness is still invalid due to 9 residual-signature collision pairs / 36 duplicate baseline-edge claims. No global Q32 closure is claimed.


### E0=0 endpoint support caps — 2026-10-29

Combined the omitted-vertex multiset identity with the aligned zero-slack H degree ledger and the forced all-Class-A repeat allocation. On T0-T1 and T0-T3, the nonrepeat exact omissions plus D's omitted vertex are all distinct and coincide with the H endpoint sets. On T0-T2, they are all distinct unless the unique D-repeat endpoint also receives an H edge, in which case exactly one endpoint can have multiplicity two. Because exact repeat owners are distinct within each track, the P0 endpoint-degree caps are (2,3,2) for T1,T2,T3; degree three on T2 requires exact-repeat, H and D-repeat incidence at the same vertex. Recorded in V47_Z01_SHARED_P_FACTOR_PACKING.md; still a necessary relaxation, not a Q32 closure.

### Class-B g=2,t=0 star-center incidence — 2026-10-29

From the exhaustive 19-case source audit, the x-in-H two-double Class-B row y∈H,a=2 has g_C=2,t_C=0 and its two large-pair surplus edges form a star centered at y, with one edge to each of the other two large tracks. Those are the two P_ij edges incident to y, so y has no H-neighbor in the other large tracks. Because y already has 11 neighbors in its K12 track and δ(H)≥12, it must be incident to at least one H edge from T0. This is a necessary source/degree incidence constraint for the CSP, not a contradiction.
