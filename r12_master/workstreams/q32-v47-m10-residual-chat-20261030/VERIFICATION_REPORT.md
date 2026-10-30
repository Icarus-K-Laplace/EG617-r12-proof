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

## 5. RETRACTED former 4+6 local verification

The former 1,872-count 5,5,5 result and 20,788-state one-column result are invalid. The previous verifier's fixed-transposition predicate rejects valid 5,5,5 inputs. See M10_555_CLASSIFICATION_RETRACTION.md.

## 6. Corrected 4+6 local verification

An independent analysis-runtime replay exhausts all 41,472 normalized 5,5,5 configurations and confirms 2,124 valid ones: 1,728 identity and 66 for each of six transpositions. It checks all 792 five-subsets for every input and matches the corrected closed-form classifier with zero mismatches. A separate analysis-runtime enumeration gives 20,842 one-column states (20,772 A/B-aligned, 70 switched) and checks all 8,704 complete independent-five candidates in the five-block induced graph for every state. It includes an explicit state omitted by the former catalog; a separate full 20-vertex five-subset check confirms that witness has alpha<=4. The committed standard-library scripts are reproduction artifacts; no GitHub-hosted CI execution is claimed. These are local finite certifications, not a six-column grid or full Q32 certificate.

## 7. Scope

Neither replay certifies:
- any ten-block weighted-heavy graph;
- any source gadget endpoint placement;
- any global 47-vertex H realization;
- any cross-color edge-disjointness or complete 12-coloring;
- any root Q32 contradiction.

Accordingly, full-support m=10 Q32 remains OPEN / NOT_CERTIFIED.


## 8. Z=4 two-aligned pattern-10 exclusion

The analytic proof in M10_Z4_TWO_ALIGNED_PATTERN10_EXCLUSION.md excludes the exact pattern with two aligned columns and four A-only switched columns for F=(3,2,2,0). Its Z=4 degree saturation is derived from the 208 pivot-block edges, e(R)=7 and e(H)=285, giving Y=0 and exact outer degree 12. The accompanying analysis-runtime replay checks all 15 perfect matchings on six columns against all 15 choices of the aligned pair (225 cut instances), verifies cut connectedness and a heavy pair wholly inside the four nonaligned columns, and checks the outer degree-vector implication for all labelled (3,2,2,0) profiles. This is a local structural closure only; other two-aligned patterns, all remaining 4+6 cases, and full m=10 remain OPEN.
