# Current theorem mapping

Verified code0d2985dbfe109fab301c157f687b3b38478c8bb6, CI43680628810.
Every listed theorem has an actual kernel build, #check and transitive axiom
report in logs/linux-43680628810-full.txt. Verbatim signatures are collected in
DECLARATION_STATEMENTS.md; full proofs remain in standard .lean files.
The baseline/global mapping is PAPER_THEOREM_MAPPING.md.

| Frozen low source | Theorem | Formal meaning |
|---|---|---|
| M2 opening ledger | r23_exact_neighbor_ledger | Original R23 contract implies exact edge/deficit distribution |
| M2 actual labels | r23_exact_labeled_neighbor_ledger | Same cycle support, exact count transfer, unique types |
| M2c | r23_exists_balanced_exterior | K8,10 excluded by actual independent12-set;9+9 parts remain |
| M2a | r23_122_case_I | All actual adjacency and10,A,1,1,B fiber sizes |
| M2b | r23_121_completion_or_missing_exterior | Actual singleton completion; only unique missing-edge alternative remains |
| M2d endpoint quotient | missing_exterior_type_orientations | Both eight-point remainders constant; every orientation included |
| M2d exact fiber ledger | missing_exterior_type_fiber_formula; c5_missing_fiber_profile | Cycle vertices plus8+8+1+1 exterior pieces give9,9,2,1,2 |
| M2d whole graph | missing_exterior_completion_or_exceptional | Compatible completion or exceptional graph, preserving real adjacency |
| Complete M2 | r23_complete_classification | Exhaustive original-hypothesis classification |
| M3 | none yet | Universal Cost-6 remains open |

Equivalence with paper definitions: independence is the bound on every finite
independent subset, induced edges are actual unordered edgeFinset cardinalities,
and every blow-up profile gives an actual-vertex map, ALL adjacency iff relations
and all five positive fiber sizes. Single-edge deletion is represented by
G sup edge(u,v) with distinct, originally nonadjacent endpoints. No finite
representative list, classification assumption or external oracle is trusted.

M3 Case I: case_I_cost_six; M3 exceptional: exceptional_cost_four and exceptional_cost_six, verified 0dc1190e / CI43791548801. Signatures in DECLARATION_STATEMENTS.md. M3 edge-deletion and complete r23_cost_six remain candidates.

Full frozen M3: r23_cost_six, with only card23, triangle-free, alpha<=11 and edge>=121 hypotheses, verified e3885e0 / CI43792528236. Single-edge lemma covers all deletions, including the singleton edge, using a stronger proof; the original parent hypotheses are retained.
