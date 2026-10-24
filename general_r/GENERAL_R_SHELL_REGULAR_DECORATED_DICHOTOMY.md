# General-r Near-Extremal Shell Regular/Decorated Dichotomy

Status: **PROVED_SYMBOLIC**, conditional on the general residual-core / near-anchor theorem and the multicolor fixed-deficit clique bound.

## 1. Setup

Let a legal pivot p have shell A of size `r+1`. Assume the residual edge deficit is

`epsilon=D_r(4r+1)-e(F)`

and the general near-anchor theorem has supplied

`q<=3r-1-epsilon`.

A shell vertex is regular if its target degree is exactly `r+1`. For a regular shell vertex y put

`d_y=d_M(y)`.

The symbolic repivot base gives

`d_y(r+1-d_y)<=q`.

For every `r>=12`,

`4(r-3)>3r-1>=q`.

Hence no regular missing degree lies in

`4<=d_y<=r-3`.

Thus every regular shell vertex belongs to one of

- low endpoint: `d_y<=3`;
- high endpoint: `d_y>=r-2`.

## 2. Low-endpoint regular vertices form a target clique

Let x,y be two low-endpoint regular shell vertices. Suppose they are target-nonadjacent.

The symbolic zero-gap theorem gives

`S_x union S_y=A`.

But

`|S_x union S_y|<=d_x+d_y<=6`,

whereas `|A|=r+1>=13` for r>=12. Contradiction.

Therefore all low-endpoint regular vertices are pairwise target-adjacent.

They also all have target degree exactly `r+1`. Hence they form a regular target clique.

By `GENERAL_R_MULTICOLOR_STABILITY_D3_WINDOW.md`,

> **`|R_low| <= [r-1+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

For epsilon<=2 one may replace this by the sharper exact Brouwer-partite bound.

## 3. High-endpoint regular vertices are O(1)

Every high-endpoint regular shell vertex has

`d_M(y)>=r-2`.

Since

`sum_(v in A)d_M(v)=2e(M)`

and

`e(M)<=q`,

we have

`|R_high|(r-2) <=2q <=2(3r-1-epsilon)`.

Thus

> **`|R_high| <= floor(2(3r-1-epsilon)/(r-2))`.**

In particular:

- for r=12, `|R_high|<=7`;
- for every r>=13, `|R_high|<=6`.

So the large missing-degree endpoint can never carry a scalable fraction of the shell.

## 4. Linear decoration lower bound

Let tau be the number of decorated shell vertices, i.e. vertices with target degree greater than `r+1`.

Every shell point is either decorated or regular. Therefore for r>=13,

`tau >= r+1-|R_low|-|R_high|`.

Using the preceding bounds,

> **`tau >= [r-9-2epsilon-epsilon sqrt(4epsilon+1)]/2`.**

For every fixed epsilon,

> **`tau >= r/2-O_epsilon(1)`.**

Thus a fixed-deficit near-extremal maximal shell is necessarily decoration-heavy unless it has already fallen into one of the excluded regular configurations.

## 5. Repivot-potential consequence

The exact symbolic transport identity is

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`,

where X is the global set of decorated vertices.

The present theorem therefore reframes the remaining global termination problem:

> in a near-extremal shell with a linear number of decorated shell vertices, prove that either some legal regular repivot moves more decorated vertices into the shell than it removes (strict tau improvement), or the decoration incidences satisfy a rigid design-like equality system.

This is a substantially narrower target than arbitrary higher-slack support classification.
