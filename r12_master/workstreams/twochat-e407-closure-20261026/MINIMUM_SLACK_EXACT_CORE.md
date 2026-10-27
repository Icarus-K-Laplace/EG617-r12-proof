# E407 Q32 — minimum-slack exact-core reduction

Date: 2026-10-27  
Status: **PROVED necessary-structure theorem under the frozen 49-block contract. Terminal exclusion remains OPEN.**

## 1. Contract

Use the E407 Q32 core contract and notation from `SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md`.

Let

\[
Y:=\sum_{w\in W} y_w,\qquad y_w=d_H(w,U)-7.
\]

At the minimum scalar boundary

\[
\epsilon_U+2\delta=9
\]

there are exactly two feasible profiles:

\[
(\delta,\epsilon_U)=(3,3)\quad\text{or}\quad(4,1),
\]

and in either profile

\[
Y=7.
\]

Assume there exists an independent four-set

\[
I=\{w_1,w_2,w_3,v\}\subset W
\]

with total W-side slack one. Then, after relabelling,

\[
y_{w_1}=y_{w_2}=y_{w_3}=0,\qquad y_v=1.
\]

By the slack-one equality theorem, the four U-neighbourhoods partition U:

\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\]

where

\[
T_i=N_H(w_i,U),\quad |T_i|=7,\qquad
R=N_H(v,U),\quad |R|=8,
\]

and every one of the 49 support blocks contains exactly one point from each of the four parts.

For \(s\in R\), let \(r_s\) be its support-class omission multiplicity, so

\[
\sum_{s\in R}r_s=7.
\]

For each i, s is paired by support blocks with exactly \(7-r_s\) points of \(T_i\). Thus exactly \(r_s\) pairs in \(T_i\times\{s\}\) are missing from the selected block pairs.

## 2. Exact four-partite core structure

### Lemma 2.1 — the three seven-parts

The sets \(T_1,T_2,T_3\) are pairwise target-anticomplete and each induces a target \(K_7\).

**Proof.** Any pair between two different T-parts occurs in exactly one support block: there are 49 blocks and 49 possible pairs, and pairwise linearity forbids repetition. Hence all such pairs are nonedges of H.

Since \(\sum_R r_s=7<8\), choose \(s\in R\) with \(r_s=0\). Then s occurs in all seven color classes and is paired by the blocks with every point of every \(T_i\), hence is target-anticomplete to all three T-parts. If some \(T_i\) contained a target-nonedge xy, choose arbitrary points in the other two T-parts. Together with s these five vertices would be target-independent, contradicting \(\alpha(H)\le4\). Thus every \(T_i\) is a clique. \(\square\)

### Lemma 2.2 — R-side nonedge rule

