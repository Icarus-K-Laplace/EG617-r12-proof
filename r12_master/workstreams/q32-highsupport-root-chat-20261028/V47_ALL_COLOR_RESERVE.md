# E408 Q32 — v=47 all-color reserve and source-correct gap ledger

Date: 2026-10-28
Status: **PROVED_CONDITIONAL reductions; v=47 remains OPEN.**

This file builds on `HIGH_SUPPORT_NEAR_TURAN.md` and the registered Q32 285-edge contract. No retracted degree-nine or exceptional-injectivity claim is used.

## 1. Exact 37-unit core-gap identity

The complement of the target core has

`e(bar H)=C(47,2)-285=796`.

Every one of the eleven non-target colors C satisfies the ordinary 47-point floor

`e_C(H)>=69`.

Define

`g_C := e_C(H)-69 >=0`.

Since the eleven non-target colors partition `bar H`, one has the exact identity

> **`sum_C g_C = 796-11*69 = 37`.**

Thus v=47 is a 37-unit multicolor near-Turan packing problem, not eleven independent single-color problems.

## 2. Exact-color gap cap

For an exact-129 color, the source-correct Type-I placement theorem gives

> **`0<=g_C<=6`.**

More precisely:

- `x_C in O`: eleven witnesses and `g_C<=4`;
- `x_C in H`, two-double placement: ten witnesses and `g_C<=5`;
- `x_C in H`, triple placement: eleven witnesses and `g_C<=6`.

The 69 and 70 layers have the rigid `4^11,3` Turan partition normal form recorded in `HIGH_SUPPORT_NEAR_TURAN.md`.

## 3. Shell-edge variable and exact tradeoff

Let

`mu_C := e_C(A)`

for a non-target color C. Because all p--A edges are target-colored, this is also the number of C-edges induced by `O={p} union A`.

For an exact color,

`129 = (69+g_C) + e_C(H,O) + mu_C`,

so

`e_C(H,O)=60-g_C-mu_C`.

Consequently the sum of the C-degrees over O is

`60-g_C+mu_C`.

Subtracting the degree-four baseline at the fourteen O-points gives

> **`S_O(C):=sum_{z in O}(d_C(z)-4)=4+mu_C-g_C`.**

In the verified Type-I graph, the ten isolated-K5 vertices have degree four, while every point of the 11-point gadget has degree at least five. Both special K5s `Ns,Nt` meet O.

Therefore:

- if `x_C in H`, at least one O-point lies in each of `Ns,Nt`, so `S_O(C)>=2` and
  
  > **`g_C <= mu_C+2`;**

- if `x_C in O`, those two gadget incidences plus x itself give `S_O(C)>=3`, so
  
  > **`g_C <= mu_C+1`.**

This is stronger than the generic degree-floor inequality and is source-correct.

## 4. Minimum shell-edge payment of an exact color

The K5 outside-count normal form also forces a direct M-edge payment.

- `x in O`: the unique double-outside K5 contributes one shell-shell edge. In addition, the Type-I gadget necessarily contributes at least one O-O color edge: if an O-point of `Ns\A0` or `Nt\{y}` is present, it is adjacent to x; otherwise the required O-points can be chosen only through `A0` and y, which creates a y--A0 O-O edge. Hence
  
  > `mu_C>=2`.

- `x in H`, two-double: the two double-outside K5s contribute two shell-shell edges, hence
  
  > `mu_C>=2`.

- `x in H`, triple: the triple-outside K5 contributes its shell triangle, hence
  
  > `mu_C>=3`.

Thus every exact color spends at least two of the shell-complement edges, and every in-H triple type spends at least three.

If `t` is the number of exact in-H triple types, then for the exact colors collectively

> **`M_exact := sum_exact mu_C >= 2m+t`.**

Since the eleven non-target colors partition M,

`M_exact <= e(M) <=32`.

This is a necessary compatibility condition, not yet a contradiction.

## 5. Full source-degree gadget quota at every residual point

For an exact Type-I color, a residual vertex has degree exactly four iff it lies in one of the ten isolated K5 components. Every vertex of the 11-point gadget has degree at least five.

Let `q_z` be the number of exact colors for which a residual point z lies in the 11-point gadget. The latest nonexact pointwise floors are

`L_8=12, L_9=7, L_10=2`.

At every residual point z,

`60 >= 13 + 4m + q_z + L_m`.

Therefore

> **`q_z<=3` for m=8; `q_z<=4` for m=9; `q_z<=5` for m=10.**

This counts every gadget membership, not merely the KP special point x.

Equivalently, every residual point lies in an isolated K5 component of at least five exact colors, for all three values m=8,9,10.

## 6. Strong m=8 weighted-surplus ledger

When `m=8`, all three nonexact colors have 130 edges and the new theorem gives degree at least four in each. Hence at every residual point z,

> **`(d_F(z)-13) + sum_{11 non-target C}(d_C(z)-4) = 3`.**

For an exact Type-I color with source parameter a, the variable gadget surpluses over degree four are

- at y: `a`;
- at x: `5-a`.

The pointwise capacity three therefore forbids `a=1` (x would use surplus4) and forbids `a=4` (y would use surplus4). Thus:

> **for every exact color in the m=8 branch, `a in {2,3}`.**

The two variable vertices then carry surplus weights `{3,2}`. Since any two variable occurrences would have total weight at least four, no residual point can be a variable vertex for two exact colors. Consequently the sixteen vertices

`{x_C,y_C : C exact}`

are pairwise distinct in the m=8 branch.

This is a source-correct replacement for the kind of injectivity that the retracted degree-nine route attempted to obtain, but it is specific to m=8 and follows from the new 130-edge minimum-degree-four theorem.

## 7. Status

The results above materially reduce v=47 but do not yet eliminate it. In particular, exact 69-edge realizations exist at the local source interface, so no root promotion is permitted.

Next load-bearing target: combine the 37-unit gap identity, the exact `g_C--mu_C` tradeoff, the m=8 weighted gadget packing (or the m=9/10 analogues), and edge uniqueness in the common H/M pools.
