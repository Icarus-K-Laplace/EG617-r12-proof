# Independent structural attack — results

Date: 2026-10-30
Overall status: Q32 OPEN; new conditional exclusions proved.

Current result: the entire registered m10 disconnected3+7 normal form is excluded, covering all18 residual types. COLORED_PACKING_OBSTRUCTION.md Section7 states the complete graph contract. The remaining frontier is outside this normal form, not an unresolved empty-fiber case within it.

## Route A — near-extremal structure

Instead of classifying all eleven core graphs near69 edges, classify the boundary of the edges incident with O. The elementary lower bound56 has only two shell shapes. Independence forces every large-track vertex to contain a whole shell clique in its O-neighborhood; equality then turns those neighborhoods into a bijection. This is an exact stability-to-rigidity argument.

NEAR_TURAN_STABILITY_THEOREM.md contains the full proof that every non-target color spends at least57 outside edges. The bound is sharp: an explicit129-edge Type-I graph attains it.

## Route B — simultaneous packing

There are749 pairs incident with O. The target owns408-285=123, leaving626 for all non-target colors. The new reserve demands11*57=627. Unique edge ownership gives a one-edge contradiction. This is not a sum of repeated witness/component incidences.

The result applies whenever the target core partitions as12+12+12+11, for every m, without any classification of the exact colors. The known aligned m10,z0/1 cells meet that interface.

## Route C — parent cap and residual rigidity

The genuine parent has alpha(F)<=5 and omega(F)<=11. The clique cap was dropped in the relaxed high-support contract. It immediately forbids target K12 tracks.

A stronger lemma in COLORED_PACKING_OBSTRUCTION.md proves that in the3+7 cell, four nonempty fibers in both residual maps force a target K12 or K13. This excludes14 of18 registered seven-point path/cycle types. New Section4 excludes C3+C4, z4, even when either map has an empty fiber, raising the count to15. The parent clique cap forces at least two special blocks; their light-neighbor classification and the two-heavy-neighbor budget force E0=6, contradicting E0>=9. This is a complete analytic conditional exclusion of the cell.

This proof does not assume that the switch normal form's labels already coincide with the outer track labels. It explicitly checks that ambiguity via degree/extra-edge budgets.

## Route D — adversarial constructions and audit

Two complete single-color graphs attain56 outside edges when the clique cap is removed; both have a K6. A third complete single-color Type-I graph meets the proper cap and attains57. Full edge lists and a separate verifier are supplied. None is a multicolor Q32 counterexample.

The current generic sibling CSP incorrectly applies the non-target clique cap5 to the target color as well. It also does not encode the stronger full-parent alpha(F)<=5 and omega(F)<=11 as such. Its generic UNSAT must not be promoted without correcting the overconstraint. No solver result has been used here.

## What is still needed

New Section5 of COLORED_PACKING_OBSTRUCTION.md excludes2C3+P1,z3. Its two additional incidences are both owned by the isolated residual vertex. The two full residual triangles force two disjoint diversion classes of at least two blocks each; opposite diversions cannot be light-adjacent. The heavy-degree bound forces exactly two of each and zero residual slack at those four blocks. Each remaining block must then realize two contradictory extra-endpoint labels. This is a complete analytic conditional exclusion, extending the count to16 of18 types.

Section6 now excludes the last two types C3+2P2,z2 and C3+P4,z3 by a uniform argument. Their unique perfect matching fixes any empty partition. Unequal empty/nonempty statuses force K13 or leave a size-two small label with no extras. Equal empty partitions force the same special-block/light-neighbor pattern as z4, even with positive residual slack, ending in E0=6<9. This closes all18 types of the registered3+7 form; the proof does not incorrectly reuse the two-triangle argument.

For the full terminal: m8,m9 and the other m10 light-component possibilities still need structural exclusions. The next interface is whether those cases admit a comparably rigid normal form. No theorem has been proved that every full-support core enters the excluded3+7 form or admits the excluded four-clique partition. Such a claim would be a new substantive theorem, not a consequence of the scalar37-gap budget.

Difference from existing lines: this work uses shell-component blockers, the parent target clique cap, analytic outside-edge packing, and the new special-block/light-neighbor exclusion. A's latest1de8a375 gives z3 catalogs, while this proves the z4 contradiction without selecting a heavy-graph isomorphism type or running the projection CSP. B's low-support casework is unchanged. No subagents were used.

