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

## Audit correction: outer monochromatic-\(K_{12}\) isolation claims withdrawn

A cross-branch audit found a false inference in the former Lemma 13.1: a monochromatic \(K_{12}\) need not be isolated in its color. For any outside vertex \(z\), the twelve edges from \(z\) to the clique must use all eleven other colors, which proves only
\[
d_C(z,K_{12})\le1,
\]
not \(d_C(z,K_{12})=0\). A single external \(C\)-edge is allowed.

The former proofs of the \(P_C=50,r_i=6\) corner and the claimed caps \(P_C\le49\), \(P_C\le48\) are withdrawn because they used the invalid single-edge inference. The \(P_C=50,r_i=6\) corner is now independently excluded by R12_P50_R6_DOUBLE_STAR_EXCLUSION.md; the profiles \((5,2,1^5)\) and \((4,3,1^5)\) are excluded by R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md. The four remaining correct profiles with \(\max_i r_i\le4\) are \((4,2,2,1^4)\), \((3,3,2,1^4)\), \((3,2,2,2,1^3)\), and \((2^5,1^2)\); the earlier alternatives \((4,2,2,2,1^3)\) and \((3,2,2,2,2,1^2)\) were an arithmetic transcription error because they sum to 13, not 12. These four profiles and all \(P_C\ge51\) profiles are now excluded by R12_HIGH_P_COLOR_CAP_COMMON_STAR.md, establishing the conditional colorwise cap \(P_C\le49\). The stronger cap \(P_C\le48\), which would exclude \(P_C=49\), remains **NOT CERTIFIED**. The former drafts remain on audit hold and are preserved in \`ARCHIVE_UNCERTIFIED_OUTER_CAPS_20261025.md\`; do not use them as dependencies.

## Result 4: universal E408 Q33 minimum-support bound \(S_0\ge13\)

The new inner-core theorem \`R12_E408_Q33_S0_12_EXCLUSION.md\` excludes the equality case \(S_0=12\) in the 31-point/56-witness boundary, conditional on the retained T61, exact-129 factor, and witness-packing contracts. It uses the exact row identity
\[
s_r=3+g_r-a_r
\]
and exhausts the possible \(q_w=|N_H(w)\cap U|\) degree patterns. The \(S_0=12\) case forces a seven-point transversal \(T\), partitions \(R=U\setminus T\) into three 8-point \(R\)-only transversals, and then contradicts \(\omega(H)\le11\) in every remaining multiplicity/high-neighborhood profile.

The conclusion is
\[
\boxed{S_0=\epsilon_U+2\delta\ge13,\qquad \delta\ge5.}
\]
The four-partite branch retains its stronger separate bound \(S_0\ge22\) and \(9\le\delta\le17\). The new arithmetic verifier \`verify_s0_12_exclusion.py\` enumerates the 14 feasible degree profiles and checks the row-sum and multiplicity bookkeeping. It does not machine-verify the graph lemmas or upstream contracts.

This inner-core result does not close E408 Q33, the outer seven-block system, E407 Q32, E408 Q32, or the original \(K_{145}\) theorem.

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

- The former single-edge proofs are on audit hold; the independent double-star/common-star proofs now establish the conditional cap P_C\le49, while P_C\le48 remains NOT CERTIFIED.

## \(P_C=49\) boundary screen — partial result

The common-star finite verifier was independently reimplemented and replayed in-session. The \(R_C\le12\) result reproduces the exact four gadget clique counts, row-pair counts, 72 profile/form checks, 2,405,684 DP transitions, and maximum 2,625 reachable intersection states.

For \(P_C=49\), \(R_C=13\), there are eleven positive seven-part profiles. The extended DP checks the nine profiles with \(\max r_i\le5\) across four gadget normal forms (36 checks, 5,021,134 transitions, maximum 3,329 states). It fails to find a common star only for \((4,4,1^5)\) in forms \(b=1,4\) and \((4,3,2,1^4)\) in forms \(b=2,3\).

Seven of the eleven profiles are now excluded:
\[
(2^6,1),\ (3,2^4,1^2),\ (3^2,2^2,1^3),\ (3^3,1^4),\
(4,2^3,1^3),\ (5,2^2,1^4),\ (5,3,1^5).
\]
The first five use the common-star plus double-star argument when all pairwise budget sums are at most six. The last two use the incidence-sensitive verifier, which carries the partial component incidence \(p\le r-a\): profile \((5,2^2,1^4)\) uses the mode \(p_5\le3,p_2\le1,p_1=0\); profile \((5,3,1^5)\) uses one of three modes \((p_5,p_3)\in(\le2,\le2),(\le3,\le1),(\le4,0)\). Their combined finite checks cover all four gadget forms with 503,748 and 1,417,758 transitions respectively, with no empty admissible star state.

The four remaining \(P_C=49\) profiles are
\[
(4,3,2,1^4),\quad (4,4,1^5),\quad (6,2,1^5),\quad (7,1^6).
\]
The first two require a pairwise-intersection alignment not dependent on a common point; the last two require corrected high-budget row analysis. The archived P49 boundary proof remains NOT CERTIFIED as a whole, and \(P_C\le48\) is not established. E408 Q33 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.


## Latest isolated commits

- P49 common-star finite screen: 84a59a5bcab57a8536c8d3a45af481f46427c6e3
- Incidence-sensitive P49 verifier: 54a26037460bdb15ae35cf027b8f141ea2179a3e
- Incidence-sensitive P49 theorem note: c884358a548ec679a5e9e46a0471161bd472ea5e
- Updated first-stage P49 screen: 511fe9bd1cfed4ea292004165876a0c05b2c4231
- Updated P49 progress log: e6b64c4ed043f15332301afe30e78e3b73bf99b5
- Updated proof dependency map: 7114eb15da34effbc9653e4dc3c649dbad368b75
- P49 Case I repaired; Cases II–V explicitly retained as NOT CERTIFIED: 8662900d1d9cff04a9a4872e38786f2f897ed79d
- P49 audit-status progress update: afc14599de7f713c5bd7f0f418f3a2c9bb53af16
- P49 profile analysis: 44f40e49a6ca84893c2cd26ef31b9dfd9c6b0875
- Progress log update: c8d4f076b6f6bce1b91210be69514ca01353e8bf
- Proof dependency map update: 8e9612dbaf5f3b70273895b40b9796d810fac412
- Common-star finite verifier: c413b1065e9926d00ad1319f2e8d8a815e4850b5
- Conditional colorwise \(P_C\le49\) theorem: 04b5ec6f9a1e118faee2216208e1f13361fb8d43
- Active ledger profile correction and common-star theorem integration: 1a41ecfc88e25207d0f52e52d43e4a48a76b4dc6
- Proof dependency map update: 94f0edd87b05f28d271bfc611fbf882ecb8f8cb0
- Progress log updated to mark obsolete \(P_C\le47/48/49\) attempts withdrawn: 7bcb314fcd2059e877912a49104934435fd3ebd7
- Corrected \(P_C=50\) high-profile partition arithmetic and removed duplicated sections: d55d0e43a1b17fd9ef2b5dd7971560f1dcc4025d; 379c1e4c8a9a511431c8de22d79c9ecf852355eb; 3215fe96fec61f4bcdd8d95f86d69d5c3e0b5adf
- Refreshed local \(P_C=50,r_i=6\) theorem scope: c7c0793973bc8095f48cf1dbfb3e18712dceee54
- S0=12 exclusion theorem, including row-identity and disjoint-part audit: a1cc059324df01bfa1afec5bf20ba7a1194dd249
- S0=12 arithmetic profile verifier: 4093c6f03aa5ca60f80765264e90590cdf85d5f1
- Repaired local \(P_C=50,r_i=6\) corner via double-star: 07b6891eefac7163b1a0fbc1c2529126c2b5b1d7; verifier 2c42edbf6996bc733f7df1ee5a182c5e8954447e
- \(P_C=50\) profiles \((5,2,1^5)\), \((4,3,1^5)\) and finite verifier: 4a1bd39ba4e08854fd35907d051a44451259b07c; d33fe53aa7cd63f1fff9cb337231e39e449b28d7
- Archived uncertified outer-cap drafts and P49/P48 audit holds: a0a8f21d872b261b24580ad5e9f15942046cc74f; a11d93b8d9a3cd58aa7f6f8da58ae3e90def8391; cfcb8f70f856dd742d3a658551b97f5d65e17fb3

**Current status: the conditional colorwise cap \(P_C\le49\) is established. E408 Q33 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.**