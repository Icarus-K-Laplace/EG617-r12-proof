# E407 Q32 — exclude the delta-13 \(\epsilon_U=1\), \(3K_4\cup K_6\) profile when the cross-edge joins two \(K_4\)'s

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite hypothesis on \(L=\overline{H[U]}\), and \(\omega(H)\le11\).

## 1. Exact contract

Assume
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\). Let \(|U|=29\), \(|W|=18\), and assume the 49 pairwise edge-disjoint independent 4-set witnesses on \(U\), seven per exact-color class. Put \(\epsilon_U=\sum_{u\in U}\epsilon_u\) and \(\delta=e(L)-294\), where \(L=\overline{H[U]}\).

Take \(\delta=13,\epsilon_U=1\), and assume \(L\) is four-partite. The transversal witnesses force U-parts \(A,B,C,D\) of sizes \(7,7,7,8\). All 49 pairs between any two small parts are used exactly once, so H[U] cross-edges occur only between \(D\) and \(A\cup B\cup C\). Since \(e(H[U])=99\) and the within-part edge count is 91, there are exactly eight such cross-edges; each small-part vertex has at most one.

Suppose \(H[W]\) is \(3K_4\dot\cup K_6\) plus one edge \(xy\) joining two of the \(K_4\) components. Call those two components \(C_0,C_1\), the remaining \(K_4\) component \(C_2\), and the \(K_6\) component \(C_3\). Let
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\},\qquad
E_i=\sum_{w\in C_i}\epsilon_w,
\]
so \(E_0+E_1+E_2+E_3=3\).

## 2. D-vertex saturation and reverse saturation

If \(d\in D\) is not complete to a W-component, the one-cross-edge transversal bound gives \(d_H(d,W)\ge6\): its non-neighbour sets at the endpoints must be exactly the endpoints, and the other components can contribute at most all their vertices. But
\[
d_H(d,W)=5+\epsilon_d-t_d\le6.
\]
Thus a nonsaturated \(d\) would have \(\epsilon_d=1,t_d=0\). The other seven D-vertices would then have zero excess and, being W-saturated to a component of size at least four, would each have \(t_d\le1\). This would give \(\sum_Dt_d\le7\), contradicting the exact eight H[U] cross-edges. Hence every D-vertex is W-saturated and
\[
d_H(d,W)\ge4,\qquad t_d\le1+\epsilon_d\le2. \tag{1}
\]

For any W-vertex \(w\) not complete to a U-part, let \(D'\) be its D-non-neighbour set. The independent-transversal argument forces, for each \(d\in D'\), one of the three small-part non-neighbour sets of \(w\) to be contained in \(N_{H[U]}(d)\), hence to have size at most \(t_d\le2\). Distinct \(d\)'s require distinct small parts because each small-part vertex has at most one D-cross-edge. Therefore the number of U-non-neighbours of \(w\) is at most \(2+7+7+1=17\) when \(|D'|=1\), at most \(2+2+7+2=13\) when \(|D'|=2\), and at most \(2+2+2+3=9\) when \(|D'|=3\). Thus
\[
\boxed{d_H(w,U)\ge12\quad\text{for every W-vertex not complete to a U-part}.} \tag{2}
\]

## 3. U-saturation: at most one exceptional vertex

A U-vertex not complete to a W-component must have its non-neighbour sets in the two components containing \(x,y\) exactly \(\{x\}\) and \(\{y\}\). The other two components are \(K_4\) and \(K_6\), so it has at most \(1+1+4+6=12\) W-non-neighbours and hence \(d_H(u,W)\ge6\).

For a small-part vertex \(u\), \(d_H(u,W)=6+\epsilon_u-t_u\le7\); for \(d\in D\), \(d_H(d,W)\le6\). If \(d_H(u,W)=6\), then \(u\) is nonadjacent to all of \(C_2\cup C_3\), and \(d_H(u,U)=6+\epsilon_u\). The endpoint \(y\) has U-degree \(8+\epsilon_y\). Every \(v\in U\setminus N_H[u]\) that is nonadjacent to \(y\) must be complete to \(C_2\) or to \(C_3\), or else \(u,v,y\) and one non-neighbour from each of \(C_2,C_3\) form an independent 5-set. Therefore
\[
|S_2|+|S_3|\ge (22-\epsilon_u)-(8+\epsilon_y)
=14-\epsilon_u-\epsilon_y. \tag{3}
\]
The component capacities proved below give \(|S_2|\le9\) and \(|S_3|\le\lfloor E_3/2\rfloor\). Since \(E_3\le3-\epsilon_y\), the right side of (3) is at least \(13-\epsilon_y\), while
\[
|S_2|+|S_3|\le9+\left\lfloor(3-\epsilon_y)/2\right\rfloor.
\]
For \(\epsilon_y=0,1,2,3\), the respective lower bounds are \(13,12,11,10\), while the upper bounds are \(10,10,9,9\). Contradiction. So no nonsaturated U-vertex can have W-degree six.

