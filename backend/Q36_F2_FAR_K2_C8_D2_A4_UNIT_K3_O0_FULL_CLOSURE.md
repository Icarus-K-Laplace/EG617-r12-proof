# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 unit-K3 O=0 closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md`, the exact f=2 shell ledger, common-S row closure, inherited D14, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the pure-d2 support contract.

This closes the final overlap-charge subcase `O_D=0` of the unique multiplicity-three A=4 unit-weight target-K3 terminal.

## 1. Setup

Let D be the multiplicity-three target K3 from the A=4 high-multiplicity reduction. Thus

- all seven d3 owners share `S=F union {x}`;
- `w_v=kappa_v+e_F(v,S)`;
- `w(D)=(1,1,1)`;
- D has defect3 and repivots to q35;
- `O_D=0`.

Hence all four external owner incidences are carried by supports disjoint from D.

Let D0 be the unique pure globally-regular d2 support and choose `v0 in D0`. The d2 contract gives that v0 is target-anticomplete to the d3-support union U and to S. Therefore `alpha(H[U])<=2`.

For every d in D and every support E disjoint from D, row closure gives

`e_H(d,E)<=w_d=1`.                                          (1)

## 2. Every vertex in a disjoint support has positive weight

Let E be any support disjoint from D, and suppose `e in E` has `w_e=0`.

Row closure against D gives

`e_H(e,D)<=w_e=0`,

so e is target-anticomplete to D. Also `w_e=0` means e is target-anticomplete to S=`F union {x}`.

Fix d in D. Suppose dx is a target nonedge. Since `w_d=1`, d cannot be adjacent to both far vertices: two F-edges alone would contribute weight at least2. Hence some `f in F` is target-nonadjacent to d.

Then

`{d,e,v0,x,f}`

is an independent5-set:

- de is a nonedge by row closure;
- e is anticomplete to x and f because `w_e=0`;
- v0 is anticomplete to U and S;
- dx and df are nonedges by choice;
- xf is a nonedge because `a_F=0`.

Contradiction. Therefore every d in D must be target-adjacent to x. Since D is a target K3, `D union {x}` is a K4, again impossible.

Hence

> every vertex in every support disjoint from D satisfies `w_v>=1`.   (2)

## 3. Every disjoint support is a unit-weight target K3

Let E be disjoint from D. A support in U cannot be an independent triple because `alpha(H[U])<=2`.

### One target edge

Then `m(E)=2`. By (2), `sum_E w>=3`, so

`Delta(E)=m(E)+sum_E w>=5>A=4`.

Impossible.

### Exactly two target edges

Then `m(E)=1` and (2) gives `Delta(E)>=4`.

If E repeats, full defect4 is forbidden by q36 lexicographic maximality.

If E is a singleton support, equality `Delta(E)=4` would repivot to q36. All three E-vertices have positive weight by (2), hence all three are globally decorated. The repivot retains the two inactive decorated shell vertices, so tau strictly increases. Impossible.

Thus the two-edge case is impossible.

### Target K3

Now `m(E)=0`. Equation (2) gives `sum_E w>=3`.

If `sum_E w>=4`, then either E repeats and full defect4 is forbidden, or E is singleton with a q36 repivot inserting three positive-weight decorated vertices while retaining the two inactive decorated shell vertices, again increasing tau.

Therefore equality is forced:

> every disjoint support E is a target K3 with `w(E)=(1,1,1)` and defect3, hence repivots to q35.   (3)

## 4. Two distinct disjoint support classes cannot coexist

Let E,E' be two distinct support classes, both disjoint from D. By (3), both are unit-weight target K3s.

For any vertex u outside a support T, row closure gives

`e_H(u,T)<=w_u=1`.                                           (4)

We distinguish the intersection size.

### 4.1 `|E intersect E'|=2`

Write

`E=P union {a}`, `E'=P union {b}`,

where |P|=2. Since both supports are K3s, P is a target edge and both a,b are adjacent to both points of P.

If ab were a target edge, `P union {a,b}` would be a K4. Hence ab is a target nonedge.

By (4), a has at most one D-neighbour and b has at most one D-neighbour. Thus among the three vertices of D there is some d target-nonadjacent to both a and b. Then `{d,a,b}` is an independent triple in U, contradiction.

### 4.2 `|E intersect E'|=1`

Let p be the shared vertex and write

`A=E\{p}`, `B=E'\{p}`.

Every a in A is adjacent to p because E is a K3. Since p lies in E', (4) applied to support E' shows that this edge to p already consumes a's full row-closure allowance. Hence a is target-anticomplete to B. Similarly every point of B is target-anticomplete to A.

Choose any a in A and b in B. Again each has at most one D-neighbour by (4), so some d in D is target-nonadjacent to both. Therefore `{d,a,b}` is an independent triple in U, contradiction.

### 4.3 `E intersect E'=empty`

Equation (4) shows that the target cross graph E--E' has maximum degree at most1 on each side, hence at most three target edges. In particular some pair `a in E`, `b in E'` is a target nonedge.

Each of a,b has at most one D-neighbour, so there is d in D target-nonadjacent to both. Again `{d,a,b}` is an independent triple in U.

Thus in every case:

> two distinct support classes disjoint from D cannot coexist.   (5)

## 5. Owner multiplicity contradiction

All four external owner incidences are disjoint from D because `O_D=0`.

By (5), they must all use one single support class E. Hence E has owner multiplicity4.

But `Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md` proves that multiplicity4 is impossible in the A=4 branch.

Contradiction.

## 6. Conclusion

The overlap-charge zero terminal is empty:

> `c=8`, `n2=1`, `A=4`, multiplicity-three unit-weight K3 with `O_D=0` is `EMPTY`.

Combined with the previously proved `O_D=1` and `O_D=2` closures, every multiplicity-three support is eliminated from the far-K2 c8 one-d2 A=4 layer.

The remaining A=4 task is the support system with multiplicity at most2.