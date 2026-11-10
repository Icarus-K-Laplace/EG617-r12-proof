# Verified M1 axiom audit

47 declarations, no missing or duplicate reports, standard three-axiom allowlist PASS. These results are from the actual Linux job, not source scanning.

|Declaration|Transitive axioms|
|---|---|
|EG617.colorGraph|propext, Quot.sound|
|EG617.colorGraph_adj_iff|propext, Quot.sound|
|EG617.validColoring_iff_colorGraph|propext, Classical.choice, Quot.sound|
|EG617.colorGraph_partition|propext, Quot.sound|
|EG617.no_independent_thirteen|propext, Classical.choice, Quot.sound|
|EG617.no_monochromatic_thirteen|propext, Classical.choice, Quot.sound|
|EG617.Vertex|none|
|EG617.Color|none|
|EG617.Edge|propext, Quot.sound|
|EG617.EdgeColoring|propext, Quot.sound|
|EG617.edgeOf|propext, Quot.sound|
|EG617.Inside|propext, Classical.choice, Quot.sound|
|EG617.edgeOf_swap|propext, Quot.sound|
|EG617.edgeOf_eq_iff|propext, Quot.sound|
|EG617.edge_has_endpoints|propext, Quot.sound|
|EG617.edgeOf_surjective|propext, Quot.sound|
|EG617.edgeOf_inside_iff|propext, Classical.choice, Quot.sound|
|EG617.inside_mono|propext, Classical.choice, Quot.sound|
|EG617.mem_complete_iff|propext, Classical.choice, Quot.sound|
|EG617.edgeEquivComplete|propext, Classical.choice, Quot.sound|
|EG617.ValidColoring|propext, Classical.choice, Quot.sound|
|EG617.EG617R12Statement|propext, Classical.choice, Quot.sound|
|EG617.validColoring_iff_endpoints|propext, Classical.choice, Quot.sound|
|EG617.originalProblem_iff_missingColor|propext, Classical.choice, Quot.sound|
|EG617.tau12|none|
|EG617.tau12_add_turanNumber|propext, Classical.choice, Quot.sound|
|EG617.independent_card_le_twelve|propext, Classical.choice, Quot.sound|
|EG617.monochromatic_card_le_twelve|propext, Classical.choice, Quot.sound|
|EG617.colorGraph_clique_card_le_twelve|propext, Classical.choice, Quot.sound|
|EG617.inducedColorGraph|propext, Classical.choice, Quot.sound|
|EG617.colorEdgeCount|propext, Classical.choice, Quot.sound|
|EG617.colorEdgeCount_univ|propext, Classical.choice, Quot.sound|
|EG617.inducedColorGraph_adj_iff|propext, Classical.choice, Quot.sound|
|EG617.induced_edge_unique_color|propext, Classical.choice, Quot.sound|
|EG617.induced_color_edges_disjoint|propext, Classical.choice, Quot.sound|
|EG617.induced_color_edges_union|propext, Classical.choice, Quot.sound|
|EG617.sum_colorEdgeCount|propext, Classical.choice, Quot.sound|
|EG617.D|none|
|EG617.colorEdgeCount_add_eleven_tau_le|propext, Classical.choice, Quot.sound|
|EG617.hereditary_color_cap|propext, Classical.choice, Quot.sound|
|EG617.hereditary_cap_subtraction_exact|propext, Classical.choice, Quot.sound|
|EG617.exists_least_color|propext, Classical.choice, Quot.sound|
|EG617.least_color_edgeCount_le_870|propext, Classical.choice, Quot.sound|
|EG617.exists_least_color_with_hereditary_cap|propext, Classical.choice, Quot.sound|
|EG617.exists_colorGraph_card_edgeFinset_le_870|propext, Classical.choice, Quot.sound|
|EG617.inducedColorGraph_compl_cliqueFree|propext, Classical.choice, Quot.sound|
|EG617.tau12_le_colorEdgeCount|propext, Classical.choice, Quot.sound|

M2 candidate declarations have not been audited yet. MainTheorem is absent. No assertion of full EG617 verification.
