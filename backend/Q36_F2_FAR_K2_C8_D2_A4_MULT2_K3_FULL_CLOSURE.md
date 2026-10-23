# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated K3 multiplicity-two full closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A4_MULT2_K3_LOWWEIGHT_CLOSURE.md`, the far-K2 c8 one-d2 A4 contract, common-S row closure, inherited D14, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the already proved elimination of support multiplicity at least3.

The low-weight closure already eliminates all repeated K3 multiplicity-two states with total weight at most2. This file eliminates the three remaining total-weight-three patterns and therefore closes the entire repeated-K3 multiplicity-two sector.

## 1. Setup

Let D be a target K3 support of owner multiplicity2. Write

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Since D repeats, full defect4 is forbidden, so `w(D)<=3`. The previous file proves `w(D)=3` in every surviving state.

D14 gives

`O_D+e_F(F,D)<=5`.                                         (1)

The remaining weight patterns, up to permutation, are

- `(3,0,0)`;
- `(2,1,0)`;
- `(1,1,1)`.

Let D0 be the unique pure d2 support and `v0 in D0`.

## 2. Pattern (3,0,0) is impossible

Write `(w_a,w_b,w_c)=(3,0,0)`.

### Intersecting owners

No one-point overlap is possible: whichever D-point is shared, one of the zero-weight points lies outside the other support and is adjacent to the shared point because D is a K3.

A two-point overlap can only contain the two zero-weight points {b,c}. Any pair containing a leaves a zero-weight point outside and violates row closure.

Thus each intersecting owner contributes exactly2 to O_D. Equation (1) implies that at most two external owners intersect D. Hence at least three external owners are disjoint from D.   (2)

### Disjoint owners

Zero-weight b is target-anticomplete to every support disjoint from D. Hence every such support must be a K3; otherwise b together with an internal target nonedge would be an independent triple in U.

Moreover b is anticomplete to the union of all disjoint supports. Therefore this union must be a target clique: any target nonedge uv would give the independent triple {b,u,v}.

Two distinct support classes would then produce a K4. Thus at most one disjoint support class exists, of owner multiplicity at most2.

This contradicts (2). Hence `(3,0,0)` is empty.              (3)

## 3. Pattern (1,1,1) is impossible

Assume all three D-points have weight1.

### 3.1 Every disjoint support is a unit-weight K3

Let E be disjoint from D and suppose e in E has `w_e=0`.

Row closure against D makes e target-anticomplete to D and `w_e=0` makes e anticomplete to S. If some d in D were target-nonadjacent to x, then since `w_d=1` it misses at least one far point f, and

`{d,e,v0,x,f}`

would be an independent5-set. Therefore every d would have to be adjacent to x, making `D union {x}` a K4. Contradiction.

Thus every vertex of every support disjoint from D has positive weight.

A one-edge support then has defect at least5 and is impossible. A two-edge support has defect at least4; if repeated, full defect4 is forbidden, while if singleton its q36 repivot inserts three positive-weight decorated vertices and retains the two inactive decorated shell vertices, increasing tau. Hence it is impossible as well.

A disjoint K3 must therefore have total weight exactly3: weight at least4 gives the same repeated/full-q36 contradiction. Consequently

> every support disjoint from D is a unit-weight K3.          (4)

### 3.2 At most one disjoint support class exists

Let E,E' be two distinct disjoint-from-D support classes. By (4), both are unit-weight K3s.

- If they intersect in two points, write `E=P union {u}`, `E'=P union {v}`. K4-freeness forces uv to be a target nonedge. Each of u,v has at most one D-neighbour by row closure, so some d in D is nonadjacent to both, giving independent triple {d,u,v}.
- If they intersect in one point p, the private two-point parts are target-anticomplete: each private point is already adjacent to p and row closure allows only one edge into the other support. Choosing one private point from each side, their D-neighbour sets have union size at most2, so some d in D completes an independent triple.
- If they are disjoint, row closure gives at most one cross edge incident to each point, hence at most3 target cross edges total. Choose a target-nonedge pair u in E, v in E'; each has at most one D-neighbour, so some d in D is nonadjacent to both.

Thus two distinct disjoint support classes cannot coexist. Hence disjoint owner capacity is at most2.   (5)

### 3.3 Intersecting owner capacity is at most two

A two-point overlap with D is impossible: the excluded D-point has weight1 but is adjacent to both shared D-points, requiring row-closure budget2.

Thus every proper overlap is one-point.

