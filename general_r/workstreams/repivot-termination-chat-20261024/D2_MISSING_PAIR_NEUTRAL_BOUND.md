# d2 Missing-Pair / Neutral-Population Bound

Assumptions: A+B, `r>=12`, and the standard backend global forbidden-configuration caps used by the existing missing-pair asset: `alpha(F)<=3`, `omega(F)<=r-1`. Let p be a legal pivot and let

`zeta=zeta(p)`

be the number of regular d0 owners in its shell.

## 1. Common-nonneighbour clique for a missing core pair

Let

`D={x,z} subset H`

be a target-nonedge in H. Let C be the set of vertices of `H\D` target-nonadjacent to both x and z.

Because xz is a nonedge and `alpha(H)<=3`, C is a target clique: if two points of C were target-nonadjacent, together with x,z they would form an independent 4-set.

Write

`c=|N_H(x) intersect N_H(z)|`.

Since

`d_H(x)=r+kappa_x`, `d_H(z)=r+kappa_z`, `|H|=3r-1`,

a four-part partition of `H\{x,z}` gives

> `c-|C|=kappa(D)-r+3`.

Hence

> **`|C|=c+r-3-kappa(D)>=r-3-kappa(D)`.**                    (1.1)

This is the general missing-pair common-nonneighbour lower bound.

---

## 2. Neutral population enlarges the common-nonneighbour clique

Every d0 shell owner has no target neighbour in the old core H. Therefore every one of the zeta d0 owners is target-nonadjacent to both x and z.

The pivot p is also target-nonadjacent to every core vertex, hence to x,z.

Thus

`C union Z_0(p) union {p}`

is contained in the common target-nonneighbour set of the nonedge pair x,z in F.

For a nonedge pair, any two common nonneighbours must be target-adjacent, otherwise those two vertices together with x,z form an independent 4-set. Hence the displayed set is a target clique in F.

Using `omega(F)<=r-1`,

`|C|+zeta+1<=r-1`.

Combine with (1.1):

`r-3-kappa(D)+zeta+1<=r-1`.

Therefore

> **Neutral/missing-pair excess bound**
>
> **`kappa(D)>=zeta-1`.**                                   (2.1)

**Status:** `PROVED_SYMBOLIC` under the stated global alpha/omega backend caps.

---

## 3. q-flat d2 consequence

Fix a d2 shell class S with allowance a. For an owner with core support D,

`q-q_y=a-[w(D)+mu(D)]`,

where

`w(D)=kappa(D)+e_F(S,D)`

and `mu(D)=1-e_H(D)`.

If the row is q-flat and D is a target-nonedge, then `mu(D)=1`, so

`a=w(D)+1>=kappa(D)+1`.

By (2.1),

> **`a>=zeta`.**                                             (3.1)

Equivalently:

> **If `a<zeta`, every q-flat d2 support must be a target edge in H.**   (3.2)

This applies equally to distinct and repeated support classes.

For a q/tau/zeta-flat repeated class at `Phi_3` maximality, the repeated-class exchange theorem gives `m<=zeta+1`. If its support is a nonedge, then additionally

> `m<=zeta+1<=a+1`.                                         (3.3)

Thus a balanced repeated nonedge correction class can scale only together with the shell allowance.

---

## 4. Equality structure

If `kappa(D)=zeta-1`, then equality must hold in every step used above:

1. `c=0`, so x and z have no common target neighbour in H;
2. `|C|=r-zeta-2`;
3. `C union Z_0(p) union {p}` is a maximum-size clique allowed by the derived count, of size `r-1`;
4. every additional common nonneighbour of x,z outside this displayed set is forbidden.

If in addition a q-flat row has `a=zeta`, then

`w(D)=zeta-1=kappa(D)`,

so

> `e_F(S,D)=0`.

Hence the sharp nonedge boundary is a rigid correction block: the support pair has no common H-neighbour, no target edge to the shell pair S, and its common-nonneighbour clique is saturated by the old pivot, all neutral owners, and `r-zeta-2` core vertices.

This is a finite equality template suitable for the next correction-cycle classification.

---

## 5. Main-theorem impact

The unique scalable q-flat d2 regime already requires `S subset X`.

This theorem splits its core supports into:

- **edge supports** (`mu=0`), which remain the main distinct-support branch;
- **nonedge supports** (`mu=1`), which require `a>=zeta`, and at equality `a=zeta` collapse to a saturated common-nonneighbour clique template.

Therefore the fully-decorated blocker can now be attacked separately in the low-allowance region `a<zeta` (edge supports only) and the high-allowance region `a>=zeta` (nonedge supports allowed but charged by neutral-population excess).