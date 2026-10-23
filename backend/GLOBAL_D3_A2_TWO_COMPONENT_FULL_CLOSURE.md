# Global d=3 A2 Two-Component Full Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_TWO_COMPONENT_EXACT_REDUCTION.md`;
- `GLOBAL_D3_A2_INTERSECTING_COMPONENT_CAPACITY.md`;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- zero-charge incidence signatures;
- common-S row closure;
- inherited cap `D(15)=72`;
- `alpha(H)<=3`, `W<=36`.

Purpose: exclude the exact two-component weighted skeleton `(2,2)|(3,2)` without owner-case enumeration. The proof uses only the hub/pair component types, charge barriers and the global one-spoke bridge.

## 1. Exact two-component skeleton

By `GLOBAL_D3_A2_TWO_COMPONENT_EXACT_REDUCTION.md`, any two-component residual consists of exactly four support classes:

- component A carries four owners with class multiplicities `(2,2)`;
- component B carries five owners with class multiplicities `(3,2)`;
- every support in A is disjoint from every support in B;
- each component has exactly two intersecting support classes.

A two-class intersecting component has a global zero core of size one or two:

- **hub type:** common zero hub;
- **pair type:** common zero target edge.

Thus only hub/pair type combinations remain.

## 2. The five-owner component cannot be pair type

Assume component B is a common-pair family with common zero target edge

`Y={y1,y2}`

and private petals b1,b2.

Its support union has four vertices. The K11 dense base together with the five owners gives15 owner-support edges. Applying `D(15)=72`:

`55 + 15 + 1 + w(b1)+w(b2) <=72`,

where the `1` is the common target edge and `w(bi)=e_H(bi,Y)` by the common-pair defect identity.

Hence

> `w(b1)+w(b2)<=1`.                                         (C1)

Therefore at least one private petal, say b0, has zero charge.

Choose any common-core vertex y in Y. Since b0 has zero charge and lies in a support containing Y,

`yb0`

is a target nonedge.

Both y and b0 are zero-charge vertices lying outside every support of component A. Common-S row closure therefore makes each of them target-anticomplete to the entire support union of A.

Component A, whether pair type or hub type, contains an independent private pair:

- pair type: its two private petals are target-nonadjacent;
- hub type: choose one petal from each of its two private K2 blocks, which are cross-anticomplete.

Let a,a' be such a pair. Then

`{y,b0,a,a'}`

is an independent4-set in H, contradiction.

Therefore:

> the five-owner component B must be hub type.                (C2)

## 3. Four-owner pair + five-owner hub is impossible by a three-block charge barrier

Assume A is pair type and B is hub type.

Let X be the common zero target-edge pair of A.

Let P1,P2 be the two private K2 blocks of the two hub supports in B. The intersecting-component theorem gives

- each P_i induces a target K2;
- P1 and P2 are target-anticomplete.

The zero pair X lies outside every B-support, so zero-charge row closure makes X target-anticomplete to P1 union P2.

Hence

> `X,P1,P2`

are three target K2 blocks which are pairwise cross-anticomplete.   (C3)

Let U be the full support union of the two components. It has

`|U|=4+5=9`.

Take any core vertex z outside U. If z were not target-complete to any of the three K2 blocks in (C3), choose from each block one target-nonneighbour of z. The three chosen vertices are pairwise target-nonadjacent, so together with z they form an independent4-set.

Thus z is target-complete to at least one of X,P1,P2.

Because z lies outside all supports, whichever block it is complete to lies inside some support D with z outside D. Row closure gives

`e_H(z,D)<=w_z`.

Completeness to the K2 already contributes two target neighbours, hence

> `w_z>=2`.                                                   (C4)

There are `35-9=26` core vertices outside U. Therefore

`W>=2*26=52`,

contradicting `W<=36`.

Hence pair/hub is impossible.

## 4. Hub + hub: a Z-type support is impossible

It remains to consider both components hub type.

Let x,y be their distinct common zero hubs. These are two distinct zero-charge incidence signatures.

A Z-type hub support contains one secondary zero private petal. Such a petal has a third zero signature. Hence across both components there can be at most one Z-type support; a second would create a fourth distinct zero signature.

Assume one Z-type exists in component A. Let u be its zero private petal. Let P be the private K2 block of the other support in A. Since there is no second Z-type, P belongs to an H-type support, so both vertices of P have charge1.

