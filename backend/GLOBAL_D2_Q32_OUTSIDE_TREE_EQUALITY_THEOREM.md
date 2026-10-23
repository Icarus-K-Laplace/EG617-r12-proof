# Global d=2 q32 Outside-Tree Equality Theorem

Status: `PROVED_ANALYTIC` relative to the retained q32/CORE211 two-hub backend contract.

Purpose: unify the two remaining short-row E334 boundary regimes formerly described separately as `r=2 / allowance=2` and `r=1 / allowance=3`.  They are the same tree-slack equality phenomenon.

## 1. Retained setup

Work in the q32 / CORE211 two-hub branch.  Let the active hub pair be

`S={a,b}`.

For a core vertex `v`, write

`w_v = kappa_v + e_F(v,S)`

and

`W = sum_H w_v = K+t_a+t_b`,

with `K=sum_H kappa=2` in CORE211.

For the outside decorated shell set `Z`, write

- `k=|Z|`,
- `r=e(M[Z])`,
- `G_Z=sum_(z in Z) g_z`.

Let

`b=e_M({a,b})`,
`C=t_a+t_b-b`,

and let the common two-point row allowance be

`A=C-22`.

The retained V6 identities give

`B=r+G_Z=q-C`,

and at q32:

`B=10-A`.

They also give

`G_Z>=6`,
`k<=B-5`,

and, for the repeated-pair owner multiplicity m,

`m>=11-b-k-r`.

The outside graph `M[Z]` is triangle-free.

## 2. The two residual regimes satisfy one equation

The two unresolved short-row regimes are

- `A=2`, `r>=2`;
- `A=3`, `r=1`.

For `A=2`, one has `B=8`.  Since

`G_Z=B-r>=6`,

we get `r<=2`; the residual assumption `r>=2` therefore forces

`r=2`, `G_Z=6`.

Also `k<=3`.  A triangle-free graph with two edges needs at least three vertices, so

`k=3`,

and necessarily

`M[Z]=P3`.

For `A=3`, one has `B=7`; the residual has `r=1`, hence

`G_Z=6`.

Now `k<=2`, while one outside missing edge requires `k>=2`.  Thus

`k=2`,

and

`M[Z]=K2`.

Therefore both residual regimes satisfy the single equality package

> `A+r=4`,
>
> `k=r+1=5-A`,
>
> `G_Z=6`,
>
> `M[Z]` is a tree with r edges on r+1 vertices.                 (T1)

For the actual q32 branch this means exactly `K2` or `P3`.

## 3. Every outside-tree vertex misses both hubs

For `z in Z`, let

`h_z=e_M(z,S)<=2`.

By the retained short-row forcing, no legal row in this branch misses a non-hub point of Z.  Hence

`d_M(z)=d_(M[Z])(z)+h_z`.

The shell degree identity is

`t_z=d_M(z)+g_z`.

Every outside missing edge `uv in M[Z]` obeys the retained edge-12 condition

`t_u+t_v>=12`.                                                 (T2)

### K2 case

The two tree degrees are `1,1` and `g_u+g_v=6`.  Thus (T2) gives

`2+h_u+h_v+6>=12`.

But `h_u+h_v<=4`.  Equality is forced throughout, so

> `h_u=h_v=2`.                                                 (T3)

Both outside vertices miss both hubs, and their tree edge has total shell weight exactly 12.

### P3 case

Let leaves be `z1,z3` and center `z2`.  Summing the two edge-12 inequalities gives

`h_1+2h_2+h_3 + g_1+2g_2+g_3 >=18`.                         (T4)

The hub-missing contribution is at most 8.
Since `g_1+g_2+g_3=6` and every decorated outside point has positive integer decoration, `g_2<=4`, so

`g_1+2g_2+g_3 = 6+g_2 <=10`.

Thus the left-hand side of (T4) is at most18.  Equality is forced.  Consequently

> `h_1=h_2=h_3=2`,                                            (T5)
>
> `(g_1,g_2,g_3)=(1,4,1)` up to reversal.                     (T6)

Again every outside-tree point misses both hubs, and both tree edges have shell weight exactly12.

