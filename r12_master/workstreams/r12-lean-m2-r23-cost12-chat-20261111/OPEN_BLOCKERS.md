# Current proof obligations

Last fully verified baseline: 875bd3de / CI 43361985046, published at 7975ad8.
C5Types is a new candidate and requires its focused kernel/type/axiom check.

1. P0 first obligation: every actual two-neighbor vertex on a five-cycle has a
unique type, and complete bipartite adjacency forces a singleton-side type quotient.
Candidate: cycleNeighborLabels_unique_type and complete_bipartite_type_image.
2. Derive all two-neighbor/singleton cases from the exact edge ledger, then lift
the quotient to exhaustive blow-up identification, including unique missing-edge
endpoint cases and singleton extension. No general classification theorem exists yet.
3. P1: Cost-6 for every independent set in every legal classified graph.
4. P2/P3: sharp R335/R336, then d10/d11 exclusions with full CoreAdmissible caps.

No mathematical error is claimed. Compatibility gives a necessary edge condition,
not a converse. Each failed obligation is allowed at most three materially different
strategies; after that record the exact failure and switch to an independent obligation.
