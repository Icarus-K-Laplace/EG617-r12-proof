# E407 Q32: exclude the \(\delta=14,\epsilon_U=1\), no-cross-edge \(K_3\cup K_5^3\) profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite \(U\)-complement contract, and the second-Turán W-profile classification.

## 1. Contract

Assume
\[
e(H)=284,\quad |U|=29,\quad |W|=18,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}(d_H(v)-12)=4.
\]
Let \(\epsilon_v=d_H(v)-12\), with \(\epsilon_U=1\), and suppose \(\delta=14\) and \(L=\overline{H[U]}\) is four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). The seven cross-edges in \(H[U]\) join \(D\) to seven distinct small-part vertices. For \(d\in D\), write \(t_d=|N_H(d)\cap(A\cup B\cup C)|\), so
\[
d_H(d,W)=5-t_d+\epsilon_d.
\]
The exact core ledger gives \(e(H[W])=33\). This profile is
\[
H[W]=C_0\dot\cup C_1\dot\cup C_2\dot\cup C_3,
\qquad C_0\cong K_3,\quad C_i\cong K_5\ (i=1,2,3),
\]
with no edges between the four components. Let \(E_i=\sum_{w\in C_i}\epsilon_w\); then
\[
E_0+E_1+E_2+E_3=3.
\]

For each component define its common-neighbour set
\[
S_i=\{u\in U:\ u\text{ is adjacent to every vertex of }C_i\}.
\]

## 2. Every U-vertex is saturated to a W-component

If \(u\in U\) were not complete to any \(C_i\), choose one non-neighbour from each of the four pairwise anticomplete clique components. Those four vertices together with \(u\) would form an independent 5-set, contrary to \(\alpha(H)\le4\). Therefore
\[
\boxed{U=S_0\cup S_1\cup S_2\cup S_3,\qquad
29\le\sum_{i=0}^3|S_i|.} \tag{1}
\]
The same argument applies to each \(d\in D\): it is complete to a W-component of size at least three. Hence \(5-t_d+\epsilon_d\ge3\), so
\[
t_d\le2+\epsilon_d\le3, \tag{2}
\]
because \(\epsilon_d\le\epsilon_U=1\).

## 3. Reverse-saturation bound for W-vertices

We claim that if \(w\in W\) is not complete to any of \(A,B,C,D\), then
\[
d_H(w,U)\ge11. \tag{3}
\]
Let \(D'=\{d\in D:wd\notin E(H)\}\), and let \(A',B',C'\) be the non-neighbour sets of \(w\) in the three small parts. If \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain an H-edge to \(d\), or that triple together with \(w,d\) is an independent 5-set. Thus one of \(A',B',C'\) is contained in \(N_H(d)\cap(A\cup B\cup C)\), so has size at most \(t_d\le3\). Distinct vertices of \(D'\) require distinct small parts, since every small-part vertex is incident to at most one cross-edge in \(H[U]\). Consequently \(|D'|\le3\). The number of non-neighbours in \(U\) is at most:
- \(1+3+7+7=18\) if \(|D'|=1\);
- \(2+3+3+7=15\) if \(|D'|=2\);
- \(3+3+3+3=12\) if \(|D'|=3\).

Thus \(d_H(w,U)\ge29-18=11\), proving (3).

## 4. K5 common-neighbour capacity

Fix \(i\in\{1,2,3\}\). Every \(w\in C_i\) has \(d_H(w,U)=8+\epsilon_w\), because there are no W-cross-edges. If some \(w\in C_i\) is not complete to a U-part, (3) implies \(8+\epsilon_w\ge11\), so \(\epsilon_w=3\). Since the total W-excess is three, every other vertex of \(C_i\) has excess zero and U-degree 8. Therefore \(|S_i|\le8=5+E_i\).

Otherwise label each \(w\in C_i\) by a U-part \(P(w)\) to which it is complete. Its number of U-edges outside that part is at most \(1+\epsilon_w\). All five vertices cannot receive the same label: a common label of size 7 would create a \(K_{12}\), and a common label \(D\) of size 8 would create a \(K_{13}\). For each \(u\in S_i\), at least one edge \(uw\) therefore lies outside the label part of \(w\). Distinct \(u\)'s consume distinct such edges, so
\[
\boxed{|S_i|\le\sum_{w\in C_i}(1+\epsilon_w)=5+E_i.} \tag{4}
\]

## 5. K3 common-neighbour capacity and contradiction

Every \(w\in C_0\) has \(d_H(w,U)=10+\epsilon_w\). Since \(S_0\subseteq N_H(w)\cap U\) for every \(w\in C_0\),
\[
|S_0|\le10+\min_{w\in C_0}\epsilon_w
\le10+\left\lfloor\frac{E_0}{3}\right\rfloor. \tag{5}
\]
Combining (1), (4), and (5),
\[
\begin{aligned}
29
&\le\sum_{i=0}^3|S_i|\\
&\le10+\left\lfloor\frac{E_0}{3}\right\rfloor
 +(5+E_1)+(5+E_2)+(5+E_3)\\
&=28-E_0+\left\lfloor\frac{E_0}{3}\right\rfloor\\
&\le28,
\end{aligned}
\]
because \(E_0\in\{0,1,2,3\}\). Contradiction.

Therefore the \(\delta=14,\epsilon_U=1\), four-partite W-profile \(K_3\cup K_5^3\) with no W-cross-edge is **excluded** under the retained contracts. This does not close the other \(\delta=14,\epsilon_U=1\) W-profiles, \(\epsilon_U=2\), the \(\delta=14\) non-four-partite branch, \(\delta\le13\), any full V12 template, or E407 Q32 / EG617(r=12) overall.
