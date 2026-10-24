# General-r Current Assessment

## 1. Which r=12 constants are now parameterized?

Successfully parameterized:

- `145 = r^2+1`;
- least-color edge budget `870 -> r(r^2+1)/2`;
- hereditary cap `D_r(n)=C(n,2)-(r-1)p_r(n)`;
- `49 -> 4r+1` and `61 -> 5r+1` inside the anchor/block-packing algebra;
- `13 -> r+1` as the symbolic backend shell degree;
- `35 -> 3r-1` conditional on the 4r+1 residual and degree-(r+1) pivot;
- `91 -> C(r+2,2)`;
- `301 -> 2r^2+r+1`;
- `211 -> [r(3r-1)+2]/2` for r>=12 under the general residual-core contract;
- `38 -> q_*(r)=3r+2` at the maximum 4r+1 residual layer;
- owner caps 9/8 -> symbolic `r-3+o(1)` / `r-4+o(1)` formulas;
- support overlap threshold `d-1`, first-high-slack `a=d`, and allowance transport are symbolic;
- Bridge A core cap `221 -> D_r(3r-1)=(3r^2+r-2)/2`, giving exact core-excess ceiling `K_r<=2r-2`.

Still not parameterized as proved all-r facts:

- the r=12 lower-order edge floor284 and related recurrence seeds;
- the exact near-anchor value `K>=8` beyond r=12;
- fixed q27/q30/q31 provenance beyond their symbolic quadratic/layer interpretation.

## 2. Is the general residual-core source proved?

Not fully.

Conditional algebra proves:

- if F has order4r+1 and pivot degree r+1, then `|H|=3r-1`;
- `omega(H)<=r-1` is inherited from F;
- `alpha(H)<=3` follows from `alpha(F)<=4` and the pivot.

The load-bearing missing statement is

> **`delta(H)>=r` for all relevant general-r pivot cores.**

At r=12 this comes from lower-order Ramsey/cap seeds. There is currently no all-r source theorem.

## 3. Exact symbolic backend identity

Under the general backend setup:

> `e(F)=C(r+2,2)+q+e(H)`.

With

`K_r=2e(H)-r(3r-1)`, one has

> `K_r=2(E-q-(2r^2+r+1))`.

For a regular repivot of missing degree d:

> `q_y=d(r+1-d)+B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

## 4. Direct near-anchor forcing is now all-r under the residual-core contract

Bridge A parameterizes exactly.

For `|H|=3r-1`, the inherited hereditary cap gives

`p_r(3r-1)=3r-2`,

`D_r(3r-1)=(3r^2+r-2)/2`,

and therefore

> **`K_r(H)<=2r-2`.**

A general graph lemma with

`n=3r-1`, `delta=r`, `omega=r-1`, `t=r-1`

then forces an independent triple with degree pattern

> **`(r, <=r+1, <=r+1)`.**

Thus every genuine core directly enters the near-anchor alternative. Common-S/signature extraction is no longer needed to *produce* anchors once the residual-core contract is available.

The remaining anchor theorem is now precisely:

> independent triple of total excess <=3 => `K_r>=8`?

Equivalently, after the already-proved reductions, the exact degree-r three-anchor theorem remains the only general anchor gap.

## 5. Which support-compatibility parts are all-r?

Conditional on the residual/common-S contract, the following are fully symbolic:

- row closure;
- allowance localization;
- anchor transport;
- zero-charge incidence signatures;
- signature diversity -> independent exact anchors;
- <=2 signatures -> <=3 zero-skeleton patterns;
- exact sunflower decomposition;
- d2 common-hub and d3 Type-H/Type-P geometry;
- loss-layer overlap threshold and repeated-support strict loss;
- exact Bridge B transport identity `kappa'_z=w_z-e_H(z,D_y)`;
- general missing-pair common-nonneighbour count.

The common-S machinery should now be viewed as an equality/positive-loss incompatibility engine, not the primary anchor-extraction engine.

## 6. General owner capacity

In the first hereditary-cap range:

### d2 common hub

`N<=r-3+(k^2-3k+6)/(2(r-k))`.

### d3 Type H

`N<=r-4+(2k^2-6k+7)/(r+1-2k)`.

### d3 Type P

`N<=r-4+(k^2-3k+10)/(2(r-k))`.

For fixed k<=3 and sufficiently large r these integerize to `r-3` and `r-4`.

Thus owner capacity is linear with slope1; owner packing alone does not provide a slope contradiction.

## 7. Bridge B general consequences

The exact transported-excess identity is symbolic:

`kappa'_z=w_z-e_H(z,D_y)`.

For a nonadjacent pair of total new excess rho in a `(3r-1)`-core, the number of common non-neighbours is

> **`r-3-rho+codeg(u,v)`.**

