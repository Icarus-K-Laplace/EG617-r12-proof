# R23 COMPLETE CLASSIFICATION VERIFIED — Cost-6 and GATE47 open

Verified code: 0d2985dbfe109fab301c157f687b3b38478c8bb6.
Linux CI43680628810, job132710251209, 2026-11-15.
Focused compilation, full lake build, exact statement inspection, all176
transitive axiom reports, all9 dependency pins and source/config SHA256 PASS.
Only propext, Classical.choice, Quot.sound. Local sources match CI hashes;
original LEVEL1 mathematical sources remain byte-identical.
Evidence: CI_STATUS.json, logs/linux-43680628810-full.txt.

r23_complete_classification proves the exhaustive frozen M2 classification from
card V=23, triangle-free, alpha<=11 and at least121 edges, with no extra terminal
hypothesis. Its alternatives are:
1. actual C5(10,A,1,1,B), A+B=11, 1<=A,B<=10;
2. adding exactly one formerly absent edge gives such a Case I graph, preserving
   triangle-freeness and alpha<=11;
3. actual C5(9,9,2,1,2).
All profiles specify every actual vertex fiber and an adjacency IFF for all
vertex pairs. This is a whole-graph classification, not just compatible labels.

The exact121/122 ledger, all three neighbor distributions, same-support C5
labeling, K8,10 exclusion, singleton graph completion, compatible missing-edge
completion, and all ten incompatible endpoint orientations are kernel-verified.

NOT proved: universal Cost-6; sharp R335/R336; GATE47; original MainTheorem.
The next work is frozen low M3, preserving every independent set and every legal
single-edge deletion. No diagnostic enumeration is a Lean premise.

## 2026-11-16 Cost-6 progress
Verified code 0dc1190e19fcbf02e2fd7b565ad16d92b27d98bd / Linux CI43791548801:
case_I_cost_six and exceptional_cost_four (hence exceptional_cost_six) PASS,
including exact witness counts for every independent set. All188 declarations,
156 theorems, full build, statement inspection, axiom audit and SHA256 PASS.
Only propext, Classical.choice and Quot.sound occur.
CostSixDeletion.lean and r23_cost_six are now CANDIDATE, awaiting kernel CI.
The next candidate covers every single-edge deletion structurally, then applies
the already verified exhaustive R23 classification. GATE47 remains open.
