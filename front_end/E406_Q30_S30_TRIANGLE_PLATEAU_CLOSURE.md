# E406 q30 plateau: uniform closure of the S30 four-triangle contract

Status: `PROVED EMPTY` under the explicit E406 q30 no-q31 plateau contract.

This theorem replaces the historical O=0,...,5 S30 casework. It uses only the modern E406 core-minimum-degree theorem and the exact q30 d=3 plateau equalities.

## 1. Setup

Let R be an E406 T61 object and p a degree-13 pivot with q_p=30. Assume no legal repivot has charge 31.

Suppose the q30 shell contains a regular missing-degree-3 vertex. Exact no-rise equality gives the standard d=3 plateau form. Writing S for the three shell hubs, the missing shell graph is

`M = K_{3,k} + (10-k) K_1`, with `k in {8,9,10}`,

and every active low vertex b has missing neighbourhood exactly S.

For each active b let U_b be its 3-point core support. Exact d=3 plateau equality gives

- `C[U_b]=K3`;
- every vertex of U_b has core degree12;
- U_b is target-anticomplete to S.

Distinct support classes are equal or disjoint, and distinct classes are pairwise target-anticomplete.

Ambient E406 excess and alpha(C)<=4 force exactly four distinct support classes, say

`T1,T2,T3,T4`,

each a K3, pairwise disjoint and pairwise target-anticomplete.

Let

`U=T1 union T2 union T3 union T4`, `H=C\U`.

Then |H|=35. Since e(C)=285, every Ti has three degree-12 vertices and the four Ti are pairwise anticomplete,

- `e(U)=12`;
- `e(U,H)=120`;
- `e(H)=153`;
- `sum_{x in H} epsilon_x=6`, where `epsilon_x=d_C(x)-12>=0`.

Also every x in H is complete to at least one Ti. Otherwise choose one target-nonneighbour of x from each of the four pairwise anticomplete triangles; together with x this is an independent 5-set in C, contradicting alpha(C)<=4.

These are exactly the historical S30 triangle-contract numerics, but the closure below is new and uniform.

## 2. Repivot one support class

Fix i in {1,2,3,4}. Because Ti is an actual support class, choose an active shell vertex b whose core support is Ti.

Repivot at b. Under the present no-q31 hypothesis and the exact d=3 plateau equality, the new pivot again has q=30. Hence its new 47-core is

`C_i=(C\Ti) union S`

and has

`e(C_i)=406-91-30=285`.

The independently proved near-extremal core theorem gives

`delta(C_i)>=12`.

Now take any x in H which is complete to Ti. Write

`r_S(x)=|N_R(x) intersect S|`.

In the old core, `d_C(x)=12+epsilon_x`. Passing from C to C_i removes all three neighbours in Ti and inserts the three shell vertices S. Therefore

`d_{C_i}(x)=12+epsilon_x-3+r_S(x)`.

Since delta(C_i)>=12,

`epsilon_x+r_S(x)>=3`.                                             (1)

Every x in H is complete to at least one of T1,...,T4, so (1) holds for every x in H (choose any complete row class for x and perform that legal plateau repivot).

## 3. Sum contradiction

Summing (1) over the 35 vertices of H gives

`sum_H epsilon_x + sum_H r_S(x) >= 105`.                           (2)

But the first sum is exactly6.

For the second sum, each of the three shell hubs s in S has old core row size10 in the d=3 plateau. Moreover every support triangle Ti is target-anticomplete to S, so none of these 30 hub-to-core incidences lands in U. Consequently all of them land in H and

`sum_H r_S(x)=30`.

Thus the left side of (2) is

`6+30=36`,

contradicting 105.

## 4. Consequence

No E406 q30 no-q31 plateau can contain a regular missing-degree-3 vertex.

A regular missing-degree-10 plateau has the same K3,10 shell and therefore also contains regular degree-3 vertices on the opposite side. Hence it is excluded by the same theorem.

Therefore every surviving q30 no-q31 shell, if any, is forced into the extreme regular-degree set

`{0,1,2,11,12}`.

This theorem closes the entire historical S30 four-triangle plateau contract at once; no O=0,...,5 profile enumeration is needed.