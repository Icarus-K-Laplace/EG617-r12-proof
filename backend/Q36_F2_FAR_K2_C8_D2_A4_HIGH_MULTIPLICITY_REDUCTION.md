# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 high-multiplicity reduction

Status: `PROVED REDUCTION` under the far-K2 c8 one-d2 contract, common-S row closure, inherited D14, CORE211, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, and the pure-d2 support contract.

This eliminates multiplicity4 and every multiplicity-three nonclique support. A multiplicity-three K3 is forced into the exact unit-weight state `(1,1,1)`.

## 1. Setup

All seven d3 owners share one missing set

`S=F union {x}`

with allowance A=4. Let D0 be the unique d2 support; D0 is a pure target K2, globally regular, and target-anticomplete to S and to the d3-support union U. Hence

`alpha(H[U])<=2`.

Write

`w_v=kappa_v+e_F(v,S)`.

For every d3 support E,

`Delta(E)=m(E)+sum_(v in E)w_v<=4`.

If E repeats, full defect4 would repivot to q36 while retaining the two inactive decorated shell vertices and inserting several globally decorated support vertices. Thus

> every repeated support has `Delta<=3`.                     (1)

## 2. Multiplicity four is impossible

Let D have owner multiplicity4. D14 gives

`12+O_D+e_F(F,D)+e_H(D)<=14`.                              (2)

A support in U cannot be an independent triple, so `e_H(D)>=1`.

- If `e_H(D)=1`, then `m(D)=2` and (1) gives non-missing allowance at most1. A disjoint support would require at least3 D-cross edges to cover the two internal nonedges of D, impossible. Hence all three outside owners intersect D, so `O_D>=3`, while (2) gives `O_D+e_F(F,D)<=1`, contradiction.
- If `e_H(D)=2`, then the non-missing allowance is at most2. A disjoint support must send at least3 edges into the unique internal nonedge, again impossible. But (2) forces `O_D=e_F(F,D)=0`, so all three outside owners would have to be disjoint. Contradiction.
- If `e_H(D)=3`, then `12+3>14` immediately.

Therefore

> multiplicity4 is EMPTY.                                   (3)

## 3. Multiplicity-three one-edge supports are impossible

Let D have multiplicity3 and exactly one internal target edge. Write D={a,b,c} with sole edge ab, so c is isolated in H[D].

D14 gives

`9+O_D+e_F(F,D)+1<=14`,

hence

`O_D+e_F(F,D)<=4`.                                         (4)

Because `m(D)=2`, (1) gives `w(D)<=1`. A support disjoint from D would require at least three target D-cross edges: each of its vertices must cover both internal nonedges ac and bc, while the non-missing cross allowance of D is at most1. Hence all four external owner incidences intersect D.

Thus `O_D>=4`; (4) forces

> `O_D=4`, `e_F(F,D)=0`, and every external owner support meets D in exactly one point.    (5)

If `w(D)=0`, any internal nonedge together with one point of D0, x and one far point gives an independent5-set. Hence `w(D)=1`.

To avoid such an independent5 on both nonedges ac and bc, the unique positive unit must lie on c, the common endpoint of the two nonedges, and it must be a genuine S-adjacency rather than pure core excess. Therefore

> `w_c=1`, `w_a=w_b=0`, `kappa(D)=0`, and c has exactly one target neighbour in S.  (6)

Now fix an external support E. Every point of `E\D` must cover both nonedges ac and bc, so every outside point has weight at least1.

The shared D-point is globally decorated, and every positive-weight outside point is globally decorated as well. Hence E cannot use full defect4: a q36 repivot would retain two inactive decorated shell vertices and insert three decorated core vertices. Therefore

`Delta(E)<=3`.                                               (7)

If E met D at a or b, its two outside vertices would each have weight at least1. With shared weight0, (7) forces `m(E)<=1`. A direct two-edge/K3 check shows this is impossible: any outside vertex adjacent to a (or b) still needs a second D-edge to cover the other nonedge, making the total weight plus missing count at least4.

Thus every external support meets D at c. Then the two outside vertices each have weight at least1; together with `w_c=1`, (7) forces

> E is a target K3, both petals have weight1, and each petal has no D-neighbour other than c.   (8)

Two distinct support classes of form (8) are impossible. A petal of one already spends its full weight1 on c, so row closure against the other support makes the two petal pairs target-anticomplete. Since a is target-nonadjacent to c and to every petal, one petal from each class together with a forms an independent triple in U.

Hence all four external owner incidences would have to use one support class, giving multiplicity4, already excluded by (3).

Therefore

> multiplicity-three one-edge supports are EMPTY.            (9)

## 4. Multiplicity-three two-edge supports are impossible

Let D have exactly two target edges. Then `m(D)=1` and repeated defect at most3 gives non-missing allowance at most2.

D14 yields

`9+O_D+e_F(F,D)+2<=14`,

so

`O_D+e_F(F,D)<=3`.                                         (10)

A support disjoint from D must cover the unique internal nonedge from each of its three vertices, requiring at least3 D-cross edges, while D allows at most2. Hence no disjoint support exists. All four external owners intersect D, so `O_D>=4`, contradicting (10).

Thus multiplicity-three two-edge supports are EMPTY.         (11)

## 5. Multiplicity-three K3: defect must be exactly three

Let D be a multiplicity-three target K3. Then (1) gives

`w(D)<=3`,                                                   (12)

and D14 gives

> `O_D+e_F(F,D)<=2`.                                        (13)

Hence at least two of the four external owner incidences belong to supports disjoint from D.

We prove that D cannot contain a zero-weight point.

Assume `d0 in D` has `w_d0=0`, and let E be any support disjoint from D.

Row closure against E gives

`e_H(d0,E)<=w_d0=0`,

so d0 is target-anticomplete to E.

If E were nonclique, an internal target nonedge of E together with d0 would be an independent triple in U, contradicting `alpha(H[U])<=2`. Therefore E is a target K3.

Now fix `e in E`. If e were target-nonadjacent to x and to some far point f, then

`{d0,e,v0,x,f}`

with `v0 in D0` would be an independent5-set: d0 is anticomplete to E and S, D0 is anticomplete to U and S, and xf is a nonedge because `a_F=0`.

Thus every e in E must satisfy:

- either ex is a target edge,
- or e is target-adjacent to both far vertices.

Because E is a K3, x can be adjacent to at most two vertices of E without forming a K4. Hence at least one E-vertex must use both far edges. Therefore

`e_F(S,E)>=4`.                                               (14)

Since E is a K3, its defect is at least4. The A=4 allowance forces equality: E has full defect4 and repivots to q36. Moreover every E-vertex has at least one S-neighbour, so all three are globally decorated. Its q36 repivot retains the two inactive decorated shell vertices and inserts three decorated support vertices, increasing tau, contradiction.

Therefore no support can be disjoint from a zero-weight D-point. But (13) requires at least two disjoint owner incidences. Contradiction.

Hence every vertex of D has positive integer weight. Together with (12), this forces the exact state

> `w(D)=(1,1,1)`.                                           (15)

In particular D has defect exactly3 and repivots to q35.

## 6. Current A=4 high-multiplicity frontier

All support multiplicities are at most3. Every multiplicity-three support is forced into the unique terminal

- D is a target K3;
- D has owner multiplicity3;
- its three support weights are exactly `(1,1,1)`;
- `O_D+e_F(F,D)<=2`, so at least two of the four external owner incidences are disjoint from D.

The next task is to close this unit-weight repeated-K3 terminal, then treat multiplicity at most2.