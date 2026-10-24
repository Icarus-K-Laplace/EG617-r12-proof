# Counterexample Audit — F-004

## 1. F-003 square-root proof

Verdict: PASS_WITH_LIMITATIONS, conditional on Füredi, Brouwer, and Kang–Pikhurko. The bound s_i<=C implies d_i>=max(3,ceil sqrt(r/1024)) is valid under the displayed inequalities but is coarse, not sharp.

Equality audit:
1. t<=r(d_i-1) uses s_i<=C and the maximum possible number of edges incident to A_i. Equality requires s_i=C and every edge incident to A_i to lie in H_i.
2. Füredi gives internal defect a<=t and missing-cross-edge defect b<=2t. The variance estimate uses D=t-b+a<=2t.
3. k>=r/(64d_i) follows from deliberately loose constants in r-d_i<=2sqrt(krd_i)+k.
4. The random-transversal estimate is a union bound. No equality classification is established.
5. Constants 512 and 1024 are not sharp. No equality family is claimed.
No algebraic sign error was found. The d_i=2 refinement depends on the Kang–Pikhurko equality classification.

## 2. Scalar optimization witness

The scalar constraints admit d_i=r and s_i=C=binom(r,2) for all i. Then sum d_i=r^2 and sum s_i=m_0. All one-color bounds hold. For prime-power r, this slack vector is realized by the old K_(r^2) affine-skeleton family when exactly C leftover-class edges are assigned to each color.

This is not a K_(r^2+1) counterexample. It shows scalar summation alone cannot close the proof.

## 3. Abstract block-system witness

For even r, take an r/2-regular bipartite support on row/column indices and put entries 2 on its edges and 0 elsewhere. Row/column sums are r and the collision budget is r^2/2, but no entry is 1. This defeats collision-budget-only orthogonality stability; it is not a full coloring.

## 4. Boundary audit

- d_i=0,1: Brouwer degree-slack lower bounds exceed r^2/2, so neither can occur for either of the two smallest-slack colors.
- d_i=2: if s_i<=C, the Kang–Pikhurko equality classification excludes the only equality case, giving s_i>=C+1. For sufficiently large r, the medium-slack square-root theorem gives the stronger exclusion.
- 3<=d_i<r: F_r(d_i) is valid but not sharp enough to force d_i=r.
- d_i>=r: the scalar lower bound may be zero; the degree sum permits all d_i=r.
- High slack: the budget permits up to r-2 colors with s_i>r^2/2; no graph-level contradiction is proved.
- Shared blockers: the probability union bound handles overlap; it does not assume disjoint sets of blocked transversals.

## Status

No full graph-level counterexample to Problem 617 has been found. No all-large-r theorem has been proved. The main negative finding is that scalar optimization and intersection-collision budgets alone are insufficient.


## 6. Cross-color incidence audit

For \(d_i\ge r\), every \(r\)-subset of \(A_i\) must contain every color \(j\ne i\). Therefore \(\alpha(G_j[A_i])\le r-1\), while \(\alpha(G_i[A_i])\le r\). This gives
\[
\binom{d_i}{2}\ge p_r(d_i)+(r-1)p_{r-1}(d_i),
\]
which rules out \(d_i>r(r-1)\). Separately, global slack summation rules out \(d_i>r^2-\lceil(3r^2-5r+2)/(2r)\rceil\). These are genuine necessary constraints, but both leave \(d_i=r\) fully feasible.
