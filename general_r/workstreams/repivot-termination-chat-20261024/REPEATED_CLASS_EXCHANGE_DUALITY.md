# Repeated-Class Exchange Duality and the zeta Coordinate

Assumptions: legal regular repivots in one residual graph F, with the standard backend clique cap `omega(F)<=r-1` where explicitly used. The exchange theorem is symbolic in support size d; d2 is the main application.

## 1. View notation

At pivot p let y be a regular shell owner with

`S=S_y`, `D=D_y`, `|S|=|D|=d`,

`T=A\(S union {y})`.

After repivoting through y,

`A_y={p} union T union D`,

`H_y=(H\D) union S`.

Define the complete exact class

`Y_{S,D}(p)={x in A:x regular, S_x=S, D_x=D}`

with multiplicity

`m=m_p(S,D)`.

Let

`Z_0(p)={z in A:z regular,d_z=0}`,

`zeta(p)=|Z_0(p)|`.

---

## 2. Exact class-neutral involution

### Theorem 2.1

For the repivot `p -> y` through `y in Y_{S,D}(p)`, one has the exact identities

> **`zeta(y)=m_p(S,D)-1`,**                                  (2.1)
>
> **`m_y(D,S)=zeta(p)+1`.**                                  (2.2)

Thus the pair

> **`(m,zeta)` transforms exactly as `(m,zeta) -> (zeta+1,m-1)`.**   (2.3)

The transformation is an involution.

### Proof

Every other owner `x in Y_{S,D}(p)\{y}` becomes d0 in the y-view: x is target-adjacent to p, T and D, and target-nonadjacent to `H\D` and S. Hence initially

`zeta(y)>=m-1`.

Conversely, take any d0 owner z in the y-view and repivot back through the old pivot p, whose reverse pair is `(D,S)`. A d0 owner under this inverse exchange becomes an `(S,D)` owner in the p-view. Distinct d0 vertices give distinct old `(S,D)` owners, and the old pivot y itself is also an `(S,D)` owner. Therefore

`m_p(S,D)>=zeta(y)+1`.

Combining with `zeta(y)>=m-1` gives equality (2.1).

Similarly, every old d0 owner in `Z_0(p)` becomes a reverse `(D,S)` owner in the y-view, and p itself is another such owner, so

`m_y(D,S)>=zeta(p)+1`.

Apply the first equality (2.1) to the inverse repivot `y -> p`: the reverse class multiplicity equals the old neutral population plus one. Hence equality (2.2).

Applying (2.3) twice gives

`(m,zeta) -> (zeta+1,m-1) -> (m,zeta)`,

so the exchange is an exact involution. QED.

**Status:** `PROVED_SYMBOLIC`.

---

## 3. d0 invariance

For d=0 the exact class is the neutral population itself. Repivoting through a d0 owner swaps p with that owner and preserves zeta:

> **`zeta(y)=zeta(p)`.**                                      (3.1)

Thus zeta descends to the quotient by neutral pivot relabellings.

---

## 4. Third potential coordinate

Define

> **`Phi_3(p)=(q_p,tau_p,zeta(p))`.**                         (4.1)

It is bounded and integer-valued.

Suppose `p -> y` is q-flat and tau-flat and y lies in an exact `(S,D)` class of multiplicity m. By the exact exchange theorem,

> **`zeta(y)=m-1`.**                                         (4.2)

Therefore:

- `m>=zeta(p)+2` gives strict `Phi_3` improvement;
- `m=zeta(p)+1` is exactly `Phi_3`-flat;
- `m<=zeta(p)` strictly decreases the third coordinate.

Hence at a `Phi_3`-maximal pivot every q/tau-flat class satisfies

> **`m<=zeta+1`,**                                           (4.3)

and the equality case is characterized exactly by

> **`m=zeta+1 iff the class repivot is Phi_3-flat`.**         (4.4)

This replaces the previous one-sided inequality by an exact update law.

---

## 5. Reverse multiplicity at every class exchange

For any exact class, not only a repeated one, a repivot exchanges class multiplicity and neutral population:

> forward class multiplicity `m` becomes new neutral count `m-1`;
>
> old neutral count `zeta` becomes reverse-class multiplicity `zeta+1`.

In particular, a distinct-support class (`m=1`) always sends

> **`zeta -> 0`**                                             (5.1)

on a q/tau-flat repivot, while creating a reverse class of multiplicity `zeta+1`.

Thus a q/tau-flat distinct-class move is `Phi_3`-flat exactly when `zeta=0`; if `zeta>0` it strictly lowers the third coordinate and its inverse is a repeated-class zeta increase back to the original level.

This sharply separates the distinct-support branch from the balanced repeated branch.

---

## 6. Balanced correction-class capacity

Now specialize to a `Phi_3`-flat d2 exact class. By (4.4),

`m=zeta+1`.

At p, the following vertices form a target clique:

- the m owners of the exact class;
- the zeta=m-1 d0 owners;
- p.

Its size is `2m`. Using `omega(F)<=r-1`,

> **`2m<=r-1`, hence `m<=floor((r-1)/2)` and `zeta<=floor((r-3)/2)`.**   (6.1)

If k distinct exact classes at p each admit `Phi_3`-flat repivots, every one has multiplicity `zeta+1`. Their owner sets are disjoint, so together with the zeta d0 owners and p they form a clique of size `(k+1)(zeta+1)`. Hence

> **`(k+1)(zeta+1)<=r-1`.**                                  (6.2)

**Status:** `PROVED_CONDITIONAL` on the standard backend clique cap.

---

## 7. d2 fully-decorated consequence

For a repeated d2 support D, both vertices of D have support multiplicity at least two and are globally decorated.

If its repivot is tau-flat, then

`|D intersect X|=|S intersect X|=2`,

so

> **`S subset X`.**                                         (7.1)

Thus every `Phi_3`-flat repeated d2 class lies in the fully-decorated shell-pair regime.

For a distinct d2 class (`m=1`), the exact update (5.1) shows that a `Phi_3`-flat distinct move additionally forces

> **`zeta=0`.**                                              (7.2)

This is a new restriction on the distinct-support plateau.

---

## 8. Main-theorem impact

The current preferred potential is

> **`Phi=(q,tau,zeta,...)`.**

The third coordinate now has an exact update law on every exact class exchange:

`zeta(new)=m(class)-1`.

Therefore the remaining plateau separates cleanly into:

1. **balanced class exchanges** with `m=zeta+1`, which are exactly `Phi_3`-flat;
2. **distinct class moves** with `m=1`, which can be `Phi_3`-flat only at `zeta=0`;
3. all larger-than-balanced classes, which strictly improve zeta.

The next potential/termination problem should exploit the new fact that the genuinely distinct-support `Phi_3` plateau lives entirely in the neutral-free slice `zeta=0`.