# Skeleton Reconstruction — F-002

Status: partial theorem proved; full reconstruction remains OPEN.

This note uses only the coloring restriction, Turán/Füredi stability, and the new-point neighborhood constraints. It does not use residual-core, three-anchor, or repivot machinery.

## 1. Counterexample contract and exact slack budget

Assume for contradiction that a coloring of \(K_{r^2+1}\) has every \((r+1)\)-set using all \(r\) colors. Fix \(x\), let \(V=V(K_{r^2+1})\setminus\{x\}\), and write \(n=r^2\).

For each color \(i\), let \(G_i\) be its graph on \(V\), and put \(H_i=\overline{G_i}\). Then:

- \(\alpha(G_i)\le r\), since an independent \((r+1)\)-set would miss color \(i\);
- \(\omega(G_i)\le r\), since a monochromatic \(K_{r+1}\) in color \(i\) is an independent \((r+1)\)-set in every other color;
- equivalently, \(H_i\) is \(K_{r+1}\)-free and \(\alpha(H_i)\le r\).

Let
\[
m_0=r\binom r2=\frac{r^2(r-1)}2,\qquad
s_i=e(G_i)-m_0.
\]
Turán gives \(s_i\ge0\), and edge partitioning gives the exact identity
\[
\boxed{\sum_{i=1}^r s_i=m_0.}
\]
Also \(e(H_i)=T_r(r^2)-s_i\), where \(T_q(m)=\mathrm{ex}(m,K_{q+1})\).

## 2. Theorem F-002A — two-color quantitative near-partition extraction

Choose \(i,j\) with the two smallest slacks. Then
\[
s_i+s_j\le \frac{2m_0}{r}=r(r-1),
\qquad s_i,s_j\le r^2/2.
\]

Apply Füredi's partition lemma to each \(K_{r+1}\)-free graph \(H_i,H_j\). There are partitions
\[
\mathcal P=(P_1,\ldots,P_r),\qquad
\mathcal Q=(Q_1,\ldots,Q_r)
\]
such that, writing \(a_i=\sum_a e(H_i[P_a])\) and \(b_i\) for the number of missing \(H_i\)-edges between distinct parts,
\[
a_i\le s_i,\qquad b_i\le 2s_i,
\]
and analogously \(a_j\le s_j,\ b_j\le2s_j\).

Interpretation in the original coloring:

- the total number of non-color-\(i\) pairs internal to the \(P_a\)'s is \(a_i\le s_i\), so the parts are monochromatic cliques except for these explicitly counted defects;
- at most \(b_i\le2s_i\) color-\(i\) edges cross the partition \(\mathcal P\);
- the analogous statements hold for color \(j\).

Let \(M_{ab}=|P_a\cap Q_b|\). Every pair contained in one cell \(P_a\cap Q_b\) must be a defect for at least one of the two partitions: an edge of color \(i\) is an internal \(H_j\)-edge, an edge of color \(j\) is an internal \(H_i\)-edge, and any other color is an internal edge in both complements. Therefore
\[
\boxed{\sum_{a,b}\binom{M_{ab}}2\le a_i+a_j\le s_i+s_j\le r(r-1).}
\]

The part sizes are quantitatively controlled as well. If \(p_a=|P_a|\), then
\[
T_r(r^2)-\sum_{a<b}p_ap_b
=\frac12\sum_a(p_a-r)^2
\le 2s_i\le r^2.
\]
Thus \(\sum_a(p_a-r)^2\le2r^2\), and at most seven parts can lie outside \([r/2,3r/2]\). The same holds for \(\mathcal Q\).

This is a genuine all-\(r\) two-color near-partition theorem, with explicit defect budgets. It does not yet give a net.

**External input:** Füredi's partition lemma: if \(H\) is \(K_{q+1}\)-free and \(e(H)\ge T_q(n)-t\), there is a \(q\)-partition with at most \(t\) internal edges and at most \(2t\) missing cross-edges. See Balogh–Clemen–Lavrov–Lidický–Pfender, *Making \(K_{r+1}\)-free graphs \(r\)-partite*, Combinatorics, Probability and Computing 30 (2021), 609–618, DOI 10.1017/S0963548320000590.

## 3. Theorem F-002B — the two selected colors both have independence number exactly \(r\)

For \(n=r^2\),
\[
T_r(n)-T_{r-1}(n)=\frac{r^2+r+2}{2}>r^2/2.
\]
If \(\alpha(G_k)\le r-1\), then \(H_k\) is \(K_r\)-free, so \(e(H_k)\le T_{r-1}(n)\), forcing \(s_k\ge (r^2+r+2)/2\). This is impossible for either of the two selected colors because their slacks are at most \(r^2/2\).

Hence \(\alpha(G_i)=\alpha(G_j)=r\). Equivalently, both \(H_i,H_j\) contain \(K_r\)'s, and the new-point color neighborhoods must hit those cliques.

## 4. What has not been reconstructed

The intersection budget
\[
\sum_{a,b}\binom{M_{ab}}2\le r(r-1)
\]
does not force \(M\) to be close to the all-ones matrix. For even \(r\), take an \(r/2\)-regular bipartite graph on row/column indices and set \(M_{ab}=2\) on its edges and \(0\) elsewhere. Every row and column sum is \(r\), while
\[
\sum_{a,b}\binom{M_{ab}}2=r^2/2\le r(r-1),
\]
yet the matrix has no entries equal to \(1\). This is a valid abstract intersection matrix of two partitions; it is not claimed to extend to a full edge-coloring.

Therefore the proved output is quantitative near-partition extraction, not exact orthogonality. The next theorem must exploit the color labels and the new-point hitting condition, not only the scalar collision budget.

## Status

- Exact slack identity: PROVED_ANALYTIC.
- Two-color near-partition extraction: PROVED_CONDITIONAL on Füredi's standard partition lemma.
- Two selected colors have \(\alpha=r\): PROVED_ANALYTIC.
- Exact net reconstruction from an arbitrary restriction: OPEN.
- All-large-\(r\) / all-\(r\) theorem: OPEN.


## 5. F-003 addendum — low-slack neighborhoods cannot be too small

For a color with \(s_i\le\binom r2\), the new-point neighborhood size \(d_i=|N_i(x)|\) satisfies
\[
d_i\ge \max\!\left\{3,\left\lceil\sqrt{r/1024}\right\rceil\right\}
\qquad(r\ge4).
\]
The proof combines the exact inequality \(t\le r(d_i-1)\) for the Turán deficit of \(H_i[V\setminus A_i]\), Füredi's partition lemma, and a transversal-defect count. Full proof is in ROBUST_NONEXTENSION.md.

This strengthens the previous \(d_i\ge3\) boundary result to \(d_i=\Omega(\sqrt r)\). It remains a local constraint and does not reconstruct the full net.
