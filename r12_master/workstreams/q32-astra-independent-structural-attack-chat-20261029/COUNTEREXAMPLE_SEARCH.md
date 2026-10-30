# Adversarial search and independent verification

Date: 2026-10-29

## Explicit objects produced

1. two_edges_without_clique_cap.json and triangle_without_clique_cap.json:
   complete labeled61-vertex single-color edge lists, each with125 edges, alpha12, omega6, and56 outside edges. Each graph is11K5 disjoint-union K6, with a different placement of O and the tracks. These disprove any attempt to improve56 without using the clique restriction. They deliberately fail omega<=5 and are not Q32 candidates.

2. sharp_typeI_single_color.json:
   complete129-edge source-correct Type-I graph, alpha12, omega5, and57 outside edges. Parameter a=1, x=10, y=5, A0={0}; Ns=0..4 and Nt=5..9; ten isolated K5s occupy11..60. O and all four independent tracks are explicit. Its core has72 edges. This proves sharpness of the new single-color reserve; it is not an eleven-color packing.

No object here satisfies all scalar, source, projection, degree and edge-color constraints of the full Q32 problem. No abstract-incidence SAT or full-color SAT is claimed. The hierarchy is maintained: a genuine single-color graph is still not a genuine multicolor counterexample.

## Checks performed

verify_outside_reserve.py, Python3.12.14, standard library only:
- all14 integer k cases in the56-edge boundary, plus p in Z;
- all16384 O-neighbor subsets in each shell shape, tested against every maximum independent12-transversal: blocker iff a full shell component is contained;
- full labeled edge-list and partition verification for all three explicit graphs;
- exact alpha/omega by exhaustive search in each connected component (largest component11);
- all four legal source parameters a=1,2,3,4 and their variable degrees;
- exact outside-edge ownership arithmetic627>626.

verify_residual_types.py:
- exhaustive component-multiset enumeration for seven-point maximum-degree-two graphs;
- direct subset computation of alpha and clique-cover number, not formulas copied from the claimed classification;
-18 registered types,14 with clique-cover number4, four remaining with number3.

These are deterministic finite replays and graph witnesses; no SAT/ILP solver, symmetry quotient on full colorings, or UNSAT proof certificate is invoked. The analytic theorems carry the conditional exclusions.

## CSP audit at immutable high-support HEAD

433a5b39a98325f00e99650b0270d79f7753a47d:
- q32_fullsupport_vertex_labelled_csp.py lines475-499 loops over range(12), searches an independent13-set and a clique6 for every color, including target0.
- verify_q32_fullsupport_candidate.py lines490-500 checks clique6 for ALL_COLORS.
- the specification says the same explicitly.

The true parent requires alpha(F)<=5 and omega(F)<=11. For C != target, omega(C)<=5 follows from alpha(F)<=5. This derivation does not give omega(F)<=5. The error is in the selected mathematical cap, not in the clique-search routine.

The target core alpha<=4 check does not replace full-parent alpha<=5 on61 vertices. Adding legitimate constraints would strengthen a relaxation; the unjustified target K6 cuts instead invalidate the advertised equivalence. We did not edit sibling code.

## Smallest unresolved cell reached here

Within the registered3+7 reduction, only:
C3+2P2 (z2), C3+P4 (z3), 2C3+P1 (z3),
with an empty fiber in at least one of the two residual maps, remain after the new theorem.

This is a reduced open family, not a proof of minimality among all possible formulations. No claim that current abstract constraints alone are feasible or insufficient in the strong success-criterion-E sense is made.

## New z4 replay, 2026-10-30

verify_z4_empty_fibers.py independently checks the local assertions used by the analytic proof in COLORED_PACKING_OBSTRUCTION.md Section4. Python3.12.14, standard library, no randomization or external solver:
-3456 normalized4,5,5 triple inputs; precisely156 have no independent5-set.
-42336 aligned/switch local representations, with every base permutation, extra edge, minority small block, and switch orientation.
-12 unordered residual clique partitions, including two with an empty class; all44 ordered pairs with at least one empty class.
-782 raw admitted23-vertex local representations, yielding158 distinct summaries; every admitted raw representation is checked before deduplication.
-Only four raw representations across the two equal-partition cases are light-compatible with the fixed special block: the special and normal forms in each case.
-The terminal integer conditions force two special and two other blocks, hence E0=6<9.

The complete summary table is z4_local_profiles.json; each row includes an actual local matching/extra representative. It is a necessary-condition table, not a full coloring assignment. All omitted full-model conditions, the symmetry justification, and the exact scope of the local replay are described in the theorem file. The hand proof, not a claim of a full-model UNSAT certificate, establishes the conditional cell exclusion. The previous exploratory program was replaced in place by this asserted verifier; no duplicate version is retained.

