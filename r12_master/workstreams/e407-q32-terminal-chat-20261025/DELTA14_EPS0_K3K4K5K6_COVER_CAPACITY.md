# E407 Q32: exclude the \(\delta=14,\epsilon_U=0\), \(K_3\cup K_4\cup K_5\cup K_6\) W-profile

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract and the four-partite W-profile classification.

## 1. Frozen boundary

Assume the E407 Q32 minimum-support boundary:
\[
e(H)=284,\quad |U|=29,\quad |W|=18,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12,
\]
with 49 pairwise edge-disjoint independent four-sets on \(U\), and
\[
e(\overline{H[U]})=294+\delta,\qquad
e(H[U])=112-\delta.
\]
Suppose \(\delta=14\), \(\epsilon_U=0\), and the four-partite \(U\)-complement has parts \(A,B,C,D\) of sizes \(7,7,7,8\). The seven extra edges of \(H[U]\) form a matching from seven distinct vertices of \(A\cup B\cup C\) into \(D\). Write \(t_d=d_{H[U]}(d)-7\) for \(d\in D\). Then
\[
\sum_{d\in D}t_d=7.
\]

The profile treated here is
\[
H[W]=C_3\dot\cup C_4\dot\cup C_5\dot\cup C_6,
\]
where \(C_s\cong K_s\). Its edge count is \(3+6+10+15=34\), as required by the exact ledger. All four units of core degree excess lie in \(W\); write
\[
\epsilon_w=d_H(w)-12\ge0,\qquad
E_s=\sum_{w\in C_s}\epsilon_w,\qquad
E_3+E_4+E_5+E_6=4.
\]

## 2. Saturation facts

Every \(u\in U\) is complete to at least one whole \(C_s\): otherwise choosing a non-neighbour of \(u\) from each of the four disjoint clique components would produce an independent five-set.

Every \(d\in D\) is likewise complete to a whole \(W\)-component. Since \(d_H(d,W)=5-t_d\) and the smallest component has size three,
\[
0\le t_d\le2.
\]

