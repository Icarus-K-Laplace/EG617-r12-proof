# Transitive axiom audit

Verified code efff7bdbf2381be3ade39d85561974d3f8739228, CI 44675114460. All project declarations below compiled.
Only propext, Classical.choice and Quot.sound are used. E286/COVER/MainTheorem remain unproved.

| Declaration | Axioms |
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
| EG617.c5_incompatible_endpoint_forces_singleton | propext, Classical.choice, Quot.sound |
| EG617.c5_missing_edge_type_sets | propext, Classical.choice, Quot.sound |
| EG617.c5_missing_endpoint_orientations | propext, Classical.choice, Quot.sound |
| EG617.c5_singleton_extension | propext, Classical.choice, Quot.sound |
| EG617.disjoint_cycle_neighbors_no_common_neighbor | propext, Classical.choice, Quot.sound |
| EG617.missing_exterior_type_presentation | propext, Classical.choice, Quot.sound |
| EG617.missing_exterior_type_orientations | propext, Classical.choice, Quot.sound |
| EG617.one_exception_type_fiber_card | propext, Classical.choice, Quot.sound |
| EG617.missing_exterior_type_fiber_formula | propext, Classical.choice, Quot.sound |
| EG617.c5_missing_fiber_profile | propext, Classical.choice, Quot.sound |
| EG617.singleton_cycle_edge_completion_witness | propext, Classical.choice, Quot.sound |
| EG617.cycle_type_fiber_card | propext, Classical.choice, Quot.sound |
| EG617.singleton_side_type_fiber_profile | propext, Classical.choice, Quot.sound |
| EG617.complete_exterior_type_fiber_profile | propext, Classical.choice, Quot.sound |
| EG617.cycleNeighborLabels_cycle_vertex | propext, Classical.choice, Quot.sound |
| EG617.complete_exterior_type_presentation | propext, Classical.choice, Quot.sound |
| EG617.exists_cycle_type_assignment | propext, Classical.choice, Quot.sound |
| EG617.complete_exterior_has_type_presentation | propext, Classical.choice, Quot.sound |
| EG617.c5Type | propext, Quot.sound |
| EG617.c5Type_card | propext, Quot.sound |
| EG617.c5Type_disjoint_iff | propext, Classical.choice, Quot.sound |
| EG617.c5_adj_iff_mem_type | propext, Classical.choice, Quot.sound |
| EG617.c5_independent_pair_unique_type | propext, Classical.choice, Quot.sound |
| EG617.c5_common_neighbors_unique | propext, Classical.choice, Quot.sound |
| EG617.c5_complete_type_sets | propext, Classical.choice, Quot.sound |
| EG617.cycleNeighborLabels | propext, Classical.choice, Quot.sound |
| EG617.cycleNeighborLabels_independent | propext, Classical.choice, Quot.sound |
| EG617.cycleNeighborLabels_unique_type | propext, Classical.choice, Quot.sound |
| EG617.adjacent_cycleNeighborLabels_disjoint | propext, Classical.choice, Quot.sound |
| EG617.complete_bipartite_type_image | propext, Classical.choice, Quot.sound |
| EG617.CostSixProperty | propext, Classical.choice, Quot.sound |
| EG617.c5Fiber | propext, Classical.choice, Quot.sound |
| EG617.mem_c5Fiber | propext, Classical.choice, Quot.sound |
| EG617.c5Fiber_disjoint | propext, Classical.choice, Quot.sound |
| EG617.c5Fiber_adjCount | propext, Classical.choice, Quot.sound |
| EG617.c5_three_fiber_witness_counts | propext, Classical.choice, Quot.sound |
| EG617.independent_c5_fiber_counts | propext, Classical.choice, Quot.sound |
| EG617.case_I_cost_arithmetic | propext, Quot.sound |
| EG617.exceptional_cost_arithmetic | propext, Quot.sound |
| EG617.coreInducedEdgeCount_mono_graph | propext, Classical.choice, Quot.sound |
| EG617.independent_sup_edge_or_endpoints | propext, Classical.choice, Quot.sound |
| EG617.independent_sup_edge_neighbor_card | propext, Classical.choice, Quot.sound |
| EG617.case_I_single_edge_deletion_cost_six | propext, Classical.choice, Quot.sound |
| EG617.r23_cost_six | propext, Classical.choice, Quot.sound |
| EG617.case_I_cost_six | propext, Classical.choice, Quot.sound |
| EG617.exceptional_cost_four | propext, Classical.choice, Quot.sound |
| EG617.exceptional_cost_six | propext, Classical.choice, Quot.sound |
| EG617.seed_private_nonadj_other_seed | propext, Classical.choice, Quot.sound |
| EG617.seed_private_mem_seed | propext, Classical.choice, Quot.sound |
| EG617.e286_pair_blocker_complete | propext, Classical.choice, Quot.sound |
| EG617.e286_subset_excess_budget | propext, Classical.choice, Quot.sound |
| EG617.e286_induced_degree_budget | propext, Classical.choice, Quot.sound |
| EG617.oddCycleBound_25 | propext, Quot.sound |
| EG617.alpha_two_25_edges_ge_155 | propext, Classical.choice, Quot.sound |
| EG617.e286_no_induced_alpha_two_25 | propext, Classical.choice, Quot.sound |
| EG617.independenceBound_common_nonNeighbors | propext, Classical.choice, Quot.sound |
| EG617.e286_common_antineighborhood_card_le_24 | propext, Classical.choice, Quot.sound |
| EG617.e286_two_disjoint_neighbor_sets | propext, Classical.choice, Quot.sound |
| EG617.e286_clique_blocker_vertex_charge | propext, Classical.choice, Quot.sound |
| EG617.e286_pair_point_degree_charge | propext, Classical.choice, Quot.sound |
| EG617.e286_f11_minimum | propext, Classical.choice, Quot.sound |
| EG617.e286_k11_pair_local_charge | propext, Classical.choice, Quot.sound |
| EG617.e286_common_neighbors_excess_bound | propext, Classical.choice, Quot.sound |
| EG617.e286_pair_excess_le_eight | propext, Classical.choice, Quot.sound |
| EG617.e286_common_neighbors_le_eleven | propext, Classical.choice, Quot.sound |
| EG617.e286_common_set_excess_charge | propext, Classical.choice, Quot.sound |
| EG617.e286_ten_clique_completers_excess | propext, Classical.choice, Quot.sound |
| EG617.e286_eleven_clique_missing_nonempty | propext, Classical.choice, Quot.sound |
| EG617.e286_pair_support_mem_multiple | propext, Classical.choice, Quot.sound |
| EG617.e286_private_k11_pair_charge | propext, Classical.choice, Quot.sound |
| EG617.e286_complementary_k11_pairs_impossible | propext, Classical.choice, Quot.sound |
| EG617.E286Hypotheses | propext, Classical.choice, Quot.sound |
| EG617.E286Statement | propext, Classical.choice, Quot.sound |
| EG617.degreeExcess12 | propext, Classical.choice, Quot.sound |
| EG617.excessSupport | propext, Classical.choice, Quot.sound |
| EG617.e286_degree_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_excess_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_support_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_support_card_le_eight | propext, Classical.choice, Quot.sound |
| EG617.e286_degree_le_twenty | propext, Classical.choice, Quot.sound |
| EG617.e286_regular_complement | propext, Classical.choice, Quot.sound |
| EG617.e286_regular_card_ge_39 | propext, Classical.choice, Quot.sound |
| EG617.e286_support_degree_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_regular_edge_ledger | propext, Classical.choice, Quot.sound |
| EG617.e286_support_type_injective | propext, Classical.choice, Quot.sound |
| EG617.seedLabelNeighbors_relabel | propext, Classical.choice, Quot.sound |
| EG617.e286_graph_support_counts_relabel | propext, Classical.choice, Quot.sound |
| EG617.e286_actual_oriented_support_orbit | propext, Classical.choice, Quot.sound |
| EG617.e286_first_support_orbit_impossible | propext, Classical.choice, Quot.sound |
| EG617.e286_actual_support_nine_remaining | propext, Classical.choice, Quot.sound |
| EG617.seedNeighbors | propext, Classical.choice, Quot.sound |
| EG617.seedPrivateClique | propext, Classical.choice, Quot.sound |
| EG617.seedMultipleSet | propext, Classical.choice, Quot.sound |
| EG617.seedNeighbors_empty_of_seed | propext, Classical.choice, Quot.sound |
| EG617.seedNeighbors_singleton_outside | propext, Classical.choice, Quot.sound |
| EG617.seedNeighbors_singleton_nonadj | propext, Classical.choice, Quot.sound |
| EG617.e286_private_class_isClique | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_dominates | propext, Classical.choice, Quot.sound |
| EG617.e286_private_multiple_card | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_incidence_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_surplus_five | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_support_counts | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_classes_cover | propext, Classical.choice, Quot.sound |
| EG617.seed_private_classes_disjoint | propext, Classical.choice, Quot.sound |
| EG617.seed_private_multiple_disjoint | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_support_reduction | propext, Classical.choice, Quot.sound |
| EG617.e286_exists_regular_independent_four | propext, Classical.choice, Quot.sound |
| EG617.e286SupportType | propext, Quot.sound |
| EG617.e286SupportWeights | none |
| EG617.e286_support_type_complete | propext, Classical.choice, Quot.sound |
| EG617.e286_support_type_weight | propext, Quot.sound |
| EG617.e286WeightedSum | propext |
| EG617.e286WeightedProfiles | none |
| EG617.e286_weighted_profiles_complete | propext, Classical.choice, Quot.sound |
| EG617.e286CountIncidence | propext, Classical.choice, Quot.sound |
| EG617.e286RelabelCounts | propext, Classical.choice, Quot.sound |
| EG617.e286SupportOrbitRepresentatives | none |
| EG617.e286_finite_support_orbit_check | propext, Classical.choice, Quot.sound |
| EG617.e286_support_counts_complete | propext, Classical.choice, Quot.sound |
| EG617.seedLabelNeighbors | propext, Classical.choice, Quot.sound |
| EG617.seedLabelNeighbors_image | propext, Classical.choice, Quot.sound |
| EG617.seedLabelNeighbors_card | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_support_code_exists | propext, Classical.choice, Quot.sound |
| EG617.e286SeedSupportCode | propext, Classical.choice, Quot.sound |
| EG617.e286_seed_support_code_spec | propext, Classical.choice, Quot.sound |
| EG617.e286GraphSupportCounts | propext, Classical.choice, Quot.sound |
| EG617.e286_ofFn_get | propext, Classical.choice, Quot.sound |
| EG617.e286_weightedSum_ofFn | propext, Classical.choice, Quot.sound |
| EG617.e286_weighted_fiber_count | propext, Classical.choice, Quot.sound |
| EG617.e286_graph_support_weighted_sum | propext, Classical.choice, Quot.sound |
| EG617.e286_graph_support_incidence | propext, Classical.choice, Quot.sound |
| EG617.e286_actual_support_orbit | propext, Classical.choice, Quot.sound |
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
| EG617.core_R447_min_degree_eleven_edges_ge_287 | propext, Classical.choice, Quot.sound |
| EG617.gate47_verified | propext, Classical.choice, Quot.sound |
| EG617.core_admissible_common_nonNeighbors | propext, Classical.choice, Quot.sound |
| EG617.core_R4_common_nonneighbors_card_le_23 | propext, Classical.choice, Quot.sound |
| EG617.core_R4_row_union_ge_twelve | propext, Classical.choice, Quot.sound |
| EG617.core_two_degrees_le_edges_add_one | propext, Classical.choice, Quot.sound |
| EG617.core_shell_row_missing_degree_le | propext, Classical.choice, Quot.sound |
| EG617.core_missing_edge_row_sum | propext, Classical.choice, Quot.sound |
| EG617.core_shell_edge_degree_ledger | propext, Classical.choice, Quot.sound |
| EG617.core_induced_edges_le_choose | propext, Classical.choice, Quot.sound |
| EG617.core_R447_min_degree_ten_edges_ge_289 | propext, Classical.choice, Quot.sound |
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
| EG617.two_cycle_neighbors_cross_card_le_nine | propext, Classical.choice, Quot.sound |
| EG617.r23_exists_balanced_exterior | propext, Classical.choice, Quot.sound |
| EG617.c5_remaining_fiber_sum | propext, Classical.choice, Quot.sound |
| EG617.R23CaseIProfile | propext, Classical.choice, Quot.sound |
| EG617.r23_122_case_I | propext, Classical.choice, Quot.sound |
| EG617.R23OneEdgeCompletion | propext, Classical.choice, Quot.sound |
| EG617.singleton_partition_completes_to_case_I | propext, Classical.choice, Quot.sound |
| EG617.R23MissingEdgeExterior | propext, Classical.choice, Quot.sound |
| EG617.r23_121_completion_or_missing_exterior | propext, Classical.choice, Quot.sound |
| EG617.R23ExceptionalProfile | propext, Classical.choice, Quot.sound |
| EG617.missing_exterior_completion_or_exceptional | propext, Classical.choice, Quot.sound |
| EG617.r23_complete_classification | propext, Classical.choice, Quot.sound |
| EG617.r23_122_complete_type_data | propext, Classical.choice, Quot.sound |
| EG617.r23_122_type_presentation | propext, Classical.choice, Quot.sound |
| EG617.triangleFree_sup_edge_of_no_common_neighbor | propext, Classical.choice, Quot.sound |
| EG617.r23_one_edge_completion_case_I | propext, Classical.choice, Quot.sound |
| EG617.deficit_sum_add | propext, Classical.choice, Quot.sound |
| EG617.deficit_zero_iff | propext, Classical.choice, Quot.sound |
| EG617.deficit_one_distribution | propext, Classical.choice, Quot.sound |
| EG617.ExactC5NeighborLedger | propext, Classical.choice, Quot.sound |
| EG617.r23_exact_neighbor_ledger | propext, Classical.choice, Quot.sound |
| EG617.not_two_colorable_of_independence_bound | propext, Classical.choice, Quot.sound |
| EG617.r23_shortestOddLoop_length_five | propext, Classical.choice, Quot.sound |
| EG617.r23_exists_five_cycle_bipartite_exterior | propext, Classical.choice, Quot.sound |
| EG617.five_cycle_copy_same_support | propext, Classical.choice, Quot.sound |
| EG617.cycleNeighborLabels_card_eq | propext, Classical.choice, Quot.sound |
| EG617.r23_exact_labeled_neighbor_ledger | propext, Classical.choice, Quot.sound |
| EG617.core_degree_eleven_neighbor_nonedge | propext, Classical.choice, Quot.sound |
| EG617.core_common_nonneighbors_clique | propext, Classical.choice, Quot.sound |
| EG617.core_edge_count_union | propext, Classical.choice, Quot.sound |
| EG617.core_pair_cross_lower_bound | propext, Classical.choice, Quot.sound |
| EG617.core_induce_compl | propext, Classical.choice, Quot.sound |
| EG617.core_induced_compl_edge_count | propext, Classical.choice, Quot.sound |
| EG617.core_fourteen_cost_obstruction | propext, Classical.choice, Quot.sound |
| EG617.core_R223_complement_cost_six | propext, Classical.choice, Quot.sound |
| EG617.core_R335_degree_eleven_nonneighbor_cost_six | propext, Classical.choice, Quot.sound |
| EG617.core_R335_degree_ne_eleven | propext, Classical.choice, Quot.sound |
| EG617.core_R335_degree_ge_twelve | propext, Classical.choice, Quot.sound |
| EG617.core_R335_edges_ge_210 | propext, Classical.choice, Quot.sound |
| EG617.core_R336_degree_ge_thirteen | propext, Classical.choice, Quot.sound |
| EG617.core_R336_edges_ge_234 | propext, Classical.choice, Quot.sound |
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
| EG617.inducedColorGraph_compl_cliqueFree | propext, Classical.choice, …9478 tokens truncated…(G : SimpleGraph V) : Finset V
```

## EG617.e286_degree_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, G.degree v = 572
```

