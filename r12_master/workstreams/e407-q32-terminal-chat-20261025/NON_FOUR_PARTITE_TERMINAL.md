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

For \(\delta=16\), FOUR_PARTITE_TERMINAL.md forces the exact \(H[W]=K_5\cup K_5\cup K_4\cup K_4\) structure and excludes the \(4+1\) and \(3+2\) endpoint splits, but the \(5+0\) labelled kernel remains OPEN. For \(\delta=14,15\), the remaining \(W\)-part profiles are not yet reconciled with the five shell templates.

## 3. Next minimal obstacle

The next nontrivial step is an adjacency-sensitive theorem that links:
- the five template-specific shell row profiles and their three hub-neighbourhoods;
- the 49-block linear design on \(U\);
- the at-most-two cross edges between the near-Turán clique parts of \(H[W]\).

A bare count of edges or witness incidences does not establish incompatibility.
