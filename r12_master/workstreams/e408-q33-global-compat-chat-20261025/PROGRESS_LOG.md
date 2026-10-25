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


## 2026-10-25 — exact \(r_i(C)=6\) boundary classified

- Proved Theorem 11.1. For a fixed exact-129 color/block with duplicate budget six, the number of rows containing no complete isolated \(K_5\) is exactly one or two.
- The one-exception-row case is rigid: one \(K_5\) is fully represented twice; the eleven full-component rows each contain one component; the repeated pair's gadget portions are disjoint and have union size six; this six-set and the no-component row's six-set cover the 11-point gadget with one common vertex. The duplicate split is \(d_K=5,d_U=1\).
- With two exception rows, either no full component repeats (ten distinct single-component rows, with the five extra duplicate incidences split as \(d_K+(d_U-1)=5\)), or one full component repeats and \(d_K=5,d_U=1\). In the latter branch, ten full occurrences mean one component is missing from the full-row list and appears only partially; eleven occurrences mean one double-component row, all ten labels represented, and one label repeated.
- Proved Corollary 11.2: when another block has \(r_j(C)=1\), at least eight component labels force C-colored edges across the two blocks. The subcase bounds are 10 / 10 / 9 / at least 8 as recorded in the theorem.
- Independent audit checked the incidence equations \(r_i=d_K+d_U=6\), the cap \(n\le2\) from \(6n\le11+d_U\le17\), the exclusion \(n=0\), and every branch in the occurrence count \(m\in\{10,11\}\). Cross-block forced edges are explicitly not charged to \(P_C\).
- This is a conditional local classification only. E408 Q33 remains OPEN / NOT_CERTIFIED; no global UNSAT or original \(K_{145}\) proof is claimed.

- Equality-case refinement: in the \(n=1\) branch, the complements of the repeated-pair gadget six-set and the no-component-row gadget six-set are disjoint five-cliques in \(C[U_C]\). They partition the gadget together with the unique vertex shared by the two six-sets. This is a sharper canonical description of the exceptional row.


## 2026-10-25 — high-\(P_C\) consequence of the \(6+1\) boundary

- Added Corollary 11.3. If an exact-129 color has \(P_C=50\) and a block with \(r_i=6\), the other six block budgets must all be one; at least eight component labels then complete to vertex-disjoint monochromatic \(K_{12}\) cliques across all seven blocks.
- If \(P_C=49\) and some block has \(r_i=6\), the other six budgets are five ones and one two. The \(r=2\) block has at least nine distinct exact blockers, intersecting the at-least-eight clean labels from the \(r=6\) block in at least seven labels. These labels complete to at least seven vertex-disjoint monochromatic \(K_{12}\) cliques.
- This connects the duplicate budget to an explicit global packing pattern. It is not a contradiction: the current proof does not show that these maximum cliques violate the remaining color-edge budget.


## 2026-10-25 — live sibling audit and Corollary 11.3 replay

- Re-read the latest emergency-sprint, ultimate-closure, witness-packing, zero-excess-witness, and E407 Q32 branches. E407's non-four-partite \(\delta=15\) subcase is excluded under its own contract, but E407 Q32 overall remains OPEN. E408 Q33 still has \(S_0\ge12\) universally and \(S_0\ge22\) in the four-partite branch; the larger-support/global terminal remains open.
- Independently checked Corollary 11.3: \(P_C=50\) gives the block-budget vector \((6,1,1,1,1,1,1)\); \(P_C=49\) gives \((6,2,1,1,1,1,1)\). The clean-label/exact-blocker intersection in the latter case has size at least \(8+9-10=7\). The clique construction uses all seven blocks and the same \(K_5\) component, and different labels yield vertex-disjoint cliques.
- No imported sibling result contradicts or closes this line. The remaining need is still a global incompatibility theorem linking the forced outer clique/edge patterns to the 56 labeled inner witnesses.


## 2026-10-25 — genuine exclusion of the \(P_C=50,\ r_i=6\) corner

