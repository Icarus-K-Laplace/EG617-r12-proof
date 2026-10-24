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
- Corrected safe counts: E407 any template has \(v\ge29\) with exactly seven exact-129 colors and \(v\ge31\) with at least eight; E408 Q33 has \(v\ge31\) for eight exact-129 colors at any beta.
- Audit correction: the claimed eight no-S components per color in E407 C/D/E, and the beta>0 implication in E408 Q33, do not follow. An S-edge permits but does not force its endpoints into one K5 component. These stronger counts were withdrawn; the remaining capacity boundaries are E407 seven-color \(v=29\) and E408 Q33 eight-color \(v=31\).
- Explicitly did not transfer the 284-edge bound to E408 Q32, whose core has 285 edges and whose own shell-support split is not certified.
- Current theorem status remains **OPEN / NOT_CERTIFIED**; no full parent graph was constructed or excluded in this round.


## 2026-10-25 — Round 4: outside-core witness-hitting inequality

- Extended R12_WITNESS_UNION_CAPACITY_REFINEMENT.md with the exact inequality
  ```
  sum(r_x*d_R(x)) + sum(r_x*epsilon_x) >= N*(3v-5) - 3*sum(r_x^2).
  ```
  Proof: each w outside the witness union U must hit every independent 4-set Q_i; count those hits with multiplicity r_x and substitute the exact core-degree identity.
- E407 A/B boundary (seven exact-129 colors, v=29): the inequality forces 2R+E_U>=4, alongside the core cap R+E_U<=16.
- Conditional algebra only: if an independent argument supplies N=56 on v=32 with r_x<=7, then 2R+E_U>=56 and R+E_U<=39. The present exact-129 count contract does not establish that premise for seven-color E407 C/D/E, so no terminal application is claimed.
- E408 Q33 boundary (eight exact-129 colors, v=31, any beta): forces 2R+E_U>=7 and R+E_U<=17; hence at least two complement edges remain uncovered.
- Commit for the strengthened theorem file: fbd9b72a50d78b7e71ff0c733528aea9985b9885. Canonical-state sync: 2cbea843acdb5d5af91fc27bd479689856a453ec.
- These are stricter necessary conditions, not terminal contradictions. No E407/E408 terminal is closed; E408 Q32 remains excluded until its own shell-support reduction is certified.


## 2026-10-25 — Round 5: live sibling audit and repaired four-partite E408 Q33 boundary

- Refreshed latest heads from emergency sprint (ad56a91), ultimate closure (1aa47d1), witness packing (5d0e3ce), zero-excess witness (98167ec), general-r architecture (a922c4d), and general-r asymptotic (fa6a5f2). Sibling branches were read-only.
- Corrected the beta-sensitive witness-count application in R12_WITNESS_UNION_CAPACITY_REFINEMENT.md: beta>0 does not force two S vertices into the same K5 component. Safe E407 floors are N>=49 for seven exact-129 colors and N>=56 for eight; safe E408 Q33 floor is N>=56 for eight exact-129 colors, regardless of beta.
- Added R12_CROSS_BRANCH_AUDIT_AND_S0_REPAIR.md (commit 5b40022ac171cc568cea6d4f034bc66ce3f8ef3b).
- Independently audited the sibling E408 Q33 four-partite S0=10 proof. Its original s=1 and s=2 steps incorrectly treated selected pairs not lying in a Q block as necessarily extra L-edges, although such pairs may be H-edges.
- Repaired s=1 by counting all selected non-Q pairs through the unused perfect matchings: 27 selected cross-part pairs cannot fit into 6 pairs from unselected-D blocks, at most 9 from the selected-D class, and at most 9 non-Q pairs; 27<=24 is impossible.
- Repaired s=2 using the degree identity epsilon_x+j_x=1[x in T*]. It implies no extra L-edge touches A0∪B0∪C0. The unused matchings then give degrees 4 from A0 to B0 and 5 from each of A0,B0 to C0, forcing a triangle in L[A0,B0,C0]. With any unselected d in D this yields an independent 4-set disjoint from T*=N_H(w*)∩U, contradicting alpha(H)<=4.
- Thus the four-partite E408 Q33 minimum-support contract excludes S0=10 and forces epsilon_U+2delta>=11, with a repaired proof. This does not close the non-four-partite branch.
- Headline status remains OPEN / NOT_CERTIFIED. E407 Q32 same-core completion, E408 Q32's separate 285-edge core, E408 Q33 non-four-partite completion, and the original K145 bridge remain open.


## 2026-10-25 — Round 6: exclude S0=11 in the four-partite E408 Q33 branch

- Added R12_E408_Q33_FOUR_PARTITE_S0_11_EXCLUSION.md (commit 4f5e9697d93e9173d2819d59bb5d6db687410f53) and verify_s0_11_profiles.py (commit c99283859b19642a50e4915c85a57987b31fe4bc).
- Under S0=11, the core budget gives delta in {4,5}, epsilon_U=11−2delta, and e_H(U,W)=125. Exact degree-profile enumeration leaves k=3,4,5,6 cases; group-capacity excludes k=3/4 and the all-size-8/9 profiles.
- In each remaining profile, one exceptional size-10/11 neighborhood T* is forced. The spillover-aware degree identity shows that every large-part vertex outside T* and at most one spillover point has epsilon_x=j_x=0, so no extra L-edge touches the remaining large-part complements.
- Those complements have at least four points in each large part. The unused-pair matching then guarantees a triangle in L[A0,B0,C0]; adding an unselected D point gives an independent 4-set disjoint from T*, contradicting alpha(H)<=4.
- Independently reproduced the exact integer degree-profile enumeration and the key common-neighbor margin (4+4−6=2). The verifier is arithmetic-only and is not a graph-realization certificate.
- The four-partite E408 Q33 minimum-support branch now has S0>=12, conditional on that branch's contract. The non-four-partite branch remains OPEN. E407 Q32, E408 Q32, the T61-to-K145 bridge, and EG617(r=12) remain OPEN / NOT_CERTIFIED.
