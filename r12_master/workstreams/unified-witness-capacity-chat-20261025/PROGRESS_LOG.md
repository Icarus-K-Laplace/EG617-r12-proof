# Progress log — unified witness-capacity

## 2026-10-25 — initial cross-terminal theorem and exact audit

- Refreshed the current source heads for emergency sprint, ultimate closure/E408 Q32, zero-excess witness, E407 Q32 terminal, and witness-packing. No sibling branch or file was modified.
- Proved a shared-label disjointness theorem: two witnesses with the same B-row or pivot label cannot share a core vertex. Thus any one label occurs at most floor(v/4) times.
- At E408 Q33, the support has 31 vertices but there are eight exact-129 colors; the seven pivot-labelled witnesses, if one per color, would need 32 distinct support vertices. Therefore at least one color has seven B-labelled witnesses. Together with total excess four this strengthens the zero-excess B-labelled count to at least 17. E407 has at least 14.
- Audited the robust zero-excess theorem: on a 284-edge core, H0-T has an independent four-set for every |T|<=6; on a 285-edge core, only |T|<=4 is certified. Hence every pair of regular B rows has a common unlabelled witness in the 284-edge cases, but not automatically in E408 Q32.
- Derived the omission identity P_int=binom(c,2)(28-sigma)+Omega and the per-vertex degree inequality d_H(x,W)>=max(0,13-v+3r_x+epsilon_x). This yields the common omission-capacity inequality and exact finite profile tables. E408 Q33 improves Omega<=66 to Omega<=48, with Omega<=24 for S0=12,13,14.
- Audited edge ownership: internal Q-pairs are unique complement edges; shell-label-to-core edges are non-target-colored and are not part of e(H); core crossing edges may be charged repeatedly and have exact multiplicity r_x r_y.
- Added a scalar-relaxation gap audit. Explicit E407 and E408 integer profiles satisfy all current omission/cross-edge/core-capacity inequalities; these are not graph counterexamples.
- Exact remaining blocker: graph-theoretic common witnesses are not automatically exact-129 color components. A separate label-transfer/component-realization lemma or sharper hub-capacity/incidence-design theorem is needed.
- Status remains OPEN / NOT_CERTIFIED.


## 2026-10-25 — finite arithmetic replay

- Independently replayed the exact endpoint-gap tables, all E407 omission-profile maxima for S=9..32, all E408 Q33 omission-profile maxima for S0=12..34, the two edge-ledger examples, and the 8-by-10 label-count matrix in local Python.
- Result: R12_UNIFIED_WITNESS_CAPACITY_ARITHMETIC_OK. This validates only the integer/degree ledgers and finite profile search; it is not a graph search and does not certify realization of the witness hypergraph.
- Corrected the shell-row note to restrict the per-row capacity-three statement to zero-excess witnesses, because the regular-row degree cap is only certified on H0.
- Latest workstream head before this log update: cbd0cdf950cc8c8c74d06fee26122b5fe2dff44c.


## 2026-10-25 — labelled four-partite capacity continuation

- Refreshed the current Q33 global-compatibility result (read-only sibling head df396de8ffc1f9c390fe3e240d0d085715f86b5b): under the four-partite contract it proves \(S_0\ge22\), so \(9\le\delta\le17\).
- Proved a per-part label-row capacity lemma: if a shell label b occurs in n_b selected transversals of a four-partite L, then its target neighborhood avoids n_b vertices in every part, giving \(|D_b\cap V_j|\le |V_j|-n_b\).
- In the Q33 four-partite branch, the 56 edge-disjoint transversals force multiplicities \(r=8\) on the size-seven part and \(r=7\) on all three size-eight parts. The omission profile is exactly \((0^7,1^{24})\), so \(\Omega=0\) and the eight color omission triples partition the 24 large-part vertices.
- Derived a labelled shell-row cap on the size-seven part: the eight incident witness labels are distinct, so each such point has at most three B-row target neighbors (at most two without a pivot-labelled witness), giving \(e_F(B,D)\le14+P\le21\). Combining with \(K_B\ge22-\beta\) yields the explicit lower bound \(e_F(B,H\setminus D)\ge\max(0,8-\beta+G_B-P)\). It remains compatible with current budgets.
- Proved that the generic crossing-edge lower bound is exactly saturated by within-part edges in any four-partite witness branch. For Q33, the weighted crossing load is \(5460+49(24-\delta)\), whereas the generic lower bound is exactly 5460. Thus edge-charge summation alone cannot exclude the four-partite branch.
- Updated the exact-arithmetic verifier with partite multiplicity, omission, label-row and edge-load checks. Replayed the new arithmetic independently in Python: NEW_PARTITE_LABEL_CAPACITY_ARITHMETIC_OK.
- Minimal remaining gap is now more specific: a contradiction must either force a labelled restriction on the unused cross-part pair slots / shell rows in the four-partite branch, or prove a packing/stability exclusion for the non-four-partite 56-K4 system. No graph counterexample or full EG617 proof is claimed.


