# General-r Multicolor Turán-Stability Route

Status: **PROVED algebraic slack budget + literature-backed single-color stability; multicolor compatibility remains OPEN**.

## 1. Exact global slack budget

Let `n=r^2+1` and suppose an r-coloring is a counterexample to Problem 617. Let G_i be the graph of color i.

Every G_i has `alpha(G_i)<=r`, so

`e(G_i)>=p_r(n)`.

For `n=r^2+1`, the balanced r-clique partition has one class of size r+1 and r-1 classes of size r, hence

`p_r(r^2+1)=C(r+1,2)+(r-1)C(r,2)`

`=r(r^2-r+2)/2`.

Define the color slack

`s_i=e(G_i)-p_r(n)>=0`.

Since the color graphs partition all edges,

`sum_i e(G_i)=C(n,2)`.

Therefore

> **`sum_i s_i = r^2(r-1)/2`.**

The average slack is

> **`(1/r)sum_i s_i=C(r,2)`.**

Thus every hypothetical counterexample is globally close to the Turán-minimum regime in relative density, but it still has Theta(r^2) slack per color on average.

## 2. Complement Turán formulation

Let `J_i=bar(G_i)`. Since `alpha(G_i)<=r`, J_i is `K_(r+1)`-free.

Moreover

`e(J_i)=t_r(n)-s_i`,

where `t_r(n)` is the Turán number for K_(r+1).

Füredi's quantitative stability theorem implies that a `K_(r+1)`-free graph with Turán deficit t contains an r-partite subgraph with all but O(t) of the Turán edges; equivalently it is O(t)-edit-close to an r-partite/Turán structure. A standard sharpened formulation gives edit distance at most `3t` to a complete r-partite Turán graph.

Therefore every color graph G_i is O(s_i)-edit-close to a union of r near-balanced cliques.

Summed across all colors, the available edit budget is only O(r^3), compared with Theta(r^4) total vertex pairs.

## 3. Why ordinary stability is not yet enough

However the average `s_i` is Theta(r^2), so single-color stability permits Theta(r^2) edits in a typical color.

This is large enough to touch every one of the r blocks in that color many times. Therefore ordinary one-color Turán stability does not by itself recover the exact affine-plane/orthogonal-partition geometry.

A proof for all sufficiently large r needs a **multicolor compatibility gain**: the r near-Turán partitions are not independent because their edge sets must partition the same complete graph.

## 4. Desired multicolor theorem

A high-leverage stability statement would be:

> If r graphs `G_1,...,G_r` partition `E(K_(r^2+1))`, each satisfies `alpha(G_i),omega(G_i)<=r`, and the total Turán slack equals `r^2(r-1)/2`, then two (or many) color classes admit near-clique partitions whose blocks are almost orthogonal; the total exceptional incidences are small enough to be repaired/rotated to exact orthogonal partitions or to force an `(r+1)`-set missing a color.

Combined with `GENERAL_R_AFFINE_PLANE_NONEXTENSION.md`, an exact version of this theorem would directly settle Problem 617 for every r in the affine-plane range, and a robust version could yield all sufficiently large r.

## 5. Strategic conclusion

The asymptotic route is not blocked by lack of ordinary stability; it is blocked by compatibility of r simultaneous near-Turán decompositions.

This is a conceptually different route from the residual-core/repivot programme, but both seek the same phenomenon: local defect must either disperse into a forbidden anchor configuration or concentrate into a rigid design-like structure.
