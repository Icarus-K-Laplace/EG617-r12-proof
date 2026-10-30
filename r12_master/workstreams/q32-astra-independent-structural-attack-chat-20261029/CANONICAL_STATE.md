# Canonical state — independent structural attack

Date: 2026-10-30
Branch: workstream/r12-astra-independent-structural-attack-20261029
Base: 433a5b39a98325f00e99650b0270d79f7753a47d
Write scope: this directory only.

Latest source refresh: high-support1de8a37556ba98ccbb8651f39a5192629453f0f1 adds z3 residual and weighted-heavy-graph catalogs, without closing those cells. The preceding541653af independently closes the same aligned z0/1 cells. Our broader nonempty-fiber theorem, sharp57-edge theorem, and new z4 empty-fiber closure are separate contributions; no priority claim is made for the shared K6 argument. Proof source base remains433a5b39.

## Proved in this workstream

The elementary outside-edge theorem in NEAR_TURAN_STABILITY_THEOREM.md gives b(C)>=57 for every non-target color in the four-track (12,12,12,11) contract with a target pivot star on the other14 vertices. The eleven colors need627 outside edges, but E408/core285 permits only626. This excludes that partition for all m.

Application: the registered m=10, disconnected3+7, z=0 and z=1 aligned cells are PROVED_CONDITIONAL impossible. The full statement and all equality-case arguments are included.

A separate parent audit observes omega(F)<=11 in the genuine T61 contract. It directly excludes any target K12, and hence the same aligned cells. This bound was omitted from the relaxed high-support contract.

## Critical CSP audit

The current sibling specification imposes omega(G_C)<=5 for all twelve colors. This is not the parent contract: only non-target colors inherit the bound5 from alpha(F)<=5; the target bound is11. In particular all-color K6 cuts make the aligned target K12 submodel trivially UNSAT. Such a solver outcome would not certify the intended relaxation. No solver was run here and no result is imported.

## Still open

COLORED_PACKING_OBSTRUCTION.md excludes the3+7 cell whenever both residual fiber partitions have four nonempty classes. Section4 excludes C3+C4 at z4 by E0=6<9. New Section5 excludes2C3+P1 at z3: two diversion classes must each contain two blocks, their cross-heavy edges exhaust their budgets, and their common light neighbors would need contradictory extra endpoints. Both exclusions cover every empty-fiber status. Of18 registered residual types,16 are now excluded. Only C3+2P2 (z2) and C3+P4 (z3) remain, each requiring an empty fiber in at least one map. These results are conditional on the named local3+7 normal form and genuine parent clique cap. Four independent finite verification scripts accompany the proofs; no full Q32 solver claim is made.

Full-support Q32 with m=8,9 and remaining m=10 cells lacking the excluded four-clique partition. No all-m classification or complete labeled graph certificate has been obtained. Root remains OPEN / NOT_CERTIFIED. E407 and Q33 parent/support-exhaustiveness gates remain separate.

This work does not assert that a model satisfying scalar or projection constraints is a genuine coloring, and does not claim success criterion E for the entire current abstract system.