## 2026-10-25 — shell-row multiplicity audit

- Added the exact multiplicity parameter \(\mu(Q)=|\{b\in B:Q\cap T_b=\varnothing\}|\) for a common graph-theoretic witness. A fixed Q can represent at most \(\binom{\mu(Q)}2\le45\) row pairs; the regular-row degree cap does not give a smaller universal multiplicity bound.
- For a selected exact-129 witness labelled b, the label anchors it directly only to pairs containing b, at most \(\mu(Q)-1\le9\) pairs. Arbitrary pair witnesses from the zero-excess theorem remain unlabelled, so they cannot be charged to the exact-129 component budget without a label-transfer lemma.
- Re-recorded the hub-complete implication: if the two rows' missing-hub sets cover S, any common independent-four witness must hit all three hubs. The template counts 39/17/39/9 are pair certificates, not distinct Q sets.
- The strict multiplicity audit closes a potential overcounting error but does not yield a contradiction. Status remains OPEN / NOT_CERTIFIED.


## 2026-10-25 — label-only relaxation audit

- Constructed an explicit 8-by-7 label array for the Q33 four-partite contract: seven pivot rows use p once plus six distinct B labels, one non-pivot row uses seven B labels, every D column uses p plus all seven B labels, and each of the seven B labels and p occurs seven times.
- Independently checked row distinctness, column distinctness, and symbol frequencies. Result: all checks pass.
- Scope warning: this is only a label-array relaxation. It does not assign the actual three large-part coordinates of the 56 witness K4s and therefore is not a witness-hypergraph realization. It proves that label counts alone cannot close the four-partite branch.
- Added the label-array check to the independent arithmetic verifier.


## 2026-10-25 — exceptional-row cross-block coupling

- Refreshed E408 Q33 sibling head fec0100abbb6124d1efdad39f2f4b352e1c8bc76; its exceptional-row refinement is conditional on the exact-129 Type-I factor theorem and remains OPEN.
- Proved a new conditional block-pair inequality. For two low-slack blocks, each nonempty intersection between their exceptional complement cliques forces the corresponding exceptional-row edge to be C-colored. Together with the ten component-representative matching edges and the requirement that every row/column has at least one C edge, this yields:
  d_ij(C) >= k + max(2-ell, 2-c) - 2,
  where k is the number of nonempty cells in the 2x2 intersection mask and ell/c are its occupied row/column counts.
- Exhaustively checked all 15 nonempty 2x2 masks: one-cell and matching patterns cost zero; adjacent two-cell and three-cell patterns cost one; the full mask costs two. Independent replay passed (EXCEPTIONAL_ROW_MASK_REPLAY_OK).
- Derived the cross-color budget sum_C eta_ij(C) <= 12 for each block pair, because the seven-block near-Latin ledger has exactly 12 duplicate units per block pair.
- This creates a precise finite interface between exceptional gadget geometry and outer duplicate budgets. It does not close the terminal because the same/matching complement pattern can persist without forcing positive duplicates.
- Updated only this workstream's verifier and notes; no sibling paths changed.