## EG617.e286_excess_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_excess_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v : V, degreeExcess12 G v = 8
```

## EG617.e286_support_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, degreeExcess12 G v = 8
```

## EG617.e286_support_card_le_eight

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_card_le_eight (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G).card ≤ 8
```

## EG617.e286_degree_le_twenty

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_degree_le_twenty (G : SimpleGraph V) (hG : E286Hypotheses G) (v : V) :
    G.degree v ≤ 20
```

## EG617.e286_regular_complement

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_complement (G : SimpleGraph V) (hG : E286Hypotheses G) :
    (excessSupport G)ᶜ = Finset.univ.filter (fun v => G.degree v = 12)
```

## EG617.e286_regular_card_ge_39

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_card_ge_39 (G : SimpleGraph V) (hG : E286Hypotheses G) :
    39 ≤ (Finset.univ.filter (fun v => G.degree v = 12)).card
```

## EG617.e286_support_degree_sum

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_support_degree_sum (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∑ v ∈ excessSupport G, G.degree v = 12 * (excessSupport G).card + 8
```

## EG617.e286_regular_edge_ledger

Source: EG617/Core/E286Excess.lean

```lean
theorem e286_regular_edge_ledger (G : SimpleGraph V) (hG : E286Hypotheses G) :
    coreInducedEdgeCount G (excessSupport G)ᶜ + 12 * (excessSupport G).card + 8 =
      286 + coreInducedEdgeCount G (excessSupport G)
```

## EG617.e286_support_type_injective

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_support_type_injective : Function.Injective e286SupportType
```

## EG617.seedLabelNeighbors_relabel

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem seedLabelNeighbors_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) (v : V) :
    seedLabelNeighbors G I (σ.symm.trans e) v =
      (seedLabelNeighbors G I e v).image σ
