# E407 Q32: \(\delta=15\) non-four-partite second-Turán packing

Date: 2026-10-25  
Status: **PROVED exclusion of the entire \\(\delta=15\\) non-four-partite branch**, conditional on the retained 49-witness/core contract and the Kang–Pikhurko equality classification.

## 1. Contract and equality classification

Assume the 29-vertex graph \(L=\overline{H[U]}\) is \(K_5\)-free, non-four-partite, and has
\[
e(L)=294+\delta=309
\]
at \(\delta=15\). Brouwer's bound gives \(e(L)\le t_4(29)-\lfloor29/4\rfloor+1=315-7+1=309\), so \(L\) is an equality graph in the non-four-partite second-Turán problem.

By the Kang–Pikhurko extremal classification (Theorem 4 and Lemma 5 of *Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite*, 2005; https://matstud.org.ua/texts/2005/24_1/24_1_012_020.pdf), \(L\) has the following form:

- a complete four-partite base on 28 vertices with ordered part sizes
  \[
  (n_1,n_2,n_3,n_4)\in\{(7,7,7,7),(6,7,7,8),(6,6,8,8)\};
  \]
- two smallest parts \(P_1,P_2\), and the two larger parts \(P_3,P_4\);
- a nonempty proper subset \(A\subsetneq P_1\), with \(a=|A|\);
- a vertex \(y\in P_2\) and an extra vertex \(x\);
- all edges \(yA\) deleted, while \(x\) is adjacent to \(A\), to \(y\), and to all vertices of \(P_3\cup P_4\).

The graph has 309 edges for each of the three listed base profiles.

The 49 witness blocks are \(K_4\)'s in \(L\), and their edge sets are pairwise disjoint because two witnesses share at most one vertex.

## 2. Blocks through the exceptional vertex

Let \(t\) be the number of witness blocks containing \(x\). Every \(K_4\) avoiding \(x\) uses one vertex from each base part. A \(K_4\) containing \(x\) has one of only two forms:
\[
\{x,a',c,d\}\quad(a'\in A,\ c\in P_3,\ d\in P_4),
\]
or
\[
\{x,y,c,d\}\quad(c\in P_3,\ d\in P_4).
\]
Indeed, \(x\)'s neighbourhood is \(A\cup\{y\}\cup P_3\cup P_4\), and \(y\) is nonadjacent to every vertex of \(A\).

Write \(t_A\) and \(t_y\) for the two types, so \(t=t_A+t_y\), with
\[
t_A\le a,\qquad t_y\le1.
\]
Every \(x\)-block uses three edges incident to \(x\), and those edges cannot repeat. Since
\[
d_L(x)=n_3+n_4+a+1,
\]
we have
\[
3t\le n_3+n_4+a+1. \tag{1}
\]

Only blocks avoiding \(x\) use a \(P_1P_2\) edge. There are \(49-t\) such blocks and only \(n_1n_2-a\) available \(P_1P_2\) edges, so
\[
t\ge49-n_1n_2+a. \tag{2}
\]

## 3. Two base profiles are impossible

For \((n_1,n_2,n_3,n_4)=(6,7,7,8)\), (2) gives \(t\ge7+a\), while (1) gives \(3t\le16+a\). Hence
\[
21+3a\le16+a,
\]
impossible for \(a\ge1\).

For \((6,6,8,8)\), (2) gives \(t\ge13+a\), while (1) gives \(3t\le17+a\). Hence
\[
39+3a\le17+a,
\]
again impossible.

Therefore:

> **If the \(\delta=15\) non-four-partite case is compatible with the 49 witnesses, its Kang–Pikhurko base profile must be \((7,7,7,7)\).**

This is a genuine elimination of two of the three equality profiles, not an elimination of the whole non-four-partite case.

## 4. Exact constraints in the surviving \((7,7,7,7)\) profile

Now \(P_1,P_2,P_3,P_4\) each have size seven, \(1\le a\le6\), \(d_L(x)=15+a\), and (1)–(2) give
\[
a\le t\le\left\lfloor\frac{15+a}{3}\right\rfloor.
\]
Since \(t=t_A+t_y\), \(t_A\le a\), and \(t_y\le1\), the only possible type counts are
\[
(t_A,t_y,t)\in\{(a,0,a),(a-1,1,a),(a,1,a+1)\}.
\]

Every witness block uses one \(P_3P_4\) edge. There are 49 blocks and exactly \(7\cdot7=49\) such edges; edge-disjointness therefore forces every \(P_3P_4\) edge to occur in exactly one witness block.

The 15-edge leave \(L\setminus\bigcup_{Q}\binom Q2\) has exact pair-type counts:

| Edge type | Unused edges |
|---|---:|
| \(P_1P_2\) | \(t-a\) |
| \(P_1P_3\) | \(t_y\) |
| \(P_1P_4\) | \(t_y\) |
| \(P_2P_3\) | \(t_A\) |
| \(P_2P_4\) | \(t_A\) |
| \(P_3P_4\) | \(0\) |
| incident to \(x\) | \(15+a-3t\) |

These counts sum to 15.

There are further vertex-level equality conditions:

- Every vertex of \(P_1\) has degree 21 in \(L\). Its leave-degree is therefore a multiple of three. The total leave-degree over \(P_1\) is exactly \(3t_y\). If \(t_y=0\), every \(P_1\)-vertex has leave-degree zero. If \(t_y=1\), exactly one \(P_1\)-vertex has leave-degree three, and the three leave edges incident to \(P_1\) all meet that same vertex.
- Every vertex of \(P_3\cup P_4\) has degree 22 in \(L\), so its leave-degree is congruent to 1 modulo 3 and is at least one. The total leave-degree over each of \(P_3\) and \(P_4\) is exactly seven. Hence **every vertex of \(P_3\) and every vertex of \(P_4\) has leave-degree exactly one**.
- In particular, if a \(P_3\)- or \(P_4\)-vertex occurs in a witness block with \(x\), its unique leave edge must go to \(P_1\) or \(P_2\); if it does not occur in an \(x\)-block, its unique leave edge is its unused edge to \(x\).

These are exact packing conditions. They do not yet contradict the balanced profile.

### Color-class omission ledger

Each exact-129 color class contains seven disjoint 4-sets, so it uses 28 of the 29 vertices of \(U\) and omits exactly one vertex.

- A class with no \(x\)-block uses one vertex from each of \(P_1,P_2,P_3,P_4\) in every block, so it covers all 28 base vertices and omits \(x\).
- A class with an \(x\)-block of type \(A\) covers all of \(P_1,P_3,P_4\) and six vertices of \(P_2\), so it omits one \(P_2\)-vertex.
- A class with an \(x\)-block of type \(y\) covers all of \(P_2,P_3,P_4\) and six vertices of \(P_1\), so it omits one \(P_1\)-vertex.

Let \(o_v\) be the number of color classes omitting \(v\). Then
\[
o_x=7-t,\quad \sum_{v\in P_1}o_v=t_y,\quad
\sum_{v\in P_2}o_v=t_A,\quad o_v=0\ \ (v\in P_3\cup P_4).
\]
Each vertex occurs in \(7-o_v\) witness blocks, so its leave degree is \(d_L(v)-3(7-o_v)\). This recovers the exact residues above: \(3o_v\) on \(P_1\) and \(P_2\setminus\{y\}\), \(1\) on \(P_3\cup P_4\), and \(15+a-3t\) at \(x\). At \(y\), the formula is \(1-a+3o_y\).

This ledger ties the 15-edge leave to the seven color classes; it still does not give a contradiction.

### Core-to-\(W\) degree restriction on the exceptional vertex

The Kang–Pikhurko exceptional vertex \(x\) is also a vertex of \(H[U]\). Since \(|U|=29\) and \(d_L(x)=15+a\),
\[
d_{H[U]}(x)=28-d_L(x)=13-a,
\qquad
d_H(x,W)=12+\epsilon_x-(13-a)=a-1+\epsilon_x.
\]
Here \(0\le\epsilon_x\le\epsilon_U\le1\).

The \(\delta=15\) \(W\)-profiles are already classified in NON_FOUR_PARTITE_TERMINAL.md:
- if \(\epsilon_U=0\), \(H[W]\) is either \(K_3\cup K_5\cup K_5\cup K_5\), \(K_4\cup K_4\cup K_4\cup K_6\), or \(K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge;
- if \(\epsilon_U=1\), \(H[W]=K_4\cup K_4\cup K_5\cup K_5\).

When \(H[W]\) is a disjoint union of four cliques, \(\alpha(H)\le4\) forces every \(u\in U\) to be complete to at least one whole clique component; otherwise one non-neighbour from each component, together with \(u\), is an independent 5-set. The same conclusion holds in the one-cross-edge profile for a vertex with at most five \(W\)-neighbours: avoiding an independent transversal without being complete to a component would require adjacency to at least three vertices in each of the two endpoint \(K_4\)'s, already six neighbours.

Applying this to \(x\) gives:
- \(\epsilon_U=0\), profile \(K_3\cup K_5^3\): \(a-1\ge3\), so \(a\ge4\);
- \(\epsilon_U=0\), either profile with minimum clique size four: \(a-1\ge4\), so \(a\ge5\);
- \(\epsilon_U=1\): \(a-1+\epsilon_x\ge4\), so \(a\ge4\), and if \(a=4\), the unique unit of \(U\)-excess must be at \(x\) (\(\epsilon_x=1\)).

Therefore the Kang–Pikhurko subset size \(a\in\{1,\ldots,6\}\) is reduced to \(a\in\{4,5,6\}\); \(a=4\) survives only with \(H[W]=K_3\cup K_5^3,\epsilon_U=0\), or with \(\epsilon_U=1,\epsilon_x=1\). This is a necessary condition, not a contradiction.

## 5. Exact leave ledger in the balanced profile

Before using the core-to-\(W\) degree constraints below, the edge-packing analysis reduces the non-four-partite branch to one balanced Kang–Pikhurko construction with:
- \(a\in\{1,\ldots,6\}\);
- one of the three \((t_A,t_y,t)\) patterns above;
- a 49-block \(K_4\) edge-packing that covers every \(P_3P_4\) pair;
- the prescribed 15-edge leave and its vertex-level degree residues;
- the exact color-class omission ledger.

The balanced profile is then eliminated by the following core-degree argument.

## 6. The core-to-\(W\) degree constraints exclude the balanced profile

The exact ledger gives
\[
e(H[W])=48-\epsilon_U-\delta=33-\epsilon_U,\qquad
\epsilon_U\in\{0,1\}.
\]
Since \(\alpha(H[W])\le4\), the complement \(\overline{H[W]}\) is \(K_5\)-free. It has 120 edges if \(\epsilon_U=0\), and 121 if \(\epsilon_U=1\). The non-four-partite Brouwer bound on 18 vertices is
\[
t_4(18)-\lfloor18/4\rfloor+1=121-4+1=118.
\]
Therefore \(\overline{H[W]}\) is four-partite in either case. The possible \(H[W]\) clique-part profiles are exactly those listed in NON_FOUR_PARTITE_TERMINAL.md; this \(W\)-side classification does not assume that \(L\) is four-partite.

In the surviving balanced Kang–Pikhurko profile, the exceptional vertex \(x\) and distinguished base vertex \(y\) have
\[
d_{H[U]}(x)=13-a,\qquad d_{H[U]}(y)=6+a.
\]
Writing \(\epsilon_x=d_H(x)-12\) and \(\epsilon_y=d_H(y)-12\),
\[
d_H(x,W)=a-1+\epsilon_x,\qquad d_H(y,W)=6-a+\epsilon_y,\qquad
\epsilon_x+\epsilon_y\le\epsilon_U\le1. \tag{3}
\]

For a disjoint union of four clique parts in \(H[W]\), every \(u\in U\) must be complete to at least one whole part: otherwise choose a non-neighbour of \(u\) from each part to obtain an independent 5-set. The same is true in the one-cross-edge \((4,4,5,5)\) profile for any \(u\) with at most five \(W\)-neighbours. If \(u\) were not complete to any part, avoiding an independent transversal would require its neighbourhood to contain all but the cross-edge endpoint in each of the two endpoint parts, costing at least \(3+3=6\) neighbours.

Now split by \(\epsilon_U\).

### Case \(\epsilon_U=0\)

Then \(\epsilon_x=\epsilon_y=0\), so the two \(W\)-degrees in (3) are \(a-1\) and \(6-a\).

- If \(H[W]=K_3\cup K_5\cup K_5\cup K_5\), both \(x\) and \(y\) must be complete to a component of size at least three. This requires \(a-1\ge3\) and \(6-a\ge3\), i.e. \(a\ge4\) and \(a\le3\), contradiction.
- If \(H[W]=K_4\cup K_4\cup K_4\cup K_6\), both must have at least four \(W\)-neighbours. This requires \(a\ge5\) and \(a\le2\), contradiction.
- If \(H[W]\) has clique-part sizes \((4,4,5,5)\) with one cross edge, both \(W\)-degrees are at most five, so both must be complete to a whole part of size at least four. Again \(a\ge5\) and \(a\le2\), contradiction.

Thus \(\epsilon_U=0\) is impossible.

### Case \(\epsilon_U=1\)

Here \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), a disjoint union of cliques of minimum size four. Equation (3) and the whole-part condition imply
\[
a-1+\epsilon_x\ge4,\qquad 6-a+\epsilon_y\ge4.
\]
The first inequality gives \(a\ge5-\epsilon_x\ge4\); the second gives \(a\le2+\epsilon_y\le3\). Contradiction.

Therefore the balanced Kang–Pikhurko profile is impossible as well.

> **Conclusion:** the \(\delta=15\), \(L\) non-four-partite branch is excluded under the retained core/witness contract. This does not exclude the \(\delta=15\) four-partite branch, \(\delta=16\), or any lower-\(\delta\) branch; E407 Q32 overall remains OPEN / NOT_CERTIFIED.
