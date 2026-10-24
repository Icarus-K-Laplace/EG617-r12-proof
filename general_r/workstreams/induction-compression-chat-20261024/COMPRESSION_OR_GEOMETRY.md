# Compression-or-Geometry: Current Theorem and Exact Gap

Status: **Alignment-free residual witness dichotomy is proved; full graph-level contradiction and finite-geometry dichotomy remain OPEN.**

## 1. Exact alternatives

For a hypothetical counterexample to P(r), let I_i be the family of independent r-sets in color i.

For each eliminated color c:

- If the union of I_i over i != c has a transversal X of size at most 2r-1, then the robust compression criterion yields a counterexample to P(r-1).
- If not, its transversal number is at least 2r. The Noncompressible-Shell Theorem gives either three pairwise disjoint independent-set witnesses with forced colored cross-edges, or a tight 2r-point transversal in which every point has a private witness.

For a fixed merge c -> j, replace the hypergraph by

\[
\mathcal H_{c,j}=
\left(\bigcup_{i\notin\{c,j\}} \mathcal I_i\right)
\cup(\mathcal I_c\cap\mathcal I_j).
\]

A transversal of size 2r-1 is exactly a successful fixed-merge shell. If none exists, the same packing/tight-transversal alternative applies.

## 2. Quantitative witness overlap

When the matching number is two, the 2r private witnesses T_v have residual parts Q_v=T_v minus {v}, each of size r-1 in R=V minus X, where |R|=(r-1)^2. The overlap graph has independence number at most two, so Mantel's theorem implies at least r(r-1) distinct witness pairs intersect in R. Incidence counting gives a residual point contained in at least three witnesses.

See WITNESS_INTERSECTION_DENSITY.md. This does not force all overlaps to have size one or witnesses to share a designated color.

## 3. Conditional bridge from tight witnesses to low-slack blocks

Suppose X is the 2r-point minimum transversal, x_0 in X, and a color i != c has local slack 1<=s_i(x_0)<=r-2 on W=V minus {x_0}. Let P_1,...,P_r be the low-slack color-i clique blocks and Y=X minus {x_0}.

The set Y hits every independent r-set of G_i[W]. For any private witness T_v of color i with v in Y intersect P_a, T_v is an independent transversal of the P-blocks and its other r-1 points lie in residual parts B_b=P_b minus Y. Every u in B_a must have a color-i defect edge to T_v minus {v}; otherwise replacing v by u creates an independent r-set disjoint from Y. Hence |B_a|<=s_i.

If some B_a is empty, all color-i private witnesses are based in that one block. Otherwise every block hosting such a witness contains at least r-s_i points of Y, so the number of witness-hosting blocks is at most floor((2r-1)/(r-s_i)).

The small-slack classification sharpens this: if s_i=1, or if s_i=2 and r>=4, all private witnesses of color i are based in at most two blocks. The weighted blocker inequality applies to the residual defect graph when all B_a are nonempty.

Full proof: TIGHT_TRANSVERSAL_LOW_SLACK_BRIDGE.md. Weighted lemma and small-edge classification are in the K branch.

## 4. K-line global constraints now available

The finite-geometry branch has proved the universal excess floor

\[
a_i\ge r-1\quad\forall i,
\qquad
\sum_i(a_i-(r-1))=\frac{r(r-1)(r-2)}2.
\]

It has also proved the local degree-budget inequality

\[
\sum_{i:s_i(x)\le r-2}(2r-s_i(x)-1)\le r^2,
\]

