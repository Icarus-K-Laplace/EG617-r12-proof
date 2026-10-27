# Q33 global capacity theorem: exclude ten exact-129 colors

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the registered T61 shell-label theorem, exact-129 Type-I factor theorem, and 31-point/56-witness minimum-support contract.  
Conclusion: the number \(m\) of exact-129 non-target colors cannot be 10; hence \(m\in\{8,9\}\). If \(m=9\), at least one of the 56 selected witnesses must be a gadget witness.

## 1. Frozen contract and notation

Use only the Q33 284-edge contract:
\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad\omega(H)\le11,\quad
d_H(v)=12+\epsilon_v,\quad \sum_{v\in H}\epsilon_v=4.
\]
Let \(U\subset H\) be the 31-point support of the 56 selected independent four-sets, and \(W=H\setminus U\), so \(|W|=16\). Put
\[
L=\overline{H[U]},\qquad e(L)=336+\delta,\qquad
\epsilon_U=\sum_{u\in U}\epsilon_u.
\]
The retained core ledger gives
\[
e(H[W])=41-\delta-\epsilon_U\ge24,\qquad
\delta+\epsilon_U\le17.
\]
In particular,
\[
e(\overline{H[W]})=120-e(H[W])=79+\delta+\epsilon_U\le96. \tag{1}
\]

There are \(m\in\{8,9,10\}\) exact-129 colors. For every such color \(C\), the retained factor theorem partitions its 61-point residual into ten isolated \(C\)-colored \(K_5\) components and an 11-vertex exceptional gadget. Each component has exactly one shell vertex and four core vertices, giving ten disjoint four-sets
\[
Q_{C,1},\ldots,Q_{C,10}\subset H.
\]
Write \(G_C=U_C\cap H\) for the seven core vertices in the exceptional gadget, and \(A_C=H\setminus G_C\) for the 40 core vertices in the ten components. Each \(Q_{C,\ell}\) is a \(K_4\) in \(\overline H\). All component-witness edge sets across all exact colors are pairwise edge-disjoint, because each such \(K_4\) is monochromatic in its own non-target color.

The 56 selected witnesses are seven labelled four-sets from each of eight selected exact-129 colors. Let \(h\) be the number of those 56 witnesses that lie in the exceptional gadget rather than among the ten isolated components. The retained shell-label theorem says at most one selected witness per selected color is a gadget witness, so \(0\le h\le8\).

## 2. The selected colors force at least \(72+6h\) edges in \(\overline{H[W]}\)

Fix one of the eight selected colors \(C\).

### Case 1: all seven selected witnesses are component witnesses

They are seven of the ten disjoint component four-sets and cover 28 points of \(U\). The other three component four-sets are disjoint from those 28 points. Since \(|U|=31\), each of the other three component sets has at most one vertex in \(U\), and therefore at least three vertices in \(W\). Each contributes at least \(\binom32=3\) distinct edges to \(\overline{H[W]}\). Thus this color contributes at least 9 such edges from its three unselected components.

### Case 2: one selected witness is a gadget witness

Six selected component witnesses cover 24 points of \(U\). The selected gadget witness is a four-set inside \(G_C\), hence disjoint from all ten component four-sets; it covers four further points of \(U\). Only three points of \(U\) remain. Consequently the four unselected component four-sets each have at most one vertex in \(U\), and their total number of \(U\)-incidences is at most three. At least one of the four sets is wholly in \(W\), contributing six edges to \(\overline{H[W]}\); each of the other three contributes at least three. Thus this color contributes at least \(6+3+3+3=15\) edges.

These contributions are edge-disjoint across all colors: every edge inside a component four-set has the component's color, so no pair can occur in two different component witnesses. Summing over the eight selected colors gives
\[
e(\overline{H[W]})\ge 9(8-h)+15h=72+6h.
\]
Together with (1),
\[
72+6h\le96,\qquad\boxed{h\le4}. \tag{2}
\]

## 3. A capacity inequality for unselected component witnesses

Let \(D\) be an exact-129 color that is **not** one of the eight selected witness colors. For its ten component four-sets define
\[
k_{D,\ell}=|Q_{D,\ell}\cap U|\in\{0,1,2,3,4\}.
\]
Because \(A_D\) has 40 core vertices and \(G_D\) has seven,
\[
\sum_{\ell=1}^{10}k_{D,\ell}
=|A_D\cap U|
=31-|G_D\cap U|
\ge24. \tag{3}
\]

For any component four-set, the \(\binom{k_{D,\ell}}2\) pairs in \(Q_{D,\ell}\cap U\) are edges of \(L\). The component four-sets of the unselected colors are edge-disjoint from each other and from selected component witnesses of the other colors. Such an edge can overlap a selected witness edge only if the selected witness is one of the \(h\) gadget witnesses.

For a gadget witness \(Q\subset G_C\), the retained factor theorem gives \(\alpha(C[U_C])\le2\), so \(\overline{C[Q]}\) is triangle-free. A triangle-free graph on four vertices has at most four edges. Every edge of an unselected exact color inside \(Q\) belongs to \(\overline{C[Q]}\), so at most four of the six edges of \(Q\) can overlap component edges of all unselected colors combined. Therefore the total overlap with the 56 selected witness edges is at most \(4h\).

All remaining such \(L\)-edges lie among the \(\delta\) edges of \(L\) not used by the 56 selected witness \(K_4\)'s. Hence, across all component four-sets of the unselected exact colors,
\[
\boxed{\sum_{D,\ell}\binom{k_{D,\ell}}2\le\delta+4h.} \tag{4}
\]

