# q36 f=2 far-target-K2 — c=8 no-d2 A=3 alpha-two disjoint-support lemma

Status: `PROVED` under common-S row closure and an induced support-union independence bound `alpha(H[U])<=2`.

This is a reusable local lemma for the corrected A=3 multiplicity analysis.

## 1. Setup

Let E,T be two distinct disjoint three-point supports in one common-S A=3 class. Assume their union lies in a core set U satisfying

`alpha(H[U])<=2`.                                            (1)

Write `e(E),e(T)` for their internal target-edge counts. Since a three-point set with zero target edges would itself be an independent triple, (1) gives

`e(E),e(T) in {1,2,3}`.

Let

`w(E)=kappa(E)+e_F(S,E)`

be the non-missing part of its defect. Because total support defect is

`Delta(E)=3-e(E)+w(E)<=3`,

we have

- if E is K3: `w(E)<=3`;
- if e(E)=2: `w(E)<=2`;
- if e(E)=1: `w(E)<=1`.                                     (2)

For disjoint common-S supports, row closure gives

`e_H(E,T)<=min(w(E),w(T))`.                                  (3)

## 2. Minimum cross edges forced by alpha-two

We record the minimum target cross-edge count required between E and T so that their six-point union has no independent triple.

### K3 versus K3

No cross edge is forced: each side is already a clique.

Minimum: 0.

### K3 versus a nonclique triple

Let uv be an internal target nonedge of the nonclique support. For every point e of the K3, the triple `{u,v,e}` must contain a target edge. Hence e must meet u or v.

This requires at least one cross edge for each of the three K3 vertices.

Minimum: at least3.

### Two-edge versus two-edge

Let ab be the unique target nonedge in E and uv the unique target nonedge in T.

Every point of T must meet a or b, otherwise it forms an independent triple with ab. Symmetrically every point of E must meet u or v.

Three cross edges cannot suffice: with three edges, the first condition gives every T-vertex positive cross degree and the second gives every E-vertex positive cross degree, so the three edges form a perfect matching. But every T-vertex must be matched into the two-point set `{a,b}`, impossible because the third E-vertex would also need positive degree.

Minimum: at least4.

### Two-edge versus one-edge

Again let ab be the unique nonedge in the two-edge support. In the one-edge support write xy for the unique target edge and z for the isolated point, so its nonedges are zx and zy.

Every T-vertex must meet a or b, requiring at least three cross edges. If exactly three existed, then every E-vertex must also have positive degree in order to hit both nonedges zx,zy. Thus the three cross edges would form a perfect matching.

An E-vertex with only one neighbour in T can hit both zx and zy only when that neighbour is z. Hence all three E-vertices would have to be matched to z, contradiction.

Minimum: at least4.

### One-edge versus one-edge

Write E with isolated point c and edge ab, and T with isolated point z and edge xy.

For each point of T, its neighbourhood in E must hit both nonedges ca,cb; for each point of E, its neighbourhood in T must hit both nonedges zx,zy.

Four cross edges suffice, for example

`cx, cy, az, bz`.

Fewer than four cannot suffice: with at most three cross edges, each of the three vertices on each side must have positive cross degree, so the cross graph is a perfect matching. Any E-vertex of cross degree1 must be matched to z to hit both T-nonedges, forcing all three matching edges to have endpoint z, impossible.

Minimum: 4.

Thus the forced cross-edge table is

| E | T | minimum cross target edges |
|---|---|---:|
| K3 | K3 | 0 |
| K3 | two-edge | 3 |
| K3 | one-edge | 3 |
| two-edge | two-edge | 4 |
| two-edge | one-edge | 4 |
| one-edge | one-edge | 4 |

## 3. Consequence for an A=3 common-S class

Compare the table with (2)--(3).

If at least one of E,T is nonclique, then

- K3/nonclique needs at least3 cross edges, but the nonclique side has w<=2;
- two-edge/two-edge needs4, but each side has w<=2;
- any pair involving a one-edge support has row-closure upper bound at most1 while at least3 or4 edges are required.

Every case contradicts (3).

Therefore:

> if two distinct support classes in an alpha-two A=3 support union are disjoint, then both supports must be target K3s.   (4)

Equivalently:

> every nonclique support class must properly intersect every other distinct support class in that alpha-two union.       (5)

This lemma is independent of the corrected D14 base and can be combined with D14/D17 multiplicity bounds in the remaining A=3 channels.