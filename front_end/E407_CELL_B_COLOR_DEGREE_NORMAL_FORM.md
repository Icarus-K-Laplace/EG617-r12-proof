# E407 Cell-B color-degree normal form

Status: **PROVED_RELATIVE_TO_BROUWER/KANG-PIKHURKO EXTREMAL THEOREMS** and the already-proved E407 Cell-B target-degree20 normal form.

## 1. A 131-edge non-target color has minimum degree at least3

Let C be a non-target color graph on61 vertices with

- alpha(C)<=12,
- omega(C)<=5,
- e(C)=131.

Suppose d_C(v)=2. Let N be the 58 non-neighbours of v and P=N_C(v), |P|=2.

Because v is nonadjacent to all of N, alpha(C[N])<=11. Also omega(C[N])<=5.

Since 58>11*5, the complement of C[N] is K12-free and non-11-partite. Brouwer's second-Turan theorem gives

 e(C[N])>=p_11(58)+floor(58/11)-1.

Now p_11(58)=125 and floor(58/11)=5, hence

 e(C[N])>=129.

Since v already contributes two incident edges, e(C)>=131. Equality would force

- e(C[N])=129;
- no edges inside P;
- no edges from P to N.

But alpha(C[N]) must then equal11 (alpha<=10 would require strictly more edges under the same omega<=5 constraint), and an independent11-set in N together with the two independent isolated points of P gives an independent13-set in C, contradiction.

Thus d_C(v) cannot be2. Degrees0,1 are even easier. Therefore

> **delta(C)>=3 whenever e(C)=131.**

## 2. Degree3 in a 130-edge color forces an isolated K4

Let C satisfy the same alpha/omega constraints and e(C)=130. Suppose d_C(v)=3 and put

P=N_C(v), |P|=3,
N=V(C)\(P union {v}), |N|=57.

Again alpha(C[N])<=11 and omega(C[N])<=5. Brouwer gives

 e(C[N])>=p_11(57)+floor(57/11)-1=120+4=124.

Write

 delta_N=e(C[N])-124>=0.

The full edge count is

130 = 3 + e(C[N]) + e(C[P]) + e_C(P,N),

so

> delta_N + e(C[P]) + e_C(P,N) = 3.   (1)

Assume P is not a triangle. Choose a nonadjacent pair p,q in P with the union of their N-neighbourhoods of size at most2. Such a pair always exists from (1):

- if e(P)=2 then e(P,N)<=1;
- if e(P)=1 then e(P,N)<=2;
- if e(P)=0 then among the three pairs one sees at most two of the at-most3 P--N incidences.

Delete those at-most2 N-neighbours of p,q. The remaining graph N' has at least55 vertices, omega<=5, and at most127 edges.

If alpha(N')<=10, then because |N'|>=55>10*5, Brouwer's second-Turan bound in the 10-partite problem gives at least129 edges already at order55, and more for larger order. Contradiction.

Hence alpha(N')>=11. Take an independent11-set I in N'. Then

 I union {p,q}

is an independent13-set in C, contradiction.

Therefore P is a triangle. Then e(P)=3, and (1) forces

 delta_N=0,
 e(P,N)=0.

Thus

> **v union P is an isolated K4 component of C,**
>
> and the remaining57 vertices form an exact 124-edge constrained second-Turan extremizer.

## 3. Apply to the E407 Cell-B subdivision vertex

In the E407 sharp Cell-B target normal form, the subdivision vertex w has target degree exactly20. Therefore the sum of its degrees in the eleven non-target colors is

60-20=40.

The total non-target edge excess above the 129-edge constrained minimum is

411-407=4.

Let s_j=e(C_j)-129. Then sum s_j=4.

The pointwise degree floors at w are now

- s=0: degree>=4;
- s=1: degree>=3;
- s=2: degree>=3 by Section1;
- s>=3 in the present s<=4 range: degree>=2.

Checking the five partitions of4 shows that the only way the eleven pointwise degrees can sum to40 is

> **4=1+1+1+1.**

Hence exactly

> **seven non-target colors have129 edges,**
>
> **four non-target colors have130 edges.**

Moreover w has degree4 in every 129-edge color and degree3 in every 130-edge color.

By Section2, each of the four 130-edge colors contains an isolated K4

> `w union T_i`,  |T_i|=3,

and the four triples T_i are pairwise disjoint because the edges incident to w have unique colors.

## 4. The special Cell-B P3 color is exact129

Inside W, the Cell-B factorization has one special color in which the subdivided edge xy is replaced by the path

x--w--y.

Thus w has the two W-neighbours x,y in the special color, but xy is not an edge of that color.

If the special color were one of the four 130-edge colors, w would have total degree3 and Section2 would force its three neighbours to form a triangle. This is impossible because x and y are not adjacent in the special color.

Therefore

> **the special Cell-B color is one of the seven exact129 colors.**

It has total degree4 at w, so besides x,y it has exactly two neighbours in O.

The other six exact129 colors are ordinary Cell-B matching colors; w has no W-neighbour in them, so all four of their w-neighbours lie in O.

The four 130-edge colors are also ordinary colors; all three of their w-neighbours lie in O and form the isolated triangles T_i.

Therefore the 38 vertices of O are partitioned exactly as

> **2 + 6*4 + 4*3 = 38**

according to the non-target color of their edge to w.

## 5. Final exact color-side normal form

Any E407 sharp Cell-B completion must satisfy simultaneously:

1. seven exact129 non-target colors;
2. four 130-edge non-target colors;
3. the special P3 color belongs to the exact129 class;
4. four pairwise disjoint triples T_1,...,T_4 in O, each a monochromatic triangle in its own 130-edge color;
5. each `w union T_i` is an isolated K4 in that color;
6. the 38 O-vertices split into w-colour classes of sizes

   `2,4,4,4,4,4,4,3,3,3,3`.

This color-side decomposition should be intersected with `E407_CELL_B_INDEPENDENT4_SATURATION.md`, which gives the independent-4 target-side 4x3 orientation rule.
