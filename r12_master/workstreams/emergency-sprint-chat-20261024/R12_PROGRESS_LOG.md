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

## 2026-10-25 — second structural result: high-multiplicity witness stars

- Proved the witness-star lemma in R12_WITNESS_OVERLAP_STAR_LEMMA.md. If \(m\) labelled witness 4-sets share a core vertex \(x\), their other triples are disjoint and their union \(U\) has \(\alpha(H[U])\le3\). Turán gives \(e(H[U])\ge3\binom m2\), and every vertex in a triple has at least \(m-1\) neighbours in the other triples.
- For the extremal \(m=10\) case, the second Turán theorem shows \(e(H[U])\le143\) forces \(H[U]=3K_{10}\); thus \(e(H[U])\) must be 135 or at least 144.
- Ruled out the \(3K_{10}\) case when \(\varepsilon_x=0\): the four core non-neighbours of \(x\) would have to be complete to one of the three \(K_{10}\) cliques; two share a clique, and the degree/excess budget lets us choose non-neighbours in each other clique, creating an independent 5-set. Hence a 10-witness star in the Turán-equality regime forces \(\varepsilon_x\ge1\).
- This is a structural reduction, not a contradiction: the \(e(H[U])\ge144\) regime and the \(3K_{10}\) regime with \(\varepsilon_x\ge1\) remain open. Need combine with the shell incidence ledger and the actual five Q32 template labels.
- Commit: 11ea1ae6971319d746f99a23d333a3336d142f7b.

## 2026-10-25 — Round 3: witness-union capacity refinement

- Added R12_WITNESS_UNION_CAPACITY_REFINEMENT.md (commit 9dd07314d73c721c9cc8b008b7a7166c825ce566).
- Proved the exact core-capacity inequality \(6N\le e(\overline{H[U]})\le\binom v2-p_4(47-v)-12v+284-E_U\), retaining the nonnegative core excess on U.
- Used the numeric caps \(C_{28}=290,C_{29}=310,C_{30}=331,C_{31}=353,C_{32}=375\) to sharpen the witness-union lower bounds.
- E407 A/B: seven exact-129 colors imply \(v\ge29\); eight or more imply \(v\ge31\). E407 C/D/E: seven exact colors imply \(v\ge32\); eight or more imply \(v\ge33\). E408 Q33/d3: \(\beta=0\) implies \(v\ge31\), while \(\beta\ge1\) implies \(v\ge33\).
- Remaining union-size boundary kernels are E407 A/B with exactly seven exact colors and \(v=29\), E407 C/D/E with exactly seven exact colors and \(v=32\), and E408 Q33/d3 with \(\beta=0,v=31\). These are not graph-level contradictions.
- Explicitly did not transfer the 284-edge bound to E408 Q32, whose core has 285 edges and whose own shell-support split is not certified.
- Current theorem status remains **OPEN / NOT_CERTIFIED**; no full parent graph was constructed or excluded in this round.


## 2026-10-25 — Round 4: outside-core witness-hitting inequality

- Extended R12_WITNESS_UNION_CAPACITY_REFINEMENT.md with the exact inequality
  ```
  sum(r_x*d_R(x)) + sum(r_x*epsilon_x) >= N*(3v-5) - 3*sum(r_x^2).
  ```
  Proof: each w outside the witness union U must hit every independent 4-set Q_i; count those hits with multiplicity r_x and substitute the exact core-degree identity.
- E407 A/B boundary (seven exact-129 colors, v=29): the inequality forces 2R+E_U>=4, alongside the core cap R+E_U<=16.
- E407 C/D/E boundary (seven exact-129 colors, v=32): r_x=7 for all 32 union vertices, forcing 2R+E_U>=56 and R+E_U<=39; hence at least 26 complement edges are not covered by the 56 witness K4s.
- E408 Q33/d3 boundary (beta=0, eight exact-129 colors, v=31): forces 2R+E_U>=7 and R+E_U<=17; hence at least two complement edges remain uncovered.
- Commit for the strengthened theorem file: fbd9b72a50d78b7e71ff0c733528aea9985b9885. Canonical-state sync: 2cbea843acdb5d5af91fc27bd479689856a453ec.
- These are stricter necessary conditions, not terminal contradictions. No E407/E408 terminal is closed; E408 Q32 remains excluded until its own shell-support reduction is certified.