If \(s,s'\in R\) are target-nonadjacent, then

\[
r_s+r_{s'}\ge7.
\]

**Proof.** In each \(T_i\), s has target neighbours only among its \(r_s\) missing block partners, and s' only among its \(r_{s'}\) missing partners. If \(r_s+r_{s'}<7\), choose in every \(T_i\) a point target-nonadjacent to both. The three chosen T-points are pairwise target-nonadjacent by Lemma 2.1, so together with s,s' they form an independent five-set. \(\square\)

### Lemma 2.3 — omission multiplicity is at most three

For \(s\in R\), let \(z_s\) be the number of its missing T-partner pairs which are also target-nonedges, i.e. extra complement edges beyond the 294 selected block pairs. Let \(q_s\) be the number of target-nonedges from s to \(R\setminus\{s\}\).

The number of target neighbours of s in the three T-parts is

\[
h_s=3r_s-z_s.
\]

Because v is complete to R, every s has at least one W-neighbour. Since its target degree inside R is \(7-q_s\),

\[
d_H(s,W)=12+\epsilon_s-(7-q_s)-h_s
=5+\epsilon_s+q_s-3r_s+z_s\ge1.
\]

Hence

\[
\epsilon_s+z_s+q_s\ge3r_s-4. \tag{1}
\]

Suppose \(r_s\ge4\). If \(q_s=0\), (1) requires at least eight units at s, but the total \(\epsilon_U+\delta\) is only 6 in profile (3,3) and 5 in profile (4,1). If \(q_s>0\), Lemma 2.2 forces the other endpoint of any R-nonedge to have omission at least three; because the total omission sum is seven, s can have only one R-nonedge. Then (1) still requires \(\epsilon_s+z_s\ge7\), again exceeding the global resource. Therefore

\[
\boxed{r_s\le3\quad\forall s\in R.}
\]

Lemma 2.2 now implies that R has no target-nonedge at all. Therefore

\[
\boxed{H[R]=K_8.}
\]

Consequently all \(\delta\) complement edges beyond the 294 selected block pairs occur among the 21 missing \(T_i\)-R partner pairs:

\[
\sum_{s\in R}z_s=\delta.
\]

Thus \(L_U=\overline{H[U]}\) is genuinely four-partite with parts \((7,7,7,8)\). The target edges inside U are exactly the 91 within-part clique edges plus \(21-\delta\) T-R cross edges.

## 3. Omission-resource inequality

Since \(q_s=0\), (1) gives

\[
\epsilon_s+z_s\ge\max(0,3r_s-4).
\]

Summing over R yields

\[
\boxed{\sum_{s\in R}\max(0,3r_s-4)\le\epsilon_U+\delta.} \tag{2}
\]

Together with \(\sum_R r_s=7\) and \(r_s\le3\), this gives the following finite list.

For \((\delta,\epsilon_U)=(3,3)\), (2) initially leaves

\[
(3,1^4,0^3),\ (2,2,2,1,0^4),\ (2,2,1^3,0^3),\ (2,1^5,0^2),\ (1^7,0).
\]

For \((4,1)\), it initially leaves the same list except \((2,2,2,1,0^4)\).

## 4. Part-complete W classes and the clique cap

For i=1,2,3 define

\[
C_i=\{w\in W:T_i\subseteq N_H(w,U)\},\qquad C=C_1\cup C_2\cup C_3,
\]

and put \(N=W\setminus C\).

### Lemma 4.1 — each C_i is a clique of size at most four

A W-vertex cannot be complete to two different T-parts: that would give \(d_H(w,U)\ge14\), hence \(y_w\ge7\). Since total Y is seven, this would concentrate all positive slack on one vertex, which is excluded for both minimum profiles by the previously proved minimum-slack concentration theorem.

If \(x,x'\in C_i\) were nonadjacent, then

\[
|N_H(x,U)\cap N_H(x',U)|\ge7.
\]

The W-side common-neighbour theorem would force \(y_x+y_{x'}\ge7\). But v already has \(y_v=1\) and v is not in any C_i, leaving only six slack units outside v. Contradiction. Thus every C_i is a clique.

Since \(T_i\) is a K7 complete to C_i and \(\omega(H)\le11\),

\[
\boxed{|C_i|\le4},\qquad \boxed{|C|\le12}. \tag{3}
\]

Every zero-slack vertex belongs to one of the three C_i, because the three T_i already exhaust the at-most-three zero-slack neighbourhood classes in the region \(\epsilon_U+2\delta=9<16\). Hence \(|C|\ge|W_0|\ge11\), so

\[
|C|\in\{11,12\},\qquad |N|\in\{7,6\}.
\]

### Lemma 4.2 — zero-omission R-points dominate N

If \(s\in R\) has \(r_s=0\), then s is target-anticomplete to every T_i. If some \(w\in N\) were nonadjacent to s, w is not complete to any T_i; choose one non-neighbour of w in each T_i. These three T-points are pairwise nonadjacent and are all nonadjacent to s, so together with w they form an independent five-set. Therefore every r=0 point is adjacent to every vertex of N.

Let

\[
q=|\{s\in R:r_s=0\}|.
\]

An r=0 point has no missing T-partner pairs, so \(z_s=0\), and because R is a clique,

\[
d_H(s,W)=5+\epsilon_s.
\]

Hence

\[
q|N|\le5q+\epsilon_U. \tag{4}
\]

Together with \(|N|\ge6\), this yields

\[
q\le3\quad\text{for }(\delta,\epsilon_U)=(3,3),
\]

and

\[
q\le1\quad\text{for }(\delta,\epsilon_U)=(4,1). \tag{5}
\]

## 5. Final minimum-slack classification

### Theorem 5.1 — profile (4,1)

In the slack-one branch with \((\delta,\epsilon_U)=(4,1)\), the only possible omission pattern is

\[
\boxed{(1^7,0)}.
\]

Moreover q=1 and (4) forces \(|N|=6\), hence

\[
\boxed{|C_1|=|C_2|=|C_3|=4}.
\]

The unique zero-omission point \(s_0\in R\) must have \(\epsilon_{s_0}=1\), and

\[
\boxed{N_H(s_0,W)=N}.
\]

Thus this branch has three exact target K11s

\[
T_i\cup C_i\cong K_{11},\qquad i=1,2,3,
\]

plus a unique R-point whose six W-neighbours are exactly the six vertices not complete to any T_i.

**Proof.** The finite list from Section 3 contains q=3,2,1 patterns. Equation (5) leaves only q=1, namely \((1^7,0)\). Since \(|N|\ge6\), (4) gives \(|N|=6\) and the single r=0 point must spend the unique U-excess unit to have W-degree six. Equation (3) and \(|C|=12\) force all three C_i to have size four. \(\square\)

### Theorem 5.2 — profile (3,3)

In the slack-one branch with \((\delta,\epsilon_U)=(3,3)\), only the following two omission families survive:

\[
\boxed{(2,1^5,0^2)}\qquad\text{or}\qquad\boxed{(1^7,0)}.
\]

For \((2,1^5,0^2)\), equation (4) forces \(|N|=6\), so all three C_i have size four. Each of the two r=0 points has \(\epsilon_s\ge1\), hence together they consume at least two of the three U-excess units.

For \((1^7,0)\), either

\[
(|C_1|,|C_2|,|C_3|)=(4,4,4),\quad |N|=6,
\]

or, up to permutation,

\[
(|C_1|,|C_2|,|C_3|)=(4,4,3),\quad |N|=7.
\]

In the second case the unique r=0 point must satisfy \(\epsilon_s\ge2\).

**Proof.** Equation (5) eliminates the q=4 pattern \((2,2,2,1,0^4)\). If q=3, (4) forces \(|N|=6\) and equality forces all three U-excess units onto the three r=0 points. Then the two possible q=3 omission patterns require, by (2), respectively at least five or four units of \(z_s\) on positive-omission points, exceeding \(\delta=3\). Hence q=3 is impossible. The remaining q=2 and q=1 cases are exactly those displayed. \(\square\)

## 6. Scope

This theorem is conditional on the existence of an independent W-four-set of total slack one. It does **not** prove that such a four-set must exist.

What it does prove is that the slack-one branch of the two minimum scalar profiles is no longer a generic low-delta problem:

- the support complement is exactly four-partite with parts \((7,7,7,8)\);
- R is a target K8;
- the W vertices complete to each T-part form cliques of size at most four;
- profile (4,1) has one unique omission pattern and a unique zero-omission R-point dominating the six-vertex residual set N;
- profile (3,3) has only two omission families.

The complementary branch, in which every independent W-four-set has total slack at least two, remains OPEN. The five shell templates and the original K145-to-T61 bridge also remain OPEN / NOT_CERTIFIED.
