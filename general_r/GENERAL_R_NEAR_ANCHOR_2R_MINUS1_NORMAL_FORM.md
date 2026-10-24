# General-r Near-Anchor `|W|=2r-1` Normal Form

Status: **PROVED_RELATIVE_TO_THE_SHARP_NON-BIPARTITE TRIANGLE-FREE EXTREMAL THEOREM AND ITS EQUALITY CLASSIFICATION**.

This file continues `GENERAL_R_NEAR_ANCHOR_COMMON_ANTINEIGHBORHOOD.md`.

## 1. Setup

Let F be a contextual `5r+1` target terminal and let T be an independent near-anchor triple. Let W be the common target anti-neighbourhood of T and suppose

`|W|=m=2r-1`.

Then

- `alpha(F[W])<=2`;
- for every non-target color C_j, `alpha(C_j[W])<=r`;
- `omega(F[W])<=r-1`.

Put

`J=bar(F[W])`.

Then J is triangle-free and

`alpha(J)<=r-1`.

In particular J cannot be bipartite: a bipartite graph on `2r-1` vertices has an independent side of size at least r.

## 2. Exact total slack

For `m=2r-1`,

`p_2(m)=(r-1)^2`

and

`p_r(m)=r-1`.

Hence

`g_r(m)=C(m,2)-p_2(m)-(r-1)p_r(m)=r-1`.

Define color excesses

`delta_0=e_F(W)-p_2(m)`

for the target color, and

`delta_j=e_(C_j)(W)-p_r(m)`

for the `r-1` non-target colors.

Because the colors partition all pairs of W,

> **`delta_0+sum_j delta_j=r-1`.**

## 3. Sharp lower bound on the target excess

The classical sharp theorem for non-bipartite triangle-free graphs gives

`e(J)<=floor((m-1)^2/4)+1=(r-1)^2+1`.

Therefore

`e_F(W)=C(2r-1,2)-e(J)`

`>=2r^2-3r+1-(r^2-2r+2)`

`=r^2-r-1`.

Since

`p_2(2r-1)=r^2-2r+1`,

we obtain

> **`delta_0>=r-2`.**

Together with the exact total slack `r-1`, only two integer cells remain.

## 4. Exact two-cell classification

### Cell A

`delta_0=r-1`,

`sum_j delta_j=0`.

Thus

- `e_F(W)=r^2-r`;
- `e(J)=(r-1)^2`;
- every one of the `r-1` non-target colors has exactly `r-1` edges on W.

A graph on `2r-1` vertices with `r-1` edges and independence number at most r must be a matching of size `r-1` plus one isolated vertex.

Hence in Cell A:

> **all `r-1` non-target colors are exact near-perfect matchings on W.**

### Cell B

`delta_0=r-2`,

`sum_j delta_j=1`.

Thus

- `e_F(W)=r^2-r-1`;
- `e(J)=(r-1)^2+1`;
- exactly one non-target color has one edge above its minimum and all remaining `r-2` colors are exact near-perfect matchings.

Moreover J attains equality in the sharp non-bipartite triangle-free extremal theorem.

By the equality classification:

> **`J = S(K_(r-1,r-1))`,**
>
> the graph obtained from `K_(r-1,r-1)` by subdividing one edge once.

This is the canonical top-layer design cell.

## 5. Canonical colored witness for Cell B

Cell B is not merely numerically feasible; it has a natural exact color decomposition.

Let the bipartition of `K_(r-1,r-1)` be A,B and choose a 1-factorization

`M_1,...,M_(r-1)`.

Choose an edge `uv in M_1` and subdivide it with a new vertex w:

`u-w-v`.

Color:

- for `i>=2`, all edges of `M_i` with non-target color i;
- in color1, use `M_1\{uv}` together with the two subdivision edges `uw,wv`.

Then:

- colors `2,...,r-1` are near-perfect matchings of size `r-1` on `2r-1` vertices;
- color1 has r edges and is a matching plus one P3 component;
- the union of all non-target colors is exactly `S(K_(r-1,r-1))`;
- every non-target color has independence number exactly r;
- the target graph is the complement and has `alpha<=2` and clique number `r-1`.

Therefore Cell B is a genuine local design extremizer.

## 6. Consequence for the global program

The top surviving common-antineighbourhood layer is no longer an amorphous near-anchor configuration.

At `|W|=2r-1`, every survivor lies in one of exactly two cells, and the sharp Cell B obstruction is the explicit

> **1-factorized subdivided complete bipartite design.**

Thus any proof that eliminates Cell B must use extension compatibility with the three anchors and the outside vertices; W-internal edge counting alone cannot eliminate it.

This identifies a concrete downstream nonextension theorem:

> **Subdivided-factorization Nonextension Theorem.** Show that the canonical Cell B coloring on W cannot be extended to the full contextual `5r+1` terminal while preserving the target near-anchor degree pattern and the balanced-coloring constraints.

Cell A remains one edge below the sharp non-bipartite triangle-free extremal layer and should be treated as the adjacent stability cell.