# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 all-singleton pairwise-intersection theorem

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A4_SINGLETON_MATCHING2_THEOREM.md`, common-S row closure, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, the induced `alpha(H[U])<=2` property, and the pure-d2 support contract.

This proves that all seven singleton supports have defect at most3 and are pairwise intersecting.

## 1. Full-defect supports form sunflower components

A singleton support of full defect4 repivots to q36. The two inactive decorated shell vertices are retained. Therefore lexicographic maximality permits at most one globally decorated support vertex; otherwise tau rises.

Every positive-weight vertex is globally decorated, and every vertex shared by two support classes is globally decorated. Hence a full-defect support has at least two clean private vertices of weight0 and can meet all other supports only through one possible shared vertex.

Consequently every connected component of the intersection graph formed only by full-defect supports is a sunflower with one common hub: once two supports meet at z, z is the unique shared vertex of each, so every further intersection in that component is forced through the same z.

By the matching-two theorem there are at most two such disjoint sunflower components. If all seven supports were full-defect, one component would contain at least three supports. Choose one clean weight-zero private petal from each of three supports in that component. Each chosen petal lies outside the other two supports and has weight0, so row closure makes the three petals pairwise target-anticomplete. This is an independent triple in U, contradicting alpha(H[U])<=2.

Therefore

> at least one support has defect at most3.                    (1)

Call such a support low.

## 2. A low nonclique support cannot be disjoint from any support

Let D be low and nonclique.

### One target edge

Then m(D)=2 and defect<=3 gives w(D)<=1. If E were disjoint from D, every vertex of E must cover both internal target-nonedges of D in order to avoid an independent triple with their endpoints. One edge to the common isolated endpoint can cover both, but each of the three E-vertices needs at least one D-neighbour. Thus

`e_H(D,E)>=3`.

Joint row closure gives `e_H(D,E)<=w(D)<=1`, contradiction.

### Two target edges

Then m(D)=1 and w(D)<=2. A disjoint support E must cover the unique internal target-nonedge from each of its three vertices, again forcing

`e_H(D,E)>=3>w(D)`.

Therefore

> every low nonclique support intersects every other support.   (2)

## 3. A low unit-weight K3 cannot occur

Let D be a low target K3 with all three support weights positive. Since w(D)<=3, necessarily

`w(D)=(1,1,1)`.                                              (3)

The standard unit-K3 row-closure argument from the already certified A4 multiplicity-two closure applies without any multiplicity assumption on D:

- every support disjoint from D is forced to be a unit-weight target K3;
- two distinct disjoint support classes cannot coexist;
- a two-point overlap with D is impossible;
- at a fixed one-point anchor, two distinct intersecting support classes cannot coexist;
- classes anchored at two different D-points cannot coexist.

Because the current system is all-singleton, this means D can coexist with at most one disjoint support and at most one intersecting support, i.e. at most two other supports total.

But six other supports are present. Contradiction.

Hence

> no low K3 has weight pattern (1,1,1); every low K3 has a zero-weight point.   (4)

## 4. Two low K3 supports cannot be disjoint

Suppose low K3 supports D,E are disjoint. By (4), choose weight-zero points d in D and e in E.

Row closure gives

- d target-anticomplete to E;
- e target-anticomplete to D.

Thus de is a target nonedge. Weight zero also makes d and e target-anticomplete to the common missing set S=F union {x}.

Let v0 be either point of the pure d2 support D0. The d2 contract makes v0 target-anticomplete to U and to S.

Because a_F=0, x is target-nonadjacent to either far vertex f in F. Therefore

`{d,e,v0,x,f}`

is an independent5-set in the parent graph, contradiction.

Together with (2), this proves

> all low supports are pairwise intersecting.                 (5)

## 5. There is at most one full-defect support

Let D be the low support guaranteed by (1). Suppose E,E' are two full-defect supports.

Choose clean private weight-zero vertices u in E and v in E'. They lie outside D, so row closure against D makes both target-anticomplete to D. Also u lies outside E' and has weight0, so uv is a target nonedge.

For any d in D, the triple `{d,u,v}` is independent in U, contradicting alpha(H[U])<=2.

Hence

> at most one full-defect support exists.                     (6)

## 6. The unique full-defect support is also impossible

Assume E is the unique full-defect support. The other six supports are low and pairwise intersecting by (5).

E cannot be disjoint from a low nonclique by (2). It also cannot be disjoint from a low K3 D: choose a zero-weight point d in D using (4), and a clean zero-weight private point u in E. Then d and u are target-nonadjacent by row closure and both are anticomplete to S. With v0 in D0, x and a far point f, the set `{d,u,v0,x,f}` is an independent5-set.

Thus E intersects every low support.

But a full-defect support has at most one shared/decorated vertex. Hence all six intersections occur at one common point z in E; every low support contains z.

Let u be one of the two clean private weight-zero points of E. For every low support L, u lies outside L and row closure gives `e_H(u,L)=0`. Hence u is target-anticomplete to the union of all six low supports.

Since alpha(H[U])<=2, that entire union must be a target clique: any target-nonedge ab in the union together with u would be an independent triple.

Inherited K4-freeness therefore forces the union to have at most three vertices. But six distinct 3-subsets cannot all lie in a three-point set. Contradiction.

Therefore no full-defect support exists.                    (7)

## 7. Conclusion

All seven singleton supports satisfy

- defect at most3;
- pairwise intersection.

Thus the final A=4 all-singleton terminal is now a purely intersecting 3-uniform support system:

> seven distinct pairwise-intersecting triples, each of defect at most3, under common-S row closure, K4-freeness and alpha(H[U])<=2.

The next step is the intersecting-family classification.