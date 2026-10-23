# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 unit-K3 O=1 closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md`, `Q36_F2_FAR_K2_C8_D2_A4_UNIT_K3_O2_CLOSURE.md`, the q35 secondary-shell bounds, common-S row closure, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, and the pure-d2 support contract.

This closes the overlap-charge `O_D=1` subcase of the unique multiplicity-three A=4 unit-weight K3 terminal.

## 1. Setup

Let D be the multiplicity-three target K3 from the A=4 high-multiplicity reduction. Thus

- `w(D)=(1,1,1)` for `w_v=kappa_v+e_F(v,S)` with `S=F union {x}`;
- D has defect3 and repivots to q35;
- `O_D=1`;
- the q35 secondary-shell bound gives `e_F(Y,D)<=1`, where `Y=X\{x}` is the inactive target K2;
- D14 gives `e_F(F,D)<=1`.

Therefore the total number of D--(Y union F) target edges is at most2. Since |D|=3, choose

`d0 in D`

that is target-anticomplete to `Y union F`.                    (1)

There are four external owner incidences and only one overlap incidence with D, so at least three external owner incidences lie in supports disjoint from D. Fix any such support E.

The pure d2 support D0 is target-anticomplete to U and to `S`; write `v0 in D0`.

## 2. At least two vertices of E are side-covering

Because `w_d0=1`, row closure against E gives

`e_H(d0,E)<=1`.

Hence at least two vertices of E are target-nonadjacent to d0.

Let e be any such vertex. If e were target-nonadjacent to some `y in Y` and some `f in F`, then

`{d0,e,v0,y,f}`

would be an independent5-set:

- d0 is anticomplete to Y and F by (1);
- e is nonadjacent to d0,y,f by choice;
- v0 is anticomplete to U and to all decorated shell vertices and far vertices in S;
- Y and F are shell blocks with no target cross-edge available to this selected y,f under the far-K2 c8 one-d2 contract.

Therefore every E-vertex nonadjacent to d0 must be adjacent to both points of Y or to both points of F. Call such a vertex **side-covering**.

Thus

> every disjoint support E contains at least two side-covering vertices.   (2)

## 3. E cannot have one internal target edge

Suppose E has exactly one target edge, so it contains an isolated point c and two internal target nonedges through c.

The vertex d0 has at most one E-neighbour. To avoid an independent triple in U using d0 and an internal nonedge of E, that unique neighbour would have to hit both internal nonedges, hence must be c.

The other two E-vertices are then both side-covering by (2). They are adjacent to each other (the unique E-edge), so they cannot side-cover the same shell side: two adjacent core vertices both adjacent to the two-point target edge Y (or both to F) would form a K4. Hence one is F-side-covering.

A F-side-covering vertex contributes at least2 units to `w`. The internal missing count is2, so

`Delta(E)>=4`.

A=4 forces equality and a q36 repivot. But both side-covering vertices are globally decorated, and the q36 repivot retains the two inactive decorated shell vertices. Thus tau would strictly exceed the chosen q36 maximum. Contradiction.

Therefore E is not one-edge.

## 4. Every disjoint E has a zero-weight vertex

There remain two possibilities.

### 4.1 E is a target K3

At least two E-vertices are side-covering by (2). They are adjacent, so they cannot use the same side without creating a K4 with Y or F. Thus one of them is F-side-covering and contributes at least2 to w.

If `Delta(E)=4`, E repivots to q36. At least the two side-covering vertices are globally decorated, and the repivot retains the two inactive decorated shell vertices, increasing tau. Hence

`Delta(E)<=3`.

Since E is a K3, `Delta(E)=w(E)<=3`; one vertex already has weight at least2, so at least one E-vertex has weight0.

### 4.2 E has exactly two target edges

Write the path as endpoints u,v and center c. The unique target nonedge is uv.

The vertex d0 must meet u or v to avoid an independent triple; because it has at most one E-neighbour, its unique E-neighbour is one endpoint. Consequently the other endpoint and the center are both nonadjacent to d0 and hence both side-covering by (2).

Those two vertices are adjacent, so they use different shell sides; one is F-side-covering and has weight at least2.

Here the internal missing count is1. If `Delta(E)=4`, the q36 repivot again retains the two inactive decorated shell vertices and inserts at least the two decorated side-covering vertices, increasing tau. Therefore `Delta(E)<=3`, so the total weight on E is at most2.

The F-side-covering vertex already contributes2, hence at least one of the other two vertices has weight0.

Thus in all cases

> every support E disjoint from D contains a vertex `e0` with `w_e0=0`.   (3)

## 5. A zero-weight disjoint vertex forces x+D to be a K4

Fix E and `e0` from (3). Since e0 lies outside support D, row closure against D gives

`e_H(e0,D)<=w_e0=0`.

Hence e0 is target-anticomplete to all of D.

Take any `d in D`. Suppose dx were a target nonedge. Since `w_d=1`, d cannot be adjacent to both far vertices: two far edges alone would already contribute2 to its weight. Therefore choose a far vertex `f in F` target-nonadjacent to d.

Then

`{d,e0,v0,x,f}`

is an independent5-set:

- e0 is anticomplete to D and to S because `w_e0=0`;
- v0 is anticomplete to U and S;
- dx and df are nonedges by choice;
- xf is a nonedge because `a_F=0`.

Contradiction.

Therefore every d in D is target-adjacent to x. Since D is a target K3,

`D union {x}`

is a K4, contradicting K4-freeness.

## 6. Conclusion

The unit-weight multiplicity-three target-K3 terminal has no `O_D=1` realization.

Combined with the O=2 closure, the only overlap charge still open in the multiplicity-three A=4 terminal is

> `O_D=0`.