# Arithmetic audit results

## Scope

Script: ARITHMETIC_AUDIT.py  
Branch: workstream/general-r-three-anchor-20261024  
GitHub blob SHA-1 of script: e36dca2def3d79ce637bf103b49438549bc2d412

The script was executed in a Python environment using the same source code committed above. It uses only the Python standard library. The checks are deliberately limited to integer rectangle inequalities and local boundary relaxations; this is not a full graph search and does not prove the all-r theorem by computation.

## Reproduced output

```text
PASS: 8 threshold inequalities on 10000 positive-integer pairs
PASS: zero-charge characterizations for R22/R23/R24/R33 on 1<=a,b<=100
PASS: c=3, r=12 relaxed mixed-focus boundary has 19 rows
  exceptional rows: gamma=1 only (k,a,b,n2)=(6,2,2,0); gamma=0 includes the (k,a,b,n2)=(6,2,2,1) one-neighbour layer
PASS: c=3, r=13 boundary is uniquely [(6, 0, 2, 2, 0)]
PASS: c=4 (0,0,2), r=12 R24 equality is uniquely [(3, 1, 4, 2, 0)]
PASS: c=4 (0,0,2), r=12 two-focus overlap has 4 relaxed orientation pairs
PASS: c=4 (0,1,1), r=12 two-slot overlap has 4 relaxed orientation pairs
LIMITATION: this script checks local arithmetic relaxations only; it is not a graph/SAT counterexample search.
```

## Interpretation

- All eight stated threshold inequalities passed for every pair (1le a,ble100); the exact zero-charge conditions also passed on that range.
- The finite c=3 boundary enumeration agrees with the analytic equality classification: at (r=13) only ((k,gamma,a,b,n_2)=(6,0,2,2,0)) survives the local relaxation; at (r=12), the 19 listed local signatures are exactly those used in the proof and are then eliminated structurally.
- The c=4 arithmetic checks reproduce the unique (R_{24}) equality at (r=12) and the four relaxed orientation pairs in each two-focus overlap branch. The mixed-orientation pairs are not actual (K=6) configurations because their six-unit charges lie on distinct vertices; identical-orientation equality further forces identical supports by saturation.
- These are consistency checks of local arithmetic, not enumeration of graphs satisfying all global constraints.

## Search limitation

No whole-graph SAT/ILP counterexample search was run. No Z3, OR-Tools, or PySAT backend was installed in the execution environment. A graph-level encoding would need to enforce all independent 4-set constraints and all (K_r)-avoidance constraints on 35–44 vertices, which is not a lightweight substitute for the analytic proof. The theorem certification therefore rests on the proofs in PUBLICATION_VERSION.md and LEMMA_VERIFICATION.md, not on a claim of exhaustive graph search.
