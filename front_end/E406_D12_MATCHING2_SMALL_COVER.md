# E406 d=12 final-rise: matching-two small-cover reduction

Status: `PROVED` reduction under the explicit E406 q30->q31 boundary contract. This does not yet close d12 or E406.

Dependencies:

- the paired dense-12 reduction;
- E406 PAIR-13;
- q30 regular-degree restriction;
- complete d2/d3 final-rise closures;
- the d1 matching machinery developed in `E406_D1_*`.

Let p be the q30 pivot and y the q31 pivot in a d12 final rise. The old shell is `{y} union S`, `|S|=12`, with y missing-adjacent to every S-vertex. Put

`K_S = M[S]`, `m=e(K_S)`.

For v in S write

`rho_v=d_{K_S}(v)`,
`g_v=d_R(v)-13`,
`h_v=rho_v+g_v`.

Because every S-vertex has the additional missing edge to y, its shell row weight is `t_v=1+h_v`.

The exact q30 ledger is

`m+G_S=18`,      (D12-BASE)

where `G_S=sum g_v`.

For every K_S-edge uv, PAIR-13 gives

`h_u+h_v>=11`.      (D12-PAIR11)

The previous matching argument gives `nu(K_S) in {2,3}`. We now remove nu=3 and reduce the nu=2 branch.

## 1. A q30 d1 plateau cannot carry a matching-three common block

We first isolate a reusable lemma.

Suppose a q30 pivot repivots across a d1 edge to another q30 pivot, exchanging two degree12 vertices that are target-nonadjacent. Let J be the common 11-point missing graph and put `h=d_J+g` on those 11 vertices.

The plateau ledger is

`e(J)+G_J=18`.

If `nu(J)=3`, let X be the six endpoints of a maximum matching. X is a vertex cover. The three matching edges give

`sum_X h>=33`.

On the other hand

`sum_X h
 <= e(J)+C(6,2)+G_J
 =33`.

Hence equality holds throughout. In particular `J[X]=K6`, contradicting `alpha(R)<=5`.

Therefore a q30 d1 plateau has `nu(J)<=2`.      (D1-PLATEAU-M2)

## 2. nu(K_S)=3 is impossible

Assume `nu(K_S)=3` and fix a maximum matching. Its six endpoints consume h-weight at least33.

The total h-weight is

`sum_S h =2m+G_S=m+18<=36`.

Hence the six unmatched vertices have total h-weight at most3. At least three unmatched vertices therefore have `h=0`.

For such a vertex s,

- `rho_s=0`;
- `g_s=0`;
- its old missing degree is exactly1, namely the edge sy;
- its core row has size1.

Repivot at s. If its unique core support had positive old-core excess, the new q-value would be31, producing a d1 final rise, already proved impossible. Therefore the support has old-core excess0 and the repivot is a q30 d1 plateau.

Since s is a K_S-isolate, the 11-point common missing graph for this plateau is exactly `K_S-s`, and it still contains the original matching of size3.

This contradicts (D1-PLATEAU-M2).

Therefore

`nu(K_S)=2`.      (D12-MATCH2)

## 3. Four-point cover ledger

Fix a maximum matching of size2 and let X be its four endpoints. Then X is a vertex cover of K_S. Put U=S\X, so |U|=8 and U is K_S-independent.

The two matching edges give

`sum_X h>=22`.

Exact cover accounting gives

`sum_X h
 = m+e_{K_S}(X)+G_X
 =18+e_{K_S}(X)-G_U`.

Hence

`e_{K_S}(X)-G_U>=4`.      (COVER)

Since a four-vertex graph has at most six edges, the only possibilities are e=4,5,6 with tiny outside decoration.

A regular U-vertex has shell missing degree `1+d_{K_S}(u)`. The q30 regular-degree restriction therefore gives

`d_{K_S}(u)<=2`.      (U-DEG2)

Consequently, if a regular U-vertex is K_S-adjacent to x in X, PAIR-11 forces `h_x>=9`.

## 4. Six-edge cover is impossible

If e=6, X induces K4.

The three possible outside-decoration levels are:

- `G_U=2`, `sum_X h=22`;
- `G_U=1`, `sum_X h=23`;
- `G_U=0`, `sum_X h=24`.

The first is impossible because summing PAIR-11 over all six K4 edges forces every pair to have sum11, hence all four integer h-values would equal11/2.

For `G_U=1`, the unique possible K4 h-multiset is `(5,6,6,6)`. No regular U-vertex can meet X because every cover h is below9. The single decorated U-vertex can contribute at most four cover edges, whereas the exact cross-edge count is at least5. Contradiction.

For `G_U=0`, the only K4 h-patterns have maximum at most7. Again no regular U-vertex can meet X, while at least five cover-to-U edges are required. Contradiction.

Thus e=6 is empty.

## 5. Five-edge cover

Now X induces `K4-e`.

### 5.1 G_U=1

Here `sum_X h=22`. Let A,B be the nonedge and C,D the other two vertices. Tight perfect matchings force

`h_A=h_B=11-t`,
`h_C=h_D=t`,

with `6<=t<=9`.

If `t<=8`, no regular U-vertex can meet X; the single decorated U-vertex supplies at most four cross edges, while at least six are required.

If `t=9`, every regular U-vertex meeting X must meet both h=9 vertices and has `d_{K_S}(u)=2`. Its old shell missing side is `{y,C,D}` with row weights12,10,10 and three internal missing edges, so the subset charge is29. Hence the repivot has q31, giving a d3 final rise, already impossible.

Thus no regular cross edge exists, again leaving at most four cross edges. Contradiction.

So `G_U=1` is empty.

### 5.2 G_U=0

Here `sum_X h=23`. The only patterns capable of supporting a regular cover-to-U edge are, up to symmetry,

`(3,3,8,9)`, `(2,3,9,9)`, `(2,2,9,10)`.

The first has only one h>=9 vertex. A regular U-vertex would need degree2 in K_S to satisfy PAIR-11, but there is no second eligible cover endpoint. Hence there is no cross edge.

In `(2,3,9,9)`, every regular cross vertex must meet both h=9 vertices, so its shell missing degree is3 and the subset charge is29. This is a d3 final rise, impossible.

Thus the only surviving five-edge cover is

`(2,2,9,10)`.

In this family every regular U-vertex meeting the h=9 vertex must also meet the h=10 vertex and gives a q30 d3 plateau; a U-vertex meeting only the h=10 vertex gives a q30 d2 plateau. No existence is asserted.

Therefore the five-edge cover is reduced to the single exact plateau family

`K4-e with h=(2,2,9,10), G_U=0`.      (D12-E5)

## 6. Four-edge cover

If e=4, (COVER) forces `G_U=0` and `sum_X h=22`.

A four-edge graph on four vertices containing a matching of size2 is, up to isomorphism, either

- `C4`, or
- a paw (triangle plus pendant edge).

These are the only remaining four-edge cover geometries.

## 7. Current d12 frontier

Every d12 final rise is reduced to exactly one of three matching-two small-cover geometries on the old 12-block:

1. `K4-e`, `h=(2,2,9,10)`, `G_U=0`;
2. `C4`, `G_U=0`, `sum_X h=22`;
3. paw, `G_U=0`, `sum_X h=22`.

All six-edge covers and all other five-edge covers are empty.
