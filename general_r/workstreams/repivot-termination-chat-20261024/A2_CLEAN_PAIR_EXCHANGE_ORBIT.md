# Allowance-2 Clean Pair-Exchange Orbit Theorem

Status: `PROVED_CONDITIONAL`.

Purpose: extract the first genuinely scalable rigid design object from the remaining fully-decorated distinct-support d2 plateau.

Dependencies:

- hypotheses A+B and `r>=12`;
- `D2_DISTINCT_SUPPORT_REDUCTION.md`;
- exact pair-set transition under repivot;
- row closure;
- exact transported excess identity;
- `alpha(H)<=3` only for the bound on zero-weight support vertices.

No use is made of the invalid global assertion `alpha(F)<=3`.

---

## 1. Setup

Work at a `Phi_3=(q,tau,zeta)`-maximal pivot in the neutral-free distinct slice

`zeta=0`.

Fix one fully-decorated d2 shell pair

`S={s_1,s_2} subset X`

with allowance

`a=2`.

For a q-flat core support `D=xy`, write

`w_x=kappa_x+e_F(x,S)`,

`mu(D)=1-e_H(xy)`.

Then

> `w_x+w_y+mu(D)=2`.                                         (1.1)

Call D **clean** if

- `xy` is a target edge of H;
- `w_x=w_y=1`.

Thus clean supports are exactly the zero-free `(1,1)` support type.

---

## 2. Any disjoint a=2 family has at most three exceptional blocks

Let

`D_1,...,D_m`

be pairwise-disjoint q-flat supports in the fixed class.

At a=2 the non-clean support types are

- target edges of weights `(0,2)` or `(2,0)`;
- target nonedges of weights `(0,1)` or `(1,0)`.

Hence every non-clean support contains a zero-weight vertex.

All zero-weight support vertices are pairwise target-nonadjacent by row closure. Since `alpha(H)<=3`, there are at most three such vertices.

Because the D_i are pairwise disjoint, each zero vertex lies in at most one D_i.

Therefore

> **among pairwise-disjoint a=2 q-flat supports, at most three are non-clean.**   (2.1)

Equivalently every disjoint family of size m contains at least

> **`m-3` clean blocks.**                                    (2.2)

This turns every large matching into an almost-pure clean-pair system.

---

## 3. Exact transport through one clean block

Choose one clean support

`D_i={x_i^0,x_i^1}`

and repivot through its owner y_i.

Let another clean support

`D_j={x_j^0,x_j^1}`

be disjoint from D_i.

By the exact pair-set transition theorem, y_j remains a regular d2 owner in the y_i-view:

- its new missing pair is D_i;
- its new core support is still D_j.

For an endpoint z of D_j, the transported excess identity is

`kappa'_z=w_z-e_H(z,D_i)`.                                  (3.1)

Because D_j is clean,

`w_z=1`.                                                     (3.2)

Row closure gives

`e_H(z,D_i)<=1`.                                             (3.3)

Hence

> `kappa'_z=1-e_H(z,D_i) in {0,1}`.                          (3.4)

Relative to the new common missing pair D_i, the new common-S weight of z is

`w'_z=kappa'_z+e_F(z,D_i)`.

Since z and D_i are old core vertices,

`e_F(z,D_i)=e_H(z,D_i)`.

Combining with (3.4),

> **`w'_z=1`.**                                              (3.5)

The internal target edge of D_j is unchanged. Thus

> **every old clean support disjoint from D_i remains a clean `(1,1)` target-K2 support after repivot through D_i.**   (3.6)

In particular the new common-pair allowance is again exactly2 whenever at least one such clean support survives.

This is an exact closure law, not an asymptotic approximation.

---

## 4. Pair-exchange orbit

Let

`P_1,...,P_k`

be pairwise-disjoint clean supports belonging to the same q/tau/zeta-flat plateau, with `k>=2`.

For every i, repivot through the owner of P_i has the following effect on the remaining clean blocks:

- P_i becomes the new shell missing pair;
- every P_j, j!=i, remains a clean d2 core support;
- every endpoint weight relative to the new missing pair remains exactly1;
- all these owner pivots stay on the same q/tau/zeta plateau.

