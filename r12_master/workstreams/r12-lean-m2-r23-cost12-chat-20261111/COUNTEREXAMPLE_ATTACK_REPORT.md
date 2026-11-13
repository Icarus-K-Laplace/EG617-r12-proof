# Counterexample attack report

Program: attacks/independent-attack.mjs. Full output: logs/independent-attack.json.
Method: fresh include/exclude recursion enumerating every independent set of each
explicit labeled representative, followed by direct edge and intersection counting.
No imported graph code or prior maximal-clique enumeration was used.

Results: 20 compatible nonempty type-set pairs, 10 incompatible missing-endpoint
cases, 55 singleton extension positions; 61 representatives, 49 legal under
alpha<=11, 271235 independent sets tested, no Cost-6 violation in that domain.
The exact feasible B23 and B18 tables are included in the output.

Limits: this is not a Lean proof, not a completeness argument for all 23-point
graphs, and not an exhaustive search of GATE47. No actual counterexample to the
unchanged GATE47 or Cost-6 target was found. Absence in this finite test is not a proof.

Semantic attack: interpreting type compatibility as actual adjacency is false.
Take C5(10,5,1,1,6) and delete one edge between classes 0 and 1. It is triangle-free,
has 121 edges and independence number 11. Any new independent set using that
deleted edge has just its two endpoints plus at most the one vertex in class 3;
other independent sets already existed in the original blow-up. Choose the fixed
C5 using other vertices in classes 0 and 1. The deleted endpoints have disjoint
two-neighbor types, but are nonadjacent. This refutes that converse, not the
original classification, which explicitly allows compatible missing endpoints.

The implemented exterior theorem retains an explicit missing-edge alternative.
No parent theorem is promoted on the basis of the invalid adjacency converse.
