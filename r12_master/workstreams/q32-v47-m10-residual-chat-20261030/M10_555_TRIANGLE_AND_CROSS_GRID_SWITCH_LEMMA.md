# M10 5,5,5 triangle classification (corrected) and K4-e cross-grid constraints

Date: 2026-10-30  
Status: COMPUTATION_CERTIFIED local theorem; the K4-e, Z=4 six-column slice is closed by Section 8, while other 4+6 slices and full Q32 remain OPEN.

## 1. Exact 5,5,5 triangle classification

Let A,B,E be pairwise disjoint independent 4-sets. Each pair graph has exactly five edges: a unique perfect matching plus one off-matching edge. Relabel A,B,E so the A-B and A-E base matchings are identity; let the B-E matching be sigma in S4. Denote the extra edges by e_AB,e_AE,e_BE.

There are exactly 24*12^3=41,472 normalized inputs. For each input, check all 792 five-subsets of A union B union E.

**Correct theorem.**
- If sigma=id, all 12^3=1,728 extra-edge triples are valid.
- If sigma is a transposition, exactly 66 extra-edge triples are valid.
- If sigma is a 3-cycle, double transposition, or 4-cycle, no extra-edge triple is valid.

Thus the exact total is 1,728+6*66=2,124.

The transposition case has the following explicit classification. By simultaneous relabelling, take sigma=(0 1), fixing 2 and 3. Then:
1. If e_AB=(0,1), either e_AE=(1,0) and e_BE is any of the 12 off-sigma edges, or else e_BE=(0,0).
2. If e_AB=(1,0), either e_AE=(0,1) and e_BE is any of the 12 off-sigma edges, or else e_BE=(1,1).
3. If e_AB is any of the other ten off-diagonal edges, the only possibilities are e_AE=(0,1), e_BE=(0,0), or e_AE=(1,0), e_BE=(1,1).

This gives 23+23+20=66 configurations. The exact classifier is checked against the independence test on every one of the 41,472 inputs by verify_m10_555_triangle.py.

### Regression witness for the former incorrect theorem

Take sigma=(0,1,3,2), e_AB=(0,1), e_AE=(2,3), e_BE=(2,2). Every extra edge is off its base matching, and direct checking of all 792 five-subsets gives alpha(A union B union E)<=4. The former 1,872-count theorem incorrectly rejected this configuration because e_AB is outside the support of sigma.

The former statement “24 valid configurations for each transposition” and the former fixed-e_AB switch rule are RETRACTED. The corrected exact count is 66 per transposition.

## 2. Application to the 4+6 K4-e cell

In the 4+6 split, suppose the four-block side S is K4-e. Its unique heavy pair A,B has five edges; the other five pairs in S have four. The six-block side T has light graph K6 minus a matching of size Z-1. In the K4-e subcase, all 24 cross pairs have exactly five edges, and for Z=4 the outer heavy graph is a perfect matching.

The internal base matchings on S and T align independently. After relabelling, all small-small and all outer-outer base matchings are identity. The remaining cross data are 24 permutations p_ij and 24 off-matching extra edges e_ij.

## 3. Exact 4,5,5 switch contract (unchanged)

For a light small-side pair Q_i,Q_k and a selected outer block E, the pair Q_iQ_k is a matching and both cross pairs have five edges. Put tau=p_i^{-1}p_k. Either tau=id, or tau is a transposition and for some s in its support

    e_i=(s,p_k(s)),    e_k=(s,p_i(s)).

This is the unchanged 4,5,5 theorem. The corrected 5,5,5 theorem above must be used for the heavy AB pair; it is strictly more permissive than the former fixed-switch rule.

## 4. Corrected one-column state catalog

Normalize the selected outer block's target labels so p_C=id. Enumerate p_A,p_B,p_D in S4 and all four cross extra edges. Impose:
- the exact corrected 5,5,5 test on A,B,E, with fixed e_AB=(A_0,B_1);
- the five 4,5,5 constraints from the light small-side pairs AC, AD, BC, BD, CD;
- alpha<=4 on the five-block induced graph.

The exact catalog is:

| Quantity | Count |
|---|---:|
| All one-column states | 20,842 |
| p_A=p_B | 20,772 |
| p_A!=p_B | 70 |
| AB-relative switch (0 1) | 30 |
| Each of the other five transpositions | 8 |
| Independent-five candidates checked per state | 8,704 |

The former catalog of 20,788 states (16 switched) is superseded. It omitted 54 valid states because it used the incorrect 5,5,5 classifier. A concrete omitted five-block witness is recorded in verify_m10_555_column_states.py; it satisfies all local pair contracts and has no independent five-set in the full 20-vertex induced graph.

The 8,704 candidate family is complete: a pair graph with a perfect matching has no independent 5-set supported on two blocks (the 3+2 and 4+1 distributions are blocked by the matching). Every three-block induced graph is one of the aligned 5,4,4 case, the 4,5,5 switch case, or the corrected 5,5,5 case, all with independence number at most four. Thus any remaining independent five-set uses either 1+1+1+1+1 or 2+1+1+1 across the five blocks.

## 5. Row/column matching-value bound

In the 4-by-6 cross grid, fix one small row i. For any two outer columns j,l, their pair is either light (four edges) or heavy (five edges); the two row-to-column pairs each have five edges. The 4,5,5 or corrected 5,5,5 theorem therefore implies p_ij and p_il are equal or differ by a transposition.

Likewise, in a fixed outer column j, any two small rows have a light or heavy pair, and both cross pairs have five edges. Their matching permutations are equal or differ by a transposition.

A subset of S4 whose distinct elements are pairwise at transposition distance has size at most two: if p,q,r were three distinct elements, then q^{-1}r=(p^{-1}q)^{-1}(p^{-1}r) would be the product of two distinct transpositions, hence a 3-cycle or double transposition, not a transposition.

Therefore every row and every column of the 4-by-6 matching matrix uses at most two permutations. This does NOT imply that the entire matrix uses only two global permutations. A 2-by-2 rectangle can use four permutations. Nor does it imply that all row/column switches use the same transposition.

## 6. Remaining load-bearing interface

The next problem is to couple the corrected 20,842 one-column states; all twelve outer light-pair 4,5,5 constraints; the three outer heavy-pair corrected 5,5,5 constraints with their actual extra-edge endpoints; exact per-vertex degree equations; the two residual clique-fiber partitions and their relative placement; and global alpha(H)<=4 and omega(H)<=11.

The exact Z=4 two-aligned-column pattern-10 terminal was the initial subcase. Its scope is now subsumed by M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md, which closes the entire K4-e, Z=4 slice. The K4 small-component branch and K4-e with Z=1,2,3 remain OPEN; full-support m=10 Q32 and the root remain OPEN.


## 8. Global use in the 4+6 K4-e, Z=4 terminal

M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md uses the corrected 5,5,5 theorem to ensure that two outer-column matchings in a fixed row differ only by identity or a transposition; this forces all switches in that row to use one common transposition. The decisive A/B switch exclusion is shorter and does not need the 5,5,5 endpoint classifier: if A switches in column j, the two light triangles A,C,E_j and A,D,E_j force both C-E_j and D-E_j extra edges to end at P(k). This gives c_j(P(k))>=2, contradicting the exact cap c_j(P(k))<=1. The verifier retains the six-case normalized 5,5,5 endpoint test as an additional regression, not as a load-bearing proof step. No retracted fixed-transposition predicate is used.
