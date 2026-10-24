# E407 Q32: stronger transversal/excess bound on the 49-witness boundary

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the E407 Q32 v=29 / 49-block exact-129 contract. No four-partite assumption is used.

## 1. Frozen boundary contract

Let H be the 47-vertex target-color core with
```
alpha(H) <= 4, minimum degree >= 12, e(H)=284.
```
Let U be the 29-point union of 49 selected independent 4-sets Q, seven from each of seven exact-129 colors. Within each color the seven Qs are disjoint; across colors any two Qs intersect in at most one vertex. Put W=V(H)\U, so |W|=18.

Let L=bar(H[U]). The 49 blocks contribute 294 pairwise-distinct edges to L. Let J be the set of L-edges not covered by any selected Q and put
```
delta = |E(J)|,
epsilon_U = sum_{x in U}(d_H(x)-12), 0 <= epsilon_U <= 4.
```
The exact core ledger is
```
e(H[U]) = 112-delta,
e_H(U,W) = 124+epsilon_U+2delta,
e(H[W]) = 48-epsilon_U-delta.
```

Every w in W must hit every Q, or w plus Q would be an independent 5-set. Each core vertex occurs in at most seven selected Qs, so every w has at least seven neighbors in U. Write N7 for the number of W vertices with exactly seven neighbors in U.

## 2. Distinct 7-transversals are disjoint

A 7-transversal is a seven-point set T⊂U meeting every selected Q. If |N_H(w)∩U|=7, that neighborhood is a 7-transversal.

**Lemma 2.1.** Two distinct 7-transversals cannot overlap.

**Proof.** Let T,T' be distinct 7-transversals with |T∩T'|=s∈{1,…,6}. Each color class has seven disjoint Q-blocks, and each transversal meets each block exactly once. Thus, in each color, the 7−s blocks whose T-point lies in T\T' pair those 7−s points with distinct points of T'\T. No ordered pair can repeat across colors, since a repeated pair would make two Q-blocks share two vertices. Therefore
```
7(7-s) <= (7-s)^2,
```
which is impossible for s>=1. Hence distinct transversals are disjoint. ∎

**Lemma 2.2.** At most two distinct 7-transversals can occur as W-neighborhoods.

**Proof.** Suppose three distinct transversals T1,T2,T3 occur. By Lemma 2.1 they are disjoint, so R=U\(T1∪T2∪T3) has eight vertices. Every Q contains exactly one point from each T_i and one point from R.

For r∈R, let q_r be the number of the seven colors whose Q-class omits r. Each color covers 28 of the 29 points of U, so
```
sum_{r in R} q_r = 7.
```
In the 7−q_r colors that contain r, its partner in each T_i is distinct across colors by linearity. Thus r has at most q_r neighbors in each T_i. Since d_H(r,R)≤7,
```
d_H(r) <= 7 + 3q_r.
```
The minimum-degree condition d_H(r)≥12 implies q_r≥2 for every r∈R, so the sum is at least 16, contradiction. ∎

Consequently, if k≤2 is the number of distinct 7-transversal neighborhoods and m_i is the multiplicity of the i-th one, then (N_7=\sum_i m_i).

## 3. Charge each 7-transversal to core excess

Fix a 7-transversal T_i with multiplicity m_i. For x∈T_i, the seven Q-blocks containing x have three vertices outside T_i each. These 21 vertices are distinct by linearity. Since |U\T_i|=22, exactly one point of U\T_i is not paired with x in any selected Q.

Let j_i(x) be the number of J-edges inside T_i incident to x. Let b_i(x)∈{0,1} indicate whether the unique uncovered pair from x to U\T_i is an edge of J. Every pair inside T_i is not a Q-pair, because T_i meets every Q only once. Hence
[
d_H(x,U)=6-j_i(x)+1-b_i(x)=7-j_i(x)-b_i(x).
]
Each of the m_i W vertices with neighborhood T_i is adjacent to every x∈T_i, so d_H(x,W)≥m_i. Writing d_H(x)=12+epsilon_x gives
[
epsilon_x\ge m_i-5-j_i(x)-b_i(x).
]
Summing over x∈T_i,
[
sum_{x\in T_i}\epsilon_x
\ge 7m_i-35-2e(J[T_i])-e_J(T_i,U\setminus T_i).
	ag{3.1}
]

The distinct T_i are disjoint. Summing (3.1) over k≤2 transversals, and observing that each J-edge contributes at most two to the subtracted incidence total, gives
[
oxed{\epsilon_U\ge 7N_7-70-2\delta.}
]
Equivalently,
[
oxed{N_7\le 10+\frac{\epsilon_U+2\delta}{7}.}
	ag{3.2}
]

## 4. Combine with the exact cross-edge budget

Every W vertex counted by N7 contributes seven edges to U; each other W vertex contributes at least eight. Therefore
[
e_H(U,W)\ge 7N_7+8(18-N_7)=144-N_7.
]
Using the exact ledger (e_H(U,W)=124+\epsilon_U+2\delta), we get
[
oxed{N_7\ge20-(\epsilon_U+2\delta).}
	ag{4.1}
]

Put (S=\epsilon_U+2\delta). If S≥20, then S≥9 already. Otherwise, combining (3.2) and (4.1) yields
[
20-S\le10+S/7
\quad\Longrightarrow\quad
S\ge70/8=8.75.
]
Since S is an integer,
[
oxed{\epsilon_U+2\delta\ge9.}
]
As (epsilon_U\le4), this forces
[
oxed{\delta\ge3.}
]

## 5. Scope

This strengthens the earlier E407 v=29 / 49-witness bound (delta\ge2) to (delta\ge3), without assuming L is four-partite. The surviving exact ledger is
[
0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad
\epsilon_U+2\delta\ge9,\quad
\delta\ge3.
]
It does not eliminate (delta=3,\ldots,16), close the E407 Q32 common-core completion, or prove the original K145 theorem. E408 Q32 remains a separate 285-edge-core case.
