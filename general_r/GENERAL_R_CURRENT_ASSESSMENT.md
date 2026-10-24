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
- support overlap threshold `d-1`, first-high-slack `a=d`, and allowance transport are symbolic.

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

## 4. Can the anchor theorem be generalized?

Substantially, but not completely.

Already symbolic:

- exact three-anchor partition;
- connector count2/3/4;
- block-size patterns as shifts of r-2;
- any low-excess independent triple reduces to the exact degree-r anchor problem for r>=12.

Remaining theorem:

> three pairwise nonadjacent degree-r vertices => `K_r>=8`?

This is proved for r=12 and OPEN for general r.

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
- loss-layer overlap threshold and repeated-support strict loss.

The only r-sensitive pieces are the anchor-excess theorem and hereditary capacity function.

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

## 7. Is there a monotone symbolic repivot potential?

Partially.

`(q,tau)` is a genuine bounded symbolic lexicographic potential, and repeated non-fully-decorated plateau supports strictly improve tau at equal q.

What is OPEN is a global theorem that every non-rigid local view improves `(q,tau)` or a finite refinement of it. Higher-slack equality can currently preserve both coordinates.

## 8. Do we have a sufficiently-large-r contradiction?

Not yet.

But a major simplification is proved:

- `q<=3r+2` under the baseline core floor;
- for r>=15, regular missing degrees `4,...,r-3` are impossible;
- high endpoint sizes `d>=r-2` support at most three common-S owners.

Hence all scalable support complexity for r>=15 lies at `d<=3`.

This is strong asymptotic reduction, not yet a contradiction.

Ordinary one-color Turán stability is also insufficient by itself because average color slack is Theta(r^2). A multicolor compatibility gain is needed.

## 9. Largest general front-end gap

The r=12 recurrence already has a symbolic form in local variables, but its order cutoffs and edge seeds are fixed-r.

The largest front gap is:

> prove an all-r (or all-r>=r0) contextual recurrence/extraction theorem forcing either a 4r+1 residual of minimum degree r+1 or a controlled 5r+1 design-like terminal, and certify `delta(H_r)>=r` for the resulting cores.

## 10. Best candidate for the eventual Problem 617 main theorem

> **Defect-Transport Stability Theorem.** In every extremal counterexample, a lexicographically maximal local view either transports defect into an independent low-excess anchor configuration, concentrates it into a bounded sunflower/design structure, or admits an improving repivot. The anchor branch violates the residual-core excess bound; the concentrated branch violates hereditary/multicolor capacity; the improvement branch contradicts maximality.

This theorem would conceptually unify the front/backend local machinery with the near-affine stability picture.

# Unique highest-leverage general-r bridge lemma

## General Residual-Core Extraction Lemma

> **For all sufficiently large r, every hypothetical balanced r-coloring of `K_(r^2+1)` contains, in its least-edge color, either**
>
> **(A)** an induced residual F on `4r+1` vertices with `alpha(F)<=4`, `omega(F)<=r-1`, `delta(F)=r+1`, such that every legal degree-(r+1) pivot core H satisfies `|H|=3r-1` and `delta(H)>=r`; **or**
>
> **(B)** a `5r+1` design-like terminal which is already forced into the multicolor near-Turán stability/nonextension branch.

Why this is the unique highest-leverage bridge:

1. all formulas after it are now largely symbolic;
2. it activates the universal q ceiling `3r+2` and r>=15 support collapse;
3. it makes the exact-anchor and support-compatibility theorems directly applicable;
4. it replaces the r=12 1752-node recurrence by one all-r theorem;
5. it is upstream of every backend contradiction, so proving it moves the dependency DAG more than any additional fixed-r lemma.

This is the next theorem that should receive the largest share of research effort.
