# Global d=3 Pattern Charge Barriers

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_ONE_LOSS_PATTERN_CAPACITY.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: turn the final three-class Type-H / Type-P equality patterns into explicit lower bounds on the total common-S charge W.

## 1. Setup

Let H have n vertices and `alpha(H)<=3`.

Let

`W=sum_(v in H) w_v`.                                      (B1)

Work in a d3 boundary one-loss support system.

The canonical nontrivial pattern families are Type H and Type P from `GLOBAL_D3_ONE_LOSS_PATTERN_CAPACITY.md`.

## 2. Type H with three distinct supports

Assume a Type-H pattern family has exactly three distinct support classes

`D_i={x,u_i,v_i}`, `i=1,2,3`,                              (B2)

where

- x is the common zero-charge hub;
- every D_i is a target K3;
- every private petal u_i,v_i has charge1;
- private petals from distinct supports are target-anticomplete.

Thus the three private pairs

`P_i={u_i,v_i}`

are target K2s, while every cross pair `P_i--P_j` is a target nonedge.

The union of the pattern contains

`1+3*2=7`

core vertices.

## 3. Every outside vertex has charge at least two

Take

`z in H\({x} union P_1 union P_2 union P_3)`.               (B3)

Suppose z is not target-complete to any P_i.

Then for each i choose a petal

`p_i in P_i`

which is target-nonadjacent to z.

The p_i are pairwise target-nonadjacent because different private pairs are cross-anticomplete.

Hence

`{z,p_1,p_2,p_3}`

is an independent4 in H, contradiction.

Therefore z is target-complete to at least one private pair P_i.

Since z lies outside support D_i, row closure gives

`e_H(z,D_i)<=w_z`.                                          (B4)

Completeness to the two petals already contributes two target neighbours in D_i, so

> `w_z>=2`.                                                  (B5)

## 4. Type-H total charge barrier

The six private petals contribute exactly

`6`

units of charge.

The common hub contributes0.

There are `n-7` outside vertices and each has charge at least2 by (B5).

Therefore

> **Type-H three-class charge barrier**
>
> `W>=6+2(n-7)=2n-8`.                                      (B6)

For the r=12 35-core:

> `W>=62`.                                                   (B7)

Hence any channel with `W<=61` cannot contain a three-class Type-H one-loss pattern.

## 5. Type P with three distinct supports

Assume a Type-P family has exactly three distinct supports

`D_i={x,y,z_i}`, `i=1,2,3`.                                (B8)

The common zero-charge pair `{x,y}` is a target edge.

Each private petal z_i has

`w_(z_i) in {1,2}`,                                         (B9)

and the three private petals are pairwise target-nonadjacent.

The pattern union has five vertices.

## 6. Every outside vertex has positive charge

Take

`v in H\{x,y,z_1,z_2,z_3}`.                                (B10)

If v were target-nonadjacent to all three private petals, then

`{v,z_1,z_2,z_3}`

would be an independent4, contradiction.

Hence v is target-adjacent to at least one z_i.

Since v lies outside support D_i, row closure gives

`e_H(v,D_i)<=w_v`.                                          (B11)

The edge vz_i is already one target edge into D_i, so

> `w_v>=1`.                                                  (B12)

## 7. Type-P total charge barrier

The three private petals contribute at least3 units of charge.

The common pair contributes zero.

There are `n-5` outside vertices, each of charge at least1.

Therefore

> **Type-P three-class charge barrier**
>
> `W>=3+(n-5)=n-2`.                                        (B13)

For the r=12 35-core:

> `W>=33`.                                                   (B14)

Hence any channel with `W<=32` cannot contain a three-class Type-P one-loss pattern.

## 8. Consequence at low total charge

Suppose a d3 one-loss common-S pattern family lies in the 35-core.

- If `W<=32`, every nontrivial Type-H or Type-P pattern family has at most two distinct support classes.
- If `W<=61`, every Type-H pattern family has at most two distinct support classes.

Thus under the charge ranges encountered in low-excess backend channels, a large owner family is forced onto at most two supports per canonical pattern, sharply increasing repeated-support multiplicity.

## 9. Equality rigidity

Equality in (B6) forces every outside Type-H vertex to have charge exactly2 and to be complete to at least one private K2.

Equality in (B13) forces every outside Type-P vertex to have charge exactly1 and to meet the private-petal independent triple.

These are global covering geometries suitable for a second hereditary-cap or incidence-count contradiction if the scalar threshold is attained exactly.

## 10. Generalization

The formulas are written for `alpha(H)<=3`. With a larger independence bound, the same idea applies to a correspondingly larger family of cross-anticomplete petal blocks / private independent petals.