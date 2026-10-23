# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated two-edge multiplicity-two reduction

Status: `PROVED REDUCTION` under the far-K2 c8 one-d2 A4 contract, common-S row closure, inherited D14, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the already proved elimination of support multiplicity at least3.

This does not yet close the repeated two-edge multiplicity-two sector. It reduces it to a small endpoint-anchored overlap terminal.

## 1. Setup

Let D={a,b,c} be a multiplicity-two support with target edges ac,bc and unique target nonedge ab. Thus c is the path center.

Write

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Because D repeats, full defect4 is forbidden. Since `m(D)=1`,

`Delta(D)=1+w(D)<=3`,

so

> `w(D)<=2`.                                                 (1)

Let D0 be the unique pure d2 support and choose `v0 in D0`; the d2 contract gives `alpha(H[U])<=2` and makes v0 target-anticomplete to U and S.

If `w(D)=0`, then a,b are target-anticomplete to S and

`{a,b,v0,x,f}`

is an independent5-set for any far point f. Hence

> `1<=w(D)<=2`.                                              (2)

## 2. No external support can be disjoint from D

Let E be a support disjoint from D.

Since ab is a target nonedge and `alpha(H[U])<=2`, every vertex of E must be target-adjacent to a or b. Therefore

`e_H(D,E)>=3`.                                               (3)

For two disjoint common-S supports, joint row closure bounds their target cross edges by the non-missing allowance of D, which here is `w(D)<=2`. Thus

`e_H(D,E)<=w(D)<=2`,

contradicting (3).

Therefore every one of the five external owner incidences belongs to a support intersecting D.   (4)

## 3. D14 leaves at most one two-point owner

Let `O_D` be the weighted external owner-overlap with D. Since all five external owners intersect D,

`O_D>=5`.

D14 for the multiplicity-two two-edge support gives

`6+O_D+e_F(F,D)+2<=14`,

hence

> `O_D+e_F(F,D)<=6`.                                        (5)

Therefore

> `O_D in {5,6}`.                                            (6)

Because each distinct external support intersects D in one or two points, write n2 for the number of external owner incidences with two-point overlap. Then

`O_D=5+n2`.

Thus

> `n2<=1`.                                                    (7)

So at least four of the five external owner incidences are one-point overlaps.

If `O_D=6`, equation (5) additionally forces `e_F(F,D)=0`.

## 4. One-point anchors are controlled by the weight pattern

Consider a support E whose intersection with D is exactly one point.

### Anchor a

If `E intersect D={a}`, then c lies outside E but ca is a target edge. Row closure against E gives

`1<=e_H(c,E)<=w_c`.

Hence

> an a-anchor requires `w_c>=1`.                             (8)

The same argument shows that a b-anchor requires `w_c>=1`.

### Anchor c

If `E intersect D={c}`, then both a and b lie outside E, while ac and bc are target edges. Therefore row closure gives

`w_a>=1`, `w_b>=1`.                                         (9)

## 5. The case w_c=0 is impossible

Assume `w_c=0`.

By (8), no one-point support can be anchored at a or b. Since at least four one-point owner incidences exist, a c-anchor must exist. Equation (9), together with `w(D)<=2`, forces the exact pattern

`(w_a,w_b,w_c)=(1,1,0)`.                                   (10)

Let E={c,u,v} be any c-anchor support.

Since a lies outside E and `w_a=1`, the existing edge ac already consumes its full row-closure budget:

`e_H(a,E)<=1`.

Thus a is target-anticomplete to u and v. Similarly b is target-anticomplete to u and v.

But ab is a target nonedge. Hence `{a,b,u}` is an independent triple in U, contradicting `alpha(H[U])<=2`.

Therefore

> `w_c>=1`.                                                  (11)

## 6. Final reduced terminal

Since `w_c>=1` and `w(D)<=2`, equation (9) shows that no one-point c-anchor can exist: it would require `w_a,w_b,w_c>=1`, total at least3.

Consequently every one-point overlap is anchored at one of the two endpoints a,b.

Combining Sections 3--5, every surviving repeated two-edge multiplicity-two state satisfies:

- `1<=w(D)<=2` and `w_c>=1`;
- all five external owners intersect D;
- at least four external owner incidences are one-point overlaps;
- every one-point overlap is anchored at a or b;
- at most one external owner has two-point overlap;
- `O_D in {5,6}`; if `O_D=6`, then `e_F(F,D)=0`.

Thus the remaining problem is a finite endpoint-anchored owner-capacity terminal. No closure beyond this reduction is claimed here.