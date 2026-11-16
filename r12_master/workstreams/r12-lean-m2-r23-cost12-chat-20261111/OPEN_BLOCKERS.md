# Current minimal proof obligations

R23 classification CLOSED at0d2985d / CI43680628810:
r23_complete_classification has only the original four R23 graph hypotheses.
All four frozen M2 cases, both singleton-side orientations, all five rotations
and both incompatible endpoint orientations have been assembled.

Next: Cost-6, with actual finite sets and unordered induced edges.
1. From a C5 type presentation, transfer arbitrary graph-independent sets to
   independent type supports and prove the exact twelve-vertex witness counts.
2. Case I: witnesses P+s+t, A+B+s, A+B+t; costs must cover EVERY independent set.
3. Single-edge deletions: separate independent sets already independent in the
   supergraph from those containing both deleted endpoints. Exclude deletion
   of the two singleton classes using the ORIGINAL alpha<=11 condition.
4. Exceptional profile: witnesses P+C+d and Q+d+E, each twelve vertices and
   two induced edges; one intersects every independent set in at most two points.
5. Then sharp R335/R336 and GATE47, including all hereditary D/alpha/omega conditions.

No mathematical counterexample has been found. Tests are not proofs.
Failed CI logs are retained, including classification instance/cardinality fixes;
they do not indicate a mathematical error. MainTheorem remains absent.

2026-11-16: items 1,2,4 above verified at 0dc1190e / CI43791548801. Item3 now has a structural candidate, not yet certified.

2026-11-16 update: item3 CLOSED by case_I_single_edge_deletion_cost_six; universal r23_cost_six PASS at e3885e0 / CI43792528236. Next minimal obligation is M4's actual fourteen-point cap contradiction; the nonneighborhood Cost-6 transfer is now a candidate.
