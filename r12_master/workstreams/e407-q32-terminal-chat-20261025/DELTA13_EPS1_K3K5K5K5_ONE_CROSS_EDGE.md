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

If a vertex \(u\in U\) is not complete to any W-component, its non-neighbour sets in the two components containing \(x,y\) must be exactly \(\{x\}\) and \(\{y\}\); otherwise one can choose one non-neighbour from each of the four components while avoiding the unique cross-edge, producing an independent 5-set with \(u\). Its non-neighbour sets in the other two components are nonempty but need not be the whole components. Therefore the total number of W-non-neighbours is at most 12 if \(xy\) joins \(C_0\) to a \(K_5\), and at most 10 if \(xy\) joins two \(K_5\)'s. Consequently:
- if \(xy\) joins \(C_0\) to a \(K_5\), then \(d_H(u,W)\ge6\), with equality only when \(u\) is nonadjacent to every vertex in the other two \(K_5\)'s;
- if \(xy\) joins two \(K_5\)'s, then \(d_H(u,W)\ge8\), with equality only when \(u\) is nonadjacent to every vertex in the other two components.

For \(d\in D\), the same alternatives apply if \(d\) is not W-saturated. In the \(K_3\)-\(K_5\) placement, a nonsaturated \(d\) must have \(d_H(d,W)\ge6\), while \(d_H(d,W)=5+\epsilon_d-t_d\le6\); hence \(d_H(d,W)=6\), forcing \(\epsilon_d=1,t_d=0\). This can occur for at most one \(d\). Every W-saturated \(d\) satisfies \(t_d\le2+\epsilon_d\). In the \(K_5\)-\(K_5\) placement, a nonsaturated \(d\) would require \(d_H(d,W)\ge8\), but \(d_H(d,W)=5+\epsilon_d-t_d\le6\), impossible; hence every \(d\in D\) is W-saturated and \(t_d\le2+\epsilon_d\). In either placement, at most one \(D\)-vertex has \(t_d=3\), and every other \(D\)-vertex has \(t_d\le2\).

## 3. Every U-vertex is complete to a W-component

### Case I: \(xy\) joins \(C_0\) to \(C_1\)

Suppose \(u\in U\) is not W-saturated. Then \(d_H(u,W)\ge6\), so \(d_H(u,U)\le6+\epsilon_u\le7\). If \(d_H(u,W)=6\), then \(u\) is nonadjacent to all of \(C_2\cup C_3\), and \(d_H(u,U)=6+\epsilon_u\). Every \(v\in U\setminus N_H[u]\) that is nonadjacent to \(y\) must then be complete to \(C_2\) or to \(C_3\). Otherwise choosing a non-neighbour of \(v\) in each of \(C_2,C_3\) gives an independent 5-set \(\{u,v,y,b,c\}\). Since \(d_H(y,U)=7+\epsilon_y\), this yields
\[
|S_2|+|S_3|\ge (22-\epsilon_u)-(7+\epsilon_y)
=15-\epsilon_u-\epsilon_y. \tag{1}
\]
As \(|S_2|+|S_3|\le13-\epsilon_y\), this is impossible because \(\epsilon_u\le1\).

If instead \(d_H(u,W)=7\), the degree equation forces \(u\) to be a small-part vertex with \(\epsilon_u=1,t_u=0\), so \(d_H(u,U)=6\). Its W-neighbourhood consists of exactly one vertex \(z\) in one of \(C_2,C_3\), while \(u\) is nonadjacent to \(x,y\) and to every other vertex of \(C_2\cup C_3\). This is the only remaining nonsaturated-U pattern. Because \(\epsilon_U=1\), there can be at most one such \(u\).

For each of \(C_2,C_3\), we claim \(|S_i|\le5+E_i\). If every vertex of \(C_i\) is complete to a U-part, label it by that part. A common label is forbidden because \(K_5\) plus any U-part of size at least seven contains a \(K_{12}\). Every common neighbour therefore uses at least one extra edge outside the chosen labels; the total load is at most \(5+E_i\). If a vertex \(w\in C_i\) is not complete to a U-part, the D-neighbourhood argument below gives \(d_H(w,U)\ge11\), so \(\epsilon_w\ge3\). Since \(E_W=3\), the other four vertices of \(C_i\) have U-degree eight and force \(|S_i|\le8=5+E_i\).

