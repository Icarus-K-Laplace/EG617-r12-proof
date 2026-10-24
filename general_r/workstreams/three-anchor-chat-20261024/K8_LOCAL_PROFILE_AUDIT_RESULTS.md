# K=8 local profile audit results

## Reproducibility and scope

Source: K8_LOCAL_PROFILE_AUDIT.py. The enumerator solves exact connector-degree equations over integer parameters and checks the \(R_{22}\) charge. It is a local necessary-condition audit, not a complete graph search.

The tuple convention is
\[
(k,\gamma,n_{\mathrm{opp}},a,b,R_{22}(a,b),k+R_{22}(a,b)).
\]

## Output

```text
c4_002_f2: r=13 profiles with k<=1: 10; r=14 equality profiles: [(0, 1, 0, 10, 1, 8, 8), (0, 1, 0, 1, 10, 8, 8)]
c4_011_s2: r=13 profiles with k<=1: 12; r=14 equality profiles: [(0, 1, 0, 10, 1, 8, 8), (0, 1, 0, 1, 10, 8, 8)]
c=3 mixed r=14 local profiles with cost <=8: 23
PASS: c=3 r=14 complete profile list, r=15 exceptional profile, r=16 empty.
LIMITATION: local integer/rectangle profiles only; no full graph H or SAT/ILP search.
```

## \(c=3\), mixed-focus boundary

At \(r=14\), exactly 23 local profiles have cost at most eight:
- 18 one-sided profiles \(a=1,b=10-k\) or \(a=10-k,b=1\), \(0\le k\le8\), each with local cost eight;
- two additional profiles \((k,a,b)=(6,2,3),(6,3,2)\), local cost eight;
- one profile \((k,a,b)=(7,2,2)\), local cost seven, leaving one global excess unit;
- two profiles \((k,a,b)=(8,2,2)\) with \((\gamma,n_{\mathrm{opp}})=(0,1)\) or \((1,0)\), local cost eight.

This exact list is then eliminated analytically in EQUALITY_K8_CLASSIFICATION.md by common-nonneighbour cliques and saturation. At \(r=15\), the only local profile is \((8,0,0,2,2,0,8)\), which is excluded by a common-nonneighbour clique of size fifteen. At \(r=16\), no local profile survives.

## \(c=4\) overlap boundaries

At \(r=13\), after applying the global overlap consequence \(k\le1\), every surviving local profile in both two-focus branches has one side of size one. The script reports 10 profiles for \((0,0,2),f=2\) and 12 for \((0,1,1),s=2\). The full graph conditions further restrict the equality candidates; the \(c=4,(0,0,2),f=2\) branch is excluded by external-incidence counting, while the \(c=4,(0,1,1),s=2\) branch remains OPEN at \(r=13\).

At \(r=14\), the only local equality orientations in either branch are \((10,1)\) and \((1,10)\), with \(\gamma=1,n_{\mathrm{opp}}=0,k=0\). Their saturated-vertex incidence contradictions are proved analytically in EQUALITY_K8_CLASSIFICATION.md.

## Explicit non-claim

These computations check local integer profiles only. They do not generate full graphs, do not verify all independent-four and clique constraints, and do not prove realizability. No graph-level SAT/ILP counterexample search was run.
