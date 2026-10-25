# E407 Q32 — exclude the delta-13 \(\epsilon_U=1\), \(3K_4\cup K_6\) profile when the cross-edge joins \(K_4\) to \(K_6\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite hypothesis on \(L=\overline{H[U]}\), and \(\omega(H)\le11\).

## 1. Exact contract

Assume
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\). Let \(|U|=29\), \(|W|=18\), and assume the 49 pairwise edge-disjoint independent 4-set witnesses on \(U\), seven per exact-color class. Put \(\epsilon_U=\sum_{u\in U}\epsilon_u\) and \(\delta=e(L)-294\), where \(L=\overline{H[U]}\).

Take \(\delta=13,\epsilon_U=1\), and assume \(L\) is four-partite. The transversal witnesses force U-parts \(A,B,C,D\) of sizes \(7,7,7,8\). All 49 pairs between any two small parts are used exactly once, so H[U] cross-edges occur only between \(D\) and \(A\cup B\cup C\). Since \(e(H[U])=99\) and the within-part edge count is 91, there are exactly eight such cross-edges; each small-part vertex has at most one. For \(d\in D\), set \(t_d=d_{H[U]}(d,A\cup B\cup C)\).

The W-side excess is \(E_W=3\). Suppose
\[
H[W]=K_4^{(0)}\dot\cup K_4^{(1)}\dot\cup K_4^{(2)}\dot\cup K_6
\]
plus one edge \(xy\) joining \(K_4^{(0)}\) to \(K_6\). Write \(C_0,C_1,C_2\cong K_4\), \(C_3\cong K_6\), and
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\},\qquad
E_i=\sum_{w\in C_i}\epsilon_w.
\]
Then \(\sum_iE_i=3\).

## 2. Saturation of U and D

Call a vertex W-saturated if it is complete to one of the four clique components of \(H[W]\). If \(u\in U\) is not W-saturated, its non-neighbour sets in the components containing \(x,y\) must be exactly \(\{x\}\) and \(\{y\}\); otherwise a choice of one non-neighbour from each component avoids the only cross-edge and gives an independent 5-set with \(u\). The other two components each contribute at most all four vertices to its non-neighbour set, so a nonsaturated \(u\) has at most \(1+1+4+4=10\) W-non-neighbours. Thus
\[
d_H(u,W)\ge8. \tag{1}
\]
But a small-part vertex has \(d_H(u,W)=6+\epsilon_u-t_u\le7\), and a D-vertex has \(d_H(d,W)=5+\epsilon_d-t_d\le6\). Therefore every \(u\in U\) is W-saturated.

The same transversal bound shows every \(d\in D\) is W-saturated, since \(d_H(d,W)\le6<8\). As every W-component has at least four vertices,
\[
d_H(d,W)=5+\epsilon_d-t_d\ge4,\qquad
t_d\le1+\epsilon_d\le2. \tag{2}
\]

## 3. Reverse saturation for W-vertices

Let \(w\in W\) be not complete to any U-part, and let \(D'\subseteq D\) be its set of non-neighbours in \(D\). For each \(d\in D'\), every triple from the three small-part non-neighbour sets of \(w\) must contain an H[U] cross-edge to \(d\), or those three vertices together with \(d,w\) form an independent 5-set. Hence one of the three small-part non-neighbour sets is contained in \(N_{H[U]}(d)\), so has size at most \(t_d\le2\). Distinct \(d\)'s require distinct small parts because each small-part vertex has at most one D-cross-edge. Thus \(|D'|\le3\). The number of non-neighbours of \(w\) in U is at most:
- \(2+7+7+1=17\) if \(|D'|=1\);
- \(2+2+7+2=13\) if \(|D'|=2\);
- \(2+2+2+3=9\) if \(|D'|=3\).

Consequently
\[
\boxed{d_H(w,U)\ge12\quad\text{for every W-unsaturated }w.} \tag{3}
\]
A K6 vertex has U-degree at most \(7+\epsilon_w\le10\), and the K4 endpoint \(x\) has U-degree \(8+\epsilon_x\le11\). So all vertices of \(C_3\) and the endpoint \(x\) are U-part-saturated.

## 4. Common-neighbour capacity of each K4

For any W-vertex that is complete to a U-part, choose its unique label: its U-degree is at most 12, while two U-parts together have at least 14 vertices. A K4 component with no W-cross-edge has U-degree \(9+\epsilon_w\) at every vertex. If any such vertex is U-unsaturated, (3) forces its excess to be three; the other three vertices then have U-degree nine, so \(|S_i|\le9\). Otherwise label all four vertices. The total extra-edge load beyond their labels is at most \(8+E_i\le11\). A common label \(D\) is forbidden because \(K_4\cup D\) would be a \(K_{12}\). A common small label gives at most \(7+\lfloor(8+E_i)/4\rfloor\le9\) common neighbours. With mixed labels, if the maximum multiplicity is at most two, each common neighbour uses at least two extra edges, so \(|S_i|\le5\). If the split is \(3+1\), the number \(a\) of common neighbours in the three-label part is at most the singleton vertex's load, \(a\le2+E_i\le5\); if \(b\) are outside that part, then \(a+3b\le8+E_i\le11\), giving \(a+b\le7\). Hence every nonincident K4 has
\[
|S_i|\le9. \tag{4}
\]

For the K4 \(C_0\) incident to \(xy\), the endpoint \(x\) has U-degree \(8+\epsilon_x\), and the other three vertices have U-degree \(9+\epsilon_w\). If a non-endpoint is U-unsaturated, (3) forces its excess to be three; then \(\epsilon_x=0\) and \(|S_0|\le d_H(x,U)=8\). Otherwise total label load is at most \(7+E_0\le10\). A common label \(D\) is forbidden; a common small label yields at most \(7+\lfloor(7+E_0)/4\rfloor\le9\); mixed labels of maximum multiplicity two give at most five common neighbours, and a \(3+1\) split gives at most six by \(a\le2+E_0\le5\) and \(a+3b\le7+E_0\le10\). Therefore
\[
|S_0|\le9. \tag{5}
\]

## 5. K6 common-neighbour capacity

Every K6 vertex is U-part-saturated by (3). Its total extra-edge load beyond its U-part label is at most its excess, so the K6 total load is at most \(E_3\). No five K6 vertices can share a small-part label, because those five plus the small part would form a \(K_{12}\); no four can share label \(D\), because those four plus \(D\) would form a \(K_{12}\). Thus every common neighbour in \(S_3\) uses at least two extra edges, and
\[
|S_3|\le\left\lfloor E_3/2\right\rfloor\le1. \tag{6}
\]

## 6. Final contradiction

Every U-vertex is W-saturated, so the four sets \(S_0,S_1,S_2,S_3\) cover \(U\). By (4)–(6),
\[
29=|U|\le\sum_{i=0}^3|S_i|
\le9+9+9+1=28,
\]
a contradiction.

Therefore the \(\delta=13,\epsilon_U=1\), four-partite-U profile \(3K_4\dot\cup K_6\) with its single W-cross-edge joining \(K_4\) to \(K_6\) is **EXCLUDED**. The alternative placement of the cross-edge between two \(K_4\) components remains OPEN, as do the other stated E407 Q32 gaps and the upstream \(K_{145}\)-to-T61 bridge.
