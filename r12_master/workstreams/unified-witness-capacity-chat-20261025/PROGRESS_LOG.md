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
