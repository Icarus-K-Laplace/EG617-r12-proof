# E408 Q33 global-compatibility — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e408-q33-global-compat-20261025  
Exclusive path: r12_master/workstreams/e408-q33-global-compat-chat-20261025/

## Headline

**E408 Q33 remains OPEN / NOT_CERTIFIED.** This workstream has produced stronger conditional structure and an explicit labeled finite contract, but no complete terminal contradiction or independently replayed UNSAT certificate.

## Frozen Q33 contract

- T61 residual F has 61 vertices, alpha(F)<=5, omega(F)<=11, and a legal degree-13 pivot p.
- Shell A=N_F(p), |A|=13; core H=V(F)\(A union {p}), |H|=47.
- e(H)=284, delta(H)>=12, alpha(H)<=4, omega(H)<=11, and sum_H(d_H-12)=4.
- E408 Q33 has q=33 and a 284-edge core; its residual non-target excess is 3. At least eight non-target colors are exact-129 on the residual.
- At the minimum-support boundary, U has 31 vertices, W=H\U has 16, and Q contains 56 labeled independent four-sets, seven from each of eight exact-129 colors. Within a color the sets are disjoint; across colors distinct sets intersect in at most one vertex.
- L=overline(H[U]), e(L)=336+delta, epsilon_U=sum_{u in U}(d_H(u)-12), and S0=epsilon_U+2delta.

## Result 1: four-partite support boundary

Under the additional contract that L is four-partite, its part sizes are 8,8,8,7. The D-part has size 7 and the three large parts A,B,C have size 8. The proof in FOUR_PARTITE_GLOBAL_COMPATIBILITY.md gives
\[
\boxed{S_0\ge22},\qquad \boxed{9\le\delta\le17}.
\]
It uses the exact D-to-W incidence equation, the transversal lemma on A,B,C, and omega(H)<=11. The m=6 profile split and part-size deduction were independently re-audited and tightened in commit 2c73c2c8f9eb4b38cc69171be5d767dbe7adae49.

This does not exclude the four-partite branch for S0>=22.

## Result 2: exact-129 low-slack blocker normal form

The pairwise blocker theorem from the read-only ultimate-closure workstream has been integrated into SEVEN_BLOCK_INCIDENCE_LEDGER.md. Its proof extends to cross-block pairs whenever the two outer vertices are assumed nonadjacent in C.

For any exact-129 color C and outer block B_i with r_i(C)<=3:
- all ten isolated K5 components are contained in exactly one row neighborhood each;
- exactly two row neighborhoods contain no full K5 component;
- each component-containing row neighborhood has size at most seven;
- for two blocks i,j with r_i(C),r_j(C)<=3, the ten same-component representatives are forced C-edges forming a matching.

Proof audit: an initial draft incorrectly assumed that two row neighborhoods which individually contain no full component cannot jointly cover one. The committed proof instead uses the valid gadget-incidence count: three no-component rows contribute at least 18 incidences to the 11-vertex gadget, while the one-or-two rule permits at most 11+r_i(C)<=14 when r_i(C)<=3.

For each low-slack block, the 56 selected witness labels are assigned to 12 row classes. Each class consists of pairwise-disjoint Q-sets and contains at most one Q from each selected color. The crude capacity 12*7=84 exceeds 56, so this condition alone is feasible and is not a contradiction.

The two no-component rows have a sharper profile: their 11-point gadget portions cover all of \(U_C\), and their complements are disjoint cliques of sizes 5+5, 5+4, or 5+3 / 4+4 according to the overlap \(a=1,2,3\). The exact repeated-incidence identity is \(r_i(C)=a+e+t\), with \(e+t\le2\). See the exceptional-row refinement in SEVEN_BLOCK_INCIDENCE_LEDGER.md.

For a color with duplicate budget \(P_C\), the number of low-slack blocks satisfies
\[
k_C=\#\{i:r_i(C)\le3\}\ge\max\left(0,7-\left\lfloor\frac{55-P_C}{3}\right\rfloor\right).
\]
In particular, \(P_C\ge35,38,41,44,47,50,53\) guarantees at least 1,2,3,4,5,6,7 low-slack blocks, respectively. The aggregate \(\sum_{C:s_C=0}P_C\ge69\) alone does not force any single color to reach 35, so this is not global closure.

## New theorem interface: row duplicate count up to five

SEVEN_BLOCK_INCIDENCE_LEDGER.md now contains Theorem 10.1. For an exact-129 color C and block \(B_i\), if \(r_i(C)\le5\), then all ten isolated K5 components occur in exactly ten distinct component-containing rows, and the other two rows have gadget portions \(X,Y\) covering all of \(U_C\). Their overlap \(a\in\{1,\ldots,5\}\), their complements are disjoint cliques, and the exact charge identity is \(r_i(C)=a+e_i+t_i\).

