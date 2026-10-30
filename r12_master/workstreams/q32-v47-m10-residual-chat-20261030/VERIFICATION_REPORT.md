# M10 residual relaxation — verification report

Date: 2026-10-30  
Status: Independent replay PASS for the residual catalog; full Q32 remains NOT_CERTIFIED.

## 1. Independent labelled replay

An independent Python implementation enumerated every labelled seven-vertex graph with 3 through 10 edges and applied:
1. alpha(R)<=4;
2. the globally proved clique-cover cap from M10_RESIDUAL_CLASSIFICATION.md, Section 2;
3. B_min(R)<=14-2Z.

The replay completed with no assertion failures. Exact counts:

| Stage | Count |
|---|---:|
| All labelled graphs with 3..10 edges | 1,048,344 |
| alpha(R)<=4 | 1,014,289 |
| alpha(R)<=4 and clique-cover(R)<=4 | 1,014,037 |
| Further rejected by B_min budget | 216,965 |
| Final labelled residual graphs | 797,072 |

The clique-cover filter removes exactly 252 labelled graphs, all isomorphic to C5 dot-union 2K1 (graph6 canonical representative FLo??, automorphism group order 20, orbit size 252). These are excluded analytically by the ten-block incidence argument, not by B_min.

## 2. Independent graph6/fiber replay

All 371 rows of M10_RESIDUAL_GRAPH_CATALOG.csv were decoded and checked independently:
- correct edge count e(R)=3+Z;
- exact B_min value;
- alpha(R)<=4;
- clique-cover-number(R)<=4;
- residual-incidence budget;
- all four-clique-fiber assignments by direct enumeration of 4^7 maps;
- pairwise non-isomorphism by canonicalizing all 7! vertex permutations;
- orbit-stabilizer sum equals 797,072.

No bad rows or duplicate isomorphism classes were found.

| Check | Result |
|---|---:|
| Non-isomorphic representatives | 371 |
| Orbit-stabilizer sum | 797,072 |
| Ordered four-clique-fiber maps | 93,120 |
| Ordered (F,G) map pairs before compatibility | 34,794,144 |
| Connected representatives | 260 |
| Disconnected representatives | 111 |

Per-Z type and fiber counts are recorded in M10_RESIDUAL_CLASSIFICATION.md.

## 3. Reproduction artifact

verify_m10_residual_catalog.py is committed as a standard-library-only independent verifier. It checks the compact graph6 catalog and can emit all fiber maps or all labelled graph masks.

The counts above were independently replayed in the analysis runtime using a separate implementation. The committed script was not executed on a GitHub-hosted shell in this session; do not describe that as a remote CI run.

## 4. Source occupancy replay

verify_m10_source_occupancy.py independently enumerates the 90 labelled aggregate factor-occupancy choices:
- 12 choices for x_C in O;
- 66 choices for x_C in H, two-double;
- 12 choices for x_C in H, triple.

It checks G_11 H-vertex counts, K5-interior H-edge counts, and source parameter-to-gap lower bounds. This is aggregate source arithmetic, not an endpoint-labelled source CSP.

## 5. New 4+6 K4-e local verification

The normalized 5,5,5 triangle verifier exhausts all 41,472 configurations and confirms exactly 1,872 valid ones: 1,728 with identity matching holonomy and 144 with transposition holonomy. The one-column K4-e verifier enumerates 20,788 switch-compatible states (20,772 A/B-aligned and 16 switched) and checks all 8,704 possible independent-five candidates in the five-block induced graph for every state; no independent five-set is found. The candidate family is complete because pair and three-block local theorems exclude any independent five-set supported on at most three blocks. The exact scripts are verify_m10_555_triangle.py and verify_m10_555_column_states.py. These are local finite certifications, not a six-column grid or full Q32 certificate.

## 6. Scope

Neither replay certifies:
- any ten-block weighted-heavy graph;
- any source gadget endpoint placement;
- any global 47-vertex H realization;
- any cross-color edge-disjointness or complete 12-coloring;
- any root Q32 contradiction.

Accordingly, full-support m=10 Q32 remains OPEN / NOT_CERTIFIED.
