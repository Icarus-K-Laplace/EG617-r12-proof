# K4,9 G=2 split plateau — 17-point core reduction

Status: `PROVED REDUCTION`.

This continues `K49_PLATEAU_INDEPENDENT_REDUCTION.md` and studies its unique surviving residual.

## Setup

The shell is `M=K4,9` with decoration split `1+1` on two vertices of the four-side. The other two four-side vertices are regular plateau pivots with disjoint pure K9 supports `D1,D2` in the 211-edge 35-core H.

Every vertex of D1 and D2:

- has H-degree12;
- has global degree13;
- has exactly one shell target neighbour, namely the corresponding regular four-side pivot.

Let

`L=H\(D1 union D2)`, `|L|=17`,

and put

`B=e_H(D1,D2)`.

## 1. Exact core ledger

Each vertex in Di has eight neighbours inside its own K9 and total H-degree12. Therefore its external H-degree is four.

Summing over either K9 gives

`e_H(Di,L)=36-B`.

The 211-edge core identity gives

`211 = 36+36+B + (36-B)+(36-B)+e(H[L])`,

hence

`e(H[L])=67+B`.

The hereditary 17-point cap gives B<=14, but the compatibility argument below improves this.

## 2. Cross-nonedge degree-sum theorem

Take `u in D1`, `v in D2` with `uv` a target nonedge in H. Let `d_B(u),d_B(v)` be their degrees in the bipartite cross graph H[D1,D2].

The number of L-neighbours is

`d_L(u)=4-d_B(u)`,
`d_L(v)=4-d_B(v)`.

Let W be the set of L-vertices nonadjacent to both u and v. Then

`|W| >= 17-(d_L(u)+d_L(v)) >= 9+d_B(u)+d_B(v)`.

Because H has independence number at most3, W cannot contain a target nonedge: otherwise u,v together with that nonedge would be an independent4-set in H. Thus W is a clique.

Since `omega(H)<=11`,

`9+d_B(u)+d_B(v) <=11`.

Therefore

`uv notin E(H) => d_B(u)+d_B(v)<=2`.   (K49-cross)

## 3. Consequence: B<=10

If some cross-graph vertex has degree at least3, (K49-cross) implies it has no nonneighbour on the opposite side, hence it is universal of degree9.

There cannot be two universal vertices on one side because that already gives at least18 cross edges, while the hereditary 18-point cap gives B<=15 (and the 17-point ledger gives B<=14).

With one universal vertex, every other same-side vertex has degree at most1. Moreover at most one such extra degree-1 edge can exist: two extras would create an opposite vertex of degree at least2 that is nonadjacent to another degree-1 or degree-0 same-side vertex, violating (K49-cross). Hence the universal case has B=9 or10.

If no universal vertex exists, all degrees are at most2. Any degree-2 vertex can have nonneighbours only of degree0. This prevents two separate positive degree-2 components; the extremal alternative is a matching, with at most9 edges. Hence again B<=9.

Thus uniformly

`B<=10`.

## 4. Final residual interface

The unique K4,9 split-decoration residual therefore satisfies

`0<=B<=10`,

`e(H[L])=67+B`,

`e(D1,L)=e(D2,L)=36-B`.

In particular

`67<=e(H[L])<=77`,

and each K9 support sends at least26 target edges into the 17-point remainder.

All shell rows other than the two regular four-side rows lie in L: the two decorated four-side rows have size10 each and the nine-side has nine rows of size4.

This is now a finite 17-point core-compatibility problem rather than a free K4,9 shell.
