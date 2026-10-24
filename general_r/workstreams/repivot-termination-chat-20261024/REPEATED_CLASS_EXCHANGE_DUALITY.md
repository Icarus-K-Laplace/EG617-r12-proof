# Repeated-Class Exchange Duality and the zeta Coordinate

Assumptions: legal regular repivots in one residual graph F, with the standard backend clique cap `omega(F)<=r-1`. The exchange lemma is symbolic in support size d; d2 is the main application.

## 1. View notation

At pivot p let y be a regular shell owner with

`S=S_y`, `D=D_y`, `|S|=|D|=d`,

`T=A\(S union {y})`.

After repivoting through y,

`A_y={p} union T union D`,

`H_y=(H\D) union S`.

Define the exact class

`Y_{S,D}={x in A:x regular, S_x=S, D_x=D}`

with multiplicity m, and let

`Z_0(p)={z in A:z regular,d_z=0}`,

`zeta(p)=|Z_0(p)|`.

---

## 2. Class-to-zero transport

Every `x in Y_{S,D}\{y}` becomes d0 in the y-view.

Indeed, x is target-adjacent to p, T and D, while it is target-nonadjacent to `H\D` and S. Hence

> **`zeta(y)>=m-1`.**                                        (2.1)

**Status:** `PROVED_SYMBOLIC`.

---

## 3. Zero-to-reverse-class transport

Every old d0 owner z becomes a regular reverse owner with

- shell missing set D;
- core support S.

The old pivot p has the same reverse pair `(D,S)`.

Therefore the reverse class in the y-view has multiplicity at least

> **`zeta(p)+1`.**                                           (3.1)

**Status:** `PROVED_SYMBOLIC`.

---

## 4. d0 invariance

If y is itself d0, repivoting only swaps p and y. Every other d0 owner stays d0 and p becomes d0. Hence

> **`zeta(y)=zeta(p)`**                                      (4.1)

for every neutral repivot.

Thus zeta descends to the quotient by d0 pivot relabellings.

---

## 5. Third potential coordinate

Define

> **`Phi_3(p)=(q_p,tau_p,zeta(p))`.**                         (5.1)

It is bounded and integer-valued.

Suppose `p -> y` is q-flat and tau-flat and y lies in an exact repeated `(S,D)` class of multiplicity m. Then (2.1) gives

`zeta(y)>=m-1`.

Therefore

> **if `m>=zeta(p)+2`, then `Phi_3(y)>_lex Phi_3(p)`.**       (5.2)

At a `Phi_3`-maximal pivot,

> **every q/tau-flat exact repeated class has `m<=zeta+1`.** (5.3)

This is a genuine monotonicity theorem.

---

## 6. Equality rigidity and reverse exchange

Assume p is `Phi_3`-maximal and a q/tau-flat repeated-class repivot has

`m=zeta(p)+1`.

Then

`zeta(y)>=m-1=zeta(p)`.

Maximality forces equality:

> **`zeta(y)=zeta(p)=m-1`.**                                 (6.1)

Thus the `m-1` surviving owners from the old class are exactly the full d0 population in the y-view: no extra vertex becomes d0.

Meanwhile the old d0 population plus p forms a reverse `(D,S)` class of multiplicity at least m. A closed `Phi_3`-flat correction cycle therefore requires exact multiplicity balance at each repeated-class exchange.

---

## 7. Balanced correction-cycle clique capacity

Now specialize to a `Phi_3`-flat d2 repeated class. Put

`z=zeta(p)`.

Flatness forces

`m=z+1`.

At p, the following vertices are all regular low-endpoint owners or the pivot:

- the m owners of the repeated `(S,D)` class;
- the z=m-1 d0 owners;
- p itself.

Any two regular low-endpoint owners are target-adjacent, and p is target-adjacent to every shell vertex. Hence these

`m+(m-1)+1=2m`

vertices form a target clique.

Using `omega(F)<=r-1`,

> **`2m<=r-1`, hence `m<=floor((r-1)/2)` and `z<=floor((r-3)/2)`.**   (7.1)

More generally, suppose there are k distinct exact repeated classes at p which each admit a `Phi_3`-flat repivot. Every such class must have multiplicity exactly `z+1`. Their owner sets are disjoint, and together with the z d0 owners and p all vertices again lie in one low-owner target clique. Therefore

> **`(k+1)(z+1)<=r-1`.**                                    (7.2)

Equivalently,

> **`k<=floor((r-1)/(z+1))-1`.**                             (7.3)

This is an exact multiplicity/class-count tradeoff for balanced correction cycles.

**Status:** `PROVED_CONDITIONAL` on the standard backend clique cap.

---

## 8. d2 fully-decorated consequence

For a repeated d2 support D, both vertices of D have support multiplicity at least two and are globally decorated.

If the repivot is tau-flat, then

`|D intersect X|=|S intersect X|=2`.

Thus

> **`S subset X`.**                                         (8.1)

Every `Phi_3`-flat repeated d2 class lies in the unique fully-decorated shell-pair regime.

Combining the results:

- multiplicity `m<=zeta+1` at `Phi_3` maximality;
- a `Phi_3`-flat class has exact `m=zeta+1`;
- balanced class multiplicity satisfies `m<=floor((r-1)/2)`;
- k simultaneous flat repeated classes satisfy `(k+1)(zeta+1)<=r-1`.

Thus repeated plateau multiplicity is coupled rigidly to the neutral population and low-owner clique capacity.

---

## 9. Main-theorem impact

The current preferred potential is

> **`Phi=(q,tau,zeta,...)`.**

The repeated-support part of the plateau is no longer an uncontrolled multiplicity problem. Any class above the zeta threshold improves the potential; equality produces a balanced reverse exchange satisfying the clique-capacity product bound.

A fourth coordinate is needed only for

1. distinct-support fully-decorated d2 plateau systems; and
2. zeta-balanced repeated correction cycles satisfying (7.2).

Complete elimination of those two regimes remains open.