## 2026-10-25 — exceptional-row alpha-two theorem

- Proved that the graph induced by all exceptional rows of one exact-129 color across low-slack blocks has independence number at most two. A hypothetical independent triple has pairwise-disjoint complementary gadget cliques of total size 9–11, hence at least 22 incidences into the 11-point gadget; the three row neighborhoods have at most24 total incidences (at most22 when two rows share a block), leaving at most two component incidences. They cannot cover any isolated K5 component, so one vertex from each of ten components plus the triple would form an independent13-set.
- Therefore, for every low-slack block pair, the non-C edges among the two exceptional rows on each side form a matching, and at least two C edges are present among those four vertices.
- Across k low-slack blocks, the exceptional-row graph has at least k(k-1) C edges. Equality in the alpha<=2 Turan bound forces two disjoint K_k cliques, with opposite exceptional-row types in each block.
- Independent arithmetic replay passed: EXCEPTIONAL_ROW_ALPHA2_REPLAY_OK. The equality structure remains feasible and does not itself close Q33.


## 2026-10-25 — near-complete component matching across outer blocks

- Refreshed E407, E408 Q33, E408 Q32, witness-packing, zero-excess, and ultimate-closure branch heads before continuing. No sibling branch or directory was modified.
- Used the latest Q33 Theorem 10.1 (exact-129 row normal form for \(r_i(C)\le5\)) to strengthen the cross-block component-matching statement. Each block has ten unique component rows and two exceptional rows; total neighborhood incidence beyond the baseline 62 is \(r_i(C)-1\).
- For a missing same-component diagonal between blocks i,j, the two corresponding row neighborhoods must spend at least five extra incidences: either cover another entire K5 component, or cover at least six vertices of the 11-point gadget so that no independent pair remains. Distinct missing labels use disjoint row-incidence charges.
- Since \(r_i+r_j-2\le8\), at most one of ten same-component diagonals can be missing for any pair with \(r_i,r_j\le5\). This gives at least nine same-label component edges; when \(r_i+r_j\le6\), all ten remain forced. At the sum-seven boundary, a missing diagonal consumes exactly five extra incidences and must cover a second K5.
- Added arithmetic verifier checks for all 25 row-budget pairs and the sum-seven boundary. Scope: exact arithmetic check plus a conditional analytic lemma, not a graph-realization certificate.
- Current obstruction: this near-matching theorem does not bound how many extra cross-label edges can occur in the 21 block pairs, nor does it force the missing diagonal patterns to contradict the witness labels. Terminal status remains OPEN / NOT_CERTIFIED.


## 2026-10-25 — missing component diagonal charged to duplicate budget

- Strengthened the near-matching result to \(m_{ij}(C)\le d_{ij}(C)\) for every exact-129 color and every pair of outer blocks with \(r_i,r_j\le5\).
- Proof audit: if one same-component diagonal were missing and \(d_{ij}=0\), the 12 cross-block C edges would form a perfect matching. The unmatched component rows must be paired with exceptional rows, leaving an independent triple consisting of one exceptional row on one side and both exceptional rows on the other. The missing diagonal consumes at least five of the combined extra-incidence budget \(r_i+r_j-2\le8\); at most three extra incidences remain, too few to cover a full K5 component. The triple plus one vertex from each of the ten components yields a C-independent 13-set.
- This closes the prior local gap where component rows could have been paired to exceptional rows. Every missing same-component label alignment now consumes at least one duplicate unit \(d_{ij}(C)\); summing gives \(\sum m_{ij}(C)\le P_C\) over low-budget block pairs.
- Independent Python replay passed over all 25 integer pairs \(r_i,r_j\in[1,5]\), including the four sum-seven boundary pairs.
- Remaining gap: the duplicate budget \(P_C\) can still be large enough to pay for all possible mismatches; no terminal has been eliminated by this result alone.


## 2026-10-25 — scalar budget relaxation identifies the next gap

