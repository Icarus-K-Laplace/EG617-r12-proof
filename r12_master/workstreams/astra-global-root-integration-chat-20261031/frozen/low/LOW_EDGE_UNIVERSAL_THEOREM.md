# Universal 47-point low-edge obstruction

Date: 2026-10-30.

**47_POINT_LOW_EDGE_UNIVERSAL_OBSTRUCTION = PROVED.**

There is no simple graph H satisfying simultaneously

    |H|=47, e(H)<=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

## Proof by uniform augmentation

Handshake gives e(H)>=282 and nonnegative total degree excess T=2e(H)-564<=6. COMMON_NEIGHBORHOOD_CAPACITY.md proves from these assumptions that every nonedge uv has at most 3+epsilon(u)+epsilon(v)<=9 common neighbors. UNIVERSAL_EDGE_AUGMENTATION_LEMMA.md proves that any such edge can be added safely: it cannot create K12, it cannot increase independence number, and it cannot reduce minimum degree.

At every intermediate graph the same five assumptions and T<=6 hold. Repeating at most three times yields a 285-edge graph under precisely the five assumptions of Astra U6. That theorem is independently audited, including its eight analytic steps and complete-attachment exceptions, in Q32_285_THEOREM_INDEPENDENT_AUDIT.md. U6 excludes the terminal graph. Contradiction.

The argument covers the entire 282--285 interval in a single induction. Graphs with fewer than282 edges already contradict minimum degree12.

## Independent direct route

DIRECT_UNIFORM_PROOF.md proves the same result with T<=6 throughout. It does not invoke exact-285 U6, exact-284 nonexistence or edge augmentation. It includes T=0 in the independent-four-set argument. A K11/K11 pair forces T=6 and a rigid equality case; the other reductions use only upper bounds by six. The final P and D templates require eight and ten excess units respectively. The two proofs share structural ideas but have distinct final dependency routes.

## Hereditary-cap corollary

Define R(a,n) by alpha<=a, omega<=11 and all induced caps e(J[U])<=D(|U|), where D(n)=binom(n,2)-11 p12(n). The source-complete minimum-degree theorem is independently reconstructed in MINIMUM_DEGREE_GATE_SELF_CONTAINED.md:

    J in R(4,47), e(J)<=286 => delta(J)>=12.

Combining it with the low-edge theorem gives the strict floor

    J in R(4,47) => e(J)>=286.                         [PROVED]

For an actual h13 T61 parent F and a degree13 pivot p, the audited identity is e(H)=E-91-q_p with H in R(4,47). Therefore

    q_p<=E-377.

In particular every such pivot has q_p<=30 for E407 and q_p<=31 for E408. The four requested E/q parent layers are impossible under the explicit T61 parent contract. Their precise dependencies and remaining root boundaries are in CROSS_ROOT_ELIMINATION_MATRIX.md.

## Acceptance boundary

The abstract theorem is graph-theoretic and proved. Its applications to E407/E408 are PROVED_CONDITIONAL on the stated genuine T61 parent contract and inherited caps. No assertion that those are the only remaining global branches is made. The original K145 front end, contextual R(4,49), h12, lower energies and the E408 q=31 layer retain their own obligations. No global or sibling state has been modified.
