# E407 Q32: exclude the remaining \(\delta=14,\epsilon_U=0\) four-partite W-profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite \(U\)-complement contract, and the second-Turán W-profile classification.

## 1. Contract

Let \(H\) be the 47-vertex core with
\[
e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}(d_H(v)-12)=4.
\]
Let \(U\subset V(H)\) have size 29, \(W=V(H)\setminus U\) have size 18, and put
\[
\epsilon_v=d_H(v)-12,\qquad \epsilon_U=\sum_{u\in U}\epsilon_u.
\]
Assume \(\epsilon_U=0\), \(\delta=14\), and \(L=\overline{H[U]}\) is four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). The exact ledger gives seven cross-edges in \(H[U]\), all between \(D\) and the small parts, with distinct small-side endpoints. For \(d\in D\), let \(t_d=|N_H(d)\cap(A\cup B\cup C)|\). Then
\[
d_H(d,W)=5-t_d,\qquad \sum_{d\in D}t_d=7.
\]
All four units of degree excess lie in \(W\).

The remaining W-profile is
\[
H[W]=C_3\dot\cup C_5^{(1)}\dot\cup C_5^{(2)}\dot\cup C_5^{(3)}
\]
plus one edge \(xy\) between two distinct components. Write \(C_0\cong K_3\) and \(C_1,C_2,C_3\cong K_5\). For a component \(C_i\), let
\[
S_i=\{u\in U:\ u\text{ is adjacent to every vertex of }C_i\},
\quad E_i=\sum_{w\in C_i}\epsilon_w.
\]
Then \(\sum_i E_i=4\).

## 2. Transversal saturation and \(t_d\le2\)

Call \(z\in U\) W-saturated if it is complete to one of the four clique components of \(H[W]\). If it is not W-saturated, each component has a non-neighbour of \(z\). The only edge between components is \(xy\). For the selected four non-neighbours to fail to form an independent 4-set, the non-neighbour sets in the two components containing \(x,y\) must be exactly \(\{x\}\) and \(\{y\}\); otherwise choose a non-endpoint in one of those sets and avoid the unique cross-edge.

Consequently, the total number of W-non-neighbours of a non-saturated vertex is at most
\[
\begin{cases}
1+1+5+5=12,&xy\text{ joins }C_0\text{ to a }K_5,\\
1+1+3+5=10,&xy\text{ joins two }K_5\text{ components}.
\end{cases} \tag{1}
\]
Every \(d\in D\) has \(d_H(d,W)=5-t_d\le5\), hence at least 13 W-non-neighbours. By (1), every \(d\in D\) is W-saturated. Since the smallest W-component has size 3, \(d_H(d,W)\ge3\), so
\[
\boxed{t_d\le2\quad(d\in D).} \tag{2}
\]

Every \(u\in U\) has \(d_H(u,W)\in\{5,6\}\): the seven small-side endpoints of the seven \(U\)-cross-edges have W-degree 5, and all other small-part vertices have W-degree 6. If \(xy\) joins two \(K_5\)'s, (1) shows every \(u\in U\) is W-saturated. If \(xy\) joins \(C_0\) to a \(K_5\), only a small-part vertex of W-degree 6 can fail saturation; its non-neighbour sets must be \(\{x\},\{y\},C_2,C_3\) (the two other \(K_5\)'s in full), since it has exactly 12 W-non-neighbours. We now rule out this exceptional case.

## 3. No exceptional unsaturated vertex in \(U\)

Assume \(xy\) joins \(C_0\) to \(C_1\), with \(x\in C_0\), \(y\in C_1\), and \(C_2,C_3\) the other two \(K_5\)'s. Suppose \(u\in U\) is not W-saturated. By the equality case in (1), \(u\) is nonadjacent to \(x,y\) and to every vertex of \(C_2\cup C_3\). Also \(d_H(u,W)=6\), so \(d_H(u,U)=6\) and
\[
|U\setminus N_H[u]|=29-(6+1)=22.
\]

For every \(v\in U\setminus N_H[u]\) that is nonadjacent to \(y\), the vertex \(v\) must be complete to \(C_2\) or to \(C_3\). Otherwise choose \(b\in C_2\setminus N_H(v)\) and \(c\in C_3\setminus N_H(v)\); then \(\{u,v,y,b,c\}\) is an independent 5-set, since \(u\) and \(y\) are anticomplete to both \(C_2,C_3\), and \(C_2,C_3\) are anticomplete to one another. There are at least
\[
22-d_H(y,U)=22-(7+\epsilon_y)=15-\epsilon_y
\]
such vertices \(v\), all in \(S_2\cup S_3\). Hence
\[
|S_2|+|S_3|\ge15-\epsilon_y. \tag{3}
\]

