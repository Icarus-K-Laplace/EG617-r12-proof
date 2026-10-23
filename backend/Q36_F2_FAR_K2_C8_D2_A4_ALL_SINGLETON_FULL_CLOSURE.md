# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 all-singleton full closure

Status: `PROVED` under the far-K2 c8 one-d2 A4 contract, common-S row closure and disjoint-support cross bounds, inherited D14, q36 lexicographic maximality, inherited K4-freeness, `alpha(F)<=4`, the induced `alpha(H[U])<=2` support-union property, and the previously proved elimination of every repeated support.

This closes the final all-singleton sector of A=4.

## 1. Setup

All seven d3 owners share the common missing set

`S=F union {x}`

and every support class is a distinct singleton support. Write

`w_v=kappa_v+e_F(v,S)`.

For every support E,

`Delta(E)=m(E)+sum_(v in E)w_v<=4`.

Let D0 be the unique pure d2 support and choose `v0 in D0`. It is target-anticomplete to U and S, so `alpha(H[U])<=2`.

The two inactive decorated shell vertices are retained by every d3 repivot.

## 2. No singleton support can have defect four

Suppose Q has `Delta(Q)=4`, so Q repivots to q36.

Because the repivot retains the two inactive decorated shell vertices, lexicographic maximality allows at most one globally decorated point of Q. Hence Q contains at least two clean globally-regular private vertices q1,q2. Such vertices have weight0.

There cannot be two q36 supports: choosing one clean weight-zero private vertex from each gives a target nonedge by row closure, and together with `v0,x,f` for any far point f yields an independent5-set.

Thus Q is the unique q36 support and every other support has defect at most3.

### 2.1 At most one support is disjoint from Q

Let E be disjoint from Q.

A clean q1 is target-anticomplete to E. Hence E cannot be nonclique: an internal target nonedge of E together with q1 would form an independent triple in U. So E is a K3.

If E had a zero-weight point e0, row closure would make e0 target-anticomplete to Q. Then `{q1,e0,v0,x,f}` is an independent5-set. Thus all three E-points have positive weight. Since `Delta(E)<=3`, E is a unit-weight K3.

If two distinct supports E,E' were disjoint from Q, q1 would be anticomplete to both. Any target nonedge between their union would form an independent triple with q1, so their union would have to be a target clique. Two distinct K3 support classes have union size at least4, producing a K4. Therefore at most one support is disjoint from Q.

Hence at least five of the remaining six supports intersect Q.                  (1)

### 2.2 The intersecting supports force a defect contradiction

The clean points q1,q2 are private, so every support intersecting Q does so through the same third point z.

For such a support E containing z, q1 lies outside E with weight0. Row closure gives `e_H(q1,E)=0`, so q1z is a target nonedge; similarly q2z is a target nonedge.

Since Q itself lies in U and `alpha(H[U])<=2`, q1q2 must be a target edge. Thus Q has exactly one internal target edge, so `m(Q)=2`. As q1,q2 have weight0 and `Delta(Q)=4`,

`w_z=2`.                                                     (2)

Now let E={z,u,v} be one of the at least five intersecting supports. The zero-weight point q1 is target-anticomplete to E. Hence E cannot contain an internal target nonedge; it is a K3.

Because u lies outside Q but is adjacent to z, row closure against Q gives `w_u>=1`; similarly `w_v>=1`.

Therefore

`Delta(E)=w_z+w_u+w_v>=2+1+1=4`.

But E is not the unique q36 support, so `Delta(E)<=3`, contradiction.

Hence no defect-four singleton support exists. Therefore

> every one of the seven supports satisfies `Delta<=3`.     (3)

## 3. Two supports cannot be disjoint

Assume E,E' are disjoint.

