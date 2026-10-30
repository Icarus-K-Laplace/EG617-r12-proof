# Q32 full-support m=8,9 — canonical state

**Status: OPEN. No UNSAT result and no closure claim.**

## Scope lock

This workstream handles only the E408/Q32 full-support terminal
`|H|=47, e(H)=285, |U|=47, m in {8,9}`.
It does not work on v=44,45,46 or m=10.

## Git isolation

- Repository: `Icarus-K-Laplace/EG617-r12-proof`
- Branch: `workstream/r12-q32-v47-m89-final-20261030`
- Branch base: high-support branch commit `1de8a37556ba98ccbb8651f39a5192629453f0f1`
- Audited workstream HEAD at report time: `c0a2ce1ca2c4890e9374efd590aad8ba878e26de`
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
7. The m=8 and m=9 scalar pivot-slack frontiers were independently enumerated: 79 and 61 states respectively.

## Scope firewall

The six common-P factors, pair-projection normal form, and residual-signature injectivity in the sibling `V47_Z01_*` documents depend on the aligned 3+7 track normal form for a special m=10 cell. They are **not imported** as m=8/9 constraints. The correct m=8/9 analogue added here is the global pivot-pair perfect-matching system with lazy composition and multi-projection cuts.

## Current limitation

**OPEN** — the strengthened full 61-point CSP has not been executed to SAT/UNSAT in this environment. Python's runtime has no `z3-solver` package. The local arithmetic and finite matching checks pass, but they do not certify the full graph-coloring problem.

No `UNSAT_CERTIFICATE.md` is issued. A future UNSAT result must include the SMT input, solver version, proof log, independent replay, and a second implementation.
