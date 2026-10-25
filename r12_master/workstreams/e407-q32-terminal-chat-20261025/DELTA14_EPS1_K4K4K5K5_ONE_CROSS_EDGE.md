# E407 Q32: exclude the \(\delta=14,\epsilon_U=1\), \((4,4,5,5)\)+one-cross-edge W-profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite \(U\)-complement contract, and the stated W-profile hypothesis.

## 1. Contract

Assume
\[
e(H)=284,\quad |U|=29,\quad |W|=18,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}(d_H(v)-12)=4,
\]
with \(\epsilon_U=1,\delta=14\), and \(L=\overline{H[U]}\) four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). The seven H-edges crossing U-parts join \(D\) to seven distinct small-part vertices. For \(d\in D\), let \(t_d=|N_H(d)\cap(A\cup B\cup C)|\), so \(\sum t_d=7\) and
\[
d_H(d,W)=5-t_d+\epsilon_d,\qquad \epsilon_d\le1.
\]
The W-side excess is three. Suppose \(H[W]\) consists of two clique components \(C_4^{(1)},C_4^{(2)}\cong K_4\) and two \(K_5\) components, plus one edge \(xy\) between two distinct components. This is the \((4,4,5,5)\)+one-cross-edge profile.

## 2. D-component assignments and exact external incidence

Because \(\alpha(H)\le4\), every \(d\in D\) is complete to at least one W-component; otherwise one non-neighbour from each of the four pairwise anticomplete components, together with \(d\), forms an independent 5-set. A D-vertex has W-degree at most \(5+\epsilon_d\le6\), while two components contain at least \(4+4=8\) vertices, so its assigned component is unique.

Let \(q_5\) be the number of D-vertices assigned to a \(K_5\). If assigned to a \(K_4\), then \(d_H(d,W)\ge4\), so \(t_d\le1+\epsilon_d\); if assigned to a \(K_5\), then \(t_d\le\epsilon_d\). Thus
\[
7=\sum_D t_d\le (8-q_5)+\sum_D\epsilon_d\le8-q_5+1,
\]
so \(q_5\le2\). At least six D-vertices are therefore assigned to the two \(K_4\) components, and some \(K_4\) component \(C\) receives \(k\ge3\) assignments.

Let \(R\) count all D-to-W edges whose W endpoint lies outside the component assigned to that D vertex. A D vertex assigned to a \(K_4\) contributes \(1-t_d+\epsilon_d\), and one assigned to a \(K_5\) contributes \(\epsilon_d-t_d\). Hence
\[
\boxed{R=1-q_5+\sum_{d\in D}\epsilon_d\le2.} \tag{1}
\]

## 3. The heavily assigned \(K_4\) forces excess beyond the budget

Fix a \(K_4\) component \(C\) receiving \(k\ge3\) D assignments. Each of those \(k\) D vertices is adjacent to every vertex of \(C\). Let \(m\) be the number of vertices \(w\in C\) complete to all of \(D\). For each such \(w\), all \(8-k\) D vertices assigned to other W-components must use an external D-to-W edge to \(w\). Therefore
\[
m(8-k)\le R\le2. \tag{2}
\]
If \(k=8\), all D vertices are assigned to \(C\), so \(C\cup D\) is a forbidden \(K_{12}\). For \(k=3,4,5,6,7\), (2) gives
\[
\begin{array}{c|ccccc}
k&3&4&5&6&7\\\hline
m\le&0&0&0&1&2\\
4-m\ge&4&4&4&3&2
\end{array}
\]
Thus at least \(4,4,4,3,2\) vertices of \(C\), respectively, are not complete to \(D\).

We claim each vertex \(w\in C\) not complete to \(D\) must be complete to a small U-part, and therefore
\[
\epsilon_w\ge k-2. \tag{3}
\]
First, \(t_d\le2\) for every \(d\in D\). A W-vertex not complete to any U-part has \(d_H(w,U)\ge12\): with \(D'=\{d:wd\notin E(H)\}\), each \(d\in D'\) forces one of the small-part non-neighbour sets to have size at most \(t_d\le2\); distinct \(d\)'s use distinct small parts. The non-neighbour counts for \(|D'|=1,2,3\) are at most \(17,13,9\), respectively, so \(d_H(w,U)\ge12\).

If a vertex \(w\in C\) not complete to \(D\) were not complete to any U-part, its U-degree would be at least 12. A non-endpoint of the W-cross-edge has \(d_H(w,U)=9+\epsilon_w\), so this forces \(\epsilon_w=3\); an endpoint has U-degree \(8+\epsilon_w\le11\), so cannot be unsaturated. In the former case \(\epsilon_w=3\) exhausts the W-excess. But (2) guarantees at least one other vertex of \(C\) not complete to \(D\); that vertex has excess zero and U-degree 8 or 9, too small both to be complete to a small U-part (which needs at least \(7+k\ge10\) U-neighbours) and to be unsaturated (which needs degree at least 12). Contradiction. Hence every vertex of \(C\) not complete to \(D\) is complete to a small U-part of size 7. Its U-degree is at least \(7+k\); since its degree into U is \(9+\epsilon_w\) if it is not a W-cross-edge endpoint and \(8+\epsilon_w\) if it is, (3) follows (with a stronger bound for an endpoint).

The W-excess required by the non-D-complete vertices is therefore at least
\[
\begin{array}{c|ccccc}
k&3&4&5&6&7\\\hline
(4-m)(k-2)&4&8&12&12&10
\end{array}
\]
Every entry exceeds the total W-excess \(3\). This contradiction shows no \(K_4\) can receive \(k\ge3\) D assignments.

But at least six D vertices are assigned to the two \(K_4\) components, so one of them must receive at least three. Contradiction.

Therefore the \(\delta=14,\epsilon_U=1\), four-partite W-profile \((4,4,5,5)\) plus one cross-edge is **excluded** under the retained contracts. This closes all three listed \(e(H[W])=33\) W-profile types in the \(\epsilon_U=1\), four-partite row, provided the registered second-Turán profile classification is exhaustive. It does not close \(\epsilon_U=2\), non-four-partite \(\delta=14\), \(\delta\le13\), any full V12 template, or E407 Q32 / EG617(r=12) overall.
