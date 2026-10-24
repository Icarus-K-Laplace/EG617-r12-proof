# Termination Closure Ledger — General-r Repivot Workstream

Branch: workstream/general-r-repivot-termination-20261024

Scope: backend termination only. The upstream front extraction and anchor-excess arguments remain conditional hypotheses A and B.

## 1. Canonical contract

A. Every legal core H has |H|=3r-1, alpha(H)<=3, omega(H)<=r-1, delta(H)>=r, and legal repivots preserve this contract.

B. K_r(H)>=8, hence q<=3r-1.

The global residual graph satisfies alpha(F)<=4 and omega(F)<=r-1. Independent four-sets in F are not forbidden. The inherited core excess cap is K=sum_v(d_H(v)-r)<=2r-2.

## 2. New structural results in this round

### C-N1 — Clean Pair Structural Theorem: PARTIAL

The exact block system is:

- blocks P_i={x_i^0,x_i^1}, each a target K2;
- every block-pair target graph is one of the seven matchings of K2,2;
- a selected endpoint transversal is independent exactly when the associated 2-CNF formula is satisfiable;
- every four-block restriction has no independent transversal and needs at least six target cross edges, verified by exhaustive enumeration of all 7^6 labelled patterns;
- the complement G=overline(H[U]) is K4-free and each block pair has at least two G-edges;
- if m >= ceil(4r/3+3), then delta(G)>5(2m)/8, so Andrasfai-Erdos-Sos makes G 3-partite. This yields three target cliques covering U and the bound m<=floor(3(r-1)/2), but not a contradiction.

A static three-clique-plus-block-matching family shows that the local block constraints alone admit arbitrarily large systems. Full core extension is not claimed.

### C-N2 — Clean Pair Nonextension: OPEN

No proof that m is absolutely bounded, and no all-large-r contradiction. The remaining task is to use outside-core degrees, the exact shell incidence total, and the global excess cap without double-counting. The high-density AES branch leaves a linear interval of possible m.

### C-N3 — Bounded-Allowance d1 Absorption: OPEN

For a fixed d1 class of allowance c and multiplicity N:

- c=0 gives N<=3;
- c>=1 gives N<=r-2 from the clique cap;
- under K<=2r-2, (N-1)c<=3r-2;
- eta concentration forces c=O(1) when eta=Omega(r).

This does not make N absolute. The one-point exchange orbit is exact but locally permits either adjacency status between distinct supports.

### C-N4 — Fifth-Coordinate Improvement: UNIVERSAL VERSION DISPROVED

The exact Delta Q2 formula is recorded in FIFTH_COORDINATE_AUDIT.md. Since repivot moves are reversible, a claim that every nontrivial Phi4-flat move strictly increases Q2 is impossible: the reverse move is also Phi4-flat and has the opposite increment. Q2 remains a bounded statistic, but it does not supply the desired universal monotonicity theorem.

### C-N5 — Endpoint Repivot Stability: OPEN

Phi4=(q,tau,zeta,eta) is a genuine bounded four-coordinate potential. The surviving terminal packages are still not all eliminated. No fifth coordinate has been certified to make every nonterminal state strictly improve.

### C-N6 — All-Large-r Conditional Contradiction: OPEN

No finite r0 is certified by this workstream. All results remain conditional on A+B and the inherited core cap where stated.

## 3. Canonical conclusion

The current exact outcome is a block-model theorem, a high-density 3-partite reduction for very large clean subsystems, a reversible-potential no-go audit, and a sharper description of the d1 terminal. These narrow the blocker but do not close it.

The single remaining research target is still:

Clean Pair Nonextension + bounded-allowance d1 absorption,

with the key missing ingredient being a no-double-counting inequality that couples the clean subsystem to the outside core and the decorated shell pair.

## 4. Audit warnings

- Do not use alpha(F)<=3.
- Do not revive D2_MISSING_PAIR_NEUTRAL_BOUND.md or D2_DISTINCT_MATCHING_COLLAPSE.md as theorems.
- Do not describe the static block model as a full legal-core counterexample.
- Do not claim all-large-r contradiction or a finite r0.
