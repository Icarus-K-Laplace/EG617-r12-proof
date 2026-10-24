# Progress log — E408 Q33 global compatibility

## 2026-10-25 — branch setup and dependency audit

- Created the isolated branch workstream/r12-e408-q33-global-compat-20261025 from the latest zero-excess-witness branch head. All authored files are confined to r12_master/workstreams/e408-q33-global-compat-chat-20261025/.
- Read the latest emergency sprint, ultimate-closure, witness-packing, and zero-excess-witness states. Confirmed that the 284-edge core is shared by E407 Q32 and E408 Q33, while E408 Q32 has 285 edges and is out of scope.
- Read the latest universal Q33 minimum-support result S0>=12. It closes S0=11 only under the retained T61 / exact-129 / 31-point / 56-witness contracts; it does not close the Q33 terminal.
- Audited the earlier ten-witness-star argument and found that its claim “e(H[U])=135 or e(H[U])>=144” is not justified: the second-Turán bound only forces L to be tripartite, not complete tripartite. Recorded this proof correction in PROOF_DEPENDENCIES.md and did not use the claim.
- Derived a new independent four-partite bound S0>=22. The proof uses the D-to-W incidence equation, a three-large-part independent-transversal lemma, and a complete case analysis of the six D-complete W-vertices at S0<=21. This implies delta>=9 in the four-partite branch, but does not close that branch.
- Built SEVEN_BLOCK_INCIDENCE_LEDGER.md, which explicitly links the outer one-or-two row system to exact-129 K5-component labels. It proves M_C>=15+P_C, sum P_exact>=69, sum M_exact>=189, and a per-block selected-component occurrence condition. It also records the baseline-edge caveat: a forced component-representative edge is not automatically a duplicate counted in P_C.
- Built NON_FOUR_PARTITE_TERMINAL.md with the exact vertex-incidence identities d_L(u)=3r_u+ell_u and d_H(u,W)=3r_u+ell_u-18+epsilon_u. The second-Turán bound e(L)<=354 does not exclude the actual interval 340<=e(L)<=353.
- No graph-completion SAT/ILP certificate was generated. No terminal is claimed closed. The remaining contract is explicit in the canonical state and the two terminal files.


## 2026-10-25 — independent proof review

- Rechecked the four-partite S0>=22 argument line by line. Tightened the part-size derivation and made the \(x_4+x_5\ge8\) lower-bound arithmetic explicit in the committed proof.
- The proof's critical finite split is: \(m\le4\) contradicts D-to-W incidence; \(m=5\) gives a K12 directly; \(m\ge7\) contradicts the total excess; \(m=6\) leaves only three top-extra profiles (3,5,5), (4,4,4), (4,4,5), each of which cannot have all three vertices pairwise nonadjacent. Thus \(S_0\le21\) is excluded under the four-partite contract.
- Confirmed that this theorem does not use the uncertified ten-witness-star dichotomy. The latter's tripartite-versus-complete-tripartite gap is explicitly documented in PROOF_DEPENDENCIES.md.
- The remaining branch is not solved: non-four-partite L remains in the second-Turán interval, and the four-partite branch with \(S_0\ge22\) still needs a genuine cross-layer contradiction or independently replayable finite certificate.