The integer capacity inequality
\[
\boxed{k\le \frac32+\frac12\binom{k}{2}\qquad(k=0,1,2,3,4)} \tag{5}
\]
is checked directly for all five possible values.

## 4. Exclusion of \(m=10\)

If \(m=10\), there are exactly two exact-129 colors outside the selected eight. They supply 20 component four-sets. By (3),
\[
\sum_{D,\ell}k_{D,\ell}\ge48.
\]
But by (2), (4), \(\delta\le17\), and \(h\le4\),
\[
\sum_{D,\ell}\binom{k_{D,\ell}}2
\le\delta+4h\le17+16=33.
\]
Applying (5) to the 20 values gives
\[
\sum_{D,\ell}k_{D,\ell}
\le 20\cdot\frac32+\frac12\cdot33
=46.5.
\]
The left side is an integer, so it is at most 46, contradicting the lower bound 48. Therefore
\[
\boxed{m\ne10.}
\]

## 5. Corollary: if \(m=9\), then \(h\ge1\)

If \(m=9\) but \(h=0\), there is one unselected exact color with ten component four-sets. By (3) their total \(k\)-sum is at least 24, while (4) gives total cost at most \(\delta\le17\). Inequality (5) yields
\[
\sum_{\ell=1}^{10}k_{D,\ell}
\le10\cdot\frac32+\frac12\cdot17=23.5,
\]
so the integer sum is at most 23, contradiction. Thus \(m=9\Rightarrow h\ge1\).

Combining with (2), the full conditional result is:
\[
\boxed{m\in\{8,9\},\qquad h\le4,\qquad m=9\Rightarrow1\le h\le4.}
\]


## 6. Quantitative frontier for the remaining \(m=9\) branch

For the one exact color outside the selected eight, (3) requires \(\sum_{\ell=1}^{10} k_\ell\ge24\). Inequality (5) then gives the sharper lower bound
\[
\sum_{\ell=1}^{10}\binom{k_\ell}{2}\ge18.
\]
Together with (4),
\[
\delta\ge18-4h.
\]
Since \(h=4\) is excluded in Section 7 below, the remaining \(m=9\) possibilities satisfy:

| \(h\) | lower bound on \(\delta\) |
|---:|---:|
| 1 | 14 |
| 2 | 10 |
| 3 | 6 |

## 7. The endpoint \(h=4\) is impossible: an orthogonal-array obstruction

Suppose \(h=4\). Section 2 gives
\[
e(\overline{H[W]})\ge72+6h=96,
\]
while (1) gives the reverse inequality. Hence equality holds:
\[
e(\overline{H[W]})=96,\quad e(H[W])=24,\quad
\delta+\epsilon_U=17.
\]
Equality in the 16-vertex Turán bound forces \(H[W]\) to be the disjoint union of four \(K_4\)'s, so \(\overline{H[W]}=K_{4,4,4,4}\).

All selected-color contributions to \(\overline{H[W]}\) must be tight. The four selected colors with a gadget witness each contribute one unselected component \(K_4\) wholly in \(W\) and three component triangles in \(W\). The other four selected colors each contribute three component triangles in \(W\). Thus four \(K_4\)'s and 24 triangles, all edge-disjoint, partition every edge of \(K_{4,4,4,4}\).

Let \(q_w\) be the number of these four \(K_4\)'s containing \(w\in W\), and \(t_w\) the number of the 24 triangles containing it. Since \(K_{4,4,4,4}\) has degree 12 at every vertex and the decomposition is edge-disjoint,
\[
3q_w+2t_w=12,
\]
so \(q_w\) is even. In each of the four parts, the four \(K_4\)'s contribute exactly four vertex incidences, hence the four \(q_w\)-values in that part sum to four. If some vertex had \(q_w=4\), all four \(K_4\)'s would contain it; edge-disjointness would force them to use four distinct vertices in each other part, giving those vertices \(q=1\), contradiction. Therefore every part has exactly two vertices with \(q=2\) and two with \(q=0\).

Restrict each part to its two \(q=2\) vertices and encode the four \(K_4\)'s as four binary rows, one coordinate per part. Every column is balanced (each of its two vertices occurs twice). For any two parts, edge-disjointness forces the four \(K_4\)'s to use all four possible pairs of selected vertices exactly once. Thus the four columns would form an orthogonal array \(OA(4,4,2,2)\).

No such array exists. After ordering the rows so the first two columns are the four binary pairs \((x,y)\in\{0,1\}^2\), a balanced third column orthogonal to both must be \(x\oplus y\) or its complement. The fourth column must likewise be one of these two, so it equals or complements the third and cannot be orthogonal to it. Contradiction.

Therefore
\[
\boxed{h\le3.}
\]
Combining with Section 5, the final capacity frontier is
\[
\boxed{m\in\{8,9\},\quad h\le3,\quad m=9\Rightarrow1\le h\le3.}
\]
The \(m=9\) branch consequently has \(\delta\ge14,10,6\) for \(h=1,2,3\), respectively. This closes the \(h=4\) terminal but does not close the remaining \(m=8,9\) branches.

## 8. Proof scope and dependencies

This is a Q33-only theorem. It uses the 284-edge core, the 31-point/56-witness support, the exact-129 component factorization, and the shell-label fact that each component contributes a four-point core witness while each gadget contributes seven core vertices. It does not use the Q32 285-edge/excess-six contract.

The conclusion removes the \(m=10\) branch from the Q33 global incidence search. It does **not** close \(m=8\) or \(m=9\), either remaining all-component-edge-present \(P_C=49\) profile, E408 Q33, or the original \(K_{145}\) theorem. Those remain **OPEN / NOT_CERTIFIED**.
