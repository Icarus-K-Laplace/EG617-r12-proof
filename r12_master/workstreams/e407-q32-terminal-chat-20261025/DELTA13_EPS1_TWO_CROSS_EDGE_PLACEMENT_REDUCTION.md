# E407 Q32: reduce the delta-13 epsilon_U=1, 2K4 + 2K5 W-profile with two cross-edges

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL: every placement of the two W-cross-edges is excluded** under the retained core/witness contract. The four formerly open same-pair placements are closed in DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_CLOSURE.md.

## 1. Contract

Assume the E407 Q32 47-core contract:
\[
|H|=47,\ e(H)=284,\ \alpha(H)\le4,\ \omega(H)\le11,\ 
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
with \(\epsilon_v=d_H(v)-12\ge0\). Let \(|U|=29,|W|=18\), \(\delta=13,\epsilon_U=1\). The exact ledger is
\[
e(H[U])=99,\quad e(H[W])=34,\quad e_H(U,W)=151,\quad
E_W:=\sum_{w\in W}\epsilon_w=3.
\]
Assume \(L=\overline{H[U]}\) is four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). As in the registered 49-witness contract, all eight \(H[U]\) cross-edges run between \(D\) and \(A\cup B\cup C\), and each small-part vertex has at most one such edge.

Suppose
\[
H[W]=C_1\dot\cup C_2\dot\cup C_3\dot\cup C_4
\]
where \(C_1,C_2\cong K_4\), \(C_3,C_4\cong K_5\), plus exactly two edges between distinct clique parts. The clique edges contribute \(2\cdot6+2\cdot10=32\), so the two cross-edges give \(e(H[W])=34\).

For each part define
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\}.
\]
If all U-vertices are W-saturated (complete to some \(C_i\)), then
\[
29\le\sum_{i=1}^4|S_i|. \tag{1}
\]

## 2. Two cross-edges joining different pairs of clique parts: no U-exceptions

Let \(u\in U\) be not complete to any \(C_i\). Choose a non-neighbour set \(T_i\subseteq C_i\), nonempty for each \(i\). To prevent an independent transversal, every choice from \(T_1\times T_2\times T_3\times T_4\) must contain one of the two W-cross-edges.

If the two cross-edges join disjoint pairs of clique parts, touching all four parts, every \(T_i\) must be the singleton endpoint of its unique incident cross-edge. Then
\[
d_H(u,W)\ge(4-1)+(4-1)+(5-1)+(5-1)=14.
\]

