# Potential Function for the Front Recurrence

Status: **PROVED for recurrence termination; edge-based potentials rejected as primary measures**.

## 1. The correct well-founded potential

For a symbolic recurrence state `(a,n)` with `0<=a<=r` and `0<=n<=r^2+1`, define

`Phi_r(a,n)=(r^2+2)a+n`.

Every genuine recursive dependency strictly decreases `Phi_r`:

1. vertex-deletion averaging uses `(a,n-1)`, so `Delta Phi=1`;
2. a minimum-degree pivot uses `(a-1,m)` with `m=n-h-1<n`, so

`Phi_r(a,n)-Phi_r(a-1,m)=(r^2+2)+(n-m)>0`;

3. pair/triangle coverage uses only maximum-order data from caps `a-2` and `a-3`, already completed at strictly smaller potential.

All other row operations are nonrecursive finite arithmetic.

Therefore there is no infinite recurrence chain. This is a literal natural-number potential, stronger than merely saying the table is evaluated lexicographically.

Equivalent formulation: `(a,n)` ordered lexicographically is well-founded on the finite state rectangle.

## 2. Why the proposed edge potentials are not the main invariant

The following quantities were tested conceptually against the recurrence transitions:

- `e-lambda_r n`;
- `e-D_r(n)`;
- positive degree excess `sum_v (d(v)-r)_+`;
- convex degree energy `sum_v C(d(v)-r+c,2)`.

None is needed for termination, and none is uniformly forced to decrease under both vertex deletion and pivot/core restriction. In particular:

- deleting a vertex changes both the edge count and the cap in a degree-dependent way;
- passing to the pivot core can lower n sharply while increasing normalized density/slack;
- the DP floor itself may remain equal across adjacent nodes because a Turan floor, seed, or previously active row remains dominant.

Thus a claim that `e-D_r(n)` or a degree energy is a strictly decreasing recurrence potential would be false without additional hypotheses.

## 3. Plateau/equality cases

There are two distinct notions of plateau:

### Numerical plateau

`B_r(a,n)` can inherit exactly the same active mechanism over several n-values or can meet `D_r(n)` at equality. This does not create a recurrence loop because the dependency coordinate has already decreased.

### Structural equality

Turan, matching, Mantel, pair-cover, or triangle-cover inequalities may all be tight. Such equalities can create rigid terminal geometries, but they do not affect well-foundedness. They should be classified only after the recurrence has reduced the outer state to a small terminal family.

Hence the correct proof architecture is:

`well-founded coordinate descent` first,

then `equality/plateau rigidity` only for the surviving terminal cone.

## 4. Optional outer potential

The outer `(d,j)` table is not itself a recursive process; it is a set of budget comparisons. If one implements an extraction algorithm that repeatedly increases the packed-block count j while keeping an anchor, the deficiency

`Theta_r(d,j)=(r-1-d)+(r-5-j)_+`

decreases whenever d is promoted or another block is packed before the extraction threshold. However no theorem in this workstream currently proves that every legal outer move decreases Theta. It is therefore recorded only as a candidate algorithmic potential, not as a proved general-r extraction invariant.

## 5. Verdict

The requested strict potential exists and is simple:

`Phi_r=(r^2+2)a+n`.

It explains the finiteness of the entire 1752-node recurrence. The remaining difficulty is quantitative: proving that the terminal budget comparisons leave only the `4r+1` extraction state and the `5r+1` terminal, not proving termination itself.
