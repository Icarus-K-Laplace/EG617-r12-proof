# E407 Q32 — exclude the delta-13 \(\epsilon_U=1\), \(K_3\cup3K_5\) plus one W-cross-edge profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite hypothesis on \(L=\overline{H[U]}\), and \(\omega(H)\le11\).

## 1. Contract and exact ledger

Assume the E407 Q32 core contract:
\[
|H|=47,\ e(H)=284,\ \alpha(H)\le4,\ \omega(H)\le11,\ \delta(H)\ge12,\ 
\sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\). Let \(U\) have 29 vertices, \(W=H\setminus U\) have 18 vertices, and suppose the 49 pairwise edge-disjoint independent 4-set witnesses give
\[
e(H[U])=112-\delta,\quad e(H[W])=48-\epsilon_U-\delta,\quad
e_H(U,W)=124+\epsilon_U+2\delta.
\]
Take \(\delta=13,\epsilon_U=1\), so \(e(H[U])=99\), \(e(H[W])=34\), and the W-side excess is \(E_W=3\).

Assume \(L=\overline{H[U]}\) is four-partite. The transversal witnesses force U-parts \(A,B,C,D\) of sizes \(7,7,7,8\), all small-small pairs to be used by witnesses, and exactly eight H[U] cross-edges, all between \(D\) and \(A\cup B\cup C\). Each small-part vertex has at most one such cross-edge. For \(d\in D\), put \(t_d=d_{H[U]}(d,A\cup B\cup C)\); then
\[
d_H(d,W)=5+\epsilon_d-t_d.
\]

Suppose \(H[W]\) consists of a \(K_3\) component \(C_0\) and three \(K_5\) components \(C_1,C_2,C_3\), plus one edge \(xy\) joining two distinct components. Let
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\},\qquad
E_i=\sum_{w\in C_i}\epsilon_w,
\]
so \(E_0+E_1+E_2+E_3=3\).

## 2. Transversal saturation and D-to-W degree bounds

If a vertex \(u\in U\) is not complete to any W-component, its non-neighbour sets in the two components containing \(x,y\) must be exactly \(\{x\}\) and \(\{y\}\); otherwise one can choose one non-neighbour from each of the four components while avoiding the unique cross-edge, producing an independent 5-set with \(u\). It is also nonadjacent to every vertex of the other two components. Thus:
- if \(xy\) joins \(C_0\) to a \(K_5\), then \(d_H(u,W)=6\);
- if \(xy\) joins two \(K_5\)'s, then \(d_H(u,W)=8\).

For \(d\in D\), the same alternatives apply if \(d\) is not W-saturated. In the \(K_3\)-\(K_5\) placement, the exceptional degree \(d_H(d,W)=6\) forces \(5+\epsilon_d-t_d=6\), hence \(\epsilon_d=1,t_d=0\); this can occur for at most one \(d\). Every other \(d\) is W-saturated and satisfies \(t_d\le2+\epsilon_d\le2\). In the \(K_5\)-\(K_5\) placement, degree eight would require \(t_d=\epsilon_d-3<0\), impossible because \(\epsilon_d\le\epsilon_U=1\); hence every \(d\) is W-saturated and \(t_d\le2+\epsilon_d\le3\). In either placement, at most one \(D\)-vertex has \(t_d=3\), and every other \(D\)-vertex has \(t_d\le2\).

## 3. Every U-vertex is complete to a W-component

### Case I: \(xy\) joins \(C_0\) to \(C_1\)

Suppose \(u\in U\) is not W-saturated. Then \(d_H(u,W)=6\), so \(d_H(u,U)=6+\epsilon_u\) and \(\epsilon_u\in\{0,1\}\). Because \(u\) misses \(x,y\) and all of \(C_2\cup C_3\), every \(v\in U\setminus N_H[u]\) that is nonadjacent to \(y\) must be complete to \(C_2\) or to \(C_3\). Otherwise choosing a non-neighbour of \(v\) in each of \(C_2,C_3\) gives an independent 5-set \(\{u,v,y,b,c\}\). Since \(d_H(y,U)=7+\epsilon_y\), it follows that
\[
|S_2|+|S_3|\ge (22-\epsilon_u)-(7+\epsilon_y)
=15-\epsilon_u-\epsilon_y. \tag{1}
\]