- Constructed an explicit integer relaxation satisfying all aggregate seven-block budget identities: each color has \(P_C+R_C+s_C=62\), total \((\sum P,\sum R,\sum s)=(252,427,3)\), every block has \(\sum_C r_i(C)=61\), and every block pair has \(\sum_C d_{ij}(C)=12\).
- In the relaxation, all eight exact colors have \(P_C=9,R_C=53,s_C=0\) and every block row parameter \(r_i(C)\) is 7 or 8. The three nonexact colors absorb \(P=(59,60,61)\), \(R=(2,1,0)\), and \(s=(1,1,1)\).
- Verified an explicit 8-by-7 row-parameter matrix and an 11-by-21 duplicate matrix; all sums match exactly and all \(d_{ij}(C)\) are within [0,12].
- This is not a graph realization. It proves only that aggregate budgets cannot force an exact color to \(P_C\ge36\) or trigger the component-matching theorem. The missing step is a structural inequality linking nonexact-color residual graphs / witness labels to outer-block duplicate assignments.


## 2026-10-25 — duplicate-budget to monochromatic K12 packing

- Proved a general exact-129 packing bound. For block i, if \(n_i(C)\) rows have C-neighborhood size five in R, the exact blocker theorem gives distinct K5 component labels and \(n_i(C)\ge11-r_i(C)\). Thus at least \(17-R_C=P_C-45\) component labels occur as exact size-five blockers in all seven blocks.
- Every common component label extends to a C-monochromatic K12: its K5 component plus one exact size-five blocker row from each outer block. If two representatives were nonadjacent, the nine other K5 components, an independent pair in the gadget, and the two rows would form an independent13-set.
- Concluded \(\nu_{12}(C)\ge\max(0,P_C-45)\). Combined with the near-matching theorem, \(P_C\ge51\) yields ten disjoint K12s; the \(P_C=50\) and \(P_C=49\) branches have the explicit bounds recorded in the canonical theorem.
- Added exhaustive integer-profile checks for \(R_C=11,12,13\) with all \(r_i\le5\): the maximum number of block pairs with \(r_i+r_j\ge7\) is 0, 1, 2. Independent Python arithmetic replay passed (see final audit below).
- This is a structural branch certificate, not a contradiction: the coloring hypothesis allows monochromatic K12 cliques. The unresolved issue remains forcing the aggregate duplicate budget into a branch whose K12 packing or witness geometry is impossible.


## 2026-10-25 — final audit for this continuation

- Independent Python replay passed for the exact-profile enumeration: \(R_C=11,12,13\) yield 210, 455, and 875 profiles with \(r_i\le5\), and maximum counts of pairs with \(r_i+r_j\ge7\) equal 0, 1, and 2.
- Independent Python replay also passed the scalar budget relaxation and the formula \(\max(0,17-R_C)=\max(0,P_C-45)\).
- Created TERMINATION_CLOSURE.md. It explicitly preserves OPEN / NOT_CERTIFIED, distinguishes analytic lemmas from arithmetic checks, and names the missing bridge: label transfer, near-exact-color structure, or a global labelled incidence inequality.
- Latest sibling heads were refreshed and recorded in CANONICAL_STATE.md. All changes remain confined to this workstream; no full graph realization or original K145 proof is claimed.


## 2026-10-25 — labelled selected-witness K12 extension

- Intersected the seven selected witness components of an exact-129 color with the common size-five blocker component set across all seven outer blocks.
- Since the latter has size at least \(P_C-45\) in a ten-component universe, inclusion-exclusion gives at least \(\max(0,P_C-48)\) selected witness components that extend to a monochromatic K12.
- Thus \(P_C\ge49\) forces at least one selected witness-labelled K12, and \(P_C=50\) forces at least two. This is a labelled incidence result, not an unlabelled packing count alone.
- Added the threshold arithmetic to the verifier and restricted it to the feasible exact-color range \(P_C\le55\).
- The aggregate scalar relaxation still permits every exact color to have \(P_C=9\); therefore this result identifies a useful branch but does not force entry into it.


## 2026-10-25 — last sibling-head refresh

