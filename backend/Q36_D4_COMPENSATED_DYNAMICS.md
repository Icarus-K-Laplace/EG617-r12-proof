# q36 compensated d4 branch — finite support dynamics

Status: `PROVED REDUCTION` under the standard legal backend contract and `Q36_COMPENSATED_K49_NORMAL_FORM.md`.

The q36 d9 branch is closed separately. This file gives the current exact interface for the remaining q36 d4 family.

## 1. Shell normal form

Let p be a q36 maximal pivot and let y be a regular d4 zero-defect shell vertex.

The compensated normal-form theorem gives a partition

`A=S sqcup U`,

where

- `|S|=4`, `|U|=9` and `y in U`;
- S and U are target cliques;
- every vertex of U is globally regular;
- all four vertices of S are globally decorated;
- the only variable shell edges are target cross edges between S and `U\{y}`;
- if C is this target cross graph, every s in S satisfies `g_s=d_C(s)`;
- every row of C on S is nonempty;
- `G=e(C)` and `4<=G<=14`.

For `u in U`, let

`c_u=d_C(u)`

and let `D_u=N_H(u)`. Then u is regular and

`|D_u|=d_M(u)=4-c_u`.                                      (1)

Call u a zero column if `c_u=0`. The original y is a zero column.

## 2. Zero-column supports

For every zero column u,

- `|D_u|=4`;
- H[D_u]=K4;
- every vertex of D_u has H-degree12;
- `e_F(S,D_u)=0`.

All zero columns have the same missing set S. The common-S theorem at q36 therefore gives:

> two zero-column supports are either equal or disjoint; distinct supports are target-anticomplete.

Since `alpha(H)<=3`, there are at most three distinct zero-column support classes. Otherwise one vertex from each of four pairwise-antocomplete supports would be an independent4-set in H.

Write the distinct classes as

`D_1,...,D_k`, `k<=3`,

with multiplicities

`m_1+...+m_k=n_0`,

where `n_0` is the number of zero columns.

Let

`a=9-n_0`

be the number of active columns.

## 3. Multiplicity cap from D14

Fix a zero column u in class i and repivot at u.

A vertex v in D_i has old-core degree12. Its old shell neighbours are

- all `m_i` zero columns in the same support class;
- any active columns w for which `v in D_w`;
- no vertex of S.

Hence, after repivoting u, its global decoration is

`g_v=(m_i-1)+#{active w : v in D_w}`.

Put

`J_i=sum_(active w)|D_w intersect D_i|`.

The new q36 shell decoration total on the four-side D_i is therefore exactly

`G_i'=4(m_i-1)+J_i`.                                       (2)

Every q36 shell obeys the inherited 14-point cap `G_i'<=14`. Thus

`m_i<=4`,                                                   (3)

and more precisely

`J_i<=18-4m_i`.                                             (4)

So the zero-column multiplicity partition has

- at most3 parts;
- every part at most4.

## 4. Singleton classes must be covered

If `m_i=1`, then (2) gives `G_i'=J_i`.

The u-repivot is again a q36 d4 compensated shell. By the all-or-nothing theorem, the new four-side D_i cannot be partially decorated.

- if `J_i=0`, the new shell is exact K4,9 with G=0, already closed;
- if `J_i>0`, all four vertices of D_i must be decorated.

Therefore every singleton support class satisfies

`D_i subseteq union_(active w) D_w`.                        (5)

In particular `J_i>=4` for a singleton class.

## 5. Tertiary zero-column maximality

Among q36 pivots with maximal shell-decoration count `tau=4`, choose p so that the number `n_0` of zero columns is maximal.

Every zero-column repivot stays at q36. Because exact K4,9 G=0 and partial-decoration d4 shells are already impossible, its new four-side is again fully decorated, so the new pivot also has tau=4. Thus tertiary maximality applies to every zero-column repivot.

For class i let

`b_i=#{active columns w : D_w intersect D_i != empty}`.

After repivoting a zero column u in class i, the new zero columns are exactly

1. the old pivot p;
2. the `n_0-m_i` zero columns belonging to the other support classes;
3. the active columns whose supports avoid D_i.

Hence

`n_0'=1+(n_0-m_i)+(a-b_i)=10-m_i-b_i`.

Maximality `n_0'<=n_0=9-a` gives

> `b_i>=a+1-m_i`.                                          (6)

This is a genuine joint-incidence constraint, not a scalar shell count.

## 6. Global incidence inequality

For an active column w, (1) gives

`|D_w|=4-c_w`,

where `c_w>=1` is its target cross-degree. Summing over active columns,

`sum_(active w)|D_w| = 4a-G`.                              (7)

The D_i are disjoint, so one active support D_w can meet at most `|D_w|` distinct classes. Therefore

`sum_i b_i <= 4a-G`.                                       (8)

Combining (6) and (8), with `sum_i m_i=n_0=9-a`, yields

`k(a+1)-(9-a) <= 4a-G`,

or equivalently

> `G <= (3-k)a + 9-k`.                                     (9)

This is the first global forcing inequality for the surviving d4 compensated system.

Consequences include:

- if `k=3`, then `G<=6`;
- if `k=2`, then `G<=a+7`;
- if `k=1`, then `G<=2a+8`.

Together with `G>=max(4,a)`, (3), (4), (5), and (6), the formerly unrestricted d4 shell is reduced to a finite support-multiplicity/incidence system.

## 7. Exact one-active-column residual

If `a=1`, all four S-rows must meet the unique active column, so that column has cross-degree4 and empty core support. Thus `G=4`.

There can be no singleton zero-support class by (5), because the only active support is empty. Since `n_0=8`, `k<=3`, and every class has size at most4, the only possible multiplicity partitions are

- `4+4`;
- `4+2+2`;
- `3+3+2`.

These three partitions are the complete a=1 residual.

## Current frontier

The q36 d9 branch is empty. The only q36 d4 ceiling survivors must satisfy the finite dynamics above.

A natural next step is to classify the remaining multiplicity partitions under (2)--(9), using the exact repivot transition

`c_w' = |D_u intersect D_w|`

for a zero-column repivot u, and then either force a previously closed exact K4,9 state or violate the 211-core capacity.