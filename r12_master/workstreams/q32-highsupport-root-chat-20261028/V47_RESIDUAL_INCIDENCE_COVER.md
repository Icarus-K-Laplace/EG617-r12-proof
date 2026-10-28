# E408 Q32 full-support — independent-set incidence constraints across pivot blocks

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural lemmas; no v=47 closure claimed.**

## 1. Setup

Use the v=47 pivot-block notation:
- (Q_1,\ldots,Q_m\) are pairwise disjoint independent 4-sets in H;
- (R=H\setminus\bigcup_i Q_i), with (|R|=47-4m\);
- (a_{ri}=|N_H(r)\cap Q_i|\ge1) for every (r\in R) and block (i);
- (y=\sum_{r\in R,i}(a_{ri}-1)\), so (e_H(Q,R)=m|R|+y).

The lower bound (a_{ri}\ge1) is forced because (Q_i\cup\{r\}) would otherwise be an independent 5-set.

## 2. Lemma — independent-set neighborhood covering

For every independent set (S\subseteq R) with (|S|=k\le4), and every block (Q_i),
[
\left|\bigcup_{r\in S}(N_H(r)\cap Q_i)\right|\ge k.
]

**Proof.** If the union had size at most (k-1), then at least (4-(k-1)=5-k) vertices of (Q_i) would be nonadjacent to every point of S. Since (Q_i) is independent, those (5-k) vertices together with S would form an independent 5-set, contradicting (alpha(H)\le4). QED.

Special cases:
- independent pair (r,s\in R): their neighborhoods in each Q_i have union size at least2;
- independent triple: the union size is at least3;
- independent 4-set: the four Q_i vertices are all covered.

## 3. Consequence when a block has no cross-edge slack

If (a_{ri}=1) for every (r\in R) (equivalently, block i contributes zero to y), each r has a unique neighbor (f_i(r)\in Q_i).

The independent-pair case of the lemma shows:
[
r,s\text{ nonadjacent in }H[R]\implies f_i(r)\ne f_i(s).
]
Thus every fiber (f_i^{-1}(q)) is a clique in H[R]. In other words, the unique-neighbor map partitions R into at most four cliques.

This is a strict structural restriction on the zero-slack case, not merely the degree-sum inequality (y+2z\ge D_m).

More generally, if (a_{ri}=a_{si}=1) and (r,s) are nonadjacent, they cannot share their unique neighbor in Q_i. Hence for positive y, every collision among singleton incidences must be paid for by at least one extra incidence (a_{ti}-1\ge1) from the same independent-pair constraints.

## 4. m=10 numerical frontier and independent-triple split

For m=10, (|R|=7), (p_4(7)=3), and the registered degree ledger gives
[
x+y+z=32,\
2x+y\ge50,\
8\le y+2z\le14.
]
Therefore (0\le z\le7), (x\ge18+z), and:
- if (z\le5), then (e(H[R])=3+z\le8). By Mantel, a graph on seven vertices with independence number at most2 has at least9 edges, so (H[R]) must contain an independent triple. The triple-covering lemma applies in every block;
- if (z\in\{6,7\}), then (e(H[R])\in\{9,10\}). The independent-triple guarantee no longer follows from edge count alone, so this is a separate high-(z) cell; the independent-pair lemma still applies.

The low-z cell therefore has a genuine triple-incidence constraint in addition to the pivot packing and degree ledger. It has not yet been converted into a full graph-level contradiction.

## 5. Firewall

The lemma uses only the 47-core contract, the independent pivot blocks, and (alpha(H)\le4). It does not invoke any retracted Kang–Pikhurko degree-nine claim or any Q33 284-edge identity. Full-support v=47 remains OPEN / NOT_CERTIFIED.

## 6. m=10 high-chromatic residual cell

Let (J_R=\overline{H[R]}). Since (omega(J_R)=alpha(H[R])\le4), if (chi(J_R)\ge5), then (chi(J_R)=5) and (J_R) is 5-critical on all seven vertices.

Justification: a 5-chromatic K5-free graph on at most six vertices cannot exist. A 5-critical graph on seven vertices has minimum degree at least4. Therefore (Delta(H[R])\le2). Since (chi(J_R)) equals the clique-cover number of (H[R]), enumerate the path/cycle components of a seven-vertex graph of maximum degree2 subject also to (alpha(H[R])<=4). The only graph with clique-cover number at least5 is (C_5 dot-union 2K_1); the other degree-2-component possibility with clique-cover number5, (C_3 dot-union 4K_1), is excluded because its independence number is5. Hence

`H[R] = C_5 \dot\cup 2K_1,quad e(H[R])=5,quad z=2.`

Now every block must have positive cross-edge slack: if (y_i=0), its unique-neighbor map partitions R into at most four cliques, equivalently 4-colors (J_R), contradiction. Thus (y\ge m=10). The degree ledger gives (y+2z\le14), so (y\le10). Therefore (y=10), and the exact edge identity gives (x=20).

Since (2x+y=50), all 40 Q-vertices have degree exactly12. Since (y+2z-8=6), all six units of core excess lie in R. Each block has exactly one extra Q-R incidence. The two isolated R vertices each need at least two extra incidences across the ten blocks; the remaining incidence excess is exactly six.

This is a rigid necessary cell, not a contradiction. The next check must couple the five independent 4-sets of (C_5 dot-union 2K_1) across the ten blocks. For each independent 4-set S in R, every vertex of every Q_i must have at least one neighbor in S; hence the four neighborhoods cover all four vertices of Q_i. In this y_i=1 cell, if the extra-incidence vertex is outside S, the four singleton neighborhoods are a bijection onto Q_i; if it is in S, the five incidences have exactly one overlap while still covering all four vertices. For an independent triple S, each Q_i has at most one vertex nonadjacent to all of S; whenever such vertices exist in two blocks, they must be adjacent.