# Canonical state — independent structural attack

Date: 2026-10-29
Branch: workstream/r12-astra-independent-structural-attack-20261029
Base: 433a5b39a98325f00e99650b0270d79f7753a47d
Write scope: this directory only.

## Proved in this workstream

The elementary outside-edge theorem in NEAR_TURAN_STABILITY_THEOREM.md gives b(C)>=57 for every non-target color in the four-track (12,12,12,11) contract with a target pivot star on the other14 vertices. The eleven colors need627 outside edges, but E408/core285 permits only626. This excludes that partition for all m.

Application: the registered m=10, disconnected3+7, z=0 and z=1 aligned cells are PROVED_CONDITIONAL impossible. The full statement and all equality-case arguments are included.

A separate parent audit observes omega(F)<=11 in the genuine T61 contract. It directly excludes any target K12, and hence the same aligned cells. This bound was omitted from the relaxed high-support contract.

## Critical CSP audit

The current sibling specification imposes omega(G_C)<=5 for all twelve colors. This is not the parent contract: only non-target colors inherit the bound5 from alpha(F)<=5; the target bound is11. In particular all-color K6 cuts make the aligned target K12 submodel trivially UNSAT. Such a solver outcome would not certify the intended relaxation. No solver was run here and no result is imported.

## Still open

Full-support Q32 with m=8,9 and remaining m=10 cells lacking the excluded four-clique partition. No all-m classification or complete labeled graph certificate has been obtained. Root remains OPEN / NOT_CERTIFIED. E407 and Q33 parent/support-exhaustiveness gates remain separate.

This work does not assert that a model satisfying scalar or projection constraints is a genuine coloring, and does not claim success criterion E for the entire current abstract system.