```

## EG617.e286_graph_support_counts_relabel

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_graph_support_counts_relabel (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (σ : Equiv.Perm (Fin 4)) :
    e286GraphSupportCounts G I (σ.symm.trans e) =
      e286RelabelCounts σ (e286GraphSupportCounts G I e)
```

## EG617.e286_actual_oriented_support_orbit

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_actual_oriented_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives
```

## EG617.e286_first_support_orbit_impossible

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_first_support_orbit_impossible (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V))
    (hcounts : e286GraphSupportCounts G I e = [1,0,0,0,0,1,0,0,0,0,1]) : False
```

## EG617.e286_actual_support_nine_remaining

Source: EG617/Core/E286OrbitRealization.lean

```lean
theorem e286_actual_support_nine_remaining (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧ ∃ e : Fin 4 ≃ (I : Set V),
        e286GraphSupportCounts G I e ∈ e286SupportOrbitRepresentatives.tail
```

## EG617.seedNeighbors

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedNeighbors (G : SimpleGraph V) (I : Finset V) (v : V) : Finset V
```

## EG617.seedPrivateClique

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedPrivateClique (G : SimpleGraph V) (I : Finset V) (s : V) : Finset V
```

## EG617.seedMultipleSet

Source: EG617/Core/E286PrivateClasses.lean

```lean
noncomputable def seedMultipleSet (G : SimpleGraph V) (I : Finset V) : Finset V
```

