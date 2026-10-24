# Slack Dichotomy — F-002

## 1. Exact accounting

On a fixed \(r^2\)-vertex restriction of a hypothetical \(K_{r^2+1}\) counterexample, define
\[
m_0=r\binom r2,\qquad s_i=e(G_i)-m_0.
\]
Then
\[
s_i\ge0,\qquad \sum_{i=1}^r s_i=m_0,\qquad \frac1r\sum_i s_i=\binom r2.
\]

The average is order \(r^2\), not order \(r\). Therefore no pigeonhole argument can force two colors with \(s_i\le r-2\).

## 2. Low-slack branch

If two colors have \(s_i,s_j\le r-2\), Brouwer stability makes both complements \(r\)-partite. Their complementary color graphs contain spanning clique partitions, and edge-disjointness forces the partitions to be exactly orthogonal.

This branch is proved, but the slack budget does not guarantee its hypothesis.

## 3. A useful fact that does follow from the budget

Let \(s_{(1)}\le s_{(2)}\le\cdots\le s_{(r)}\). Then
\[
s_{(2)}\le \frac{m_0}{r-1}=\frac{r^2}{2}.
\]
For \(n=r^2\),
\[
T_r(n)-T_{r-1}(n)=\frac{r^2+r+2}{2}>\frac{r^2}{2}.
\]
If a selected color had \(\alpha(G_i)\le r-1\), its complement would be \(K_r\)-free and would force \(s_i\ge T_r-T_{r-1}\), contradiction. Thus the two smallest-slack colors both satisfy \(\alpha(G_i)=r\). They have genuine maximum independent \(r\)-sets, and the new-point neighborhoods must hit all such sets.

This is stronger than an unqualified average-slack observation, but it is not yet a clique-partition theorem.

## 4. Why a scalar high-slack contradiction is false

On the affine-skeleton \(K_{r^2}\) construction, each color already contains its full \(P_i\)-partition, while the remaining \(Q\)-edges can be colored arbitrarily. The slack \(s_i\) is exactly the number of \(Q\)-edges assigned to color \(i\). A nearly even assignment has \(s_i\ge r-1\) for every color, despite the exact underlying skeleton.

Therefore a valid high-slack argument must use the extension data \(A_i=N_i(x)\) and its transversal-hitting property. Slack values alone cannot distinguish a rigid net from a coloring with no recoverable net.

## 5. Remaining high-slack target

For \(A_i=N_i(x)\), \(B_i=V\setminus A_i\), and \(H_i=\overline{G_i}\), the counterexample condition gives
\[
H_i[B_i]\text{ is }K_r\text{-free}.
\]
Indeed, a \(K_r\) in \(H_i[B_i]\) together with \(x\) would be an \((r+1)\)-set missing color \(i\).

The next step is to combine this K_r-free induced-subgraph condition with \(\alpha(H_i)\le r\), the Turán slack, and the cross-color edge partition. The scalar identity by itself does not close the high-slack branch.

## Status

- Exact slack identity: PROVED_ANALYTIC.
- At least two colors have \(\alpha=r\): PROVED_ANALYTIC.
- Two low-slack colors imply an exact orthogonal pair: PROVED_CONDITIONAL.
- Low-slack/high-slack dichotomy closing all counterexamples: OPEN.
- All-large-\(r\) theorem: OPEN.


## 6. F-003: high slack cannot be avoided by a scalar argument, but small neighborhoods are constrained

The extension condition plus Füredi stability gives a new quantitative statement: if \(s_i\le\binom r2\), then
\[
|A_i|\ge\max\!\left\{3,\left\lceil\sqrt{r/1024}\right\rceil\right\}
\quad(r\ge4).
\]
Thus a low-slack color cannot have a tiny new-point neighborhood. The proof uses a transversal-defect count on the near-\(T_{r-1}\) graph \(H_i[B_i]\), not merely the scalar slack identity.

This does not eliminate the high-slack branch: a color with \(d_i<\sqrt{r/1024}\) must have slack \(s_i>\binom r2\), but the total slack budget can accommodate several such colors. A further cross-color argument is needed.
