# CHAT J — Induction / Compression in r

Branch: workstream/general-r-induction-compression-20261024

Scope: parameter compression r -> r-1 or r-c. Do not duplicate residual-core extraction or backend repivot work.

## Current status

**J1: achieved.** The exact shell criteria and the first noncompressibility structure theorem are proved.

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

## New theorem: noncompressible shell => packing or tight critical transversal

For a fixed c, let H_{-c}=union_{i != c} I_i. If no robust shell of size 2r-1 exists, then tau(H_{-c})>=2r.

For every r-uniform hypergraph, tau <= r nu because the union of a maximal matching is a transversal. Hence H_{-c} has a matching of size at least two.

- If its matching number is at least three, there are three pairwise disjoint independent r-sets S_a in colors i_a != c. The counterexample property forces at least r edges between S_a and S_b in each distinct designated color among {i_a,i_b}; every outside vertex has at least one edge of color i_a into each S_a.
- If its matching number is exactly two, the union X of any maximum matching has size 2r and is a minimum transversal. Every v in X has a private witness independent r-set T_v in some color i_v != c with T_v intersect X={v}.

The same theorem applies to the fixed-merge hypergraph. The complete proof and colored-incidence inequalities are in NONCOMPRESSIBLE_SHELL_THEOREM.md.

## Geometry audit

This is a genuine hypergraph-structural result, but not yet a geometric theorem. The packed independent sets are disjoint, not line-like blocks with pairwise intersections at most one. An abstract r-uniform hypergraph can have tau=2r and nu=2 without any affine geometry. Therefore no Kakeya bound is currently licensed.

The missing bridge is graph-specific: upgrade the colored domination/private-witness constraints to many blocks with proved intersection constraints, or construct a shell directly.

## Affine-model obstruction

For the standard affine-plane coloring on r^2 points, reducing the independence number of t surviving single-direction colors requires deleting one full line from each direction. If those lines have pairwise intersections at most one, then |X| >= tr-C(t,2). This rules out a purely hereditary 2r-1 shell for the indicated affine model when r>=5, but it is not a counterexample to P(r), because the affine coloring is known not to extend to r^2+1 points.

## Deliverables and latest status

- COMPRESSION_CRITERION.md: corrected adaptive-recoloring caveat and exact fixed-merge criterion.
- NONCOMPRESSIBLE_SHELL_THEOREM.md: proved packing / tight-transversal alternative.
- COMPRESSION_OR_GEOMETRY.md: exact theorem boundary and the missing geometry bridge.
- P(r) => P(r-1): **not established**.
