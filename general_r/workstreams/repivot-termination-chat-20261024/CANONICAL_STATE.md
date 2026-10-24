# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. The front extraction and anchor-excess theorem are upstream.

## Conditional hypotheses

- **A (residual-core contract).** Every legal backend view used here has a core `H` with
  `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and every legal regular repivot again has core minimum degree at least `r`.
- **B (anchor excess).** Every legal core satisfies `K_r>=8`.

Consequently

`q<=3r-1`.

For every `r>=12`, the quadratic repivot base excludes

`4<=d<=r-3`.

Thus only

`d in {0,1,2,3,r-2,r-1,r}`

remain.

## Exact identities in force

`e(F)=C(r+2,2)+q+e(H)`.

`K_r=2(E-q-(2r^2+r+1))`.

For a regular repivot `p -> y`,

`q_y=d(r+1-d)+B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

Transport:

`kappa'_z=w_z-e_H(z,D_y)` for `z in H\D_y`,

`kappa'_s=sigma_s-e_F(s,D_y)` for `s in S_y`.

Potential:

`Psi_2=(q,tau)`, `tau=|A intersect {v:d_F(v)>r+1}|`.

## Results proved in this workstream

### R1. Plateau transport / cycle identity — PROVED_SYMBOLIC

`K_y-K_p=-2(q_y-q_p)=2(q_p-q_y)`.

Therefore K is affine-redundant with q. Every closed q-non-improving repivot cycle is q-flat; every closed `(q,tau)`-non-improving cycle is simultaneously q-flat and tau-flat. Repeated non-fully-decorated supports cannot occur on such a plateau cycle.

### R2. d3 closure — PROVED_CONDITIONAL

The equality B-floor eliminates the allowance-five frontier. Every d3 local/common-S representation satisfies

`q<=3r-2`, hence `a+B<=4`.

Together with the pre-existing low-charge absorption (`b=2` and `b=1,a<=4`), no d3 terminal survives under A+B.

### R3. High Endpoint Three-Owner Theorem — PROVED_CONDITIONAL

Let `Y_hi` be **all** regular shell vertices with `d_y>=r-2`. Then

> `|Y_hi|<=3`

for every `r>=12`.

Proof mechanism: any four high owners have at least one target edge by zero-gap/core packing, so their incident shell missing edges number at least `4r-13`. For `r>=13` this exceeds `q<=3r-1`. At the sole equality boundary `r=12`, four owners force `q=35`, hereditary equality and a 10-vertex regular target clique, contradicting the multicolor equality regular-clique obstruction.

This is a global bound across different missing sets, not a per-common-S bound.

### R4. High Endpoint Bounded-Complement Reduction — PROVED_CONDITIONAL

For high owners put `s_y=r-d_y in {0,1,2}`. Since there are at most three owners:

- all high-owner shell target-neighbour sets live in a kernel of at most 9 vertices;
- core membership in the support sets `D_y` has at most `2^3=8` incidence-signature classes;
- the owner graph has at most three vertices.

Hence the high endpoint is an r-independent finite skeleton. This reaches the intended **Level 3 high-endpoint reduction**.

### R5. Exact d2 charge identity — PROVED_SYMBOLIC

For every d2 common-S system, with `b=e_M(S) in {0,1}`, allowance a, and total common-S core charge W,

> `W=K+2r-2+a+b`.

If a one-loss common-hub system has three distinct support classes, the existing charge barrier `W>=3r-2` implies

> `K+a+b>=r`.

Thus three-class d2 terminals can exist only in a linearly high excess/allowance regime. The known state `(K,a,b)=(8,3,1)` therefore forces `r<=12` immediately.

### R6. d0 neutral symmetry — PROVED_SYMBOLIC

If a regular owner has d=0, then `S=D=empty`, the core is unchanged, and the repivot preserves both q and tau exactly. Such moves are pure pivot relabellings and can be quotiented out of any termination graph.

## Current theorem level

- d0: quotient-neutral, frozen.
- d3: closed under the stated upstream low-charge assets.
- high endpoint: finite bounded-complement skeleton, at most three total owners.
- d2: exact scalar charge reduction obtained, but the linearly high `K+a+b>=r` terminal regime remains.
- d1: exact one-vertex exchange still needs a closure/rigidity theorem.
- global potential: `(q,tau)` exact; K redundant; an equal-plateau refinement is still required.

## Unique next blocker

**d2 linearly-high plateau stability:** eliminate or rigidify d2 non-improving states with `K+a+b>=r`. This is now the only endpoint family whose structural size can still scale with r.