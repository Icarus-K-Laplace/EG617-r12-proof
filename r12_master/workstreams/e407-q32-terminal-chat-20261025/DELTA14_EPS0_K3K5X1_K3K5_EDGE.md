# E407 Q32: exclude the \(\delta=14,\epsilon_U=0\), \(K_3\cup K_5^3\) profile when its cross-edge joins \(K_3\) to a \(K_5\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract and four-partite W-profile classification.

## 1. Contract and notation

Assume
\[
e(H)=284,\quad |U|=29,\quad |W|=18,\quad
\alpha(H)\le4,\quad \omega(H)\le11,\quad
\epsilon_U=0,\quad \delta=14.
\]
The complement \(L=\overline{H[U]}\) is four-partite with parts \(A,B,C,D\) of sizes \(7,7,7,8\). The seven cross-edges of \(H[U]\) have distinct endpoints in \(A\cup B\cup C\); a vertex of \(D\) may support more than one. Write \(t_d=d_{H[U]}(d)-7\). Whole-component saturation for \(d\in D\) gives
\[
\sum_{d\in D}t_d=7,\qquad 0\le t_d\le2.
\]
All excess lies in \(W\): \(\epsilon_w=d_H(w)-12\ge0\) and \(\sum_{w\in W}\epsilon_w=4\).

Suppose \(H[W]\) consists of \(T\cong K_3\) and three \(K_5\)'s \(P,Q,R\), with the sole cross-edge \(ab\), where \(a\in T\) and \(b\in P\). Let \(t_1,t_2\) be the other two vertices of \(T\).

## 2. The only unsaturated U-vertices form a rigid set \(X\)

Every \(u\in U\) has at most six neighbours in \(W\): a small-part vertex has six or seven U-neighbours, and a \(D\)-vertex has \(7+t_d\le9\) U-neighbours. If \(u\) is not complete to any of \(T,P,Q,R\), an independent transversal can be blocked only by the cross-edge \(ab\). Its non-neighbour sets in \(T,P\) must therefore be exactly \(\{a\},\{b\}\), forcing
\[
N_H(u,W)=(T\setminus\{a\})\cup(P\setminus\{b\}),\qquad
d_H(u,W)=6,\quad d_H(u,U)=6.
\]
Such a vertex lies in a small U-part and is not an endpoint of a cross-edge of \(H[U]\). Let \(X\) be the set of these vertices. Every vertex outside \(X\) belongs to at least one of the common-neighbour sets \(S_T,S_P,S_Q,S_R\), where \(S_C\) denotes the U-vertices complete to the W-component \(C\). Hence
\[
29\le |X|+|S_T|+|S_P|+|S_Q|+|S_R|. \tag{1}
\]

## 3. Component-capacity bounds

The reverse-saturation lemma in DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md applies to W-vertices: if a W-vertex is not complete to any U-part, it has at least 12 U-neighbours. Using U-part labels and extra-edge loads gives
\[
|S_P|\le4+\epsilon_P,\qquad
|S_Q|\le5+\epsilon_Q,\qquad
|S_R|\le5+\epsilon_R. \tag{2}
\]
For completeness, the endpoint \(b\) has U-degree \(7+\epsilon_b\le11\) and is always part-saturated. A non-endpoint vertex of \(P\) or \(Q\) can fail part-saturation only if its excess is four; then the endpoint has excess zero and U-degree seven, directly giving \(|S_P|\le7\le4+\epsilon_P\) (or the analogous bound for \(Q\)). In \(R\), the same exceptional excess-four case gives \(|S_R|\le8\le5+\epsilon_R\). Otherwise the label-load argument applies: no whole \(K_5\) can have all five labels equal to one U-part, and the total extra-edge loads are at most \(4+\epsilon_P\), \(4+\epsilon_Q\), and \(5+\epsilon_R\).

Put \(E_T=\sum_{w\in T}\epsilon_w\). The degree identities are
\[
d_H(a,U)=9+\epsilon_a,\qquad
d_H(t_i,U)=10+\epsilon_{t_i}\quad(i=1,2).
\]

## 4. Case I: \(T\) is not complete to \(D\)

For each \(d\in D\), the unique cross-edge in \(H[W]\) cannot block an independent transversal using only five W-neighbours. Thus \(d\) is complete to a whole W-component. If \(t_d>0\), then \(d_H(d,W)=5-t_d\le4\), so \(d\) must be complete to \(T\). If \(t_d=0\), it is either complete to \(T\) or anticomplete to \(T\) and complete to a \(K_5\). Consequently the three vertices of \(T\) have the same D-neighbourhood, say \(D_0\), of size \(h\). Since \(\sum t_d=7\) and \(t_d\le2\), \(h\ge4\).