- Proved Lemma 13.1: a monochromatic \(C\)-colored \(K_{12}\) is an isolated component of \(C\). For any outside vertex, the 12 edges to the clique must contain all eleven other colors at least once, so no edge can be \(C\).
- Proved Lemma 13.2: if \(m\) vertex-disjoint \(C\)-colored \(K_{12}\)'s each meet every target block once, then \(P_C\le21(12-m)\). After removing the \(m\) isolated clique representatives, each target block has \(12-m\) leftover vertices; the remaining C-edge bipartite graph for every block pair has minimum degree 1 and maximum degree 2.
- Used Theorem 11.1 to split \(r_i=6\) into its four terminal profiles. When \(P_C=50\), the other six block budgets are all one. Every profile forces at least ten isolated C-colored \(K_{12}\)'s:
  - \(n=1\): 10 label-based plus a gadget-based \(K_{12}\);
  - \(n=2,k=1,m=10\): 9 label-based plus 2 gadget-based;
  - \(n=2,k=1,m=11\): at least 8 label-based plus 2 gadget-based;
  - \(n=2,k=0\): all ten component rows are clean.
- Therefore \(P_C\le21(12-10)=42\), contradicting \(P_C=50\). The exact \(P_C=50,r_i=6\) corner is now **EXCLUDED** under the retained contracts.
- The adjacent \(P_C=49,r_i=6\) branch is not closed: the current packing can guarantee only nine isolated \(K_{12}\)'s, giving \(P_C\le63\), which is insufficient. E408 Q33 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


- Proof-audit refinement: Cases A and B in Theorem 13.3 actually yield an immediate contradiction, because a six-neighbor gadget row plus the six low-block representatives and a fixed \(D_j\cong K_5\) would form a \(C\)-colored \(K_{12}\), while that row also has a \(C\)-edge to the one gadget vertex outside \(D_j\). Lemma 13.1 forbids any such external edge. Case C is handled by the isolated-clique duplicate cap. The theorem proof was rewritten to make this fork explicit.


## 2026-10-25 — universal exact-129 outer budget cap

- Proved Theorem 14.1: every exact-129 color has \(P_C\le49\), equivalently \(R_C\ge13\), under the retained contracts.
- For \(P_C\ge51\), \(R_C\le11\), so every block-pair budget sum is at most six. Corollary 10.2 forces all ten component matchings across all 21 block pairs, yielding ten C-colored \(K_{12}\)'s. Any extra C-neighbor outside a designated \(K_5\) contradicts isolation; with no extras, the clique-budget cap gives \(P_C\le42\).
- For \(P_C=50\), the \(r_i=6\) vector was already excluded by Theorem 13.3. The only other positive budget vectors with a pair sum above six are \((5,2,1^5)\) and \((4,3,1^5)\). If the one exceptional same-label edge is present, the \(K_{12}\) argument applies. If absent, pairwise blocker compatibility forces the two rows to cover a second full \(K_5\), which exhausts their five extra incidences and forces both overlap parameters to equal one. The resulting gadget-based \(K_{12}\) has an external C-edge, contradiction.
- Independent audit checked the positive-partition enumeration for \(R_C=12\), the exceptional pair-sum cases, and the exact incidence equality \(a_i=a_j=1\). The universal cap is a proved colorwise constraint, not a full E408 or \(K_{145}\) closure.


## 2026-10-25 — \(P_C=49\) equality layer excluded; exact-129 cap improved to 48

### Main result

Proved under the retained seven-block equality and exact-129 factor contracts:
\[
\boxed{P_C\le48,\qquad R_C\ge14}
\]
for every exact-129 color \(C\). This excludes the \(R_C=13\) equality layer that remained after Theorem 14.1.

### Finite gadget alignment

- Derived/used the exact 11-vertex gadget normal form for \(s=1,2,3,4\).
- Added GADGET_ALIGNMENT_VERIFIER.js and GADGET_ALIGNMENT_CERTIFICATE.md.
- Deterministic in-session enumeration covered all subsets of the four 11-vertex graphs, all \(K_4/K_5\) cliques, all disjoint \(K_5/K_5\) pairs, all disjoint \(K_5/K_4\) pairs, and all high omitted cliques of size four or five.
- Alignment counts: 380 high-\(K_5\) checks + 1,776 high-\(K_4\) checks = 2,156 checks, zero failures. Expected clique/pair counts are asserted by the committed verifier.