Hence the two apparent residual branches have one common geometric meaning: the entire outside missing graph is a saturated tree whose vertices all miss both hubs.

## 4. Exact charge budget

Because

`W=K+t_a+t_b`

and

`t_a+t_b=C+b=22+A+b`,

CORE211 gives

`W=2+22+A+b=24+A+b`.

Using `A+r=4`:

> `W=28-r+b <=28`.                                             (T7)

The V6 zero-charge concentration theorem therefore applies.  Its quantitative form gives at least

> `29-W = 1+r-b`                                              (T8)

zero-charge core vertices outside the repeated-support union U.

In particular there is at least one such outside zero, and the retained zero-charge theorem yields

> `alpha(H[U])<=2`.                                           (T9)

Thus both residual regimes enter the same low-independence support-capacity problem.

## 5. Unified owner lower bound

The retained repeated-pair row count gives

`m>=11-b-k-r`.

Substituting `k=r+1` gives

> `m>=10-b-2r`
>
> `  =2A+2-b`.                                                (T10)

Hence

- `A=2,r=2`: `m>=6-b`;
- `A=3,r=1`: `m>=8-b`.

The row-incidence bounds also become one parameterized pair:

> `mu(v)<=r+1=5-A`,                                           (T11)
>
> `mu(u)+mu(v)+1_(uv in E(H)) <= r+3=7-A`.                   (T12)

These hold for support-incidence multiplicity `mu` on the repeated two-point row system.

## 6. Immediate rigidity consequences

### A=3, r=1

Here `mu(v)<=2`.  If two vertices both have multiplicity2 and are target-adjacent, then

`2+2+1>4`,

contradicting (T12).  Thus all multiplicity-2 vertices are pairwise target-nonadjacent.  By `alpha(H[U])<=2`, there are at most two of them.

Since the total support incidence is `2m`, this yields

> `|U|>=2m-2`.                                                 (T13)

Equivalently the support multigraph has maximum degree2 and at most two degree-2 vertices: it is a matching together with at most one exceptional component carrying at most three row edges.

### A=2, r=2

Here `mu(v)<=3`.  Two multiplicity-3 vertices cannot coexist, because even as a target nonedge their sum6 exceeds the bound5 in (T12).  Hence at most one multiplicity-3 vertex exists.

Moreover a multiplicity-3 vertex and any multiplicity-2 vertex must be target-nonadjacent, since

`3+2+1>5`.                                                     (T14)

Thus the two regimes are controlled by the same principle: large incidence multiplicity consumes the entire allowed pair budget and forces target nonadjacency.

## 7. Unified frontier

The two former E334 residuals are therefore not independent cases.  They are one parameterized object:

> **Outside-tree support system.**
> A q32 / CORE211 repeated two-point row system satisfying
>
> - `A+r=4`;
> - outside tree `M[Z]` with `|Z|=r+1`;
> - `G_Z=6`;
> - every outside-tree vertex misses both hubs;
> - `W=28-r+b<=28`;
> - `alpha(H[U])<=2`;
> - owner lower bound `m>=2A+2-b`;
> - incidence bounds (T11)--(T12).

The only actual parameter values are `(A,r)=(2,2)` and `(3,1)`.

The remaining task is a single **Tree-Slack Support Capacity Theorem** showing that no such support system can meet its owner lower bound under the retained hereditary density and repivot contracts.

This theorem does not assert E334 closed.  The d3 bridge from the source-reported V7 eleven-view system to the independently proved simultaneous-owner capacity also remains to be certified.

## 8. Generalization

The derivation uses only

- a fixed hub set;
- the shell identity `B=r+G_Z=q-C`;
- a lower decoration floor;
- a triangle-free outside missing graph;
- edge-weight lower bounds;
- a low total core charge theorem;
- support incidence capacities.

Accordingly the structural statement `allowance + outside-edge-count = constant` and the resulting saturated outside tree are not inherently r=12-specific.  In higher-r analogues, the constants change, but the same mechanism can produce a tree-slack equality regime whose support capacity is the only remaining obstruction.