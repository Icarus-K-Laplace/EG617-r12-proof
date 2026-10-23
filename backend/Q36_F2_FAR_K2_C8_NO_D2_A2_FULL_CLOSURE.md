# q36 f=2 far-target-K2 — c=8 no-d2, allowance two full closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, inherited D14/K4-freeness, CORE211, and `alpha(H)<=3`.

All eight d3 owners belong to one common missing-set class S=F union {x} with allowance A=2.

Write

`w_v=kappa_v+e_F(v,S)`.

For every support E,

`Delta(E)=m(E)+w(E)<=2`.

If E repeats, full defect2 would repivot to q36 while retaining the two inactive decorated shell vertices and inserting repeated decorated support vertices. Hence every repeated support satisfies

`Delta(E)<=1`.                                               (1)

## 1. Repeated two-edge supports are impossible

A repeated one-edge support is already impossible because its internal missing count is2>1.

Let D be a repeated two-edge support. Then `m(D)=1`, so (1) forces

`w(D)=0`.                                                     (2)

Proper overlap costs2 and is impossible for D. Hence every distinct support class is disjoint from D. Joint row closure gives zero target D-cross edges.

Let ab be the unique internal target nonedge of D.

If two distinct external support classes E,E' exist, their cross target graph has fewer than nine edges, so choose a target-nonedge pair e in E, e' in E'. Since D is target-anticomplete to both classes,

`{a,b,e,e'}`

is an independent4-set in H, contradiction.

Thus at most one distinct external class can coexist with D.

A repeated two-edge support has owner multiplicity at most4 by D14. If D has multiplicity at most3, at least five owners remain and cannot fit into one class. If D has multiplicity4, exactly four owners remain; a single K3 class has multiplicity at most3, so the only possible one-class fill is another repeated two-edge support of multiplicity4.

But two such supports are target-anticomplete and each contains an internal target nonedge. Taking one nonedge pair from each gives an independent4-set.

Therefore

> no repeated two-edge support exists.                        (3)

## 2. Repeated K3 supports force at most two external classes

Let D be a repeated target K3. By (1),

`w(D)<=1`,                                                    (4)

so D contains a zero-weight point z. Proper overlap is impossible because its cost2 exceeds the repeated-support allowance, hence every distinct support class is disjoint from D. Row closure makes z target-anticomplete to every external support.

Suppose an external support E is nonclique. Since A=2, E has either one target edge with w(E)=0 or two target edges with w(E)<=1. Let uv be an internal target nonedge of E.

There must be another distinct external class E': the repeated K3 D has multiplicity at most3, while a single external class has multiplicity at most4, so one class cannot carry all remaining owners in any eight-owner partition compatible with (3).

