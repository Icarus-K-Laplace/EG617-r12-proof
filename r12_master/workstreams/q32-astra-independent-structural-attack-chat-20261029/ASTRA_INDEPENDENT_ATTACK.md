# Independent structural attack — results

Date: 2026-10-29
Overall status: Q32 OPEN; new conditional exclusions proved.

## Route A — near-extremal structure

Instead of classifying all eleven core graphs near69 edges, classify the boundary of the edges incident with O. The elementary lower bound56 has only two shell shapes. Independence forces every large-track vertex to contain a whole shell clique in its O-neighborhood; equality then turns those neighborhoods into a bijection. This is an exact stability-to-rigidity argument.

NEAR_TURAN_STABILITY_THEOREM.md contains the full proof that every non-target color spends at least57 outside edges. The bound is sharp: an explicit129-edge Type-I graph attains it.

## Route B — simultaneous packing

There are749 pairs incident with O. The target owns408-285=123, leaving626 for all non-target colors. The new reserve demands11*57=627. Unique edge ownership gives a one-edge contradiction. This is not a sum of repeated witness/component incidences.

The result applies whenever the target core partitions as12+12+12+11, for every m, without any classification of the exact colors. The known aligned m10,z0/1 cells meet that interface.

## Route C — parent cap and residual rigidity

The genuine parent has alpha(F)<=5 and omega(F)<=11. The clique cap was dropped in the relaxed high-support contract. It immediately forbids target K12 tracks.

A stronger new lemma in COLORED_PACKING_OBSTRUCTION.md proves that in the3+7 cell, four nonempty fibers in both residual maps force a target K12 or K13. Independent enumeration shows that this excludes14 of the18 registered seven-point path/cycle types. Four triangle-containing types with an empty-fiber escape remain.

This proof does not assume that the switch normal form's labels already coincide with the outer track labels. It explicitly checks that ambiguity via degree/extra-edge budgets.

## Route D — adversarial constructions and audit

Two complete single-color graphs attain56 outside edges when the clique cap is removed; both have a K6. A third complete single-color Type-I graph meets the proper cap and attains57. Full edge lists and a separate verifier are supplied. None is a multicolor Q32 counterexample.

The current generic sibling CSP incorrectly applies the non-target clique cap5 to the target color as well. It also does not encode the stronger full-parent alpha(F)<=5 and omega(F)<=11 as such. Its generic UNSAT must not be promoted without correcting the overconstraint. No solver result has been used here.

## What is still needed

For the3+7 branch: exclude the four remaining residual types with at least one empty fiber, or construct a true global completion. This requires coupling the empty-label switch/double configurations with actual endpoint labels and source colors. The symmetric four-nonempty-fiber proof does not apply there.

For the full terminal: m8,m9 and the other m10 light-component possibilities still need structural exclusions. No theorem has been proved that every full-support core admits the excluded four-clique partition. Such a claim would be a new substantive theorem, not a consequence of the scalar37-gap budget.

Difference from existing lines: this work uses shell-component blockers, the parent target clique cap, and analytic outside-edge packing. It does not duplicate A's projection CSP or B's low-support casework. No subagents were used.