so the number of colors with slack at most s is bounded by floor(r^2/(2r-s-1). These are genuine global/local constraints, but neither implies that a low-slack color occurs at a vertex x_0 in the tight transversal X.

Canonical proof and graph-level sharpness note: [K-line LOW_SLACK_COORDINATIZATION.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/workstream/general-r-finite-geometry-20261024/general_r/workstreams/finite-geometry-chat-20261024/LOW_SLACK_COORDINATIZATION.md).

## 5. Exact remaining gap

The old J/K neighborhood-low-slack bridge has an impossible premise under the full counterexample contract: K's Local Slack Gap Theorem gives s_i(x)>=r-1 for every x,i. The live Case B route is instead the alignment-free residual-excess theorem in ALIGNMENT_FREE_WITNESS_RIGIDITY.md, which extracts a q-net from R=V minus X. That net is genuine geometry, but its blocks are not shown to lie in a deletion shell and it does not yet imply a contradiction.

The abstract hypergraph example with two disjoint clusters of all r-subsets still shows that matching/transversal data alone are insufficient to force affine geometry.

## 6. Current verdict

- Exact robust compression criterion: PROVED.
- Exact fixed-merge criterion: PROVED.
- No-shell => packing or tight critical transversal: PROVED.
- Tight case => at least r(r-1) intersecting witness pairs: PROVED.
- Tight case => common residual hub in at least three witnesses: PROVED.
- Tight case + aligned low-slack color => witness-block concentration and weighted blocker: PROVED.
- Small-slack aligned case (s=1 or s=2, r>=4) => at most two witness-hosting blocks: PROVED.
- Universal K-line excess floor and local degree budget: PROVED.
- Existence of a full-counterexample neighborhood color with slack s_i(x)<=r-2: IMPOSSIBLE by K's Local Slack Gap Theorem; the earlier aligned bridge is conditional but vacuous under the full contract.
- Case B => residual q-net with at least ceil(q/2) orthogonal directions (q=r-1): PROVED.\n- No-shell => a deletion shell containing the net blocks: NOT PROVED.
- Kakeya contradiction: NOT AUTHORIZED; the net blocks have not been shown to be shell-hitting objects.
- Alignment-free residual budget/dichotomy and same-color symmetric-difference matchings: PROVED in ALIGNMENT_FREE_WITNESS_RIGIDITY.md.\n- Case A colored-packing budget and small-r label audit: PROVED but noncontradictory in COLORED_WITNESS_EDGE_BUDGET.md.\n- P(r) => P(r-1): NOT ESTABLISHED.


## 7. Alignment-free residual witness theorem (new)

In Case B, let R=V minus X and b_i=e(G_i[R])-m_{r-1} for i != c. The exact residual budget gives

\[
b_i\ge0,\qquad \sum_{i\ne c}b_i\le \binom{r-1}{2}.
\]

Consequently either a repeated witness color has b_i<=r-3, in which case the complement-Turan/Brouwer argument gives a q=r-1 clique partition of R and every residual witness of that color is a transversal; or one color appears on at least four private witnesses. The latter follows because if every repeated color had b_i>=r-2, at most floor((r-1)/2) colors could repeat, leaving insufficient slots to distribute 2r witness roots with every class of size at most three.

For every same-color pair, the graph on the symmetric differences has a perfect matching by Konig's theorem and the independence-number cap. A duplicate-safe incidence inequality records how many witness pairs one physical edge can serve. These are graph-level constraints, but neither branch is yet contradictory.

The separate Case A packing inequalities count disjoint edge classes correctly; their r=3,4,5 evaluations remain below the universal color-edge floor and therefore do not close the packing branch.


## 8. First high-excess threshold interface

In the alignment-free Case B alternative, if the repeated witness color has residual excess b_i=q-1 (q=r-1), K's Kang–Pikhurko classification gives an exact finite normal form; see K branch commit b20a3dde117facb37e78c2311160a149e578b27c, Theorem K.RM4.

Either G_i[R] is a q-clique partition plus q-1 cross-block color-i edges, or a single exceptional point can be deleted to leave q clique blocks (sizes q except one q-1) plus a nonempty star of cross-block color-i edges. The exceptional point has residual color-i degree 2q-2-a for 1<=a<=q-1.

This is a finite incidence kernel at equality, not a contradiction. If b_i>=q, the exact extremal classification does not apply directly.


## 9. Exact small-parameter kernel at r=7

For q=r-1=6, the finite-geometry branch proves an exact Case B profile (K branch commit eb238d01b9aebf98a7614dba00e2696a2f3d05cf): three zero-excess orthogonal directions, three non-q-partite colors at b_i=q-1=5 with exceptional-star normal forms, and the omitted color's seven clique blocks of sizes 6,5,5,5,5,5,5. The size-6 block is a transversal of the 3-net and the six size-5 blocks are near-transversals.

This is a genuine finite incidence kernel, but not yet an excluded one. The absence of an orthogonal mate for order 6 cannot be applied directly, because the kernel supplies one full transversal plus six near-transversals, not six disjoint full transversals.