If \(h<8\), every \(w\in T\) is not complete to \(D\). It must be complete to a small U-part: otherwise the reverse-saturation lemma would give a non-neighbour \(d\in D\) with \(t_d>0\), but such a \(d\) is complete to \(T\). Hence
\[
9+\epsilon_a\ge7+h,\qquad
10+\epsilon_{t_i}\ge7+h.
\]
It follows that \(E_T\ge(h-2)+2(h-3)=3h-8\). The global excess budget forces \(h=4\) and
\[
\epsilon_a=2,\qquad \epsilon_{t_1}=\epsilon_{t_2}=1,\qquad E_T=4.
\]
Each vertex of \(T\) then has exactly 11 U-neighbours, namely \(D_0\) and one whole small U-part. Call those labelled parts \(A_a,A_1,A_2\).

- If all three labels are the same part \(A_0\), then \(X=\varnothing\) (each \(x\in X\) is nonadjacent to \(a\), which is complete to \(A_0\)), and \(S_T=D_0\cup A_0\), so \(|S_T|=11\).
- If the labels are not all the same and \(A_1\ne A_2\), then \(X=\varnothing\), because any \(x\in X\) must be adjacent to both \(t_1,t_2\) and lie in \(A_1\cap A_2\). Also \(S_T=D_0\), so \(|S_T|=4\).
- The remaining possibility is \(A_1=A_2=A_0\) and \(A_a\ne A_0\). Then \(X\subseteq A_0\), so \(|X|\le7\), while \(S_T=D_0\) and \(|S_T|=4\).

In all three subcases, \(E_P=E_Q=E_R=0\), so (2) gives \(|S_P|+|S_Q|+|S_R|\le14\). The right-hand side of (1) is at most \(11+14=25\), \(4+14=18\), or \(7+4+14=25\), respectively. Each is less than 29. Thus \(T\) must be complete to \(D\).

## 5. Case II: \(T\) is complete to \(D\)

Now \(D\subseteq S_T\). Since the three vertices of \(T\) are labelled by \(D\), every member of \(S_T\setminus D\) uses three extra edges, and the total extra-edge load is
\[
(9+\epsilon_a-8)+(10+\epsilon_{t_1}-8)+(10+\epsilon_{t_2}-8)=5+E_T.
\]
Therefore
\[
|S_T|\le C_T:=8+\left\lfloor\frac{5+E_T}{3}\right\rfloor.
\]
Together with (2) and \(E_T+\epsilon_P+\epsilon_Q+\epsilon_R=4\), this gives
\[
|S_T|+|S_P|+|S_Q|+|S_R|
\le C_T+18-E_T.
\]
For \(E_T=0,1,2,3,4\), the respective upper bounds are \(27,27,26,25,25\). Also, every \(x\in X\) is adjacent to both \(t_1,t_2\), whose eight D-neighbours leave exactly \(2+\epsilon_{t_i}\) possible small-part neighbours. Hence
\[
|X|\le 2+\min(\epsilon_{t_1},\epsilon_{t_2})
\le 2+\left\lfloor\frac{E_T}{2}\right\rfloor.
\]
The resulting total upper bounds in (1) are \(29,29,29,28,29\). Thus only \(E_T\in\{0,1,2,4\}\) with \(|X|\) attaining its displayed maximum could conceivably reach 29.

In each such equality case, choose \(t_i\) with the smaller excess. Its number of small-part neighbours is exactly \(2+\min(\epsilon_{t_1},\epsilon_{t_2})=|X|\), and all of them are in \(X\). No small vertex outside \(X\) is adjacent to this \(t_i\), so \(S_T=D\) and \(|S_T|=8\). Replacing \(C_T\) by 8 lowers the corresponding total bounds to \(28,27,27,26\), respectively. All are less than 29. This contradicts (1).

Therefore the \(\delta=14,\epsilon_U=0\), four-partite W-profile \(K_3\cup K_5^3\) with its sole cross-edge joining \(K_3\) to a \(K_5\) is **EXCLUDED**.

## 6. Scope

Together with DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md, DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, and DELTA14_EPS0_K3K5X1_K5K5_EDGE.md, this excludes all four-partite W-profiles at \(\delta=14,\epsilon_U=0\). It does not close the \(\delta=14,\epsilon_U\in\{1,2\}\) rows, the \(\delta=14\) non-four-partite branch, any \(\delta\le13\) case, or E407 Q32 overall. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