We will prove below the component capacity bound \(|S_i|\le5+E_i\) for each \(K_5\) not incident to \(xy\). Applying it to \(C_2,C_3\),
\[
|S_2|+|S_3|\le10+E_2+E_3
\le10+(4-\epsilon_y)=14-\epsilon_y, \tag{4}
\]
contradicting (3). Thus every \(u\in U\) is W-saturated, regardless of the location of \(xy\).

## 4. Common-neighbour capacities for the W-components

First consider a \(K_5\) component \(C_i\) not incident to \(xy\). Each \(w\in C_i\) has
\[
d_H(w,U)=8+\epsilon_w.
\]
If \(w\) is W-side-unsaturated, then it is not complete to any U-part. For each \(d\in D\) nonadjacent to \(w\), the \(\alpha(H)\le4\) condition forces at least one of the three small-part non-neighbour sets of \(w\) to be contained in \(N_H(d)\cap(A\cup B\cup C)\). By (2), that set has size at most 2; distinct such \(d\)'s must be assigned distinct small parts because every small-side vertex has at most one cross-edge in \(H[U]\). It follows that if \(w\) is not complete to a U-part, then \(d_H(w,U)\ge12\). Therefore an unsaturated \(w\in C_i\) has \(\epsilon_w=4\); one of the other four vertices of \(C_i\) has excess 0 and U-degree 8. Thus \(|S_i|\le8\le5+E_i\).

If every vertex of \(C_i\) is complete to a U-part, label each \(w\in C_i\) by one such part \(P(w)\). The number of its U-edges outside that part is at most \(1+\epsilon_w\). No single U-part can label all five vertices: otherwise a small part together with \(C_i\) gives a \(K_{12}\), or \(D\cup C_i\) gives a \(K_{13}\). Every \(u\in S_i\) therefore uses at least one edge \(uw\) outside the label part of \(w\). Counting these distinct extra edges yields
\[
\boxed{|S_i|\le5+E_i} \tag{5}
\]
for each nonincident \(K_5\).

Now let \(C_1\cong K_5\) be incident to \(xy\) at \(y\). Its endpoint has \(d_H(y,U)=7+\epsilon_y\), while the other four vertices have U-degree \(8+\epsilon_w\). The endpoint \(y\) is necessarily complete to a U-part: the unsaturated-degree lemma above would require U-degree at least 12, whereas \(7+\epsilon_y\le11\). If a non-endpoint vertex of \(C_1\) is unsaturated, it has excess 4; then \(\epsilon_y=0\) and \(|S_1|\le d_H(y,U)=7\le4+E_1\). Otherwise all five vertices have U-part labels. The endpoint contributes at most \(\epsilon_y\) extra edges, and the other four vertices together contribute at most \(4+\sum_{w\in C_1\setminus\{y\}}\epsilon_w\). Again no common label is possible by \(\omega(H)\le11\), so
\[
\boxed{|S_1|\le4+E_1.} \tag{6}
\]

Finally, if \(C_0\cong K_3\) is incident to \(xy\) at \(x\), then \(d_H(x,U)=9+\epsilon_x\), so
\[
\boxed{|S_0|\le9+E_0.} \tag{7}
\]
If \(C_0\) is not incident to \(xy\), any \(w\in C_0\) has U-degree \(10+\epsilon_w\), giving
\[
\boxed{|S_0|\le10+E_0.} \tag{8}
\]

## 5. Final cover contradiction

Every \(u\in U\) is W-saturated, so \(U=S_0\cup S_1\cup S_2\cup S_3\) and
\[
29=|U|\le\sum_{i=0}^3|S_i|.
\]
If \(xy\) joins \(C_0\) to a \(K_5\), use (5)–(7):
\[
\sum_i|S_i|\le(9+E_0)+(4+E_1)+(5+E_2)+(5+E_3)
=23+4=27.
\]
If \(xy\) joins two \(K_5\)'s, use (5), (6) for both incident components, and (8):
\[
\sum_i|S_i|\le(10+E_0)+(4+E_1)+(4+E_2)+(5+E_3)
=23+4=27.
\]
Both contradict \(29\le\sum_i|S_i|\).

Therefore the \(\delta=14,\epsilon_U=0\), four-partite W-profile \(K_3\cup K_5^3\) plus one cross-edge is impossible. Combined with the three sibling profile exclusions, this closes the entire \(\delta=14,\epsilon_U=0\), four-partite branch under the retained contracts. It does not close \(\delta=14\) with \(\epsilon_U\in\{1,2\}\), the \(\delta=14\) non-four-partite branch, \(\delta\le13\), any of the five templates globally, or E407 Q32 / EG617(r=12) overall.