We need the reverse-saturation lemma. If \(w\in W\) is not complete to any of \(A,B,C,D\), let \(D'\) and \(A',B',C'\) be its non-neighbour sets in those parts; all four sets are nonempty. For each \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain a vertex adjacent to \(d\) in \(H[U]\), or that triple together with \(d,w\) would be an independent five-set. Equivalently, at least one of \(A',B',C'\) is contained in \(N_H(d)\cap(A\cup B\cup C)\), and so has size at most \(t_d\le2\). The chosen small part must be different for distinct \(d\in D'\): a small-side vertex has at most one cross-edge, so it cannot lie in the cross-neighbourhoods of two different vertices of \(D\). Hence \(|D'|\le3\).

If \(|D'|=1\), the total number of non-neighbours in \(U\) is at most \(t_d+7+7+1=t_d+15\), so \(d_H(w,U)\ge14-t_d\ge12\). If \(|D'|=2\), two distinct small non-neighbour sets have size at most two and the third has size at most seven; thus there are at most \(2+2+7+2=13\) non-neighbours, giving \(d_H(w,U)\ge16\). If \(|D'|=3\), all three small non-neighbour sets have size at most two, giving at most \(2+2+2+3=9\) non-neighbours and \(d_H(w,U)\ge20\). If \(D'=\varnothing\), \(w\) is complete to \(D\), contrary to the assumed failure of part-saturation. Therefore
\[
\boxed{w\text{ not complete to any U-part}\ \Longrightarrow\ d_H(w,U)\ge12.} \tag{1\)

For \(w\in C_s\), \(d_H(w,U)=13-s+\epsilon_w\). In particular every vertex of \(C_6\) is part-saturated, because \(7+\epsilon_w\le11\).

## 3. Common-neighbour cover

For each \(s\in\{3,4,5,6\}\), define
\[
S_s=\{u\in U:\ u\text{ is adjacent to every vertex of }C_s\}.
\]
The first saturation fact gives \(U=S_3\cup S_4\cup S_5\cup S_6\), so
\[
29=|U|\le |S_3|+|S_4|+|S_5|+|S_6|. \tag{2}
\]

We prove the opposite bound \( \sum_s |S_s|\le28\).

### 3.1. A label and extra-edge accounting rule

For each part-saturated \(w\), choose one U-part \(P(w)\in\{A,B,C,D\}\) to which it is complete. Define its extra-edge load
\[
r_w=d_H(w,U)-|P(w)|.
\]
This is the number of its U-neighbours outside the chosen part. If \(P(w)\) is a small part, \(r_w=6-s+\epsilon_w\); if \(P(w)=D\), \(r_w=5-s+\epsilon_w\). In either case, the total load in \(C_s\), whenever all its vertices are labelled, is at most
\[
\sum_{w\in C_s}r_w\le
\begin{cases}
E_6,&s=6,\\
5+E_5,&s=5,\\
8+E_4,&s=4,\\
9+E_3,&s=3.
\end{cases} \tag{3}
\]
A vertex \(u\in S_s\) lying outside the chosen label part of \(w\) consumes one of the extra edges counted by \(r_w\).

### 3.2. The \(K_6\) component

No five vertices of \(C_6\) can all be labelled to the same small part, and no four can all be labelled to \(D\), since either would create a \(K_{12}\). Thus, for any \(u\in S_6\), at least two of the six vertices of \(C_6\) have a label different from the part containing \(u\). The two corresponding edges to \(u\) are extra edges. By (3),
\[
\boxed{|S_6|\le\lfloor E_6/2\rfloor.} \tag{4}
\]

### 3.3. The \(K_5\) component

A full common label is impossible: \(K_5\) joined to any U-part of size at least seven contains a \(K_{12}\). Therefore every \(u\in S_5\) needs at least one extra edge from \(C_5\), and (3) gives \(|S_5|\le5+E_5\), provided all vertices are labelled.

If a vertex of \(C_5\) is not part-saturated, (1) forces its excess to be four. The other four vertices of \(C_5\) then have excess zero and U-degree eight. Since every \(u\in S_5\) is adjacent to each of those four vertices, \(|S_5|\le8\le5+E_5=9\). Hence in all cases
\[
\boxed{|S_5|\le5+E_5.} \tag{5}
\]

### 3.4. The \(K_4\) component

If the four vertices are not all labelled to one part, each \(u\in S_4\) requires at least one extra edge, so \(|S_4|\le8+E_4\).

A full label to \(D\) is forbidden by \(K_4\cup D\cong K_{12}\). If all four vertices are labelled to a small part \(P\), then \(P\subseteq S_4\) and \(|P|=7\). Every additional vertex of \(S_4\setminus P\) requires four extra edges, while the total extra-edge load is \(8+E_4\). Thus
\[
|S_4|\le7+\left\lfloor\frac{8+E_4}{4}\right\rfloor
\le8+E_4+\mathbf1_{\{E_4=0\}}.
\]
If a vertex of \(C_4\) is not part-saturated, (1) gives excess at least three; since the total excess is four, another vertex of \(C_4\) has excess zero and U-degree nine, so \(|S_4|\le9\), also within the bound. Therefore
\[
\boxed{|S_4|\le8+E_4+\mathbf1_{\{E_4=0\}}.} \tag{6}
\]

### 3.5. The \(K_3\) component

If its vertices are not all labelled to one part, every \(u\in S_3\) needs at least one extra edge, giving \(|S_3|\le9+E_3\).

If all three are labelled to a part \(P\), then \(|P|\in\{7,8\}\), \(P\subseteq S_3\), and each extra vertex of \(S_3\setminus P\) requires three extra edges. The total extra-edge load is \(9+E_3\) for a small label and \(6+E_3\) for label \(D\). In either case,
\[
|S_3|\le10+\lfloor E_3/3\rfloor
\le9+E_3+\mathbf1_{\{E_3=0\}}.
\]

If a vertex of \(C_3\) is not part-saturated, (1) gives excess at least two. Among the other two vertices there is one with excess at most one, hence U-degree at most eleven. Therefore \(|S_3|\le11\le9+E_3\). We conclude
\[
\boxed{|S_3|\le9+E_3+\mathbf1_{\{E_3=0\}}.} \tag{7}
\]

## 4. Contradiction

Combining (4)–(7) and \(E_3+E_4+E_5+E_6=4\),
\[
\begin{aligned}
\sum_s|S_s|
&\le \lfloor E_6/2\rfloor+(5+E_5)
 +(8+E_4+\mathbf1_{\{E_4=0\}})
 +(9+E_3+\mathbf1_{\{E_3=0\}})\\
&=26-\lceil E_6/2\rceil
 +\mathbf1_{\{E_4=0\}}+\mathbf1_{\{E_3=0\}}\\
&\le28.
\end{aligned}
\]
The last inequality is immediate if \(E_6=0\), since the two indicators contribute at most two; if \(E_6\ge1\), the base term is at most 25 and the indicators contribute at most two. This contradicts (2), which requires the sum to be at least 29.

Therefore the \(\delta=14,\epsilon_U=0\), four-partite profile \(H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\) is **excluded**.

## 5. Scope

Together with DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, this excludes the \((4,4,5,5)\)+two-cross-edge, \((4,4,4,6)\)+one-cross-edge, and \((3,4,5,6)\)+zero-cross-edge W profiles at \(\delta=14,\epsilon_U=0\). The \((3,5,5,5)\)+one-cross-edge profile remains open, as do \(\epsilon_U=1,2\), the \(\delta=14\) non-four-partite branch, and all \(\delta\le13\) cases. E407 Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
