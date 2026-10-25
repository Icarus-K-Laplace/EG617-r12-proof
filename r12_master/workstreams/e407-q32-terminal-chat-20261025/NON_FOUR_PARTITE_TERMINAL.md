# E407 Q32 — non-four-partite and near-extremal residuals

Date: 2026-10-25  
Status: **OPEN**, with exact numerical reductions below.

## 1. Non-four-partite \(L=\overline{H[U]}\)

On the 29-point, 49-witness boundary,
\[
e(L)=294+\delta,\qquad 3\le\delta\le16,\qquad
\delta+\epsilon_U\le16.
\]
The graph \(L\) is \(K_5\)-free. Brouwer's second-Turán bound says that a non-four-partite \(K_5\)-free graph on 29 vertices has at most
\[
t_4(29)-\lfloor29/4\rfloor+1=315-7+1=309
\]
edges. Therefore:
- \(\delta=16\) is automatically four-partite;
- the non-four-partite branch can occur only for \(\delta\le15\);
- at \(\delta=15\), the non-four-partite case is the exact second-Turán boundary \(e(L)=309\), and cannot be discarded by the edge count alone;
- \(\delta\le14\) remains below that threshold.

The \(\delta=15\) non-four-partite branch is now excluded by DELTA15_SECOND_TURAN_PACKING.md, using the Kang–Pikhurko equality classification and incompatible \(x,y\) degrees into \(W\). The \(\delta\le14\) non-four-partite branch remains OPEN. The five regular-\(K_{11}\) templates must be combined with their labelled witness system, not replaced by the scalar edge count.

## 2. If \(L\) is four-partite and \(\delta\in\{14,15,16\}\)

The part sizes on \(U\) are forced to \(7,7,7,8\). The exact ledger gives
\[
e(H[W])=48-\epsilon_U-\delta=32+c,\qquad
c=16-\epsilon_U-\delta\in\{0,1,2\}.
\]
The complement \(\overline{H[W]}\) is \(K_5\)-free and has at least 119 edges, so Brouwer's second-Turán bound on 18 vertices (at most 118 edges for a non-four-partite \(K_5\)-free graph) forces \(\overline{H[W]}\) to be four-partite.

The four part sizes of \(\overline{H[W]}\), equivalently the clique sizes of the within-part subgraphs of \(H[W]\), must be one of
\[
(4,4,5,5),\ (3,5,5,5),\ (4,4,4,6),\ (3,4,5,6),
\]
because their within-part edge count is at most \(e(H[W])\le34\). The number of \(H[W]\) edges between these four clique parts is \(e(H[W])-\sum_i\binom{n_i}{2}\), hence at most two. The exact allowed profiles are:

| \(\delta\) | \(\epsilon_U\) | \(e(H[W])\) | Allowed clique-part sizes | Cross edges between \(W\)-parts |
|---:|---:|---:|---|---:|
| 14 | 0 | 34 | (4,4,5,5), (3,5,5,5), (4,4,4,6), (3,4,5,6) | 2, 1, 1, 0 respectively |
| 14 | 1 | 33 | (4,4,5,5), (3,5,5,5), (4,4,4,6) | 1, 0, 0 respectively |
| 14 | 2 | 32 | (4,4,5,5) | 0 |
| 15 | 0 | 33 | (4,4,5,5), (3,5,5,5), (4,4,4,6) | 1, 0, 0 respectively |
| 15 | 1 | 32 | (4,4,5,5) | 0 |
| 16 | 0 | 32 | (4,4,5,5) | 0 |

For \(\delta=16\), FOUR_PARTITE_TERMINAL.md excludes all three endpoint splits; the \(5+0\) case forces a forbidden \(K_{12}\). For \(\delta=14,15\), the remaining \(W\)-part profiles are not yet reconciled with the five shell templates.

## 3. Next minimal obstacle

The next nontrivial step is an adjacency-sensitive theorem that links:
- the five template-specific shell row profiles and their three hub-neighbourhoods;
- the 49-block linear design on \(U\);
- the at-most-two cross edges between the near-Turán clique parts of \(H[W]\).

A bare count of edges or witness incidences does not establish incompatibility.

**Update (2026-10-25):** At \(\delta=14,\epsilon_U=0\), the cover-capacity proof in DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md excludes the \((3,4,5,6)\) profile with zero W-cross-edges. DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md excludes \((4,4,5,5)\) with two cross edges and \((4,4,4,6)\) with one cross edge. Thus only \((3,5,5,5)\) with one cross edge remains in this \(\epsilon_U=0\) four-partite row. The \(\epsilon_U=1,2\) rows and the \(\delta=14\) non-four-partite branch remain OPEN.


**Update (2026-10-25, Round 10):** The remaining \(\delta=14,\epsilon_U=0\) profile \((3,5,5,5)\) with one W-cross-edge is further split by endpoint placement. DELTA14_EPS0_K3K5X1_K5K5_EDGE.md excludes the placement joining two \(K_5\) parts by a 29-point cover versus a 27-point capacity bound. Only the placement joining the \(K_3\) to a \(K_5\) remains OPEN.


**Update (2026-10-25, Round 11):** DELTA14_EPS0_K3K5X1_K3K5_EDGE.md excludes the last \((3,5,5,5)\) profile with a cross-edge between \(K_3\) and \(K_5\). Combined with the three earlier exclusions, **all four-partite W profiles at \(\delta=14,\epsilon_U=0\) are excluded**. The \(\epsilon_U=1,2\) and \(\delta=14\) non-four-partite cases remain OPEN.


**Update (2026-10-25, Round 12):** DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md excludes the no-cross-edge profiles \(K_3\cup K_5^3\) for \(\epsilon_U=1,2\), \(K_4^3\cup K_6\) for \(\epsilon_U=1\), and \(K_4\cup K_4\cup K_5\cup K_5\) for \(\epsilon_U=2\). Thus the only \(\delta=14\) four-partite W-profile still open is \(\epsilon_U=1\), \(K_4\cup K_4\cup K_5\cup K_5\) plus one W-cross-edge.