If the two edges share one clique part but join different pairs of parts, the non-neighbour set in the shared part must be contained in the two edge endpoints, and the non-neighbour sets in the other two incident parts must each be a singleton endpoint. Therefore
\[
d_H(u,W)\ge(4-2)+(4-1)+(5-1)=9
\]
when the shared part is a \(K_4\), and at least \(9\) when it is a \(K_5\) (then the other two parts are the two \(K_4\)'s). Both bounds exceed seven.

Every U-vertex has W-degree at most seven: a small-part vertex has \(6+\epsilon_u-t_u\le7\), and a D-vertex has \(5+\epsilon_u-t_u\le6\). Thus **if the two cross-edges join different pairs of clique parts, every U-vertex is W-saturated**.

## 3. Component capacity bounds

Let \(e_i\) be the number of W-cross-edge incidences at \(C_i\), and \(E_i=\sum_{w\in C_i}\epsilon_w\). Then
\[
\sum_i e_i=4,\qquad \sum_i E_i=3.
\]

A reverse-saturation lemma under this four-partite-U contract gives
\[
w\text{ not complete to any U-part}\Longrightarrow d_H(w,U)\ge12.
\]
Indeed, \(t_d\le2\) for \(d\in D\): a W-saturated \(d\) has at least four W-neighbours, giving \(t_d\le1+\epsilon_d\le2\). If \(d\) is not W-saturated, the two-edge blocker structure requires at least five W-neighbours (the minimum is the K4–K4 star), so \(5+\epsilon_d-t_d\ge5\) and \(t_d\le\epsilon_d\le1\). For an unlabelled \(w\), each non-neighbour \(d\in D\) forces one of the non-neighbour sets in \(A,B,C\) to have size at most two; distinct \(d\)'s force distinct small parts. The resulting non-neighbour counts are at most \(17,13,9\) for one, two, or three such D-vertices, so \(d_H(w,U)\ge12\).

Hence every K5 vertex is labelled by a unique U-part, because its U-degree is at most eleven. For a K5 component,
\[
\boxed{|S_i|\le \min(5+E_i-e_i,\,7).} \tag{2}
\]
The total label load is at most \(5+E_i-e_i\). A common label is forbidden because \(K_5\) plus any U-part of size at least seven contains a \(K_{12}\), so every common neighbour consumes at least one extra-edge incidence. If the load bound is eight (only \(E_i=3,e_i=0\)), a common-neighbour set of size eight is still impossible: four W-vertices cannot share label D, and a multiplicity-four small label supports at most seven U-vertices. Thus (2).

For a K4 component,
\[
\boxed{|S_i|\le 8+\mathbf 1_{\{E_i\ge e_i\}}.} \tag{3}
\]
If all four W-vertices are labelled, their total extra-edge load is at most \(8+E_i-e_i\). When \(E_i<e_i\), this is at most seven: a common small label gives at most \(7+\lfloor7/4\rfloor=8\) common neighbours, and mixed labels give no larger bound. When \(E_i\ge e_i\), the general K4 load argument gives \(|S_i|\le9\). If one K4 vertex is unlabelled, it has excess three, so \(E_i=3\ge e_i\); the other three vertices have zero excess and the same bound \(|S_i|\le9\) holds.

## 4. Exact capacity enumeration for different-pair placements

The possible component-incidence vectors \(e=(e_1,e_2,e_3,e_4)\), up to symmetric relabelling, are:
- \(e=(1,1,1,1)\) for disjoint W-cross-edges;
- \(e=(2,1,1,0)\) when the edges share a K4 component;
- \(e=(1,0,2,1)\) when they share a K5 component.

Enumerating all nonnegative integer excess profiles \(E_1+\cdots+E_4=3\) using (2)–(3) gives maximum total cover capacities \(27,28,27\), respectively. Each is strictly below 29, contradicting (1). Thus every placement where the two cross-edges join different pairs of clique parts is excluded.

## 5. Both cross-edges between the two K5 parts

Here \(e=(0,0,2,2)\). The same excess enumeration gives
\[
\sum_i|S_i|\le27.
\]
If the two edges are disjoint, a nonsaturated U-vertex would need at least \(4+4=8\) W-neighbours, impossible. If the two edges form a star in the K5–K5 pair, a nonsaturated U-vertex needs at least \((5-1)+(5-2)=7\) W-neighbours. Equality forces a small-part vertex with \(\epsilon_u=1,t_u=0\), so there is at most one exception. At least 28 U-vertices are therefore covered, but the total capacity is at most 27. Contradiction.

Both K5–K5 placements are excluded.

## 6. Complete same-pair terminal closure

The same-pair disjoint K4-K5 placement is excluded in DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_CLOSED.md. The four other formerly open placements—K4-K4 matching, K4-K4 star, K4-K5 star centred in the K4, and K4-K5 star centred in the K5—are excluded in DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_CLOSURE.md.

The proof combines the common \(k\ge5\) exception floor, the exact Type-I/Type-II blocker classification, the fact that at least six D-vertices have \(t_d=1,\epsilon_d=0\), and an independent-5-set contradiction. Therefore the entire four-partite-\(L\), \(\delta=13,\epsilon_U=1\), \(2K_4\cup2K_5\)-plus-two-cross-edge W-profile is **EXCLUDED** under the retained core/witness contract.

The \(\epsilon_U=2\) one-cross-edge profile, the \(\epsilon_U=0\) row, non-four-partite \(L\), \(\delta\le12\), the five shell templates globally, and the \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.
