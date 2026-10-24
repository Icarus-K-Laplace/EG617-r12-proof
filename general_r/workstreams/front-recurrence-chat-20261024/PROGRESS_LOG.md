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

## 2026-10-24 — H+I quantitative transfer audit

### New proved statements
1. The counterexample property is hereditary under induced vertex restriction, so the multicolor local-avoidance argument applies to every seed residual with at least r+1 vertices.
2. For a distinguished color graph J with alpha(J)<=a, its local avoidance sets have alpha at most a-1, while the other colors have the inherited r-1 bound.
3. The exact transfer inequality is
   `2 T_2 + 3 T_3 <= m [ C(m-1,2) - Lambda_{r,a}(m) ]`,
   with Lambda defined by the balanced-sum minimization in ASYMPTOTIC_SEED_ENVELOPE.md.
4. The transfer plus the wedge identity yields `2 e(J)^2/m - e(J) <= m[C(m-1,2)-Lambda]`; this is an upper constraint on e(J), not a stronger lower seed floor.
5. The exact outer-budget gap was derived in terms of `t=r-d`:
   `U-p_a(ar+t)=C(r,2)-(a+1)t^2/(2a)+t-b(a-b)/(2a)`, where `b=t mod a`.
6. At `t=1`, the exact gap is `C(r,2)`. The transfer's degree-free asymptotic relaxation leaves a factor-a scale gap at `m=ar+O(1)`.

### Status update
- H1: ACHIEVED.
- H2: PROVED conditionally on a finite sound seed package.
- H3: OPEN; no general-r improved seed excesses or cutoff theorem were obtained.
- H4: remains conditional on all-state outer-budget dominance.
- No explicit r0 is certified.

### Commit trail for this pass
- `ASYMPTOTIC_SEED_ENVELOPE.md`: `954d9e9d37fa1ac33ad6d4f650340480e2d1ad1c`
- `OUTER_BUDGET_DOMINANCE.md`: `b82e9391600e736199bede03f6cd9d12e6344b6f`

### Unique blocker
Convert the valid induced multicolor inequality into a **lower** edge floor that incorporates `alpha<=a`, `omega<=r-1`, and inherited caps. Current transfer is directionally insufficient for seed closure.

### Formatting/verification follow-up

The display-math delimiters in both joint-audit notes were normalized and the exact outer-gap identity was independently checked over integer parameters in a finite verification sweep. Latest note commits:
- seed note formatting: `0f64a7f9413717bacb661551000fa19e4d01d5e8`
- outer-gap note formatting: `ffb399e6b09973b2eb2270ccbeb50192ccc4b14d`

## 2026-10-24 — Round 2: threshold low-order cutoffs

### New proved theorem package
1. Proved `M_r(2)<=2r-1` for all `r>=6`. For n>=2r+1, complement H is triangle-free and `Delta(H)<=r-1`; the inherited cap forces `e(H)>n(r-1)/2), contradiction. At n=2r, equality forces H to be (r-1)-regular; Andrásfai–Erdős–Sós makes it bipartite for r>=6, contradicting alpha(H)<=r-1.
2. Proved `M_r(3)<=3r` for all `r>=6`. A minimum-degree pivot has core size at most 2r-1; therefore h>=n-2r. The edge floor `e(J)>=n(n-2r)/2` beats the inherited cap exactly when `2(r-1)p_r(n)>n(2r-1)`, verified for every integer n>=3r+1 and r>=6.
3. Eliminated the t=1 outer states `(a,n)=(2,2r+1)` and `(3,3r+1)` for all r>=6.
4. Audited the low-r boundary: the abstract contract admits examples at `(r,n)=(4,8)` and `(5,10)`, so `M_r(2)<=2r-1` must remain thresholded. These are not full EG617 colorings.
5. Recorded exact dependency and assumption ledgers; the contextual `a=4,n=4r+1` cutoff remains only under the no-extraction reductio.

### Status
- H1: ACHIEVED.
- H2: PROVED conditionally on a finite sound seed/cutoff package.
- Low-order cutoffs: `M_r(2)<=2r-1`, `M_r(3)<=3r` PROVED for r>=6.
- Five general-r seed excesses: OPEN.
- All-state outer-budget dominance: OPEN.
- Explicit all-large-r EG617 threshold: NOT PROVED.

### New artifacts
- `LOW_ORDER_CUTOFF_THEOREMS.md`
- `DEPENDENCY_DAG.md`
- `ASSUMPTION_LEDGER.md`

## Round 2 — Final synchronization audit

### Final mathematical status
- `M_r(2)<=2r-1` and `M_r(3)<=3r` are PROVED for every integer r>=6.
- The t=1 outer states a=2 and a=3 are eliminated for r>=6.
- The abstract contract has explicit r=4,5 examples at n=2r, so the stronger a=2 cutoff is correctly thresholded.
- Five all-r seed-floor excesses and all-state outer-budget dominance remain OPEN. The a=4,n=4r+1 extraction state is retained unless the contextual no-extraction reductio is assumed. No EG617 all-large-r r0 is claimed.

### Commit trail
- Integrated cutoff theorem, dependency DAG, and assumption ledger: `15a6a781cd7d94bc67c94cc4f71ff534ab9ffdd9`.
- Added finite small-parameter verifier: `6e616edc9035d9257b123a8922ae38193de25a34`.
- Subsequent exact-status / formatting updates are included in the current branch history; this log update is based on the branch head `51c9e391cac93836e7894750314a385e865fc5fa`.

### Reproducibility
`LOW_ORDER_CUTOFF_THEOREMS.md` contains the full all-r proof and a finite verifier for the r=4,5 abstract-contract obstructions. `DEPENDENCY_DAG.md` and `ASSUMPTION_LEDGER.md` record the precise dependencies and conditional boundaries.
