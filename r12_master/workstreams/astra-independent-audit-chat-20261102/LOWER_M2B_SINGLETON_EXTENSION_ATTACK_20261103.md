# Lower-order M2b: independent attack on the singleton-neighborhood extension

Date: 2026-11-03  
Frozen source: `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`, Section M2b, at integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO GAP FOUND.** The only delicate M2b move is adding one cycle edge to the exceptional exterior vertex with a singleton C5-neighborhood. An independent exhaustive check verifies that such an extension always exists for every compatible pair of type sets and every possible singleton neighbor.

## Exact condition

Let the five C5 vertices be Z/5Z and let a two-neighbor type be
[
T_i={i-1,i+1}.
]
The compatibility graph on types is C5: two types are compatible exactly when their indices are adjacent in C5.

For the K9,9 exterior, let A and B be the nonempty type sets on the two sides after removing the exceptional vertex u from A. Every A-B pair is compatible. The type quotient implies one side is a singleton and the other has at most two types. The singleton cycle-neighbor p of u lies outside
[
U_B=igcup_{jin B}T_j,
]
otherwise u and a neighbor of type T_j would form a triangle.

To add a second cycle edge u-q while preserving triangle-freeness and the two-neighbor type form, it suffices to find q outside U_B such that {p,q}=T_i for some i. If |B|=1, the complement of U_B has three vertices; every one belongs to an independent pair within that complement. If |B|=2, B must be the two types compatible with the singleton A-type; their union has size3, and its two-vertex complement is itself an independent pair.

## Independent exhaustive check

`RECHECK_LOWER_M2B_EXTENSION.py` independently reconstructs all compatible nonempty type-set pairs and checks every possible p outside U_B.

- Compatible type-set pairs:20.
- Singleton-neighborhood positions checked:55.
- Every position has at least one valid q.
- Each selected pair {p,q} is a genuine T_i and is disjoint from every opposite-side type, so adding u-q creates no triangle.

This verifies the M2b extension step. The subsequent M3 12-set cost certificate already checks all edge-deleted blowup representatives and their maximal independent sets. This local check does not certify the entire minimum-degree gate or the global EG617 proof.
