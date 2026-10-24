# General-r Program

Status: ACTIVE SYMBOLIC RESEARCH PROGRAM. No r=12 theorem is promoted without a separate derivation.

## Target architecture

`K_(r^2+1)`
` -> least-colour hereditary cap / front extraction`
` -> F_r on 4r+1 or controlled 5r+1 terminal`
` -> H_r on 3r-1`
` -> symbolic repivot/defect transport`
` -> anchor-or-sunflower dichotomy`
` -> global contradiction`.

## What is now genuinely symbolic

### Original/front algebra

- ambient order `r^2+1`;
- least-color budget `r(r^2+1)/2`;
- hereditary cap `D_r(n)=C(n,2)-(r-1)p_r(n)`;
- target-K_r block cross-matchings;
- residual order `r^2-d-jr` after an anchor and j K_r blocks;
- at `d=r-1`, `j=r-5` gives `4r+1`, while `j=r-6` gives `5r+1`.

The OPEN part is not these formulas; it is the all-r recurrence/forcing which reaches the same stops.

### Backend algebra

Conditional on a legal 4r+1 residual and degree-(r+1) pivot:

- shell size `r+1`;
- core size `3r-1`;
- exact backend identity

  `e(F)=C(r+2,2)+q+e(H)`;

- excess identity

  `K_r=2(E-q-(2r^2+r+1))`;

- symbolic repivot

  `q_y=d(r+1-d)+nonnegative corrections`;

- symbolic row closure and nonadjacent zero-gap relation.

### Core floor

For every r>=12, conditional on

`|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`,

AES excludes `K_r=0`. Hence

`K_r>=2`,

`e(H)>=[r(3r-1)+2]/2`.

CORE211 is the r=12 evaluation of this theorem.

### Anchor reduction

The exact three-anchor partition is symbolic: connector count is always 2,3,4 and the exclusive block sizes are fixed shifts of r-2.

Every independent triple of total degree excess<=3 reduces, for r>=12, to the **exact degree-r three-anchor problem**. The only unresolved anchor statement is therefore:

> exact independent degree-r triple => `K_r>=8`?

This is proved for r=12 but OPEN symbolically.

### Support compatibility

The following are all symbolic once the general residual-core/common-S setup exists:

- allowance localization `a=e_M(S)+sum sigma_s`;
- anchor transport `d_(H_y)(s)-r=sigma_s-|D_s intersect D_y|`;
- row closure `e_H(v,D)<=kappa_v+e_F(v,S)`;
- zero-charge incidence-signature capacity;
- three signatures -> exact degree-r anchors;
- at most two signatures -> at most three zero-skeleton sunflower patterns;
- d2 common-hub and d3 Type-H/Type-P classification.

### Owner capacities

In the first hereditary-cap range:

- d2 common-hub:

  `N<=r-3+(k^2-3k+6)/(2(r-k))`;

- d3 Type H:

  `N<=r-4+(2k^2-6k+7)/(r+1-2k)`;

- d3 Type P:

  `N<=r-4+(k^2-3k+10)/(2(r-k))`.

For fixed k<=3 and sufficiently large r these integerize to `r-3` and `r-4`.

Therefore owner packing alone has slope one and does not yield an asymptotic slope contradiction.

## Alternative stability route

The standard affine-plane construction on r^2 vertices cannot be extended by one vertex for any r>=3. The proof only needs two orthogonal clique partitions.

Every hypothetical counterexample has exact total Turán slack

`sum_i s_i=r^2(r-1)/2`.

Single-color Turán stability makes each color graph O(s_i)-close to a union of r cliques, but average slack is Theta(r^2), so ordinary stability is too weak. The missing statement is a multicolor compatibility/stability theorem forcing two near-partitions to become robustly orthogonal.

## Current bottlenecks in dependency order

1. **Front extraction / residual-core source:** prove general forcing to a 4r+1 residual with degree r+1 and prove `delta(H_r)>=r`.
2. **Exact three-anchor excess:** prove `K_r>=8` (or stronger `f(r)`) for three independent degree-r anchors.
3. **Global repivot termination:** symbolic `(q,tau)` is a bounded lexicographic potential locally, but no theorem yet says every non-rigid configuration improves it.
4. **Final forcing/capacity comparison:** owner capacities have slope one, so a stronger gain is required.

## Unique highest-leverage bridge lemma

### General Residual Defect-Transport Stability Lemma

For every r>=r0, let H_r be a legal `(3r-1)`-point residual core produced from a maximal degree-(r+1) pivot. Then every nonterminal local view satisfies at least one of:

1. it produces an independent degree-r anchor triple;
2. its zero/low-charge incidence system collapses into one of at most three sunflower patterns whose owner demand exceeds the symbolic hereditary capacity;
3. there is a legal repivot strictly increasing the bounded lexicographic potential `(q,tau,...)`.

The only terminal equality configurations are design-like near-Turán structures, and those cannot accept the extra `r^2+1`st vertex.

This one statement would connect the r=12 pivot/support/anchor machinery to both the backend and the affine-plane stability picture. It is the current best candidate for the main structural theorem behind Problem 617.
