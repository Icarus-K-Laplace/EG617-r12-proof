# q36 f=2 far-target-K2 — c=8, one d2 row, allowance-three full closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`, `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_FULL_CLOSURE_V2.md`, common-S row closure and overlap inequalities, inherited D14, CORE211 (`sum kappa<=2`), q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, and the pure-d2 support contract.

This closes the entire `c=8,n2=1,A=3` far-target-K2 layer. No fixed 12-point remainder is used.

## 1. Setup

Let D0 be the unique d2 support. It is a pure target K2 of globally regular core vertices and is target-anticomplete to

`S=F union {x}`

and to the union U of all seven d3 supports. Hence

`alpha(H[U])<=2`.                                           (1)

For any core vertex v write

`w_v=kappa_v+e_F(v,S)`.

Every d3 support E has

`Delta(E)=m(E)+sum_(v in E) w_v <=3`,

where `m(E)=3-e_H(E)`. A repeated support cannot use full defect3, because a q36 repivot would retain the two inactive decorated shell vertices and insert multiple globally decorated support vertices. Therefore every repeated support has defect at most2.

The previous two closure files eliminate every multiplicity-three support. It remains to eliminate multiplicity-two supports and then the all-singleton system.

## 2. Repeated nonclique supports are impossible

Let D be a support of multiplicity2. Repetition gives `Delta(D)<=2`.

### 2.1 One-edge D dies immediately

If `e_H(D)=1`, then `m(D)=2`, so `w(D)=0`.

Choose a target-nonedge pair u,v inside D. Both are target-anticomplete to S. Choose `v0 in D0` and one far point `f in F`. Since `a_F=0`, xf is a nonedge, and D0 is target-anticomplete to U and S. Thus

`{u,v,v0,x,f}`

is an independent5-set, contradicting `alpha(F)<=4`.

Hence a repeated nonclique support must have exactly two target edges.

### 2.2 Exact surviving two-edge normal form

Write D={a,b,c} with unique target nonedge ab and edges ac,bc. Then `m(D)=1`, so

`w(D)<=1`.

If `w(D)=0`, the pair ab together with `v0,x,f` again gives an independent5-set. Therefore `w(D)=1`.

If the unique positive unit lay on c, or if it were pure core excess with no S-adjacency, then a and b would both be target-anticomplete to S and the same independent5 contradiction would apply. Thus, up to swapping a,b,

> `w_a=1`, `w_b=w_c=0`, `kappa(D)=0`, and a has exactly one target neighbour in S.   (2)

Any support disjoint from D is impossible: the unique nonedge ab must be covered from each of its three vertices, requiring at least3 D--E target edges, while the non-missing cross allowance of D is at most1.

Hence all five external owner incidences meet D. D14 gives

`6+O_D+e_F(F,D)+2<=14`,

so

`O_D+e_F(F,D)<=6`,                                         (3)

with `O_D>=5`.

### 2.3 Every external support has defect at most2

Let E be one of the five external supports. It intersects D. Every vertex of `E\D` must meet the nonedge {a,b}, otherwise it forms an independent triple with a,b in U. Row closure against D therefore gives

`w_v>=1` for every `v in E\D`.                             (4)

All vertices of D are globally decorated because D repeats, and every vertex satisfying (4) is also globally decorated: it has its owner shell neighbour plus positive `kappa+S` weight.

Thus every vertex of E is globally decorated. If E had defect3, its q36 repivot would retain the two inactive decorated shell vertices and insert three decorated core vertices, increasing tau above the chosen q36 maximum. Therefore

> every external support E has `Delta(E)<=2`.               (5)

### 2.4 Exact overlap templates

If `|E intersect D|=1`, then the shared point cannot be a (the positive-weight vertex). The two outside vertices each have weight at least1 by (4), so (5) forces zero weight on the shared point, both outside weights exactly1, and `m(E)=0`.

If the shared point were c, each outside vertex would have to meet {a,b} in addition to its K3 edge to c, giving at least two D-edges but weight1, impossible by row closure. Hence every one-point overlap has the exact form