For each of \(C_2,C_3\), we claim \(|S_i|\le5+E_i\). If every vertex of \(C_i\) is complete to a U-part, label it by that part. A common label is forbidden because \(K_5\) plus any U-part of size at least seven contains a \(K_{12}\). Every common neighbour therefore uses at least one extra edge outside the chosen labels; the total load is at most \(5+E_i\). If a vertex \(w\in C_i\) is not complete to a U-part, the D-neighbourhood argument below gives \(d_H(w,U)\ge11\), so \(\epsilon_w\ge3\). Since \(E_W=3\), the other four vertices of \(C_i\) have U-degree eight and force \(|S_i|\le8=5+E_i\).

To justify the stated lower bound \(d_H(w,U)\ge11\) for an unsaturated K5 vertex \(w\), let \(D'\) be its non-neighbour set in \(D\). For every \(d\in D'\), an independent-transversal argument forces one of the three small-part non-neighbour sets of \(w\) to be contained in \(N_{H[U]}(d)\). Distinct \(d\)'s require distinct small parts because each small-part vertex has at most one D-cross-edge. At most one \(d\) can have \(t_d=3\), all others have \(t_d\le2\). If \(|D'|=1\), the number of non-neighbours in \(U\) is at most \(3+7+7+1=18\), so \(d_H(w,U)\ge11\). If \(|D'|=2\), the two selected small sets have total size at most \(3+2\), the third has size at most seven, and \(|D'|=2\), giving at most 14 non-neighbours and \(d_H(w,U)\ge15\). If \(|D'|=3\), the selected small sets have total size at most \(3+2+2\), giving at most 10 non-neighbours and \(d_H(w,U)\ge19\). Thus the claimed lower bound holds.

Consequently
\[
|S_2|+|S_3|\le10+E_2+E_3\le13-\epsilon_y, \tag{2}
\]
because \(E_2+E_3\le E_W-\epsilon_y=3-\epsilon_y\). Equations (1)–(2) are incompatible: their bounds differ by at least \(2-\epsilon_u\ge1\). Hence no such \(u\) exists.

### Case II: \(xy\) joins two \(K_5\) components

A nonsaturated \(u\in U\) would have \(d_H(u,W)=8\). But for a small-part vertex \(d_H(u,W)=6+\epsilon_u-t_u\le7\), and for \(d\in D\), \(d_H(d,W)=5+\epsilon_d-t_d\le6\). Contradiction.

Thus in either placement every \(u\in U\) is W-saturated. The four sets \(S_i\) cover \(U\), so
\[
29\le\sum_{i=0}^3|S_i|. \tag{3}
\]

## 4. Component capacities

For a \(K_5\) not incident to \(xy\), the preceding unsaturated-vertex bound gives \(|S_i|\le5+E_i\). For the \(K_5\) component incident to \(xy\), its endpoint \(y\) has U-degree \(7+\epsilon_y\). If a non-endpoint vertex were unsaturated, it would need excess three; then \(E_i=3,\epsilon_y=0\), and \(|S_i|\le d_H(y,U)=7=4+E_i\). Otherwise label all five vertices by their unique U-parts. No common label is possible by \(\omega(H)\le11\); the endpoint's extra-edge load is at most \(\epsilon_y\), and the other four loads sum to at most \(4+E_i-\epsilon_y\). Thus the incident K5 has
\[
|S_i|\le4+E_i. \tag{4}
\]

If the \(K_3\) component is incident to \(xy\), its endpoint has U-degree \(9+\epsilon_x\), hence \(|S_0|\le9+E_0\). If it is not incident to \(xy\), every triangle vertex has U-degree \(10+\epsilon_w\), giving \(|S_0|\le10+E_0\).

If \(xy\) joins \(C_0\) to a \(K_5\), these bounds imply
\[
\sum_i|S_i|\le(9+E_0)+(4+E_1)+(5+E_2)+(5+E_3)
=23+E_W=26<29.
\]
If \(xy\) joins two \(K_5\)'s, they imply
\[
\sum_i|S_i|\le(10+E_0)+(4+E_1)+(4+E_2)+(5+E_3)
=23+E_W=26<29.
\]
Both contradict (3).

## 5. Conclusion and scope

The \(\delta=13,\epsilon_U=1\), four-partite-U profile \(K_3\dot\cup3K_5\) plus one W-cross-edge is **EXCLUDED**, regardless of which two components the edge joins.

This does not exclude the \((4,4,4,6)\)-plus-one-edge or \((4,4,5,5)\)-plus-two-edge profiles at \(\epsilon_U=1\), the \(\epsilon_U=0\) row, non-four-partite U-complements, \(\delta\le12\), the five shell templates globally, or the upstream \(K_{145}\)-to-T61 bridge. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