### Proof structure

- \(R_C=13\) integer profiles were exhausted by maximum pair-sum: \(\le6\), \(7\), or \(8\).
- Pair-sum-seven profiles \((5,2,2,1^4)\) and \((4,3,2,1^4)\) reduce to two \(a=1\) blocks if a label edge is missing; gadget alignment gives a \(K_{12}\) with an external C-edge.
- Pair-sum-eight profiles \((5,3,1^5)\) and \((4,4,1^5)\) were split correctly into the second-component and no-second-component branches. In the latter, the six-vertex gadget coverage equality forces \(a_i=a_j=1\).
- Profile \((6,2,1^5)\): the \(r_i=6\) Case A/B alternatives are excluded by a gadget-only row; Case C is closed using the 17-incidence ceiling and the \(6+1\), \(6+2\) blocker cases.
- Profile \((7,1^6)\): full-component occurrence counts and gadget-incidence budgets reduce every branch to gadget alignment or ten disjoint \(K_{12}\)'s.

### Audit corrections made before recording the theorem

- The first draft incorrectly assumed every missing edge at pair-sum eight forces a second full component. This is not true: the remaining gadget may be a \(K_5\). The proof was corrected to handle this equality branch.
- The first draft of the \(6+1\) Case C argument incorrectly continued with a second-component charge after the one-full-component contract made that branch impossible. It was corrected to an explicit contradiction.
- The \(r_i=7\) branch was expanded to distinguish double-component rows from one-component rows and to include size-four omitted cliques; it is no longer justified by assuming a full representative exists for every component.

### Commits

- Corrected \(6+1\) Case C branch: 333cc2d6cbd48b01dde395ad8b1135b6c10a3d26
- Tightened \(r_i=6\) terminal proof: 132b7195f5c563149844bc8b0e4808f7029c1aa4
- P49 theorem and extended gadget alignment proof: 787427120154b300f5d9c7f137c5cb366cfa434a
- Canonical state update: c603fc32955bec4facfa1b734380bb947812d923
- Dependency map update: a73b899d6e15fca7427cdaef7f2f64eb5f0ed4f4

**Scope:** the \(P_C\le48\) result is a colorwise conditional theorem. E408 Q33, both four-partite and non-four-partite 56-witness terminals, and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 2026-10-25 — \(P_C=48\) boundary excluded; cap strengthened to 47

### Main result

Under the retained exact-129 factor theorem and seven-block equality contract, the colorwise duplicate cap is now
\[
\boxed{P_C\le47,\qquad R_C\ge15.}
\]
The new theorem excludes the \(R_C=14\) profiles \((6,3,1^5)\), \((6,2,2,1^4)\), \((7,2,1^5)\), \((8,1^6)\), and the all-low-budget case.

### Expanded finite alignment certificate

- Extended GADGET_ALIGNMENT_VERIFIER.js to check single-row, pair/pair, and triple alignment properties across all four exact 11-vertex gadget normal forms.
- Deterministic in-session replay: **467,696 alignment checks, zero failures**.
- Exact categories: 2,156 base \(K_4/K_5\)-to-\((55)/(54)\) checks; 312 \(K_3\)-to-\((55)\); 1,476 \(K_5\)-to-\((53)/(44)\); 10,592 fixed-\(K_5\)-plus-two-low-pair checks; 60,288 pair/pair checks excluding \(53+53\); 392,872 triple-alignment checks.
- The verifier explicitly avoids two false overclaims: not every \(53+53\) pair/pair configuration aligns, and a high \(K_4\) does not always align with a low \(53\) pair in isolation.

### Proof outline

- All \(r_i\le5\): a missing edge forces either a second full component (at least five component excess) or coverage of at least six gadget vertices. The budget \(R_C=14\) limits the omitted-pair types to the certified alignment cases.
- \((6,3,1^5)\): Theorem 11.1 Cases A/B give a fixed omitted \(K_5\); Case C either forces all component edges or aligns the high/low omitted pairs, with the \(53+53\) exception ruled out directly by the budget.
- \((6,2,2,1^4)\): Cases A/B align one \(K_5\) with two \(r=2\) pairs; Case C is handled by triple alignment or direct edge forcing.
- \((7,2,1^5)\): row-count cases \(n=0,1,2,3\) are resolved by occurrence counts, gadget incidence bounds, alignment, or ten isolated \(K_{12}\)'s.
- \((8,1^6)\): analogous \(n=0,1,2,3\) split; high gadget-only rows align, while low gadget incidence forces all component edges.

