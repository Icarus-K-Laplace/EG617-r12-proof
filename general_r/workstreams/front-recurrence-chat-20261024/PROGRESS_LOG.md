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
