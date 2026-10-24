# Exact Orthogonality from Two Turan-Equality Colors

Status: **PROVED for all `q>=2`; no prime-power assumption needed.**

## Setup

Let `W` be a set of `q^2` vertices in an edge-coloring, and let `G_i[W]`, `G_j[W]` be two color graphs satisfying

`alpha(G_i[W]) <= q`, `alpha(G_j[W]) <= q`.

The minimum number of edges in a `q^2`-vertex graph with independence number at most `q` is

`m_q := q*C(q,2) = q^2(q-1)/2`.

This is the complement form of Turan's theorem. Equality holds iff the graph is a disjoint union of `q` cliques `K_q`.

## Theorem K.1

If

`e(G_i[W]) = e(G_j[W]) = m_q`,

then the two clique decompositions are orthogonal: every `i`-clique meets every `j`-clique in exactly one vertex.

### Proof

Equality in Turan gives partitions

`W = A_1 disjoint union ... disjoint union A_q`,

`W = B_1 disjoint union ... disjoint union B_q`,

with every `A_a` and `B_b` of size `q`, and with all pairs inside `A_a` colored `i`, all pairs inside `B_b` colored `j`.

Because the edge-coloring assigns a unique color to each edge, no intersection `A_a intersect B_b` can contain two vertices: otherwise the edge between those two vertices would simultaneously have colors `i` and `j`.

Hence

`|A_a intersect B_b| <= 1`

for all `a,b`.

There are `q^2` ordered block pairs `(a,b)` and exactly `q^2` vertices. Every vertex lies in exactly one such intersection. Therefore all `q^2` intersections have size exactly one.

## Corollary K.2 — Local nonextension test

Let `chi` be a hypothetical counterexample to `P(q)` on `q^2+1` vertices. Fix any vertex `x` and put `W=V\{x}`.

Then **at most one** color graph on `W` can have exactly `m_q` edges.

### Proof

If two colors were exact, Theorem K.1 would give two orthogonal `q`-by-`q` clique partitions on `W`. The abstract two-partition nonextension theorem already proved in `GENERAL_R_AFFINE_PLANE_NONEXTENSION.md` says that no new vertex `x` can be attached while keeping every `(q+1)`-set incident with both colors. Contradiction.

## Equivalent slack form

For each color `i` and removed vertex `x`, define

`s_i(x) := e(G_i)-d_i(x)-m_q >= 0`.

Then in any counterexample to `P(q)`, for every vertex `x`,

`#{ i : s_i(x)=0 } <= 1`.

This is an exact multicolor anti-equality constraint. It is a natural starting point for a quantitative stability theorem in which `s_i(x)` is small but nonzero.