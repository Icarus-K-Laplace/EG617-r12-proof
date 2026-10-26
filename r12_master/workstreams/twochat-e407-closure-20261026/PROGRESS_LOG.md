# Progress log — E407 Q32 two-chat closure workstream

## 2026-10-26 — Round 1: rebuild actual frontier and unify the labelled high-k witness floor

### Repository isolation
Created branch workstream/r12-twochat-e407-closure-20261026 from main (3f42fcce5761ca2372140618adda56f95fcbe253). All writes in this workstream are restricted to r12_master/workstreams/twochat-e407-closure-20261026/. Source branches are read-only.

### Source audit
Read the actual latest heads:
- E407 terminal 79c1086efca893fad8933210a92a432457232410;
- unified witness capacity faa8183c150dd78b000d0957fa8a63cebd52e146;
- emergency sprint f4c3b06891d29238d4f9cca2588f442004b6dc97;
- ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40;
- main 3f42fcce5761ca2372140618adda56f95fcbe253.

Re-read E407 canonical/progress state, FIVE_TEMPLATE_COMPATIBILITY.md, all registered DELTA13/14/15/16 notes, the Round 31 two-cross-edge terminal proof, root canonical state/proof DAG, and the sibling exact-129 packing / row-transversal / witness-capacity records.

### New theorem (conditional necessary structure)
Every exact-129 color has at least six B-labelled no-S K5 components \(\{b\}\cup Q\). The V12 row-type floors force at least 6/8/6/7/5 high-k B rows in templates A/B/C/D/E. Since at most four B labels are outside the six-or-more B-labelled no-S components, each exact-129 color has at least 2/4/2/3/1 high-k no-S witnesses, respectively. A/C's selected high-k rows include k=3, so those witnesses hit all three S rows. In B/D/E, each selected high-k witness hits at least two S rows. Every selected Q hits at least three shell rows total; cross-color Q intersections are at most one, and same-B-label Q sets across colors are disjoint.

Across at least seven exact-129 colors, this gives per-template floors of 14/28/14/21/7 labelled high-k witness sets and at least 42/84/42/63/21 total shell-row-hit incidences. The proof is written in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md. It is a strict incidence reduction, not a contradiction and not a template closure.

### Exact low-delta frontier
The integer ledger was rebuilt from \(\delta+\epsilon_U\le16\), \(\epsilon_U+2\delta\ge9\), \(0\le\epsilon_U\le4\), and \(\delta\ge3\). The full feasible table is in LOW_DELTA_TERMINAL_TABLE.md. The main unresolved low-delta rows are \(\delta=13,\epsilon_U=0\), \(\delta=13,\epsilon_U=2\) with the one-cross-edge (4,4,5,5) W profile under four-partite \(L_U\), all non-four-partite \(\delta=13\) cases, and every \(\delta\le12\) case.

### Proof dependency audit
The exact-129 factorization, the five-template screen, Brouwer/Kang–Pikhurko classifications, and the Didin-dependent saturated branch are recorded separately from pure graph facts. The root main proof DAG and sibling conditional R(4,49) treatment are not silently reconciled; E407 and the original bridge remain OPEN / NOT_CERTIFIED.

### Next attack
Join the 49 support-block labels to the high-k no-S component labels and shell row sets \(D_a\), without assuming these witness families coincide. Seek a contradiction common to multiple templates or a minimal surviving incidence contract. Independently audit any candidate inequality against the exact \(D_a\) row supports before using it.
