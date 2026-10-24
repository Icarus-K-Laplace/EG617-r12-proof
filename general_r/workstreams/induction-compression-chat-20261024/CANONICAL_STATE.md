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

This is a proved J/K interface, but it is conditional: no theorem yet guarantees a low-slack color at a vertex x_0 in the tight transversal X.

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
