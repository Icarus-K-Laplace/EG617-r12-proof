# q36 f=2 far-target-K2 — c=8, one d2 row, allowance-two closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_REDUCTION.md`, common-S row closure, inherited D14, lexicographic q36 maximality, and `alpha(H)<=3`.

This closes the A=2 terminal left by the c=8 one-d2 reduction.

## 1. Setup

Let D0 be the unique d2 support. By the global far-K2 d2 reduction, D0 is a pure target K2 of globally regular core vertices.

All seven remaining low owners are d3 rows in one common missing-set class with missing set

`S=F union {x}`

and allowance A=2.

The two vertices of D0 are globally regular and have no target shell neighbour except their own d2 owner.

## 2. D0 is target-anticomplete to every d3 support

Let E be any d3 support and let u be a vertex of D0.

Since u is outside E, row closure for E gives

`e_H(u,E)<=kappa_u+e_F(u,S)`.

Global regularity of u gives `kappa_u=0`. Its only shell target neighbour is its own d2 owner, which is not in S, so `e_F(u,S)=0`.

Hence

`e_H(u,E)=0`.

Thus

> D0 is target-anticomplete to every d3 support.             (1)

Consequently the union U of all d3 supports has

> `alpha(H[U])<=2`.                                          (2)

Indeed an independent triple in U together with either vertex of D0 would form an independent4-set in H, contradicting alpha(H)<=3.

## 3. Repeated supports have defect at most one

If a repeated d3 support used full defect2, its repivot would remain at q36. It removes the active decorated vertex x but retains the two other decorated shell vertices. Because the support repeats, all three inserted support vertices are globally decorated. Thus tau would rise from3 to at least5, contradiction.

Hence every repeated support has defect at most1 and repivots to q<=35.          (3)

A repeated support cannot properly overlap another distinct support because a proper overlap of two triples costs2>A_repeated.

## 4. Repeated multiplicity is at most three

Let E be a repeated support of multiplicity m.

Because its defect is at most1, E cannot have one internal target edge (`m(E)=2`). Thus E has at least two target edges.

The target K11 base `{p} union C union F` and D14 give

`3m + O_E + e_F(F,E) + e_H(E) <=14`.

### If E is a K3

Then `e_H(E)=3`, so

`3m+3<=14`,

hence m<=3.

### If E has exactly two target edges

Then `m(E)=1`. Defect<=1 forces

- `kappa(E)=0`;
- `e_F(S,E)=0`;
- the non-missing allowance `u(E)=0`.

If m=4, D14 forces equality

- `O_E=0`;
- `e_F(F,E)=0`;
- `e_H(E)=2`.

All three remaining owner incidences therefore belong to supports disjoint from E. But joint row closure from the zero-allowance support E gives zero target cross edges to any such support.

Let ab be the unique internal target nonedge of E. Every vertex v of a disjoint support must be target-adjacent to a or b; otherwise `{a,b,v}` is an independent triple in U, violating (2). Thus at least three E--support target edges are required, contradiction.

Therefore m=4 is impossible here as well.

Hence in all cases

> every repeated support has multiplicity at most3.          (4)

## 5. Singleton intersection components have size at most two

Two distinct singleton supports can properly overlap only at full allowance2.

An overlap of size2 is impossible: both shared vertices are globally decorated, and repivoting either singleton support retains the two inactive decorated shell vertices while inserting those two decorated vertices, raising tau above3.

Thus every proper singleton overlap has size1.

If one singleton support met two others at two different shared vertices, its q36 repivot would again insert two decorated vertices while retaining the two inactive decorated shell vertices, increasing tau. Hence every connected intersection component of singleton supports is a common-hub sunflower.

At overlap equality, the standard common-S row-closure equality forces petals of different supports in the sunflower to be target-anticomplete. A sunflower of size3 would therefore contain an independent triple in U by taking one petal from each support, contradicting (2).

Thus

> every singleton intersection component has size at most2. (5)

## 6. At most two support components exist

A repeated support class is an isolated support component by Section3. Every singleton component has size at most2 by (5).

Suppose three distinct support components existed. Choose one support triple from each component. Supports from different components are disjoint. Common-S joint row closure gives at most2 target edges between any pair of triples.

Choose one vertex uniformly from each of the three triples. The expected number of target edges among the three selected vertices is at most

`3*(2/9)=2/3<1`.

Hence some choice is an independent triple in U, contradicting (2).

Therefore

> there are at most two support components.                  (6)

## 7. Owner-capacity contradiction

Each support component carries at most three owners:

- a repeated class has multiplicity at most3 by (4);
- a singleton sunflower component has size at most2 by (5).

With at most two components, the seven d3 owners can contribute at most

`3+3=6`

owner incidences.

Contradiction.

Therefore

> `c=8`, `n2=1`, `A=2` is EMPTY.

Combined with `Q36_F2_FAR_K2_C8_D2_REDUCTION.md`, the only remaining c=8 one-d2 allowance levels are A=3 and A=4.