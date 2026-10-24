# CHAT J — Induction / Compression in r

Branch: workstream/general-r-induction-compression-20261024

Scope: parameter compression r -> r-1 or r-c. Do not duplicate residual-core extraction or backend repivot work.

## Current status

**J1: achieved.** The exact shell criteria and the noncompressibility packing/tight-transversal theorem are proved.

**J2/J3/J4: OPEN.** No theorem yet proves that a hypothetical counterexample at r yields one at r-1.

## Exact compression criteria

Let I_i be the r-uniform hypergraph of independent r-sets in color graph G_i.

- Robust compression after deleting X and eliminating color c is guaranteed if X hits every I_i for i != c. This is sufficient for arbitrary recoloring of surviving c-edges, not an iff.
- For a fixed merge c -> j, success is equivalent to X hitting
  \[
  \left(\bigcup_{i\notin\{c,j\}} I_i\right)\cup(I_c\cap I_j).
  \]
  This checks every untouched color and the merged color exactly.

The shell size is 2r-1 because r^2+1-(2r-1)=(r-1)^2+1.

## Noncompressible shell => packing or tight critical transversal

For a fixed c, let H_{-c}=union_{i != c} I_i. If no robust shell of size 2r-1 exists, then tau(H_{-c})>=2r.

- If the matching number is at least three, there are three pairwise disjoint independent r-sets S_a in colors i_a != c. The counterexample property forces at least r edges between S_a and S_b in each distinct designated color among {i_a,i_b}; every outside vertex has at least one edge of color i_a into each S_a.
- If the matching number is exactly two, the union X of a maximum matching is a minimum transversal of size 2r. Every v in X has a private witness T_v independent in some color i_v != c with T_v intersect X={v}; its other r-1 vertices lie in R=V minus X.

For r>=3, pigeonhole gives at least three private witnesses of the same designated color. Since no three witnesses can be pairwise disjoint, at least two of these same-color witnesses overlap in R. For same-color independent r-sets A,B with intersection size h, there are at least r-h cross-edges between A minus B and B minus A.

## Quantitative witness overlap

In the matching-number-two case, the overlap graph on the 2r private witnesses has independence number at most two. Mantel's theorem gives at least r(r-1) distinct intersecting witness pairs. Incidence counting also forces a point of R to belong to at least three private witnesses. See WITNESS_INTERSECTION_DENSITY.md.

## Conditional bridge to low-slack geometry

See TIGHT_TRANSVERSAL_LOW_SLACK_BRIDGE.md.

Assume the tight case, choose x_0 in X, and suppose a color i != c has low slack 1<=s_i(x_0)<=r-2 on W=V minus {x_0}. Its r clique partition P_1,...,P_r and residual parts B_a=P_a minus (X minus {x_0}) obey:

- every block hosting a private witness of color i contains at least r-s_i points of X minus {x_0};
- hence the number of blocks that can host such witnesses is at most floor((2r-1)/(r-s_i));
- for s_i=1, or s_i=2 with r>=4, the exact blocker classification strengthens this to at most two witness-hosting blocks;
- if all residual parts B_a are nonempty, the color-i defect graph on them has no independent transversal and satisfies the weighted obstruction inequality.

The K branch also proves a universal global excess floor a_i>=r-1 for every color and a local degree-budget inequality for the number of low-slack colors at a vertex. These do not guarantee a low-slack color at a vertex x_0 in X. See the K branch LOW_SLACK_COORDINATIZATION.md.

## Geometry audit

The packing/private-witness structure and the conditional low-slack interface do not yet imply affine geometry. There is no proved pairwise-intersection-at-most-one property for blocks and no three-direction family. No Kakeya bound is currently licensed.

## Affine-model obstruction

For the standard affine-plane coloring on r^2 points, reducing the independence number of t surviving single-direction colors requires deleting one full line from each direction. If those lines have pairwise intersections at most one, then |X| >= tr-C(t,2). This rules out a purely hereditary 2r-1 shell for the indicated affine model when r>=5, but it is not a counterexample to P(r), because the affine coloring is known not to extend to r^2+1 points.

## Deliverables and latest status

- COMPRESSION_CRITERION.md: corrected adaptive-recoloring caveat and exact fixed-merge criterion.
- NONCOMPRESSIBLE_SHELL_THEOREM.md: proved packing / tight-transversal alternative and same-color overlap consequence.
- WITNESS_INTERSECTION_DENSITY.md: proved at least r(r-1) intersecting witness pairs and a common residual hub.
- TIGHT_TRANSVERSAL_LOW_SLACK_BRIDGE.md: proved conditional witness-block concentration, small-slack support, and weighted blocker interface.
- COMPRESSION_OR_GEOMETRY.md: theorem boundary and exact missing bridge.
- P(r) => P(r-1): **not established**.


## Round 2 — alignment-free residual witness rigidity

New proof asset: ALIGNMENT_FREE_WITNESS_RIGIDITY.md.

