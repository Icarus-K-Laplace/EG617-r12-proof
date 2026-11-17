# Paper-to-Lean mapping

Frozen attribution: low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md, c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2,
M1-M6, via the retained independent audit. Exact source theorem statements are
collected in DECLARATION_STATEMENTS.md; CI prints their elaborated types.

| Paper item | Lean declaration(s) | Meaning and boundary |
|---|---|---|
| Original K145 | EG617R12Statement; originalProblem_iff_missingColor | Original coloring statement preserved; truth not proved |
| Frontend M1 | hereditary_color_cap; sum_colorEdgeCount; exists_least_color_with_hereditary_cap | Original exact color ledger and all induced caps, <=870 |
| Low M1 | core_R224_empty_of_card | Full CoreAdmissible 2 on any finite 24-vertex type impossible |
| Low M2 shortest odd cycle | shortestOddCycle_iff_shortestOddLoop; shortestOddLoop_isCycle; shortestOddLoop_isChordless | Working walk definition proved equivalent to usual minimal simple odd cycle |
| Low M2 cycle/cross/exterior ledger | cycle_support_card; chordless_cycle_induced_edges; shortestOddLoop_neighbor_card_le; edge_partition; triangleFree_induced_mantel | Standard Finset vertex and unordered edge counts; no capacity assumption |
| Low M2 B(n,k) | shortestOddCycle_edge_bound; triangleFree_nonbipartite_edge_bound | Arbitrary finite type; actual graph upper bound |
| Low M2 numeric bounds | oddCycleBound_23_two; oddCycleBound_23_ge_three; oddCycleBound_23_three; oddCycleBound_18; oddCycleBound_18_two | Feasible k domain explicit; floor is natural division |
| Low M2 shortest C5 | r23_shortestOddLoop_length_five | 23 vertices, triangle-free, e>=121, shortest odd loop |
| Low M2 exterior | r23_exists_five_cycle_bipartite_exterior | Full alpha<=11 assumption supplies nonbipartiteness; exterior has 18 vertices and >=80 edges |
| Low M2 exterior three forms | bipartite_18_dense_classification | Parts are independent, cover all vertices; every cross adjacency is specified |
| Low M2a / Case I,122 edges | r23_122_case_I; R23CaseIProfile | VERIFIED CI43618192344: actual adjacency iff and exact10,A,1,1,B fibers; A+B=11; 1<=A,B<=10 |
| Low M2c / K8,10 exclusion | r23_exists_balanced_exterior | VERIFIED: original R23 contract implies balanced9+9 exterior |
| Low M2b /singleton graph completion | r23_121_completion_or_missing_exterior | VERIFIED: actual added edge, triangle-free, alpha<=11, exactly122 edges, Case I |
| Low M2d /unique missing edge | missing_exterior_completion_or_exceptional | VERIFIED: compatible completion or full9,9,2,1,2 adjacency/fiber profile |
| Complete Low M2 | r23_complete_classification | VERIFIED CI43680628810; only original23-vertex, triangle-free, alpha<=11, e>=121 hypotheses |
| Low M3 | r23_cost_six; case_I_cost_six; case_I_single_edge_deletion_cost_six; exceptional_cost_four | VERIFIED universal Cost-6; all deletions, every independent set; exceptional Cost-4 |
| Low M4 | core_fourteen_cost_obstruction; core_R335_degree_ne_eleven; core_R335_degree_ge_twelve; core_R335_edges_ge_210 | VERIFIED: actual14-set, derived Cost-6,72>D14=69, sharp degree12/e210 with full graph class |
| Low M5 | core_R336_degree_ge_thirteen; core_R336_edges_ge_234; core_R337_empty_of_card | VERIFIED: sharp degree13/e234, inherited full caps and exact neighbor deletion; R337 retained |
| Low M6 / Theorem M | core_R447_min_degree_ten_edges_ge_289; core_R447_min_degree_eleven_edges_ge_287; gate47_verified | VERIFIED: exact frozen Gate47Statement, all original graph conditions; full helper mapping in GATE47_FORMALIZATION.md |
| Original conclusion | MainTheorem absent | No full EG617 proof |

CoreAdmissible contains ALL finite induced D bounds, alpha and omega bounds.
No theorem gains completion credit by assuming Cost-6, the classification, or GATE47.
