# Stability Conjecture — corrected formulation

## KILLED formulation

The following naive target is false if “distance” means edge recolorings to one standard affine coloring:

> every balanced coloring on `r^2-O(r)` or `r^2` vertices is `O(r)` / `o(r^2)` edits from the standard construction with one heavy color.

Reason: an affine plane supports arbitrary recoloring of every edge in the leftover parallel class `Q`, while preserving balance. There are `Theta(r^3)` such edges.

## Correct invariant: partition skeleton

The stability object should forget the exact colors on leftover edges and recover a system of near-orthogonal partitions.

### Skeleton Stability v1

For sufficiently large `r`, let `C` be a balanced `r`-coloring on at least `r^2-Cr` vertices. Then after deleting `O_C(r)` vertices (or another explicitly controlled defect set), there exist many colors `i` with a partition of almost all remaining vertices into `r+O_C(1)` color-`i` cliques of size `r+O_C(1)`, and the partitions are pairwise almost orthogonal.

This is still conjectural.

### Skeleton Stability v2 — counterexample-specific

A more relevant form avoids classifying all balanced `K_{r^2}` colorings:

> If `C` is the restriction of a hypothetical balanced coloring of `K_{r^2+1}` obtained by deleting one vertex, then `C` contains an `r`-net skeleton (or at least enough of one to invoke a robust version of the matching-preclusion nonextension argument).

The extension hypothesis is extra information and should be exploited; classifying arbitrary sharp examples is unnecessarily strong.

### Common-deletion perfection target

The strongest clean sufficient theorem is:

> In every hypothetical balanced coloring of `K_{r^2+1}`, there exists a vertex `x` such that, for every color `i`, `C_i-x` contains a spanning partition into `r` monochromatic `K_r` blocks.

If true, the perfect-sector classification and nonextension theorem finish Problem 617 immediately.

## Turan-scale evidence

For `n=r^2+1`, each color complement is `K_{r+1}`-free. The exact Turan lower bound on a color class is

`T_r = C(r+1,2)+(r-1)C(r,2) = r(r^2-r+2)/2`.

The total excess over these `r` minima is

`C(r^2+1,2)-r*T_r = r^2(r-1)/2`.

Hence the average excess per color is only `Theta(r^2)` while each color has `Theta(r^3)` edges. So on a relative scale most color classes are near their Turan extremum. This is evidence for partition stability, but standard fixed-`r` Turan stability cannot simply be quoted uniformly because here the forbidden clique size `r+1` grows with `n`.

## Research direction

Highest-value next lemma:

> obtain an explicit growing-`r` stability theorem for a graph on `r^2+O(1)` vertices with `alpha<=r` and only `O(r^2)` edges above the Turan minimum, strong enough to produce an actual or near clique partition.

Then combine two or more such partitions using edge-disjointness to force near orthogonality.
