# Current classification theorem mapping

2026-11-15 exact ledger: r23_exact_neighbor_ledger (Core/R23ExactLedger.lean)
maps to frozen low M2 opening edge ledger and the saturation in M2a-M2d.
VERIFIED 4454d72 / CI 43573005534. Hypotheses: card V=23, triangle-free,
CoreIndependenceBound 11, at least121 edges; conclusion retains the SAME shortest
five-cycle support, 18 exterior vertices, five internal edges, 80<=y<=81,
121<=e<=122, e=5+x+y, x in {35,36}, and exact neighbor deficits/distributions.
CoreIndependenceBound is the original finite-set alpha bound; induced counts
are actual induced-graph edgeFinset cardinalities, not abstract ledger variables.

Candidate: five_cycle_copy_same_support, cycleNeighborLabels_card_eq,
r23_exact_labeled_neighbor_ledger (Core/R23TypeLift.lean). These connect that
same support to the actual Fin 5 neighbor labels; not a graph classification.
All exact theorem statements are in the named .lean source and Audit/R23TypeLift.lean.

All candidates in the table below are now kernel/type/axiom PASS at 89183d0,
CI 43570397008. The original candidate labels are historical.
Also verified: c5_missing_edge_type_sets (singleton remaining types on both sides),
c5_missing_endpoint_orientations (all five rotations and two orientations), and
c5_singleton_extension (extension compatible with every opposite-side type).
These correspond to frozen low M2 Cases IV and II. The four-label finite domain
is the exact type domain supplied by cycleNeighborLabels_unique_type; no external
representative list is trusted. Whole-graph isomorphism/classification is still open.

Frozen low M2 type-quotient paragraph; exact source statements are retained in .lean.
Baseline mappings and original K145 semantics: PAPER_THEOREM_MAPPING.md.

| Obligation | Lean theorem | Scope | Current check |
|---|---|---|---|
| Exhaustive five two-neighbor types | c5_independent_pair_unique_type | Every independent two-element subset of Fin 5, unique center | Candidate |
| Actual graph-to-type bridge | cycleNeighborLabels_unique_type | Any C5 copy in any triangle-free graph; exact neighbor cardinality 2 | Candidate |
| Adjacency requires compatibility | adjacent_cycleNeighborLabels_disjoint | Actual graph edge implies disjoint label sets; no converse asserted | Candidate |
| Complete compatible type sets | c5_complete_type_sets | Nonempty complete cross-compatible type sets: singleton side, both sizes <=2 | Candidate |
| Complete bipartite quotient | complete_bipartite_type_image | Explicit actual cross edges and exact label/type equality | Candidate |

The finite checks range over the entire formal types Fin 5 / Finset (Fin 5),
not an externally supplied list of representatives. The graph-to-type bridge proves
why that finite domain applies. No external enumerator is trusted.
