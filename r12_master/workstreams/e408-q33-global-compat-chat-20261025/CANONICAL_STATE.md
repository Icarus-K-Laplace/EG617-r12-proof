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

- Four-partite proof audit: 2c73c2c8f9eb4b38cc69171be5d767dbe7adae49
- Low-slack blocker proof repair: 75a7a877ab4879cf8dcc2e11e76ecfe64c582e0d
- Pairwise blocker scope audit: f272b81656d6abcee4afee5ec26b9262a47f42b0
- Progress log with both audits: 0d9b19ce8acb094b7e239250988b5edb492a5977

**Status remains OPEN / NOT_CERTIFIED.**