If every point of E' met u or v, then `e_H(E,E')>=3`, but joint row closure gives at most w(E)<=1. Hence some e' in E' is target-nonadjacent to both u,v.

Because z is anticomplete to E and E',

`{z,u,v,e'}`

is an independent4-set. Contradiction.

Thus every external support class is a target K3.             (5)

Now suppose three distinct external K3 classes E1,E2,E3 exist.

If two of them overlap, proper overlap costs2. Since both are singleton classes in that overlap (repeated classes have allowance<=1 and cannot overlap), they have full defect2 and repivot to q36. Lexicographic maximality permits only the shared point to be globally decorated, so each has two clean private weight-zero points. Choosing one clean private point from each of the two overlapping supports gives two target-nonadjacent points, both target-anticomplete to the third support by row closure; any point of the third support completes an independent3 among external supports, and z gives an independent4.

If E1,E2,E3 are pairwise disjoint, each pair has at most2 target cross-edges. Choosing one point uniformly from each gives expected target-edge count at most

`3*(2/9)=2/3<1`,

so some choice is an independent triple, again completed by z to an independent4.

Therefore

> at most two distinct external support classes coexist with a repeated K3 D.   (6)

## 3. Owner counting forces three repeated K3 blocks

The repeated K3 D has multiplicity at most3. By (6), the remaining owners lie in at most two support classes. Repeated two-edge supports are excluded by (3), and a repeated K3 has multiplicity at most3.

To carry all eight owners, both external classes must therefore be repeated target K3s. The three owner multiplicities are `3,3,2` up to permutation.

Repeated-support allowance (1) implies every one of the three K3 blocks has total weight at most1. Proper overlap is impossible, so the three K3 blocks are pairwise disjoint. Joint row closure gives at most one target cross-edge between every pair of blocks.             (7)

## 4. Three low-weight K3 blocks contradict the global weight budget

Let B1,B2,B3 be the three blocks and let v be any of the other 26 core vertices.

Suppose `w_v<=1`. Row closure against each Bi gives

`e_H(v,B_i)<=1`.

Hence each Bi contains at least two target-nonneighbours of v. From each Bi choose uniformly one of two such nonneighbours. Between every pair of blocks there is at most one target edge, so the expected number of target edges among the three choices is at most

`3*(1/4)=3/4<1`.

Thus there is a choice of one point from each block that is pairwise target-nonadjacent and also target-nonadjacent to v. This is an independent4-set in H, contradiction.

Therefore every core vertex outside the nine block vertices has

`w_v>=2`.

So

`sum_H w_v >= 26*2 =52`.                                    (8)

On the other hand `sum_H kappa_v=2` by CORE211. The common missing set is S=F union {x}. Each regular far row has at most12 core neighbours, and the active decorated row x has core-row size

`|D_x|=d_M(x)+g_x=10-t_x+nu_x+g_x`
`     =10-t_x+A+a_F`
`     <=14`

because A=2 and a_F<=2. Hence

`sum_H e_F(v,S) <=12+12+14=38`.

Therefore

`sum_H w_v <= 2+38=40`,                                     (9)

contradicting (8).

Thus

> no repeated K3 support exists.                             (10)

Combined with (3), there are no repeated support classes at all.

## 5. All eight supports are singleton triples

All support classes are now distinct singleton triples.

If two supports properly overlap, the overlap cost is2, hence both have exact defect2 and repivot to q36. The two inactive decorated shell vertices are retained, so lexicographic maximality allows at most one globally decorated support point. Therefore two overlapping singleton supports can share only one point, and that shared point is the unique decorated/shared point of each support. Their remaining two points are clean private weight-zero vertices.

Moreover a singleton support cannot intersect two different support classes at two different support vertices: that would give at least two globally decorated inserted points in its q36 repivot. Hence every connected component of the support-intersection graph is a common-hub sunflower.     (11)

## 6. Component size and component count

A sunflower component cannot contain four supports. If it did, choose one clean private weight-zero petal from each of four supports. Each chosen petal lies outside the other three supports and row closure makes the four points pairwise target-anticomplete, giving an independent4-set.

Hence every intersection component has size at most3.        (12)

There cannot be four distinct components. In each component choose a support and then choose a weight-zero private point of that support. Such a point exists because every singleton support has defect at most2 on three vertices; in a nontrivial component the clean petal is supplied by (11), while in an isolated component at least one support vertex has weight0. Points chosen from different components lie outside one another's supports, and row closure makes them pairwise target-anticomplete. Four components would therefore yield an independent4-set.

Hence there are at most three components.                   (13)

Eight supports split into components of size at most3 and at most three components. Thus the only possible size partition is

> `3+3+2`.                                                   (14)

All three components are nontrivial sunflowers.

## 7. Exact structure of a nontrivial component

Let a component have hub z and let E={z,u,v} be one of its supports. The petals u,v are clean private weight-zero points.

Take another support E' in the same component. Since u lies outside E' and has weight0, row closure gives `e_H(u,E')=0`, so in particular uz is a target nonedge. Similarly vz is a target nonedge.

Thus E has at least two internal target nonedges. Since its total defect is exactly2, equality is forced:

- `m(E)=2`;
- `w_z=0`;
- uv is the unique target edge of E.

Therefore every support in every nontrivial component is a one-edge triple whose hub and petals all have weight0. Row closure then makes distinct components completely target-anticomplete to each other.   (15)

## 8. Final independent4 contradiction

Choose one of the three components. Take its hub z and one petal u; zu is a target nonedge by (15).

Take the hubs z',z'' of the other two components. Different components are target-anticomplete, so every cross pair among `{z,u}` and `{z',z''}` is a target nonedge, and z'z'' is also a target nonedge.

Hence

`{z,u,z',z''}`

is an independent4-set in H, contradiction.

Therefore

> q36 f=2 far-target-K2, c=8, no-d2, A=2 is EMPTY.

Combined with `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION.md`, the remaining no-d2 allowance levels are A=3 and A=4.