Corollary 10.2: if \(r_i(C)+r_j(C)\le6\), the same ten component labels force a C-colored matching of size ten between \(B_i\) and \(B_j\). Since \(R_C=62-P_C\), \(P_C\ge36\) guarantees at least one such block pair. This improves the earlier \(r_i\le3\) theorem without extending it past its proved range; \(r_i=6\) remains outside Theorem 10.1 because split-component boundary cases may occur.

This is a verified conditional structure theorem, not a global contradiction: the aggregate \(\sum_{C:s_C=0}P_C\ge69\) still does not force a single exact color to have \(P_C\ge36\). The exceptional boundary \(r_i(C)=6\), where a full-component row can split into two labels or one component can be absent from the full-row list, is now classified separately in Theorem 11.1 below.

## Result 3: exact six-duplicate boundary

Theorem 11.1 in SEVEN_BLOCK_INCIDENCE_LEDGER.md classifies \(r_i(C)=6\) completely by the number of rows without a full \(K_5\) component and the number of repeated full components. There are exactly one or two no-component rows. The one-row case is rigid: one \(K_5\) is represented twice, all ten labels occur, and the gadget incidence pattern is a pair-union six-set intersecting the exceptional row's six-set in one vertex. The two-row case has either no repeated full component (ten distinct single-component rows) or one repeated component with the precise \(m=10\) split-label / \(m=11\) double-row alternatives.

Corollary 11.2: if one block has \(r_i(C)=6\) and another has \(r_j(C)=1\), at least eight component labels force a \(C\)-colored matching across those blocks; the lower bound is ten in the rigid one-row case and the no-repeated-full-component case, nine in the \(m=10\) split-label case, and at least eight in the \(m=11\) double-row case.

Corollary 11.3 adds a high-budget consequence: if \(P_C=50\) and one block has \(r_i=6\), at least eight vertex-disjoint monochromatic \(K_{12}\) cliques are forced; if \(P_C=49\), at least seven are forced. These are valid packing constraints, not contradictions by themselves.

This closes the local \(r_i=6\) classification gap but is not a global contradiction. Forced edges may still be baseline block-pair edges and are not charged to \(P_C\) without an independent duplicate-incidence argument.

## Seven-block global ledger

For each non-target color C,
\[
P_C+R_C+s_C=62,\quad \sum_C P_C=252,\quad
\sum_C R_C=427,\quad \sum_C s_C=3.
\]
For exact-129 colors, R_C>=7, P_C<=55, and exact size-five blocker occurrences satisfy M_C>=15+P_C. Hence sum of P_C over exact colors is at least 69 and total exact-blocker occurrence count over at least eight exact colors is at least 189.

The ledger keeps the selected K5 component labels, high-k shell labels, outer block rows, and duplicate budget attached. A forced same-component edge between two blocks may be a baseline edge; it is not automatically charged to P_C.

## Remaining terminal contract

1. **Non-four-partite L:** K5-free on 31 vertices, 56 edge-disjoint labeled K4 witnesses, e(L)=336+delta in [340,353], delta+epsilon_U<=17, S0>=12, plus the vertex-incidence identities in NON_FOUR_PARTITE_TERMINAL.md. The second-Turán bound e(L)<=354 does not exclude this interval.
2. **Four-partite L:** parts 8,8,8,7; 56 witnesses transversal; unused pair slots between large parts form perfect matchings; S0>=22 and delta in [9,17]. The seven-block labeled ledger remains mandatory.

The next proof target is a stability/packing contradiction in Case 1 or a genuinely color-labeled global contradiction in Case 2. Scalar bounds alone are not being promoted to closure.

## Audit warnings and scope firewall

- The earlier ten-witness-star file in the emergency sprint claims e(H[U])=135 or e(H[U])>=144, but its argument only forces the complement to be tripartite, not complete tripartite. This workstream does not rely on that dichotomy.
- All results here remain conditional on the retained T61 reduction, exact-129 factor theorem, 31-point/56-witness minimum-support boundary, and outer seven-block equality contract.
- This workstream does not close E408 Q32 (285-edge core), E407 Q32, or the original K145 theorem.

## Latest isolated commits

- Live sibling audit and Corollary 11.3 independent check: 597f0db0c7f37e97bb2bb448f0a50bf1f4872809
- High-\(P_C\) clique-packing theorem: c1cf309955e6435ef3aaad498bc136d5f24ddc6b
- Live sibling-head dependency refresh: 7ead15c3d79b0099a650be1157b8e68cc9574a17
- Canonical integration of high-\(P_C\) clique-packing corollary: 097aad468745c6b62101200969938981ad376910
- Proof-dependency integration: 6aaa2a6cc508344bc320cd49d254ba228b1df344
- Exact \(r_i(C)=6\) classification and 6+1 matching: 6a1f034fe9d0b2ba5ca49acde9ae57a3c2d652ce
- Theorem 11.1 / Corollary 11.2: c74b01170b4bab70e148e541b1c610279013f106
- Theorem 10.1 / Corollary 10.2: 73f02a07d4722e09af203cbc0ac8d5d82af405e4

**Status remains OPEN / NOT_CERTIFIED.**
