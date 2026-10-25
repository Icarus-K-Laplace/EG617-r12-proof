# E407 Q32: exclude the \(\delta=14,\epsilon_U=0\), \(K_3\cup K_5^3\) profile when its cross-edge joins two \(K_5\)'s

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract and four-partite W-profile classification.

## 1. Contract

Assume the common E407 boundary:
\[
e(H)=284,\quad |U|=29,\quad |W|=18,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,
\]
with \(\epsilon_U=0\), four-partite \(L=\overline{H[U]}\) having parts \(A,B,C,D\) of sizes \(7,7,7,8\), and seven cross-edges of \(H[U]\) between \(A\cup B\cup C\) and \(D\). The seven cross-edges have distinct small-side endpoints. For \(d\in D\), let \(t_d\) be its cross-degree. Since every \(d\in D\) is complete to a whole W-component and the smallest component has size three,
\[
\sum_{d\in D}t_d=7,\qquad 0\le t_d\le2.
\]
All degree excess lies in \(W\):
\[
\epsilon_w=d_H(w)-12\ge0,\qquad \sum_{w\in W}\epsilon_w=4.
\]

Suppose \(H[W]\) consists of \(T\cong K_3\) and three \(K_5\)'s \(P,Q,R\), with its sole cross-edge \(pq\) joining \(p\in P\) to \(q\in Q\).

## 2. Every \(u\in U\) is complete to a whole W-component

A small-part vertex \(u\in A\cup B\cup C\) has \(d_H(u,U)=6\) or \(7\), since it has six neighbours in its own part and at most one cross-edge to \(D\). A vertex \(d\in D\) has \(d_H(d,U)=7+t_d\le9\). Hence every \(u\in U\) has at most six neighbours in \(W\).

If \(u\) were not complete to any of \(T,P,Q,R\), choose a non-neighbour from each component. The four chosen vertices can fail to be independent only if the choices in \(P,Q\) are exactly \(p,q\), the endpoints of the unique cross-edge. But then \(u\) is adjacent to the other four vertices of \(P\) and the other four vertices of \(Q\), giving at least eight W-neighbours, contradiction.

Thus, for
\[
S_T=\{u\in U:u\text{ is complete to }T\},\quad
S_P,S_Q,S_R\text{ defined analogously},
\]
we have \(U=S_T\cup S_P\cup S_Q\cup S_R\), and therefore
\[
29\le |S_T|+|S_P|+|S_Q|+|S_R|. \tag{1}
\]

## 3. Reverse saturation and the three \(K_5\) cover bounds

Use the reverse-saturation lemma in DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md: a W-vertex not complete to any of \(A,B,C,D\) has at least 12 U-neighbours. The degree of a W-vertex is
\[
d_H(w,U)=13-s+\epsilon_w-c_w
\]
when \(w\) belongs to a \(K_s\) component and \(c_w=1\) at a cross-edge endpoint, \(0\) otherwise.

For \(P,Q\), the endpoint has U-degree \(7+\epsilon_w\le11\), so every vertex of those components is part-saturated. For \(R\), every vertex is saturated unless one has \(\epsilon_w=4\); in that exceptional case the other four vertices have excess zero and U-degree eight, which directly gives \(|S_R|\le8\le5+\epsilon_R\).

Choose one U-part label for each saturated vertex of a \(K_5\). A full common label of all five vertices is impossible: \(K_5\) joined to a U-part of size at least seven would give a \(K_{12}\) or larger. Hence every \(u\in S_P\) requires at least one extra edge outside a chosen label part. The total extra-edge load in \(P\) is at most \(4+\epsilon_P\): its four non-endpoint vertices contribute at most \(1+\epsilon_w\) each and endpoint \(p\) contributes at most \(\epsilon_p\). Thus
\[
|S_P|\le4+\epsilon_P.
\]
Likewise \(|S_Q|\le4+\epsilon_Q\), while \(|S_R|\le5+\epsilon_R\).

## 4. The \(K_3\) cover bound

Put \(E_T=\sum_{w\in T}\epsilon_w\). If all vertices of \(T\) are part-saturated and their labels are not all the same U-part, each \(u\in S_T\) uses at least one extra edge; the total load is at most \(9+E_T\). If all three labels are the same small part, that part contributes seven vertices and every additional member of \(S_T\) uses three extra edges, giving
\[
|S_T|\le 7+\left\lfloor\frac{9+E_T}{3}\right\rfloor.
\]
If all labels are \(D\), the analogous bound is
\[
|S_T|\le 8+\left\lfloor\frac{6+E_T}{3}\right\rfloor.
\]
Both full-label bounds are at most \(9+E_T+\mathbf 1_{\{E_T=0\}}\).

If some vertex of \(T\) is not part-saturated, its excess is at least two. One of the other two vertices has excess at most one and U-degree at most eleven, so \(|S_T|\le11\le9+E_T\). In all cases,
\[
|S_T|\le9+E_T+\mathbf 1_{\{E_T=0\}}. \tag{2}
\]

## 5. Contradiction

Combining the component bounds and \(E_T+\epsilon_P+\epsilon_Q+\epsilon_R=4\),
\[
\begin{aligned}
|S_T|+|S_P|+|S_Q|+|S_R|
&\le 9+E_T+\mathbf 1_{\{E_T=0\}}
 +(4+\epsilon_P)+(4+\epsilon_Q)+(5+\epsilon_R)\\
&=26+\mathbf 1_{\{E_T=0\}}\\
&\le27,
\end{aligned}
\]
contradicting (1), which requires the sum to be at least 29.

Therefore the \(\delta=14,\epsilon_U=0\) W-profile \(K_3\cup K_5^3\) with its single cross-edge joining two \(K_5\) components is **EXCLUDED**.

## 6. Scope

The only \(\delta=14,\epsilon_U=0\), four-partite W-profile not excluded by the current files is now the same clique profile with the single cross-edge joining \(K_3\) to a \(K_5\). That endpoint placement remains OPEN. The \(\epsilon_U=1,2\), non-four-partite, and \(\delta\le13\) branches remain OPEN; E407 Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
