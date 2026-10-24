# General-r Near-Anchor Common Antineighbourhood Compression

Status: **PROVED_RELATIVE_TO_CLASSICAL_TRIANGLE-FREE EXTREMAL THEOREMS**.

This theorem is downstream of the `5r+1` direct near-anchor extraction theorem.

## 1. Setup

Let F be a contextual target-color terminal on `5r+1` vertices with

- `alpha(F)<=5`;
- `omega(F)<=r-1`;
- the original balanced r-color completion on the same vertex set.

Let `T={x,y,z}` be an independent target triple.

Define the common target anti-neighbourhood

`W={v outside T : vx,vy,vz are all target nonedges}`

and put `m=|W|`.

Because T is independent and `alpha(F)<=5`,

> **`alpha(F[W])<=2`.**

For every non-target color C_j, the balanced-coloring condition still gives

> **`alpha(C_j[W])<=r`.**

## 2. Pair-count inequality

The target color on W has at least

`p_2(m)`

edges.

Each of the other `r-1` colors has at least

`p_r(m)`

edges.

Since the r colors partition all pairs of W,

> **`p_2(m)+(r-1)p_r(m) <= C(m,2)`.**

Define the slack

`g_r(m)=C(m,2)-p_2(m)-(r-1)p_r(m)`.

At

`m=2r+2`,

a direct calculation gives

> **`g_r(2r+2)=5-r`.**

Hence `g_r(2r+2)<0` for every `r>=6`.

Moreover

`g_r(m+1)-g_r(m)`

`=m-floor(m/2)-(r-1)floor(m/r)`

`=ceil(m/2)-(r-1)floor(m/r)`.

For `2r+2<=m<=5r-2` and `r>=6`, this increment is strictly negative in each of the ranges `floor(m/r)=2,3,4`.

Therefore:

> **For every r>=6, `m<=2r+1`.**

## 3. Lower bounds from anchor degrees

If the extracted triple has degree pattern

`(r,<=r+1,<=r+1)`,

then its neighbourhood union has size at most `3r+2`, so

> **`m>=2r-4`.**

If the triple has degree pattern

`(r+1,<=r+2,<=r+2)`,

then its neighbourhood union has size at most `3r+5`, so

> **`m>=2r-7`.**

Thus pair counting alone already leaves only a constant-width size window.

## 4. Eliminate m=2r+1

Let

`J=bar(F[W])`.

Since `alpha(F[W])<=2`, J is triangle-free.

Also

`alpha(J)=omega(F[W])<=r-1`.

On `2r+1` vertices, J cannot be bipartite, since every bipartite graph has an independent side of size at least `r+1`.

The classical Erdős/Gallai/Andrásfai extremal theorem for non-bipartite triangle-free graphs gives

`e(J)<=floor((m-1)^2/4)+1=r^2+1`.

Hence

`e_F(W)>=C(2r+1,2)-(r^2+1)=r^2+r-1`.

But

`p_2(2r+1)=r^2`.

Therefore the target color alone uses at least

`r-1`

units above its pair-count minimum.

On the other hand

`g_r(2r+1)=2`.

For every `r>=4`, `r-1>2`, contradiction.

Thus:

> **`m!=2r+1` for r>=4.**

## 5. Eliminate m=2r

Again J is triangle-free with `alpha(J)<=r-1`, hence non-bipartite.

The same extremal theorem gives

`e(J)<=floor((2r-1)^2/4)+1=r^2-r+1`.

Therefore

`e_F(W)>=C(2r,2)-(r^2-r+1)=r^2-1`.

Since

`p_2(2r)=r^2-r`,

the target color uses at least

`r-1`

slack units.

But

`g_r(2r)=r`.

Hence all `r-1` non-target colors together use at most one excess unit above their individual minima.

For `m=2r`,

`p_r(2r)=r`.

A graph on `2r` vertices with exactly r edges and independence number at most r must be a perfect matching. Therefore at least `r-2` non-target colors induce perfect matchings on W.

Their edges are pairwise disjoint because colors partition pairs. Hence every vertex of J has degree at least

`r-2`.

For `r>=11`,

`r-2 > (2/5)(2r)`.

The triangle-free Andrásfai-Erdős-Sós theorem then forces J to be bipartite. But a bipartite graph on `2r` vertices has an independent side of size at least r, contradicting `alpha(J)<=r-1`.

Therefore:

> **`m!=2r` for every r>=11.**

## 6. Final common-antineighbourhood windows

For the low terminal layer triple `(r,<=r+1,<=r+1)`, every `r>=11` survivor satisfies

> **`2r-4 <= m <=2r-1`.**

For the high terminal layer triple `(r+1,<=r+2,<=r+2)`, every `r>=11` survivor satisfies

> **`2r-7 <= m <=2r-1`.**

Thus after direct anchor extraction, the common anti-neighbourhood has only finitely many possible offsets from `2r`, independent of r.

This converts the remaining near-anchor incompatibility problem into a bounded-offset classification problem rather than a growing asymptotic family.