# E407 Q32 — minimum-slack W-kernel reduction

Date: 2026-10-27  
Status: **PROVED necessary-structure theorem inside the slack-one exact-core branch. E407 Q32 remains OPEN.**

## 1. Contract

Assume the full hypotheses and conclusions of `MINIMUM_SLACK_EXACT_CORE.md`.

Thus

\[
\epsilon_U+2\delta=9,
\]

there is an independent four-set in W of total y-slack one, and

\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad |T_i|=7,\quad |R|=8,
\]

where:

- each \(T_i\) is a target K7;
- the three T-parts are pairwise target-anticomplete;
- \(R\) is a target K8;
- every support block contains exactly one point from each part;
- for \(w\in W\), \(y_w=d_H(w,U)-7\ge0\), and \(\sum_Wy_w=7\);
- for \(C_i=\{w:T_i\subseteq N_H(w,U)\}\), each \(C_i\) is a clique of size at most four;
- \(C=C_1\cup C_2\cup C_3\) has size 11 or 12;
- \(N=W\setminus C\) has size 7 or 6;
- all zero-slack vertices lie in C.

Let \(q\) be the number of points of R having omission multiplicity zero. Every such point is adjacent to every vertex of N.

The surviving omission patterns are:

- profile \((\delta,\epsilon_U)=(4,1)\): \((1^7,0)\), hence q=1, \(|C_i|=4\), \(|N|=6\);
- profile \((3,3)\): either \((1^7,0)\), q=1, or \((2,1^5,0^2)\), q=2.

## 2. The seven slack units have only two multiplicity types

Since all zero-slack vertices lie in C and \(|C|\le12\),

\[
|N|\le |\{w:y_w>0\}|\le7.
\]

But \(|N|\ge6\). Therefore the number p of positive-slack vertices is either six or seven.

Because \(\sum_Wy_w=7\), the positive y-multiset is exactly

\[
\boxed{(2,1,1,1,1,1)}
\]

when p=6, and

\[
\boxed{(1,1,1,1,1,1,1)}
\]

when p=7. In particular,

\[
\boxed{y_w\le2\quad\text{for every }w\in W.} \tag{2.1}
\]

If \(|N|=7\), then all seven vertices of N have y=1 and every C-vertex has y=0.

If \(|N|=6\), then either:

1. N contains one y=2 vertex and five y=1 vertices and every C-vertex has y=0; or
2. all six vertices of N have y=1 and exactly one C-vertex has y=1.

## 3. Cylinder forcing from an R-nonedge

### Lemma 3.1

Let \(w\in N\) and \(s\in R\) be target-nonadjacent. Then for some i,

\[
|N_H(w,U)\cap T_i|\ge7-r_s. \tag{3.1}
\]

**Proof.** The point s has target neighbours in at most \(r_s\) vertices of each T-part, because its other \(7-r_s\) partners in that part occur with s in support blocks and are therefore target-nonedges.

If (3.1) failed for all three i, then in every \(T_i\) the union of the target-neighbour sets of w and s would have size at most six. Choose one common target-nonneighbour \(t_i\in T_i\). The three chosen T-points are pairwise target-nonadjacent, and all are nonadjacent to w and s; since ws is also a nonedge,

\[
\{w,s,t_1,t_2,t_3\}
\]

would be an independent five-set in H. Contradiction. \(\square\)

### Lemma 3.2 — every non-R-complete vertex is near exactly one T-part

Let \(w\in N\) and suppose w is not complete to R. Then

\[
\boxed{|N_H(w,U)\cap T_i|=6}
\]

for a unique i.

**Proof.**

In the q=1 omission pattern, the unique r=0 point dominates N, so any R-point missed by w has r=1. Lemma 3.1 gives six neighbours in some T-part.

In the q=2 pattern \((2,1^5,0^2)\), suppose w missed no r=1 point. Since both r=0 points dominate N, the only R-point w could miss is the unique r=2 point; hence w has at least seven R-neighbours. Lemma 3.1 would then give at least five neighbours in some T-part, so

\[
d_H(w,U)\ge12,
\]

contradicting (2.1), which gives \(d_H(w,U)=7+y_w\le9\). Thus w misses an r=1 point here as well, and again Lemma 3.1 gives at least six neighbours in one T-part.

Because \(w\in N\), it is not complete to any T-part, so the number is exactly six. It cannot have six neighbours in two different T-parts: together with even one zero-omission R-neighbour this would give at least 13 U-neighbours, again contradicting \(d_H(w,U)\le9\). \(\square\)

## 4. Four clique classes on N

Define

\[
J=\{w\in N:R\subseteq N_H(w,U)\}
\]

and, for i=1,2,3,

\[
M_i=\{w\in N\setminus J:|N_H(w,U)\cap T_i|=6\}.
\]

By Lemma 3.2,

\[
\boxed{N=J\dot\cup M_1\dot\cup M_2\dot\cup M_3}. \tag{4.1}
\]

### Lemma 4.1 — J is a clique and |J|≤3

Two J-vertices have all eight R-points as common U-neighbours. If they were nonadjacent, the W-side common-neighbour theorem would give

