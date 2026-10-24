# R12 Recurrence Decompilation

Status: **STRUCTURAL DECOMPILATION COMPLETE; general quantitative seeds open**.

## 1. What the 1752 nodes really are

The r=12 certificate is not a collection of 1752 unrelated cases. It is the rectangular dynamic-programming table

`(a,n), 1<=a<=12, 1<=n<=145`,

with contextual state

`C_G(a,n) = { induced J<=G : |J|=n, alpha(J)<=a, omega(J)<=11 }`

inside one fixed least-color graph G, under the temporary assumption that no induced `R(4,49)` occurs.

The table stores a lower edge floor `B(a,n)` and an emptiness flag. The only recursive dependencies are:

- `(a,n-1)` through vertex-deletion averaging;
- `(a-1,m)`, `m=n-h-1`, through a minimum-degree pivot;
- already completed maximum-order data for `a-2` and `a-3` through pair/triangle row coverage.

Thus the node count is an implementation artifact. The proof DAG is two-dimensional.

## 2. Seven transition schemas

### T0 — base / seed injection

Base states are `B(a,0)=0`, positive-order `a=0` empty, and `a=1` a clique of order at most 11. The r=12 numerical interface adds order cutoffs 24,37,49 for `a=2,3,4` and five edge floors

`(2,23):131`, `(3,35):210`, `(3,36):234`, `(4,47):284`, `(4,48):308`.

### T1 — vertex deletion averaging

Every edge belongs to exactly `n-2` vertex-deleted subgraphs, hence

`B(a,n) >= ceil(n B(a,n-1)/(n-2))`.

This is the only same-a recursive transition.

### T2 — minimum-degree pivot / core restriction

For a minimum-degree vertex p of degree h, put

`A=N(p)`, `C=J-N[p]`, `m=n-h-1`.

Then `alpha(C)<=a-1`, so the core invokes the already completed state `(a-1,m)`.

### T3 — shell-complement / hereditary-cap forcing

Let `M=bar(J[A])`, `z=e(M)`, `g_v=d_J(v)-h`, and `q=z+sum g_v`. Then

`e(J)=C(h+1,2)+q+e(C)`.

For r=12, `alpha(M)<=10` and

`q>=z>=max(p_10(h), C(h+1,2)-D(h+1), C(h,2)-D(h))`.

This is an algebraic local update, not a recursive graph state.

### T4 — pair coverage / matching forcing

When `h>=11`, M contains an edge. If `M_b` is the maximum nonempty order at independence cap b, an M-edge forces core-row union

`beta=max(0,m-M_(a-2))`.

A matching of t shell-complement edges yields

`q>=t beta-C(2t,2)+p_a(2t)`.

The generic matching guarantee comes from the fact that a maximum matching leaves an independent set in M. The extra r=12 upgrades at shell sizes 12 and 13 are quantitative cap improvements, not a new recurrence schema.

### T5 — triangle dichotomy

If M is triangle-free, Mantel sharpens the matching contribution to

`q>=t beta-t^2`.

If M contains a triangle, its three core rows have union at least

`gamma=max(0,m-M_(a-3))`,

so `q>=gamma-3`, subject to the inherited density test `e(C)+gamma<=D(m+3)`. The node uses the minimum of surviving alternatives after all common q-floors are imposed.

### T6 — cap / emptiness / terminal recognition

For each h,

`L_h=max(ceil(nh/2), B(a-1,m)+C(h+1,2)+Q_h)`.

The node floor is the maximum of the Turan floor `p_a(n)`, deletion floor, explicit seed floor, and `min_h L_h`. A node is empty when a predecessor is empty in the required way, no h-row survives, or the resulting lower floor exceeds the hereditary cap D(n).

These seven schemas account for the entire recurrence logic. No per-node parameterization is needed.

## 3. Why it is finite

The certificate is acyclic for a structural reason:

- T1 lowers n at fixed a;
- T2 lowers a (and also lowers n);
- T4/T5 query only maximum-order data from strictly smaller independence caps;
- T0/T3/T6 are nonrecursive computations.

The strict descent is therefore in the state coordinates, not in the numerical edge floor.

## 4. Outer-stop compression

The 144 r=12 outer rows also have one symbolic form. With anchor degree d and j packed target K12 blocks,

`a=11-j`,
`n=144-d-12j`,
`U(d,j)=870-C(d+1,2)-66j`.

The last expression is the edge budget before subtracting the nonnegative embedding charges. The unique r=12 survivor is

`d=11, j=6, a=5, n=61`, with recurrence floor 397 and budget 408.

At `d=11,j=7`, the coordinates are `a=4,n=49`, which is precisely the temporarily excluded extraction state.

Hence the 144-row table is likewise a two-parameter budget comparison, not 144 distinct structural cases.

## 5. Decompilation verdict

**H1 is achieved at the structural level:** the 1752-node certificate compresses to seven transition schemas plus a two-coordinate outer budget map.

What is r=12-specific is not the termination mechanism. It is the numerical seed package strong enough to make every outer budget comparison fail except the `(5,61)` terminal and the excluded `(4,49)` extraction state.