### Commits

- P48 boundary theorem: 26ef67f0a9cd139e7bfb29655987e9f5ad58a528
- Pair-sum-seven branch clarification: 9408fcd6f26f1e4b1c566192044e1e00054c497f
- Alignment certificate: 320dbcdb82bc42ae8f770084ae8c9f72491eaea2
- Alignment verifier: 2209c1764182a1aaa5b945469d8edf9fc81cffa5
- Canonical state: 4284f17c132d9cb6dc9b5dba8fdefc0f13828265
- Seven-block ledger: 5d002b324c2346afca57d770d07d6502b768118c
- Dependency map: 727e9fcd2cb56081831f9f1d5a8ac396a0a95091

**Scope:** the \(P_C\le47\) theorem is colorwise and conditional. The aggregate eleven-color ledger, both 56-witness support branches, E408 Q33, and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 2026-10-25 — post-commit proof audit and correction

A line-by-line audit found assumptions in the first P48 draft that needed repair before relying on the \(P_C\le47\) conditional bound:

1. An \(r_i=3\) block can have omitted-pair type \(55\), \(54\), \(53\), or \(44\); the type depends on the overlap \(a\), since \(r_i=a+e_i+t_i\).
2. In the \(r_i=6\), Case C branch, the two gadget-only rows are not automatically known to cover all of \(U_C\). The corrected proof tracks total repeated gadget excess \(d_U\), component-row gadget incidence \(e_i\), and the intersection of their omitted cliques. For \(d_U\le3\), a high \(53/44\) pair forces \(e_i=0\) and is therefore disjoint; a \(55/54\) profile contains a \(K_5\) that can be aligned individually. For \(d_U\ge4\), either the missing-edge incidence thresholds force the edge or \(e_i\ge4\) yields a row omitting a \(K_5\).
3. In the \(r_i=7,8\), \(n=2\) branches, representing all ten full components once does not by itself imply \(t_i=0\), because partial component incidences can remain. The corrected proof splits on \(t_i+e_i\): a large sum yields a row omitting a \(K_4/K_5\); a small sum rules out both a second full component and six gadget incidences.
4. The \(53+53\) pair/pair alignment is not universal. It is no longer used: the all-low occurrence is ruled out by the pair-sum budget, and the \((6,3,1^5)\) occurrence is closed directly from \(t_i+t_j<5\) and \(e_i+e_j<6\).

The finite gadget verifier still records 467,696 checks with zero failures. The theorem remains conditional on the retained exact-129 factor theorem and seven-block equality contract; E408 Q33 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

### Audit-correction commits

- Corrected P48 proof: 6a1b3b428f85e5600f1786f812571cbf1a7ee434
- Clarified \(r=8,n=1\) excess wording: 658b0881a69b87fb35fe713765e6fbee7b470613
- Clarified 53+53 verifier scope: 6b5b356b1c3e8c70a7b8a296d6af46863b6a2a49
- Updated alignment certificate: 06a1ff0507035e44829586a1f543b63643a957ae
- Updated seven-block ledger: 7416d7ff2834190e517bcc1a5363bd6b07cfbb2f
- Updated dependency map: cb48797b4b8579ea54e5ff5b0c754b6e0040b291


## 2026-10-25 continuation — inner-core \(S_0=12\) equality excluded; outer-star audit correction

### New conditional inner-core theorem

Added R12_E408_Q33_S0_12_EXCLUSION.md. Under the retained T61, exact-129 factor, and 31-point/56-witness contracts, the case \(S_0=\epsilon_U+2\delta=12\) is impossible, improving the universal minimum-support bound to
\[
\boxed{S_0\ge13,\qquad \delta\ge5.}
\]
The four-partite branch retains its separate stronger \(S_0\ge22\) result.