\[
8\le y_w+y_{w'}.
\]

But by (2.1), and because at most one W-vertex can have y=2, the right side is at most three. Hence J is a clique.

Since R is a target K8 complete to J,

\[
R\cup J
\]

is a clique, and \(\omega(H)\le11\) gives

\[
\boxed{|J|\le3}. \tag{4.2}
\]

### Lemma 4.2 — every M_i is a clique

Two vertices of \(M_i\) each see six of the seven points of \(T_i\), so they have at least five common T_i-neighbours. They also share all q≥1 zero-omission R-points, because those dominate N. Hence they have at least six common U-neighbours.

If they were nonadjacent, the common-neighbour theorem would give at most \(y_w+y_{w'}\le3\) common U-neighbours. Contradiction. Thus every \(M_i\) is a clique. \(\square\)

Therefore every slack-one minimum profile has a six- or seven-vertex residual N partitioned into at most four target cliques.

## 5. The q=1 omission family forces exactly two R-complete vertices

Assume the omission pattern is

\[
(1^7,0).
\]

This covers the entire slack-one \((4,1)\) profile and one of the two surviving \((3,3)\) families.

Let \(R_1\subset R\) denote the seven r=1 points and let \(s_0\) be the unique r=0 point.

### Lemma 5.1 — |J|≤2

For \((4,1)\), `MINIMUM_SLACK_EXACT_CORE.md` already gives \(\epsilon_{s_0}=1\), so every point of \(R_1\) has epsilon zero. If \(z_s\) is the number of extra complement edges from s to the T-parts, then

\[
d_H(s,W)=2+z_s,
\qquad \sum_{s\in R_1}z_s=\delta=4.
\]

If \(|J|\ge3\), every one of the seven R1-points is adjacent to all J and has W-degree at least three, forcing \(z_s\ge1\) for all seven s, impossible because their z-sum is four.

For \((3,3)\),

\[
d_H(s,W)=2+\epsilon_s+z_s,
\]

and

\[
\sum_{s\in R_1}(\epsilon_s+z_s)\le\epsilon_U+\delta=6.
\]

Again \(|J|\ge3\) would require at least one extra unit at each of seven R1-points, impossible. Hence in either q=1 profile,

\[
\boxed{|J|\le2}. \tag{5.1}
\]

### Lemma 5.2 — |J|≥2

A C-vertex already uses seven U-neighbours on its complete T-part, so the number of its R1-neighbours is at most its y-slack. Hence

\[
e_H(C,R_1)\le y(C):=\sum_{w\in C}y_w. \tag{5.2}
\]

A vertex of \(M_i\) uses six neighbours in \(T_i\) and the mandatory neighbour \(s_0\), so it has at most y_w neighbours in R1. Every J-vertex is adjacent to all seven R1-points. Thus, if \(|J|\le1\),

\[
e_H(N,R_1)\le13-y(C). \tag{5.3}
\]

Indeed for J empty the upper bound is even smaller; for one J-point, its seven R1-edges plus the remaining y-budget give at most \(7+(7-y(C)-1)=13-y(C)\).

For \((4,1)\), the total R1-to-W degree is exactly

\[
\sum_{s\in R_1}d_H(s,W)=14+\sum z_s=18.
\]

By (5.2), this forces

\[
e_H(N,R_1)\ge18-y(C)>13-y(C),
\]

contradicting (5.3).

For \((3,3)\), the same total is

\[
17+\epsilon(R_1)\ge17,
\]

so

\[
e_H(N,R_1)\ge17-y(C)>13-y(C),
\]

again a contradiction. Therefore

\[
\boxed{|J|\ge2}. \tag{5.4}
\]

Combining (5.1) and (5.4):

\[
\boxed{|J|=2\quad\text{for every q=1 slack-one minimum profile}.} \tag{5.5}
\]

## 6. Exact kernel for profile (4,1)

In the \((\delta,\epsilon_U)=(4,1)\) slack-one branch:

- \(|N|=6\);
- \(|J|=2\);
- exactly four vertices lie in \(M_1\cup M_2\cup M_3\);
- J and every M_i are target cliques;
- each M_i-vertex has exactly six neighbours in its unique T_i;
- the unique r=0 point \(s_0\) is adjacent to all six N-vertices and has no W-neighbour outside N;
- each r=1 point is adjacent to both vertices of J and has
  \[
  d_H(s,W)=2+z_s,
  \]
  so it has exactly z_s further W-neighbours outside J;
- the seven integers z_s are nonnegative and sum to four.

Thus the former low-delta branch is reduced to a six-point W kernel with two distinguished R-complete vertices, four near-T vertices, three clique labels M_i, and only four R1-to-W correction incidences beyond the mandatory J edges.

## 7. Remaining q=2 branch

For the \((3,3)\) omission pattern

\[
(2,1^5,0^2),
\]

we still have

\[
|N|=6,
\qquad
N=J\dot\cup M_1\dot\cup M_2\dot\cup M_3,
\qquad
|J|\le3,
\]

with all four classes cliques. The two r=0 points dominate N and consume at least two of the three U-excess units. The exact value of |J| is not yet forced by the present budget.

## 8. Scope

This theorem does not prove that the slack-one branch occurs, and it does not close any of the five shell templates. It converts the q=1 exact-core branch to an explicit bounded W-kernel and leaves one q=2 six-point kernel plus the complementary branch in which every independent W-four-set has total slack at least two.

No original K145 conclusion is claimed.
