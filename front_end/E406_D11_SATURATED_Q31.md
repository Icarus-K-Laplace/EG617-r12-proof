# E406 d11: saturated q31 normal form for every m_D=4 residual

Status: `PROVED` under the corrected d11 shielding table. `E406` remains `OPEN`.

Assume a surviving d11 residual has `m_D=4` and, as forced by the one-budget cover reduction, all four D-star leaves share the same 3-row Q in the q31 y-shell.

This includes every corrected A1/B1 row with `m_D=4`.

## 1. Repivoting a D-leaf saturates q31

Pick one D-star leaf d.

The three vertices of Q each have core degree at least12 in the y-core and are adjacent to all four members of the shared leaf class. Hence after repivoting d, each Q-vertex has shell decoration at least3.

Thus the new shell has

    G_d >=9.

But every E406 pivot has q<=31 and z>=22, so `G<=9`. Therefore equality holds throughout:

    q_d=31,
    z_d=22,
    G_d=9.

Each Q-vertex has decoration exactly3, and there is no other decorated shell vertex.

## 2. Exact shell graph

After repivoting d the shell consists of

- the old pivot y;
- the other nine noncentre vertices of D: three remaining star leaves and six D-star isolates;
- the three support vertices Q.

The Q-vertices are adjacent in the target graph to the three remaining shared-class leaves and to no other shell vertex: equality in the decoration bound leaves no room for any additional shell adjacency.

Hence Q is missing to

- y;
- the six D-star isolates.

This gives 21 missing edges between Q and the seven-point set

    R={y}+{six D-isolates}.

Since z=22, there is exactly one additional missing edge inside Q. Therefore

    M = K_{3,7} + e_Q + 3K1,

where `e_Q` is one edge inside the 3-side and the three remaining D-star leaves are M-isolates.

Equivalently the target graph on Q is a P3.

The shell row weights are

    11,11,10 on Q,
    3^7 on R,
    0^3 on the M-isolates.

## 3. All seven vertices of R are q31 pivots

The vertex y is q31 by construction.

Each of the six D-star isolates already has q31 in the y-shell: its missing neighbourhood is exactly `{p,T}`, whose row weights are11 and11, while the complementary shell charge is9. The repivot lower bound gives no loss, so the global q<=31 ceiling forces q=31.

Thus every vertex of R is a q31 pivot.

## 4. Their 3-row supports are anticomplete to Q

Fix `v in R` and let `P_v` be its 3-row in the saturated q31 core.

Repivoting v moves Q into the new core and removes P_v.

For an endpoint q of the unique missing edge inside Q,

- q has old row weight11;
- q has one target neighbour inside Q.

Thus its new-core degree is

    11 + 1 - d(q,P_v) = 12-d(q,P_v).

The new core has minimum degree at least12, so `d(q,P_v)=0`.

For the third Q-vertex the same calculation is

    10 + 2 - d(q,P_v)=12-d(q,P_v),

again forcing zero.

Therefore

    e(Q,P_v)=0

for every `v in R`.

## 5. Each support is P3 or K3

The complementary shell charge outside Q is zero. The exact d3 exchange gives

- if `q_v=30`, then `P_v` is a K3 and has zero core excess;
- if `q_v=31`, then `P_v` is either a P3 with zero core excess or a K3 with total core excess1.

Here every v in R already has q31, so every P_v is exactly

    P3 with epsilon(P_v)=0,

or

    K3 with epsilon(P_v)=1.

## 6. Saturated D14 gives a column cap3

Let W be the closed neighbourhood of the repivoted D-leaf d. It has14 vertices.

Since z=22,

    e(W)=13+(78-22)=69=D(14).

For any core vertex x outside W, the hereditary 15-point cap gives

    d_W(x)<=D(15)-D(14)=72-69=3.

The pivot d is anticomplete to the core, so x is adjacent to at most three shell vertices.

Hence across the seven supports `{P_v:v in R}`, every core vertex occurs in at most three rows.

Thus they form a 3-uniform incidence system with

    7 rows,
    total incidence21,
    column multiplicity<=3.

## 7. The support union has alpha<=3

Let

    U=union_{v in R} P_v.

The two endpoints of the unique missing edge inside Q form a target-independent pair. Q is target-anticomplete to U by Section 4.

If U contained an independent4-set, that pair plus the four U-vertices would form an independent6-set in the T61 parent.

Therefore

    alpha(R[U])<=3.

## 8. Current saturated-design problem

Every d11 residual with `m_D=4` has therefore been reduced to the following finite incidence-design problem:

- seven 3-subsets P_v;
- each induces P3 or K3;
- every column occurs at most3 times;
- their union U has alpha<=3;
- all seven rows are anticomplete to the fixed P3 shell block Q;
- the ambient q31 core has only four total excess units.

No shell-shape freedom remains. The next task is to exclude this 7-row design or classify its unique extremal designs.