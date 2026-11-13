# Complete transitive axiom audit

Verified code commit 875bd3de7478129b507b4f8e9df14f0c8e8bd4f5, Linux CI 43361985046.

All 122 project declarations compiled and audited. Allowed logical axioms: propext, Classical.choice, Quot.sound.
Source scan and kernel audit both passed. No sorry/admit/custom axiom/unsafe/implemented_by/native_decide is used.
No diagnostic enumeration is imported into Lean. All graph hypotheses appear in DECLARATION_STATEMENTS.md.
Unfinished results are absent proofs: complete type classification, Cost-6, sharp R335/R336, GATE47 and MainTheorem.

| Declaration | Transitive axioms |
|---|---|
| EG617.colorGraph | propext, Quot.sound |
| EG617.colorGraph_adj_iff | propext, Quot.sound |
| EG617.validColoring_iff_colorGraph | propext, Classical.choice, Quot.sound |
| EG617.colorGraph_partition | propext, Quot.sound |
| EG617.no_independent_thirteen | propext, Classical.choice, Quot.sound |
| EG617.no_monochromatic_thirteen | propext, Classical.choice, Quot.sound |
| EG617.Vertex | none |
| EG617.Color | none |
| EG617.Edge | propext, Quot.sound |
| EG617.EdgeColoring | propext, Quot.sound |
| EG617.edgeOf | propext, Quot.sound |
| EG617.Inside | propext, Classical.choice, Quot.sound |
| EG617.edgeOf_swap | propext, Quot.sound |
| EG617.edgeOf_eq_iff | propext, Quot.sound |
| EG617.edge_has_endpoints | propext, Quot.sound |
| EG617.edgeOf_surjective | propext, Quot.sound |
| EG617.edgeOf_inside_iff | propext, Classical.choice, Quot.sound |
| EG617.inside_mono | propext, Classical.choice, Quot.sound |
| EG617.mem_complete_iff | propext, Classical.choice, Quot.sound |
| EG617.edgeEquivComplete | propext, Classical.choice, Quot.sound |
| EG617.ValidColoring | propext, Classical.choice, Quot.sound |
| EG617.EG617R12Statement | propext, Classical.choice, Quot.sound |
| EG617.validColoring_iff_endpoints | propext, Classical.choice, Quot.sound |
| EG617.originalProblem_iff_missingColor | propext, Classical.choice, Quot.sound |
| EG617.tau12 | none |
| EG617.tau12_add_turanNumber | propext, Classical.choice, Quot.sound |
| EG617.CoreIndependenceBound | propext, Classical.choice, Quot.sound |
| EG617.CoreCliqueBound | propext, Classical.choice, Quot.sound |
| EG617.coreInducedEdgeCount | propext, Classical.choice, Quot.sound |
| EG617.CoreAdmissible | propext, Classical.choice, Quot.sound |
| EG617.core_induced_edge_count_univ | propext, Classical.choice, Quot.sound |
| EG617.core_independenceBound_induce | propext, Classical.choice, Quot.sound |
| EG617.core_cliqueBound_induce | propext, Classical.choice, Quot.sound |
| EG617.core_independence_nonNeighbors | propext, Classical.choice, Quot.sound |
| EG617.core_compl_edge_count | propext, Classical.choice, Quot.sound |
| EG617.core_induced_edge_count_image | propext, Classical.choice, Quot.sound |
| EG617.core_admissible_induce | propext, Classical.choice, Quot.sound |
| EG617.core_admissible_nonNeighbors | propext, Classical.choice, Quot.sound |
| EG617.Gate47Statement | propext, Classical.choice, Quot.sound |
| EG617.two_colorable_partition | propext, Classical.choice, Quot.sound |
| EG617.bipartition_edge_count | propext, Classical.choice, Quot.sound |
| EG617.adjCount_eq_card_product_filter | propext, Classical.choice, Quot.sound |
| EG617.adjCount_add_missing_eq_product | propext, Classical.choice, Quot.sound |
| EG617.complete_cross_of_no_missing | propext, Classical.choice, Quot.sound |
| EG617.unique_missing_cross_of_card_one | propext, Classical.choice, Quot.sound |
| EG617.bipartite_18_dense_classification | propext, Classical.choice, Quot.sound |
| EG617.adjCount | propext, Classical.choice, Quot.sound |
| EG617.adjCount_eq_sum_filter | propext, Classical.choice, Quot.sound |
| EG617.degree_induce_eq_filter | propext, Classical.choice, Quot.sound |
| EG617.adjCount_self | propext, Classical.choice, Quot.sound |
| EG617.adjCount_symm | propext, Classical.choice, Quot.sound |
| EG617.adjCount_union_left | propext, Classical.choice, Quot.sound |
| EG617.adjCount_union_right | propext, Classical.choice, Quot.sound |
| EG617.edge_partition | propext, Classical.choice, Quot.sound |
| EG617.adjCount_right_univ | propext, Classical.choice, Quot.sound |
| EG617.adjCount_le_sum_degrees | propext, Classical.choice, Quot.sound |
| EG617.adjCount_independent_zero | propext, Classical.choice, Quot.sound |
| EG617.twice_independent_card_le_of_degree_two | propext, Classical.choice, Quot.sound |
| EG617.oddCycleBound | propext |
| EG617.oddCycleBound_23_two | propext |
| EG617.oddCycleBound_23_ge_three | propext, Quot.sound |
| EG617.oddCycleBound_23_three | propext |
| EG617.oddCycleBound_18 | propext, Quot.sound |
| EG617.oddCycleBound_18_two | propext |
| EG617.cycle_support_card | propext, Classical.choice, Quot.sound |
| EG617.chordless_cycle_induced_degree_two | propext, Classical.choice, Quot.sound |
| EG617.chordless_cycle_induced_edges | propext, Classical.choice, Quot.sound |
| EG617.twice_subset_independent_card_le_of_induced_degree_two | propext, Classical.choice, Quot.sound |
| EG617.shortestOddLoop_neighbor_card_le | propext, Classical.choice, Quot.sound |
| EG617.triangleFree_induced_mantel | propext, Classical.choice, Quot.sound |
| EG617.shortestOddLoop_edge_bound | propext, Classical.choice, Quot.sound |
| EG617.shortestOddLoop_half_length_ge_two | propext, Classical.choice, Quot.sound |
| EG617.triangleFree_nonbipartite_edge_bound | propext, Classical.choice, Quot.sound |
| EG617.triangleFree_nonbipartite_18_edges_le_73 | propext, Classical.choice, Quot.sound |
| EG617.IsShortestOddCycle | propext |
| EG617.shortestOddCycle_iff_shortestOddLoop | propext, Classical.choice, Quot.sound |
| EG617.shortestOddCycle_edge_bound | propext, Classical.choice, Quot.sound |
| EG617.IsShortestOddLoop | propext |
| EG617.bypass_parity_of_short_loops_even | propext, Classical.choice, Quot.sound |
| EG617.shortestOddLoop_isCycle | propext, Classical.choice, Quot.sound |
| EG617.exists_shortestOddLoop | propext, Classical.choice, Quot.sound |
| EG617.exists_odd_cycle_of_not_two_colorable | propext, Classical.choice, Quot.sound |
| EG617.walk_end_edge_mem_of_length_one | propext, Classical.choice, Quot.sound |
| EG617.shortestOddLoop_isChordless | propext, Classical.choice, Quot.sound |
| EG617.cycleGraph_twice_independent_card_le | propext, Classical.choice, Quot.sound |
| EG617.cycle_copy_twice_neighbor_card_le | propext, Classical.choice, Quot.sound |
| EG617.core_not_two_colorable_of_card_24 | propext, Classical.choice, Quot.sound |
| EG617.core_triangleFree_edges_lt_132_of_card_24 | propext, Classical.choice, Quot.sound |
| EG617.core_R224_empty_of_card | propext, Classical.choice, Quot.sound |
| EG617.core_not_two_colorable_24 | propext, Classical.choice, Quot.sound |
| EG617.core_triangleFree24_edges_lt_132 | propext, Classical.choice, Quot.sound |
| EG617.core_R224_empty | propext, Classical.choice, Quot.sound |
| EG617.core_R3_card_le_degree_add_24 | propext, Classical.choice, Quot.sound |
| EG617.core_R335_degree_ge_11 | propext, Classical.choice, Quot.sound |
| EG617.core_R337_empty_of_card | propext, Classical.choice, Quot.sound |
| EG617.core_R337_empty | propext, Classical.choice, Quot.sound |
| EG617.core_R4_card_le_degree_add_37 | propext, Classical.choice, Quot.sound |
| EG617.core_R447_degree_ge_10 | propext, Classical.choice, Quot.sound |
| EG617.not_two_colorable_of_independence_bound | propext, Classical.choice, Quot.sound |
| EG617.r23_shortestOddLoop_length_five | propext, Classical.choice, Quot.sound |
| EG617.r23_exists_five_cycle_bipartite_exterior | propext, Classical.choice, Quot.sound |
| EG617.independent_card_le_twelve | propext, Classical.choice, Quot.sound |
| EG617.monochromatic_card_le_twelve | propext, Classical.choice, Quot.sound |
| EG617.colorGraph_clique_card_le_twelve | propext, Classical.choice, Quot.sound |
| EG617.inducedColorGraph | propext, Classical.choice, Quot.sound |
| EG617.colorEdgeCount | propext, Classical.choice, Quot.sound |
| EG617.colorEdgeCount_univ | propext, Classical.choice, Quot.sound |
| EG617.inducedColorGraph_adj_iff | propext, Classical.choice, Quot.sound |
| EG617.induced_edge_unique_color | propext, Classical.choice, Quot.sound |
| EG617.induced_color_edges_disjoint | propext, Classical.choice, Quot.sound |
| EG617.induced_color_edges_union | propext, Classical.choice, Quot.sound |
| EG617.sum_colorEdgeCount | propext, Classical.choice, Quot.sound |
| EG617.D | none |
| EG617.colorEdgeCount_add_eleven_tau_le | propext, Classical.choice, Quot.sound |
| EG617.hereditary_color_cap | propext, Classical.choice, Quot.sound |
| EG617.hereditary_cap_subtraction_exact | propext, Classical.choice, Quot.sound |
| EG617.exists_least_color | propext, Classical.choice, Quot.sound |
| EG617.least_color_edgeCount_le_870 | propext, Classical.choice, Quot.sound |
| EG617.exists_least_color_with_hereditary_cap | propext, Classical.choice, Quot.sound |
| EG617.exists_colorGraph_card_edgeFinset_le_870 | propext, Classical.choice, Quot.sound |
| EG617.inducedColorGraph_compl_cliqueFree | propext, Classical.choice, Quot.sound |
| EG617.tau12_le_colorEdgeCount | propext, Classical.choice, Quot.sound |
