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
