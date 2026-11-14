# Current proof obligations

2026-11-15: P0 exact ledger CLOSED by r23_exact_neighbor_ledger,
4454d72 / CI 43573005534. All saturation obligations below are historical.
Current smallest obligation: verify same-support C5 copy and cardinal transfer
(R23TypeLift candidate), then derive the complete actual-vertex type partition
and its cross-side constraints in each of the three exact exterior forms.
Frozen M2a-M2d source has now been read: see FROZEN_CLASSIFICATION_SOURCE.md.
No whole-graph blow-up equivalence, singleton graph extension, or Cost-6 theorem
has been established. Compatibility must not be used to infer an edge.

Update 2026-11-14: C5Types and C5MissingEdge PASS in 89183d0 / CI 43570397008.
The final elaboration fix unfolded ExistsUnique before kernel decision; no
mathematical hypothesis changed. All first-obligation candidates below now pass.
The history of failed obligations is retained below for reproducibility.

Highest-value open obligation: derive exact cycle-neighbor saturation from the
121/122 edge ledger, then partition all actual vertices into the proved types.
The quotient theorems explicitly require labels and full cross edges; these must
be derived from the original R23 hypotheses, never assumed as terminal conditions.
Next: blow-up cardinalities and adjacency equivalences for all four cases.
Cost-6, sharp R335/R336 and GATE47 remain FORMALIZATION_GAP.

Last fully verified baseline: 875bd3de / CI 43361985046, published at 7975ad8.
C5Types and C5MissingEdge are candidates in addeeb4d, CI 43570190760.
Focused checks precede the full build. No candidate is promoted before actual CI output.

Resolved source obligations from failed CI 43365758378 (recheck pending):
- c5_independent_pair_unique_type: instead of deciding over all Finsets without
  a Fintype instance, decompose card=2 by Finset.card_eq_two, then check all Fin 5 pairs.
- c5_complete_type_sets: specify `(s := A)` in Finset.one_lt_card to avoid an
  unconstrained cardinality metavariable. This was a tactic elaboration issue.

Next graph-level obligation: derive neighbor-cardinality saturation (all two-neighbor
vertices, or exactly one singleton) from the exact 121/122 edge ledger, so the
type-image theorem's explicit label hypotheses follow from the original R23 contract.
Missing-edge type sets, all five rotations/two orientations, and singleton extension
are included in the current focused check. They do not yet identify whole blow-ups.

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
