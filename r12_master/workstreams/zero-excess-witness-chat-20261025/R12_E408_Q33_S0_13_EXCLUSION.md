# E408 Q33 minimum-support boundary: exclude \(S_0=13\)

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the registered E408 Q33 core, exact-129, and minimum-support contracts.  
Conclusion: combined with the audited \(S_0\ge12\) theorem, this proves
\[
\boxed{S_0=\epsilon_U+2\delta\ge14}
\]
for the 31-point / 56-witness boundary, without assuming that \(L\) is four-partite. It does not close larger-support or other E407/E408 terminals.

## 1. Frozen contract and the unique seven-point transversal

Let \(H\) be the 47-vertex core satisfying
\[
e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad
d_H(x)=12+\epsilon_x,\quad \epsilon_x\ge0,\quad \sum_H\epsilon_x=4.
\]
Let \(U\) be the 31-point union of 56 selected independent four-sets \(\mathcal Q\), seven from each of eight exact-129 colors. Within a color the seven sets are disjoint; across all colors distinct sets intersect in at most one vertex. Put \(W=H\setminus U\), \(|W|=16\), and \(L=\overline{H[U]}\).

The 56 witness \(K_4\)'s are edge-disjoint, so write
\[
e(L)=336+\delta,\qquad \epsilon_U=\sum_{u\in U}\epsilon_u,\qquad
S_0=\epsilon_U+2\delta.
\]
The exact degree ledger gives
\[
e_H(U,W)=114+S_0.
\]

Assume \(S_0=13\). Then \(\sum_{w\in W}q_w=127\), where \(q_w=|N_H(w)\cap U|\). Every \(w\) must hit every \(Q\in\mathcal Q\), or \(Q\cup\{w\}\) would be an independent five-set. The retained linear-family transversal theorem gives \(q_w\ge7\). Since \(127<128\), at least one \(w\) has \(q_w=7\), so a seven-point transversal \(T\subset U\) exists.

### Lemma 1.1 — \(T\) is unique, a clique, and anticomplete to \(R=U\setminus T\)

Each exact-129 color has seven disjoint witnesses, so a seven-point transversal meets each witness exactly once. For each \(t\in T\), the eight witness sets containing \(t\) (one from each color) have disjoint three-point remainders and partition \(R\), since \(|R|=24\). Thus every pair \(t r\), \(r\in R\), lies in an independent witness and is a nonedge of \(H\): \(T\) is anticomplete to \(R\).

The set \(T\) is a clique. Otherwise two nonadjacent points of \(T\), together with any independent witness triple in \(R\), form an independent five-set.

There cannot be a second distinct seven-point transversal \(T'\). If \(s=|T\cap T'|\), each of the eight colors produces \(8(7-s)\) distinct pairs between \(T\setminus T'\) and \(T'\setminus T\); pairwise linearity allows at most \((7-s)^2\) such pairs. For distinct transversals this would require \(8\le7-s\), impossible. Therefore \(T\) is unique.

Let \(k=|\{w\in W:q_w=7\}|\). Every such \(w\) has \(N_H(w)\cap U=T\). These \(k\) vertices form a clique: otherwise two nonadjacent ones plus an independent witness triple in \(R\) give an independent five-set. Since \(T\) is a clique and is complete to those vertices, \(T\) together with them is a clique of size \(7+k\). The core contract \(\omega(H)\le11\) gives
\[
1\le k\le4. \tag{1}
\]

For each \(t\in T\), its eight witness triples partition \(R\) into eight triples. A \(q=8\) neighborhood is either \(T\cup\{r\}\) for one \(r\in R\), or an eight-point set contained in \(R\) meeting every one of these partitions (an **R-only transversal**). More generally, if \(q_w>8\) and \(b_w=|N_H(w)\cap T|<7\), then \(b_w\le q_w-8\) and \(N_H(w)\cap R\) is a transversal of the \(7-b_w\) partitions indexed by \(T\setminus N_H(w)\).

## 2. R-only transversal geometry

### Lemma 2.1 — distinct R-only eight-transversals are disjoint; two force a third transversal

