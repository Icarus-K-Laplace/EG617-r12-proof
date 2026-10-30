# E407 Q32 — generalized support-size reserve beyond MS-29

Date: 2026-10-30

Status: **PROVED_CONDITIONAL necessary-structure theorem** under the E407 47-core contract, the exact-129 Type-I factorization, and the registered non-target independence bounds. This does not close E407 Q32.

## 1. Contract and notation

Let H be the 47-vertex target-color core with

- e(H)=284;
- minimum degree at least 12;
- independence number at most 4.

There are eleven non-target colors. For every such color D, alpha(D)<=12: otherwise a 13-set would miss D, contrary to the retained balanced-coloring counterexample contract.

For n,k define the Turan minimum-edge function

    p_k(n) = (k-r) binom(q,2) + r binom(q+1,2),
    n = qk+r, 0 <= r < k.

Thus every n-vertex graph with independence number at most k has at least p_k(n) edges. Put

    T_4(n) = binom(n,2) - p_4(n),

the maximum number of edges in a K5-free graph.

Fix seven selected exact-129 colors. In each color, the exact-129 factor theorem supplies ten disjoint K5 components; the shell/core argument selects seven components with exactly one outside-core anchor and four core vertices. Their four-sets Q_{c,j} are disjoint within one color and pairwise linear across different colors. Let

    U_7 = union of the 49 selected four-sets,
    v = |U_7|,  W = V(H) \ U_7,
    L_7 = complement(H[U_7]).

The 49 blocks own 49*binom(4,2)=294 distinct non-target edges in L_7.

## 2. The support union satisfies v >= 29

Because alpha(H)<=4, L_7 is K5-free. The 49 blocks give e(L_7)>=294.

For v<=27, T_4(v)<294, impossible. If v=28, then T_4(28)=294, so equality forces L_7 to be the balanced complete four-partite graph with four parts of size 7. Hence H[U_7] is the disjoint union of four K7s and e(H[U_7])=84.

Now |W|=19 and alpha(H[W])<=4, so e(H[W])>=p_4(19)=36. The degree sum on U_7 is at least 12*28=336, and therefore

    e_H(U_7,W) >= 336 - 2*84 = 168.

It follows that

    e(H) >= 84 + 168 + 36 = 288,

contrary to e(H)=284. Thus v>=29.

## 3. Four unselected colors strengthen the reserve

The seven selected colors own 294 distinct edges of L_7. There are four other non-target colors. Each has alpha(D[U_7])<=12, so each contributes at least p_12(v) edges inside U_7. Their edges are mutually disjoint and are disjoint from the 294 selected edges by unique edge ownership. Consequently

    e(L_7) >= 294 + 4 p_12(v).                         (1)

For the upper bound, write epsilon_U=sum_{u in U_7}(d_H(u)-12)>=0 and e_W=e(H[W]). Since alpha(H[W])<=4, e_W>=p_4(47-v). The degree sum on U_7 gives

    12v + epsilon_U = 2e(H[U_7]) + e_H(U_7,W),

while

    284 = e(H[U_7]) + e_H(U_7,W) + e_W.

Eliminating the cross term yields

    e(H[U_7]) = 12v + epsilon_U + e_W - 284.

Therefore

    e(L_7) <= binom(v,2) - 12v + 284 - p_4(47-v).      (2)

Comparing (1) and (2) gives the following exact arithmetic.

| v | p_12(v) | lower bound (1) | upper bound (2) | lower - upper |
|---:|---:|---:|---:|---:|
| 29 | 22 | 382 | 310 | +72 |
| 30 | 24 | 390 | 331 | +59 |
| 31 | 26 | 398 | 353 | +45 |
| 32 | 28 | 406 | 375 | +31 |
| 33 | 30 | 414 | 398 | +16 |
| 34 | 32 | 422 | 422 | 0 |
| 35 | 34 | 430 | 447 | -17 |

Thus

    v in {29,30,31,32,33} is impossible.

This is stronger than the old one-unselected-color contradiction at v=29. It does not assume v=29.

## 4. The v=34 equality terminal

If v=34, both (1) and (2) must be equalities. Therefore:

1. epsilon_U=0;
2. e(H[W])=p_4(13)=15, with equality in the independence-number bound, so H[W] is K4 disjoint union 3K3;
3. e(L_7)=422 and e(H[U_7])=binom(34,2)-422=139;
4. e_H(U_7,W)=12*34-2*139=130, and the full core excess four is all on W;
5. each of the four unselected colors has exactly p_12(34)=32 edges on U_7. Equality forces each induced color graph to be 10K3 disjoint union 2K2;
6. each selected color has exactly its 42 selected-block edges on U_7 and no additional edge of that color inside U_7.

This is a rigid equality case, not a contradiction. It is the next finite/structural target.

For v>=35, the scalar lower bound is no larger than the upper bound in the tested range; this reserve argument alone does not exclude those cases.

## 5. Crosscut using all exact-129 colors

A separate global crosscut, E407_SEVEN_EXACT_COLOR_EXCLUSION.md, proves m in {8,9,10} for a genuine E407 residual, conditional on its registered exact-129 Type-I factor theorem, nonexact pointwise degree floors, and Brouwer–Kang–Pikhurko input.

For each of the m exact colors, select seven K5 components and their four-core-vertex blocks. Let U_m be the union of all 7m blocks and v_m=|U_m|. The blocks are pairwise linear, so L_m=complement(H[U_m]) has at least 42m edges and is K5-free.

The support floors are:

- m=8: 56 blocks give 336 edges. Turan gives v_m>=30. If v_m=30, the Brouwer second-Turan bound gives at most 331 edges for a non-complete-four-partite K5-free graph, so L_m must be four-partite. Each K4 block then uses one point from each part, and each pair of parts must supply at least 56 distinct pairs. No four-partition of 30 has every pair-product at least 56: if a part has size at most 6, another has size at most 8; otherwise the only partitions are 7+7+7+9 or 7+7+8+8, both with a 7*7=49 pair. Hence v_m>=31.
- m=9: 42m=378>T_4(31)=360, so v_m>=32.
- m=10: 42m=420>T_4(33)=408, so v_m>=34.

For each selected exact color, its induced graph on U_m has at least max(42,p_12(v_m)) edges. Each of the other 11-m non-target colors has at least p_12(v_m) edges. Hence

    e(L_m) >= m*max(42,p_12(v_m)) + (11-m)*p_12(v_m).  (3)

The same core ledger gives

    e(L_m) <= binom(v_m,2) - 12v_m + 284 - p_4(47-v_m). (4)

The arithmetic excludes:

| m | initial support floor | excluded v_m | resulting floor |
|---:|---:|---:|---:|
| 8 | 31 | 31–34 | v_m>=35 |
| 9 | 32 | 32–34 | v_m>=35 |
| 10 | 34 | 34–35 | v_m>=36 |

Important: U_m is the union over all exact colors; it is not U_7. These bounds do not imply v_7>=35 and do not prove the MS-29 statement for the seven selected colors.

## 6. Promotion firewall

This result closes support sizes 29–33 for U_7 and gives a rigid v=34 equality terminal. It does not prove that every V12 A–E survivor has |U_7|=29, does not eliminate v=34 or v>=35, and does not prove the same-core compatibility theorem.

The V12 finite replay remains COMPUTATION_CERTIFIED under C0. E407 Q32 remains PROVED_CONDITIONAL under C0 plus the applicable support/factor contracts. No unconditional E407 or EG617(r=12) promotion is issued.