- **Residual edge budget (PROVED):** in Case B, with R=V minus X, |R|=(r-1)^2, and b_i=e(G_i[R])-(r-1)C(r-1,2), every b_i>=0 and sum_{i!=c} b_i <= C(r-1,2).
- **Alignment-free dichotomy (PROVED):** either a repeated witness color has b_i<=r-3, giving a q=r-1 clique partition of R and making all its residual witnesses transversals; or some witness color occurs at least four times.
- **Same-color witness rigidity (PROVED):** for every same-color pair, both the residual symmetric difference and the full witness symmetric difference have perfect matchings. An edge-ownership inequality counts repeated use of the same physical edge without double-charging it.
- **Case A colored-packing budget (PROVED):** see COLORED_WITNESS_EDGE_BUDGET.md. The exact per-color bound and r=3,4,5 label-pattern audit do not exceed the known full-color floor, so Case A remains open.
- **Fixed merge (OPEN):** see FIXED_MERGE_ESCAPE.md for the exact private-witness criterion and a pure-hypergraph obstruction; neither proves nor refutes a graph-level fixed-merge theorem.

Important cross-line correction: K's Local Slack Gap Theorem proves that under the full hypothetical-counterexample contract, every neighborhood slack s_i(x)>=r-1. Thus the earlier J/K bridge requiring s_i(x_0)<=r-2 at x_0 in X has an impossible premise in a full counterexample. It remains a valid conditional lemma, but the alignment-free residual theorem above is the live route: its excess b_i is measured on R, not on a full neighborhood V minus {x}.

Current verdict: no full graph-level contradiction, no guaranteed fixed merge, and no not-P(r) => not-P(r-1) theorem yet.


## Round 2 — residual multinet extraction

The strongest new geometry-facing result is Theorem J.W5 in ALIGNMENT_FREE_WITNESS_RIGIDITY.md (source commit 009a546cf0d66e4060a601bba168674214e7ac6c).

In Case B, q=r-1 and R=V minus X has q² vertices. The residual excess budget is sum_{i!=c} b_i<=C(q,2), so at least ceil(q/2) of the q colors i!=c have b_i<=q-2. For q>=3, Brouwer's threshold gives q-clique partitions on R for each such color; any two partitions are orthogonal. Thus the tight-transversal case unconditionally extracts a q-net with at least ceil(q/2) directions.

This does not rely on the now-vacuous neighborhood-low-slack bridge. Residual excess b_i on R is distinct from full-neighborhood slack s_i(x), which K proves is always >=r-1.

Exact design interface: N(q)>=ceil(q/2)-2 MOLS(q). For r=11, Case B implies three MOLS(10), an open question, not a contradiction. If the omitted color c also has alpha(G_c[R])<=q, the budget forces a full affine plane of order q; extension by X remains open.

Current theorem boundary unchanged: Case A is not closed, Case B is not contradicted, no fixed merge is guaranteed, and not-P(r) => not-P(r-1) remains unproved.


Threshold refinement: if the repeated witness color in the high-excess branch has b_i=q-1, K's exact Kang–Pikhurko interface gives a finite normal form (q-clique partition plus q-1 defects, or one exceptional point and a defect star after deletion). Exact source: K branch commit b20a3dde117facb37e78c2311160a149e578b27c, RESIDUAL_MULTINET_EXTRACTION.md, Theorem K.RM4. This remains a structured kernel, not a contradiction; b_i>=q remains unclassified.


Special fixed-parameter consequence: K's Theorem K.RM5 (commit eb238d01b9aebf98a7614dba00e2696a2f3d05cf) gives an exact Case B profile at r=7: three zero-excess directions, three exceptional-star colors with b_i=5, and the omitted color's seven clique blocks of sizes 6,5,5,5,5,5,5. The size-6 block is a transversal of the 3-net and the six size-5 blocks are near-transversals. This is a finite incidence kernel, not yet a contradiction.


Audit correction: the r=7 Case B's 3-net plus one-transversal/six-near-transversal design subkernel is realizable; see K branch commit 825c48ae4e5cc47e7feb6abab6337de62db6fd6c. It is not a full graph-level EG617 counterexample, but prevents claiming that the Latin-square partition alone is contradictory. The high-color exceptional-star and root/witness constraints are still the live gap.


## Round 2 decisive subresult — Case B equality eliminated

Theorem J.W8 (in ALIGNMENT_FREE_WITNESS_RIGIDITY.md, commit c0c31e82b2bd8b4c3c5a7ab6092b660d16bd686b) proves that in any full hypothetical counterexample with a tight-transversal Case B and r>=5,

\[
\sum_{i\ne c}b_i\le\binom{r-1}{2}-1.
\]

Equality would force the c-color graph on R to be q+1 disjoint cliques of sizes q and q-1 (q times), and every root must fully c-dominate one block. The block capacities sum to 2q+1, fewer than |X|=2q+2, contradiction.

Consequently at least ceil((q+1)/2) residual colors have pairwise orthogonal q-clique partitions. At r=7 (q=6), four directions would give two orthogonal Latin squares of order 6, impossible. **Case B is closed at r=7.** Case A (matching number at least three) remains open, so the full compression implication is not yet proved.