The proof uses the exact row identity \(s_r=3+g_r-a_r\), the degree sum \(\sum_Wq_w=126\), and the \(T\)-to-\(W\) degree ledger. The possible \(q_w\) profiles reduce to 14 cases after imposing \(0\le\epsilon_T\le4\) and the degree constraints at zero-excess points of \(T\). Each case is excluded by multiplicity of the three R-only 8-transversals, a special-incidence lower bound, or a \(K_{12}\) contained entirely in \(H\), contradicting \(\omega(H)\le11\).

Added verify_s0_12_exclusion.py. An independent replay of its finite arithmetic logic returned exactly 14 canonical degree profiles; the row identity \(8m=84-\epsilon_T-A\), multiplicity partitions for \(m=8,9,10\), and the uncovered-point incidence bounds all passed. This is arithmetic verification only, not a machine proof of the graph lemmas.

### Important cross-branch correction: outer isolation lemma invalid

The sibling unified-witness-capacity audit exposed a false inference in the former outer Lemma 13.1: a monochromatic \(K_{12}\) need not be isolated. The correct star condition is only \(d_C(z,K_{12})\le1\) for every outside vertex \(z\); a single external \(C\)-edge is allowed.

Accordingly:
- withdrew Sections 13–16 from the active SEVEN_BLOCK_INCIDENCE_LEDGER.md and preserved them in ARCHIVE_UNCERTIFIED_OUTER_CAPS_20261025.md;
- marked P49_BOUNDARY_EXCLUSION.md and P48_BOUNDARY_EXCLUSION.md as **NOT CERTIFIED — AUDIT HOLD**;
- corrected CANONICAL_STATE.md and PROOF_DEPENDENCIES.md so \(P_C\le49\), \(P_C\le48\), and the \(P_C=50,r_i=6\) corner are not used as proved dependencies until repaired.

This correction does not affect the new inner-core \(S_0\ge13\) theorem: its \(K_{12}\) contradictions occur inside \(H\) and use \(\omega(H)\le11\), not an external-edge argument.

### Current blocker

E408 Q33 remains OPEN / NOT_CERTIFIED. The four-partite support branch has \(S_0\ge22\); the general 31-point/56-witness boundary has \(S_0\ge13\). The remaining task is a valid global compatibility contradiction linking the inner witness structure to the outer seven-block/color system, without relying on the withdrawn single-external-edge inference.

### Commits

- Inner theorem proof audit: a1cc059324df01bfa1afec5bf20ba7a1194dd249
- Arithmetic verifier: 4093c6f03aa5ca60f80765264e90590cdf85d5f1
- Active ledger audit correction: c80e36782de9a0dfb5a6eb3b8059aa343e136774
- Archived uncertified outer-cap drafts: a0a8f21d872b261b24580ad5e9f15942046cc74f
- P49/P48 audit holds: a11d93b8d9a3cd58aa7f6f8da58ae3e90def8391; cfcb8f70f856dd742d3a658551b97f5d65e17fb3
- Canonical state update: 5b82013a9b6200480d10b574d750eb7d7c8070bb
- Dependency map update: c7fc225531eea0eeec8720864b667dcacf9a19fe


## 2026-10-25 continuation — repaired \(P_C=50,r_i=6\) corner with double-star

The outer-star audit initially withdrew the former \(P_C=50,r_i=6\) proof because it treated a single external \(C\)-edge from a monochromatic \(K_{12}\) as impossible. This continuation repairs that exact corner rather than restoring the invalid lemma.

**Theorem added:** under the retained exact-129 factor theorem, seven-block row contract, gadget normal form, and \(r=1,6\) row classifications, the profile \(P_C=50,\ r_i(C)=6\) is impossible.

- The identity \(P_C+R_C=62\) forces \(R_C=12\), so the other six block budgets are all \(r_j=1\).
- Select one no-component row from the \(r=6\) block and one no-component row from each \(r=1\) block.
- The exact gadget alignment predicate supplies a \(K_5\) clique \(D\) disjoint from all seven omitted gadget sets; pairwise intersections of the omitted sets give a valid pairwise-blocker proof that the seven rows plus \(D\) form a monochromatic \(K_{12}\).
- The verifier supplies a gadget vertex \(z\) adjacent to the high row and also either to \(D\) or to a selected low row. Hence \(d_C(z,K_{12})\ge2\), contradicting the correct star-capacity bound \(d_C(z,K_{12})\le1\).