Therefore the clean subsystem is closed under exchanging the distinguished shell pair with any one clean core pair.

> **Clean Pair-Exchange Orbit.**
>
> A disjoint family of clean a=2 plateau supports is a repivot-closed pair system: modulo objects outside the subsystem, the local correction dynamics only chooses which clean pair is the shell pair and which clean pairs remain in the core.   (4.1)

This is the first scalable rigid design terminal extracted in the general-r backend.

---

## 5. The old shell pair as the unique possible special block

Repivot through a clean D_i. The old pivot p becomes a d2 owner whose new core support is the old shell pair S.

Write

`b=e_M(S) in {0,1}`

and transport slacks

`sigma_1+sigma_2=2-b`.

For `s in S`,

`kappa'_s=sigma_s-e_F(s,D_i)`,

and its new weight relative to shell pair D_i is

`w'_s=kappa'_s+e_F(s,D_i)=sigma_s`.                           (5.1)

The old shell pair has internal target defect b, so its reverse support satisfies

> `w'(S)+mu(S)=(sigma_1+sigma_2)+b=2`.                       (5.2)

Thus the reverse support is one of exactly three symbolic types:

1. `b=0`, `(sigma_1,sigma_2)=(1,1)`: S is itself clean;
2. `b=0`, slacks `(0,2)` up to order: S is a target edge of weights `(0,2)`;
3. `b=1`, slacks `(0,1)` up to order: S is a target nonedge of weights `(0,1)`.

So the correction orbit consists of a clean pair system plus at most a bounded number of special zero-containing blocks.

---

## 6. Extraction from an arbitrary large a=2 distinct-support family

`D2_DISTINCT_SUPPORT_REDUCTION.md` already proves that the zero-free `(1,1)` support graph has maximum degree at most3.

Hence if it has E clean support edges, a greedy matching has size at least

> `ceil(E/5)`.                                                (6.1)

(Each chosen edge removes itself and at most four other edges incident with its two endpoints.)

Combined with Section2:

> every unbounded a=2 distinct-support family contains an unbounded clean disjoint subsystem, and every linear-size a=2 family contains a linear-size clean matching subsystem.   (6.2)

By Sections3--5 that subsystem is repivot-closed under pair exchange, up to at most three exceptional zero-containing blocks.

Therefore the former `a=2 max-degree-three graph` blocker is sharpened to one rigid scalable object:

> **a clean pair-exchange design plus O(1) special blocks.**   (6.3)

---

## 7. Structural encoding of the clean terminal

For clean blocks

`P_i={x_i^0,x_i^1}`,

every endpoint has weight1 relative to the distinguished shell pair.

For two distinct clean blocks P_i,P_j, row closure gives

> each endpoint of P_i has at most one target neighbour in P_j.   (7.1)

Hence the target cross graph between two clean blocks is a matching of size0,1,or2.

Equivalently the complete clean terminal is encoded by a 2-vertex block system in which

- every block is a target K2;
- every inter-block target graph is a matching;
- `alpha(H)<=3` forbids an independent transversal through four blocks;
- repivot exchanges the distinguished pair while preserving the clean block condition.

This bounded local rule is independent of r. The number of blocks may still scale with r.

---

## 8. Main-theorem impact

This theorem does **not** yet contradict the clean terminal. It does something more structural than the previous max-degree-three reduction:

- arbitrary a=2 overlap geometry is no longer the scalable object;
- every scalable branch contains a large repivot-closed clean pair system;
- all local data of that system are fixed (`K2` blocks, weight1 endpoints, matching cross graphs);
- only the number of blocks grows with r;
- all non-clean contamination is O(1) inside a disjoint subsystem.

Thus the next blocker is a single design/nonextension problem:

> **Clean Pair Nonextension Theorem.** Show that a sufficiently large repivot-closed system of clean K2 blocks with matching cross graphs and no independent 4-transversal is incompatible with the hereditary cap, clique cap, or global multicolor structure.

A successful proof would close the first genuinely scalable allowance layer `a=2`.