# Q32 full-support m=8,9 — canonical state

**Status: OPEN / NOT_CERTIFIED.** The previous analytic closure relied on unavailable omega(H)<=5, omega(C)<=5 and universal Type-I source assumptions; it is retracted in AUDIT_RETRACTION_BALANCED_PREMISES.md.

## Scope lock

This workstream handles only the E408/Q32 full-support terminal
`|H|=47, e(H)=285, |U|=47, m in {8,9}`.
It does not work on v=44,45,46 or m=10.

## Git isolation

- Repository: `Icarus-K-Laplace/EG617-r12-proof`
- Branch: `workstream/r12-q32-v47-m89-final-20261030`
- Branch base: high-support branch commit `1de8a37556ba98ccbb8651f39a5192629453f0f1`
- Pre-canonical-update audit HEAD: `ef7bdd09c8bdd1892e586b92a8991e8cf74c5953` (the following canonical/receipt commits advance the branch)
- Sole write directory: `r12_master/workstreams/q32-v47-m89-final-chat-20261030/`
- The sibling branches and their directories were not modified.

## Canonical color vectors

- m=8: target 408; eight exact colors 129 each; three nonexact colors 130 each.
- m=9: target 408; nine exact colors 129 each; nonexact colors 130 and 131.
- Both vectors sum to `C(61,2)=1830`.

## Verified advances

1. **PROVED_CONDITIONAL** — the existing full-support source-labelled CSP has the correct twelve-factor Type-I source mode, including all legal placements of the double/triple outside factor(s); it does not force the surplus factor(s) into a special factor or force the ten isolated factors to be single-outside.
2. **PROVED_CONDITIONAL** — every exact color supplies at least ten disjoint single-outside K4 witnesses. Cross-color pairwise linearity follows from unique edge ownership and is also checked by the copied independent verifier.
3. **PROVED_CONDITIONAL** — every pair of disjoint pivot K4 blocks has a target-color perfect matching.
4. **PROVED_CONDITIONAL** — light-pair matching composition: two unique perfect matchings through a common pivot block force the composed matching in the third pair.
5. **PROVED_CONDITIONAL** — exact per-pivot-block six-unit degree ledger: `X_i+Y_i=5+epsilon_i`.
6. **COMPUTATION_CERTIFIED** — the K4,4 minimum-edge table `mu_4(t)` was exhaustively checked over all 65,536 bipartite edge sets; 2,304 local composition cases were replayed.
7. The m=8 and m=9 scalar pivot-slack frontiers were independently enumerated: 79 and 61 states respectively; the corrected z ranges are 0..12 and 0..9.
8. **PROVED_CONDITIONAL** — exact source-core accounting (e_C(H)=B_C+G_C^H) and parameter-dependent gap bounds for x in O / two-double / triple placements.
9. **PROVED_CONDITIONAL structural result, no closure.** Every non-target color in the 69/70 layer has an 11K4+K3 near-Turán partition under the registered second-Turán input. This does not exclude the layer: the tight-part consequence is a K7 in H, and omega(H)<=11 allows it. The old CSP removed these variables only in its augmented K6-free submodel.
10. **WITHDRAWN / repaired** — the first unconditional lazy matching-composition cuts were overconstraints; they have been replaced by source- and pivot-selection-guarded implications.
11. **PROVED_CONDITIONAL — historical intermediate result.** Simultaneous 69/70 partitions are pairwise orthogonal. The earlier solver/verifier revisions encoded this condition; the current terminal no longer needs it.
12. **PROVED_CONDITIONAL** — every double-outside source factor's H-interior K3 lies in one near-Turan part; the solver and independent verifier encode/check this.
13. **PROVED_CONDITIONAL — historical low-layer source localization.** The exact 69/70 source placement constraints remain valid as an intermediate result but are not used by the final Type-I obstruction.
14. **PROVED_CONDITIONAL structural result.** Given an 11K4+K3 partition, Hall matching gives a 253-edge skeleton and 32-edge residual. This is a conditional graph structure, not an exclusion.


## Scope firewall

The six common-P factors, pair-projection normal form, and residual-signature injectivity in the sibling `V47_Z01_*` documents depend on the aligned 3+7 track normal form for a special m=10 cell. They are **not imported** as m=8/9 constraints. The correct m=8/9 analogue added here is the global pivot-pair perfect-matching system with lazy composition and multi-projection cuts.

## Dependency reconciliation

The latest root branch HEAD is `b0459807acd4b7e386148056ddf77d7998918893`. Its global canonical/dependency summaries contain an older `L_9=6` line. The read-only Case-II canonical/dependency audit explicitly supersedes that value: the correct m=9 nonexact degree-floor sum is `L_9=4+3=7`. This solver uses 4 for 130-edge and 3 for 131-edge colors. No sibling or root directory was modified.

## Current limitation and promotion boundary

The m=8/9 full-support Q32 terminal remains OPEN. The Type-I source partition obstruction forces a K6/K7 only under an unproved source mode; such cliques are permitted by omega(H)<=11. The full verifier is Type-I-only, and the solver adds K6-free constraints not present in EG617. Neither artifact certifies the original Q32 problem. No full SMT run or UNSAT certificate exists.

15. **PROVED_CONDITIONAL** — for the 32-edge residual F of any selected 253-edge matching skeleton, if q of the 36 M-degree-11 vertices carry positive excess and t is the number of isolated K2 components, then F has 36-q leaves, a core of 11+q≤17 vertices, and exactly q+t-4 core edges; q+t≥4.

16. **PROVED_CONDITIONAL lemma; global floor WITHDRAWN.** Any 11K4+K3 partition of H with e(H)=285, delta(H)>=12, alpha(H)<=4, and the extra omega(H)<=5 cap forces an independent 5-set or a K7. The K7 contradiction and e_C(H)>=71 floor require omega(H)<=5. Since EG617 only gives omega(H)<=11 on the Q32 core, the 71-edge floor and 37-unit slack claim are not valid for the original problem.

17. **RETRACTED AS EG617 CLOSURE — Type-I partition route.** Conditional on Type-I source factors, every exact color induces one of three H-independent-part partitions. The Hall/tight-part lemma forces an independent 5-set or a clique of size at least six. The latter is allowed because omega(H)<=11. Moreover balancedness only gives omega(C)<=12; it does not ensure the non-12-partite/size-six exclusion needed for Type I. Therefore this lemma closes neither m=8 nor m=9.

18. **VERIFIER SCOPE CORRECTED.** The verifier format is Type-I-only. Its default no longer rejects monochromatic K6; the optional --check-omega mode tests an augmented K6-free problem only. The matching helper's K6/K7 witness is allowed under EG617. The full verifier was not executed.

19. **RETRACTED — parent all-support/m-independent promotion.** The obstruction's missing clique/source hypotheses are not supplied for any support row. It excludes no Q32 row under the actual EG617 contract.

20. **CRITICAL AUDIT — missing clique/source hypotheses.** EG617 balancedness gives alpha(C),omega(C)<=12, and the Q32 47-core has omega(H)<=11. The previous Type-I source partition closure assumed omega(C)<=5 and omega(H)<=5, neither of which is available. The exact-129 source may also be 12-partite; C0=5K6+3K5+4K4 is a 61-vertex, 129-edge local example with alpha=12, omega=6 and 12-partite complement. See AUDIT_RETRACTION_BALANCED_PREMISES.md. Q32 m=8,9 is OPEN / NOT_CERTIFIED.
