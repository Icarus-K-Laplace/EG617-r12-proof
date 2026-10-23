# Global One-Spoke Clique-Forcing Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_M6_PAIR_GEOMETRY_REDUCTION.md`;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- common-S row closure;
- `alpha(H)<=3` and `omega(H)<=11`.

Purpose: close the unique surviving `M=6,b=0` P3-plus-K3 equality geometry by a multi-pivot argument. The contradiction comes from the fact that all one-spoke pivots are forced to form a target clique.

## 1. Equality geometry

Let

- `D={a,b,c}` be the P3 support, with target edges `ac,bc` and target nonedge `ab`;
- `E={e1,e2,e3}` be the target K3 support;
- there are no target D--E edges.

This is exactly Type C from `GLOBAL_D3_A2_M6_PAIR_GEOMETRY_REDUCTION.md`.

The fully-decorated support-to-one-spoke bridge supplies at least

`k>=14`

legal one-spoke pivots `v` outside the owner-support union.

For every such pivot,

- `w_v=1`;
- `v` lies outside D and E.

Hence common-S row closure gives

`e_H(v,D)<=1`,
`e_H(v,E)<=1`.                                              (C1)

## 2. Every one-spoke pivot hits exactly one P3 endpoint

Fix a one-spoke pivot v.

Suppose v were target-nonadjacent to both a and b.

By (C1), v has at most one target neighbour in the K3 E, so at least two vertices of E are target-nonadjacent to v. Choose one such vertex e.

Because D--E is target-anticomplete and ab is a target nonedge,

`{v,a,b,e}`

is a target-independent 4-set, contradicting `alpha(H)<=3`.

Therefore v is target-adjacent to at least one of a,b.

But (C1) says v has at most one target neighbour in all of D. Hence v is target-adjacent to exactly one endpoint from `{a,b}`, and in particular

> v is target-nonadjacent to the P3 center c.                (C2)

Equivalently, in the complement graph

`J=overline(H)`,

v is adjacent to c and to the other P3 endpoint.

## 3. Any two one-spoke pivots are target-adjacent

Take two distinct one-spoke pivots v,w.

By (C1), each of v,w has at most one target neighbour in E. Therefore each has at least two J-neighbours in the 3-set E.

Two subsets of a 3-set of size at least2 must intersect. Hence there exists

`e in E`

such that

`ve,we in E(J)`.                                            (C3)

By (C2), both v and w are J-adjacent to the common P3 center c:

`vc,wc in E(J)`.                                            (C4)

Since D--E is target-anticomplete,

`ce in E(J)`.                                                (C5)

Suppose for contradiction that v and w were target-nonadjacent in H, i.e.

`vw in E(J)`.

Then by (C3)--(C5),

`{v,w,c,e}`

induces a K4 in J.

But `J=overline(H)` and `alpha(H)<=3`, so J is K4-free.

Contradiction.

Therefore every pair of distinct one-spoke pivots is target-adjacent in H.

Hence:

> **One-spoke clique forcing:** the entire one-spoke set induces a target clique in H.   (C6)

## 4. Final contradiction

The bridge gives at least14 distinct one-spoke pivots.

By (C6), H contains a target K14.

But the residual core inherits

`omega(H)<=11`.

Contradiction.

Therefore:

> **P3-plus-K3 equality closure.**
> The unique Type-C `M=6,b=0` geometry is impossible.         (C7)

Combined with the previous Type-A and Type-B exclusions, the entire `M=6,b=0` two-block equality window is empty.

## 5. Reusable abstract form

The proof uses only the following local pattern:

1. a 3-support D contains a distinguished vertex c which every legal one-spoke pivot must miss in the target graph;
2. a target clique E of size3 is target-anticomplete to c;
3. row closure forces every one-spoke pivot to have at most one target neighbour in E;
4. the complement core is K4-free.

Then any two one-spoke pivots share

- c as a complement neighbour;
- at least one common complement neighbour in E;

and these two common neighbours are adjacent in the complement. Thus the one-spoke pivots must form a target clique.

This is a multi-pivot compatibility theorem rather than an owner-multiplicity case argument.