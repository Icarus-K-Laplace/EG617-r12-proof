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