Choose p in P.

Let Q1,Q2 be the two private K2 blocks of component B. Blocks Q1,Q2 are target-anticomplete.

The zero vertex u lies outside all B-supports, so u is target-anticomplete to Q1 union Q2.

The charge-one vertex p is target-nonadjacent to the B-hub y. Row closure against each B-support therefore lets p have at most one target neighbour in each Q_i. Hence choose

`q_i in Q_i`

target-nonadjacent to p for i=1,2.

Now

- u and p are in distinct private blocks of the same hub family, hence target-nonadjacent;
- u is target-nonadjacent to q1,q2;
- p is target-nonadjacent to q1,q2 by choice;
- q1q2 is a target nonedge.

Thus

`{u,p,q1,q2}`

is independent4, contradiction.

Therefore:

> no Z-type support exists in the hub/hub regime.              (C5)

All four supports are H-type target K3s.

## 5. Hub + hub forces many one-spoke pivots

Each H-type support has two private unit-charge petals.

Thus the full support union U consists of

- two zero hubs;
- eight private charge-one vertices.

Hence

`|U|=10`,
`W_U=8`.                                                     (C6)

The four private K2 blocks have:

- no target edges between the two blocks belonging to the same component;
- between opposite-component blocks, row closure permits at most a matching, because each private vertex has charge1 and is target-nonadjacent to the opposite hub.

Therefore the private eight-vertex graph has at most

`4 + 4*2 =12`

target edges: four internal K2 edges plus at most two edges in each of four cross block pairs.

We claim it contains an independent triple.

If its independence number were at most2, its complement would be triangle-free on eight vertices. Mantel gives at most16 complement edges, so the target graph would have at least12 edges. Equality would be forced throughout. The complement would be `K_(4,4)`, hence the target graph would be `K4 union K4`.

Each private K2 block must lie inside one target K4. Since the two A-blocks are cross-anticomplete they must lie in different K4s; the two B-blocks must likewise lie in different K4s. Therefore some A-block and B-block lie in the same K4, forcing all four cross target edges between those two K2s, contradicting the row-closure matching bound of at most2.

Hence

> `alpha(H[U])=3`.                                           (C7)

The global fully-decorated support-to-one-spoke theorem now applies:

`k >= 32-2|U|+W_U =32-20+8=20`.                              (C8)

So at least20 legal one-spoke pivots exist outside U.

## 6. But hub + hub admits no one-spoke pivot

Let v be any putative one-spoke pivot. It has common-S charge

`w_v=1`

and lies outside all four supports.

Let A1,A2 be the two private K2 blocks around hub x, and B1,B2 the two around hub y.

For every choices `b1 in B1`, `b2 in B2`, the triple

`{x,b1,b2}`

is target-independent:

- x is zero-charge and lies outside both B-supports, so it is target-anticomplete to B1 union B2;
- B1 and B2 are cross-anticomplete.

Suppose v were target-nonadjacent to x. To avoid an independent4, v would have to meet every pair `b1,b2` in target adjacency.

But row closure against each B-support allows v at most one target neighbour in each two-point private block (and if v sees the hub y, it allows none). A set containing at most one vertex from B1 and at most one from B2 cannot meet all four pairs in `B1 x B2`.

Contradiction.

Thus

> `vx` is a target edge.                                     (C9)

By symmetry

> `vy` is a target edge.                                     (C10)

These two hub edges consume the full row-closure allowance of v in every A- and B-support respectively. Hence v is target-anticomplete to all eight private vertices.

But Section5 proved that the private eight-vertex graph contains an independent triple. Together with v this gives an independent4-set.

Contradiction.

Thus the hub/hub regime contains no one-spoke pivot, contradicting the at-least20 pivots forced by (C8).

Therefore hub/hub is impossible.

## 7. Full two-component closure

Section2 forces the five-owner component to be hub type. Sections3 and4--6 exclude pair/hub and hub/hub respectively.

Hence:

> **Two-component full closure.**
> The final q32 fully-decorated nine-owner A2 support system cannot have two connected components in its support-intersection graph.   (C11)

Combining with the previous reductions, every remaining nine-owner survivor must have

- a connected support-intersection graph;
- support matching number exactly2;
- maximal disjoint-pair owner weight `M<=5`.

This is now the unique fully-decorated N=9 structural regime.