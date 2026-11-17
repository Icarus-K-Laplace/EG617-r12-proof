# Counterexample attack report

Latest classification attack (logs/type-lift-attack.json):3240 actual singleton
edge deletions/completions,90 compatible missing-edge cases, and ALL10
incompatible endpoint configurations. Graph adjacency was checked against the
lifted type assignment on every vertex pair; exceptional fiber sizes and121
edges were checked in each incompatible case. No counterexample was found in
this explicitly stated diagnostic domain. The arbitrary-graph completeness
claim comes from r23_complete_classification, not from these tests.

The same90 complete9+9 multiplicity assignments were additionally checked
against ALL Case I fiber conditions, in every available cyclic center.
All satisfy10,A,1,1,B with A+B=11 and1<=A,B<=10. These checks remain
diagnostic; r23_122_case_I independently proves the arbitrary-graph result.

2026-11-15 type-lift check: attacks/type-lift-attack.mjs, output
logs/type-lift-attack.json. All 20 compatible nonempty support pairs were
tested with all positive multiplicity splits: 90 K8,10 assignments each have
an explicit independent 12-element neighborhood; 90 K9,9 assignments satisfy
the full graph/type adjacency equivalence for every vertex pair. A triangle-free
121-edge graph obtained by deleting a compatible cross edge was also checked:
its missing edge refutes the compatibility-to-adjacency converse.
These are diagnostic checks within this specified domain, not completeness
proofs for arbitrary R23 graphs and not trusted Lean inputs.

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

2026-11-16 stronger-deletion attack: attacks/cost-six-deletion-attack.mjs and
logs/cost-six-deletion-attack.json. All61 representatives, including alpha>11
deletions, and EVERY one of351071 independent sets were tested. Worst minimum
cost6 for Case I/deletions and4 for the exceptional graph; no failure.
Rotations/reflections preserve costs and class automorphisms move any deleted
edge to its class-edge representative. This describes the test domain only.
The arbitrary-graph and all-deletions theorems are proved independently in Lean,
using actual finite sets and elementary Fin5 relation certificates. The test
program supplies no theorem premise and no trusted oracle output.

2026-11-18 M4/GATE47 diagnostic attacks:
attacks/r335-fourteen-attack.mjs and logs/r335-fourteen-attack.json checked1000
seeded14-point graphs. All exact complement/cross/union ledgers held; all58
instances of the low-cost condition gave the claimed>=72-edge bound. Removing
the endpoint-outside-T hypothesis is falsified by K12 with T=all12 vertices
and both endpoints inside T: cost0 but only66 total edges.

attacks/gate-shell-attack.mjs and logs/gate-shell-attack.json checked1000 exact
shell ledgers,110000 distinct-endpoint incidence bounds and63940 qualified
row-sum instances. Negative controls detected all deliberately weakened claims:
counting the same endpoint twice (star K1,10); omitting the row-pair>=12 bound
(one-edge missing graph); omitting the per-row missing-degree lower bounds
(K11 missing graph with only two nonzero rows); and omitting the R(4,47)
contract (empty47-vertex graph).

These are precisely bounded diagnostic domains, not an exhaustive search for
R335/R336/GATE47 graphs. No actual counterexample to the retained hypotheses
was found. The formal proofs derive the tested local hypotheses in their parent
theorems; no attack script, output or external certificate is a Lean premise.
