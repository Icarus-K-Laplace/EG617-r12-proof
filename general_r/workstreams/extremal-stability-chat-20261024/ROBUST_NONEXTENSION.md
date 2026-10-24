# Robust Nonextension — F-002

The exact affine-skeleton nonextension theorem is frozen and is not reproved here. This file records the extension constraints that any arbitrary hypothetical counterexample must satisfy, plus a new local slack reduction.

## 1. New-point hitting condition

Fix a vertex \(x\) in a hypothetical balanced coloring of \(K_{r^2+1}\). On the old vertex set \(V\), let \(G_i\) be the color-\(i\) graph and \(H_i=\overline{G_i}\). Define
\[
A_i=N_i(x),\qquad d_i=|A_i|,\qquad B_i=V\setminus A_i.
\]
The \(A_i\) partition \(V\), so \(\sum_i d_i=r^2\).

The counterexample condition implies that \(A_i\) hits every \(K_r\) in \(H_i\), equivalently
\[
H_i[B_i]\text{ is }K_r\text{-free}.
\]
Otherwise a \(K_r\subseteq H_i[B_i]\), together with \(x\), would be an \((r+1)\)-set with no color-\(i\) edge.

Also \(\alpha(H_i)=\omega(G_i)\le r\): a color-\(i\) clique of size \(r+1\) would be independent in every other color.

## 2. Degree-slack inequality

Write \(s_i=T_r(r^2)-e(H_i)\), so \(s_i=e(G_i)-m_0\). Let
\[
p_q(m)=\binom m2-T_q(m)
\]
be the minimum number of edges in an \(m\)-vertex graph with independence number at most \(q\).

Suppose \(d_i<r\), and put \(m=r^2-d_i\). Then \(m>r(r-1)\). The graph \(H_i[B_i]\) is \(K_r\)-free and has independence number at most \(r\), so it cannot be \((r-1)\)-partite: an \((r-1)\)-partite graph with independent parts of size at most \(r\) has at most \(r(r-1)\) vertices.

Brouwer's non-partite Turán theorem, applied with parameter \(r-1\), gives
\[
e(H_i[B_i])\le T_{r-1}(m)-\left\lfloor\frac{m}{r-1}\right\rfloor+1.
\]
Since at most \(d_i m+\binom{d_i}{2}\) further edges touch \(A_i\), rearrangement yields
\[
\boxed{s_i\ge p_{r-1}(r^2-d_i)-m_0+
\left\lfloor\frac{r^2-d_i}{r-1}\right\rfloor-1.}
\]

In particular, for \(r\ge4\):
- \(d_i=0\) forces \(s_i\ge (r^2+r+2)/2+r\), which is larger than \(\binom r2\);
- \(d_i=1\) forces \(s_i\ge \binom r2+r\), also larger than \(\binom r2\);
- the generic bound for \(d_i=2\) is \(s_i\ge\binom r2-1\).

## 3. Boundary case \(d_i=2\) for a low-slack color

A further one-edge improvement is available when \(d_i=2\). Then \(m=r^2-2\), and \(H_i[B_i]\) is a \(K_r\)-free, non-\((r-1)\)-partite graph. Brouwer's bound is
\[
e(H_i[B_i])\le T_{r-1}(m)-r+1.
\]
Equality is classified by Kang–Pikhurko: deleting one vertex leaves a complete \((r-1)\)-partite graph on \(m-1=r^2-3\) vertices. For \(r\ge4\), this many vertices cannot fit into \(r-1\) independent parts of size at most \(r\), contradicting \(\alpha(H_i[B_i])\le r\). Hence
\[
e(H_i[B_i])\le T_{r-1}(m)-r,
\qquad s_i\ge\binom r2.
\]

Now suppose \(s_i\le\binom r2\). Equality must hold throughout. In particular, the two vertices of \(A_i\) are adjacent in \(H_i\) and both are complete to \(B_i\). Since \(H_i\) is \(K_{r+1}\)-free, \(H_i[B_i]\) must then be \(K_{r-1}\)-free. But equality gives
\[
e(H_i[B_i])=T_{r-1}(r^2-2)-r>T_{r-2}(r^2-2),
\]
because
\[
T_{r-1}(r^2-2)-T_{r-2}(r^2-2)=\frac{r^2+3r+4}{2}>r.
\]
Contradiction.

Therefore the following local theorem is proved, conditional on Brouwer and the Kang–Pikhurko extremal classification:

> **Low-slack neighborhood lemma.** For \(r\ge4\), every color \(i\) with \(s_i\le\binom r2\) must satisfy \(d_i\ge3\).

At least one color has \(s_i\le\binom r2\), by the exact slack average. Thus every hypothetical counterexample has, at each deleted vertex, a minimum-slack color whose incident degree is at least three.

This does not yet force \(d_i\ge r\). The cases \(3\le d_i<r\) remain open.

## 4. Robustness boundary

The exact affine-skeleton theorem relies on every color having an exact spanning \(K_r\)-partition and on the resulting family of permutation transversals. The present near-partition theorem only controls defects by \(O(r^2)\), and an abstract intersection matrix can distribute those defects across \(O(r^2)\) cells. Applying exact nonextension to such a structure would be invalid.

To close the arbitrary case, one must prove a robust transversal-hitting theorem that controls:
- missing cross-color edges;
- intersection cells of size at least two;
- exceptional/empty blocks;
- the sets \(A_i\) that must hit every \(K_r\) in \(H_i\).

## Status

- New-point K_r-hitting condition: PROVED_ANALYTIC.
- Degree-slack inequality: PROVED_CONDITIONAL on Brouwer's theorem.
- Low-slack neighborhood lemma \(s_i\le\binom r2\Rightarrow d_i\ge3\): PROVED_CONDITIONAL on Brouwer and Kang–Pikhurko.
- Robust nonextension for arbitrary near-skeletons: OPEN.
- All-large-\(r\) theorem: OPEN.