If E is nonclique, an internal target nonedge of E must be covered from every point of E' to avoid an independent triple. Thus `e_H(E,E')>=3`.

For disjoint common-S supports, joint row closure bounds the cross target edges by the non-missing allowance `w(E)`. Since `Delta(E)<=3` and E is nonclique, `w(E)<=2`, contradiction.

Thus E and E' are both K3s.

Suppose E has a zero-weight point z. Then z is target-anticomplete to E'. For every e' in E', the pair z,e' is a target nonedge. If e' were target-nonadjacent to x and to some far point f, `{z,e',v0,x,f}` would be an independent5-set. Therefore every e' is adjacent to x or to both far points.

Since E' is a K3 with total weight at most3, all three vertices must use the minimum one-unit option: each is adjacent to x and has weight1. But then `E' union {x}` is a K4. Contradiction.

Hence neither E nor E' has a zero-weight point. Their K3 weight sums are at most3, so both are exact unit-weight K3s:

`w=(1,1,1)`.                                                 (4)

Row closure makes their cross target graph a matching: every point has cross degree at most1.

Now consider a third support T.

If T had two vertices outside `E union E'`, let t be either such vertex. To avoid an independent triple consisting of t and a target-nonedge pair across E,E', the target neighbourhood of t in `E union E'` must cover the bipartite target-nonedge graph. Since the cross target graph is a matching, that nonedge graph is K3,3 with at most a matching removed and has vertex-cover number3. Hence

`e_H(t,E)+e_H(t,E')>=3`.

Row closure gives each summand at most `w_t`, so `w_t>=2`. Two such outside vertices would contribute weight at least4 to T, contradicting `Delta(T)<=3`.

Thus T contains at least two vertices of `E union E'`.

But T cannot contain two vertices from E: the third E-point lies outside T, has weight1, and is adjacent to both selected E-points, violating row closure. Similarly T cannot contain two vertices from E'.

Therefore T has exactly one point e from E, one point e' from E', and one outside point t.

For each d in `E\{e}`, the target edge de already consumes d's full weight1 against support T, so d is target-anticomplete to e' and t. Likewise each point of `E'\{e'}` is target-anticomplete to e and t.

Among the four cross pairs `(E\{e}) x (E'\{e'})`, the matching cross graph cannot contain all four edges. Choose a target-nonedge d d'. Then d,d' are both target-nonadjacent to t, producing an independent triple.

Contradiction. Thus two disjoint supports cannot exist.

Therefore

> the seven singleton supports are pairwise intersecting.     (5)

## 4. No support can have exactly one target edge

Let E={a,b,c} have sole target edge ab, with c isolated. Since `Delta(E)<=3`, `w(E)<=1`.

As in the repeated one-edge analysis, independent5 forces the exact normal form

- `w_c=1` supplied by the target edge cx;
- `w_a=w_b=0`;
- no far target edge from E.                                  (6)

Every other support intersects E by (5). A zero-weight outside point forbids intersection types containing exactly one of a,b or containing c with one endpoint. Thus every other support intersects E either in `{c}` or in `{a,b}`.

Let n_c,n_ab be the numbers of these two types. Then

`n_c+n_ab=6`,
`O_E=n_c+2n_ab=6+n_ab`.

D14 gives

`3+O_E+e_H(E)<=14`.

With `e_H(E)=1`, `O_E<=10`, hence `n_ab<=4` and therefore

`n_c>=2`.                                                     (7)

But two distinct c-only support classes are impossible. For E_i={c,u_i,v_i}, zero-weight a is target-anticomplete to the petals. Since ac is a target nonedge, alpha-two forces c to be target-adjacent to both petals of every c-only support.

For two distinct c-only supports, alpha-two with a forces the two petal pairs to be joined by a complete K2,2. A petal then has at least three target edges into the other support: the edge to c plus the two petal-cross edges. Row closure forces petal weight at least3, making its support defect exceed3.

Thus `n_c<=1`, contradicting (7).

Hence one-edge supports are impossible.                     (8)

## 5. No support can have exactly two target edges

Let E={a,b,c} be the path with edges ac,bc and unique nonedge ab. Since `Delta(E)<=3`, `w(E)<=2`.

All six other supports intersect E by (5).

Let n1,n2 be the counts of one-point and two-point intersections. Then

`n1+n2=6`,
`O_E=n1+2n2=6+n2`.

D14 gives

`3+O_E+e_F(F,E)+2<=14`,

so `O_E<=9` and therefore

> `n2<=3`, hence `n1>=3`.                                   (9)

We show that every weight pattern permits at most two one-point support classes, contradiction.

### 5.1 If w_c=0

A one-point support anchored at a or b is impossible because c lies outside and is adjacent to the anchor but has weight0.

A c-anchor requires `w_a,w_b>=1`; with `w(E)<=2` this forces `(w_a,w_b,w_c)=(1,1,0)`. But for a c-anchor support, the existing edges ac,bc consume the full row-closure budgets of a,b, making them target-anticomplete to both private petals. Since ab is a target nonedge, an independent triple results.

Thus no one-point support exists.

### 5.2 If `(w_a,w_b,w_c)=(0,0,1)`

One-point supports may be anchored only at a or b. At a fixed anchor there is at most one class: the opposite zero-weight endpoint is anticomplete to all petals and alpha-two forces a complete K2,2 petal cross graph between two distinct classes, making each petal weight at least3.

Classes at a and b cannot coexist. The center c has weight1 and its edge to each anchor consumes its row-closure budget, so c is target-anticomplete to all petals. Alpha-two then forces a complete K2,2 cross graph between the two endpoint classes; the resulting petal weights make either a nonclique support exceed allowance3 or a K3 support have defect at least4.

Hence at most one one-point class exists.

### 5.3 If `(w_a,w_b,w_c)=(0,0,2)`

Again there is at most one class at each endpoint by the zero opposite endpoint argument. Thus at most two one-point classes exist.

### 5.4 If `(w_a,w_b,w_c)=(1,0,1)` or its symmetric pattern

At a fixed endpoint there is at most one class. Moreover the center's weight1 is exhausted by its edge to either anchor, so if classes at both endpoints coexisted, c would be anticomplete to both petal pairs and alpha-two would force a complete K2,2 cross graph. The support at the positive endpoint then has the shared endpoint weight1 plus two petals of weight at least2, exceeding allowance3.

Thus at most one one-point class exists.

In every case the number of one-point supports is at most2, contradicting `n1>=3` from (9).

Therefore two-edge supports are impossible.                 (10)

## 6. Hence every support is a target K3

By (8)--(10), all seven pairwise-intersecting singleton supports are target K3s. Their total weight is at most3.

## 7. Two supports cannot intersect in two points

Suppose

`E={a,b,c}`, `E'={a,b,d}`

share the pair {a,b}.

Because both supports are K3s, if cd were a target edge then {a,b,c,d} would be a K4. Thus cd is a target nonedge.

Point c lies outside E' but is target-adjacent to both a,b, so row closure gives `w_c>=2`. Similarly `w_d>=2`.

Since both K3 support weights are at most3,

> `w_a+w_b<=1`.                                              (11)

Consider any other support T. By pairwise intersection, T meets both E and E'. If T contained neither a nor b, then it would have to contain both c and d, but cd is a target nonedge and T is a K3. Hence every other support contains a or b.

No third support can contain both a,b: its new petal together with c,d would give three pairwise target-nonadjacent petals (K4-freeness makes the petals of three K3s on common edge {a,b} pairwise nonadjacent), contradicting alpha-two.

Now consider an a-only support T={a,u,v}. Point b lies outside T and the target edge ba consumes row-closure budget `w_b<=1`; consequently b is target-anticomplete to u,v whenever `w_b=1`, while if `w_b=0` the support is impossible already. Two distinct a-only supports would then force a complete K2,2 petal cross graph to avoid an independent triple with b, which gives petal weight at least3 and violates the K3 weight bound. Hence there is at most one a-only support. Symmetrically there is at most one b-only support.

But five supports remain besides E,E', while at most two can be accommodated. Contradiction.

Therefore

> every two distinct supports intersect in exactly one point. (12)

## 8. No core point belongs to three supports

Suppose a core point z belongs to three supports

`E_i={z} union P_i`, i=1,2,3.

By (12), the petal pairs P_i are pairwise disjoint.

For a petal u in P_i and j != i, support E_j contains z and u lies outside it. The target edge uz therefore gives

`w_u>=1`.                                                     (13)

Each K3 support has total weight at most3, so `w_z<=1`.

If `w_z=1`, both petals in every P_i have weight exactly1. For a petal u in P_i, its edge to z exhausts its row-closure budget against every other E_j, so u is target-anticomplete to P_j. Choosing one petal from each P_i gives an independent triple.

If `w_z=0`, each petal pair has two positive integer weights summing at most3, so each P_i contains at least one unit-weight petal p_i. Again the edge p_i z exhausts its row-closure budget against the other z-supports, and the three selected unit petals are pairwise target-nonadjacent.

Both cases contradict `alpha(H[U])<=2`.

Therefore

> every core point belongs to at most two of the seven supports.   (14)

## 9. Final incidence contradiction

The support family is pairwise intersecting and linear by (12). A given support has only three vertices. By (14), each of those vertices can be shared with at most one other support.

Hence one support can intersect at most three other supports.

But in a family of seven pairwise-intersecting supports it must intersect the other six.

Contradiction.

Therefore the all-singleton A=4 support system is EMPTY.