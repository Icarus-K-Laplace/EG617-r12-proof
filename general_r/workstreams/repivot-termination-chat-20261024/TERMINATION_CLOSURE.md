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


---

# Round 2 — 2026-10-24: global budget and d1 second budget

## C-N7 — AES six-type optional-degree bound: PROVED_CONDITIONAL

In the AES three-part branch, the six endpoint type classes have two independent transversal triples T0=(A0,B1,C0), T1=(A1,B0,C1). Each outside vertex must be adjacent to a full type class in each triple, or alpha(H)<=3 is violated.

Assign one witness class per triple. The assignment slacks in each triple sum to exactly four. This yields the endpoint identity

t_x<=kappa_x+u_T-1<=4,

so the optional cross-block graph has maximum degree at most four. This conclusion is conditional on the core contract and high-density AES threshold.

## C-N8 — Off-part witness excess: PROVED_CONDITIONAL

If an outside vertex has no same-part pair of fully-seen witness classes, a residual class triple with relation pattern (optional, matching, empty) forces at least a-4 additional neighbours in U. Therefore

kappa_o>=3a-4-r>=8.

For X exceptional outside vertices,

X(3a-4-r)<=K_O<=2r-2-K_U.

Since h=r+1-2a, equivalently X<=floor((4r-4-2K_U)/(r-3h-5)); the denominator is at least 16 in the high-density branch.

This is the correct statement; the stronger claim that every outside vertex sees a whole part is **not proved** and is not used.

## C-N9 — Exact clean-pair budget identity: PROVED_CONDITIONAL

For nonexceptional outside vertices assigned to parts, define u_i=s_i+2-g_i. Then sum_i u_i=4+X. With t_x the optional degree and rho_x the number of outside neighbours not in the assigned group,

t_x+rho_x=kappa_x+u_i-1,

and

2 e_opt + E_foreign = K_U + sum_i n_i(u_i-1).

This is exact no-double-counting, but does not by itself contradict K<=2r-2.

## C-N10 — d1 second excess budget: PROVED_CONDITIONAL / OPEN

For a d1 class of allowance c and multiplicity N, each support has kappa in {c-1,c}, giving

N(c-1)<=K_U<=2r-2,

in addition to (N-1)c<=3r-2 and N<=r-2. For c>=2 this is a stronger independent bound, but it remains linear in r for fixed c. Bounded-allowance d1 absorption remains OPEN.

## Updated canonical conclusion

The high-density clean-pair branch is now reduced to a six-type system with optional degree at most four and an excess-charged exceptional set. The exceptional count may still be linear near the AES threshold, so Clean Pair Nonextension is OPEN. The d1 class has an additional independent excess bound, but c=1 and fixed c>=2 multiplicities remain unresolved.

No finite r0 and no all-large-r contradiction are certified.


## C-N11 — Shell-incidence strengthening: PROVED_CONDITIONAL

For the clean a_2=2 family,

K_U>=2m-2r-b_2,

because each of the 2m endpoints has kappa_x=1-e_F(x,S_2) and the shell pair has total incidence 2r+b_2. Together with the exceptional outside charge L=3lambda-4-r, this gives

2m-2r-b_2+X L<=2r-2,

and

X<=floor(2(r-1+h+b_2)/(r-3h-5)).

Near the lower AES threshold this improves the exceptional count to X<=r/6+O(1), still allowing linear X.

## C-N12 — Overlap-corrected joint d1/d2 budget: PROVED_CONDITIONAL / OPEN

For a d1 support set V_1 of size N_1 and allowance c, define J_2=|V_1 intersect U_2| and J_X=|V_1 intersect O_exc|. Then

2m-2r-b_2+N_1(c-1)+X L
-(c-1)J_2-min(c-1,L)J_X<=2r-2.

Replacing N_1 by ceil(eta/5) gives an eta-explicit necessary inequality. For 3<=c<=L-1, both intersections vanish and the clean form is

2m-2r-b_2+ceil(eta/5)(c-1)+X L<=2r-2.

The d2 matching/allowance inequality remains ceil(N_2/(eta+1))(a_2-1)<=4r-4+a_2+b_2. These are separate necessary projections of the same budget and cannot be added without proving disjointness. Fixed-allowance d1 absorption remains OPEN.
