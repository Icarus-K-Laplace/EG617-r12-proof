# Four-partite global compatibility: strengthened core boundary

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL:** in the 31-point / 56-witness four-partite branch, \(S_0\ge22\). The branch remains OPEN above this boundary.

## 1. Frozen four-partite contract

Assume the Q33 minimum-support contract and that L=overline(H[U]) is four-partite. Since the 56 witness four-sets are K4s in L, every witness is transversal to the four parts. The part sizes are
\[
|A|=|B|=|C|=8,\qquad |D|=7.
\]
Every pair of part sizes must have product at least 56 because the 56 witnesses use distinct cross-part pairs. A part of size at most six would force each other part to have size at least ten, impossible on 31 vertices. Thus every part has size at least seven, and at most one part can have size seven because (7cdot7<56). If all four parts had size at least eight there would be at least 32 vertices. Hence exactly one part has size seven and the other three have size eight. Every pair between D and a large part occurs in exactly one witness, so all 7·8=56 such pairs are used. The eight unused pairs between any two large parts form a perfect matching: each vertex of one part appears in seven witnesses with seven distinct vertices of the other part.

Consequences:
- D is a clique K7 in H[U], and each d in D has exactly six H-neighbours inside U.
- Every vertex in a large part has at most one H-neighbour in each other large part: seven of the eight cross-part pairs are used witness edges of L.
- Every \(w\in W\) has \(T_w=N_H(w)\cap U\) meeting all 56 witnesses.
- The exact cross-edge count is \(e_H(U,W)=114+S_0\), and
  \[
  \sum_{d\in D}d_H(d,W)=42+\epsilon_D,\qquad
  \epsilon_D=\sum_{d\in D}\epsilon_d\in[0,4].
  \]

## 2. Independent-transversal lemma for the three large parts

