# Retraction and correction: M10 5,5,5 switch classification

Date: 2026-10-30  
Scope: this workstream only; no sibling branch is modified.

## 1. Error found

The former 5,5,5 triangle file claimed that each transposition sigma had 24 valid configurations, with a fixed relation between e_AB and e_AE. Its verifier encoded that predicate and asserted a total of 1,872 valid inputs.

Independent exhaustive replay of the exact 41,472 normalized inputs and all 792 five-subsets per input gives 2,124 valid configurations:
- identity: 1,728;
- each of six transpositions: 66;
- all other permutations: zero.

The former predicate rejects the explicit valid input

    sigma=(0,1,3,2), e_AB=(0,1), e_AE=(2,3), e_BE=(2,2).

All three extra edges are off their base matchings, and the induced 12-vertex graph has alpha<=4.

## 2. Downstream correction

The old one-column verifier restricted p_B to p_A or p_A o (0 1), and in the switched case fixed e_A from the former theorem. This omitted 54 valid one-column states.

The corrected exact one-column enumeration has 20,842 states:
- 20,772 with p_A=p_B;
- 70 with p_A!=p_B;
- the 70 switches comprise 30 with relative transposition (0 1) and 8 for each other transposition.

The explicit five-block witness in verify_m10_555_column_states.py passes every small-side pair constraint and all 8,704 independent-five candidates; a separate direct check finds no independent five-set among all 15,504 five-subsets of its 20 vertices.

## 3. Claims that must not be imported

Until separately reproved using the corrected 5,5,5 classification, do not use:
- “the AB extra edge determines a unique transposition across all columns”;
- “all nontrivial AB switches have one fixed endpoint pattern”;
- the former 20,788-state one-column catalog;
- any six-column endpoint propagation that depends on those claims;
- any Z=4 two-aligned-column terminal classification derived from the uncommitted chat-only endpoint rules.

The robust surviving consequence is only the row/column matching-value bound: each fixed row and each fixed column uses at most two matching permutations, because every pairwise relative permutation is identity or a transposition. This does not bound the whole 4-by-6 matrix to two global permutations.

## 4. Status

The 5,5,5 theorem is now corrected and its finite classifier is exhaustively checked. The one-column catalog is corrected and replayable. The six-column 4+6 K4-e grid remains OPEN. Full-support m=10 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
