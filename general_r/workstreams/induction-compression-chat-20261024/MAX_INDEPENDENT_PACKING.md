# Maximum-Independent-Set Packing Lemma

Status: **PROVED**.

Let `G_i` be one color graph of an `r`-counterexample on `N=r^2+1` vertices. Thus `alpha(G_i)<=r`.

## Lemma J.6 — Cross-edge lower bound

Let `S_1,...,S_t` be pairwise disjoint independent sets of size `r` in `G_i`, and put

`R = V \ (S_1 union ... union S_t)`.

Then

1. for every distinct `a,b`, the bipartite graph `G_i[S_a,S_b]` has minimum degree at least one on both sides, hence at least `r` edges;
2. every vertex of `R` has at least one neighbor in every `S_a`, hence at least `t` incident edges from `R` into the packed independent sets.

Consequently

`e(G_i) >= r*C(t,2) + t|R|`

and therefore

`e(G_i) >= r*C(t,2) + t(r^2+1-tr)`.

### Proof

Every independent `r`-set in a counterexample is dominating in its color graph. Apply this first to `S_a` and vertices of `S_b`, then symmetrically, proving the no-isolated-vertex statement between every pair. Apply domination of each `S_a` to every vertex of `R`. The counted edge classes are disjoint.

## Equality structure

If equality holds, then:

- every pair `S_a,S_b` is joined by exactly `r` edges and hence by a perfect matching;
- every `v in R` has exactly one neighbor in each `S_a`;
- there are no additional color-`i` edges inside `R` beyond those forced elsewhere by the global coloring.

Thus a large packing of disjoint maximum independent sets naturally creates matching/Latin-square-like incidence structure.

## The case `t=r`

Then `|R|=1` and the lower bound becomes

`e(G_i) >= r*C(r,2)+r = (r^3-r^2+2r)/2`.

This is exactly the ordinary Turan-complement minimum `p_r(r^2+1)` for independence number at most `r`.

If equality occurred, Turan equality would force `G_i` to be a union of `r` balanced cliques, one of size `r+1`, which contains a `K_(r+1)` and is impossible in a genuine multicolor counterexample. Hence in a genuine counterexample with such an `r`-packing,

`e(G_i) >= p_r(r^2+1)+1`.

More importantly, near equality forces every pair of packed independent sets to be close to a perfect matching, so a failed transversal/compression may itself generate a design-like coordinate system.

## Compression consequence

For the hypergraph `H_i` whose edges are the independent `r`-sets of color `i`, a maximal matching of size `t` supplies a transversal of `H_i` of size at most `rt` (take the union of the matching edges). Therefore:

> either one color's maximum-independent-set hypergraph has a small transversal, or it contains many disjoint maximum independent sets, in which case Lemma J.6 forces a dense matching geometry.

This is a concrete bridge from induction/compression failure to the finite-geometry/design terminal route.