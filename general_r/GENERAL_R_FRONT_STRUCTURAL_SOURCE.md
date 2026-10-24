# General-r Front Structural Source

Status: **PROVED_SYMBOLIC for the algebraic/color-class statements; extraction recurrence remains OPEN**.

## 1. Counterexample color-class contract

Suppose an r-coloring of `K_(r^2+1)` is a counterexample to Erdős Problem 617, i.e. every `(r+1)`-vertex set sees every color.

Fix one color and let G be its spanning color graph. Then

- `alpha(G)<=r`, because an independent `(r+1)`-set would miss this color;
- `omega(G)<=r`, because a monochromatic `(r+1)`-clique in this color would miss every other color.

For the least-edge color,

> **`e(G)<=C(r^2+1,2)/r = r(r^2+1)/2`.**

For r=12 this is 870.

## 2. General hereditary cap

Let `p_r(n)` be the minimum number of edges in an n-vertex graph with independence number at most r; by Turán complementarity this is the number of edges in a union of r balanced cliques.

On any n-set W, each of the other `r-1` color graphs has independence number at most r, hence contributes at least `p_r(n)` edges. Since the color classes partition all pairs,

> **`e_G(W)<=D_r(n):=C(n,2)-(r-1)p_r(n)`.**

This is the exact general form of the r=12 inherited D-cap.

## 3. K_r block cross-matching

At `n=r+1`, one has `p_r(r+1)=1`, so

`D_r(r+1)=C(r+1,2)-(r-1)=C(r,2)+1`.

Let Q be a target `K_r` and x an outside vertex. If x had two target neighbours in Q, then `Q union {x}` would contain

`C(r,2)+2>D_r(r+1)`

target edges, impossible.

Hence:

> every outside vertex has at most one target neighbour in a target K_r;
>
> cross edges between pairwise-disjoint target K_r blocks form matchings.

This is the all-r source of the r=12 K12-block matching geometry.

## 4. Anchor/block residual order

Take a vertex v of target degree d. Its nonneighbourhood has

`r^2-d`

vertices. Remove j disjoint target `K_r` blocks from this nonneighbourhood. The residual R has exact order

> **`|R|=r^2-d-jr`.**

Maximality/greedy representatives give the symbolic independence estimate corresponding to the r=12 argument:

`alpha(R)<=r-1-j`.

A maximal block packing also gives

`omega(R)<=r-1`.

## 5. Origin of 4r+1 and 5r+1

At the r=12 terminal anchor degree one has `d=r-1`.

Then

`|R|=r^2-r+1-jr`.

If

`j=r-5`,

then

> **`|R|=4r+1`**

and the greedy bound gives `alpha(R)<=4`.

If

`j=r-6`,

then

> **`|R|=5r+1`**

and `alpha(R)<=5`.

Thus the constants 49 and 61 are not numerical fits: they are exact consequences of the anchor/block-packing algebra.

What remains OPEN is the forcing statement that a hypothetical general-r counterexample must reach anchor degree `r-1` and one of these block counts. The r=12 proof establishes this by a 1752-node contextual recurrence with r=12-specific seeds.

## 6. Conditional backend residual

If the front reduction supplies a legal induced target residual F on `4r+1` vertices with

`alpha(F)<=4`, `omega(F)<=r-1`, and minimum degree `r+1`,

then a minimum-degree pivot has

- shell size `r+1`;
- core size

> **`(4r+1)-1-(r+1)=3r-1`.**

The independence cap descends to

`alpha(H)<=3`

because an independent four-set in H together with the pivot is an independent five-set in F.

The clique cap descends to

`omega(H)<=r-1`.

The only part of the desired residual-core contract not supplied by this algebra is

> **`delta(H)>=r`.**

For r=12 this is proved from lower-order Ramsey/cap seeds. Its all-r analogue is currently OPEN and is a load-bearing generalization gap.

## 7. Front-end bottleneck

The r=12 contextual recurrence is already symbolically shaped in `(a,n,h)` and uses exact minimum-pivot identities, matching lower bounds, triangle alternatives and deletion averaging. However its maximum-order cutoffs and edge floors are r=12-specific.

The general front-end problem is therefore:

> prove symbolic lower-order cutoffs/floors strong enough that the recurrence has no stops except the `4r+1` extraction or a controlled `5r+1` obstruction.

This—not the formulas 49 or61 themselves—is the general front-end gap.