Let \(S,S'\subset R\) be distinct eight-point transversals and \(s=|S\cap S'|\). Pair-counting across the seven partitions first gives
\[
7(8-s)\le(8-s)^2,
\]
so \(s\le1\). If \(s=1\), let \(p\) be the common point. In each of the seven partitions indexed by \(t\in T\), the witness triple containing \(p\) must have its other two points outside \(S\cup S'\), because both transversals already meet that triple at \(p\). These seven witness triples are pairwise disjoint outside \(p\), by linearity, and so require 14 distinct points outside \(S\cup S'\). But \(R\setminus(S\cup S')\) has only \(24-15=9\) points. Contradiction. Therefore distinct R-only eight-transversals are disjoint.

If \(S,S'\) are disjoint, \(R_0=R\setminus(S\cup S')\) has size eight. Every witness triple in every T-partition contains one point of \(S\) and one point of \(S'\), so its third point lies in \(R_0\). Thus \(R_0\) is itself a third R-only eight-transversal. This is a mathematical transversal; it need not be realized as a W-neighborhood.

### Lemma 2.2 — at most three distinct R-only transversals, and any three partition R

Distinct R-only eight-transversals are disjoint by Lemma 2.1. Four such sets would contain 32 points of \(R\), impossible because \(|R|=24\). Hence there are at most three distinct sets. If there are three, they are disjoint eight-sets and therefore partition \(R\).

### Lemma 2.3 — multiplicity cap and clique consequences

For \(r\in R\), let \(j_r\) be the degree of \(r\) in the \(\delta\) leftover edges of \(L\) not covered by witness \(K_4\)'s, and put \(g_r=\epsilon_r+j_r\). Each \(r\) lies in one witness with each \(t\in T\), giving 21 distinct incident witness edges in \(L\). Hence
\[
d_H(r,U)=9-j_r,\qquad d_H(r,W)=3+g_r.
\]
Let \(s_r\) be the number of R-only eight-neighborhoods containing \(r\), and \(a_r\) the number of special incidences at \(r\) from the \(T\cup\{r\}\) neighborhoods and from vertices with \(q>8\). Then
\[
s_r=3+g_r-a_r,\qquad
\sum_{r\in R}g_r=S_0-\epsilon_T=13-\epsilon_T.
\]
For an R-only set \(S\) occurring \(m_S\) times,
\[
8m_S\le\sum_{r\in S}s_r
\le24+\sum_{r\in R}g_r
=37-\epsilon_T\le37.
\]
Thus every distinct R-only eight-set has multiplicity at most four. Also, if \(r\) is uncovered by all R-only neighborhoods, then \(s_r=0\) forces \(a_r=3+g_r\ge3\).

Whenever \(S_1,S_2,S_3\) are three R-only eight-transversals partitioning \(R\), let \(G_i\subseteq W\) be the set of vertices whose U-neighborhood is exactly \(S_i\), and let \(m_i=|G_i|\). The sets \(G_i\) may be empty: this matters when two realized neighborhoods force a third mathematical transversal that is not itself realized in W.

For each \(u\in S_i\) and each other part \(S_j\), the seven witness blocks indexed by \(t\in T\) and containing \(u\) supply seven distinct nonneighbors of \(u\) in \(S_j\). Thus every vertex of \(S_i\) has at most one H-neighbor in each other part. This cross-part degree bound and \(\alpha(H)\le4\) imply that each \(S_i\) is a clique: if \(u,v\in S_i\) were nonadjacent, choose \(a\in S_j\) nonadjacent to both, then \(b\in S_k\) nonadjacent to \(u,v,a\), and finally any \(t\in T\); the five vertices would be independent.

Each \(G_i\) is also a clique. If \(w,w'\in G_i\) were nonadjacent, choose a nonadjacent pair \(a\in S_j,b\in S_k\) using the cross-part degree bound, and any \(t\in T\). Because \(N_H(w)\cap U=N_H(w')\cap U=S_i\) and \(T\) is anticomplete to \(R\), these five vertices would be independent. By definition \(G_i\) is complete to \(S_i\). Consequently
\[
m_i\ge4\quad\Longrightarrow\quad S_i\cup G_i\cong K_{8+m_i}\supseteq K_{12}, \tag{2}
\]
contrary to \(\omega(H)\le11\).

### Lemma 2.4 — high neighborhoods contain a part, or force an impossible W-degree

Let \(y\in W\) have \(q_y\in\{9,10,11\}\), put \(b_y=|N_H(y)\cap T|<7\), and \(Y=N_H(y)\cap R\), so \(|Y|=q_y-b_y\). For every \(t\in T\setminus N_H(y)\), the set \(Y\) must hit every witness triple in the partition indexed by \(t\); otherwise that independent Q-block together with \(y\) is an independent five-set.

If \(S_i\) is an R-only eight-transversal not contained in \(Y\), put \(s=|S_i\cap Y|<8\). In each of the \(d=7-b_y\) partitions hit by \(Y\), every point \(x\in S_i\setminus Y\) lies in a triple whose other two points are outside \(S_i\), and at least one of them belongs to \(Y\). Choose one such point \(z\in Y\setminus S_i\) and record the pair \((x,z)\). Within each partition these are \(8-s\) distinct pairs; the same pair cannot recur in another partition by linearity. Hence
\[
d(8-s)\le(8-s)(|Y|-s),
\]
and therefore
\[
|Y\cap S_i|=s\le |Y|-d=(q_y-b_y)-(7-b_y)=q_y-7. \tag{3}
\]

For \(q_y=9\), the bound (3) is two. If no part \(S_i\) were contained in \(Y\), the three parts would cover at most six points of \(Y\), whereas \(|Y|=9-b_y\ge8\). Thus \(Y\) contains a part.

For \(q_y=10,b_y=0\), (3) bounds each intersection by three; if no part were contained, the three parts would cover at most nine points, less than \(|Y|=10\). Thus \(Y\) contains a part.

For \(q_y=10,b_y\in\{1,2\}\), or \(q_y=11,b_y\le3\), suppose no part is contained. Then (3) leaves at least five points of each part outside \(Y\) in the q=10 case, and at least four in the q=11 case. If \(y\) missed any vertex \(w\in G_i\), choose a nonadjacent pair from the other two parts outside \(Y\), using the cross-part degree bound, and choose \(t\in T\setminus N_H(y)\). The set \(\{y,w,a,b,t\}\) would be an independent five-set. Therefore \(y\) would have to be adjacent to every vertex in \(G_1\cup G_2\cup G_3\), forcing \(d_H(y,W)\ge m\). For q=10, \(d_H(y,W)=2+\epsilon_y\le6<m\) in the profiles where this case occurs; for q=11, \(d_H(y,W)=1+\epsilon_y\le5<m\). Contradiction. So \(Y\) contains a part in every feasible high-degree case.

If \(Y\) contains \(S_i\), then \(y\) is adjacent to every vertex of \(G_i\). Otherwise, since \(|Y\setminus S_i|=q_y-b_y-8\le3\), each of the other two parts has at least five vertices outside \(Y\). Choose a nonadjacent pair from those parts and a point \(t\in T\setminus N_H(y)\); together with \(y\) and the missed \(G_i\)-vertex they form an independent five-set.

If two high vertices \(y,z\) with \(b_y,b_z<7\) both contain the same \(S_i\), then they are adjacent. Each has at most three R-neighbors outside \(S_i\), so each of the other two parts has at least two vertices outside both neighborhoods. Choose a nonadjacent pair from those two sets. Also choose \(t\in T\setminus(N_H(y)\cup N_H(z))\), which exists because the allowed low-b values satisfy \(b_y+b_z\le6\). If \(y,z\) were nonadjacent these five vertices would be independent. Hence they are adjacent. Together with (2), two such vertices sharing a part of multiplicity two form a \(K_{12}\) with that part and its \(G_i\).

## 3. Exhaustive degree profiles when \(S_0=13\)

Put \(a=\#\{w:q_w=8,\ T\subseteq N_H(w)\}\), the number of \(T\)-type eight-neighborhoods, and let \(m\) be the number of R-only eight-neighborhoods, with multiplicity. For each high vertex \(y\) with \(q_y>8\), put \(b_y=|N_H(y)\cap T|\), and \(B=\sum_{q_y>8}b_y\). The T-to-W incidence sum is
\[
42+\epsilon_T=7k+7a+B,\qquad
\epsilon_T=7(k+a-6)+B.
\]
Since \(S_0=13\), \(\epsilon_U\in\{1,3\}\), so \(0\le\epsilon_T\le3\). Also \(k+a\le6\), because at least three vertices of \(T\) have zero excess and each has exactly six W-neighbors. The cross-edge sum 127 implies that the high-degree profiles are precisely those listed below.

| \(m\) | All feasible profile families \((k;\ q>8\text{ degrees and }b\text{-values};\ a)\) | Special-incidence total \(A=\sum_R a_r\) | High vertices with \(b<7\) |
|---:|---|---:|---:|
| 10 | \((1;\ \varnothing;\ 5)\); \((2;\ 9[7];\ 3)\); \((3;\ 9[7],9[7];\ 1)\); \((3;\ 10[7];\ 2)\); \((4;\ 9[7],10[7];\ 0)\); \((4;\ 11[7];\ 1)\) | 5 in every case | 0 |
| 9 | \((2;\ 9[0/1];\ 4)\); \((3;\ 9[7],9[0/1];\ 2)\); \((3;\ 10[0/1/2];\ 3)\); \((4;\ 9,9,9\text{ with two }b=7;\ 0)\); \((4;\ 9,10\text{ with one }b=7;\ 1)\); \((4;\ 11[0/1/2/3];\ 2)\) | 10–13 | At least 1 |
| 8 | \((3;\ 9[0/1],9[0/1];\ 3)\); \((4;\ 9,9,9\text{ with one }b=7;\ 1)\); \((4;\ 9[0/1],10[0/1/2];\ 2)\) | 18–21 | At least 2 |
| 7 | \((4;\ 9[0/1],9[0/1],9[0/1];\ 2)\) | 26–29 | 3 |

Here \(q[b]\) means a high vertex with U-degree \(q\) and \(b\) neighbors in \(T\); unspecified \(b\)-values in the table are those required by \(0\le\epsilon_T\le3\). The table is exhaustive from \(\epsilon_T=7(k+a-6)+B\), \(k+a\le6\), and the allowed values \(b=0,\ldots,q-8\) or \(b=7\). The accompanying arithmetic verifier enumerates all 60 labelled parameter cases and confirms the table's four \(m\)-classes.

## 4. Eliminate every profile

### Case \(m=10\)

There are at least three distinct R-only sets, since each has multiplicity at most four and two sets account for at most eight copies. There are at most three distinct sets, so Lemma 2.2 gives a partition \(S_1,S_2,S_3\). Their multiplicities sum to ten; at least one is at least four, contradicting (2).

### Case \(m=9\)

Again there must be exactly three distinct sets partitioning \(R\). If any multiplicity is at least four, (2) is contradicted. Otherwise all three multiplicities are three. The table guarantees a high vertex with \(b<7\); Lemma 2.4 forces its neighborhood to contain one part, and the same lemma makes it complete to the corresponding \(G_i\). That part and \(G_i\) already form a \(K_{11}\), so adding the high vertex gives a \(K_{12}\).

### Cases \(m=8\) and \(m=7\): force three realized neighborhoods

There are at most three distinct R-only eight-neighborhoods by Lemma 2.2. There cannot be only one, because its multiplicity would be \(m\in\{7,8\}\), contradicting the multiplicity cap \(m_i\le4\).

Suppose there were exactly two distinct realized neighborhoods \(S_1,S_2\). They are disjoint by Lemma 2.1, and their complement \(S_3=R\setminus(S_1\cup S_2)\) is a third mathematical R-only transversal. Thus \(S_1,S_2,S_3\) partition \(R\), and the clique consequences in Lemma 2.3 apply even if \(G_3=\varnothing\). Since the two multiplicities sum to \(m\) and each is at most four, for \(m=8\) they must be \((4,4)\), while for \(m=7\) they must be \((4,3)\). In either case a multiplicity-four group gives a \(K_{12}\) by (2), contradiction.

Therefore both \(m=8\) and \(m=7\) have exactly three distinct realized R-only neighborhoods, which partition \(R\) by Lemma 2.2.

### Case \(m=8\)

The three multiplicities sum to eight. Any multiplicity four gives a \(K_{12}\); otherwise they are \(3,3,2\). The two high vertices with \(b<7\) must each contain a part. To avoid an immediate \(K_{12}\), both must contain the unique part of multiplicity two. Lemma 2.4 makes both complete to its \(G_i\), and the pairwise-adjacency conclusion of that lemma forces them adjacent. The part, its two-vertex group, and these two high vertices form a \(K_{12}\), contradiction.

### Case \(m=7\)

The three multiplicities sum to seven. A multiplicity four gives a \(K_{12}\). Otherwise the only patterns are \(3,3,1\) and \(3,2,2\). There are three high vertices with \(b<7\), each forced to contain one of the parts.

- For \(3,3,1\), any high vertex containing a multiplicity-three part gives a \(K_{12}\). Thus, to avoid contradiction, all three high vertices would have to contain the singleton part. They are pairwise adjacent by Lemma 2.4, and each is complete to that part and its one-vertex group; together these make a \(K_{12}\).
- For \(3,2,2\), any high vertex containing the multiplicity-three part gives a \(K_{12}\). Hence all three must choose one of the two multiplicity-two parts. By pigeonhole, two choose the same part; Lemma 2.4 forces them adjacent, giving a \(K_{12}\) with that part and its group.

Both subcases contradict \(\omega(H)\le11\).

Every profile under \(S_0=13\) is impossible. Combining with the already-audited universal \(S_0\ge12\) theorem yields
\[
\boxed{S_0=\epsilon_U+2\delta\ge14.}
\]
Since \(\epsilon_U\le4\), this also gives \(\delta\ge5\) in the minimum-support Q33 boundary. No upper bound on \(\delta+\epsilon_U\) follows from this exclusion alone.

## 5. Scope firewall

This is a conditional exclusion of the \(S_0=13\) minimum-support E408 Q33 boundary. It uses the registered \(\omega(H)\le11\) core contract, the eight-color/56-witness exact-129 factor, pairwise linearity, and the previously proved \(S_0\ge12\) result. It does not exclude \(S_0\ge14\), larger witness-support sizes, E407 Q32, E408 Q32's separate 285-edge/excess-six core, or the original \(K_{145}\)-to-T61 bridge. EG617(\(r=12\)) remains **OPEN / NOT_CERTIFIED**.
