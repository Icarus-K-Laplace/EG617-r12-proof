# Progress Log

## 2026-10-24 — F-001

- Read the mother-branch affine-plane nonextension theorem and the original 1999 Erdős–Gyárfás construction.
- Corrected the sharp-family picture: the unused affine parallel class can be colored edge-by-edge arbitrarily while each color retains one full parallel class and balance on \(K_{r^2}\).
- Killed naive \(O(r)\) / \(o(r^2)\) edge-edit stability to one standard affine coloring; the correct invariant is an orthogonal-partition skeleton.
- Proved the grid matching-preclusion lemma: a set meeting every permutation transversal in an \(r\times r\) grid has size at least \(r\); equality for \(r\ge3\) is exactly a full row or full column.
- Proved the arbitrary-leftover affine-skeleton nonextension theorem for every \(r\ge3\).
- Identified skeleton reconstruction as the remaining headline blocker.

## 2026-10-24 — F-002: quantitative near-partitions and neighborhood slack

### New proved assets

1. **Exact slack budget.** On any \(r^2\)-point restriction, \(s_i=e(G_i)-r\binom r2\ge0\) and \(\sum_i s_i=r\binom r2\).
2. **Two-color near-partition extraction.** Choose the two smallest slacks. Füredi's partition lemma gives two \(r\)-partitions with internal defect at most \(s_i,s_j\), cross-color defect at most \(2s_i,2s_j\), part-size variance at most \(4s_i,4s_j\), and intersection collision budget \(\sum_{a,b}\binom{M_{ab}}2\le s_i+s_j\le r(r-1)\).
3. **Two selected colors have \(\alpha=r\).** Since the second-smallest slack is at most \(r^2/2\), it is below \(T_r(r^2)-T_{r-1}(r^2)=(r^2+r+2)/2\); neither selected color can have independence number at most \(r-1\).
4. **New-point neighborhood condition.** For \(A_i=N_i(x)\), \(H_i=\overline{G_i}\), the complement induced on \(V\setminus A_i\) is \(K_r\)-free.
5. **Low-slack neighborhood lemma.** For \(r\ge4\), any color with \(s_i\le\binom r2\) must have \(|A_i|\ge3\). The proof uses Brouwer's non-partite Turán bound and the Kang–Pikhurko classification in the \(d_i=2\) boundary case.

### Red-team finding inside F

The collision budget alone does not force orthogonality. For even \(r\), the matrix with entries two on an \(r/2\)-regular bipartite support and zero elsewhere has row/column sums \(r\), collision budget \(r^2/2\), and no entries equal to one. This is an abstract block-system obstruction, not a full coloring counterexample.

### Still open

- Reconstruct an exact \(r\)-net from arbitrary near-partitions plus the color-label constraints.
- Close the high-slack branch using the new-point hitting condition.
- Prove a robust nonextension theorem for approximate skeletons.
- All-large-\(r\) and all-\(r\) Problem 617 remain OPEN.

### External dependencies

- Füredi partition lemma: Balogh et al., *Making \(K_{r+1}\)-free graphs \(r\)-partite*, CPC 30 (2021), DOI 10.1017/S0963548320000590.
- Brouwer non-partite Turán bound: if a \(K_{q+1}\)-free graph on \(m\ge2q+1\) vertices is not \(q\)-partite, then \(e\le T_q(m)-\lfloor m/q\rfloor+1\).
- Kang–Pikhurko extremal classification for equality in Brouwer's bound: *Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite*, Matematychni Studii 24 (2005), 12–20, DOI 10.30970/ms.24.1.12-20.


## 2026-10-24 — F-003: square-root neighborhood lower bound

- Strengthened the low-slack neighborhood lemma from \(d_i\ge3\) to \(d_i\ge\max\{3,\lceil\sqrt{r/1024}\rceil\}\) for every color with \(s_i\le\binom r2\).
- Key exact reduction: the Turán deficit \(t\) of \(H_i[V\setminus A_i]\) relative to \(T_{r-1}\) obeys \(t\le r(d_i-1)\).
- Füredi's partition gives at most \(2r(d_i-1)\) missing cross-edges and part-size variance at most \(4rd_i\).
- A random-transversal blocker count shows that the oversized parts require at least \(r^2/(512d_i)\) missing cross-edges, contradicting the upper bound when \(r>1024d_i^2\).
- Status: PROVED_CONDITIONAL on Füredi, Brouwer, and Kang–Pikhurko. This does not yet force \(d_i\ge r\) or close the arbitrary-counterexample reconstruction.


## 2026-10-24 — F-004: joint slack–neighborhood rigidity

1. Proved the weighted transversal-hitting lemma for arbitrary nonempty partitions and shared missing-edge blockers.
2. Derived the joint inequality d_i >= L_i-2s_i/L_i for L_i=r-2sqrt(s_i)>0.
3. Obtained linear rigidity: s_i<=r^2/100 implies d_i>=31r/40.
4. Inverted the tradeoff to s_i>=ceil(U_r(d_i)^2) for d_i<r.
5. Extended the previous square-root argument to s_i<=r^2/2, giving d_i>=max(2,ceil sqrt(r/1600)); both smallest-slack colors satisfy this.
6. Audited F-003 equality points: the proof is algebraically consistent but deliberately non-sharp; no equality family is asserted.
7. Solved the scalar optimization: its minimum lower-bound cost is zero at d_i=r for every i. Taking s_i=binom(r,2) realizes the exact total slack, so scalar summation cannot close the proof.

Current status: joint local rigidity PROVED_CONDITIONAL; robust exact skeleton reconstruction OPEN; direct missing-color obstruction for distributed defects OPEN; all-large-r/all-r theorem OPEN.

External dependencies remain Füredi's partition lemma, Brouwer's non-partite Turán bound, and Kang–Pikhurko's equality classification for the d_i=2 boundary.
