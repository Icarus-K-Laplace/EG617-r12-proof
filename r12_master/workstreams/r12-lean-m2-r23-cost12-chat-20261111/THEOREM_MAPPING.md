# Current classification theorem mapping

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
