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


## 2026-10-25 — low-slack blocker normal form and audit repair

- Integrated the read-only pairwise blocker-compatibility theorem from the ultimate-closure branch. Clarified that its proof extends from same-block pairs to cross-block pairs only when the two outer vertices are assumed nonadjacent in C.
- Derived a low-slack theorem for an exact-129 color and any outer block with \(r_i(C)\le3\): all ten isolated K5 components are represented in exactly one row neighborhood, exactly two rows contain no full component, and each component-containing row has size at most seven.
- Audit caught a gap in the first draft of this theorem: two rows that individually contain no full component can jointly cover a component, so their pairwise blocker parameter need not be zero. Replaced that argument with the stronger, simpler gadget-incidence count: three no-component rows each contribute at least six incidences to the 11-point gadget, giving at least 18 gadget incidences, whereas the one-or-two rule allows at most \(11+r_i(C)\le14\). The committed proof now uses this valid contradiction.
- Cross-block consequence: when \(r_i(C),r_j(C)\le3\), each of the ten component labels has a unique representative in each block. The two representatives must be C-adjacent: each row contains the component plus at most two extra vertices, so at least seven gadget vertices remain outside their union, contradicting pairwise compatibility if the representatives were C-nonadjacent.
- For each low-slack block, the 56 selected witness labels are partitioned among 12 row vertices; each row class is a matching of pairwise-disjoint Q-sets and contains at most one Q from each selected color. The immediate capacity bound \(12\cdot7=84\) still exceeds 56. This is a sharper finite contract, not a terminal contradiction.
- E408 Q33 remains OPEN / NOT_CERTIFIED; the non-four-partite L branch and the four-partite branch with \(S_0\ge22\) remain unresolved.


## 2026-10-25 — four-partite proof audit

- Rechecked the \(S_0\ge22\) theorem after the low-slack integration. Closed two presentation gaps in the written proof: the part-size argument now explicitly excludes two 7-point parts because \(7\cdot7<56\), and the \((4,4,4)\) case in the \(m=6\) split now explicitly shows why three pairwise nonadjacent extra-neighbor sets cannot each union to a large part.
- The corrected proof remains conditional only on the frozen four-partite Q33 contract and the already stated core/independence constraints. The remaining \(\delta\in[9,17]\) branch is still open.
- Canonical state consolidated to remove duplicate sections and now explicitly records both proof audits and the current status.


## 2026-10-25 — exceptional-row refinement and duplicate thresholds

- Strengthened the low-slack normal form: the two rows containing no full K5 component have gadget portions whose union is all of U_C. Their complements are disjoint cliques of sizes 5+5, 5+4, or (for r_i=3) 5+3 / 4+4. If a is the overlap of the two gadget portions, and e,t count the additional gadget/component incidences in component rows, then the exact budget is \(r_i(C)=a+e+t\) with \(1\le a\le3\) and \(e+t\le2\).
- Derived a duplicate-budget threshold: \(k_C=\#\{i:r_i(C)\le3\}\ge\max(0,7-\lfloor(55-P_C)/3\rfloor)\). Thus P_C thresholds 35,38,41,44,47,50,53 guarantee at least 1,2,3,4,5,6,7 low-slack blocks respectively.
- Explicitly recorded the limitation: \(\sum_{C:s_C=0}P_C\ge69\) does not by itself force any one exact color to have P_C>=35, so these branch filters do not close the global terminal.

## 2026-10-25 — extended exact-129 row theorem

- Proved and committed Theorem 10.1 for every exact-129 color/block with \(r_i(C)\le5\). It strengthens the earlier \(r_i\le3\) normal form and explicitly handles the critical \(r_i=5\) boundary: one no-component row or a double-component row would force at least 67 incidences, exceeding \(61+r_i\le66\).
- The two no-component rows cannot jointly cover a K5 component when \(r_i\le5\); doing so adds five component incidences to the baseline 62, again forcing at least 67. Pairwise blocker compatibility therefore forces their gadget portions to cover all 11 gadget vertices.
- Derived the exact charge identity \(r_i=a+e_i+t_i\) and the complete complement-clique size profiles for \(a=1,\ldots,5\).
- Proved Corollary 10.2: if \(r_i+r_j\le6\), the ten unique component representatives form a forced C-colored matching between the two blocks. A color with \(P_C\ge36\) necessarily has at least one such pair.
- Scope remains conditional and E408 Q33 remains OPEN / NOT_CERTIFIED. The aggregate duplicate bound does not yet force \(P_C\ge36\) for any single exact-129 color.


## 2026-10-25 — independent audit of Theorem 10.1

- Re-audited the \(r_i\le5\) proof after committing it. The delicate one-no-component-row branch requires ruling out \(k\ge2\) in the pairwise blocker theorem before deriving six gadget incidences. The proof now explicitly uses the duplicate budget: \(r_i\le5\) permits at most one repeated K5 component; all ten components must then be represented, so the union of the repeated pair cannot cover a second component. Hence \(k=1\), and the six-gadget-incidence bound is valid.
- Made the one-repeat deduction explicit in the committed theorem. The \(r_i=5\) boundary is now handled without assuming pairwise compatibility with \(k=1\) prematurely.
- No graph-level UNSAT result follows from this lemma alone. The exact-129 colors may still have \(r_i(C)\ge6\) across most blocks, and the aggregate duplicate ledger does not force a color to have \(P_C\ge36\).
