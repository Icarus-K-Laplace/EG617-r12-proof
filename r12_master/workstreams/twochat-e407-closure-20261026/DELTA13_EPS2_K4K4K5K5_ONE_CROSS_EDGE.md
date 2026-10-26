# E407 Q32 — delta 13, epsilon_U 2, (4,4,5,5) plus one W-cross-edge

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the frozen 47-core / 49-witness contract, four-partite support-complement hypothesis, and exact W-profile hypothesis.

## Theorem

There is no E407 Q32 core H satisfying all of the following:
\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
\delta(H)\ge12,\quad \sum_{v\in H}\epsilon_v=4,
\]
where \(\epsilon_v=d_H(v)-12\ge0\), with a 29/18 support split \(U\dot\cup W\), \(\delta=13\), \(\epsilon_U=2\), and
\[
e(H[U])=99,\quad e(H[W])=33,\quad e_H(U,W)=152.
\]
Assume \(L=\overline{H[U]}\) is four-partite with parts \(P_1,P_2,P_3,D\) of sizes \(7,7,7,8\), and \(H[W]\) consists of clique parts \(C_1,C_2\cong K_4\), \(C_3,C_4\cong K_5\), with exactly one edge between two distinct parts.

## 1. The exact U-side structure

The 49 linear support blocks force every pair between two of \(P_1,P_2,P_3\) to occur exactly once as a witness pair. Since
\[
e(H[U])=99,\qquad
\sum_{i=1}^3\binom{7}{2}+\binom{8}{2}=91,
\]
there are exactly eight H-edges between different U-parts. They all join D to \(P_1\cup P_2\cup P_3\), and each vertex in a small part \(P_i\) is incident to at most one such edge. This is the standard four-partite support consequence recorded in the Round 31 source proof.

For \(d\in D\), put
\[
t_d=|N_H(d)\cap(P_1\cup P_2\cup P_3)|.
\]
Then
\[
\sum_{d\in D}t_d=8,\qquad
d_H(d,W)=5+\epsilon_d-t_d,\qquad
\sum_{d\in D}\epsilon_d\le\epsilon_U=2.
\]
In particular, every \(d\in D\) has \(d_H(d,W)\le7\).

The total W-excess is
\[
E_W:=\sum_{w\in W}\epsilon_w=4-\epsilon_U=2.
\]
A non-endpoint vertex of a K4 part has \(d_H(w,U)=9+\epsilon_w\); an endpoint of the unique W-cross-edge in a K4 part has \(d_H(w,U)=8+\epsilon_w\).

## 2. D-vertices and the one-cross-edge blocker

Call \(d\in D\) **assigned** if it is complete to one W clique part. It cannot be complete to two parts, because two parts have at least \(4+4=8\) vertices while \(d_H(d,W)\le7\).

If d is not assigned, choose one non-neighbour of d in each of the four W clique parts. Every such transversal must contain an H-edge, or it would form an independent 5-set with d. Since the only W-cross-edge is xy, the non-neighbour sets in the two endpoint parts must be exactly the singleton endpoints x and y. Thus d is adjacent to all other vertices of both endpoint parts. Consequently:
- a K4–K4 cross-edge requires \(d_H(d,W)\ge6\);
- a K4–K5 cross-edge requires \(d_H(d,W)\ge7\);
- a K5–K5 cross-edge requires \(d_H(d,W)\ge8\), impossible here.

In every case an unassigned d has \(t_d\le\epsilon_d-1\). If assigned to a K4 part, \(t_d\le1+\epsilon_d\); if assigned to a K5 part, \(t_d\le\epsilon_d\).

Let z be the number of unassigned D-vertices and q5 the number assigned to K5 parts. Summing these bounds gives
\[
8=\sum_D t_d\le (8-q_5-z)+\sum_D\epsilon_d-z
=8-q_5-2z+\sum_D\epsilon_d.
\]
Therefore
\[
q_5+2z\le\sum_D\epsilon_d\le2. \tag{1}
\]
So z is either 0 or 1, and \(q_5\le2\).

## 3. Case z=0: the assigned-component external-edge budget

All D-vertices are assigned. Let R be the number of D–W edges whose W endpoint lies outside the component to which that D-vertex is assigned. An assigned K4 vertex contributes \(1+\epsilon_d-t_d\) to R; an assigned K5 vertex contributes \(\epsilon_d-t_d\). Hence
\[
R=(8-q_5)+\sum_D\epsilon_d-\sum_Dt_d
=\sum_D\epsilon_d-q_5\le2. \tag{2}
\]
At least six D-vertices are assigned to the two K4 parts, so one K4 part C receives k at least 3 assignments. If k=8, then C union D is a K12, impossible. Thus \(3\le k\le7\).

Let m be the number of vertices of C complete to all eight vertices of D. Each of the other \(8-k\) D-vertices is assigned to a different W part, so if it is adjacent to a vertex counted by m, that edge contributes to R. Therefore
\[
m(8-k)\le R\le2.
\]
This gives the following lower bound on the number of vertices of C not complete to D:

