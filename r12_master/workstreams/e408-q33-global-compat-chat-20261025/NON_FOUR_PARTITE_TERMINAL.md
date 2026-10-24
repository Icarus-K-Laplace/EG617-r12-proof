# Non-four-partite terminal: exact packing and degree contract

Date: 2026-10-25  
Status: **OPEN.** The second-Turán edge bound does not exclude the current interval. This file records the exact finite contract that any non-four-partite completion must satisfy.

## 1. Contract

Let H be the 47-vertex core with
\[
e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
d_H(x)=12+\epsilon_x,\quad \epsilon_x\ge0,\quad \sum_H\epsilon_x=4.
\]
Let U be the 31-point support of the 56 selected independent four-sets \(\mathcal Q\), and W=H\U, |W|=16. Put
\[
L=\overline{H[U]},\quad e(L)=336+\delta,\quad
\epsilon_U=\sum_{u\in U}\epsilon_u,\quad S_0=\epsilon_U+2\delta.
\]
Each Q in \(\mathcal Q\) is a K4 in L. The 56 K4 edge sets are pairwise edge-disjoint. They are seven labeled witnesses from each of eight exact-129 colors; within a color the seven sets are disjoint, and across colors distinct sets intersect in at most one vertex.

The retained universal boundary theorem gives \(S_0\ge12\). The core degree ledger gives
\[
e_H(U,W)=114+S_0,\qquad
e(H[W])=41-\delta-\epsilon_U.
\]
Since \(\alpha(H[W])\le4\), Turán's minimum-edge bound gives \(e(H[W])\ge24\), hence
\[
\delta+\epsilon_U\le17.
\]
As \(\epsilon_U\le4\), it follows that
\[
4\le\delta\le17,\qquad 340\le e(L)\le353.
\]

## 2. Why the second-Turán bound does not close this branch

The graph L is K5-free because \(\alpha(H[U])\le4\). If L is not four-partite, Brouwer's second-Turán bound gives
\[
e(L)\le t_4(31)-\lfloor31/4\rfloor+1
=360-7+1=354.
\]
Our interval reaches 353, one edge below this maximum. Therefore the general second-Turán edge count alone does **not** exclude the non-four-partite branch. It also does not imply that L is four-partite.

The packing-specific input still needed is a stability/incidence theorem that uses the fact that 336 of the 340–353 edges are partitioned into 56 edge-disjoint K4 witnesses.

## 3. Exact vertex-incidence identities

For \(u\in U\), define
\[
r_u=|\{Q\in\mathcal Q:u\in Q\}|.
\]
There are 56 four-sets, so
\[
\sum_{u\in U}r_u=224.
\]
Each color contributes seven pairwise-disjoint Q-sets, so a vertex occurs at most once per selected color:
\[
1\le r_u\le8.
\]
Consequently, the total omission count is
\[
\sum_{u\in U}(8-r_u)=8\cdot31-224=24.
\]

Let \(\ell_u\) be the number of leftover L-edges incident to u, where a leftover edge is an edge not used by any of the 56 selected K4s. There are exactly \(\delta\) such edges, hence
\[
\sum_{u\in U}\ell_u=2\delta.
\]
Because Q-sets containing u have no common second vertex, their 3-neighbour sets are disjoint. Thus the exact degree identity is
\[
d_L(u)=3r_u+\ell_u.
\]
As \(|U|=31\),
\[
d_H(u,U)=30-d_L(u),
\]
and therefore
\[
\boxed{d_H(u,W)=3r_u+\ell_u-18+\epsilon_u\ge0.} \tag{1}
\]
This is a vertex-by-vertex constraint, not merely a total edge count.

For every \(w\in W\), let \(q_w=|N_H(w)\cap U|\). Since w must hit every independent four-set Q, otherwise \(Q\cup\{w\}\) is an independent five-set in H, the retained transversal theorem gives \(q_w\ge7\). Moreover,
\[
\sum_{w\in W}q_w=e_H(U,W)=114+S_0.
\]
The remaining induced graph has
\[
e(H[W])=41-\delta-\epsilon_U\ge24.
\]

## 4. Labeled color constraints that must remain attached

The 56 K4s are not anonymous graph motifs. Each is the H-part of a specific isolated K5 component of an exact-129 color C, with its fifth vertex in the 61-point residual outside H. For each selected Q:
- Q is independent in H and a K4 in L;
- its four vertices form one isolated C-colored K5 component together with its component label;
- two Q-sets from different colors intersect in at most one vertex, by unique edge ownership;
- no pair of vertices can be assigned two different non-target colors.

The finite reduction must preserve these labels. It is invalid to replace the 56 Q-sets by arbitrary K4s of L, or to assume every K4 in L is one of the selected witnesses.

## 5. Remaining finite mathematical contract

A non-four-partite terminal is a tuple
\[
(H,U,W,L,\mathcal Q,\lambda)
\]
satisfying all of the following simultaneously:

1. \(|V(H)|=47\), \(e(H)=284\), \(\alpha(H)\le4\), \(\omega(H)\le11\), \(\delta(H)\ge12\), and \(\sum\epsilon_x=4\).
2. \(|U|=31\), \(|W|=16\), \(L=\overline{H[U]}\) is K5-free and non-four-partite.
3. \(e(L)=336+\delta\), \(4\le\delta\le17\), \(\delta+\epsilon_U\le17\), and \(S_0=\epsilon_U+2\delta\ge12\).
4. \(\mathcal Q\) consists of 56 labeled independent four-sets, seven per exact-129 color, with pairwise intersections at most one and union U.
5. The 56 K4 edge sets are disjoint; the remaining \(\delta\) edges of L are precisely the leftover edges counted by \(\ell_u\).
6. For every \(u\in U\), \(d_L(u)=3r_u+\ell_u\) and \(d_H(u,W)=3r_u+\ell_u-18+\epsilon_u\ge0\).
7. For every \(w\in W\), \(q_w\ge7\), \(\sum q_w=114+S_0\), and \(e(H[W])=41-\delta-\epsilon_U\ge24\).
8. The exact-129 factor theorem, the shell-label/hub-hit constraints, and the seven-block global incidence ledger in SEVEN_BLOCK_INCIDENCE_LEDGER.md all hold.

**No contradiction is claimed.** The unresolved theorem must use the labeled K4-packing together with (1), the W-transversal system, or the global seven-block incidence constraints. The generic K5-free edge bound alone is insufficient.
