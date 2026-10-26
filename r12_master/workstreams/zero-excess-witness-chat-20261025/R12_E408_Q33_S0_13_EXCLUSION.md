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

### Lemma 2.1 — distinct R-only eight-transversals meet in at most one point

Let \(S,S'\subset R\) be distinct eight-point transversals and \(s=|S\cap S'|\). In each of the seven partitions indexed by \(t\in T\), the \(8-s\) points of \(S\setminus S'\) pair in their triples with \(8-s\) distinct points of \(S'\setminus S\). The resulting ordered pairs cannot repeat across partitions, since a repeated pair would make two witness sets share two points. Hence
\[
7(8-s)\le(8-s)^2,
\]
so \(s\le1\).

### Lemma 2.2 — three distinct R-only transversals partition \(R\)

There are at most three distinct R-only eight-transversals: four such sets would have union size at least \(4\cdot8-\binom42=26>24\). If there are three, their union has size at least \(24-3=21\), so at most three points of \(R\) are uncovered.

Suppose two of the three sets intersect at \(p\). Every one of the seven witness blocks containing \(p\) must also contain an uncovered point: if \(p\) belongs to exactly two sets, the block's remaining R-points must hit the third set and then lie outside the union; if \(p\) belongs to all three, both remaining R-points lie outside the union. Pairwise linearity permits at most one witness block for each pair \(p r\), so seven blocks containing \(p\) require at least seven uncovered points, contradicting the bound of three. Therefore the three sets are pairwise disjoint and partition \(R\).

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

Suppose now the R-only neighborhoods comprise three distinct sets \(S_1,S_2,S_3\). By Lemma 2.2 they partition \(R\). Write \(G_i\subset W\) for the vertices whose U-neighborhood is exactly \(S_i\), and \(m_i=|G_i|\).

Every vertex of \(S_i\) has at most one H-neighbor in each other \(S_j\): for each \(t\in T\), the witness containing \(t\) and the given vertex supplies a distinct nonneighbor in \(S_j\). It follows from \(\alpha(H)\le4\) and \(T\) anticomplete to \(R\) that each \(S_i\) is a clique. Each \(G_i\) is also a clique, since two nonadjacent vertices in \(G_i\), together with a nonadjacent pair from the other two parts and a point of \(T\), would be an independent five-set. By definition, \(G_i\) is complete to \(S_i\). Therefore
\[
m_i\ge4\quad\Longrightarrow\quad S_i\cup G_i\cong K_{8+m_i}\supseteq K_{12}, \tag{2}
\]
contrary to \(\omega(H)\le11\).

### Lemma 2.4 — a high neighborhood must contain a part, or exceeds its W-degree

Let \(y\in W\) have \(q_y\in\{9,10,11\}\) and \(b_y=|N_H(y)\cap T|<7\). If \(N_H(y)\cap R\) does not contain a particular \(S_i\), pair-counting against the \(7-b_y\) partitions it hits gives
\[
|N_H(y)\cap S_i|\le1+b_y. \tag{3}
\]
Indeed, the pairs between \(N_H(y)\cap R\setminus S_i\) and \(S_i\setminus N_H(y)\) are distinct across the \(7-b_y\) partitions.

For \(q_y=9\), \(b_y\in\{0,1\}\), so (3) bounds each intersection by two; the neighborhood has at least eight R-points and therefore must contain one of the three parts. For \(q_y=10\), \(b_y\in\{0,1\}\) similarly forces a part. If \(q_y=10,b_y=2\) and no part is contained, each other part has at least five vertices outside \(N_H(y)\). If \(y\) missed a vertex of any \(G_i\), choose a nonadjacent pair from the other two parts outside \(N_H(y)\), and a point of \(T\setminus N_H(y)\); this gives an independent five-set. Thus \(y\) would be adjacent to every vertex in \(G_1\cup G_2\cup G_3\), forcing \(d_H(y,W)\ge m\). In the cases below \(m\ge7\), whereas \(d_H(y,W)=12+\epsilon_y-10\le6\), impossible. So a part is contained.

For \(q_y=11,b_y\le3\), if no part is contained, every part has at least four vertices outside \(N_H(y)\). The same independent-five argument forces \(y\) adjacent to all \(G_i\), hence \(d_H(y,W)\ge m\ge9\), but \(d_H(y,W)=1+\epsilon_y\le5\). Therefore \(N_H(y)\cap R\) contains a part.

