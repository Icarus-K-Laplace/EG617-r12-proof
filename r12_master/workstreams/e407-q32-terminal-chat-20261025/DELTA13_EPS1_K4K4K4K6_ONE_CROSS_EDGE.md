# E407 Q32: exclude the delta-13, epsilon_U=1 profile 3K4 + K6 with one W-cross-edge

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract, the four-partite hypothesis on \(L=\overline{H[U]}\), and \(\omega(H)\le11\).

## 1. Contract and ledger

Assume
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\). Let \(U\) have 29 vertices and \(W=V(H)\setminus U\) have 18 vertices. The E407 Q32 ledger is
\[
e(H[U])=112-\delta,\quad e(H[W])=48-\epsilon_U-\delta,\quad
e_H(U,W)=124+\epsilon_U+2\delta.
\]
Take \(\delta=13,\epsilon_U=1\). Then
\[
e(H[U])=99,\quad e(H[W])=34,\quad e_H(U,W)=151,\quad
E_W:=\sum_{w\in W}\epsilon_w=3.
\]

Assume \(L=\overline{H[U]}\) is four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). The 49 transversal witnesses force all pairs between two small parts to be used, so the eight cross-edges of \(H[U]\) run only between \(D\) and \(A\cup B\cup C\), with at most one such edge at each small-part vertex. For \(d\in D\), write \(t_d=d_{H[U]}(d,A\cup B\cup C)\). Then
\[
d_H(d,W)=5+\epsilon_d-t_d,\qquad t_d\le2. \tag{1}
\]
The latter follows from the saturation argument below: if \(d\) is W-saturated, it must have at least four W-neighbours, giving \(t_d\le1+\epsilon_d\le2\); if it is not W-saturated, the only possible case is the \(K_4\)-\(K_4\) placement, where \(d_H(d,W)=6\) and \(\epsilon_d=1,t_d=0\).

Suppose \(H[W]\) consists of three clique parts \(C_1,C_2,C_3\cong K_4\) and one \(C_6\cong K_6\), plus exactly one edge \(xy\) between distinct parts. The base cliques have 33 edges and the extra edge gives the required \(e(H[W])=34\). There are two placements: \(xy\) joins a \(K_4\) to \(K_6\), or it joins two \(K_4\)'s.

For each clique part \(C_i\), define
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\}.
\]

## 2. Saturation dichotomy for U-vertices

A vertex \(u\in U\) that is not complete to any W-part has a non-neighbour in each of the four clique parts. Since there is only one cross-edge \(xy\), an independent transversal can fail only if the non-neighbour sets in the two incident parts are exactly \(\{x\}\) and \(\{y\}\). Hence such a vertex must be adjacent to all other vertices of those two parts.

If \(xy\) joins a \(K_4\) and a \(K_6\), this requires at least
\[
(4-1)+(6-1)=8
\]
W-neighbours. But a small-part vertex of \(U\) has W-degree \(6+\epsilon_u-t_u\le7\), and a D-vertex has W-degree \(5+\epsilon_u-t_u\le6\). Therefore **every U-vertex is complete to some W-part** in this placement.

Now suppose \(xy\) joins two \(K_4\)'s, with endpoints \(x\in C_1\), \(y\in C_2\). Any U-vertex not complete to a W-part must be adjacent to the six non-endpoint vertices of \(C_1\cup C_2\), and nonadjacent to \(x,y\). Its W-degree is either six or seven. A degree-seven exception must be a small-part vertex with \(\epsilon_u=1,t_u=0\), so there is at most one such exception. A degree-six exception has \(\epsilon_u=t_u\); if it is in \(D\), then \(\epsilon_u=1,t_u=0\), so there is at most one D-exception.

Let \(E\subseteq U\) be the set of U-vertices not complete to any W-part, and \(k=|E|\). Every \(u\in E\) has at most one W-neighbour outside the six non-endpoint vertices of \(C_1\cup C_2\). Thus it has at least three non-neighbours in \(C_3\) and at least five in \(C_6\).

