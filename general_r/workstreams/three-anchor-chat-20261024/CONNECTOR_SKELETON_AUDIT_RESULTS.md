# Connector-skeleton audit results

## Source and scope

Script: CONNECTOR_SKELETON_AUDIT.py  
GitHub blob SHA-1: 15159c50b07bfa8d7849dc8e6bc966e52d1e1383

The script was executed in Python from the committed source. It enumerates every labelled connector adjacency graph for c=3 (2^3=8 graphs) and c=4 (2^6=64 graphs), every connector-excess allocation with total at most six, and the permitted focus/focus-owner assignments for r=12,13,14,15. For each nonfocused connector it computes the minimum local rectangle charge compatible with its degree inequality. An adjacent same-group pair is relaxed using max(R1,R2), not R1+R2.

The search is intentionally a local relaxation, not a graph generator. It does not impose every vertex-level edge constraint, all independent-4 constraints, or all K_r-avoidance constraints on a complete graph H. Its survivors are therefore relaxed arithmetic skeletons, not counterexamples.

## Exact output

```text
c=2 connector-only skeletons (edge/no-edge x excess allocations): 56
r=12: relaxed low-budget skeletons {'c3': 44, 'c4_002': 2, 'c4_011': 2}; c3-focus={1: 22, 2: 22}; c4_002-focus-count={2: 2}; c4_011-slot-count={2: 2}
r=13: relaxed low-budget skeletons {'c3': 4, 'c4_002': 0, 'c4_011': 0}; c3-focus={1: 2, 2: 2}; c4_002-focus-count={}; c4_011-slot-count={}
r=14: relaxed low-budget skeletons {'c3': 0, 'c4_002': 0, 'c4_011': 0}; c3-focus={}; c4_002-focus-count={}; c4_011-slot-count={}
r=15: relaxed low-budget skeletons {'c3': 0, 'c4_002': 0, 'c4_011': 0}; c3-focus={}; c4_002-focus-count={}; c4_011-slot-count={}
PASS: every labelled connector adjacency graph and allowed focus-owner assignment was enumerated for c=3 and c=4.
LIMITATION: counts are local degree/rectangle relaxations, not full graphs H and not counterexamples.
```

## Interpretation

- The c=2 connector-only enumeration covers both possible p-q edges and all 28 nonnegative pairs (k_p,k_q) with k_p+k_q<=6. It is only a bookkeeping check; the analytic E_i argument is the actual c=2 proof.
- At r=12, the c=4 relaxed survivors are exactly the two focus-group choices for the two-focus overlap branch. Their local rectangles must be the (1,8)/(8,1) equality configurations; the analytic saturation contradictions in PUBLICATION_VERSION.md eliminate them.
- At r=13, the four c=3 survivors are connector-graph variants of the same local signature (k,gamma,a,b,n2)=(6,0,2,2,0), eliminated by the triple-connector degree argument.
- No relaxed c=4 skeleton remains at r=13,14,15. No c=3 relaxed skeleton remains at r=14,15.
- The 44 c=3 r=12 relaxations reduce to the 19 local degree/rectangle signatures listed in ARITHMETIC_AUDIT_RESULTS.md; each is removed by the analytic saturated-vertex or one-neighbor argument.

## Explicit non-claim

This is not an exhaustive search over graphs H and does not establish nonexistence by computation. The proof remains analytic. No full graph-level SAT/ILP search was run.