Finally, if \(y\) contains \(S_i\) and \(b_y<7\), then \(y\) is adjacent to every vertex of \(G_i\). Otherwise choose a nonadjacent pair from the other two parts outside \(N_H(y)\) (each loses at most three points to \(y\)), and a point of \(T\setminus N_H(y)\); together with \(y\) and the missed \(G_i\)-vertex this is an independent five-set.

If two high vertices \(y,z\) with \(b_y,b_z<7\) both contain the same \(S_i\), then they are adjacent. Each has at most three R-neighbors outside \(S_i\), so each of the other two parts has at least two vertices outside both neighborhoods. Choose a nonadjacent pair from those two sets; also choose \(t\in T\setminus(N_H(y)\cup N_H(z))\), which exists because \(b_y+b_z\le6\). If \(y,z\) were nonadjacent these five vertices would be independent. Hence they are adjacent. Combined with the previous paragraph, two such vertices sharing a part of multiplicity two form a \(K_{12}\) with that part and its \(G_i\).

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

### Cases \(m=8\) and \(m=7\): first force three distinct sets

Suppose there were only two distinct R-only sets \(S_1,S_2\). Their union misses at least eight points of \(R\). Every uncovered point requires at least three special incidences, so the uncovered points require at least 24 special incidences in total.

But every high vertex with \(b<7\) must contain one of \(S_1,S_2\): otherwise (3) bounds its intersection with each by at most three, while its R-neighborhood has at least eight points. Thus each such high vertex contributes at most \(q-b-8\le2\) special incidences outside \(S_1\cup S_2\). In the \(m=8\) profiles, the T-type neighborhoods contribute at most three incidences, the low-\(b\) high vertices contribute at most two more (or at most three in the \(q=9,9,9\) family), and a possible \(b=7,q=9\) vertex contributes at most two. The total is at most five. In the \(m=7\) profile, the two T-type neighborhoods and three low-\(b\) high vertices likewise contribute at most \(2+3=5\). This is below 24, contradiction.

Therefore the \(m=8,7\) cases also have three distinct R-only sets, which partition \(R\) by Lemma 2.2.

### Case \(m=8\)

The three multiplicities sum to eight. Any multiplicity four gives a \(K_{12}\); otherwise they are \(3,3,2\). The two high vertices with \(b<7\) must each contain a part. To avoid an immediate \(K_{12}\), both must contain the unique part of multiplicity two. Lemma 2.4 makes both complete to its \(G_i\), and the pairwise-adjacency conclusion of that lemma forces them adjacent. The part, its two-vertex group, and these two high vertices form a \(K_{12}\), contradiction.

### Case \(m=7\)

The three multiplicities sum to seven. A multiplicity four gives a \(K_{12}\). Otherwise the only patterns are \(3,3,1\) and \(3,2,2\). There are three high vertices with \(b<7\), each forced to contain one of the parts.

- For \(3,3,1\), any high vertex containing a multiplicity-three part gives a \(K_{12}\). Thus, to avoid contradiction, all three high vertices would have to contain the singleton part. They are pairwise adjacent by Lemma 2.4, and each is complete to that part and its one-vertex group; together these make a \(K_{12}\).
- For \(3,2,2\), any high vertex containing the multiplicity-three part gives a \(K_{12}\). Hence all three must choose one of the two multiplicity-two parts. By pigeonhole, two choose the same part; Lemma 2.4 forces them adjacent, giving a \(K_{12}\) with that part and its group.

Both subcases contradict \(\omega(H)\le11\).

Every profile under \(S_0=13\) is impossible. Combining with the already-audited universal \(S_0\ge12\) theorem yields
\[
\boxed{S_0\ge14,\qquad \delta+\epsilon_U\le17.}
\]
Since \(\epsilon_U\le4\), this also gives \(\delta\ge5\) in the minimum-support Q33 boundary.

## 5. Scope firewall

This is a conditional exclusion of the \(S_0=13\) minimum-support E408 Q33 boundary. It uses the registered \(\omega(H)\le11\) core contract, the eight-color/56-witness exact-129 factor, pairwise linearity, and the previously proved \(S_0\ge12\) result. It does not exclude \(S_0\ge14\), larger witness-support sizes, E407 Q32, E408 Q32's separate 285-edge/excess-six core, or the original \(K_{145}\)-to-T61 bridge. EG617(\(r=12\)) remains **OPEN / NOT_CERTIFIED**.