Added R12_P50_R6_DOUBLE_STAR_EXCLUSION.md and verify_p50_r6_double_star.py. The finite replay passed 204 Case-A/B and 49,008 Case-C configurations, 49,212 total, zero failures. The script verifies the gadget alignment predicate only; row classifications and the exact-129 factor theorem remain explicit dependencies.

Cross-branch reconciliation also found a separate conditional sibling theorem excluding \(P_C=49,r_i=6\) via the same double-star method: workstream/r12-unified-witness-capacity-20261025, OUTER_EXCEPTIONAL_ROW_COUPLING.md §12, verifier blob 23cd4ef874faadbd5931c5e3553a1a55415c7a79. This is a local corner result, not a universal cap.

**Important remaining limit:** the other \(P_C=50\) profiles \((5,2,1^5)\), \((4,3,1^5)\), the other \(P_C=49\) profiles, and the claimed \(P_C=48\) boundary remain NOT CERTIFIED because their existing proofs still use single-external-edge contradictions. E408 Q33 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.

### Commits
- P50/r6 double-star theorem: 07b6891eefac7163b1a0fbc1c2529126c2b5b1d7
- P50/r6 finite verifier: 2c42edbf6996bc733f7df1ee5a182c5e8954447e
- Active ledger update: e714b150a0d63fff1b7fa295fd8fa372e91c6950
- Canonical state update: 14024726e042bd167ac6da444a8b0a61f0f6ecfd
- Dependency map update: 5a01f8e4614e70fe4c3582b56d701ba6c7011471


## 2026-10-25 continuation — exclude \(P_C=50\) profiles \((5,2,1^5)\) and \((4,3,1^5)\)

Built on the corrected double-star method rather than the withdrawn isolation lemma.

For \(P_C=50\), \(R_C=12\). The remaining high positive profiles after the \(r_i=6\) corner are \((5,2,1^5)\) and \((4,3,1^5)\). For each profile, choose one no-component row from each of the two non-\(r=1\) blocks and one from each of the five \(r=1\) blocks. The gadget verifier finds a \(K_5\) \(D\) disjoint from all selected omitted complements, with all pairwise intersections needed for the blocker argument, and an outside gadget vertex \(z\) that sees the high row and at least one more vertex of the \(K_{12}\). This yields \(d_C(z,K_{12})\ge2\), contradicting the correct \(d_C(z,K_{12})\le1\) bound.

The component-incidence budget is the key proof safeguard. For a block with omitted-complement sizes \(s,t\), \(a=11-s-t\) and the total partial component incidence is at most \(r-a\). The only dangerous cases are when both non-\(r=1\) blocks have complement profile \((5,5)\); then the verifier exhausts all allocations \(p_1+p_2\le r_H-a_H\) and \(q_1+q_2\le r_Q-a_Q\), requiring an aligned choice with \(p_H+q_Q\le4\). All other complement-profile pairs have combined budget at most four already.

Added R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md and verify_p50_remaining_high_profiles.py. Independent replay passed:
- \((5,2,1^5)\): 512,618 non-sensitive plus 150 sensitive base configurations;
- \((4,3,1^5)\): 1,143,930 non-sensitive plus 150 sensitive base configurations;
- 1,656,848 base configurations total, zero failures, with every sensitive case expanded over all component-incidence allocations.

Combining the \(P_C=50,r_i=6\) theorem with the two high-profile double-star exclusions leaves the four correct profiles \((4,2,2,1^4)\), \((3,3,2,1^4)\), \((3,2,2,2,1^3)\), and \((2^5,1^2)\). The earlier list used \((4,2,2,2,1^3)\) and \((3,2,2,2,2,1^2)\), both of which sum to 13 rather than 12. The four correct low profiles are now excluded by the common-star theorem below; the colorwise cap \(P_C\le49\) is conditionally established, while \(P_C\le48\) remains NOT CERTIFIED.

