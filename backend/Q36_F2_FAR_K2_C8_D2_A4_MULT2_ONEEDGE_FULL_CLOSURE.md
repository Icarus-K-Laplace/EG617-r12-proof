# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated one-edge multiplicity-two closure

Status: `PROVED` under the far-K2 c8 one-d2 A4 contract, common-S row closure, inherited D14, q36 lexicographic maximality, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the already proved elimination of support multiplicity at least3.

This eliminates every multiplicity-two support with exactly one internal target edge.

## 1. Setup

Let D={a,b,c} be a support of owner multiplicity2 with the unique internal target edge ab; c is isolated in H[D].

Write

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Since D repeats, full defect4 is forbidden by q36 lexicographic maximality. Here `m(D)=2`, so

`Delta(D)=2+w(D)<=3`,

hence

> `w(D)<=1`.                                                 (1)

Let D0 be the unique pure d2 support and fix `v0 in D0`. The d2 contract makes v0 target-anticomplete to U and S, and `alpha(H[U])<=2`.

## 2. Exact one-edge normal form

If `w(D)=0`, choose either internal target-nonedge, say ac. Both a and c are target-anticomplete to S. For any far point f,

`{a,c,v0,x,f}`

is an independent5-set, contradiction.

Thus `w(D)=1`.

The unique positive unit cannot lie on a or b: if, say, a is positive, then the other internal nonedge bc has both endpoints of weight0 and again gives the independent5-set `{b,c,v0,x,f}`.

Therefore the positive unit lies on c.

If it were pure core excess, c would still be target-anticomplete to S and the same independent5 argument would apply. If it were a single far edge cf1, then using the other far point f2 the set `{a,c,v0,x,f2}` would be independent.

Hence the only possible state is

> `w_c=1`, `w_a=w_b=0`, `kappa(D)=0`, and cx is a target edge.   (2)

In particular D has no far target edge.

## 3. No external support can be disjoint from D

Let E be a support disjoint from D and e any point of E.

Because ac and bc are target-nonedges and `alpha(H[U])<=2`, e must meet both pairs. But a and b have weight0. Row closure against support E gives

`e_H(a,E)<=w_a=0`, `e_H(b,E)<=w_b=0`.

Thus every e in E must be target-adjacent to c.

Hence `e_H(c,E)=3`, contradicting row closure

`e_H(c,E)<=w_c=1`.

Therefore every one of the five external owner incidences belongs to a support intersecting D.   (3)

## 4. Only two overlap types survive

Consider a distinct support E intersecting D.

- If E contains a but not b, then b lies outside E and the target edge ba gives `e_H(b,E)>=1`, contradicting `w_b=0`.
- Symmetrically, E cannot contain b but not a.
- If E contains {a,c} but not b, the same b--a edge contradicts row closure at b.
- Symmetrically, E cannot contain {b,c} without a.

Since E is distinct from D, the only possible intersections are therefore

> `{c}` or `{a,b}`.                                          (4)

Let n_c and n_ab be the numbers of external owner incidences of these two types. Then

`n_c+n_ab=5`,
`O_D=n_c+2n_ab=5+n_ab`.

D14 for the multiplicity-two one-edge support D gives

`6+O_D+e_F(F,D)+e_H(D)<=14`.

Using `e_F(F,D)=0` and `e_H(D)=1` from (2),

`O_D<=7`,

so

> `n_ab<=2`, hence `n_c>=3`.                                 (5)

## 5. There is at most one c-only support class

Let E={c,u,v} be a c-only support.

Because a has weight0 and lies outside E, row closure gives

`e_H(a,E)=0`.

Thus a is target-nonadjacent to c,u,v. Since ac is already a nonedge and `alpha(H[U])<=2`, both cu and cv must be target edges; otherwise `{a,c,u}` or `{a,c,v}` is an independent triple. The same conclusion follows using b.

Now suppose E1={c,u1,v1} and E2={c,u2,v2} are two distinct c-only support classes.

The point a is target-anticomplete to all four petals. Therefore, to avoid an independent triple `{a,p1,p2}`, every petal of E1 must be target-adjacent to every petal of E2. Hence the petal-to-petal cross graph is K2,2.

Fix a petal u1 of E1. It is already target-adjacent to c, and c belongs to support E2. Together with the two forced petal-cross edges,

`e_H(u1,E2)>=3`.

Row closure against E2 gives `w_u1>=3`. The same holds for v1.

But E1 also contains c with `w_c=1`, so

`Delta(E1)>=w_c+w_u1+w_v1>=7>A=4`,

contradiction.

Therefore

> at most one distinct c-only support class exists.           (6)

## 6. Owner-capacity contradiction

By (5), at least three external owner incidences are c-only. By (6), all of them would have to use the same support class.

That class would have owner multiplicity at least3, but all support multiplicities at least3 have already been eliminated in the A4 high-multiplicity closure chain.

Contradiction.

Therefore

> no repeated one-edge multiplicity-two support exists in the far-K2 c8 one-d2 A4 layer.