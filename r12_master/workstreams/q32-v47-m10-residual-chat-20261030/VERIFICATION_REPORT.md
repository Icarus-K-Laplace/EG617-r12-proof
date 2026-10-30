# M10 residual relaxation — verification report

Date: 2026-10-30  
Verifier: verify_m10_residual_catalog.py  
Dependencies: Python standard library only; no SAT/SMT solver.

## 1. Executed check

The verifier was executed successfully against M10_RESIDUAL_GRAPH_CATALOG.csv. It:
- decodes each graph6 representative;
- checks its edge count and Z value;
- recomputes alpha(R), clique-cover number, and B_min(R);
- enumerates all 4^7 ordered maps R->[4] and checks that every fiber is a clique;
- computes automorphism counts and canonical codes over all 7! vertex permutations;
- checks that the 371 representatives are pairwise non-isomorphic;
- independently enumerates every labelled seven-vertex graph with 3 through 10 edges;
- checks that the orbit-stabilizer sum equals the labelled survivor count.

The replay completed without assertion failure.

## 2. Exact counts

| Stage | Count |
|---|---:|
| All labelled graphs with 3..10 edges | 1,048,344 |
| alpha(R)<=4 | 1,014,289 |
| alpha(R)<=4 and clique-cover(R)<=4 | 1,014,037 |
| Further rejected by B_min<=14-2Z | 216,965 |
| Final labelled residual graphs | 797,072 |
| Non-isomorphic graph6 representatives | 371 |
| Orbit-stabilizer sum | 797,072 |
| Ordered four-fiber maps on representatives | 93,120 |
| Ordered pairs (F,G) on representatives | 34,794,144 |

Per-Z counts and component profiles are in M10_RESIDUAL_CLASSIFICATION.md. The CSV contains all 371 graph6 representatives and the exact B_min and fiber-map count for each one.

## 3. Reproduction

From this directory:

    python verify_m10_residual_catalog.py
    python verify_m10_residual_catalog.py --dump-fibers fibers.jsonl
    python verify_m10_residual_catalog.py --dump-labelled-graphs labelled_graphs.csv

The first command performs the complete replay. The second writes all 93,120 ordered fiber maps on canonical representatives. The third writes all 797,072 labelled feasible residual graph masks. These generated dumps are intentionally not checked in because they are reproducible from the compact catalog and verifier.

## 4. Independent-source status

The Astra branch's verification_log.txt records PASS for its residual path/cycle catalog and local structural replays. Those branch-local programs were read but not rerun in this Python execution. The full vertex-labelled Q32 CSP in the high-support branch is explicitly formulation-only; no full m=10 SAT/UNSAT run or independently replayed proof certificate is registered.

## 5. Scope

This verifier certifies only the stated seven-vertex necessary-condition relaxation and its clique-fiber assignment counts. It does not certify:
- any ten-block weighted-heavy graph;
- any source K5 endpoint placement;
- any global 47-vertex H realization;
- any cross-color edge-disjointness or complete 12-coloring;
- any root Q32 contradiction.

Accordingly, the m=10 Q32 root terminal remains OPEN / NOT_CERTIFIED.
