# Emergency r=12 sprint — progress log

## 2026-10-25 — first isolated sprint result

- Read the emergency-sprint branch's canonical state, open-frontier ledger, live three-line state, proof-completeness audit, asset ledger, E407 Cell-B proof files, E408 seven-block equality system, Q33 almost-regular core and exact-budget files, and the prior shell/core witness lemma and witness-capacity cross-cut.
- Reconciled the key arithmetic: E407 Q32 has \(q=32,e(H)=284\), core excess \(4\); E408 Q32 has \(q=32,e(H)=285\), core excess \(6\); E408 Q33 has \(q=33,e(H)=284\), core excess \(4\).
- Confirmed that the V11/V12 finite replay certifies the reported finite screens, not a completed parent graph. E407 Q32 still has five common-regular-\(K_{11}\) templates; E408 Q32/Q33 remain open.
- Proved Theorem 2.1 in R12_EXACT129_WITNESS_PACKING_STRENGTHENING.md: every exact-129 color has at least six no-\(S\), B-labelled \(K_5\) components of form \(\{b\}\cup Q\). Audit correction: at most one of the seven no-S components can contain pivot p; the original proof omitted p, so seven B-labelled components are not guaranteed.
- Counted at least 42 labelled witness 4-sets for E407 and at least 48 for E408 Q33/d3, with pairwise intersections at most one across distinct color components.
- Derived the E407 template A/C consequence: at most five of the seven witnesses per exact-129 color can be non-hub-complete, since each such witness needs at least six distinct \(B\)-to-\(H\) edges and the entire \(B\)-to-\(H\) budget is at most 30. Therefore at least seven hub-complete witness occurrences exist across the seven or more exact-129 colors.
- **No terminal is closed.** The labelled overlap theorem for the same core remains OPEN; E408 Q32 is not covered by the d3 contract unless its own reduction supplies \(M[B]=\varnothing\). The root theorem remains NOT_CERTIFIED.
- No SAT/ILP graph search was run; no local integer profile was promoted to graph realizability.


## 2026-10-25 — Round 2: blocker-occurrence budget and two audit corrections

- Proved \(M_C\ge15+P_C\) for every exact-129 color in the outer seven-block E408 equality system. Here \(M_C\) is the number of size-five blocker occurrences across outer blocks and \(P_C\) is the block-block duplicate count. The proof sums \(e_C(B_i,R)\ge72-m_i(C)\) and uses \(P_C+R_C=62\).
- Aggregating over \(m=8,9,10\) exact-129 colors gives \(\sum M_C\ge77m-427\), namely 189, 266, or 343. This is necessary structure only.
- Retracted the attempted E408 885-edge contradiction: it incorrectly treated the local bound \(\omega(C[R])\le5\) on the 61-point T61 residual as a global bound on C, even for outer vertices outside R. The correct blocker bound remains \(e_C(B_i,R)\ge62\).
- Corrected the witness-packing count: among seven components avoiding S, one may contain pivot p. The proved lower bound is six B-labelled no-S K5 witnesses per exact-129 color, yielding at least 42 for E407 and 48 for E408 Q33/d3.
- Corrected the E407 A/C corollary from at least two to at least one hub-complete witness per exact-129 color, hence at least seven occurrences overall.
- No E407/E408 terminal is closed. The next target remains a labelled overlap/capacity theorem that combines these corrected witness sets with the 284-edge core and exact outer-block budgets.
