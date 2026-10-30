# Q32 full-support m=8,9 — canonical state

**Status: ANALYTICALLY EXCLUDED (PROVED_CONDITIONAL).** Both full-support m=8 and m=9 Q32 branches are impossible under the registered Type-I factorization and frozen H-core contract. No SMT UNSAT result is claimed.

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
9. **PROVED_CONDITIONAL — historical intermediate result, superseded by item 17.** Every non-target color in the 69/70 layer has an 11K4+K3 near-Turán partition. The old CSP encoded this conditional structure; those variables have been removed from the current solver after the stronger Type-I partition obstruction.
10. **WITHDRAWN / repaired** — the first unconditional lazy matching-composition cuts were overconstraints; they have been replaced by source- and pivot-selection-guarded implications.
11. **PROVED_CONDITIONAL — historical intermediate result.** Simultaneous 69/70 partitions are pairwise orthogonal. The earlier solver/verifier revisions encoded this condition; the current terminal no longer needs it.
12. **PROVED_CONDITIONAL** — every double-outside source factor's H-interior K3 lies in one near-Turan part; the solver and independent verifier encode/check this.
13. **PROVED_CONDITIONAL — historical low-layer source localization.** The exact 69/70 source placement constraints remain valid as an intermediate result but are not used by the final Type-I obstruction.
14. **PROVED_CONDITIONAL — historical 69/70 matching skeleton.** The 253-edge/32-edge residual decomposition is superseded by the unified 250/253-edge Type-I partition skeleton in item 17 and V47_TYPEI_PARTITION_OBSTRUCTION.md.


## Scope firewall

The six common-P factors, pair-projection normal form, and residual-signature injectivity in the sibling `V47_Z01_*` documents depend on the aligned 3+7 track normal form for a special m=10 cell. They are **not imported** as m=8/9 constraints. The correct m=8/9 analogue added here is the global pivot-pair perfect-matching system with lazy composition and multi-projection cuts.

## Dependency reconciliation

The latest root branch HEAD is `b0459807acd4b7e386148056ddf77d7998918893`. Its global canonical/dependency summaries contain an older `L_9=6` line. The read-only Case-II canonical/dependency audit explicitly supersedes that value: the correct m=9 nonexact degree-floor sum is `L_9=4+3=7`. This solver uses 4 for 130-edge and 3 for 131-edge colors. No sibling or root directory was modified.

## Current limitation and promotion boundary

The m=8/9 full-support Q32 terminal is no longer open: the Type-I source partition obstruction proves that every exact-129 color would induce one of three impossible H-partitions. The independent verifier now replays the Hall/tight-part dichotomy.

The full SMT model was not executed; no solver UNSAT result, proof log, or UNSAT_CERTIFICATE is claimed. This is an analytic closure, not a computational closure. Parent promotion still requires the root workstream to audit the imported Type-I factorization and the H-core contract as dependencies. This branch does not close E408 globally, Q33, E407, or the original Erdős r=12 theorem.

15. **PROVED_CONDITIONAL** — for the 32-edge residual F of any selected 253-edge matching skeleton, if q of the 36 M-degree-11 vertices carry positive excess and t is the number of isolated K2 components, then F has 36-q leaves, a core of 11+q≤17 vertices, and exactly q+t-4 core edges; q+t≥4.

16. **PROVED** — any 11K4+K3 partition of H with \(e(H)=285\), \(\delta(H)\ge12\), \(\alpha(H)\le4\), and \(\omega(H)\le5\) forces an independent 5-set or a K7. Therefore all eleven non-target colors satisfy \(e_C(H)\ge71\), and the 37-unit gap ledger becomes \(\sum_c(e_C(H)-71)=15\). This is independent of m=8/9 and Type-I special-factor placement.

17. **PROVED_CONDITIONAL — Q32 m=8,9 analytic exclusion.** Every exact-129 Type-I color induces one of three H-independent-part partitions: \(11K_4+K_3\), \(10K_4+2K_3+K_1\), or \(11K_4+K_2+K_1\). A unified Hall-matching/tight-part lemma excludes all three: it forces an independent 5-set or a K6 in H. Since m=8 and m=9 require exact Type-I colors, both full-support v47 branches are analytically impossible, conditional on the published Kang–Pikhurko equality classification, the balanced-coloring alpha<=12 premise, global monochromatic-K6 exclusion, and the frozen H-core contract. No full SMT run is claimed or needed. Parent root promotion remains a separate dependency-audit task.

18. **VERIFIER IMPLEMENTED / SYNTHETIC LOGIC REPLAYED** — the independent verifier reconstructs each exact color's H-interior partition, builds the 250/253-edge Hall matching skeleton, and returns an independent 5-set or a clique of size at least six. A standalone Python replay of the helper on the committed synthetic 285-edge fixture returned clique witnesses of sizes 7, 6, and 7 for the three partition shapes. The committed full verifier self-test includes these cases; the full verifier file itself was not executed in this environment.

19. **PARENT-LEVEL COROLLARY — all Q32 supports and m values.** The Type-I partition obstruction uses neither the selected-witness union U nor its support size v nor m beyond m>=1. The parent E408/Q32 outer ledger has m in {8,9,10}; if the same frozen H-core and global coloring premises are explicitly carried for every support row, the theorem excludes all v=44,45,46,47 and all m=8,9,10. This is a promotion implication recorded in ROOT_PROMOTION_NOTE.md; the parent/root branch was not modified here.
