# CHAT F — Canonical State

Branch: workstream/general-r-extremal-stability-20261024

Headline target: explain the \(r^2\) threshold through extremal/design rigidity and prove nonextension to \(r^2+1\) without using residual-core, three-anchor, or repivot machinery.

## Frozen result F4 — exact affine-skeleton nonextension

For every \(r\ge3\), an affine-plane skeleton on \(r^2\) points with \(r\) pure parallel classes \(P_1,\ldots,P_r\) and an arbitrarily colored leftover class \(Q\) cannot be extended by one new vertex. The proof is in NONEXTENSION_THEOREMS.md and is not repeated in this round.

## F-002 — proved reconstruction assets

### Exact slack accounting

For a fixed deleted vertex \(x\), let \(G_i\) be the color-\(i\) graph on the remaining \(r^2\) points and \(s_i=e(G_i)-r\binom r2\). Then \(s_i\ge0\) and \(\sum_i s_i=r\binom r2\).

### Quantitative two-color near-partition theorem

Choose the two smallest slacks. Füredi's partition lemma gives two partitions into \(r\) parts, with internal defects at most \(s_i,s_j\), cross-color defects at most \(2s_i,2s_j\), and intersection matrix \(M\) satisfying
\[
\sum_{a,b}\binom{M_{ab}}2\le s_i+s_j\le r(r-1).
\]
Each selected slack is at most \(r^2/2\), so both selected colors have independence number exactly \(r\).

### Low-slack exact orthogonal-pair theorem

If two colors happen to satisfy \(s_i,s_j\le r-2\), Brouwer's theorem makes both complements \(r\)-partite. Edge-disjointness forces their clique partitions to be exactly orthogonal, with every intersection size one. This gives two orthogonal partitions, not yet an \(r\)-net.

### New-point neighborhood constraint

For \(A_i=N_i(x)\), \(B_i=V\setminus A_i\), and \(H_i=\overline{G_i}\), \(H_i[B_i]\) is \(K_r\)-free. The low-slack neighborhood lemma shows that, for \(r\ge4\), any color with \(s_i\le\binom r2\) must have \(|A_i|\ge3\). This uses Brouwer's theorem and the Kang–Pikhurko equality classification.

## Important limitation

The collision budget does not force the intersection matrix close to the all-ones matrix: explicit abstract matrices with entries 0 and 2 satisfy the budget. The exact affine-skeleton theorem cannot be applied to approximate partitions without a robust transversal-hitting theorem.

## Current status

- F1 known sharp family: PARTIALLY CLOSED; affine-plane orders only.
- F2 local regularity: OPEN.
- F3 orthogonal-skeleton stability: PARTIAL PROGRESS, headline theorem OPEN.
- F4 exact affine-skeleton nonextension: PROVED.
- F5 robust nonextension for arbitrary approximate skeletons: OPEN.
- F6 all-\(r\) Problem 617: OPEN.

## Unique blocker

Use the color labels and the new-point hitting condition to upgrade the quantitative two-color near-partitions into enough exact orthogonal partitions, or prove that every distributed-defect alternative already forces an \((r+1)\)-set missing a color.


## F-003 — stronger neighborhood lower bound

For every color \(i\) with \(s_i\le\binom r2\), the new-point degree satisfies
\[
|N_i(x)|\ge\max\!\left\{3,\left\lceil\sqrt{r/1024}\right\rceil\right\}
\qquad(r\ge4).
\]
This follows from the Turán deficit bound \(t\le r(d_i-1)\), Füredi's partition lemma, and a random-transversal defect count. Full proof: ROBUST_NONEXTENSION.md.

This is quantitative local progress, not a full reconstruction theorem. The cases \(d_i\) between order \(\sqrt r\) and \(r-1\) remain open, as does the high-slack branch.
