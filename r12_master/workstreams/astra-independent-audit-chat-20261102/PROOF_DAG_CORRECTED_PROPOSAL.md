# Corrected proof-DAG proposal

This file is an audit proposal only. It is not a replacement for the frozen Astra integration DAG.

The proposed graph adds two explicit theorem nodes already present as separate entries in `GLOBAL_THEOREM_LEDGER.md`:

- `GATE47`: the 47-vertex low-edge minimum-degree gate.
- `D48`: the 48-vertex minimum-degree-12 theorem.

It adds the corresponding load-bearing edges:
- `R447_FLOOR287 -> GATE47`;
- `R448_FLOOR310 -> D48`;
- `H12_EMPTY -> D48`.

The two new nodes depend on `LOWER_ORDER`. The existing graph's other nodes and edges are preserved. A local DFS over this proposal found 27 nodes, all parent references resolved, and no directed cycle.

This only repairs the specific ledger/DAG omissions identified in `DAG_COMPLETENESS_AUDIT.md`. It is not a full semantic dependency checker; the theorem statements and exact source mapping still require human review.


## Additional dependency made explicit

The audit proposal also now maps `Q20_CLASSIFICATION` to `LOWER_ORDER` (and `TURAN`). This is required because the q=20 shell proof uses the M1 theorem (R(2,24)=\varnothing) to establish the pair-row inequality (t_a+t_b\ge12), as well as the induced density cap. The prior proposal had `Q20_CLASSIFICATION` depending only on `TURAN`, which did not expose that lower-order input. The revised JSON corrects this.


## Additional missing shell-matching dependency

A further source-to-DAG crosswalk found that the frontend recurrence's (h=13) matching lower bound is proved in COVER Section4, and the (h=14) special matching bound is proved in the same frontend section. The recurrence takes
[
k=\max\!\left(\left\lceil\frac{h-10}{2}\right\rceil,
1+[h\ge12]+[h\ge13]\right),
]
so it uses the (h=13,14) cases to force a 3-matching. COVER's q≥29 argument also uses the (h=13) 3-matching lemma, while the q20 shell theorem uses the (h=12) two-matching case.

The corrected proposal therefore introduces a packaged elementary node `SHELL_MATCHING_BOUNDS`, covering the h=12,13,14 matching floors and the general unmatched-vertex bound. Its only mathematical input is the shell density cap (and the fixed alpha/omega shell contract); the bipartite matching-cover theorem is proved directly in the frontend text, not imported as an external black box. Edges are added from:
- `Q20_CLASSIFICATION` to `SHELL_MATCHING_BOUNDS`;
- `COVER_Q29_GENERAL` to `SHELL_MATCHING_BOUNDS`;
- `RECURRENCE` to `SHELL_MATCHING_BOUNDS`.

The proposal now has 28 nodes. This is a dependency-documentation correction; the matching arguments themselves were re-read and no counterexample was found.
