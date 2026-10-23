# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated K3 multiplicity-two low-weight closure

Status: `PROVED` under the far-K2 c8 one-d2 A4 contract, common-S row closure, inherited D14, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the already proved elimination of support multiplicity at least3.

This proves that every repeated target-K3 support of multiplicity2 must have total common-S weight exactly3. Equivalently all weight patterns of total weight0,1,2 are empty.

## 1. Setup

Let D be a target K3 support of owner multiplicity2. Write

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Since D repeats, full defect4 is forbidden. Because D is a K3,

`Delta(D)=w(D)<=3`.                                         (1)

D14 gives

`6+O_D+e_F(F,D)+3<=14`,

hence

> `O_D+e_F(F,D)<=5`.                                        (2)

Let D0 be the unique pure d2 support and choose `v0 in D0`. The pure-d2 contract makes v0 target-anticomplete to U and S, and implies `alpha(H[U])<=2`.

A recurring observation is:

> if z in D has `w_z=0` and E is disjoint from D, then row closure gives `e_H(z,E)=0`.   (3)

Thus z is target-anticomplete to every support disjoint from D.

## 2. Weight zero is impossible

Assume `w(D)=0`.

Let E be any support disjoint from D. If E contained an internal target nonedge uv, then any z in D together with u,v would be an independent triple, contradicting `alpha(H[U])<=2`. Hence every disjoint support is a target K3.

By (3), any fixed z in D is target-anticomplete to the union of all supports disjoint from D. Therefore that union must itself be a target clique: any target nonedge uv in it would give the independent triple {z,u,v}.

Two distinct support classes would have union of size at least4, producing a K4. Thus there is at most one disjoint support class, of owner multiplicity at most2.

Intersecting supports are impossible as well: any proper intersection leaves some zero-weight point of the target K3 D outside the other support while still adjacent to a shared D-point, violating row closure.

Hence at most2 of the five external owner incidences can be realized, contradiction.

Therefore `w(D)!=0`.                                        (4)

## 3. Total weight one is impossible

Up to relabelling, let

`(w_a,w_b,w_c)=(1,0,0)`.

No distinct support can intersect D:

- a one-point overlap leaves at least one zero-weight D-point outside the support, and that point is adjacent to the shared D-point because D is a K3;
- a two-point overlap either leaves a zero-weight point outside, or leaves a outside, which has weight1 but is adjacent to both shared D-points, requiring row-closure budget2>1.

Thus all five external owner incidences are disjoint from D.

Any disjoint support is a K3 by the same zero-weight argument as Section2. The zero-weight point b is anticomplete to every such support, so the union of all disjoint supports must be a target clique. Hence there is at most one distinct disjoint support class, of multiplicity at most2.

Five owners cannot be carried. Contradiction.

Therefore `w(D)!=1`.                                        (5)

## 4. Pattern (2,0,0) is impossible

Let

`(w_a,w_b,w_c)=(2,0,0)`.

### Overlap capacity

No one-point overlap is possible: whichever D-point is shared, one of the zero-weight points lies outside the support and is adjacent to the shared point.

A two-point overlap can only contain the two zero-weight points {b,c}. Any pair containing a leaves a zero-weight point outside and violates row closure.

Thus every intersecting external owner contributes exactly2 to O_D. By (2), at most two external owners can intersect D.

Hence at least three external owners are disjoint from D.              (6)

### Disjoint capacity

Every disjoint support is a K3 because b is zero-weight and anticomplete to it; any internal target nonedge would make an independent triple with b.

Moreover b is anticomplete to the union of all disjoint supports. Therefore, as in Section2, two distinct disjoint support classes would force their union to be a target clique and hence contain a K4.

So there is at most one disjoint support class, carrying at most2 owners, contradicting (6).

Thus `(2,0,0)` is impossible.                                (7)

## 5. Pattern (1,1,0) is impossible

Let

`(w_a,w_b,w_c)=(1,1,0)`.

### Allowed overlap type

A one-point overlap at a or b is impossible because zero-weight c lies outside the support but is adjacent to the shared point.

A two-point overlap is impossible:

- if it contains a,b, zero-weight c lies outside and sees two target edges;
- if it contains a,c, the excluded point b has weight1 but sees both included D-points;
- similarly for b,c.

Hence the only possible proper overlap is a one-point support anchored at c.   (8)

### At most one c-anchor support class

Let E1={c,u1,v1} and E2={c,u2,v2} be two distinct c-anchor classes.

For E1, point a lies outside with weight1 and is already adjacent to c, so row closure forces a to be target-anticomplete to u1,v1. The same holds for b, and likewise for the petals of E2.

If any petal of E1 were target-nonadjacent to any petal of E2, that pair together with a would be an independent triple. Therefore all four petal-to-petal cross edges are present.

Fix u1. Row closure against E2 sees at least the two forced petal cross edges, so `w_u1>=2`; likewise `w_v1>=2`.

Thus `Delta(E1)>=4`. If E1 is nonclique, the internal missing count makes `Delta(E1)>4`, impossible. If E1 is a K3, equality `Delta(E1)=4` gives a q36 repivot. The shared point c is globally decorated because D repeats, and both positive-weight petals are globally decorated; the repivot also retains the two inactive decorated shell vertices, so tau strictly increases. Contradiction.

Hence at most one c-anchor support class exists, carrying at most2 owners.   (9)

### Disjoint capacity

Zero-weight c is anticomplete to every disjoint support. Thus every disjoint support is a K3 and at most one distinct disjoint class exists, again of capacity2.

Therefore all five external owner incidences have total capacity at most

`2+2=4`,

contradiction.

So `(1,1,0)` is impossible.                                  (10)

## 6. Conclusion

All target-K3 multiplicity-two states with total weight at most2 are empty.

Therefore every surviving repeated K3 support satisfies

> `w(D)=3`.

Up to permutation, the only remaining weight patterns are

- `(1,1,1)`;
- `(2,1,0)`;
- `(3,0,0)`.

No closure of these three weight-three patterns is claimed in this file.