# R12 proof DAG — current audited version

Headline target: original balanced coloring of K145 -> contradiction.

1. Assume a balanced 12-coloring of K145.
2. Choose a least-edge target color G; e(G)<=870. [PROVED by counting]
3. Apply the FRONTEND_BRIDGE_THEOREM anchor/block recurrence. Its 1752-node, 144-stop certificate is repository-reported; this workstream has not rerun the generator/verifier. [SOURCE_REPORTED / REPLAY NOT DONE]
4. The recurrence's contextual split is induced R(4,49) or embedded T61. [SOURCE_REPORTED under F6–F8]
5. R(4,49) branch: under the exact F5 original-coloring contract, delta(F)>=13 and alpha(F)<=4. The target has at least319 edges; each other color has at least79, forcing target edges at most307. Contradiction. [PROVED_CONDITIONAL on F5 and second-Turan theorem]
6. Therefore the only live original-proof branch is embedded T61, provided steps 3–5 retain their exact contracts.
7. T61:
   - E397–E406: repository-canonical closure under stated contracts.
   - E407: sharp Cell-B |W|=23 subcase excluded; Q32 five-template / common-K11 versus 284-core completion remains OPEN.
   - E408: sharp Cell-B |W|=23 subcase excluded; Q32 and Q33 seven-block/color-factor compatibility remains OPEN.
8. Hence the original proof currently terminates at an unexcluded T61 state. [OPEN]

Parallel abstract backend DAG (not silently identified with the T61 branch):
- Legal abstract R(4,49) -> degree-13 pivot -> 35-core H and E-layer.
- E333 conditional closure; E334 source-reported forcing closure with independent graph obstruction; E335–E340 OPEN.
- If the contextual R(4,49) contradiction is accepted as an original-coloring lemma, this abstract branch is not a required branch in the original theorem DAG, although its independent classification remains open.

No cycle is used in this DAG. V11/V12 finite-state certificates are now independently replayed and COMPUTATION_CERTIFIED. Their analytic exclusion rules retain their stated contracts; no completed parent graph is claimed. V8/E334 package-level forcing bridge remains source-reported pending replay.

## Added proved interface node (does not close a terminal)

T61 shell/core witness lemma
- Inputs: contextual no-R(4,49), alpha(H)<=4, omega(H)<=11, and the hereditary D(n) target-edge cap.
- Outputs: t_a<=7 => an independent 4-set in H anticomplete to a; at least eight shell rows are good.
- Q33/d3 specialization: all ten B-rows are good and their witnesses hit each S-row corresponding to an M-edge; at least five witnesses hit at least two S-rows.
- Outgoing edge: feeds the E408 Q33 witness-capacity subproblem.
- Status: PROVED as a constraint; no contradiction edge to bottom has been established.


## Added witness-capacity node

The theorem R12_WITNESS_CAPACITY_CROSSCUT.md is a necessary-structure node:
- each independent 4-set in H hits at least three shell rows;
- its hit hubs cover M[S] and include all missing hubs of its associated b;
- independent triples extend inside H_b for t_b<=3, with defect-sensitive failure condition t_b>=8-epsilon(X);
- E408 Q33 supplies at least five no-S K5 witnesses per exact-129 color and at least 7-beta hub-hit incidences across any selected five.

This node feeds E407's five-template/core completion problem and E408's exact-129 witness-packing problem. It does not currently feed a contradiction node.


## Added E407 row-profile reduction

For the five V12 templates, the row-count constraints imply the hub-missing degree floors recorded in R12_WITNESS_CAPACITY_CROSSCUT.md. In A/C, any Q_b missing a hub must hit at least six B rows, so it can witness at most four B labels and its four vertices carry parent target-degree excess at least2. This leaves two precise branches: hub-complete witnesses, or a high-B-degree witness family with nontrivial overlaps. No contradiction node has been established.


## Added boundary-classification node — minimum 7-transversals (2026-10-25)

Source: R12_TRANSVERSAL_BOUNDARY_CLASSIFICATION.md; arithmetic audit: verify_transversal_boundary_classification.py.

- Input: the exact-129 linear independent-four witness family at the support-boundary kernels; \(\alpha(H)\le4\), \(\delta(H)\ge12\), total excess four, and the seven-neighbour transversal floor.
- Shared lemma: distinct 7-transversals are disjoint by pair counting across selected color classes.
- E407 Q32 output: \(\delta_{\mathrm{pack}}\ge2\), where \(\delta_{\mathrm{pack}}\) is the number of complement edges in \(\overline{H[U]}\) not covered by the 49 selected witness K4s.
- E408 Q33 output: \(2\delta_{\mathrm{pack}}+\epsilon_U\ge8\), with \(\delta_{\mathrm{pack}}+\epsilon_U\le17\).
- These remove low-budget boundary profiles only. They do not construct a contradiction for the surviving profiles and do not cover E408 Q32's 285-edge core.

## Audit firewall — shell-incidence union bound

R12_SHELL_INCIDENCE_UNION_AUDIT.md corrects an imported inequality: vertices with zero shell support contribute negative terms to the global sum. Since at most four core vertices can have zero shell support, the safe full-row support-union floors are 7 for E407 template A and 6 for C. The earlier 11/10 floors must not be used unless a separate theorem proves zero-support absence.

The original proof DAG still has an OPEN T61 terminal and an OPEN original K145-to-T61 certification edge.
