# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 unit-K3 O=2 closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md`, the exact f=2 shell ledger, q35 shell floor `z>=22`, row closure, inherited D14, q36 lexicographic maximality, K4-freeness, `alpha(F)<=4`, and the pure-d2 support contract.

This closes the overlap-charge `O_D=2` subcase of the unique multiplicity-three A=4 terminal.

## 1. A4 inactive-shell normal form

Here c=8, n2=1, a_F=0 and all seven d3 owners miss the same active decorated vertex x. Write

`X={x} union Y`, `|Y|=2`.

For A=4 the class identity is

`nu_x+g_x=5`.                                               (1)

The exact shell ledger gives

`G=7-nu`,

where `nu=nu_x+eta` and `eta=e_M(Y)`.

Hence the total decoration on the two inactive points is

`G_Y=G-g_x=2-eta`.                                         (2)

Both points of Y are decorated, so `G_Y>=2`. Therefore

> `eta=0`, Y is a target K2, and both Y-points have decoration exactly1.   (3)

## 2. Repivoting the unit-weight repeated K3

Let D be the multiplicity-three K3 terminal from the high-multiplicity reduction. Thus

`w(D)=3`, with weights `(1,1,1)`,

and D repivots to q35.

Let `O_D` be the external owner-incidence overlap with D. The low-owner incidence on D is

`lambda(D)=9+O_D`.

For a core point v promoted to the shell,

`g_v=kappa_v+(old shell target degree of v)-1`.

Summing over D and using

`kappa(D)+e_F(F union {x},D)=w(D)=3`

gives

`sum_(d in D)g_d = 9+O_D+e_F(Y,D)`.                        (4)

The new q35 shell retains Y with total decoration2, so

`G'=11+O_D+e_F(Y,D)`.                                      (5)

Every q35 shell has at least22 missing edges, hence `G'<=13`. Therefore

> `O_D+e_F(Y,D)<=2`.                                       (6)

D14 for D independently gives

> `O_D+e_F(F,D)<=2`.                                       (7)

## 3. Consequences when O_D=2

Assume `O_D=2`. Equations (6)--(7) force

`e_F(Y,D)=0`, `e_F(F,D)=0`.                                (8)

Thus D is target-anticomplete to all four shell points in `Y union F`.

At least two of the four external owner incidences are carried by supports disjoint from D. Fix one such support E.

Each d in D has weight1, so row closure gives

`e_H(d,E)<=1`.                                               (9)

## 4. A disjoint K3 support is impossible

Assume E is a target K3.

Every e in E has at least one target nonneighbor in D: otherwise e is adjacent to all three vertices of the target K3 D, creating a K4.

Fix such a nonedge de. Since D is anticomplete to Y and F by (8), if e were nonadjacent to some `y in Y` and some `f in F`, then

`{d,e,v0,y,f}`

with `v0 in D0` would be an independent5-set. Therefore the neighbourhood of e in `Y union F` must cover the complete bipartite nonedge graph between Y and F. A minimum vertex cover of K2,2 is an entire side, so every e satisfies

- e is adjacent to both vertices of Y, or
- e is adjacent to both vertices of F.                      (10)

The three vertices of the K3 E receive only these two side-types. Two adjacent vertices must share one type, and together with the corresponding target edge inside Y or F they form a K4. Contradiction.

Thus E cannot be a K3.

## 5. The only nonclique possibility is an exact path

A support in U cannot be independent, so E has one or two target edges.

If E has only one target edge, its two internal nonedges share an isolated vertex c. Each d in D has at most one E-neighbour by (9) but must hit both internal nonedges to avoid an independent triple in U. Hence every d must be adjacent to c. Then `D union {c}` is a K4. Impossible.

Therefore E has exactly two target edges. Write its unique nonedge endpoints as u,v and its center as c.

Every d in D must be adjacent to u or v; by (9) exactly one. K4-freeness forbids all three d choosing the same endpoint, so the three cross edges split 2+1 between u and v. In particular every one of u,v,c has a D-nonneighbour.

The independent5 argument from Section4 therefore applies to each vertex of E: every E-vertex is side-covering, i.e. adjacent to both Y or both F.

Adjacent vertices of the path cannot have the same side-type, or together with the corresponding edge of Y or F they form a K4. Thus the only two-colouring of the path gives the endpoints one type and the center the other.

If the endpoints were F-type, each contributes at least2 units to the common-S weight, so with the internal missing count1 we would have `Delta(E)>=5`, impossible for A=4.

Hence the endpoints are Y-type and the center is F-type. Therefore

- u,v are adjacent to both Y;
- c is adjacent to both F;
- the internal missing count is1;
- `w_c>=2`.

So `Delta(E)>=3`. If `Delta(E)=4`, E repivots to q36. But all three of u,v,c are globally decorated: u,v have two Y shell neighbours, and c has two F shell neighbours. The q36 repivot retains the two inactive decorated shell vertices and inserts three decorated support vertices, increasing tau. Contradiction.

Thus equality is forced:

> `Delta(E)=3`, `w_u=w_v=0`, `w_c=2`, with no additional core/S weight.   (11)

## 6. The exact path still creates a K4

The zero-weight endpoints u,v are target-anticomplete to `S=F union {x}`.

Every d in D is adjacent to exactly one of u,v. Hence for every d, the other endpoint e(d) is target-nonadjacent to d.

D is target-anticomplete to F by (8). If dx were also a nonedge, then

`{d,e(d),v0,x,f}`

would be an independent5-set for either far point f: e(d) and v0 are anticomplete to S, and v0 is anticomplete to U.

Therefore every d in D must be target-adjacent to x. But D is a target K3, so

`D union {x}`

is a K4. Contradiction.

## 7. Conclusion

No support can be disjoint from D when `O_D=2`, while D14/owner incidence requires at least two disjoint external owner incidences. Therefore

> the unit-weight multiplicity-three K3 terminal has no `O_D=2` realization.

The only remaining overlap charges are

`O_D in {0,1}`.