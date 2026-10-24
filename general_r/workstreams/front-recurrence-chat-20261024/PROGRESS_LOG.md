# Progress Log — Front Recurrence

## 2026-10-24 — Decompilation pass 1

### Inputs audited

Read the canonical r=12 recurrence proof, two independent integer recurrence implementations, the 144-row outer-stop table, the front bridge theorem, and the mother-line general-r structural dictionary.

### Substantive advances

1. Identified the 1752-node certificate as a two-dimensional DP in `(a,n)`, not a large collection of structural cases.
2. Compressed all recurrence behavior into seven transition schemas.
3. Proved the natural-number well-founded potential
   `Phi_r(a,n)=(r^2+2)a+n`.
4. Generalized the shell-complement floor to
   `Z_r(h)=max(p_(r-2)(h),C(h+1,2)-D_r(h+1),C(h,2)-D_r(h))`.
5. Generalized the automatic matching guarantee to
   `k_0(r,h)=ceil((h-r+2)/2)` for `h>=r-1`; r=12 shell-cap upgrades are isolated as optional quantitative improvements.
6. Compressed the outer table to
   `a=r-1-j`, `n=r^2-d-jr`,
   `U_r(d,j)=r(r^2+1)/2-C(d+1,2)-j C(r,2)`.
7. Proved `d<=r-1` for the least-color anchor for every `r>3` using average degree plus Brooks.
8. Formulated and proved the conditional symbolic extraction theorem: if the recurrence floors beat every outer budget except `(r-1,r-6)` and the extraction coordinate `(r-1,r-5)`, then every counterexample yields a `(4r+1)` residual or `(5r+1)` design terminal.
9. Isolated a small seed interface mirroring the exact r=12 proof: two low-a cutoffs plus five edge-floor coordinates.

### Status against requested goals

- H1: ACHIEVED.
- H2: ACHIEVED (conditional on sound finite seeds; all `r>3`).
- H3: OPEN.
- H4: PROVED CONDITIONALLY on symbolic outer-budget dominance.

### Unique blocker

Derive uniform/asymptotic formulas for the low-order seed envelope and prove that their recurrence closure beats all nonterminal outer budgets.

### Next attack

Do not parameterize more r=12 nodes. Instead derive analytic lower bounds for the five seed coordinates, beginning with `(2,2r-1)` and the two `a=3` coordinates, and test whether coarse asymptotics already imply the required outer dominance for sufficiently large r.