### Commits
- Remaining high-profile theorem: 4a1bd39ba4e08854fd35907d051a44451259b07c
- Remaining high-profile verifier: d33fe53aa7cd63f1fff9cb337231e39e449b28d7
- Active ledger update: 682ea469f41a31d07573ee6ec08c31f6ad27294e
- Canonical state update: 455673197a67288520f8528c753a5aa5d5e5feec
- Dependency map update: 087aba82e410b86b0750493d5835ea8da5d8800f


## 2026-10-25 continuation — common-star theorem establishes conditional \(P_C\le49\)

### Finite gadget certificate

Added R12_HIGH_P_COLOR_CAP_COMMON_STAR.md and verify_high_p_common_star.py. For each of the four exact 11-point gadget normal forms, the verifier enumerates every disjoint clique pair with the registered complement-size profile for budgets \(r=1,\ldots,5\). A pair's candidate set consists of all \((D,w)\) such that \(D\) is a gadget \(K_5\), \(w\notin D\), and one complement contains \(w\) while avoiding \(D\).

The dynamic program takes every intersection of candidate sets over all seven-block budget profiles with \(1\le r_i\le5\) and \(\sum_i r_i\le12\). It checked 18 sorted profiles across four normal forms (72 cases), 2,405,684 transitions, and at most 2,625 reachable intersection states. No empty intersection occurred. I independently replayed the same finite logic in Python: all 72 profile/form pairs passed, with the same 2,405,684 transition count and maximum state count 2,625.

### Mathematical consequence

For every allowed row-pair tuple in this range, there is a common \(K_5\) \(D\) and common gadget point \(w\) contained in one selected complement from every block, with all selected complements disjoint from \(D\). If every pair of selected rows has at most four partial component incidences in total, then their complements intersect at \(w\), so the pairwise-blocker theorem forces the seven rows to be pairwise \(C\)-adjacent. Together with \(D\), they form a monochromatic \(K_{12}\).

Each selected complement is a proper subset of the six-point set \(U_C\setminus D\), so the seven omission sets have total size at least seven. Pigeonhole gives an external gadget vertex omitted by at least two selected complements, hence \(C\)-adjacent to at least two vertices of the \(K_{12}\). This contradicts the valid star-capacity bound \(d_C(z,K_{12})\le1\), not an invalid isolation claim.

- \(P_C\ge51\): \(\sum r_i\le11\), so \(r_i+r_j\le6\) for every pair and the component-incidence budget is at most four.
- \(P_C=50\), \(\max r_i\le4\): the four correct profiles are \((4,2,2,1^4)\), \((3,3,2,1^4)\), \((3,2,2,2,1^3)\), and \((2^5,1^2)\); they also satisfy the pairwise budget condition.
- \(P_C=50\), \(\max r_i\ge5\): \((6,1^6)\) is closed by the \(r_i=6\) double-star theorem; \((5,2,1^5)\) and \((4,3,1^5)\) are closed by the incidence-sensitive double-star verifier.

Therefore every exact-129 color satisfies the conditional cap
\[
\boxed{P_C\le49,\quad R_C\ge13.}
\]
This is a corrected proof independent of the withdrawn outer-isolation lemma. The old attempt at \(P_C\le48\) (excluding \(P_C=49\)) remains NOT CERTIFIED because its single-external-edge inference is invalid. E408 Q33, E407 Q32, E408 Q32, and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.

### Arithmetic audit note

The seven positive profiles summing to \(R_C=12\) are exactly
\[
(6,1^6), (5,2,1^5), (4,3,1^5), (4,2,2,1^4),
(3,3,2,1^4), (3,2,2,2,1^3), (2^5,1^2).
\]
This correction supersedes the two incorrect profile strings in the preceding log entry and the earlier draft of R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md.

### Commits
- Common-star verifier: c413b1065e9926d00ad1319f2e8d8a815e4850b5
- Common-star conditional cap theorem: 04b5ec6f9a1e118faee2216208e1f13361fb8d43
- Corrected active incidence ledger: 1a41ecfc88e25207d0f52e52d43e4a48a76b4dc6
- Corrected high-profile theorem: d55d0e43a1b17fd9ef2b5dd7971560f1dcc4025d
- Updated proof dependency map: 94f0edd87b05f28d271bfc611fbf882ecb8f8cb0