> `E={b,u,v}`, E is a target K3, `w_u=w_v=1`, and u,v have no D-neighbour other than b.   (6)

If `|E intersect D|=2`, the pair cannot contain a. Thus the shared pair is exactly {b,c}. Let E={b,c,v}. From (4)--(5) only two possibilities remain:

- `E` is a K3, `w_v=2`, with v adjacent to b,c and to no other point of D;
- `E` has exactly the two edges bc,bv, `w_v=1`, with v nonadjacent to a,c.

Call these the h2 templates.                                               (7)

### 2.5 Owner capacity contradiction

Two distinct h1 supports at b are impossible. If

`E_i={b,u_i,v_i}`, E_j={b,u_j,v_j}`

are distinct, a petal of one already spends its full weight1 on the edge to b. Row closure against the other support forces the two petal pairs to be target-anticomplete. The zero-weight point c is target-nonadjacent to every petal, so choosing one petal from each support together with c gives an independent triple in U.

Hence all h1 owner incidences can use only one support class, of multiplicity at most2.

From (3):

- if the unique S-edge of a goes to F, then `e_F(F,D)=1`, so `O_D=5`; all five external owners are h1;
- if it goes to x, then `e_F(F,D)=0` and `O_D` is 5 or6. For O_D=5 all five are h1; for O_D=6 exactly one owner is h2 and four are h1.

In every case at least four h1 owner incidences are required, but the unique possible h1 class carries at most2 owners. Contradiction.

Therefore

> no repeated nonclique support exists.                     (8)

## 3. Repeated K3 supports are impossible

Let D be a repeated target K3 of multiplicity2.

Any support disjoint from D must also be a K3: a nonclique disjoint support has an internal target nonedge requiring at least3 D-cross edges, while the repeated K3 D has non-missing allowance at most2.

If two distinct disjoint K3 classes existed, the correct common-pair argument from `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_FULL_CLOSURE_V2.md` applies verbatim and gives an independent5-set. If one disjoint K3 class carried at least two owners, it would itself be repeated; both repeated K3s contain a zero-weight vertex, and row closure yields the same zero-zero independent5 contradiction.

Hence

> at most one external owner is carried by a support disjoint from D.   (9)

Thus at least four external owners intersect D.

A proper overlap of two 3-supports costs2 in the common-S overlap inequality. Since D repeats, `Delta(D)<=2`; the existence of an intersecting distinct support therefore forces

`w(D)=Delta(D)=2`.                                          (10)

The three integer weights on D are consequently either

`(1,1,0)` or `(2,0,0)`.                                    (11)

### 3.1 Intersecting support templates

First note that at most one intersecting support can have defect3. Indeed a q36 support overlapping D retains the two inactive decorated shell vertices and already inserts a decorated shared D-vertex. Therefore its other two vertices must be globally regular. Such vertices have weight0 and are private. If two distinct q36 supports existed, choose one clean private vertex from each; row closure makes them a target nonedge, and together with `v0,x,f` they form an independent5-set.

For a q36 support E with one-point overlap `{d}` with D, the two clean outside vertices are anticomplete to D. Since E cannot itself be an independent triple by (1), they form a K2 while d is isolated from them. Hence `m(E)=2` and defect3 forces

> `w_d=1`.                                                   (12)

So a q36 exception can only be anchored at a weight-one vertex of D.

Every other intersecting support has defect at most2.

If it has one-point overlap `{d}`, a short edge-count enumeration gives a unique possibility:

> d has weight0; the support is a target K3; its two private petals have weight1 and use their entire row-closure budget on d.   (13)

If it has two-point overlap, both shared D-points must have weight0. Writing the support as `{d1,d2,v}`, the only possibilities are

- a K3 with `w_v=2`, or
- a two-edge support in which v is adjacent to exactly one shared point and `w_v=1`.

No q36 two-point overlap is possible because it would insert at least two already-decorated D-points and retain two inactive decorated shell vertices.                         (14)

### 3.2 Weight pattern `(1,1,0)`

There is only one zero-weight point z in D. By (14) no two-point overlap exists. Every low-defect intersecting support is therefore a K3 anchored at z as in (13).

Two distinct such K3 classes are impossible: their petal pairs are target-anticomplete by row closure, and either of the other two D-points is target-nonadjacent to all petals, producing an independent triple.

Thus the low-defect supports contribute at most one support class, of multiplicity at most2. Together with the at-most-one q36 exception from (12), at most3 intersecting owner incidences are possible, contradicting (9), which requires at least4.

Hence `(1,1,0)` is impossible.

### 3.3 Weight pattern `(2,0,0)`

There is no weight-one D-point, so (12) shows that no q36 intersecting support exists. All intersecting supports have defect at most2 and use only the two zero-weight D-points.

One-point K3 supports cannot be anchored at both zero points: if one is anchored at z1 and another at z2, a petal from each is target-nonadjacent to the positive-weight third D-point; alpha-two then forces all four petal cross-edges, while row closure from a weight-one petal allows at most one such edge. Contradiction.

Hence all one-point supports use the same zero anchor, and two distinct classes at that anchor are impossible by the same petal-pair/other-zero independent-triple argument. So the one-point owner incidences occupy at most one class of multiplicity2.

Now use D14 for D:

`6+O_D+e_F(F,D)+3<=14`,

so

`O_D+e_F(F,D)<=5`.                                         (15)

If there is no disjoint owner, all five external owners intersect D, so O_D>=5. Equality in (15) forces O_D=5 and every owner is a one-point overlap, requiring five one-point owner incidences, impossible because their total capacity is2.

If there is one disjoint owner, four owners intersect D. If O_D=4, all four are one-point overlaps, again impossible. If O_D=5, exactly one intersecting owner is a two-point template and the remaining three are one-point overlaps; three still exceed the one-point capacity2.

Thus `(2,0,0)` is also impossible.

Therefore

> no repeated K3 support exists.                            (16)

Combining (8) and (16), every one of the seven d3 supports is a distinct singleton support.

## 4. The all-singleton system has no q36 support

Suppose a singleton support Q has defect3 and repivots to q36. The repivot retains the two inactive decorated shell vertices, so Q contains at most one globally decorated vertex. Hence at least two vertices of Q are clean globally regular vertices with weight0.

Every other support E has defect at most2 unless it is another q36 support. Two q36 supports are impossible: clean private zero-weight vertices from the two supports are target-nonadjacent by row closure and, together with `v0,x,f`, form an independent5-set.

Now let E be any low-defect support. If E were disjoint from Q, E contains a zero-weight vertex because its three nonnegative weights sum to at most2 after subtracting its internal missing count. A clean zero-weight vertex of Q is anticomplete to E by row closure, so again a zero-zero pair plus `v0,x,f` is an independent5-set. Hence all six other supports meet Q.

The two clean vertices of Q cannot be shared, since a second owner would make them globally decorated. Therefore every intersection uses the same possible decorated point z of Q. Each low support overlaps Q properly and has defect at most2. Equality in the common-S overlap inequality forces

`w_z=0`.                                                     (17)

Thus all three vertices of Q have weight0. Since Q itself lies in U and `alpha(H[U])<=2`, Q is not an independent triple, so `m(Q)<=2`. Therefore `Delta(Q)<=2`, contradicting the assumed defect3.

Hence

> every singleton support has defect exactly2.              (18)

## 5. All seven singleton supports are pairwise intersecting

Suppose two defect-two supports E,E' were disjoint.

If either were nonclique, an internal target nonedge would have to be covered from every vertex of the other support, requiring at least3 cross edges, whereas its non-missing allowance is at most1. Contradiction.

If both are K3s, each has a zero-weight vertex because its three weights sum to at most2. A zero-weight vertex of E' is anticomplete to E by row closure. Choosing zero-weight vertices from both supports gives a target nonedge pair, and together with `v0,x,f` gives an independent5-set.

Therefore all seven supports are pairwise intersecting. Every proper overlap costs2, and each support has defect2, so overlap equality implies:

> every globally shared support vertex has weight0.          (19)

## 6. No singleton support can be nonclique

Assume D is nonclique. Because `Delta(D)=2`:

- the one-edge case has `w(D)=0` and dies immediately by the internal nonedge plus `v0,x,f`;
- hence D has exactly two target edges and a unique target nonedge ab.

Exactly as in Section2, survival forces the exact path normal form

`w_a=1`, `w_b=w_c=0`,

where c is the center and the positive unit on a is a real S-adjacency. By (19), a is private, so every other support intersects D only through b,c.

Let E be another support.

- If `E intersect D={b}`, then the two outside vertices must each cover the nonedge ab, so each has weight at least1. Defect2 forces E to be a K3, the two outside weights to be1, and their only D-neighbour to be b.
- `E intersect D={c}` is impossible: defect2 would force E to be a K3, but then each outside vertex would need an additional a/b edge to cover ab, exceeding its row-closure weight1.
- If `|E intersect D|=2`, the shared pair is exactly {b,c}; the only possibilities are the two h2 templates from Section2.4.

Thus all six other supports contain b.

Two distinct h1 supports at b are impossible: their petal pairs are target-anticomplete by row closure, and c is anticomplete to all petals, giving an independent triple.

Two distinct h2 supports are impossible: their outside vertices exhaust their weights on the shared pair {b,c}, so they are target-nonadjacent to each other and to a, again giving an independent triple.

Therefore at most one h1 and one h2 support can coexist, i.e. at most two supports besides D. But six are required. Contradiction.

Hence

> all seven singleton supports are target K3s.               (20)

## 7. Final K3 shared-set contradiction

Each K3 support has defect2. By (19), shared vertices have weight0. Therefore each support has either

- one shared vertex and two private vertices of weight1 each; or
- two shared vertices and one private vertex of weight2.

Let `S_E` be the shared-vertex subset of support E. The seven sets `S_E` have size1 or2 and are pairwise intersecting.

### 7.1 No common shared point

Then every `S_E` has size2 and the pairwise-intersecting 2-set family is supported on a triangle, with pair types ab,ac,bc. Let their multiplicities be

`n_ab+n_ac+n_bc=7`.

For a support of pair type ab, let v be its private vertex. If r_a,r_b are the total owner multiplicities of the shared points, the low-owner incidence in this support is

`lambda(E)=r_a+r_b+1`.

Since `r_a+r_b=7+n_ab`, D14 gives

`(7+n_ab)+1+e_F(F,E)+3<=14`,

hence

`n_ab+e_F(F,E)<=3`.                                        (21)

Thus `n_ab<=3`, and similarly for the other pair types.

If `n_ab=3`, (21) forces zero far incidence for every support of that type. Its private vertex has weight2, so with no far incidence and at most one x-edge it has `kappa_v>=1`. The three private vertices are distinct, forcing total core excess at least3, contradicting CORE211 `sum kappa<=2`.

Hence every pair type has multiplicity at most2. Their total capacity is at most6, contradicting seven supports.

### 7.2 Common shared point

Now all `S_E` contain one common point z. Let k be the number of supports with a second shared point. Then `7-k` supports have shared set exactly {z}; their two private vertices have weight1.

For two such supports, a private vertex already spends its full weight1 on the edge to z, so different private pairs are target-anticomplete. Three such supports would yield an independent triple by choosing one private vertex from each. Hence

`7-k<=2`, so `k>=5`.                                       (22)

Consider two supports with second shared vertices y_i and y_j. Every shared vertex has weight0 by (19). If `y_i != y_j`, then y_j is adjacent to z inside its own K3 but lies outside the other support; row closure against that other support would require

`1<=e_H(y_j,E_i)<=w_yj=0`,

impossible. Therefore all k supports use the same second shared point y.

Their private vertices each have weight2 and are adjacent to both z and y. Row closure between two such supports spends the full weight2 on z,y, so their private vertices are pairwise target-nonadjacent. Three of them would form an independent triple. Therefore k<=2, contradicting (22).

Thus the common-point case is also impossible.

## 8. Conclusion

The allowance-three layer has no repeated supports and no all-singleton realization. Therefore

> `c=8, n2=1, A=3` is EMPTY.

Combined with the previously proved A=2 closure, the only remaining `c=8,n2=1` far-target-K2 allowance level is A=4.