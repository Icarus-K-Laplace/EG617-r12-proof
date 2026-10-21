# S30: remaining singleton-edge configurations

Scope: ONLY the specified row-labelled `(5,7,8,8)` case inside the canonical S30 contract. This document neither claims all S30 states have this profile nor proves the outer T61-to-S30 interface.

## S0. Explicit incidence contract — CONDITIONAL

C has47 vertices, four pairwise anticomplete row triangles `T_s,T_C,T_A,T_B`, and H of order35. Its `alpha<=4`, `omega<=11`, `delta>=12`. The pure classes have sizes5,7,8,8. Row1 is A. Singleton carriers `u,v` have full row s and `w` has full row C. The four distinct double overlaps have no partial edges. The three singleton carriers each have one partial edge, to distinct vertices of T_A. H has153 edges and total nonnegative excess sum `epsilon=6`, with `epsilon=d_C-12`.

## S1. Incidence consequences — PROVED

Pure classes are cliques and complete to their singleton-full-row carriers. Counts force the simple double-row graph `{sA,sB,sC,BC}`. Write `t=X_BC`.

The edge `uv` is forced. The edges `uw,vw` are NOT assumed. Let `k=1_uw+1_vw`. Up to u-v symmetry, the configurations are `k=0`, `k=1` with `uw` present, and `k=2`.

## S2. Nonduplicating local accounting — PROVED

Let `A_t` be the nonneighbours of t in `P_C`, size `a`, and `B_t` those in `P_B`, size `b`. Then `0<=a<=7`, `1<=b<=8`. The pair `A_t,B_t` is completely joined.

On disjoint vertex sets:

    epsilon_t >= (9-a-b)_+
    sum_(A_t) epsilon >= a(b-2)_+
    sum_(B_t) epsilon >= b(a-2)_+

Let `h_t` count t's H-neighbours outside `P_C union P_B`; then `epsilon_t=9-a-b+h_t`. Let `h_w` count w's neighbours outside `P_C` and its k adjacent members of `{u,v}`. Then

    epsilon_w=k-1+h_w>=0.

Hence the necessary inequality is

    L(a,b)+max(0,k-1)<=6,
    L(a,b)=(9-a-b)_+ + a(b-2)_+ + b(a-2)_+.

## S3. Exact scalar cases before new closures — PROVED

For `k=2`, the six possibilities are `a=0,b=4..8` and `(a,b)=(2,2)`. They are analytically excluded by the included singleton-triangle proof.

For `k=0` or `1`, the 22 possibilities satisfying `L<=6` are:

|a|b|
|---:|---|
|0|3,4,5,6,7,8|
|1|2,3,4,5,6,7,8|
|2|1,2,3|
|3|1,2|
|4,5,6,7|1|

These are scalar necessary cases, not liftable graph families.

## S4. Saturation lemma — PROVED

Suppose `L=6` and `a>=2`. The eight pairs are

    (2,1),(2,3),(3,1),(3,2),(4,1),(5,1),(6,1),(7,1).

The disjoint lower bounds use all six excess units. Hence `epsilon_w=0`, all `x,y,z` have epsilon0, and `h_t=0`. Every beta in `B_t` has `epsilon_beta=a-2`, with its full H-neighbourhood saturated. Choosing a special r nonadjacent to w, then beta, then a suitable alpha in P_A produces an independent5, contradiction.

This removes the eight cases for EACH of `k=0,1` and does not use the singleton-triangle assumption.

## S5. Compatibility lemma for k=1,a=0 — PROVED

Assume `uw` is an edge and `vw` is not. Then t is complete to P_C and `tw` is forbidden by K12. Exact accounting gives

    h_t+h_w+sum_(r notin {t,w}) epsilon_r=b-3.

Then `tv` is forced. Otherwise t,w,v are pairwise nonadjacent and the budget above leaves enough regular vertices in `P_A` and `B_t` to build an independent5.

For `b=3` the right side is zero but `h_t>=1`, contradiction. Thus `(k,a,b)=(1,0,3)` is removed. For `b=4..8`, the compulsory `tv` edge consumes one unit of `h_t` and must be retained in any exact completion.

## S6. Exact remaining list — OPEN

|singleton edges|remaining (a,b)|additional exact condition|
|---|---|---|
|uv only (k0)|a0,b3..8; a1,b2..8; (2,2)|w has at least one outside-P_C neighbour; epsilon_w=h_w-1|
|uv,uw only (k1)|a0,b4..8; a1,b2..8; (2,2)|if a0, tv is compulsory; epsilon_w=h_w|
|uv,uw,vw (k2)|none|analytic closure|

There are 14 and 13 scalar cases in the two remaining rows. This is NOT a classification of full incidence types, a proof of realizability, or a counterexample.

The first unproved line for a wholesale application of the old labelled closure remains: `uw and vw are both forced`. S4/S5 bypass part of this assertion but do not establish it.

## S7. Relation to global bridge — OPEN

Even a full closure of this labelled profile would not prove that all T61 states enter this S30 configuration. The T61-to-S30 coverage theorem is independently missing.