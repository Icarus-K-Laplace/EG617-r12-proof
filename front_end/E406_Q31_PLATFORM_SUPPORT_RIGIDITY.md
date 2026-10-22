# E406 q31 platform support rigidity

Status: `PROVED` for the platform families identified in `E406_D3_D10_FINAL_RISE_NORMAL_FORM.md`. E406 remains `OPEN`.

This note studies legal regular repivots *inside* the q31 platform states reached by a q30 -> q31 final rise.

## 1. Degree-3 platform rows

Consider any q31 platform whose missing graph has a 3-point cover D and an independent 10-side B, as in the d=3 final-rise families. For every active regular `b in B` with missing degree3,

`N_M(b)=D`,

and the exact subset charge is

`t(D)-e_M(D)=31`.

Let `U=N_C(b)` be the 3-point core row of b in the q31 284-edge core. The exact repivot identity gives

`q_b-31 = 2 + eps_C(U) - e_C(U) + e_F(D,U)`.

Since q31 is globally maximal,

`e_C(U) >= 2 + eps_C(U) + e_F(D,U)`.

Thus every such 3-row is one of only two structural types:

- `P3` on three core-degree12 vertices and anticomplete to D;
- `K3`, with `eps_C(U)+e_F(D,U)<=1`.

In particular, if repivoting b drops back to q30, then

`q_b-31=-1`,

so necessarily

`C[U]=K3`, `eps_C(U)=0`, `e_F(D,U)=0`.

Hence every reverse edge q31 -> q30 uses a **pure K3 support** consisting entirely of core-degree12 vertices and anticomplete to the 3-point shell cover.

The seven d=3 final-rise platforms therefore carry between7 and10 legal degree-3 support rows, at least one of which is pure K3.

## 2. Degree-10 platform rows

Consider either d=10 q31 platform. The missing graph has an independent 3-side B and a 10-side D. For every regular `b in B`,

`N_M(b)=D`,

and again

`t(D)-e_M(D)=31`.

Let `U=N_C(b)` be the 10-point core row. Exact repivot gives

`q_b-31 = 44 + eps_C(U) - e_C(U) + e_F(D,U)`.

Maximality implies

`e_C(U) >= 44 + eps_C(U) + e_F(D,U)`.

Therefore every 10-row is either

- `K10-e` with `eps_C(U)=0` and `e_F(D,U)=0`, or
- `K10` with `eps_C(U)+e_F(D,U)<=1`.

If repivoting b is the reverse edge to q30, then

`q_b-31=-1`,

and necessarily

`C[U]=K10`, `eps_C(U)=0`, `e_F(D,U)=0`.

Thus every reverse q31 -> q30 edge uses a **pure K10 support** of ten core-degree12 vertices, anticomplete to the 10-point shell side.

## 3. A pure K10 reverse support is disjoint from the other two supports

Let `U1` be the pure K10 support of the reverse q31 -> q30 edge. Every vertex of U1 has core degree exactly12. Let U2 be any other legal degree-10 support.

### 3.1 Nonzero intersection would have size at least7

If `U1 intersect U2` is nonempty, put `t=|U1 intersect U2|`.

Every shared vertex x has nine neighbours inside U1 and therefore exactly three available core-neighbour slots outside U1.

Inside U2 it has at least eight support-neighbours. For `t<=5`, even an endpoint of the unique missing edge of a possible `K10-e` support would require at least `9-t>=4` neighbours outside U1, impossible.

For `t=6`, among the six shared vertices at least one is not an endpoint of the unique missing edge of U2; that vertex has nine U2-neighbours, of which `10-t=4` lie outside U1, again impossible.

Hence

`U1 intersect U2 != empty => t>=7`.   (I)

The same applies to U3.

### 3.2 The 13-point cap permits at most one such overlap

Let `B={b1,b2,b3}` be the 3-side of the shell platform, with Ui the core row of bi and U1 the pure reverse support.

The induced 13-set `U1 union B` contains

- 45 edges inside U1;
- 3 edges inside B;
- 10 edges from b1 to U1;
- `|U1 intersect U2|` edges from b2 to U1;
- `|U1 intersect U3|` edges from b3 to U1.

The hereditary cap `D(13)=67` therefore gives

`|U1 intersect U2| + |U1 intersect U3| <=9`.   (II)

By (I), if one overlap is nonzero the other is zero.

### 3.3 The 14-point cap kills even the single-overlap possibility

Assume without loss that

`t=|U1 intersect U2| in {7,8,9}`

and `U1 intersect U3=empty`.

Choose `x in U2\U1`, which exists because t<=9.

The 13-set `U1 union B` already has exactly at least

`58+t`

edges.

Since `C[U2]` is `K10` or `K10-e`, the vertex x is adjacent to at least `t-1` vertices of `U1 intersect U2`; it is also adjacent to its shell pivot b2. Hence x adds at least

`t`

edges to that 13-set.

Thus the 14-set `U1 union B union {x}` has at least

`58+2t >=72`

edges, contradicting the hereditary cap `D(14)=69`.

Therefore no nonzero overlap is possible:

`U1 intersect U2 = U1 intersect U3 = empty`.

So the d=10 coexistence geometry has the exact form:

- one pure K10 reverse support U1;
- two near-K10 supports U2,U3 lying completely in the remaining37 core vertices.

As a useful exact by-product, deleting U1 from the 284-edge core leaves a 37-vertex induced graph with

`284 - 45 - 30 = 209`

edges, because every vertex of U1 has degree12 and U1 has45 internal edges.

## 4. Current frontier

For d=3 final-rise platforms, the remaining problem is compatibility of 7--10 three-point supports, each P3/K3-rigid and with at least one pure K3 support.

For d=10 final-rise platforms, the remaining problem is compatibility of two near-K10 supports inside a 37-vertex, 209-edge remainder, disjoint from the pure reverse K10 support.

Distances1,2,11,12 remain separate E406 final-rise classes unless the V7 q30 theorem is shown to exclude them.