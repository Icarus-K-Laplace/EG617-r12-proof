# Nonextension Theorems

## Theorem F4.1 — arbitrary-leftover affine-skeleton nonextension

Let `r>=3`. Let an affine plane of order `r` have parallel classes

`P_1,...,P_r,Q`.

Color `K_{r^2}` so that for every `i in [r]`, every edge inside a `P_i` line has color `i`. Every edge on the remaining class `Q` may be assigned an arbitrary color.

Then this coloring cannot be extended by one new vertex `x` to a balanced `r`-coloring of `K_{r^2+1}`.

### Proof

For each color `i`, put

`A_i={v: color(xv)=i}`.

The `A_i` partition the `r^2` old vertices, so

`sum_i |A_i|=r^2`.

Fix color `i`. Identify the points with an `r x r` grid using `P_i` as rows and `Q` as columns.

Every permutation transversal `T` (one point from each row and each column) is color-`i` independent among old vertices: two points of `T` share neither a `P_i` line nor a `Q` line, hence their unique affine line belongs to some `P_j`, `j!=i`, and their edge has color `j`.

If some permutation transversal avoided `A_i`, then all its `r` vertices have `x`-edges of colors different from `i`, and it has no internal color-`i` edge. Together with `x` it would give an `(r+1)`-set missing color `i`. Therefore `A_i` meets every permutation transversal.

By the matching-preclusion lemma for `K_{r,r}`,

`|A_i|>=r`.

Summing over all `r` colors and using `sum_i|A_i|=r^2`, equality holds for every color:

`|A_i|=r`.

Moreover each `A_i` is either

1. one full row, i.e. a line of `P_i`, or
2. one full column, i.e. a line of `Q`.

Call these the row and column cases.

#### Row cases

If colors `i!=j` both use row cases, then `A_i` is a `P_i` line and `A_j` a `P_j` line. Distinct parallel classes meet in exactly one point, contradicting that the incident-color sets `A_i,A_j` are disjoint. Hence at most one color uses a row case.

#### Column cases

Suppose color `i` uses a column case, so `A_i=Q_0` for some `Q`-line `Q_0`.

Take any other `Q`-line `L!=Q_0`. If `L` contains an edge `uv` whose color is not `i`, then `u,v` occupy two distinct `P_i` rows. There are `r-2` remaining rows and exactly `r-2` `Q`-lines distinct from both `Q_0` and `L`. Choose one point from each remaining row, bijectively across those remaining columns. The resulting `r` points lie outside `A_i`; the only pair sharing a `Q`-line is `uv`, which is not color `i`, and every other pair lies on some base class `P_j`, `j!=i`. Thus these `r` points are color-`i` independent, contradicting balance with `x`.

Therefore if `A_i` is a `Q`-line, **every edge on every other `Q`-line must have color `i`**.

If two distinct colors `i,j` both use column cases, choose a `Q`-line different from both blocker lines; this exists because `r>=3`. Every edge on that line would have to have both colors `i` and `j`, impossible. Hence at most one color uses a column case.

We have shown that at most one color can be a row case and at most one can be a column case. For `r>=3` this cannot account for all `r` incident color classes `A_i`. Contradiction.

QED.

## Corollary F4.2 — the original standard affine construction is nonextendable

Immediate, as it is a special case of Theorem F4.1.

This strictly strengthens the mother-branch theorem that used two pure parallel-class colors.

## Corollary F4.3 — perfect-sector nonextension (with classical net completion)

Assume a balanced coloring of `K_{r^2}` has, for every color `i`, a spanning partition into at most `r` color-`i` cliques.

Pairwise edge-disjointness forces these partitions to be `r` mutually orthogonal partitions into `r` blocks of size `r`. They form an `r`-net. By the classical deficiency-one completion theorem, add the unique missing parallel class `Q`; the coloring is an arbitrary-leftover affine-skeleton coloring. Hence Theorem F4.1 forbids any balanced one-vertex extension for `r>=3`.

Status of the reduction to an `r`-net: elementary/proved.
Status of the unique net completion: classical external theorem; literature audit required before promotion into a master proof.

## Significance

The new theorem removes a major false bottleneck: the leftover parallel class need **not** be monochromatic, and no pair of pure colors is needed. The remaining Problem 617 task is reconstruction/stability, not nonextension of the canonical design family.