**Lemma 2.1.** Let \(A',B',C'\) be subsets of A,B,C obtained by excluding at most ten vertices in total, and suppose none of A',B',C' is empty. Then H has an independent transversal \(a\in A',b\in B',c\in C'\).

**Proof.** Between any two large parts every vertex has at most one H-neighbour. If all three allowed sets have size at least three, choose a in A', then b in B' nonadjacent to a, then c in C' nonadjacent to both; at most one vertex is forbidden at the second step and at most two at the third.

If one allowed set has size one, at most seven vertices were excluded from that part and at most three from the other two, so each other allowed set has size at least five. Choose the unique vertex in the singleton part, then choose a non-neighbour in a second part, then one nonadjacent to both in the third. If one allowed set has size two, at most six vertices were excluded from it and at most four from the other two, so those two allowed sets have size at least four; the same greedy choice works. \(\square\)

For \(w\in W\) with \(D\subseteq T_w\), define its extra-neighbour set
\[
E_w=T_w\setminus D\subseteq A\cup B\cup C,\qquad x_w=|E_w|=q_w-7.
\]
If two D-complete vertices w,w' are nonadjacent in H and \(|E_w|+|E_{w'}|\le10\), Lemma 2.1 implies that \(E_w\cup E_{w'}\) must cover an entire large part. Otherwise an independent transversal in the three large parts, together with w,w', would be an independent five-set in H.

In particular, if \(|E_w|+|E_{w'}|\le7\), then w and w' must be adjacent, since their union cannot cover an eight-point part.

## 3. Theorem: the four-partite branch has \(S_0\ge22\)

**Theorem 3.1.** Under the contract in Section 1,
\[
\boxed{S_0=\epsilon_U+2\delta\ge22.}
\]

**Proof.** Let
\[
Z=\{w\in W:D\subseteq T_w\},\qquad m=|Z|.
\]
For \(w\notin Z\), choose \(d\in D\setminus T_w\). The eight witnesses containing d have pairwise-disjoint triples partitioning A union B union C. Since \(T_w\) hits every witness but misses d, it must contain at least eight large-part vertices. Hence
\[
q_w\ge8,\qquad |T_w\cap D|\le q_w-8\quad(w\notin Z).
\]

Write
\[
E_Z=\sum_{w\in Z}(q_w-7),\qquad
E_N=\sum_{w\notin Z}(q_w-8).
\]
Since \(\sum_W q_w=114+S_0\),
\[
E_Z+E_N=(114+S_0)-\bigl(7m+8(16-m)\bigr)=S_0+m-14. \tag{1}
\]
The D-to-W incidence sum gives
\[
42+\epsilon_D
=\sum_{w\in W}|T_w\cap D|
\le7m+E_N. \tag{2}
\]
Combining (1) and (2),
\[
E_Z\le S_0+8m-56-\epsilon_D. \tag{3}
\]

Suppose \(S_0\le21\).

### Case 1: \(m\le4\)

Equation (2) and (1) imply
\[
42+\epsilon_D\le7m+E_Z+E_N
= S_0+8m-14\le S_0+18\le39,
\]
a contradiction. Thus \(m\ge5\).

### Case 2: \(m=5\)

By (3), \(E_Z\le S_0-16-\epsilon_D\le5\). The five extra-neighbour counts therefore sum to at most five. Every pair of vertices in Z has at most five excluded large-part vertices, so Lemma 2.1 forces the pair to be adjacent. Thus D together with the five vertices of Z is a K12 in H, contradicting \(\omega(H)\le11\).

### Case 3: \(m\ge7\)

Sort the extra counts in Z as \(x_1\le\cdots\le x_m\). If \(x_4+x_5\le7\), the five vertices with smallest extra counts are pairwise adjacent by Lemma 2.1; together with D they form a K12. Hence a hypothetical configuration must have \(x_4+x_5\ge8\).

This implies
\[
E_Z\ge4m-12.
\]
To see this, if x4>=4, then x4,...,xm are all at least four, giving E_Z>=4(m-3). If x4<=3, then x5>=8-x4 and x6,...,xm are at least x5, so E_Z>=x4+(m-4)(8-x4)>=5m-17>=4m-12 for m>=7.. But (1) gives \(E_Z\le E_Z+E_N=S_0+m-14\le m+7\). For \(m\ge7\), \(4m-12>m+7\), contradiction.

### Case 4: \(m=6\)

Equation (1) gives \(E_Z\le13\). As before, \(x_4+x_5\le7\) would yield a K12, so \(x_4+x_5\ge8\). The only possible triples of largest extra counts are
\[
(3,5,5),\qquad(4,4,4),\qquad(4,4,5),
\]
and in each case \(x_1+x_2+x_3\le1\).

The three vertices with the smallest extra counts are pairwise adjacent and adjacent to all three vertices with the largest counts. If any pair among the latter three were adjacent, those five vertices together with D would form a K12. Hence the three large-extra vertices would have to be pairwise nonadjacent.

For any such nonadjacent pair, the union of their extra-neighbour sets must cover a full large part by Lemma 2.1, since the pairwise size sum is at most ten. This is impossible in each of the three size profiles:
- For (4,4,4), every pair of four-sets must partition a large part. If (E_1\cup E_2=A) and (E_1\cup E_3=B), then (E_1\subseteq A\cap B), so (A=B) because distinct parts are disjoint. But then both (E_2) and (E_3) are the complement of (E_1) in A, so (E_2=E_3), whose union has size four and cannot cover a large part. Contradiction.
- For (4,4,5), the two four-sets must partition a large part D'. The five-set would have to cover D' with each four-set, so it would have to contain both complementary four-sets, impossible.
- For (3,5,5), each three-plus-five pair must partition the same eight-point part. Both five-sets would then be the same complement of the three-set, so they could not cover a part when paired with each other.

Thus the three large-extra vertices cannot be pairwise nonadjacent. This contradicts the requirement in Case 4.

All cases under \(S_0\le21\) are impossible, proving \(S_0\ge22\). \(\square\)

## 4. Consequences for the 284-edge core

Since \(\epsilon_U\le4\), Theorem 3.1 gives
\[
\delta\ge9.
\]
The retained W-edge budget also gives \(\delta+\epsilon_U\le17\), so \(\delta\le17\). Therefore
\[
345\le e(L)=336+\delta\le353.
\]
There are 24 unused cross-part pair slots between A,B,C. Exactly \(\delta\) of these slots are present as leftover edges of L; hence at least seven of the 24 are absent from L and are H-edges.

This is a structural restriction on the four-partite terminal, not its exclusion.

## 5. Joint seven-block compatibility ledger

The local four-partite result must be combined with the global color system, not substituted for it. The simultaneous requirements are:

- the eight selected exact-129 colors each contribute seven labeled K4 witnesses;
- every exact-129 color has ten isolated K5 components and an 11-vertex exceptional gadget in its 61-point restriction;
- for each outer target K12 block, each of the twelve row vertices has C-degree one or two into that block for every non-target color C;
- for each exact-129 color C, \(P_C+R_C=62\), \(R_C\ge7\), \(P_C\le55\), and \(M_C\ge15+P_C\);
- the labeled blocker/component cross-cut constraints in SEVEN_BLOCK_INCIDENCE_LEDGER.md hold;
- the 56 K4 witness blocks cover 336 distinct L-edges, and the \(\delta\ge9\) leftover L-edges must occupy unused matching-pair slots among A,B,C.

A component represented as an exact size-five blocker in two outer blocks forces a C-colored edge between its two block representatives. That edge is a baseline one-per-color edge unless an additional repeated C-incidence is separately proved; it must not be automatically counted in \(P_C\).

No contradiction between these global requirements and the remaining \(\delta\in[9,17]\) four-partite contract has yet been established. The four-partite branch remains OPEN.
