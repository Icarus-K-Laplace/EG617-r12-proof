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


## 5. Quantitative small-degree exclusion: \(d_i=\Omega(\sqrt r)\)

The preceding lemma can be strengthened using the full partition defect budget.

Fix a color with \(s_i\le C:=\binom r2\), and suppose \(1\le d:=d_i<r\). Put \(m=r^2-d\) and \(H=H_i[B_i]\). Its Turán deficit relative to \(T_{r-1}(m)\) is
\[
t:=T_{r-1}(m)-e(H)\ge0.
\]
From \(e(H_i)\ge T_r(r^2)-C\) and \(e(H_i)\le e(H)+dm+\binom d2\), exact cancellation gives
\[
t\le m_0+C-p_{r-1}(r^2-d)=r(d-1).
\]
Here \(p_{r-1}(r^2-d)-m_0=r(r+1-2d)/2\) for \(1\le d<r\).

Apply Füredi's partition lemma to \(H\), which is \(K_r\)-free. It gives a partition into \(q=r-1\) parts \(V_1,\ldots,V_q\), with at most \(t\) internal edges and at most \(b\le2t\le2r(d-1)\) missing cross-edges. If \(n_a=|V_a|\) and \(\mu=m/q\), the same lemma gives
\[
\sum_a(n_a-\mu)^2\le4t+q/4\le4rd.
\]
Since \(\mu>r\), the part-size sum exceeds \(qr\) by exactly \(r-d\). Let \(k\) be the number of parts of size greater than \(r\). Every such part contains an internal edge, because \(\alpha(H)\le r\). By Cauchy–Schwarz,
\[
r-d\le\sqrt{k\sum_a(n_a-\mu)^2}+k\le2\sqrt{krd}+k.
\]
Consequently \(k\ge r/(64d)\) whenever \(d\le r/2\): if \(k<r/(64d)\), the right-hand side is less than \(r/4+r/64<r/2\), contradicting \(r-d\ge r/2\).

Now use the following transversal-defect count. Select one internal edge \(u_av_a\) from each of the \(k\) oversized parts. For a fixed edge, choose a uniformly random transversal consisting of one vertex from each of the other \(q-1\) parts. Because \(H\) is \(K_{q+1}=K_r\)-free, every such transversal together with \(u_a,v_a\) must contain a missing cross-edge. If \(c_a\) is the number of missing cross-edges incident to \(u_a\) or \(v_a\), then a missing edge incident to an endpoint is selected with probability at most \(1/L\), while any other missing cross-edge is selected with probability at most \(1/L^2\), where \(L\) is a lower bound on all part sizes. Hence
\[
1\le c_a/L+b/L^2,\qquad c_a\ge L-b/L.
\]
Summing over the selected internal edges gives \(\sum_a c_a\le2b\), since each missing edge has at most two selected endpoints. Therefore
\[
b(2+k/L)\ge kL.
\]

If \(d<\sqrt{r/1024}\), then \(d\le r/16\), all parts have size at least \(L=r/2\), and \(k\le r-1\) gives \(k/L<2\). Thus
\[
b\ge kL/4\ge \frac{r^2}{512d}.
\]
But the slack bound gives \(b\le2r(d-1)<2rd\). These inequalities contradict \(r>1024d^2\).

Combining this with the \(d=0,1,2\) exclusions above proves the stronger theorem:
\[
\boxed{
s_i\le\binom r2
\quad\Longrightarrow\quad
d_i\ge \max\!\left\{3,\left\lceil\sqrt{r/1024}\right\rceil\right\}
\qquad(r\ge4).
}
\]

This is an all-\(r\) quantitative neighborhood lower bound, conditional only on the cited Füredi, Brouwer, and Kang–Pikhurko inputs. It still does not force \(d_i\ge r\), so it is not a nonextension theorem.


## 6. F-004 — equality audit and joint slack–neighborhood inequality

### Audit of F-003

Verdict: PASS_WITH_LIMITATIONS, conditional on the cited Füredi, Brouwer, and Kang–Pikhurko inputs. The bound is coarse, not sharp. The inequality t <= r(d_i-1) uses s_i <= C and the maximum possible number of edges incident to A_i; equality requires s_i=C and every edge incident to A_i to lie in H_i. Füredi gives internal defect a<=t and missing-cross-edge defect b<=2t; the variance estimate uses D=t-b+a<=2t. The oversized-part bound k>=r/(64d_i) uses deliberately loose constants. The random-transversal step is a union bound, with no equality classification. No algebraic sign error was found; constants 512 and 1024 are not claimed sharp. The d_i=2 refinement depends on Kang–Pikhurko.

### Linear low-slack rigidity

Apply Füredi to H_i with r parts. If their sizes are n_a, then the exact partition identity gives sum_a (n_a-r)^2 <= 4s_i; the missing cross-edge count b is at most 2s_i. If s_i<=r^2/100, all parts have size at least L=4r/5 and b<=r^2/50. Since A_i hits every K_r of H_i, weighted transversal hitting gives 1<=d_i/L+b/L^2. Hence d_i>=L-b/L>=31r/40.

### Medium-slack strengthening

The F-003 defect argument also works for s_i<=r^2/2. For 1<=d_i<r, the Turán deficit t of H_i[B_i] obeys t<=r(d_i-1/2)<=r d_i; the partition variance is <5r d_i and b<=2r d_i. The same oversized-part/transversal argument rules out d_i<sqrt(r/1600). Brouwer bounds rule out d_i=0,1 in this slack range. Therefore s_i<=r^2/2 implies d_i>=max{2,ceil sqrt(r/1600)}. The two smallest-slack colors both satisfy this because s_(2)<=r^2/2.

## 7. F-004 status

- Weighted transversal-hitting lemma: PROVED_ANALYTIC.
- Joint slack–neighborhood inequality: PROVED_CONDITIONAL on Füredi.
- Linear low-slack rigidity: PROVED_CONDITIONAL.
- Scalar summation as a complete proof: DISPROVED as a strategy by d_i=r, s_i=C for all i.
- Cross-color incidence theorem and robust skeleton reconstruction: OPEN.


## 8. F-005 — cross-color neighborhood incidence

If d_i>=r, every r-subset of A_i, together with x, is an (r+1)-set whose x-edges all have color i. Therefore every other color j must occur inside every r-subset of A_i, so alpha(G_j[A_i])<=r-1 for j!=i. Also alpha(G_i[A_i])<=r. Consequently
binom(d_i,2) >= p_r(d_i)+(r-1)p_(r-1)(d_i).
Using p_q(d+1)-p_q(d)=floor(d/q), equality holds at d_i=r(r-1), and the inequality fails for larger d_i<=r^2. Thus d_i<=r(r-1).

A separate global slack sum gives
d_i <= r^2-ceil((3r^2-5r+2)/(2r)).
For r>=5 this is stronger and excludes any neighborhood containing all but fewer than roughly 1.5r old vertices.

These are necessary conditions only. They do not constrain the central regime d_i≈r, where the scalar optimum remains feasible.