## EG617.seedNeighbors_empty_of_seed

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_empty_of_seed (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    seedNeighbors G I s = ∅
```

## EG617.seedNeighbors_singleton_outside

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_singleton_outside (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s v : V)
    (hv : seedNeighbors G I v = {s}) : v ∉ I
```

## EG617.seedNeighbors_singleton_nonadj

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem seedNeighbors_singleton_nonadj (G : SimpleGraph V) (I : Finset V)
    (s v : V) (hv : seedNeighbors G I v = {s}) (t : V) (ht : t ∈ I)
    (hts : t ≠ s) : ¬ G.Adj v t
```

## EG617.e286_private_class_isClique

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_private_class_isClique (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (s : V) (hs : s ∈ I) :
    G.IsClique (seedPrivateClique G I s : Set V)
```

## EG617.e286_seed_dominates

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_seed_dominates (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (v : V) (hv : v ∉ I) : (seedNeighbors G I v).Nonempty
```

## EG617.e286_private_multiple_card

Source: EG617/Core/E286PrivateClasses.lean

```lean
theorem e286_private_multiple_card (G : SimpleGraph V)
    (I : Finset V) (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I)
    (hdeg : G.degree s = 12) :
    (seedPrivateClique G I s).card +
      ((seedMultipleSet G I).filter (G.Adj s)).card = 13
```

## EG617.e286_seed_incidence_sum

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_incidence_sum (G : SimpleGraph V) (I : Finset V)
    (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ Iᶜ, (seedNeighbors G I v).card = 48
```

## EG617.e286_seed_surplus_five

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_surplus_five (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    ∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1) = 5
```

## EG617.e286_seed_support_counts

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_support_counts (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V))
    (hdeg : ∀ s ∈ I, G.degree s = 12) :
    3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
    (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47
```

## EG617.e286_seed_classes_cover

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_classes_cover (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hcard : I.card = 4) (hI : G.IsIndepSet (I : Set V)) (v : V) :
    v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s
```

## EG617.seed_private_classes_disjoint

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem seed_private_classes_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s t : V) (hs : s ∈ I) (ht : t ∈ I)
    (hst : s ≠ t) : Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t)
```

## EG617.seed_private_multiple_disjoint

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem seed_private_multiple_disjoint (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) (s : V) (hs : s ∈ I) :
    Disjoint (seedPrivateClique G I s) (seedMultipleSet G I)
```

## EG617.e286_seed_support_reduction

Source: EG617/Core/E286SeedLedger.lean

```lean
theorem e286_seed_support_reduction (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ s ∈ I, G.degree s = 12) ∧
      3 ≤ (seedMultipleSet G I).card ∧ (seedMultipleSet G I).card ≤ 5 ∧
      (∑ v ∈ seedMultipleSet G I, ((seedNeighbors G I v).card - 1)) = 5 ∧
      (∑ s ∈ I, (seedPrivateClique G I s).card) + (seedMultipleSet G I).card = 47 ∧
      (∀ s ∈ I, G.IsClique (seedPrivateClique G I s : Set V) ∧
        (seedPrivateClique G I s).card ≤ 11 ∧
        (seedPrivateClique G I s).card + ((seedMultipleSet G I).filter (G.Adj s)).card = 13) ∧
      (∀ v, v ∈ seedMultipleSet G I ∨ ∃ s ∈ I, v ∈ seedPrivateClique G I s) ∧
      (∀ s ∈ I, ∀ t ∈ I, s ≠ t →
        Disjoint (seedPrivateClique G I s) (seedPrivateClique G I t)) ∧
      (∀ s ∈ I, Disjoint (seedPrivateClique G I s) (seedMultipleSet G I)) ∧
      ∀ v ∈ seedMultipleSet G I, 2 ≤ (seedNeighbors G I v).card ∧
        (seedNeighbors G I v).card ≤ 4
```

## EG617.e286_exists_regular_independent_four

Source: EG617/Core/E286Seeds.lean

```lean
theorem e286_exists_regular_independent_four (G : SimpleGraph V)
    (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      ∀ v ∈ I, G.degree v = 12
```

## EG617.e286SupportType

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportType (i : Fin 11) : Finset (Fin 4)
```

## EG617.e286SupportWeights

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportWeights : List ℕ
```

## EG617.e286_support_type_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_type_complete (S : Finset (Fin 4)) (hS : 2 ≤ S.card) :
    ∃! i : Fin 11, e286SupportType i = S
```

## EG617.e286_support_type_weight

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_type_weight (i : Fin 11) :
    (e286SupportType i).card - 1 = e286SupportWeights[i.val]!
```

## EG617.e286WeightedSum

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286WeightedSum : List ℕ → List ℕ → ℕ
  | w :: ws, x :: xs => w * x + e286WeightedSum ws xs
  | _, _ => 0

/-- All nonnegative count vectors with prescribed weighted surplus.
The bound on each first coordinate is proved in the completeness theorem. -/
def e286WeightedProfiles : List ℕ → ℕ → List (List ℕ)
  | [], b => if b = 0 then [[]] else []
  | w :: ws, b => (List.range (b + 1)).flatMap fun x =>
      if w * x ≤ b then (e286WeightedProfiles ws (b - w * x)).map (x :: ·) else []

theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286WeightedProfiles

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286WeightedProfiles : List ℕ → ℕ → List (List ℕ)
  | [], b => if b = 0 then [[]] else []
  | w :: ws, b => (List.range (b + 1)).flatMap fun x =>
      if w * x ≤ b then (e286WeightedProfiles ws (b - w * x)).map (x :: ·) else []

theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286_weighted_profiles_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_weighted_profiles_complete (ws xs : List ℕ) (b : ℕ)
    (hpos : ∀ w ∈ ws, 1 ≤ w) (hlen : xs.length = ws.length)
    (hsum : e286WeightedSum ws xs = b) :
    xs ∈ e286WeightedProfiles ws b
```

## EG617.e286CountIncidence

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286CountIncidence (xs : List ℕ) (s : Fin 4) : ℕ
```

## EG617.e286RelabelCounts

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286RelabelCounts (σ : Equiv.Perm (Fin 4)) (xs : List ℕ) : List ℕ
```

## EG617.e286SupportOrbitRepresentatives

Source: EG617/Core/E286SupportCounts.lean

```lean
def e286SupportOrbitRepresentatives : List (List ℕ)
```

## EG617.e286_finite_support_orbit_check

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_finite_support_orbit_check :
    ∀ xs ∈ e286WeightedProfiles e286SupportWeights 5,
      (∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) →
      ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives
```

## EG617.e286_support_counts_complete

Source: EG617/Core/E286SupportCounts.lean

```lean
theorem e286_support_counts_complete (xs : List ℕ)
    (hlen : xs.length = 11) (hsum : e286WeightedSum e286SupportWeights xs = 5)
    (hinc : ∀ s : Fin 4, 2 ≤ e286CountIncidence xs s) :
    ∃ σ : Equiv.Perm (Fin 4),
      e286RelabelCounts σ xs ∈ e286SupportOrbitRepresentatives
```

## EG617.seedLabelNeighbors

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def seedLabelNeighbors (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) : Finset (Fin 4)
```

## EG617.seedLabelNeighbors_image

Source: EG617/Core/E286SupportLift.lean

```lean
theorem seedLabelNeighbors_image (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).image (fun i => (e i : V)) = seedNeighbors G I v
```

## EG617.seedLabelNeighbors_card

Source: EG617/Core/E286SupportLift.lean

```lean
theorem seedLabelNeighbors_card (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : V) :
    (seedLabelNeighbors G I e v).card = (seedNeighbors G I v).card
```

## EG617.e286_seed_support_code_exists

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_seed_support_code_exists (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    ∃ i : Fin 11, e286SupportType i = seedLabelNeighbors G I e v
```

## EG617.e286SeedSupportCode

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def e286SeedSupportCode (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) : Fin 11
```

## EG617.e286_seed_support_code_spec

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_seed_support_code_spec (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (v : (seedMultipleSet G I : Set V)) :
    e286SupportType (e286SeedSupportCode G I e v) = seedLabelNeighbors G I e v
```

## EG617.e286GraphSupportCounts

Source: EG617/Core/E286SupportLift.lean

```lean
noncomputable def e286GraphSupportCounts (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) : List ℕ
```

## EG617.e286_ofFn_get

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_ofFn_get (f : Fin 11 → ℕ) (i : Fin 11) :
    (List.ofFn f)[i.val]! = f i
```

## EG617.e286_weightedSum_ofFn

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_weightedSum_ofFn (f : Fin 11 → ℕ) :
    e286WeightedSum e286SupportWeights (List.ofFn f) =
      ∑ i : Fin 11, ((e286SupportType i).card - 1) * f i
```

## EG617.e286_weighted_fiber_count

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_weighted_fiber_count {W : Type u} [Fintype W]
    (code : W → Fin 11) (w : Fin 11 → ℕ) :
    (∑ i : Fin 11, w i * (Finset.univ.filter (fun v => code v = i)).card) =
      ∑ v : W, w (code v)
```

## EG617.e286_graph_support_weighted_sum

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_graph_support_weighted_sum (G : SimpleGraph V) (hG : E286Hypotheses G)
    (I : Finset V) (hc : I.card = 4) (hi : G.IsIndepSet (I : Set V))
    (hd : ∀ v ∈ I, G.degree v = 12) (e : Fin 4 ≃ (I : Set V)) :
    e286WeightedSum e286SupportWeights (e286GraphSupportCounts G I e) = 5
```

## EG617.e286_graph_support_incidence

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_graph_support_incidence (G : SimpleGraph V) (I : Finset V)
    (e : Fin 4 ≃ (I : Set V)) (s : Fin 4) :
    e286CountIncidence (e286GraphSupportCounts G I e) s =
      ((seedMultipleSet G I).filter (G.Adj (e s))).card
```

## EG617.e286_actual_support_orbit

Source: EG617/Core/E286SupportLift.lean

```lean
theorem e286_actual_support_orbit (G : SimpleGraph V) (hG : E286Hypotheses G) :
    ∃ I : Finset V, I.card = 4 ∧ G.IsIndepSet (I : Set V) ∧
      (∀ v ∈ I, G.degree v = 12) ∧
      ∃ e : Fin 4 ≃ (I : Set V), ∃ σ : Equiv.Perm (Fin 4),
        e286RelabelCounts σ (e286GraphSupportCounts G I e) ∈
          e286SupportOrbitRepresentatives
```

## EG617.adjCount

Source: EG617/Core/EdgePartition.lean

```lean
noncomputable def adjCount (G : SimpleGraph V) (S T : Finset V) : ℕ
```

## EG617.adjCount_eq_sum_filter

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_eq_sum_filter (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = ∑ x ∈ S, (T.filter (G.Adj x)).card
```

## EG617.degree_induce_eq_filter

Source: EG617/Core/EdgePartition.lean

```lean
theorem degree_induce_eq_filter (G : SimpleGraph V) (S : Finset V) (x : S) :
    (G.induce (S : Set V)).degree x = (S.filter (G.Adj x)).card
```

## EG617.adjCount_self

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_self (G : SimpleGraph V) (S : Finset V) :
    adjCount G S S = 2 * coreInducedEdgeCount G S
```

## EG617.adjCount_symm

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_symm (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T = adjCount G T S
```

## EG617.adjCount_union_left

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_union_left (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint S T) : adjCount G (S ∪ T) U = adjCount G S U + adjCount G T U
```

## EG617.adjCount_union_right

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_union_right (G : SimpleGraph V) (S T U : Finset V)
    (hd : Disjoint T U) : adjCount G S (T ∪ U) = adjCount G S T + adjCount G S U
```

## EG617.edge_partition

Source: EG617/Core/EdgePartition.lean

```lean
theorem edge_partition (G : SimpleGraph V) (S : Finset V) :
    G.edgeFinset.card = coreInducedEdgeCount G S + adjCount G S Sᶜ +
      coreInducedEdgeCount G Sᶜ
```

## EG617.adjCount_right_univ

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_right_univ (G : SimpleGraph V) (S : Finset V) :
    adjCount G S Finset.univ = ∑ x ∈ S, G.degree x
```

## EG617.adjCount_le_sum_degrees

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_le_sum_degrees (G : SimpleGraph V) (S T : Finset V) :
    adjCount G S T ≤ ∑ x ∈ S, G.degree x
```

## EG617.adjCount_independent_zero

Source: EG617/Core/EdgePartition.lean

```lean
theorem adjCount_independent_zero (G : SimpleGraph V) (I : Finset V)
    (hI : G.IsIndepSet (I : Set V)) : adjCount G I I = 0
```

## EG617.twice_independent_card_le_of_degree_two

Source: EG617/Core/EdgePartition.lean

```lean
theorem twice_independent_card_le_of_degree_two (G : SimpleGraph V)
    (hd : ∀ v, G.degree v = 2) (I : Finset V) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ Fintype.card V
```

## EG617.core_R447_min_degree_eleven_edges_ge_287

Source: EG617/Core/Gate47.lean

```lean
theorem core_R447_min_degree_eleven_edges_ge_287 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w) :
    287 ≤ G.edgeFinset.card
```

## EG617.gate47_verified

Source: EG617/Core/Gate47.lean

```lean
theorem gate47_verified : Gate47Statement
```

## EG617.core_admissible_common_nonNeighbors

Source: EG617/Core/GateRows.lean

```lean
theorem core_admissible_common_nonNeighbors (G : SimpleGraph V) (a : ℕ)
    (hG : CoreAdmissible (a + 2) G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    CoreAdmissible a (G.induce (S : Set V))
```

## EG617.core_R4_common_nonneighbors_card_le_23

Source: EG617/Core/GateRows.lean

```lean
theorem core_R4_common_nonneighbors_card_le_23 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (x y : V) (hxy : x ≠ y) (hnxy : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    S.card ≤ 23
```

## EG617.core_R4_row_union_ge_twelve

Source: EG617/Core/GateRows.lean

```lean
theorem core_R4_row_union_ge_twelve (G : SimpleGraph V) (hG : CoreAdmissible 4 G)
    (C : Finset V) (hC : C.card = 35) (x y : V) (hxy : x ≠ y)
    (hnxy : ¬ G.Adj x y) (hx : x ∉ C) (hy : y ∉ C) :
    12 ≤ ((C.filter (G.Adj x)) ∪ (C.filter (G.Adj y))).card
```

## EG617.core_two_degrees_le_edges_add_one

Source: EG617/Core/GateRows.lean

```lean
theorem core_two_degrees_le_edges_add_one (G : SimpleGraph V) (x y : V) (hxy : x ≠ y) :
    G.degree x + G.degree y ≤ G.edgeFinset.card + 1
```

## EG617.core_shell_row_missing_degree_le

Source: EG617/Core/GateRows.lean

```lean
theorem core_shell_row_missing_degree_le (G : SimpleGraph V) (v : V)
    (hd : G.degree v = 11) (hmin : ∀ w, 11 ≤ G.degree w)
    (a : (G.neighborFinset v : Set V)) :
    ((G.induce (G.neighborFinset v : Set V))ᶜ).degree a ≤
      ((Gᶜ.neighborFinset v).filter (G.Adj a)).card
```

## EG617.core_missing_edge_row_sum

Source: EG617/Core/GateRows.lean

```lean
theorem core_missing_edge_row_sum (M : SimpleGraph V) (r : V → ℕ)
    (hrow : ∀ a, M.degree a ≤ r a) (a b : V) (hab : a ≠ b)
    (hpair : 12 ≤ r a + r b) :
    M.edgeFinset.card + 11 ≤ ∑ x : V, r x
```

## EG617.core_shell_edge_degree_ledger

Source: EG617/Core/GateShell.lean

```lean
theorem core_shell_edge_degree_ledger (G : SimpleGraph V) (v : V) :
    let S
```

## EG617.core_induced_edges_le_choose

Source: EG617/Core/GateShell.lean

```lean
theorem core_induced_edges_le_choose (G : SimpleGraph V) (S : Finset V) :
    coreInducedEdgeCount G S ≤ S.card.choose 2
```

## EG617.core_R447_min_degree_ten_edges_ge_289

Source: EG617/Core/GateShell.lean

```lean
theorem core_R447_min_degree_ten_edges_ge_289 (G : SimpleGraph V)
    (hV : Fintype.card V = 47) (hG : CoreAdmissible 4 G) (v : V)
    (hd : G.degree v = 10) (hmin : ∀ w, 10 ≤ G.degree w) :
    289 ≤ G.edgeFinset.card
```

## EG617.oddCycleBound

Source: EG617/Core/OddCycleArithmetic.lean

```lean
def oddCycleBound (n k : ℕ) : ℕ
```

## EG617.oddCycleBound_23_two

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_two : oddCycleBound 23 2 = 122
```

## EG617.oddCycleBound_23_ge_three

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_ge_three (k : ℕ) (hk : 3 ≤ k)
    (hfit : 2 * k + 1 ≤ 23) : oddCycleBound 23 k ≤ 119
```

## EG617.oddCycleBound_23_three

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_23_three : oddCycleBound 23 3 = 119
```

## EG617.oddCycleBound_18

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_18 (k : ℕ) (hk : 2 ≤ k)
    (hfit : 2 * k + 1 ≤ 18) : oddCycleBound 18 k ≤ 73
```

## EG617.oddCycleBound_18_two

Source: EG617/Core/OddCycleArithmetic.lean

```lean
theorem oddCycleBound_18_two : oddCycleBound 18 2 = 73
```

## EG617.cycle_support_card

Source: EG617/Core/OddCycleBound.lean

```lean
theorem cycle_support_card {v : V} (p : G.Walk v v) (hp : p.IsCycle) :
    p.support.toFinset.card = p.length
```

## EG617.chordless_cycle_induced_degree_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem chordless_cycle_induced_degree_two {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) (x : p.support.toFinset) :
    (G.induce (p.support.toFinset : Set V)).degree x = 2
```

## EG617.chordless_cycle_induced_edges

Source: EG617/Core/OddCycleBound.lean

```lean
theorem chordless_cycle_induced_edges {v : V} (p : G.Walk v v)
    (hp : p.IsCycle) (hc : p.IsChordless) :
    coreInducedEdgeCount G p.support.toFinset = p.length
```

## EG617.twice_subset_independent_card_le_of_induced_degree_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem twice_subset_independent_card_le_of_induced_degree_two
    (G : SimpleGraph V) (S : Finset V)
    (hd : ∀ v : S, (G.induce (S : Set V)).degree v = 2)
    (I : Finset V) (hIS : I ⊆ S) (hI : G.IsIndepSet (I : Set V)) :
    2 * I.card ≤ S.card
```

## EG617.shortestOddLoop_neighbor_card_le

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_neighbor_card_le {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) (ht : G.CliqueFree 3) (k : ℕ)
    (hlen : p.length = 2 * k + 1) (x : V) :
    (p.support.toFinset.filter (G.Adj x)).card ≤ k
```

## EG617.triangleFree_induced_mantel

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_induced_mantel (G : SimpleGraph V) (ht : G.CliqueFree 3)
    (S : Finset V) : coreInducedEdgeCount G S ≤ S.card ^ 2 / 4
```

## EG617.shortestOddLoop_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_edge_bound (G : SimpleGraph V) (ht : G.CliqueFree 3)
    {v : V} (p : G.Walk v v) (hp : IsShortestOddLoop p) (k : ℕ)
    (hlen : p.length = 2 * k + 1) :
    G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.shortestOddLoop_half_length_ge_two

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddLoop_half_length_ge_two (G : SimpleGraph V)
    (ht : G.CliqueFree 3) {v : V} (p : G.Walk v v) (hp : IsShortestOddLoop p)
    (k : ℕ) (hlen : p.length = 2 * k + 1) : 2 ≤ k
```

## EG617.triangleFree_nonbipartite_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_nonbipartite_edge_bound (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (hb : ¬ G.Colorable 2) :
    ∃ k : ℕ, 2 ≤ k ∧ 2 * k + 1 ≤ Fintype.card V ∧
      G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.triangleFree_nonbipartite_18_edges_le_73

Source: EG617/Core/OddCycleBound.lean

```lean
theorem triangleFree_nonbipartite_18_edges_le_73 (G : SimpleGraph V)
    (hV : Fintype.card V = 18) (ht : G.CliqueFree 3) (hb : ¬ G.Colorable 2) :
    G.edgeFinset.card ≤ 73
```

## EG617.IsShortestOddCycle

Source: EG617/Core/OddCycleBound.lean

```lean
def IsShortestOddCycle {v : V} (p : G.Walk v v) : Prop
```

## EG617.shortestOddCycle_iff_shortestOddLoop

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddCycle_iff_shortestOddLoop {v : V} (p : G.Walk v v) :
    IsShortestOddCycle p ↔ IsShortestOddLoop p
```

## EG617.shortestOddCycle_edge_bound

Source: EG617/Core/OddCycleBound.lean

```lean
theorem shortestOddCycle_edge_bound (G : SimpleGraph V) (ht : G.CliqueFree 3)
    {v : V} (p : G.Walk v v) (hp : IsShortestOddCycle p) (k : ℕ)
    (hlen : p.length = 2 * k + 1) :
    G.edgeFinset.card ≤ oddCycleBound (Fintype.card V) k
```

## EG617.IsShortestOddLoop

Source: EG617/Core/OddCycleStructure.lean

```lean
def IsShortestOddLoop {v : V} (p : G.Walk v v) : Prop
```

## EG617.bypass_parity_of_short_loops_even

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem bypass_parity_of_short_loops_even (N : ℕ)
    (hN : ∀ v (q : G.Walk v v), q.length < N → Even q.length)
    {a b : V} (p : G.Walk a b) (hp : p.length < N) :
    p.bypass.length % 2 = p.length % 2
```

## EG617.shortestOddLoop_isCycle

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem shortestOddLoop_isCycle {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsCycle
```

## EG617.exists_shortestOddLoop

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem exists_shortestOddLoop (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p
```

## EG617.exists_odd_cycle_of_not_two_colorable

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem exists_odd_cycle_of_not_two_colorable (hG : ¬ G.Colorable 2) :
    ∃ v, ∃ p : G.Walk v v, p.IsCycle ∧ IsShortestOddLoop p
```

## EG617.walk_end_edge_mem_of_length_one

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem walk_end_edge_mem_of_length_one {a b : V} (p : G.Walk a b)
    (hp : p.length = 1) : s(a, b) ∈ p.edges
```

## EG617.shortestOddLoop_isChordless

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem shortestOddLoop_isChordless {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.IsChordless
```

## EG617.cycleGraph_twice_independent_card_le

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem cycleGraph_twice_independent_card_le (m : ℕ)
    (S : Finset (Fin (m + 3)))
    (hS : (SimpleGraph.cycleGraph (m + 3)).IsIndepSet (S : Set (Fin (m + 3)))) :
    2 * S.card ≤ m + 3
```

## EG617.cycle_copy_twice_neighbor_card_le

Source: EG617/Core/OddCycleStructure.lean

```lean
theorem cycle_copy_twice_neighbor_card_le (m : ℕ)
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph (m + 3)) G)
    (ht : G.CliqueFree 3) (x : V) :
    2 * ((Finset.univ : Finset (Fin (m + 3))).filter
      (fun i => G.Adj x (f i))).card ≤ m + 3
```

## EG617.core_not_two_colorable_of_card_24

Source: EG617/Core/R224.lean

```lean
theorem core_not_two_colorable_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
```

## EG617.core_triangleFree_edges_lt_132_of_card_24

Source: EG617/Core/R224.lean

```lean
theorem core_triangleFree_edges_lt_132_of_card_24 (L : SimpleGraph V)
    (hV : Fintype.card V = 24)
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
```

## EG617.core_R224_empty_of_card

Source: EG617/Core/R224.lean

```lean
theorem core_R224_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 24) : ¬ CoreAdmissible 2 G
```

## EG617.core_not_two_colorable_24

Source: EG617/Core/R224.lean

```lean
theorem core_not_two_colorable_24 (L : SimpleGraph (Fin 24))
    (hI : CoreIndependenceBound 11 L) : ¬ L.Colorable 2
```

## EG617.core_triangleFree24_edges_lt_132

Source: EG617/Core/R224.lean

```lean
theorem core_triangleFree24_edges_lt_132 (L : SimpleGraph (Fin 24))
    (ht : L.CliqueFree 3) (hI : CoreIndependenceBound 11 L) :
    L.edgeFinset.card < 132
```

## EG617.core_R224_empty

Source: EG617/Core/R224.lean

```lean
theorem core_R224_empty (G : SimpleGraph (Fin 24)) : ¬ CoreAdmissible 2 G
```

## EG617.core_R3_card_le_degree_add_24

Source: EG617/Core/R224.lean

```lean
theorem core_R3_card_le_degree_add_24 (G : SimpleGraph V)
    (hG : CoreAdmissible 3 G) (v : V) : Fintype.card V ≤ G.degree v + 24
```

## EG617.core_R335_degree_ge_11

Source: EG617/Core/R224.lean

```lean
theorem core_R335_degree_ge_11 (G : SimpleGraph (Fin 35))
    (hG : CoreAdmissible 3 G) (v : Fin 35) : 11 ≤ G.degree v
```

## EG617.core_R337_empty_of_card

Source: EG617/Core/R224.lean

```lean
theorem core_R337_empty_of_card (G : SimpleGraph V)
    (hV : Fintype.card V = 37) : ¬ CoreAdmissible 3 G
```

## EG617.core_R337_empty

Source: EG617/Core/R224.lean

```lean
theorem core_R337_empty (G : SimpleGraph (Fin 37)) : ¬ CoreAdmissible 3 G
```

## EG617.core_R4_card_le_degree_add_37

Source: EG617/Core/R224.lean

```lean
theorem core_R4_card_le_degree_add_37 (G : SimpleGraph V)
    (hG : CoreAdmissible 4 G) (v : V) : Fintype.card V ≤ G.degree v + 37
```

## EG617.core_R447_degree_ge_10

Source: EG617/Core/R224.lean

```lean
theorem core_R447_degree_ge_10 (G : SimpleGraph (Fin 47))
    (hG : CoreAdmissible 4 G) (v : Fin 47) : 10 ≤ G.degree v
```

## EG617.two_cycle_neighbors_cross_card_le_nine

Source: EG617/Core/R23BalancedExterior.lean

```lean
theorem two_cycle_neighbors_cross_card_le_nine (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (hI : CoreIndependenceBound 11 G)
    (S B : Finset V) (v : V) (hd : (S.filter (G.Adj v)).card = 2)
    (hB : B ⊆ Sᶜ) (hedges : ∀ b ∈ B, G.Adj v b) : B.card ≤ 9
```

## EG617.r23_exists_balanced_exterior

Source: EG617/Core/R23BalancedExterior.lean

```lean
theorem r23_exists_balanced_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      ∃ A : Finset ((Sᶜ : Finset V) : Set V),
        let H
```

## EG617.c5_remaining_fiber_sum

Source: EG617/Core/R23CaseI.lean

```lean
theorem c5_remaining_fiber_sum (n : Fin 5 → ℕ) (a : Fin 5)
    (hs : ∑ i, n i = 23) (ha : n a = 10)
    (hplus : n (a + 2) = 1) (hminus : n (a - 2) = 1) :
    n (a + 1) + n (a - 1) = 11
```

## EG617.R23CaseIProfile

Source: EG617/Core/R23CaseI.lean

```lean
def R23CaseIProfile (G : SimpleGraph V) : Prop
```

## EG617.r23_122_case_I

Source: EG617/Core/R23CaseI.lean

```lean
theorem r23_122_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    R23CaseIProfile G
```

## EG617.R23OneEdgeCompletion

Source: EG617/Core/R23CaseII.lean

```lean
def R23OneEdgeCompletion (G : SimpleGraph V) : Prop
```

## EG617.singleton_partition_completes_to_case_I

Source: EG617/Core/R23CaseII.lean

```lean
theorem singleton_partition_completes_to_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S A B : Finset V)
    (hS : Finset.univ.image f = S) (hcover : A ∪ B = Sᶜ)
    (hA : G.IsIndepSet (A : Set V)) (hB : G.IsIndepSet (B : Set V))
    (hAc : A.card = 9) (hBc : B.card = 9)
    (hedges : ∀ x ∈ A, ∀ y ∈ B, G.Adj x y)
    (hd : ∃ u ∈ Sᶜ, (S.filter (G.Adj u)).card = 1 ∧
      ∀ x ∈ Sᶜ, x ≠ u → (S.filter (G.Adj x)).card = 2) :
    R23OneEdgeCompletion G
```

## EG617.R23MissingEdgeExterior

Source: EG617/Core/R23CaseII.lean

```lean
def R23MissingEdgeExterior (G : SimpleGraph V) : Prop
```

## EG617.r23_121_completion_or_missing_exterior

Source: EG617/Core/R23CaseII.lean

```lean
theorem r23_121_completion_or_missing_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121) :
    R23OneEdgeCompletion G ∨ R23MissingEdgeExterior G
```

## EG617.R23ExceptionalProfile

Source: EG617/Core/R23Classification.lean

```lean
def R23ExceptionalProfile (G : SimpleGraph V) : Prop
```

## EG617.missing_exterior_completion_or_exceptional

Source: EG617/Core/R23Classification.lean

```lean
theorem missing_exterior_completion_or_exceptional (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (hm : R23MissingEdgeExterior G) :
    R23OneEdgeCompletion G ∨ R23ExceptionalProfile G
```

## EG617.r23_complete_classification

Source: EG617/Core/R23Classification.lean

```lean
theorem r23_complete_classification (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    R23CaseIProfile G ∨ R23OneEdgeCompletion G ∨ R23ExceptionalProfile G
```

## EG617.r23_122_complete_type_data

Source: EG617/Core/R23CompleteExterior.lean

```lean
theorem r23_122_complete_type_data (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
      (t : V → Fin 5) (P Q : Finset V),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      (∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)) ∧
      P ∪ Q = Sᶜ ∧ P.card = 9 ∧ Q.card = 9 ∧
      (∀ x ∈ P, ∀ y ∈ Q, G.Adj x y)
```

## EG617.r23_122_type_presentation

Source: EG617/Core/R23CompleteExterior.lean

```lean
theorem r23_122_type_presentation (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 122) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G)
      (t : V → Fin 5), Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, cycleNeighborLabels f x = c5Type (t x)) ∧
      ∀ x y, G.Adj x y ↔ (SimpleGraph.cycleGraph 5).Adj (t x) (t y)
```

## EG617.triangleFree_sup_edge_of_no_common_neighbor

Source: EG617/Core/R23EdgeCompletion.lean

```lean
theorem triangleFree_sup_edge_of_no_common_neighbor (G : SimpleGraph V)
    (ht : G.CliqueFree 3) (u v : V) (hne : u ≠ v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    (G ⊔ SimpleGraph.edge u v).CliqueFree 3
```

## EG617.r23_one_edge_completion_case_I

Source: EG617/Core/R23EdgeCompletion.lean

```lean
theorem r23_one_edge_completion_case_I (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : G.edgeFinset.card = 121)
    (u v : V) (hne : u ≠ v) (hn : ¬ G.Adj u v)
    (hcommon : ∀ w, G.Adj u w → ¬ G.Adj v w) :
    let H
```

## EG617.deficit_sum_add

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_sum_add (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) + (∑ v ∈ T, d v) = 2 * T.card
```

## EG617.deficit_zero_iff

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_zero_iff (T : Finset V) (d : V → ℕ) (hd : ∀ v ∈ T, d v ≤ 2) :
    (∑ v ∈ T, (2 - d v)) = 0 ↔ ∀ v ∈ T, d v = 2
```

## EG617.deficit_one_distribution

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem deficit_one_distribution (T : Finset V) (d : V → ℕ)
    (hd : ∀ v ∈ T, d v ≤ 2) (h : (∑ v ∈ T, (2 - d v)) = 1) :
    ∃ v ∈ T, d v = 1 ∧ ∀ w ∈ T, w ≠ v → d w = 2
```

## EG617.ExactC5NeighborLedger

Source: EG617/Core/R23ExactLedger.lean

```lean
def ExactC5NeighborLedger (G : SimpleGraph V) (S : Finset V) : Prop
```

## EG617.r23_exact_neighbor_ledger

Source: EG617/Core/R23ExactLedger.lean

```lean
theorem r23_exact_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧ p.length = 5 ∧
      ExactC5NeighborLedger G p.support.toFinset
```

## EG617.not_two_colorable_of_independence_bound

Source: EG617/Core/R23Reduction.lean

```lean
theorem not_two_colorable_of_independence_bound (G : SimpleGraph V) (a : ℕ)
    (hI : CoreIndependenceBound a G) (hV : 2 * a < Fintype.card V) :
    ¬ G.Colorable 2
```

## EG617.r23_shortestOddLoop_length_five

Source: EG617/Core/R23Reduction.lean

```lean
theorem r23_shortestOddLoop_length_five (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (he : 121 ≤ G.edgeFinset.card) {v : V} (p : G.Walk v v)
    (hp : IsShortestOddLoop p) : p.length = 5
```

## EG617.r23_exists_five_cycle_bipartite_exterior

Source: EG617/Core/R23Reduction.lean

```lean
theorem r23_exists_five_cycle_bipartite_exterior (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ v, ∃ p : G.Walk v v, IsShortestOddLoop p ∧ p.IsCycle ∧
      p.IsChordless ∧ p.length = 5 ∧
      p.support.toFinsetᶜ.card = 18 ∧
      80 ≤ coreInducedEdgeCount G p.support.toFinsetᶜ ∧
      (G.induce ((p.support.toFinsetᶜ : Finset V) : Set V)).Colorable 2
```

## EG617.five_cycle_copy_same_support

Source: EG617/Core/R23TypeLift.lean

```lean
theorem five_cycle_copy_same_support {v : V} (p : G.Walk v v)
    (hc : p.IsCycle) (h5 : p.length = 5) :
    ∃ f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G,
      Finset.univ.image f = p.support.toFinset
```

## EG617.cycleNeighborLabels_card_eq

Source: EG617/Core/R23TypeLift.lean

```lean
theorem cycleNeighborLabels_card_eq
    (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G) (S : Finset V)
    (hS : Finset.univ.image f = S) (x : V) :
    (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card
```

## EG617.r23_exact_labeled_neighbor_ledger

Source: EG617/Core/R23TypeLift.lean

```lean
theorem r23_exact_labeled_neighbor_ledger (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (ht : G.CliqueFree 3)
    (hI : CoreIndependenceBound 11 G) (he : 121 ≤ G.edgeFinset.card) :
    ∃ (S : Finset V) (f : SimpleGraph.Copy (SimpleGraph.cycleGraph 5) G),
      Finset.univ.image f = S ∧ ExactC5NeighborLedger G S ∧
      (∀ x, (cycleNeighborLabels f x).card = (S.filter (G.Adj x)).card) ∧
      (∀ x ∈ Sᶜ, (S.filter (G.Adj x)).card = 2 →
        ∃! i : Fin 5, cycleNeighborLabels f x = c5Type i)
```

## EG617.core_degree_eleven_neighbor_nonedge

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_degree_eleven_neighbor_nonedge (G : SimpleGraph V)
    (hG : CoreCliqueBound 11 G) (v : V) (hd : G.degree v = 11) :
    ∃ x ∈ G.neighborFinset v, ∃ y ∈ G.neighborFinset v, x ≠ y ∧ ¬ G.Adj x y
```

## EG617.core_common_nonneighbors_clique

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_common_nonneighbors_clique (G : SimpleGraph V)
    (hG : CoreIndependenceBound 3 G) (x y : V) (hxy : x ≠ y) (hnot : ¬ G.Adj x y)
    (S : Finset V) (hS : ∀ z ∈ S, z ≠ x ∧ z ≠ y ∧ ¬ G.Adj x z ∧ ¬ G.Adj y z) :
    G.IsClique (S : Set V)
```

## EG617.core_edge_count_union

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_edge_count_union (G : SimpleGraph V) (S T : Finset V) (hd : Disjoint S T) :
    coreInducedEdgeCount G (S ∪ T) = coreInducedEdgeCount G S +
      adjCount G S T + coreInducedEdgeCount G T
```

## EG617.core_pair_cross_lower_bound

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_pair_cross_lower_bound (G : SimpleGraph V) (T : Finset V)
    (x y : V) (hxy : x ≠ y) :
    T.card ≤ adjCount G T {x, y} + (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card
```

## EG617.core_induce_compl

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_induce_compl (G : SimpleGraph V) (T : Finset V) :
    (G.induce (T : Set V))ᶜ = Gᶜ.induce (T : Set V)
```

## EG617.core_induced_compl_edge_count

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_induced_compl_edge_count (G : SimpleGraph V) (T : Finset V) :
    coreInducedEdgeCount G T + coreInducedEdgeCount Gᶜ T = T.card.choose 2
```

## EG617.core_fourteen_cost_obstruction

Source: EG617/Core/R335Fourteen.lean

```lean
theorem core_fourteen_cost_obstruction (G : SimpleGraph V)
    (hcap : ∀ U : Finset V, coreInducedEdgeCount G U ≤ D U.card)
    (T : Finset V) (hT : T.card = 12) (x y : V) (hxy : x ≠ y)
    (hx : x ∉ T) (hy : y ∉ T)
    (hcost : coreInducedEdgeCount Gᶜ T +
      (T.filter (fun z => ¬ G.Adj x z ∧ ¬ G.Adj y z)).card ≤ 6) : False
```

## EG617.core_R223_complement_cost_six

Source: EG617/Core/R335Neighborhood.lean

```lean
theorem core_R223_complement_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 23) (hG : CoreAdmissible 2 G) :
    CostSixProperty Gᶜ
```

## EG617.core_R335_degree_eleven_nonneighbor_cost_six

Source: EG617/Core/R335Neighborhood.lean

```lean
theorem core_R335_degree_eleven_nonneighbor_cost_six (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G)
    (v : V) (hd : G.degree v = 11) :
    let S
```

## EG617.core_R335_degree_ne_eleven

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_degree_ne_eleven (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    G.degree v ≠ 11
```

## EG617.core_R335_degree_ge_twelve

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_degree_ge_twelve (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) (v : V) :
    12 ≤ G.degree v
```

## EG617.core_R335_edges_ge_210

Source: EG617/Core/R335Sharp.lean

```lean
theorem core_R335_edges_ge_210 (G : SimpleGraph V)
    (hV : Fintype.card V = 35) (hG : CoreAdmissible 3 G) :
    210 ≤ G.edgeFinset.card
```

## EG617.core_R336_degree_ge_thirteen

Source: EG617/Core/R336Sharp.lean

```lean
theorem core_R336_degree_ge_thirteen (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) (v : V) :
    13 ≤ G.degree v
```

## EG617.core_R336_edges_ge_234

Source: EG617/Core/R336Sharp.lean

```lean
theorem core_R336_edges_ge_234 (G : SimpleGraph V)
    (hV : Fintype.card V = 36) (hG : CoreAdmissible 3 G) :
    234 ≤ G.edgeFinset.card
```

## EG617.independent_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem independent_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hind : ∀ u ∈ S, ∀ v ∈ S, ¬ (colorGraph c i).Adj u v) :
    S.card ≤ 12
```

## EG617.monochromatic_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem monochromatic_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hmono : ∀ u ∈ S, ∀ v ∈ S, ∀ h : u ≠ v, c (edgeOf u v h) = i) :
    S.card ≤ 12
```

## EG617.colorGraph_clique_card_le_twelve

Source: EG617/Frontend/ColoringReduction.lean

```lean
theorem colorGraph_clique_card_le_twelve (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) (i : Color)
    (hclique : ∀ u ∈ S, ∀ v ∈ S, u ≠ v → (colorGraph c i).Adj u v) :
    S.card ≤ 12
```

## EG617.inducedColorGraph

Source: EG617/Frontend/EdgeCounting.lean

```lean
def inducedColorGraph (c : EdgeColoring) (i : Color) (S : Finset Vertex) :
    SimpleGraph S
```

## EG617.colorEdgeCount

Source: EG617/Frontend/EdgeCounting.lean

```lean
noncomputable def colorEdgeCount (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) : ℕ
```

## EG617.colorEdgeCount_univ

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem colorEdgeCount_univ (c : EdgeColoring) (i : Color) :
    colorEdgeCount c i Finset.univ = (colorGraph c i).edgeFinset.card
```

## EG617.inducedColorGraph_adj_iff

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem inducedColorGraph_adj_iff (c : EdgeColoring) (i : Color)
    (S : Finset Vertex) (u v : S) :
    (inducedColorGraph c i S).Adj u v ↔
      ∃ h : (u : Vertex) ≠ (v : Vertex), c (edgeOf u v h) = i
```

## EG617.induced_edge_unique_color

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_edge_unique_color (c : EdgeColoring) (S : Finset Vertex)
    (u v : S) (h : u ≠ v) :
    ∃! i : Color, (inducedColorGraph c i S).Adj u v
```

## EG617.induced_color_edges_disjoint

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_color_edges_disjoint (c : EdgeColoring) (S : Finset Vertex) :
    ((Finset.univ : Finset Color) : Set Color).PairwiseDisjoint
      (fun i => (inducedColorGraph c i S).edgeFinset)
```

## EG617.induced_color_edges_union

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem induced_color_edges_union (c : EdgeColoring) (S : Finset Vertex) :
    (Finset.univ.biUnion fun i : Color => (inducedColorGraph c i S).edgeFinset) =
      (⊤ : SimpleGraph S).edgeFinset
```

## EG617.sum_colorEdgeCount

Source: EG617/Frontend/EdgeCounting.lean

```lean
theorem sum_colorEdgeCount (c : EdgeColoring) (S : Finset Vertex) :
    ∑ i : Color, colorEdgeCount c i S = S.card.choose 2
```

## EG617.D

Source: EG617/Frontend/HereditaryCaps.lean

```lean
def D (n : ℕ) : ℕ
```

## EG617.colorEdgeCount_add_eleven_tau_le

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem colorEdgeCount_add_eleven_tau_le (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    colorEdgeCount c i S + 11 * tau12 S.card ≤ S.card.choose 2
```

## EG617.hereditary_color_cap

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem hereditary_color_cap (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) : colorEdgeCount c i S ≤ D S.card
```

## EG617.hereditary_cap_subtraction_exact

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem hereditary_cap_subtraction_exact (c : EdgeColoring) (hc : ValidColoring c)
    (S : Finset Vertex) : D S.card + 11 * tau12 S.card = S.card.choose 2
```

## EG617.exists_least_color

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_least_color (c : EdgeColoring) :
    ∃ i : Color, ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ
```

## EG617.least_color_edgeCount_le_870

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem least_color_edgeCount_le_870 (c : EdgeColoring) (i : Color)
    (hi : ∀ j : Color,
      colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) :
    colorEdgeCount c i Finset.univ ≤ 870
```

## EG617.exists_least_color_with_hereditary_cap

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_least_color_with_hereditary_cap (c : EdgeColoring)
    (hc : ValidColoring c) :
    ∃ i : Color,
      (∀ j : Color, colorEdgeCount c i Finset.univ ≤ colorEdgeCount c j Finset.univ) ∧
      colorEdgeCount c i Finset.univ ≤ 870 ∧
      (∀ S : Finset Vertex, colorEdgeCount c i S ≤ D S.card)
```

## EG617.exists_colorGraph_card_edgeFinset_le_870

Source: EG617/Frontend/HereditaryCaps.lean

```lean
theorem exists_colorGraph_card_edgeFinset_le_870 (c : EdgeColoring) :
    ∃ i : Color, (colorGraph c i).edgeFinset.card ≤ 870
```

## EG617.inducedColorGraph_compl_cliqueFree

Source: EG617/Frontend/TuranBounds.lean

```lean
theorem inducedColorGraph_compl_cliqueFree (c : EdgeColoring)
    (hc : ValidColoring c) (i : Color) (S : Finset Vertex) :
    (inducedColorGraph c i S)ᶜ.CliqueFree 13
```

## EG617.tau12_le_colorEdgeCount

Source: EG617/Frontend/TuranBounds.lean

```lean
theorem tau12_le_colorEdgeCount (c : EdgeColoring) (hc : ValidColoring c)
    (i : Color) (S : Finset Vertex) :
    tau12 S.card ≤ colorEdgeCount c i S
```