Fix an anchor d in D. Suppose two distinct support classes E1={d,u1,v1}, E2={d,u2,v2} share that anchor.

The other two D-points each have weight1 and their edge to d already consumes the full row-closure budget, so they are target-anticomplete to all four petals. Therefore every petal of E1 must be target-adjacent to every petal of E2; otherwise one of the other D-points with a target-nonedge petal pair gives an independent triple.

Hence each petal has at least two target edges into the other support, so its weight is at least2. Each support also contains the shared D-point of weight1, yielding defect at least5, impossible. Thus at most one support class exists at a fixed anchor.

Now suppose classes anchored at two different D-points coexist. The third D-point has weight1 and is target-adjacent to each anchor, so row closure makes it target-anticomplete to all petals of both classes. The same petal-cross argument forces a complete K2,2 cross graph and again defect at least5.

Therefore all intersecting owners occupy at most one support class, of multiplicity at most2. Intersecting owner capacity is at most2.   (6)

By (5)--(6), the five external owners have total capacity at most4. Contradiction.

Thus `(1,1,1)` is empty.                                    (7)

## 4. Pattern (2,1,0) is impossible

Write `(w_a,w_b,w_c)=(2,1,0)`.

### 4.1 Disjoint capacity

Zero-weight c is target-anticomplete to every support disjoint from D. Hence every disjoint support is a K3 and the union of all disjoint supports must be a target clique, or c together with a target nonedge in that union would be an independent triple.

Therefore at most one distinct disjoint support class exists, carrying at most2 owners. Let d be the number of disjoint owner incidences; then

`d<=2`.                                                       (8)

### 4.2 Allowed overlap types

A one-point overlap at a or b is impossible because zero-weight c lies outside and is adjacent to the shared point.

A two-point overlap containing a,b is impossible because c lies outside with weight0 and sees both shared points. A two-point overlap containing a,c is impossible because the excluded point b has weight1 but sees two shared target edges.

Thus the only overlap types are

- a one-point overlap at c;
- a two-point overlap on {b,c}.                              (9)

Let n1,n2 be their owner counts. Then

`n1+n2+d=5`,
`O_D=n1+2n2`.

By (1), `O_D<=5`, hence

`n2<=d`.                                                      (10)

### 4.3 c-anchor capacity

Two distinct one-point c-anchor support classes cannot coexist.

Indeed, for a c-anchor support, b lies outside with weight1 and its edge to c consumes its full row-closure budget, so b is target-anticomplete to both private petals. If two distinct c-anchor classes existed, every petal-cross pair would have to be a target edge to avoid an independent triple with b. Thus every petal has at least two target edges into the other support and hence weight at least2.

A support with two such petals has defect at least4. If it is nonclique the defect exceeds4; if it is a K3, equality gives a q36 repivot whose shared c-point is globally decorated by D and whose positive-weight petals are decorated, while the two inactive decorated shell points remain. Tau increases. Contradiction.

Therefore

`n1<=2`                                                        (11)

because the unique c-anchor class has multiplicity at most2.

### 4.4 Counting forces a repeated disjoint unit K3

If d=0, then (10) gives n2=0 and n1=5, contradicting (11).

If d=1, then n2<=1 and therefore `n1=4-n2>=3`, again contradicting (11).

Hence

> `d=2`.                                                      (12)

By (8), the two disjoint owners use the unique disjoint support class E, so E has multiplicity2.

Since c has weight0 and is anticomplete to E, E must be a K3. No point e in E can have weight0: otherwise c,e,v0,x,f would form an independent5-set for any far point f. Therefore all three E-points have positive weight.

Because E repeats, full defect4 is forbidden. Thus its K3 weight sum is at most3, forcing

`w(E)=(1,1,1)`.

But Section3 has just proved that the repeated-K3 multiplicity-two pattern `(1,1,1)` is impossible.

Contradiction. Hence `(2,1,0)` is empty.                     (13)

## 5. Conclusion

All total-weight-three patterns are impossible. Combined with `Q36_F2_FAR_K2_C8_D2_A4_MULT2_K3_LOWWEIGHT_CLOSURE.md`, this proves:

> no repeated target-K3 support of multiplicity2 exists in the far-K2 c8 one-d2 A4 layer.

Together with the repeated one-edge closure, the only repeated multiplicity-two geometry still open is the repeated two-edge endpoint-anchored terminal from `Q36_F2_FAR_K2_C8_D2_A4_MULT2_TWOEDGE_REDUCTION.md`.