If \(d_H(u,W)=7\), the degree equation forces \(u\) to be a small-part vertex with \(\epsilon_u=1,t_u=0\); its W-neighbourhood consists of the six non-endpoints of the two endpoint K4s and exactly one additional vertex in \(C_2\) or \(C_3\). Since \(\epsilon_U=1\), at most one such U-vertex exists. Hence at least 28 of the 29 U-vertices are W-saturated.

## 4. Component common-neighbour capacities

For a K4 component not incident to \(xy\), every vertex has U-degree \(9+\epsilon_w\). If any vertex is not complete to a U-part, (2) forces its excess to be three; the other three vertices then have U-degree nine, giving \(|S_i|\le9\). If all four vertices are labelled by their unique U-parts, the total extra-edge load beyond labels is at most \(8+E_i\le11\). A common label \(D\) is forbidden by \(\omega(H)\le11\). A common small-part label yields at most \(7+\lfloor(8+E_i)/4\rfloor\le9\) common neighbours. With mixed labels, maximum multiplicity at most two gives at most five common neighbours; a \(3+1\) split gives \(a\le2+E_i\le5\) common neighbours in the three-label part and \(a+3b\le8+E_i\le11\), hence \(a+b\le7\). Thus every nonincident K4 has
\[
|S_i|\le9. \tag{4}
\]

For a K4 component incident to \(xy\), the endpoint has U-degree \(8+\epsilon_x\), and its other three vertices have U-degree \(9+\epsilon_w\). The endpoint cannot be U-unsaturated by (2); if a non-endpoint is unsaturated, it has excess three, the endpoint has excess zero and U-degree eight, so \(|S_i|\le8\). Otherwise total extra-edge load is at most \(7+E_i\le10\). A common label \(D\) is forbidden; a common small label yields at most \(7+\lfloor(7+E_i)/4\rfloor\le9\); mixed labels of maximum multiplicity two give at most five common neighbours, and a \(3+1\) split gives at most six. Thus every incident K4 also satisfies
\[
|S_i|\le9. \tag{5}
\]

Every K6 vertex is U-saturated by (2), since its U-degree is at most \(7+\epsilon_w\le10\). The total extra-edge load beyond labels is at most \(E_3\). No five K6 vertices can share a small-part label and no four can share label \(D\), or a \(K_{12}\) results. Hence each common neighbour in \(S_3\) uses at least two extra edges, and
\[
|S_3|\le\lfloor E_3/2\rfloor\le1. \tag{6}
\]

## 5. Final contradiction

If all U-vertices are W-saturated, then \(U=S_0\cup S_1\cup S_2\cup S_3\), and (4)–(6) give
\[
29\le\sum_i|S_i|\le9+9+9+1=28,
\]
impossible.

It remains only to rule out the single possible U-saturation exception from Section 3. Suppose such a vertex \(u\) exists, in small part \(P_0\). Then at least 28 U-vertices are covered by the \(S_i\)'s, so \(\sum_i|S_i|\ge28\). If any K4 capacity is at most eight, the total capacity is at most \(8+9+9+1=27\), contradiction. Thus all three K4 capacities would have to equal nine.

If a K4 component has a W-vertex not complete to a U-part, its excess must be three. If it is an endpoint K4, its capacity is at most eight; if it is the nonincident K4, the two endpoint K4s have zero excess and capacities at most eight, while the K6 has zero excess and capacity zero. In either case the total cover capacity is below 28. Therefore all vertices in all three K4s must have U-part labels.

A K4 common-neighbour capacity can equal nine only if all four vertices have the same small-part label: the mixed-label bounds in Section 4 are at most seven for a nonincident K4 and at most six for an incident K4, and a common label \(D\) is forbidden. No K4 can be labelled by \(P_0\), because then \(u\in P_0\) would be complete to that component, contrary to the exceptional pattern. The three K4 components must therefore each choose one of the other two small parts as its common label. By pigeonhole, two components share a small-part label \(P\), so \(P\subseteq S_i\cap S_j\). Their common-neighbour sets overlap in at least seven vertices, and the union of all four sets has size at most \(28-7=21\), contradicting the requirement to cover at least 28 U-vertices.

Therefore the \(\delta=13,\epsilon_U=1\), four-partite-U profile \(3K_4\dot\cup K_6\) with one W-cross-edge between two K4 components is **EXCLUDED**. Together with DELTA13_EPS1_3K4_K6_K4K6_EDGE.md, this closes both placements of the unique cross-edge for this W-profile. E407 Q32 overall and the original EG617(r=12) theorem remain OPEN / NOT_CERTIFIED.