- E407 Q32 branch advanced again to bd385f7dfe102deb426810baf1999a8e94dd488f. The latest canonical state now excludes both the \(\delta=16\) and \(\delta=15\) four-partite extremes; E407 remains open on templates A–E, the \(\delta=14\) compatibility branch, and the low-excess non-four-partite branch.
- E408 Q33 remains at a6bbb918c3484bedd1a4eafb410901288cdff085 with the \(r_i=6\) row classification; E408 Q32, witness-packing, zero-excess-witness, and ultimate-closure heads were also refreshed and recorded in CANONICAL_STATE.md.
- This workstream remains isolated: the repository compare against the initial head shows changes only under r12_master/workstreams/unified-witness-capacity-chat-20261025/.


## 2026-10-25 — top-cell-A cross-layer theorem

- Refreshed sibling heads: E407 Q32 bd385f7dfe102deb426810baf1999a8e94dd488f; E408 Q32 a0ba6db26c7e8b00a4217dcbcbf298895dff93ce; E408 Q33 a6bbb918c3484bedd1a4eafb410901288cdff085; witness-packing f5d3daa07403877ede9885e1bd5c2f46b16d81da; zero-excess 07d19abfd6c1c749c7360526e4a04a3eb865fb2e; ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40.
- Combined the sibling \(|W|=23\), \(e_F(W)=132\), near-perfect-matching cell with the exact-129 factor theorem. Every exact color's ten K5 components intersect W in profile \(2^{10}\) or \(2^9,1\); its gadget intersects W in 3 or 4 vertices and contributes respectively one or two W-edges.
- Proved the exact global cross-edge defect identity \(\sum_C t_C=K_W\) for E408 and \(K_W+1\) for E407, where \(t_C=e_C(O)-42\ge0\), \(O=V(F)\\W\), and \(K_W\) is the target degree excess inside W.
- Proved \(0\le t_C\le6\) for every exact-129 color. At \(t_C=0\), equality in the 38-vertex Turan floor forces C[O] to be ten triangles plus two K4s.
- Added finite arithmetic checks for both intersection profiles, the 42-edge Turan floor, the exact-color t-cap arithmetic, and the global identity for every possible \(K_W\).
- Status remains OPEN / NOT_CERTIFIED: the new ledger is an exact coupling but does not itself prohibit a feasible \(t_C\) distribution or the resulting partial clique-partition design.


## 2026-10-25 — classify Type-A gadget at zero defect

- In the \(t_C=0\), Type-A case, the gadget splits as \(U[O]=K_4\cup K_4\) and \(U[W]=K_2\cup K_1\). Its cross-edge count is exactly 16.
- The alpha/omega constraints and exact cross-edge count force a four-valued parameter \(a\in\{0,1,2,3\}\): one matched W endpoint has degree \(5+a\), the unmatched W gadget vertex has degree \(8-a\), and the remaining nine gadget vertices have degree five.
- Thus the gadget degree multiset is \(5^{10},8\) or \(5^9,6,7\); all eleven gadget vertices have degree at least five. The independent Python arithmetic replay passed all four profiles.
- This is a conditional local classification only. The remaining global obstacle is still to show the 11 color partitions on O cannot coexist with the target degree and witness constraints.


## 2026-10-25 — identify the repeated-color vertex in each r_i=1 block

- Combined the top-cell-A intersection profile with the exact row theorem for \(r_i(C)=1\). The ten component rows are exact K5 neighborhoods and the two exceptional rows are complements of disjoint K5s in the gadget.
- The component rows contribute 20 W incidences in Type A or 19 in Type B. The two exceptional rows contribute 3/4 or 4/5 respectively, so total \(e_C(B_i,W)\) is exactly 23 or24.
- Since every vertex w and every target block B_i must see all eleven non-target colors among the 12 incident edges (else B_i∪{w} is a forbidden independent 13-set in a missing color), exactly one non-target color is repeated at each (w,B_i). Thus the unique C-duplicate for \(r_i(C)=1\) lies in W iff \(e_C(B_i,W)=24\), and in O iff the count is23.
- Refreshed E408 Q33: c01f7dc6951b2bb7ea5209f252b1644ca0ecd40a adds exact gadget clique normal form and strengthened high-budget packings; no closure claimed.


