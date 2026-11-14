# Current classification theorem mapping

Update 2026-11-15, code 2dba3b9 / CI 43616747074: all the following
statements are kernel/type/axiom PASS. Exact signatures are preserved in the
named standard .lean modules and the full CI statement-inspection output.

| Frozen source obligation | Verified theorem | Exact scope |
|---|---|---|
| M2 same C5 neighbor labeling | r23_exact_labeled_neighbor_ledger | Original R23 hypotheses, same support image, exact count transfer, unique types |
| M2c exclusion of K8,10 | r23_exists_balanced_exterior | Original R23 hypotheses; SAME labeled C5; only K9,9 or K9,9-e exterior |
| M2a complete graph/type lift | complete_exterior_has_type_presentation | Actual complete cross edges plus two-neighbor counts; types constructed |
| M2a 122-edge graph presentation | r23_122_type_presentation | Original R23 assumptions plus exactly122 edges; adjacency iff C5 type adjacency |

Equivalence: Fin 5 is the labeled cycle itself; cycleNeighborLabels records
actual G edges to that copy. The map in the last theorem is assigned to every
actual vertex, and the iff describes all ordered vertex pairs. It is the C5
blow-up adjacency definition, but does NOT yet assert the required fiber sizes.
The subtype exterior is exactly the complement finset of this SAME cycle.
M2b and M2d remain graph-level gaps despite their verified finite type lemmas.

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
