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
| Low M2 four type cases | none | Complete classification gap |
| Low M3 | none | Cost-6 gap |
| Low M4 | core_R335_degree_ge_11 only | Sharp degree12 and e210 still gaps |
| Low M5 | core_R337_empty_of_card | R337 done; sharp R336 still gap |
| Low M6 | core_R447_degree_ge_10 only; Gate47Statement definition | d10/d11 exclusions and degree12 theorem absent |
| Original conclusion | MainTheorem absent | No full EG617 proof |

CoreAdmissible contains ALL finite induced D bounds, alpha and omega bounds.
No theorem gains completion credit by assuming Cost-6, the classification, or GATE47.