## 2026-10-25 — sibling external-edge contradiction closes the P_C=50, r_i=6 corner

- Refreshed E408 Q33 to 8b4bfef7a9e3d957c7150af30aadba703a08d31f and read its new external-edge proof.
- Lemma 13.1: any monochromatic K12 is isolated in its color, because the 12 edges from an outside vertex to the clique must contain all eleven other colors, leaving no edge of the clique's color.
- Lemma 13.2: \(m\) disjoint color-C K12s, each using one vertex from every outer block, force \(P_C\le21(12-m)\) by the one-or-two rule on the remaining block vertices.
- Theorem 13.3 eliminates \(P_C=50,r_i=6\): cases A/B produce a K12 with an external color-C edge; case C either does likewise or forces ten isolated K12s and \(P_C\le42\).
- Therefore any exact color with \(P_C=50\) has all \(r_i\le5\), and the existing low-budget theorem yields at least nine common component labels. \(P_C=49,r_i=6\) is not yet excluded.


## 2026-10-25 — finite gadget contradiction excludes \(P_C=49,r_i=6\)

- Added Theorem 12.1 to OUTER_EXCEPTIONAL_ROW_COUPLING.md. For \(P_C=49\), the residual block budget is \(R_C=13\), so an \(r_i=6\) block leaves five \(r=1\) blocks and one \(r=2\) block.
- Built a finite exact verifier over all four 11-vertex gadget normal forms. It enumerates all disjoint K5/K5 pairs for \(r=1\), K5/K5 and K5/K4 pairs for \(r=2\), and all admissible \(r=6\) Case-C complement pairs. For each configuration it finds a common K5 core and seven outer representatives whose omitted sets pairwise intersect; the high row then has an external same-color edge from the resulting K12.
- Ran the committed checker locally: PASS for all 159,244 checks (380 A/B and 158,864 C checks). No floating-point arithmetic or external library is used.
- This closes the \(P_C=49,r_i=6\) corner conditionally on the retained reduction/gadget/row contracts. It does not close EG617.
- Using sibling Q33's \(P_C\le49\) theorem, the \(P_C=49\) profiles now reduce to the open \(r=7\) profile \((7,1^6)\) and four all-\(r\le5\) high-pair profiles: \((5,3,1^5)\), \((4,4,1^5)\), \((5,2,2,1^4)\), and \((4,3,2,1^4)\). Five all-\(r\le5\) profiles with every pair sum \(\le6\) are excluded by ten isolated K12s and the \(P_C\le42\) cap.


## 2026-10-25 — corrected external-star logic and strengthened P49/r=6 finite check

- Audited the current E408 Q33 P49 boundary proof. Its Lemma 2.1 incorrectly infers that a monochromatic \(K_{12}\) has no external edge of its own color. The exact star count proves only \(d_C(z,K_{12})\le1\); one external \(C\)-edge is allowed. Sibling conclusions relying solely on one external \(C\)-edge, including \(P_C\le49\) and \(P_C\le48\), are not certified as written.
- Rewrote the local \(P_C=49,r_i=6\) argument to use a double-\(C\)-edge contradiction. Added the safe-row incidence split for Cases A/B/C and restricted the verifier to the exact Case-C complement profiles from the row theorem.
- Replayed the finite predicates: 2,132 Case-A/B configurations and 412,768 exact-profile Case-C configurations passed. The checker tests both high-row choices for the risky \((5,5)\) and \((5,4)\) profiles; other profiles have at most three total partial component incidences and admit either safe high row.
- Scope remains conditional: this excludes only the \(P_C=49,r_i=6\) corner under the retained exact-129/gadget/row contracts. It cannot be combined with the sibling \(P_C\le49\) cap until that cap is independently repaired. The original \(K_{145}\) theorem remains OPEN / NOT_CERTIFIED.
