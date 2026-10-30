# EG617 r=12 — Q32 m=10 residual closure workstream

Date: 2026-10-30  
Branch: workstream/r12-q32-v47-m10-residual-final-20261030  
Write scope: r12_master/workstreams/q32-v47-m10-residual-chat-20261030/  
Base commit: 1de8a37556ba98ccbb8651f39a5192629453f0f1 (high-support root branch)

## Mission and firewall

This workstream attacks only the full-support Q32 terminal with m=10 exact-129 colors. It does not modify or replace the m=8,9 work of sibling Chat A, and it does not modify the high-support, case-II, Astra, or root workstreams.

The parent 47-core contract is:
- |H|=47, e(H)=285;
- alpha(H)<=4, delta(H)>=12;
- sum over v in H of (d_H(v)-12)=6;
- ten disjoint independent pivot blocks Q_1,...,Q_10, each of order four, with residual R of order seven;
- the pivot/residual slack variables satisfy the exact ledger recorded in the structural proof.

The Type-I exact-color source is the published-source factorization 10 isolated K5 components plus an 11-vertex gadget G_11. This workstream preserves all source outside-count placements; it does not impose the invalid assumption that all ten isolated K5s are single-outside or that an isolated triple is generically impossible.

## Verified results entering this workstream

1. The disconnected light-block graph L has exactly two components, with sizes 1+9, 2+8, 3+7, 4+6, or 5+5. Three or more components are impossible.
2. The 3+7 graph-theoretic normal form is excluded by the Astra theorem once its five upstream properties are established. This is conditional on the 3+7 split, not a universal m=10 closure.
3. The aligned z=0,1 cell has its registered K6 contradiction.
4. The m=10 high-chromatic residual cell is excluded by the incidence-cover theorem; every remaining residual satisfies clique-cover number at most four.
5. The source-correct isolated-double audit identifies an eight-vertex residual branch; its exceptional large-track-centered subcase remains open.
6. The source-correct Type-I occupancy catalog has 90 labelled aggregate factor assignments. It includes isolated-double, special-double, two-isolated-double, isolated-triple, and special-triple modes.
7. New dense-component lemma: the 4+6 side contains four aligned K4 tracks (with a sharper K4-e reduction); each side of a 5+5 split contains an aligned four-block K4/K4-e core. Their cross matching grids remain open.
8. RETRACTED: the former 5,5,5 classifier (1,872 valid) and 20,788-state one-column catalog were incorrect. Corrected exact replay gives 2,124 valid 5,5,5 configurations and 20,842 one-column states (70 switched). The six-column grid remains OPEN.
9. The low-support Q32 layers |U|=44,45,46 are closed on the case-II branch. This does not close full support |U|=47.

## New verified residual catalog

An independent labelled enumeration covered all 1,048,344 seven-vertex graphs with 3 through 10 edges. The source-correct incidence proof excludes the 252 labelled copies of C5 dot-union 2K1; after alpha, clique-cover and B_min filters, 797,072 labelled residual graphs remain.

Their 371 isomorphism representatives, 93,120 ordered four-clique-fiber maps and 34,794,144 ordered pairs (F,G) are checked in the independent replay report. This is a necessary-condition catalog, not a full 47-vertex Q32 enumeration. It does not enumerate the ten-block weighted-heavy graph, source endpoint placements, all global color edge ownership, or all compatible F/G pairs.

10. Corrected 4+6 local result: each fixed row and fixed column of the 4-by-6 matching matrix uses at most two permutations, but the entire matrix need not use only two. The old fixed-transposition endpoint propagation is not valid.

## Current status

Status: OPEN. Full-support m=10 Q32 is not closed.

The disconnected component-size catalog is complete. The 4+6 and 5+5 cells have aligned four-block core reductions. The 3+7 branch is conditionally closed. The 1+9, 2+8, 4+6, 5+5 and connected-light-graph branches remain open. The endpoint-labelled Type-I source placements, including H-TI isolated-triple, remain open.

No full-model SAT/UNSAT certificate is claimed. No root EG617(r=12) closure is claimed.


11. Z=4 two-aligned-column pattern-10 terminal: PROVED IMPOSSIBLE for the exact case p_A=P on two columns, p_A=P tau on four columns, p_B=p_C=p_D=P, with small residual fiber profile (3,2,2,0). The proof and cut/degree verifier are M10_Z4_TWO_ALIGNED_PATTERN10_EXCLUSION.md and verify_m10_z4_two_aligned_cut.py. This does not close other 4+6 patterns.
