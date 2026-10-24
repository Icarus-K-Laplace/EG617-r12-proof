# R12 linear-witness transversal theorem and boundary-core budget

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL necessary-structure theorem** under the retained T61, exact-129 factor, and witness-packing contracts.  
Scope: the sharp support boundaries E407 Q32 (v=29, 49 witnesses) and E408 Q33 (v=31, 56 witnesses). This does not exclude either boundary.

## 1. Frozen contract

Let H be the 47-vertex core with
\[
\alpha(H)\le4,\quad \delta(H)\ge12,\quad e(H)=284,\quad
\sum_{x\in H}\epsilon_x=4,\qquad \epsilon_x=d_H(x)-12\ge0.
\]
The exact-129 witness-packing theorem supplies a linear family \(\mathcal Q\) of independent 4-sets in H:
- E407 Q32 at its unresolved boundary: m=49 sets and U=union Q, |U|=v=29;
- E408 Q33 at its unresolved boundary: m=56 sets and U=union Q, |U|=v=31.

“Linear” means |Q intersect Q'|<=1 for distinct Q,Q'. Let W=V(H) minus U. Each Q is a K4 in L=complement of H[U], and the six edges contributed by different Qs are disjoint.

## 2. A linear 4-set family of either boundary has transversal number at least seven

**Theorem 2.1.** In either boundary case, no set T subset U of size at most six meets every member of Q. Thus
\[
\tau(\mathcal Q)\ge7.
\]

**Proof.** Put t=|T|. Let n1 be the number of Qs meeting T in exactly one point and n2=m-n1 the number meeting T in at least two points.

For a fixed x in T, the three-point sets Q minus {x} from Qs satisfying Q intersect T={x} are pairwise disjoint subsets of U minus T: otherwise two Qs would intersect in both x and another point. Hence
\[
n_1\le t\left\lfloor\frac{v-t}{3}\right\rfloor. \tag{1}
\]
Also, each Q counted by n2 contains a pair from T, and no pair can occur in two Qs by linearity. Therefore
\[
n_2\le {t\choose2}. \tag{2}
\]
For E407, (1)+(2) already contradict m=49 for t<=4. For E408, they contradict m=56 for t<=5.

For the remaining cases use incidence counting. Any fixed point x belongs to at most floor((v-1)/3) members of Q, because the other triples in the Qs containing x are pairwise disjoint. Thus
\[
I(T):=\sum_{Q\in\mathcal Q}|Q\cap T|
\le t\left\lfloor\frac{v-1}{3}\right\rfloor. \tag{3}
\]
On the other hand every Q is hit, and every Q counted by n2 contributes at least one incidence above the baseline one. Hence
\[
I(T)\ge m+n_2\ge 2m-t\left\lfloor\frac{v-t}{3}\right\rfloor. \tag{4}
\]

For E407 (v,m,t)=(29,49,5), (4) gives I(T)>=98-40=58, while (3) gives I(T)<=5*9=45, impossible. For t=6, (4) gives I(T)>=98-42=56, while (3) gives I(T)<=6*9=54, impossible.

For E408 (v,m,t)=(31,56,t=6), (4) gives I(T)>=112-48=64, while (3) gives I(T)<=6*10=60, impossible. The smaller t cases were already excluded by (1)+(2). Thus no transversal of size at most six exists. QED.

## 3. Consequence: every outside core vertex has at least seven neighbours into U

For every w in W, the set N_H(w) intersect U meets every Q. Otherwise Q together with w would be an independent 5-set in H. Theorem 2.1 therefore gives
\[
\boxed{d_H(w,U)\ge7\quad\text{for every }w\in W.} \tag{5}
\]

This is stronger than the trivial “each outside vertex hits every witness” statement: it quantifies the minimum number of hits in the two exact support-boundary kernels.

## 4. Exact E407 boundary budget (v=29, m=49)

