# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. The front extraction and anchor-excess theorem are upstream.

## Conditional hypotheses

- **A (residual-core contract).** Every legal backend view used here has a core `H` with
  `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and every legal regular repivot again has core minimum degree at least `r`.
- **B (anchor excess).** Every legal core satisfies `K_r>=8`.

Consequently the strengthened charge ceiling is

`q<=3r-1`.

For every `r>=12`, the quadratic repivot base excludes every regular missing degree

`4<=d<=r-3`.

Thus only the endpoint degrees

`d in {0,1,2,3,r-2,r-1,r}`

remain.

## Exact identities in force

`e(F)=C(r+2,2)+q+e(H)`.

`K_r=2(E-q-(2r^2+r+1))`.

For a regular repivot `p -> y`,

`q_y=d(r+1-d)+B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

For `z in H\D_y`,

`kappa'_z=w_z-e_H(z,D_y)`.

For `s in S_y`,

`kappa'_s=sigma_s-e_F(s,D_y)`.

The bounded two-coordinate potential is

`Psi_2=(q,tau)`, `tau=|A intersect {v:d_F(v)>r+1}|`.

## Results proved in this workstream

### R1. Plateau transport / cycle identity

For every regular repivot in a fixed residual graph,

`K_y-K_p=-2(q_y-q_p)=2(q_p-q_y)`.

Hence `K` is not an independent potential coordinate. On every closed repivot cycle the signed q-loss sums to zero. If every step is q-non-improving, every step is q-flat. If every step is also `(q,tau)`-non-improving, every step is both q-flat and tau-flat.

### R2. d3 common-S closure

Using the existing equality B-floor, every d3 common-S family satisfies

`q<=3r-2`, hence `a+B<=4` and `a<=4` for every `r>=12`.

Together with the existing low-charge absorption (`b=2` and `b=1,a<=4`), the d3 common-S endpoint has no surviving terminal under A+B.

### R3. High-endpoint absolute owner bound

Let `Y_hi` be all regular shell vertices with `d_y>=r-2`. Then for every `r>=12`,

`|Y_hi|<=7`.

This is stronger than the previous per-common-S multiplicity bound `<=3`: it bounds the total number of high-endpoint regular owners, even across different missing sets.

### R4. High-endpoint fixed-width incidence kernel

For `Y=Y_hi`, the target graph `G=F[Y]` has `Delta(G)<=2`, `alpha(G)<=3`, and `|Y|<=7`.

Each high owner has a shell target-neighbour complement `T_y` of size at most 2. Hence all high-owner shell incidences are supported on a kernel of at most `|Y|+sum|T_y|<=21` shell vertices.

For each core vertex `v`, define its owner-incidence signature

`I(v)={y in Y : v in D_y}`.

The zero-gap theorem implies `I(v)` is a clique of `G`. A graph with `Delta<=2` and at most 7 vertices has at most 16 nonempty cliques (at most 7 vertices, 7 edges and 2 triangles), so the core owner-incidence data uses at most 17 signature classes including the empty signature.

Thus the high endpoint is an r-independent finite-width interaction skeleton.

## Current theorem level

- Low endpoint: d3 common-S branch closed; d2 global equality/positive-loss branch still open; d0/d1 not yet frozen.
- High endpoint: reduced to a fixed-width kernel with at most 7 owners, 21 shell interaction vertices and 17 core incidence-signature classes. Full contradiction of every high kernel remains open.
- Global potential: `(q,tau)` is exact and bounded. `K` is redundant with q. A third plateau coordinate is still required.

## Unique next blocker

**d2 Plateau Equality/Positive-Loss Stability:** prove that every d2 state which is non-improving in `(q,tau)` either contradicts support compatibility/transport or collapses to a bounded rigid skeleton. This is now the only scalable low-endpoint obstruction.