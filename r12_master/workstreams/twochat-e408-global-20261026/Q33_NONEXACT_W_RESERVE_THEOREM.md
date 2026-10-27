# Q33 nonexact-color reserve theorem on the 16-point complement

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the Q33 284-edge / 31-point / 56-witness contract and the retained exact-129 factor theorem.  
Scope: sharpens the global exact-color count terminal. It does not close E408 Q33 or EG617(r=12).

## 1. Universal four-edge reserve for every non-target color on W

Let \(W=H\setminus U\), \(|W|=16\). For every non-target color \(C\), the global coloring contract gives
\[
\alpha(C[W])\le 12.
\]
Hence
\[
\boxed{e_C(W)\ge 4.}\tag{1}
\]
Indeed, if \(e_C(W)\le3\), choose one endpoint from each edge; this is a vertex cover of size at most three, so \(C[W]\) has an independent set of size at least \(16-3=13\), impossible.

Equality in (1) is rigid:
\[
e_C(W)=4\quad\Longrightarrow\quad C[W]=4K_2\dot\cup 8K_1.\tag{2}
\]
If two of four edges met, their shared endpoint together with one endpoint from each remaining edge would be a vertex cover of size at most three. Thus four edges with independence number at most twelve must be a matching.

If there are \(m\) exact-129 colors, there are \(11-m\) nonexact non-target colors, and by unique edge ownership their induced edge sets on \(W\) are pairwise disjoint and disjoint from every exact-color component-witness edge. Therefore these colors reserve at least
\[
\boxed{4(11-m)}\tag{3}
\]
edges of \(\overline{H[W]}\).

## 2. Combine with the selected exact-color contribution

Let \(h\) be the number of gadget witnesses among the 56 selected witnesses. The previously proved selected-color lower bound is
\[
e_{\rm selected\ components}(W)\ge72+6h.\tag{4}
\]
Also
\[
e(\overline{H[W]})=79+\delta+\epsilon_U\le96,\qquad \delta+\epsilon_U\le17.\tag{5}
\]

### 2.1 The branch m=8

There is no unselected exact color. Equations (3)--(5) give
\[
84+6h\le e(\overline{H[W]})\le96,
\]
so
\[
\boxed{h\le2.}\tag{6}
\]
If \(h=2\), equality holds throughout:
\[
e(\overline{H[W]})=96,\qquad \delta+\epsilon_U=17.
\]
Thus \(H[W]=4K_4\) and \(\overline{H[W]}=K_{4,4,4,4}\). The eight selected exact colors contribute exactly two component \(K_4\)'s and twenty-four component triangles, totaling 84 edges. The three nonexact colors each attain equality in (1), hence each contributes a four-edge matching. Therefore the entire 96-edge graph \(K_{4,4,4,4}\) is partitioned into
\[
\boxed{2K_4+24K_3+3M_4,}\tag{7}
\]
where the two \(K_4\)'s belong to the two gadget-witness selected colors, the 24 triangles are grouped three-per-selected-color and are vertex-disjoint within each color, and each \(M_4\) is a matching of four edges.

This kernel is exact but, by itself, is not contradictory.

### 2.2 The branch m=9

There are exactly two nonexact colors, reserving at least eight W-edges. Let the ninth exact color outside the selected eight have ten component four-sets \(Q_\ell\), and put
\[
k_\ell=|Q_\ell\cap U|,
\quad c_U=\sum_{\ell=1}^{10}\binom{k_\ell}{2},
\quad c_W=\sum_{\ell=1}^{10}\binom{4-k_\ell}{2}.
\]
The prior U-capacity theorem gives
\[
\sum k_\ell\ge24,\qquad c_U\le\delta+4h.\tag{8}
\]
After reserving the eight nonexact-color edges, the W-capacity improves to
\[
\boxed{c_W\le \delta+\epsilon_U-1-6h.}\tag{9}
\]

If \(h=3\), the right side of (9) is at most
\[
17-1-18=-2,
\]
impossible. Hence
\[
\boxed{m=9\Longrightarrow h\le2.}\tag{10}
\]
Together with the earlier \(h\ge1\),
\[
\boxed{m=9\Longrightarrow h\in\{1,2\}.}\tag{11}
\]

For \(h=1\), the pointwise inequality \(k\le\tfrac32+\tfrac12\binom{k}{2}\) implies \(c_U\ge18\), so (8) gives \(\delta\ge14\).

For \(h=2\), suppose \(\delta\le13\). Then \(c_U\le21\), while (9) and \(\delta+\epsilon_U\le17\) give \(c_W\le4\). Write \(x_\ell=k_\ell-2\), \(X=\sum x_\ell\ge4\), and \(Q=\sum x_\ell^2\). The exact identities are
\[
c_U=\frac{Q+3X+20}{2},\qquad
c_W=\frac{Q-3X+20}{2}.\tag{12}
\]
Since \(Q\ge X\) for integer \(x_\ell\in\{-2,-1,0,1,2\}\) with \(X\ge0\), the bound \(c_W\le4\) gives \(X\ge6\), while \(c_U\le21\) gives \(X\le5\), contradiction. Thus
\[
\boxed{m=9\Longrightarrow \delta\ge14.}\tag{13}
\]

The endpoint \(h=2,\delta=14\) is rigid. Then \(\epsilon_U\le3\). If \(\epsilon_U\le2\), (9) gives \(c_W\le3\), which together with (12) and \(c_U\le22\) is impossible. Hence \(\epsilon_U=3\). Equations (8),(9),(12) then force
\[
(k_1,\ldots,k_{10})=(2^4,3^6),\qquad c_U=22,\qquad c_W=4.
\]
All capacities are saturated:
\[
e(\overline{H[W]})=96,
\]
so again \(H[W]=4K_4\) and \(\overline{H[W]}=K_{4,4,4,4}\). The ninth exact color contributes four disjoint W-edges (one from each \(k=2\) component); the two nonexact colors each contribute a four-edge matching. Therefore the same exact kernel (7) appears:
\[
\boxed{2K_4+24K_3+3M_4.}\tag{14}
\]

## 3. Updated exact-color frontier

Combining this theorem with the prior \(m=10\) exclusion and \(h=4\) orthogonal-array obstruction gives
\[
\boxed{m\in\{8,9\}.}
\]
More precisely:
- \(m=8\): \(h\le2\); if \(h=2\), the exact kernel (7) is forced.
- \(m=9\): \(h\in\{1,2\}\) and \(\delta\ge14\); if \(h=2,\delta=14\), the exact same kernel (14) is forced.

The next structural input must act on this kernel or on the remaining \(m=8,h\le1\) and \(m=9,h\in\{1,2\},\delta\ge14\) branches. Pure scalar edge capacity is now exhausted.