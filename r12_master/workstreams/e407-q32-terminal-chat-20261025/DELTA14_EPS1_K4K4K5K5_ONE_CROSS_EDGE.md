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

## 2. Saturation and the exceptional D-vertex case

A D-vertex has
\[
d_H(d,W)=5+\epsilon_d-t_d\le6,
\]
because \(\epsilon_d\le\epsilon_U=1\). If it is not complete to any W-clique component, an independent transversal can be blocked only by choosing the two endpoints of the unique W-cross-edge. To block every transversal, its non-neighbour sets in the two endpoint components must be exactly those endpoints, so it must be adjacent to all other vertices in those two components. This requires at least \(3+3=6\) W-neighbours, and equality is possible only when the cross-edge joins the two \(K_4\) components. Thus any exceptional D-vertex must have
\[
\epsilon_d=1,\qquad t_d=0,\qquad d_H(d,W)=6,
\]
with W-neighbourhood consisting of the three non-endpoint vertices in each \(K_4\) and no vertices of either \(K_5\). There can be at most one such vertex because \(\epsilon_U=1\).

We first rule out this exceptional case. The other seven D-vertices have zero excess and must be complete to a W-component. Each has \(t_d\le1\); since the seven cross-edges of \(H[U]\) have total cross-degree seven, all seven have \(t_d=1\), and each is assigned to a \(K_4\) component. One \(K_4\), call it \(C\), receives \(k\ge4\) of these D-vertices. The exceptional vertex is adjacent to the three non-endpoint vertices of \(C\), so each non-endpoint vertex of \(C\) has at least \(k+1\) D-neighbours; the cross-edge endpoint has at least \(k\).

Here \(t_d\le1\) for all \(d\). Repeating the reverse-saturation count from Section 3 with \(t_d\le1\) gives at least 13 U-neighbours for any W-vertex not complete to a U-part (and a stronger bound if \(|D'|\ge2\)); a \(K_4\)-vertex has U-degree at most 12. Thus every vertex \(w\in C\) is complete to a U-part. If \(k=7\), the cross-edge endpoint of \(C\) is not complete to \(D\) and would need at least \(7+k=14\) U-neighbours from a small U-part plus its D-neighbours, while its U-degree is at most 11; contradiction. For \(k=4,5,6\), no vertex of \(C\) is complete to \(D\), so every vertex of \(C\) is complete to a small U-part. A non-endpoint \(w\in C\) therefore satisfies
\[
9+\epsilon_w=d_H(w,U)\ge7+(k+1),
\]
and the cross-edge endpoint satisfies
\[
8+\epsilon_w=d_H(w,U)\ge7+k.
\]
In both cases \(\epsilon_w\ge k-1\ge3\). All four vertices of \(C\) would consume at least 12 W-excess units, contradicting the total W-excess three. The exceptional case is impossible.

Consequently every D-vertex is complete to a unique W-component. Let \(q_5\) be the number assigned to a \(K_5\). A D-vertex assigned to a \(K_4\) has \(t_d\le1+\epsilon_d\); one assigned to a \(K_5\) has \(t_d\le\epsilon_d\). Hence
\[
7=\sum_D t_d\le (8-q_5)+\sum_D\epsilon_d\le8-q_5+1,
\]
so \(q_5\le2\). At least six D-vertices are assigned to the two \(K_4\) components, and some \(K_4\) receives \(k\ge3\) assignments.

Let \(R\) count all D-to-W edges whose W endpoint lies outside the component assigned to that D vertex. A D-vertex assigned to a \(K_4\) contributes \(1+\epsilon_d-t_d\), and one assigned to a \(K_5\) contributes \(\epsilon_d-t_d\). Therefore
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