Write
\[
\delta=e(L)-294\ge0,\qquad \epsilon_U=\sum_{u\in U}\epsilon_u,\qquad
\epsilon_W=4-\epsilon_U.
\]
Since binom(29,2)=406,
\[
e(H[U])=112-\delta.
\]
The exact degree and edge identities give
\[
e_H(U,W)=348+\epsilon_U-2e(H[U])
=124+2\delta+\epsilon_U, \tag{6}
\]
and
\[
e(H[W])=284-e(H[U])-e_H(U,W)
=48-\delta-\epsilon_U. \tag{7}
\]
Because alpha(H[W])<=4, Turan's complement form gives e(H[W])>=p_4(18)=32. Thus
\[
\boxed{\delta+\epsilon_U\le16.} \tag{8}
\]
Equation (5) gives e_H(U,W)>=7|W|=126. Combining with (6),
\[
\boxed{\epsilon_U+2\delta\ge2.} \tag{9}
\]
Finally, L is K5-free and the edge budget gives e(L)=294+delta<=310, hence the unconditional bound is 0<=delta<=16. If L were complete four-partite, the 49 edge-disjoint K4 witnesses force part sizes (8,7,7,7), whose complete four-partite graph has 315 edges, contradicting e(L)<=310. This only rules out a complete four-partite graph; a non-complete four-partite subgraph is not excluded.

If L is separately proved non-four-partite, Brouwer's second-Turan bound gives e(L)<=309 and therefore delta<=15. In particular, delta=16 forces L to be four-partite, with parts (8,7,7,7) and five cross-part edges deleted from the complete four-partite graph. The 49 witnesses use 294 distinct edges, leaving 16 existing edges not used by witnesses, so the present arithmetic does not rule this branch out.

So the unconditional E407 boundary window is
\[
0\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad \epsilon_U+2\delta\ge2.
\]
In particular, the zero-extra-edge case delta=0 forces at least two of the four core-excess units to lie inside U.

## 5. Exact E408 Q33 boundary budget (v=31, m=56)

Now binom(31,2)=465. Put
\[
\delta=e(L)-336\ge0,\qquad \epsilon_U=\sum_{u\in U}\epsilon_u.
\]
Then
\[
e(H[U])=129-\delta,
\]
\[
e_H(U,W)=372+\epsilon_U-2e(H[U])
=114+2\delta+\epsilon_U,
\]
and
\[
e(H[W])=284-e(H[U])-e_H(U,W)
=41-\delta-\epsilon_U.
\]
Since alpha(H[W])<=4, e(H[W])>=p_4(16)=24, giving
\[
\boxed{\delta+\epsilon_U\le17.} \tag{10}
\]
The transversal theorem requires at least 7|W|=112 cross edges; the exact identity already gives 114+2delta+epsilon_U, so this condition is automatically met but confirms that the boundary has at least two cross-edge incidences above the seven-per-vertex floor.

Thus the E408 boundary window is
\[
0\le\delta\le17,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le17.
\]
The K5-free complement L cannot be complete four-partite: the 56 edge-disjoint K4 witnesses force every pair of part sizes to have product at least 56, which on 31 vertices forces part sizes (8,8,8,7) and hence 360 edges, contradicting e(L)<=353. This does not prove that L is non-four-partite. A four-partite subgraph with up to seven cross-part edges deleted has 353 edges and is not ruled out by the current budget. Brouwer's non-four-partite bound is 354, weaker than e(L)<=353, so it does not tighten the boundary window.

## 6. Interpretation and status firewall

The theorem proves a seven-neighbour transversal floor for every core vertex outside the selected witness support. It also turns the two support boundaries into explicit integer windows coupling:
- the number of extra complement edges beyond the witness K4 packing;
- the placement of the four core-degree-excess units;
- the induced edge budget on the remaining 18- or 16-vertex graph.

This is not yet a contradiction. In particular, the bounds e(H[W])>=32 for E407 and e(H[W])>=24 for E408 are compatible with the displayed upper bounds. The remaining attack must use the labelled shell rows, the exact-129 color classes, and the induced H[W] structure to eliminate the surviving integer windows.

The invalid m=10 star dichotomy from the emergency sprint is not used: a tripartite complement need not be complete tripartite. The attempted E408 outer-block contradiction that promoted omega(C[R])<=5 to a global clique bound is also not used; its correction remains in the sibling audit file. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 7. Subsequent four-partite refinement

R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.md now excludes the \(S_0=10\) equality kernel under the additional hypothesis that L is four-partite. Thus the four-partite E408 Q33 boundary has \(S_0=\epsilon_U+2\delta\ge11\). The non-four-partite branch remains open; the edge count \(e(L)\le353\) alone does not decide four-partiteness.
