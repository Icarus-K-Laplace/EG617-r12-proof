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

Added `V45_M9_130_COLOR_DEGREE4_LOCAL_STRUCTURE.md`. For a 130-edge nonexact color D and a vertex v of degree4, the 56-point non-neighborhood has at least119 D-edges by the source-checked KP second-Turan bound at (56,11). The neighborhood S has either 5 edges with exactly2 S-to-N edges, or 6 edges with 0 or1 S-to-N edges. This local classification does not force the v45 W-pair edge; the earlier unsupported pair-rigidity inference is withdrawn. The arithmetic verifier returned `130_COLOR_DEG4_LEDGER_OK`.

## New v47 residual incidence-cover lemma

Added `V47_RESIDUAL_INCIDENCE_COVER.md`: for every independent k-set S in R, k<=4, and every pivot block Q_i, the union of H-neighborhoods from S into Q_i has size at least k. If a block has zero cross-edge slack (every r has exactly one neighbor in Q_i), its neighbor map partitions R into at most four cliques. For m=10, z<=5 forces an independent triple in R, activating the triple-cover constraint; z=6,7 remains a separate high-z cell. No v47 closure is claimed.

## 132-edge minimum-degree upgrade (2026-10-28)

`Q32_132_MINDEG3.md` proves `delta(D)>=3` for the unique132-edge nonexact color by excluding degrees0,1,2 with the (60,59,58)-point second-Turan bounds and the Kang–Pikhurko equality classification at (58,11). Therefore `L_10=3) and the pointwise surplus budget becomes `r_10=4), improving the full-support gadget quota to `q_z<=4). This strengthens the existing non-full-support m=10 contradictions but does not itself close full support v47.
