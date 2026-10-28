# E407 Q32 — delta=12 four-partite-U epsilon_U=4 closure

Date: 2026-10-28  
Status: **PROVED / CLOSED under the frozen delta=12 four-partite support kernel and support-block W-capacity theorem.** No Didin input is used. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Exact kernel

Use `DELTA12_FOURPARTITE_SUPPORT_KERNEL.md`. The 29-point support is
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad |T_i|=7,\quad |R|=8.
\]
Inside H[U], every T_i is K7, R is K8, the T_i are pairwise anticomplete, and all nine target cross edges run between R and the T-parts.

For r in R let r_r be its support omission count. Then
\[
\sum_{r\in R}r_r=7.
\tag{1.1}
\]
For each i, r has exactly r_r leave pairs into T_i; let h_i(r) be the number of those leave pairs that are target edges. Then
\[
0\le h_i(r)\le r_r,
\qquad h_r:=\sum_i h_i(r),
\]
and the pointwise W-degree identity is
\[
\boxed{d_W(r)=5+\epsilon_r-h_r.}
\tag{1.2}
\]

At epsilon_U=4 the whole four units of core excess lie in U, so epsilon_W=0. Also
\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5.
\tag{1.3}
\]
Hence a W vertex in a K4 component has
\[
d_U(w)=9,\quad y_w=d_U(w)-7=2,
\]
and a W vertex in a K5 component has
\[
d_U(w)=8,\quad y_w=1.
\tag{1.4}
\]
The support-block common-neighbour theorem says that if w,w' are nonadjacent in W,
\[
|N_U(w)\cap N_U(w')|\le y_w+y_{w'}\le4.
\tag{1.5}
\]

## 2. Low-omission R points force a whole W component

Fix r in R with
\[
q:=r_r\le2.
\]
For i=1,2,3 define
\[
A_i=T_i\setminus N_H(r).
\]
Since r has at most q target neighbours in each T_i,
\[
|A_i|=7-h_i(r)\ge7-q\ge5.
\tag{2.1}
\]

Let w in W be nonadjacent to r. If w were not complete to any A_i, choose t_i in A_i nonadjacent to w. The four vertices r,t_1,t_2,t_3 are independent because the T_i are pairwise anticomplete and each t_i is nonadjacent to r. Adding w gives an independent 5-set, contradicting alpha(H)<=4.

Therefore every W-nonneighbour of r is complete to at least one A_i. Assign such a w a label i.

If two r-nonneighbours w,w' lie in distinct W-components and receive the same label i, then they are H-nonadjacent and
\[
|N_U(w)\cap N_U(w')|\ge|A_i|\ge5,
\]
contradicting (1.5). Thus label sets used by different W-components are disjoint.

There are four W-components but only three labels. Therefore at least one W-component has no r-nonneighbour at all:
\[
\boxed{r\text{ is target-complete to an entire W-component}.}
\tag{2.2}
\]
In particular d_W(r)>=4.

## 3. Sharpen the degree lower bound using the K12 cap

We prove
\[
\boxed{d_W(r)\ge\max(4,6-h_r).}
\tag{3.1}
\]

The bound four is (2.2). It remains to handle h_r=0 or 1.

### h_r=0

All three sets A_i equal the full K7 part T_i. If a K5 W-component is not entirely adjacent to r and all five of its vertices are r-nonneighbours, then, because its label set is a singleton once the other nonempty components use disjoint labels, all five vertices are complete to the same T_i=K7. This would form K12. Hence every non-full K5 component contributes at least one r-neighbour.

If the full component from (2.2) is a K4, both K5 components require one additional r-neighbour, so d_W(r)>=4+2=6. If the full component is a K5, the other K5 requires one additional neighbour, so d_W(r)>=5+1=6. More than one full component only increases the degree. Thus d_W(r)>=6.

### h_r=1

Exactly one label i has h_i=1 and the other two have h=0. Again choose one full component. If it is a K5, d_W(r)>=5. If it is a K4, the remaining three components use the three labels. There are two remaining K5 components but only one positive-h label, so at least one K5 receives an h=0 label and therefore cannot be entirely composed of r-nonneighbours without creating K12. It contributes one additional r-neighbour. Hence d_W(r)>=4+1=5.

For h_r>=2, (2.2) already gives d_W(r)>=4. This proves (3.1).

## 4. Every low-omission R point consumes core excess

Combine (1.2) and (3.1):
\[
\epsilon_r=d_W(r)-5+h_r.
\]
If h_r=0, d_W(r)>=6 gives epsilon_r>=1. If h_r=1, d_W(r)>=5 gives epsilon_r>=1. If h_r>=2, d_W(r)>=4 gives
\[
\epsilon_r\ge h_r-1\ge1.
\]
Therefore
\[
\boxed{r_r\le2\Longrightarrow\epsilon_r\ge1.}
\tag{4.1}
\]

## 5. Global omission budget contradiction

There are eight R points and their omission weights are nonnegative integers summing to seven. At most two of them can be at least three. Hence at least six R points satisfy r_r<=2.

By (4.1), each of those six points carries at least one unit of U-excess. Therefore
\[
\epsilon_R\ge6.
\]
But the whole core has only four excess units and epsilon_U=4, contradiction.

Thus
\[
\boxed{
\delta=12,\ L_U\text{ four-partite},\ \epsilon_U=4
\Longrightarrow\bot.
}
\]

## 6. Dependency audit

This proof uses only:
1. the exact delta=12 four-partite support kernel `(7,7,7,8)` and its leave identities;
2. the support-block W common-neighbour capacity theorem;
3. the exact epsilon_U=4 W profile `K4+K4+K5+K5`;
4. pure alpha(H)<=4 and omega(H)<=11 reasoning.

It does not use the Didin preprint, the non-four-partite augmentation classification, or the five shell templates. The delta=12 four-partite branches epsilon_U=0,1,2,3 remain open.