Thus the low-charge pair mechanism gets easier as r grows, conditional on the general near-anchor theorem.

A major small-r collapse also occurs. The first d2 positive-loss concentrated state with

`K_r=8, a=3, ell=1`, no outside zero, and at least two distinct supports

has charge sum

`W=2r+10`.

All zeros lie in the intersection of the distinct 2-supports, so at most one zero exists and hence `W>=3r-2`. Therefore

> **`r<=12`.**

So this entire concentration state is impossible for every `r>=13`; the r=12 `0,1^34` profile is an exact small-r boundary artifact.

If the general near-anchor theorem gives `K_r>=8`, then `q<=3r-1`. For d=3 this implies `a<=5` for every r>=12. Hence all d3 complexity is uniformly bounded: b=2 is fully in the low-charge window, b=1 is absorbed through a<=4, and only the symbolic boundary `b=1,a=5` survives the pair-excess<=3 test.

## 8. Is there a monotone symbolic repivot potential?

Partially.

`(q,tau)` is a genuine bounded symbolic lexicographic potential, and repeated non-fully-decorated plateau supports strictly improve tau at equal q.

What is OPEN is a global theorem that every non-rigid local view improves `(q,tau)` or a finite refinement of it. Higher-slack equality can currently preserve both coordinates.

Bridge B confirms that numerical envelope absorption alone is insufficient: positive-loss owner cores have `K_y=K+2ell_y`, so equality/incompatibility must cover more than the `K_y=8` plateau.

## 9. Do we have a sufficiently-large-r contradiction?

Not yet.

But the asymptotic reduction is now stronger than before.

Baseline:

- `q<=3r+2` from the universal core floor;
- for r>=15, missing degrees `4,...,r-3` are impossible.

Conditional on the general near-anchor theorem, direct Bridge A forcing applies to every core and yields

> **`K_r>=8` and `q<=3r-1`.**

Then for every r>=12, not merely r>=15,

> **`4<=d<=r-3` is impossible.**

The only scalable support sizes are d<=3; high endpoint sizes d>=r-2 have at most three common-S owners.

Moreover the first d2 positive-loss concentration is absent for all r>=13, and d3 has only one fixed `b=1,a=5` equality boundary beyond the low-charge bridge.

Thus the large-r backend has become a bounded-width endpoint problem rather than a growing case tree.

Ordinary one-color Turán stability remains insufficient by itself because average color slack is Theta(r^2); a multicolor compatibility gain is still needed for the front/design route.

## 10. Largest general front-end gap

The r=12 recurrence already has a symbolic form in local variables, but its order cutoffs and edge seeds are fixed-r.

The largest front gap is:

> prove an all-r (or all-r>=r0) contextual recurrence/extraction theorem forcing either a 4r+1 residual of minimum degree r+1 or a controlled 5r+1 design-like terminal, and certify `delta(H_r)>=r` for the resulting cores.

This gap is now even more important because once `delta(H_r)>=r` is available, direct near-anchor forcing turns on automatically for every genuine core.

## 11. Best candidate for the eventual Problem 617 main theorem

> **Direct-Anchor Defect Stability Theorem.** Every extremal counterexample admits a legal residual-core view. The hereditary cap then directly forces a low-excess independent triple. Either the resulting anchor equality is incompatible with the core, or every surviving equality configuration is concentrated into a bounded d<=3 support/design structure; any non-rigid such structure admits a strict repivot potential improvement.

Compared with the previous architecture, the anchor-extraction component no longer needs a common-S dichotomy. Common-S machinery moves downstream and is used only to kill equality/positive-loss structures.

# Unique highest-leverage general-r bridge lemma

## General Residual-Core Extraction Lemma

> **For all sufficiently large r, every hypothetical balanced r-coloring of `K_(r^2+1)` contains, in its least-edge color, either**
>
> **(A)** an induced residual F on `4r+1` vertices with `alpha(F)<=4`, `omega(F)<=r-1`, `delta(F)=r+1`, such that every legal degree-(r+1) pivot core H satisfies `|H|=3r-1` and `delta(H)>=r`; **or**
>
> **(B)** a `5r+1` design-like terminal which is already forced into the multicolor near-Turán stability/nonextension branch.

Why this remains the unique highest-leverage bridge:

1. once it supplies the residual-core contract, direct near-anchor forcing is automatic by hereditary cap;
2. a general near-anchor theorem would then immediately sharpen q to `3r-1` for every core;
3. all medium missing degrees vanish for every r>=12;
4. Bridge B reduces to bounded d2/d3 equality incompatibility rather than broad extraction;
5. it replaces the r=12 1752-node recurrence by one all-r theorem and activates essentially the entire symbolic backend stack.

This remains the theorem that should receive the largest share of research effort.
