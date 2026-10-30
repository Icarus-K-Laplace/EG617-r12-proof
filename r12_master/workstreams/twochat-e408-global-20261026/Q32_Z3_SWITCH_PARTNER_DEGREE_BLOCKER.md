# RETRACTED — Q32 z=3 switch-partner pointwise degree blocker

Date: 2026-10-30  
Status: **RETRACTED; do not use as a proof.**

## Invalid inference

The earlier version claimed that the outer vertex q=D_j is adjacent to every residual vertex r in F_j because q is adjacent to the small-block vertices A_j and B_j, while r is also adjacent to A_j and B_j.

This is invalid. Two vertices sharing one or more neighbors need not be adjacent. The local normalized 4,5,5 switch table establishes the small-block neighbor-label sets and k(q)=2; it does not establish q-r adjacency for r in F_j.

Consequently, the claimed mismatched-case inequality d_R(q)>=n_s+n_j and the direct conclusion that all F/G mismatch modes are impossible by this pointwise bound are withdrawn.

## What remains valid

The normalized local label pattern is valid:
- A-D and B-D base matchings are identity;
- C-D base matching is sigma=(s j);
- extra edges are A_sD_j, B_sD_j, C_sD_s;
- q=D_j has neighbor-label sets {s,j},{s,j},{s} and k(q)=2.

This is only a label/endpoint statement. The companion script now checks only this local pattern and explicitly makes no residual-adjacency inference.

## Correct replacement

The valid mismatch elimination is in Q32_Z3_MISMATCH_RESIDUAL_DEGREE_CLOSURE.md. It uses the five-switch/two-aligned-endpoint normal form, equality in the incidence-slack inequality, and d_R(r)+b_r=2. It rules out 2+1 splits by a K3 degree contradiction and 1+1 splits by either a K2 degree contradiction or an impossible isolated K2 component in C3+P4.

For F=G only, the earlier aligned-case switch blocker remains valid because track completeness really does give adjacency to F_j=G_j. The no-double-track z=3 branch therefore reduces to aligned profile (2,2,2,1), all outer blocks aligned.

This retraction does not change the global status: full-support Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
