# E407 Q32 — delta=12 four-partite-U epsilon_U=3 closure

Date: 2026-10-28  
Status: **PROVED / CLOSED under the frozen delta=12 four-partite support kernel, W-profile list, and support-block W-capacity theorem.** No Didin input is used. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Kernel and low-omission sets

Use the exact kernel
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad |T_i|=7,\quad |R|=8,
\]
from `DELTA12_FOURPARTITE_SUPPORT_KERNEL.md`.

For r in R let q=r_r be its omission weight and h_i(r) the number of target leave edges from r into T_i. Then
\[
0\le h_i(r)\le q,
\qquad h_r=\sum_i h_i(r),
\qquad d_W(r)=5+\epsilon_r-h_r.
\tag{1.1}
\]
Also
\[
\sum_{r\in R}r_r=7.
\tag{1.2}
\]

Fix r with q<=1 and define
\[
A_i=T_i\setminus N_H(r).
\]
Then
\[
|A_i|=7-h_i(r)\ge6.
\tag{1.3}
\]
If w in W is nonadjacent to r, then w must be complete to at least one A_i; otherwise choose a nonneighbor t_i in each A_i and obtain the independent five-set {r,t1,t2,t3,w}.

Call such an i a label of w.

At epsilon_U=3 the W-excess is exactly one:
\[
\epsilon_W=1.
\tag{1.4}
\]
For a q=0 clique component of size s, a W vertex has support slack
\[
y_w=d_U(w)-7=6+\epsilon_w-s.
\tag{1.5}
\]
If two nonadjacent W vertices have the same A_i label, their U-neighborhood intersection has size at least six. The support-block W-capacity theorem would then require
\[
y_w+y_{w'}\ge6.
\tag{1.6}
\]
The single W-excess unit will make this impossible across different components in the two q=0 profiles below.

## 2. q=0 profile K3 + K5 + K5 + K5

The base support slacks are 3,1,1,1; the one excess unit raises at most one of these by one. Thus any pair from distinct components has slack sum at most five. By (1.6), two r-nonneighbours in different components cannot share a label.

With four components and only three labels, at least one whole W-component is target-adjacent to r.

We claim
\[
d_W(r)\ge6-h_r.
\tag{2.1}
\]
If the full component is K3, the three remaining K5 components use distinct labels. A K5 assigned label i can have all five vertices nonadjacent to r only when |A_i|<=6, equivalently h_i=1; if h_i=0, K5 union A_i is K12, so that K5 contributes at least one r-neighbour. Since h_i in {0,1}, at least 3-h_r of the three K5s have h_i=0. Hence
\[
d_W(r)\ge3+(3-h_r)=6-h_r.
\]
If the full component is K5, the degree is already five. For h_r>=1 this is at least 6-h_r; for h_r=0 each of the other two non-full K5s with labels needs a neighbour, so the degree is at least seven. Thus (2.1) always holds.

## 3. q=0 profile K4 + K4 + K4 + K6

The base support slacks are 2,2,2,0; one excess unit raises at most one by one. Again every cross-component slack sum is at most five, so labels cannot repeat across distinct components. Hence r is complete to one W-component.

If the full component is K6, d_W(r)>=6>=6-h_r. If it is a K4, the remaining K6 receives some label i. Its r-nonneighbours, all complete to A_i, can number at most
\[
11-|A_i|=4+h_i
\]
without producing a clique larger than 11. Therefore the K6 contributes at least
\[
6-(4+h_i)=2-h_i
\]
additional r-neighbours. Thus
\[
d_W(r)\ge4+2-h_i\ge6-h_r.
\tag{3.1}
\]
So the same universal bound holds.

## 4. q=1 W-profile: K4 + K4 + K5 + K5 plus one cross edge

Now H[W] has the four clique components above and exactly one cross edge between two components.

For a nonadjacent cross-component pair, the support-slack sum is still at most five, so same-label reuse is impossible. Therefore, if all four components contain r-nonneighbours, the pigeonhole repetition of one of three labels can occur only on the two endpoints of the unique W-cross edge.

Moreover those two incident components can contain no other r-nonneighbour carrying the repeated label: such a vertex would be nonadjacent to the opposite endpoint and violate (1.6). Since the other two components need the other two labels, the two cross-edge components can have only their respective endpoint as r-nonneighbour. Thus r is adjacent to every other vertex in both components. Their combined contribution to d_W(r) is at least
\[
(4-1)+(4-1)=6
\]
even in the minimum-size case. Hence d_W(r)>=6>=6-h_r.

If some component has no r-nonneighbour, r is complete to that component. The same clique-cap minimization as for the q=0 `(4,4,5,5)` profile gives
\[
d_W(r)\ge6-h_r:
\]
- a full K5 gives degree at least five, and when h_r=0 the other K5 with an h=0 label contributes one more neighbour;
- a full K4 costs four, while the two K5 components together require at least max(0,2-h_r) additional neighbours.

Thus in the one-defect profile as well,
\[
\boxed{d_W(r)\ge6-h_r.}
\tag{4.1}
\]

## 5. Every omission-0/1 R point consumes excess

From (1.1) and the uniform bound from Sections 2–4,
\[
5+\epsilon_r-h_r=d_W(r)\ge6-h_r,
\]
so
\[
\boxed{r_r\le1\Longrightarrow\epsilon_r\ge1.}
\tag{5.1}
\]

But eight nonnegative omission weights sum to seven. At most three R points can have weight at least two; hence at least five R points satisfy r_r<=1. Equation (5.1) gives
\[
\epsilon_R\ge5.
\]
This contradicts epsilon_U=3.

Therefore
\[
\boxed{
\delta=12,\ L_U\text{ four-partite},\ \epsilon_U=3
\Longrightarrow\bot.
}
\]

## 6. Dependencies

The proof uses only:
1. the exact delta=12 four-partite `(7,7,7,8)` support kernel and leave identities;
2. the epsilon_U=3 W-profile list;
3. the support-block W common-neighbour capacity theorem;
4. pure alpha(H)<=4 and omega(H)<=11 reasoning.

No Didin theorem and no non-four-partite augmentation classification is used. The four-partite epsilon_U=0,1,2 branches remain open.