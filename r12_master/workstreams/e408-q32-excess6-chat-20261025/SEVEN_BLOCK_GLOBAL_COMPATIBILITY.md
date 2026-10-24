# Seven-block global compatibility — E408 Q32

Status: **PROVED necessary-condition coupling; global incompatibility remains OPEN.** This file combines the outer seven-block ledger with the 285-edge core witness family without assuming M[B]=∅.

## 1. Outer equality system

Conditional on the registered outer embedding ledger, the 145 vertices split as seven target K12 blocks B_0,…,B_6 and a 61-point residual R with e(F)=408. Every color has exactly870 edges globally. For each of the eleven non-target colors C,

\[
e_C(R)=129+s_C,\quad s_C\ge0,\quad \sum_Cs_C=3,
\]
\[
P_C+R_C+s_C=62,\qquad
\sum_CP_C=252,\quad \sum_CR_C=427.
\]

Here P_C is the block-block duplicate count, R_C the block-R duplicate count, and s_C the excess above 129 inside R. Thus m∈{8,9,10} colors are exact-129.

For every exact-129 color, the registered blocker theorem gives R_C≥7 and hence P_C≤55. The more detailed occurrence count below is also proved under the same Type-I contract.

## 2. Blocker-occurrence inequality

For an exact-129 color C, let M_C be the number of outer block vertices b∈B_i whose C-neighborhood N_C(b)∩R has size exactly five. A size-five blocker is one of the ten isolated K5 components of C[R]. Each such component can be used at most once in a fixed outer block: if two vertices of one target K12 block used the same K5 as their entire C-neighborhood, the two vertices together with an independent 11-set in R minus that K5 would form a C-independent 13-set.

If m_i(C) is the size-five blocker count in block B_i, the other 12-m_i(C) vertices have C-degree at least six into R. Therefore

\[
e_C(B_i,R)\ge5m_i(C)+6(12-m_i(C))=72-m_i(C).
\]

Summing over seven blocks yields R_C≥77-M_C. Since s_C=0 and P_C+R_C=62,

\[
\boxed{M_C\ge15+P_C.}
\]

Each of the ten isolated K5 components can appear at most once in each of seven blocks, so M_C≤70. In particular P_C=55 forces M_C=70, i.e. all ten components are used once in every outer block.

## 3. Coupling blocker occurrences to core witnesses

From the component-support classification, at least eight of the ten isolated K5 components in each exact-129 color have the form {y}∪Q with y∈{p}∪A and Q⊂H an independent 4-set. Call these the good witness components. At most two isolated components per color are not good, and they can account for at most 14 blocker occurrences across seven blocks.

Consequently the number of good-component blocker occurrences for C is at least

\[
M_C-14\ge P_C+1.
\]

A good component can be used at most once per block, hence at most seven times overall. If g_C is the number of distinct good witness components used as size-five blockers, then

\[
\boxed{g_C\ge\left\lceil\frac{P_C+1}{7}\right\rceil
=\left\lfloor\frac{P_C}{7}\right\rfloor+1.}
\]

If the exceptional gadget vertex x for color C lies outside H, there are at least nine good isolated components and at most one bad isolated component; the same argument strengthens to g_C≥floor(P_C/7)+2.

## 4. Aggregate lower bounds across exact-129 colors

The nonexact colors have total excess three. Since P_C+R_C+s_C=62 and R_C≥0,

\[
\sum_{s_C>0}P_C\le62(11-m)-3.
\]

Using Σ_C P_C=252 gives

\[
\boxed{\sum_{s_C=0}P_C\ge62m-427.}
\]

For m exact colors, each residue P_C mod 7 is at most six, so

\[
\sum_{s_C=0}\left\lfloor\frac{P_C}{7}\right\rfloor
\ge\left\lceil\frac{62m-427-6m}{7}\right\rceil
=8m-61.
\]

Therefore the seven-block near-Latin system forces

\[
\boxed{\sum_{s_C=0}g_C\ge9m-61.}
\]

| Exact-129 colors m | Σ exact P_C lower bound | Distinct good witness components used as blockers |
|---:|---:|---:|
| 8 | 69 | at least 11 |
| 9 | 131 | at least 20 |
| 10 | 193 | at least 29 |

If k of the m exceptional gadget vertices lie outside H, the last lower bound improves to 9m-61+k.

This is stronger than merely counting 48/54/60 or more independent 4-sets: it certifies that a specified subset of at least 11/20/29 labelled witness components is linked to exact size-five blocker neighborhoods in the outer seven blocks. It still does not force a contradiction by itself.

## 5. Combined E408 Q32 terminal ledger

All of the following are simultaneously necessary:

1. Core: e(H)=285, α(H)≤4, δ(H)≥12, total excess six.
2. Shell: 22≤e(M)≤32 and Σ_A g_a=32-e(M)≤10; zero-shell-support core vertices are allowed but at most six.
3. Witness packing: N≥8m pairwise-linear independent 4-sets in H, uniformly over both shell-support cases.
4. Support size: v≥33,35,37 for m=8,9,10, respectively, with the exact capacity inequality 6N≤Cap_285(v)-E_U.
5. Outer blocks: P_C+R_C+s_C=62, Σs_C=3, P_C≤55 for exact colors, and at least 11/20/29 distinct good witness components are used as size-five blockers for m=8/9/10.

No complete SAT/ILP/CSP instance has been built here. The remaining task is a graph-level compatibility theorem using the actual H adjacency, the shell labels on Q, and the seven-block blocker assignments. Do not promote these necessary constraints to a global contradiction.
