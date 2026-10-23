# q36 f=2, 2K1 far, a_F=0 — c=2 repeated d2 support star reduction

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A0_REDUCTION.md`, inherited D14, and `alpha(F)<=4`.

This treats the c=2 subbranch in which the two low owners share one repeated d2 support D.

## 1. Repeated support and D14

A repeated d2 support has zero defect, hence

- `H[D]=K2`;
- `kappa(D)=0`;
- the repivot has q=35.

Let X be the nine decorated shell vertices, let

`nu=e_M(X)`,
`k=e_F(D,X)`.

The 12-point set `{p} union C union X` spans `66-nu` target edges. Adding D contributes

- one internal D-edge;
- four C--D owner edges;
- k D--X edges.

D14 gives

`66-nu+1+4+k<=69`,

so

> `k<=nu-2`.                                                (1)

The decoration floor gives `nu<=4`, while (1) and k>=0 give `nu>=2`. Therefore

`nu in {2,3,4}`.

## 2. Every D-endpoint must cover M[X]

The far pair F={a,b} is target-nonadjacent and target-anticomplete to X and D.

Fix d in D. If an M[X]-edge x1x2 had both endpoints target-nonadjacent to d, then

`{a,b,d,x1,x2}`

would be an independent5-set, contradicting `alpha(F)<=4`.

Hence the target neighbourhood `N_X(d)` is a vertex cover of M[X]. Writing tau for the vertex-cover number of M[X], each endpoint of D has at least tau neighbours in X. Thus

> `k>=2 tau`.                                               (2)

Since M[X] has nu>0 edges, tau>=1.

Combining (1)--(2),

`2 tau <= nu-2`.

### nu=2

The right side is0, impossible because tau>=1.

### nu=3

The right side is1, again impossible because 2tau>=2.

### nu=4

Now `2tau<=2`, so tau=1. Equality is forced throughout:

- `k=2`;
- each endpoint of D has exactly one target neighbour in X;
- both one-point neighbourhoods are vertex covers of M[X].

A simple graph with four edges and vertex-cover number1 has all four edges incident to one common vertex h. Thus

> `M[X]=K_{1,4} disjoint_union 4K1`.                       (3)

Since each D-endpoint has a unique X-neighbour and that neighbour must cover all four missing edges, both endpoints are target-adjacent exactly to h.

## 3. Exact equality terminal

The only repeated-support c=2 survivor is therefore:

- `|X|=9`;
- `M[X]=K1,4 + 4 isolated vertices`;
- `nu=4`;
- `G=13-nu=9`, so every X-vertex has decoration exactly1;
- the two low owners share one pure K2 support D;
- both D-endpoints are target-adjacent to the star centre h and to no other X-vertex;
- each D-endpoint has global decoration2;
- the q35 repivot retains decoration9 and inserts decoration4, so the new shell has the saturated value `G'=13` and missing-edge count22.

This is a reduction, not yet a closure. The c=2 distinct-support branch and c=1 remain separate.