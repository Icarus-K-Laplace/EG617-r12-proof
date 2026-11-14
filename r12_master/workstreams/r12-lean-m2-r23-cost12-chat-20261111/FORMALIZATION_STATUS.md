# Verified partial R23 classification — GATE47 remains open

Latest verified code: 2dba3b922460dabe71fc91e4949190182217db07.
Linux CI 43616747074, job 132513365166 (2026-11-15 Asia/Shanghai).
Focused build, whole lake build, exact statement inspection, all 152 transitive
axiom reports, nine fixed dependencies and source SHA256 checks PASS.
Only propext, Classical.choice and Quot.sound. Full log:
logs/linux-43616747074-full.txt. Local source hashes match Linux output.

New mathematical results:
- r23_exact_labeled_neighbor_ledger keeps the SAME shortest C5 support when
  assigning actual neighbor labels; no unrelated C5 is substituted.
- r23_exists_balanced_exterior derives K9,9 or K9,9 minus one cross edge from
  the original R23 contract. K8,10 is excluded by a 12-element independent
  neighborhood (ten exterior neighbors plus the two forced cycle neighbors).
- r23_122_type_presentation derives a map t : V -> Fin 5 from the original
  23-vertex, triangle-free, alpha<=11, exactly122-edge assumptions and proves
  G.Adj x y iff cycleGraph 5.Adj (t x) (t y).
  The reverse direction uses ACTUAL complete cross edges.

Exact 121/122 ledger was verified at 4454d72 / CI 43573005534, including
all three neighbor distributions and x=35 iff exactly one singleton.
C5 type compatibility and missing-endpoint orientations were verified at
89183d0 / CI 43570397008. Baseline mathematics remains unchanged.

NOT proved: the final 122-edge class sizes, the 121-edge singleton graph
completion, the compatible/incompatible missing-edge whole-graph cases,
Cost-6 for arbitrary independent sets, sharp R335/R336, GATE47, MainTheorem.
C5TypeFibers.lean is a local candidate for class sizes, not yet CI-verified.
No progress percentage or theorem count is used as evidence of those targets.
