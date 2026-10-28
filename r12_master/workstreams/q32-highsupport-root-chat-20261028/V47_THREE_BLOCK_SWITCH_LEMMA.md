# E408 Q32 — exact three-block switch lemma (4,5,5 edge counts)

Date: 2026-10-28  
Status: **FINITE-EXHAUSTIVE LOCAL THEOREM; no global Q32 closure claimed.**

## 1. Statement

Let A,B,C be pairwise disjoint independent 4-sets in a graph G with `alpha(G)<=4`. Assume
- `e_G(A,B)=4`;
- `e_G(A,C)=5`;
- `e_G(B,C)=5`.

Each bipartite pair graph has vertex-cover number at least four, since otherwise the union of the two independent 4-sets would contain an independent set of size at least five. By König, each pair graph has a perfect matching. The 4-edge pair A-B is exactly a matching; each 5-edge pair is a perfect matching plus one extra edge, and that perfect matching is unique.

Relabel the four vertices in A and B along their A-B matching, and relabel C along the A-C matching. The A-B and A-C matchings are now identity maps, while the B-C matching is a permutation `sigma in S4`.

**Theorem.** The condition `alpha(G[A union B union C])<=4` holds exactly in the following cases:

1. `sigma=id`: both extra edges may be any nonmatching edge of their respective pair graph (12 choices each).
2. `sigma=(ab)` is a transposition: choose `s in {a,b}`; the two extra edges must be
   - `A_s C_{sigma(s)}` in A-C, and
   - `B_s C_s` in B-C.
   There are exactly two valid extra-edge pairs for each transposition.
3. If `sigma` is a 3-cycle, a double transposition, or a 4-cycle, no extra-edge pair gives independence number at most four.

Thus the base matchings of the two 5-edge pairs either agree, or differ by a single transposition whose two extra edges form the corresponding switch. In the mismatch case the two extra edges share the same A/B track label `s` and exchange the two C labels.

## 2. Why this is relevant to Q32

In the disconnected m=10 light-block cases 2+8 and 3+7, the small light component has respectively two or three blocks. Every cross pair from that component to a block outside it is heavy with exactly five edges. Therefore:
- for a 2-block light component, each outside block's two incident base matchings are either aligned or make exactly the switch above;
- for a 3-block light triangle, each outside block's three base matchings are pairwise either aligned or differ by a switch. Consequently at most two distinct matching permutations can occur among the three incident pairs; if one differs, its transposition and extra-edge endpoints are synchronized against both aligned pairs.

This removes arbitrary matching freedom from the 2+8 and 3+7 cells. It is a local constraint only; it does not by itself eliminate either global cell.

## 3. Exhaustive certificate

The accompanying `verify_three_block_switch_lemma.py` normalizes A-B and A-C to identity, enumerates all 24 permutations `sigma`, all 12 nonmatching extra edges in A-C, and all 12 nonmatching extra edges in B-C. For each of the 3,456 configurations it computes the exact independence number of the 12-vertex graph by subset enumeration.

Expected verified counts:
- identity: 144 valid extra-edge pairs;
- six transpositions: 2 valid pairs each, 12 total;
- all 3-cycles, double transpositions and 4-cycles: 0;
- total normalized valid configurations: 156.

The script verifies the finite local classification. It does not check the global 47-core graph, the source Type-I premise, or root closure.
