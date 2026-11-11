# Complete axiom audit

Verified code ee2dbe9d6d0c5298dc6cfc8a4f8c91e5d8bcdf06; [actual Linux run](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/42953650338). 72 declarations, 53 theorems. Every declaration has exactly one actual transitive axiom report; allowed union only propext, Classical.choice, Quot.sound.

No sorryAx, custom mathematical axiom, admit, native_decide, unsafe implementation or external proof oracle. Unfinished major theorems are absent, not supplied as placeholders. Gate47Statement is a target Prop definition without a proof. Graph hypotheses are explicit in the full types and CoreAdmissible expansion, not hidden axioms. The original ValidColoring premise is an assumption used in frontend conditional lemmas; its impossibility remains unproved.

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
