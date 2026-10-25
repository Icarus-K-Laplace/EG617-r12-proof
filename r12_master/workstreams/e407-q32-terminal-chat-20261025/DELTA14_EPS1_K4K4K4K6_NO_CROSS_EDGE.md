# E407 Q32: exclude the \(\delta=14,\epsilon_U=1\), no-cross-edge \(K_4^3\cup K_6\) profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite \(U\)-complement contract, and the second-Turán W-profile classification.

## 1. Contract

Assume the 47-vertex core contract
\[
e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}(d_H(v)-12)=4,
\]
with \(|U|=29, |W|=18\), \(\epsilon_U=1\), \(\delta=14\), and four-partite \(L=\overline{H[U]}\) with parts \(A,B,C,D\) of sizes \(7,7,7,8\). There are seven \(H[U]\) cross-edges between \(D\) and distinct small-part vertices. Put \(t_d=|N_H(d)\cap(A\cup B\cup C)|\); then \(\sum_{d\in D}t_d=7\) and
\[
d_H(d,W)=5-t_d+\epsilon_d,\qquad \epsilon_d\le1.
\]
The exact ledger gives \(e(H[W])=33\). Consider
\[
H[W]=C_1\dot\cup C_2\dot\cup C_3\dot\cup C_6,
\qquad C_i\cong K_4\ (i=1,2,3),\quad C_6\cong K_6,
\]
with no W-cross-edges. The W-side excess is \(\sum_{w\in W}\epsilon_w=3\).

## 2. D-vertices are assigned uniquely to W-components

Because the four W-components are pairwise anticomplete and \(\alpha(H)\le4\), every \(d\in D\) is complete to at least one W-component: otherwise a non-neighbour from each component together with \(d\) would be an independent 5-set. A vertex \(d\in D\) has W-degree at most \(5+\epsilon_d\le6\), while two W-components have at least \(4+4=8\) vertices. Hence it is complete to exactly one component.

Let \(q\in\{0,1\}\) be the number of D-vertices assigned to \(K_6\). If \(d\) is assigned to \(K_6\), then \(d_H(d,W)\ge6\), forcing \(\epsilon_d=1,t_d=0\); therefore \(q\le1\), and if \(q=1\), the unique such vertex uses the entire U-excess.

If \(d\) is assigned to a \(K_4\), then \(d_H(d,W)\ge4\), so \(t_d\le1+\epsilon_d\le2\). If assigned to \(K_6\), then \(t_d\le\epsilon_d-1=0\). In particular, \(t_d\le2\) for all \(d\in D\).

Let \(R\) count all D-to-W edges going outside the unique W-component to which their D endpoint is assigned. A D-vertex assigned to a \(K_4\) contributes \(d_H(d,W)-4=1-t_d+\epsilon_d\); one assigned to \(K_6\) contributes \(d_H(d,W)-6=-1-t_d+\epsilon_d\). Therefore the exact identity is
\[
\boxed{R=1-2q+\sum_{d\in D}\epsilon_d.} \tag{1}
\]
If \(q=0\), then \(\sum_D\epsilon_d\le1\), so \(R\le2\). If \(q=1\), then \(\sum_D\epsilon_d=1\), so \(R=0\).

## 3. A K4 component cannot receive three D assignments

Fix a \(K_4\) component \(C\), and let \(k\) be the number of D-vertices assigned to \(C\). Every such D-vertex is adjacent to all four vertices of \(C\).

Let \(m\) be the number of vertices \(w\in C\) that are complete to all of \(D\). For each such \(w\), all \(8-k\) D-vertices assigned to other W-components must use an extra D-to-W edge to \(w\). Thus
\[
m(8-k)\le R\le2. \tag{2}
\]
If \(k=8\), every D-vertex is assigned to \(C\), so \(C\cup D\) is a forbidden \(K_{12}\). Suppose \(3\le k\le7\). Equation (2) gives the following upper bounds on \(m\):
\[
\begin{array}{c|ccccc}
k&3&4&5&6&7\\\hline
m\le&0&0&0&1&2\\
4-m\ge&4&4&4&3&2
\end{array}
\]
Hence at least \(4,4,4,3,2\) vertices of \(C\), respectively, are not complete to \(D\).

We claim each such vertex \(w\) has \(\epsilon_w\ge k-2\). First, \(w\) cannot fail to be complete to every U-part. Indeed, with \(t_d\le2\), the usual transversal argument gives \(d_H(w,U)\ge12\) for a W-vertex not complete to a U-part, whereas \(d_H(w,U)=9+\epsilon_w\le12\). If such a vertex had \(\epsilon_w=3\), it would consume all W-excess; another vertex of \(C\) not complete to \(D\) would then have excess zero and U-degree 9, too small both to be U-part-saturated (it needs at least \(7+k\ge10\) neighbours) and to satisfy the unsaturated lower bound 12. Thus every vertex of \(C\) not complete to \(D\) is complete to a small U-part of size 7. It already has \(k\) neighbours in \(D\), so
\[
9+\epsilon_w=d_H(w,U)\ge7+k,
\quad\text{and therefore}\quad
\epsilon_w\ge k-2. \tag{3}
\]

Combining the lower row above with (3), the W-excess required by \(C\) is at least
\[
\begin{array}{c|ccccc}
k&3&4&5&6&7\\\hline
(4-m)(k-2)&4&8&12&12&10
\end{array}
\]
Every entry exceeds the available W-excess \(3\). Thus no \(K_4\) component can receive \(k\ge3\) D-assignments.

But if \(q=0\), all eight D-vertices are assigned among three \(K_4\) components; if \(q=1\), seven are. Since each \(K_4\) can receive at most two, these components can receive at most six D-vertices in total. Contradiction in both cases.

Therefore the \(\delta=14,\epsilon_U=1\), four-partite W-profile \(K_4^3\cup K_6\) with no W-cross-edge is **excluded** under the retained contracts. This is one profile only; the \((4,4,5,5)\)+one-cross-edge profile and the remaining \(\epsilon_U=1\) branches remain open.