| k | maximum m | at least \(4-m\) vertices not complete to D |
|---:|---:|---:|
| 3 | 0 | 4 |
| 4 | 0 | 4 |
| 5 | 0 | 4 |
| 6 | 1 | 3 |
| 7 | 2 | 2 |

**Lemma 3.1.** Every vertex w of C not complete to D is complete to one of the three small U-parts.

Proof. Since every D-vertex is assigned, \(t_d\le3\). Suppose w is not complete to any U-part. Let \(D'\) be its non-neighbour set in D. For each \(d\in D'\), every triple of non-neighbours of w in \(P_1,P_2,P_3\) must contain a U-edge to d, or w, d and that triple would be an independent 5-set. Hence at least one of the three small-part non-neighbour sets has size at most \(t_d\le3\). Distinct d in \(D'\) force distinct small parts, because each small-part vertex has at most one D-neighbour. If \(|D'|=1,2,3\), the number of non-neighbours of w in U is at most \(18,15,12\), respectively, so \(d_H(w,U)\ge11\).

A K4 non-endpoint has U-degree \(9+\epsilon_w\le11\), and an endpoint has U-degree \(8+\epsilon_w\le10\). Thus the only possible unassigned w in C is a non-endpoint with \(\epsilon_w=2\). There can be at most one such vertex because \(E_W=2\). But the table above guarantees at least two vertices of C not complete to D. A second such vertex has excess zero and U-degree 8 or 9; it is neither unassigned (which requires U-degree at least 11) nor complete to a small part (which, with k D-neighbours, requires at least \(7+k\ge10\) U-neighbours). Contradiction. Therefore every vertex of C not complete to D is complete to a small U-part. \(\square\)

A non-endpoint w of C not complete to D now has at least \(7+k\) U-neighbours, so \(9+\epsilon_w\ge7+k\), or \(\epsilon_w\ge k-2\). An endpoint has the stronger bound \(\epsilon_w\ge k-1\). Consequently the W-excess needed by the vertices not complete to D is at least
\[
(4-m)(k-2)\in\{4,8,12,12,10\}
\]
for \(k=3,4,5,6,7\), respectively. Every value exceeds \(E_W=2\), contradiction. Thus z=0 is impossible.

## 4. Case z=1: the unique exceptional D-vertex

Equality in (1) forces
\[
q_5=0,\quad \sum_D\epsilon_d=2,
\]
and equality in every individual t-bound. The unique unassigned vertex \(d_0\) has \(t_{d_0}=\epsilon_{d_0}-1\), hence \(d_H(d_0,W)=6\). Therefore the W-cross-edge must join the two K4 parts, and \(d_0\) is adjacent to exactly the three non-endpoint vertices in each K4 and to no K5 vertex. The other seven D-vertices are assigned to K4 parts. Also \(t_d\le2\) for every d in D.

At least one K4 part C receives k at least 4 of the seven assigned D-vertices.

If k=7, the endpoint of the W-cross-edge in C is not adjacent to \(d_0\), so it is not complete to D. Since \(t_d\le2\), the same transversal argument as Lemma 3.1 shows that every K4 vertex is complete to a U-part: a vertex not complete to any U-part would have U-degree at least 12, whereas a K4 vertex has U-degree at most 11. The selected endpoint would then have at least \(7+7=14\) U-neighbours, but its U-degree is at most 10. Contradiction.

If k is 4, 5, or 6, every vertex of C is not complete to D: the three non-endpoint vertices see k assigned D-vertices plus \(d_0\), and the cross-edge endpoint sees the k assigned vertices but not \(d_0\). As \(t_d\le2\), every vertex of C is complete to a U-part. Since none is complete to D, that U-part must be one of the small parts \(P_1,P_2,P_3\). A non-endpoint vertex has at least \(7+(k+1)\) U-neighbours, and the endpoint has at least \(7+k\). Their exact U-degrees are \(9+\epsilon_w\) and \(8+\epsilon_w\), respectively, so all four vertices require \(\epsilon_w\ge k-1\ge3\). This requires at least 12 W-excess units, contradicting \(E_W=2\).

Thus z=1 is impossible as well.

## Conclusion and scope

Both cases are impossible. Hence the four-partite-L profile
\[
\delta=13,\quad \epsilon_U=2,\quad
H[W]=K_4\cup K_4\cup K_5\cup K_5
\text{ plus one W-cross-edge}
\]
is **EXCLUDED** under the frozen core/witness and row-profile contracts.

This closes that one four-partite \(\delta=13,\epsilon_U=2\) W-profile. It does not close \(\delta=13,\epsilon_U=0\), non-four-partite L, \(\delta\le12\), the five shell templates globally, or the original \(K_{145}\)-to-T61 bridge. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
