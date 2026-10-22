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

## 3. Intersection compression around a pure K10 support

Let `U1` be such a pure K10 support in the q31 284-edge core. Every vertex of U1 has core degree exactly12. Let U2 be any other legal degree-10 support in the same q31 platform.

If `U1 intersect U2` is nonempty, then in fact

`|U1 intersect U2| >=7`.

Proof: every shared vertex x has nine neighbours inside the K10 U1 and hence exactly three available core neighbours outside U1. In U2, x has at least eight support-neighbours. If the intersection had size t, at least `9-t` of those support-neighbours would lie outside U1 even in the `K10-e` case; for t<=5 this already exceeds three. If t=6, at least one of the six shared vertices is not an endpoint of the unique missing edge of a possible K10-e, and that vertex has nine U2-neighbours, of which `10-t=4` lie outside U1, again impossible. Hence t>=7.

Now let `B={b1,b2,b3}` be the 3-side of the shell platform, with Ui the core row of bi and U1 the pure reverse support.

The hereditary 13-point cap applied to `U1 union B` gives

`58 + |U1 intersect U2| + |U1 intersect U3| <=67`,

because U1 is K10, B is K3, and b1 is complete to U1.

Therefore

`|U1 intersect U2| + |U1 intersect U3| <=9`.

Combining with the 0-or-at-least7 intersection gap shows:

- at most one of U2,U3 intersects U1;
- any nonzero intersection has size7,8 or9;
- at least one of U2,U3 is disjoint from U1.

Thus the d=10 E406 coexistence problem is reduced to a sharply constrained three-support geometry: one pure K10 support, one support disjoint from it, and the third either disjoint or overlapping in exactly7--9 vertices.

## 4. Current frontier

For d=3 final-rise platforms, the remaining problem is compatibility of 7--10 three-point supports, each P3/K3-rigid and with at least one pure K3 support.

For d=10 final-rise platforms, the remaining problem is compatibility of exactly three near-K10 supports satisfying the intersection theorem above.

Distances1,2,11,12 remain separate E406 final-rise classes unless the V7 q30 theorem is shown to exclude them.