# Current theorem mapping

All listed proved results are kernel-checked with exact types and transitive
axioms in the complete CI log identified by CI_STATUS.json. Full verbatim source
signatures: DECLARATION_STATEMENTS.md. Global mapping: PAPER_THEOREM_MAPPING.md.
Frozen source: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2, low minimum-degree gate.

| Frozen item | Lean theorem | Actual mathematical meaning |
|---|---|---|
| M2 edge ledger | r23_exact_neighbor_ledger | Exact121/122 edges and all three neighbor distributions |
| M2 actual labels | r23_exact_labeled_neighbor_ledger | Same cycle support and unique real vertex types |
| M2c | r23_exists_balanced_exterior | K8,10 excluded using original independence bound |
| M2a | r23_122_case_I | All adjacency iff and10,A,1,1,B actual fibers |
| M2b | r23_121_completion_or_missing_exterior | Actual singleton completion or unique missing edge |
| M2d | missing_exterior_completion_or_exceptional | Compatible completion or9,9,2,1,2 whole graph |
| Complete M2 | r23_complete_classification | Only four original R23 hypotheses |
| M3 actual witness ledger | c5_three_fiber_witness_counts | Exact cardinality, induced unordered edges and intersections |
| M3 arbitrary independent sets | independent_c5_fiber_counts | Actual independence forces adjacent fiber intersections empty on one side |
| M3 Case I | case_I_cost_six | Universal Cost-6 via three actual twelve-point witnesses |
| M3 single-edge deletion | case_I_single_edge_deletion_cost_six | All new independent sets; stronger sublemma also covers singleton deletion |
| M3 exceptional | exceptional_cost_four; exceptional_cost_six | Universal Cost-4, hence Cost-6 |
| Complete M3 | r23_cost_six | Original R23 hypotheses imply the exact universal Cost-6 property |
| M4 input from full caps | core_R223_complement_cost_six | D(23), alpha and omega derive every Cost-6 input |
| M4 actual nonneighborhood | core_R335_degree_eleven_nonneighbor_cost_six | Full R(3,35), degree11, actual23-point nonneighborhood |
| Remaining M4/M5/M6 | no sharp/gate theorem | Fourteen-point ledger, sharp R335/R336 and GATE47 open |

Equivalence: independent sets are actual Finsets; the independence bound ranges
over every such set; edges are unordered induced edgeFinset cardinalities.
The blow-up maps prescribe ALL adjacency iff relations and fiber sizes.
The classified deleted-edge graph is precisely G with one absent edge added.
The deletion helper proves a stronger property, but r23_cost_six retains all
original hypotheses. No oracle, representative enumeration or terminal assumption
supplies a parent theorem. MainTheorem is absent.