Every vertex of \(E\) is adjacent to all six non-endpoint vertices of \(C_1\cup C_2\), and neither \(x\) nor \(y\) is adjacent to any vertex of \(E\). Because each exception has W-degree at most seven, it has at most one additional W-neighbour outside those six vertices. In particular, each exception has at least three non-neighbours in \(C_3\) and at least five in \(C_6\). No bound on the number or mutual adjacency of the exceptions is needed below.

## 3. W-vertices are labelled by U-parts, except for at most one

We first prove the reverse-saturation bound:
\[
\boxed{w\text{ is not complete to any U-part}\ \Longrightarrow\
d_H(w,U)\ge12.} \tag{2}
\]

Let \(A',B',C',D'\) be the non-neighbour sets of \(w\) in the four U-parts. If \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain an H-edge to \(d\); otherwise that triple together with \(w,d\) is an independent 5-set. Thus one of \(A',B',C'\) has size at most \(t_d\le2\). Distinct \(d\in D'\) require distinct small-part non-neighbour sets because each small vertex has at most one H-edge to D. Hence \(|D'|\le3\). The number of U-non-neighbours of \(w\) is at most
\[
\begin{array}{c|c|c}
|D'|&\text{maximum non-neighbours in U}&d_H(w,U)\text{ lower bound}\\\hline
1&2+7+7+1=17&12\\
2&2+2+7+2=13&16\\
3&2+2+2+3=9&20.
\end{array}
\]
The case \(D'=\varnothing\) would make \(w\) complete to D, contrary to the hypothesis. This proves (2).

A W-vertex has U-degree at most 12, while two U-parts together contain at least 14 vertices. Therefore any W-vertex that is complete to a U-part has a unique such label. By (2), an unlabelled W-vertex must have U-degree at least 12. Only a non-endpoint vertex of a \(K_4\) can reach this: its U-degree is \(9+\epsilon_w\), so it must have \(\epsilon_w=3\). Since \(E_W=3\), there is at most one unlabelled W-vertex, and if it exists all other W-excesses vanish. The endpoints of the cross-edge have U-degree \(8+\epsilon_w\le11\); vertices of \(K_6\) have U-degree at most \(10\).

## 4. Common-neighbour capacity bounds

### Lemma 4.1: each K4 part has \(|S_i|\le9\)

For a labelled W-vertex \(w\), let \(P(w)\in\{A,B,C,D\}\) be its U-part label and let
\[
\ell(w)=d_H(w,U)-|P(w)|
\]
be its number of U-neighbours outside its label. If the K4 component is not incident to \(xy\), then \(d_H(w,U)=9+\epsilon_w\) and the total label load is at most \(8+E_i\le11\). If it is incident, one endpoint has U-degree \(8+\epsilon_w\) and the other three have degree \(9+\epsilon_w\), so the load is at most \(7+E_i\le10\). If one W-vertex is unlabelled, its excess is three; the other three vertices have zero excess and their total label load is at most six (at most five if the component is incident to \(xy\)).

Every \(u\in S_i\) in U-part P consumes one extra-edge incidence for each labelled \(w\in C_i\) whose label differs from P. This gives the following exhaustive label-pattern bounds:
- If all four labels agree, the common label cannot be D because \(K_4\cup D\) would form a \(K_{12}\). For a common small-part label, there are at most seven common neighbours in that part, and each common neighbour outside it costs four extra incidences. Thus \(|S_i|\le7+\lfloor11/4\rfloor=9\).
- If the four labels are mixed with multiplicities \(3+1\), common neighbours in the majority label cost at least one incidence each and those outside it cost at least three. With load at most 11 and part size at most eight, there are at most nine common neighbours.
- For multiplicities \(2+2\), \(2+1+1\), or \(1+1+1+1\), every common neighbour costs at least two, two, or three incidences, respectively, so the bound is at most five.
- If one W-vertex is unlabelled, there are only three labels and load at most six. If the labels are mixed, every common neighbour costs at least one incidence, giving \(|S_i|\le6\). If all three labels agree on a small part, at most seven common neighbours lie in it and each outside costs three incidences, giving at most nine. If all three labels agree on D, their total load is at most three and each common neighbour outside D costs three, giving at most \(8+1=9\).

Thus every K4 component satisfies \(|S_i|\le9\).

### Lemma 4.2: the K6 part has \(|S_6|\le\lfloor E_6/2\rfloor\le1\)

Every K6 vertex is labelled by (2). Its U-degree is \(7+\epsilon_w\) if it is not incident to the cross-edge, or \(6+\epsilon_w\) if it is the K6 endpoint. Hence its label load satisfies \(\ell(w)\le\epsilon_w\), so the total K6 label load is at most \(E_6\).

At most four K6 vertices can have the same small-part label, and at most three can have label D; otherwise the corresponding K6 vertices together with that U-part would form a \(K_{12}\). Therefore every \(u\in S_6\) has at least two K6 vertices labelled by a different U-part, and the two corresponding edges are extra incidences. Consequently
\[
2|S_6|\le E_6,\qquad |S_6|\le\lfloor E_6/2\rfloor\le1.
\]

## 5. Exclude both cross-edge placements

### Case I: the cross-edge joins a K4 and K6

Every U-vertex is W-saturated by Section 2, so
\[
29=|U|\le\sum_i|S_i|
\le 9+9+9+\lfloor E_6/2\rfloor
\le28,
\]
a contradiction.

### Case II: the cross-edge joins two K4 parts

If \(E=\varnothing\), every U-vertex is W-saturated, and the same cover inequality gives \(29\le9+9+9+1=28\), contradiction.

Suppose \(k=|E|\ge1\). Let \(C_1,C_2\) be the two K4 parts incident to \(xy\), \(C_3\) the remaining K4, and \(C_6\) the K6. The sets \(S_1,S_2\) are disjoint from E because their respective cross-edge endpoints are nonadjacent to every exception. Each of the three non-endpoint vertices \(w\in C_i\), \(i=1,2\), is adjacent to every vertex of E and every vertex of \(S_i\). Since \(d_H(w,U)=9+\epsilon_w\),
\[
k+|S_i|\le9+\epsilon_w
\]
for each of those three vertices. Taking the minimum over them gives
\[
|S_i|\le9-k+\left\lfloor\frac{E_i}{3}\right\rfloor,\qquad i=1,2.
\]
Combining this with Lemmas 4.1–4.2,
\[
\begin{aligned}
\sum_i|S_i|
&\le 27-2k+
\left\lfloor\frac{E_1}{3}\right\rfloor+
\left\lfloor\frac{E_2}{3}\right\rfloor+
\left\lfloor\frac{E_6}{2}\right\rfloor\\
&\le29-2k,
\end{aligned}
\]
because \(E_1+E_2+E_3+E_6=3\), so the three floor terms sum to at most two. But all \(29-k\) nonexceptional U-vertices are W-saturated, hence
\[
29-k\le\sum_i|S_i|\le29-2k,
\]
impossible for \(k\ge1\).

Both placements are excluded. Therefore the \(\delta=13,\epsilon_U=1\), four-partite-U profile \(3K_4\dot\cup K_6\) plus one W-cross-edge is **EXCLUDED** under the stated contracts.

## 6. Scope

This closes one of the two remaining \(\epsilon_U=1\) W-cross-edge profiles. The \((4,4,5,5)\)-plus-two-cross-edges profile at \(\epsilon_U=1\), the \(\epsilon_U=2\) one-cross-edge profile, \(\epsilon_U=0\), non-four-partite U-complements, \(\delta\le12\), the five shell templates globally, and the original \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED. E407 Q32 and EG617(\(r=12\)) overall remain OPEN / NOT_CERTIFIED.