To justify the stated lower bound \(d_H(w,U)\ge11\) for an unsaturated K5 vertex \(w\), let \(D'\) be its non-neighbour set in \(D\). For every \(d\in D'\), an independent-transversal argument forces one of the three small-part non-neighbour sets of \(w\) to be contained in \(N_{H[U]}(d)\). Distinct \(d\)'s require distinct small parts because each small-part vertex has at most one D-cross-edge. At most one \(d\) can have \(t_d=3\), all others have \(t_d\le2\). If \(|D'|=1\), the number of non-neighbours in \(U\) is at most \(3+7+7+1=18\), so \(d_H(w,U)\ge11\). If \(|D'|=2\), the two selected small sets have total size at most \(3+2\), the third has size at most seven, and \(|D'|=2\), giving at most 14 non-neighbours and \(d_H(w,U)\ge15\). If \(|D'|=3\), the selected small sets have total size at most \(3+2+2\), giving at most 10 non-neighbours and \(d_H(w,U)\ge19\). Thus the claimed lower bound holds.

Consequently
\[
|S_2|+|S_3|\le10+E_2+E_3\le13-\epsilon_y, \tag{2}
\]
because \(E_2+E_3\le E_W-\epsilon_y=3-\epsilon_y\). Equations (1)–(2) are incompatible: their bounds differ by at least \(2-\epsilon_u\ge1\). Hence the \(d_H(u,W)=6\) nonsaturated case is impossible.

### Case II: \(xy\) joins two \(K_5\) components

A nonsaturated \(u\in U\) would have \(d_H(u,W)=8\). But for a small-part vertex \(d_H(u,W)=6+\epsilon_u-t_u\le7\), and for \(d\in D\), \(d_H(d,W)=5+\epsilon_d-t_d\le6\). Contradiction.

Thus every U-vertex is W-saturated in the \(K_5\)-\(K_5\) placement. In the \(K_3\)-\(K_5\) placement, the \(d_H(u,W)=6\) case is impossible and at most one \(d_H(u,W)=7\) exception can remain. Therefore at least 28 of the 29 vertices of \(U\) are W-saturated, so
\[
28\le\sum_{i=0}^3|S_i|. \tag{3}
\]

## 4. Component capacities

For a \(K_5\) not incident to \(xy\), the preceding unsaturated-vertex bound gives \(|S_i|\le5+E_i\). For the \(K_5\) component incident to \(xy\), its endpoint \(y\) has U-degree \(7+\epsilon_y\). If \(xy\) joins \(C_0\) to a \(K_5\), these bounds imply
\[
\sum_i|S_i|\le(9+E_0)+(4+E_1)+(5+E_2)+(5+E_3)
=23+E_W=26<28.
\]
At least 28 vertices of \(U\) are W-saturated in this placement, so their membership in the \(S_i\)'s contradicts this bound. If \(xy\) joins two \(K_5\)'s, all 29 vertices are W-saturated and
\[
\sum_i|S_i|\le(10+E_0)+(4+E_1)+(4+E_2)+(5+E_3)
=23+E_W=26<29,
\]
again a contradiction.

## 5. Conclusion and scope

The \(\delta=13,\epsilon_U=1\), four-partite-U profile \(K_3\dot\cup3K_5\) plus one W-cross-edge is **EXCLUDED**, regardless of which two components the edge joins. The proof allows one potential degree-7 W-neighbourhood exception in the \(K_3\)-\(K_5\) placement, but shows that all other U-vertices are saturated; the common-neighbour capacity is at most 26, below the required 28.

This does not exclude the \((4,4,4,6)\)-plus-one-edge or \((4,4,5,5)\)-plus-two-edge profiles at \(\epsilon_U=1\), the \(\epsilon_U=0\) row, non-four-partite U-complements, \(\delta\le12\), the five shell templates globally, or the upstream \(K_{145}\)-to-T61 bridge. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
