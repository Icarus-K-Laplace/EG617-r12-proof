# E408 Q33 minimum-support boundary: exclude \(S_0=12\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61, exact-129 factor, and \(31\)-point/\(56\)-witness contracts.  
Scope: strengthens the universal minimum-support bound from \(S_0\ge12\) to \(S_0\ge13\). It does not close E408 Q33.

## 1. Contract and inherited structure

Use the notation of the witness-packing line:
- \(H\) is the \(47\)-vertex, \(284\)-edge core, \(\alpha(H)\le4\), and \(d_H(x)=12+\epsilon_x\), with \(\epsilon_x\ge0\) and \(\sum_H\epsilon_x=4\).
- \(U\) has \(31\) vertices, \(W=H\setminus U\) has \(16\), and \(\mathcal Q\) consists of \(56\) pairwise-linear independent \(4\)-sets. Within each exact color the selected \(Q\)-sets are disjoint; any two distinct \(Q\)-sets intersect in at most one point.
- \(L=\overline{H[U]}\), \(e(L)=336+\delta\), \(\epsilon_U=\sum_{u\in U}\epsilon_u\), and \(S_0=\epsilon_U+2\delta\).
- The inherited \(S_0\ge12\) theorem gives a unique possible \(7\)-point transversal \(T\), \(R=U\setminus T\), \(|R|=24\). The set \(T\) is a clique in \(H\), anticomplete to \(R\). For every \(t\in T\), the eight \(Q\)-blocks containing \(t\), after deleting \(t\), partition \(R\) into eight triples.
- Every \(w\in W\) has \(q_w=|N_H(w)\cap U|\ge7\). There are at most four vertices with \(q_w=7\); each such vertex has \(U\)-neighborhood exactly \(T\). A \(q_w=8\) neighborhood is either \(T\cup\{r\}\) for one \(r\in R\), or an \(R\)-only \(8\)-set transversal of all seven partitions.
- Distinct \(R\)-only \(8\)-transversals intersect in at most one point. For an \(R\)-only \(8\)-transversal \(S\), write \(G(S)\subseteq W\) for the \(W\)-vertices with \(U\)-neighborhood \(S\).

For \(r\in R\), let \(j_r\) be the degree of \(r\) in the \(\delta\) leftover edges of \(L\) not used by the witness \(K_4\)'s, and put \(g_r=\epsilon_r+j_r\). All leftover edges lie inside \(R\), because every \(T\)-to-\(R\) edge of \(L\) belongs to a \(Q\)-block. Hence
\[
\sum_{r\in R}g_r=S_0-\epsilon_T.
\]
Each \(r\in R\) lies in one \(Q\)-block for each \(t\in T\), so the \(21\) incident \(L\)-edges contributed by these seven witness \(K_4\)'s are distinct; thus \(d_L(r)=21+j_r\). Since \(d_H(r,U)=30-d_L(r)=9-j_r\), it follows that \(d_H(r,W)=12+\epsilon_r-d_H(r,U)=3+\epsilon_r+j_r\). For each \(r\), let \(a_r\) count the special incidences at \(r\) from \(W\)-vertices whose \(U\)-neighborhood is not an \(R\)-only \(8\)-set. If \(s_r\) is the number of \(R\)-only \(8\)-neighborhoods containing \(r\), the exact row identity is
\[
s_r=3+g_r-a_r. \tag{1}
\]

Assume for contradiction that \(S_0=12\). Then
\[
\sum_{w\in W}q_w=e_H(U,W)=114+S_0=126. \tag{2}
\]

## 2. Two lemmas used in the finite case split

### Lemma 2.1 — cross-part degree and clique forcing

Let \(S_i,S_j\subset R\) be distinct \(R\)-only \(8\)-transversals. Every vertex of \(S_i\) has at most one \(H\)-neighbor in \(S_j\).

**Proof.** Fix \(u\in S_i\). For each \(t\in T\), the \(R\)-triple in the unique \(Q\)-block containing \(t,u\) has exactly one point \(v_t\in S_j\), because \(S_j\) hits each of the eight triples in the \(t\)-partition exactly once. The \(Q\)-block is independent in \(H\), so \(u\) and \(v_t\) are nonadjacent. The seven \(v_t\)'s are distinct: otherwise the same pair \(u,v_t\) would lie in two \(Q\)-sets, violating linearity. Thus \(u\) has at least seven nonneighbors in the \(8\)-set \(S_j\), leaving at most one neighbor. \(\square\)

Consequences:
1. Every \(S_i\) in a partition \(R=S_1\dot\cup S_2\dot\cup S_3\) by \(R\)-only \(8\)-transversals is a clique in \(H\). Otherwise choose two nonadjacent vertices in \(S_i\), a common nonneighbor in \(S_j\), and then a vertex in \(S_k\) nonadjacent to those three; append a point of \(T\) to get an independent \(5\)-set.
2. Each \(G(S_i)\) is a clique. Otherwise two nonadjacent vertices with neighborhood \(S_i\), together with a nonadjacent pair from the other two parts and a point of \(T\), form an independent \(5\)-set.
3. If \(y\in W\) has \(q_y\in\{9,10\}\) and its \(U\)-neighborhood contains \(S_i\), then \(y\) is adjacent to every vertex of \(G(S_i)\). The set \(N_H(y)\cap R\) has at most two points outside \(S_i\), so each of \(S_j\setminus N_H(y)\) and \(S_k\setminus N_H(y)\) has at least six points; the cross-part degree bound gives a nonadjacent pair \(a,b\) in those two sets. Also \(T\setminus N_H(y)\ne\varnothing\). If \(y\) missed some \(w\in G(S_i)\), then \(y,w,a,b,t\) would be an independent \(5\)-set. Thus \(|G(S_i)|\ge3\) immediately gives a \(K_{12}\) when \(S_i\subseteq N_H(y)\).

### Lemma 2.2 — partition even with two uncovered points

Consider a family of \(m\in\{8,9,10\}\) \(R\)-only \(8\)-neighborhoods, with multiplicity, whose union misses at most two points of \(R\). Then its distinct sets are exactly three \(8\)-sets \(S_1,S_2,S_3\), and they partition \(R\).

**Proof.** The union has size at least \(22\). Four distinct \(8\)-sets with pairwise intersections at most one would have union size at least \(8\cdot4-\binom42=26>24\), while two sets cover at most \(16\) points. Thus there are exactly three distinct sets. If their union has size \(23\), the original one-uncovered-point argument applies: the unique intersection point of two sets lies in seven \(Q\)-blocks, and each such block must also contain the uncovered point, violating linearity. If the union has size \(22\), there are two uncovered points \(r_0,r_1\) and two duplicated incidences. Either a point \(p\) lies in exactly two of the \(S_i\), or one point lies in all three. In the first case, each of the seven \(Q\)-blocks containing \(p\) must contain one of \(r_0,r_1\), but each pair \(p,r_0\) and \(p,r_1\) can occur in at most one \(Q\)-block. In the triple-intersection case, every \(Q\)-block containing the common point must contain both \(r_0,r_1\), again violating linearity. Therefore the union is all of \(R\). \(\square\)

### Multiplicity and clique bookkeeping

From (1), for any distinct \(R\)-only \(8\)-set \(S\) occurring \(m_S\) times,
\[
8m_S\le\sum_{r\in S}s_r
\le24+\sum_{r\in R}g_r
=36-\epsilon_T\le36.
\]
So \(m_S\le4\). If the distinct sets partition \(R\), their multiplicities sum to \(m\). Any multiplicity \(4\) gives \(|G(S_i)|=4\), and \(S_i\cup G(S_i)\) is a \(K_{12}\), impossible. If a multiplicity-one set occurs, each of its eight points has \(s_r=1\), hence \(a_r=2+g_r\ge2\); this requires at least \(16\) special incidences on that set.

For a high vertex \(y\in W\), put \(b_y=|N_H(y)\cap T|\). If \(q_y=9\), then \(b_y\in\{0,1,7\}\); if \(q_y=10\), then \(b_y\in\{0,1,2,7\}\). When \(b_y<7\), its \(R\)-neighborhood is a \((q_y-b_y)\)-point transversal of the \(7-b_y\) partitions indexed by \(T\setminus N_H(y)\). Pair-counting against an \(R\)-only \(8\)-transversal \(S\) gives
\[
|N_H(y)\cap R\cap S|\le(q_y-b_y)-(7-b_y)=q_y-7\le3,
\]
unless \(N_H(y)\cap R\) contains \(S\). In particular, if such a high neighborhood does not contain any \(S_i\) in a partition of \(R\), it meets each \(S_i\) in at most three points; if \(q_y=9\), it meets each in at most two points.

## 3. Exhaustion of \(S_0=12\)

Let \(N_7=|\{w\in W:q_w=7\}|\). By (2) and \(q_w\ge7\),
\[
126=\sum_W q_w\ge7N_7+8(16-N_7)=128-N_7,
\]
so \(N_7\ge2\); the inherited bound gives \(N_7\le4\). For each case, let \(a\) be the number of \(q=8\) vertices with neighborhood \(T\cup\{r\}\). Let \(B\) be the sum of \(b_y\) over the high vertices with \(q_y>8\). The \(T\)-to-\(W\) degree sum gives
\[
42+\epsilon_T=7N_7+7a+B,\qquad
\epsilon_T=7N_7+7a+B-42. \tag{3}
\]
Every zero-excess \(t\in T\) has \(H\)-degree six, so the \(N_7\) vertices and the \(a\) \(T\)-type \(q=8\) vertices leave room for at most \(6-N_7-a\) high vertices adjacent to \(t\). At least three points of \(T\) have zero excess. This bounds \(a\) and, with (3), leaves only the cases below.

For each row, \(m\) is the number of \(R\)-only \(8\)-neighborhoods, and \(A\) is the total number of special \(R\)-incidences. Equation (1) gives the check \(8m=72+(12-\epsilon_T)-A\).

| \(N_7\) | high degrees \(q_y\) | forced \(a\) and high \(b_y\) | \(\epsilon_T\) | \(m\) | \(A\) |
|---:|---|---|---:|---:|---:|
| 2 | fourteen \(8\)'s | \(a=4\) | 0 | 10 | 4 |
| 3 | one \(9\), twelve \(8\)'s | \(b=7,a=2\) | 0 | 10 | 4 |
| 3 | one \(9\), twelve \(8\)'s | \(b=1,a=3\) | 1 | 9 | 11 |
| 3 | one \(9\), twelve \(8\)'s | \(b=0,a=3\) | 0 | 9 | 12 |
| 4 | two \(9\)'s, ten \(8\)'s | \(b_y=b_z=7,a=0\) | 0 | 10 | 4 |
| 4 | two \(9\)'s, ten \(8\)'s | one \(b=7\), other \(c\in\{0,1\}\), \(a=1\) | \(c\) | 9 | \(12-c\) |
| 4 | two \(9\)'s, ten \(8\)'s | \(b_y,b_z\in\{0,1\}\), \(a=2\) | \(B=b_y+b_z\) | 8 | \(20-B\) |
| 4 | one \(10\), eleven \(8\)'s | \(b=7,a=1\) | 0 | 10 | 4 |
| 4 | one \(10\), eleven \(8\)'s | \(b\in\{0,1,2\},a=2\) | \(b\) | 9 | \(12-b\) |

An uncovered point \(r\) has \(s_r=0\), so (1) forces \(a_r=3+g_r\ge3\). This gives the uncovered-point bounds used below: with four total special incidences there can be at most one uncovered point; with three \(T\)-type extras plus one high vertex, an uncovered point requires at least two \(T\)-type extras and the high vertex at the same point, so there is at most one; with one \(T\)-type extra plus two high vertices, there is at most one; with two \(T\)-type extras and two high vertices, every uncovered point must receive at least one of those two \(T\)-type extras, so there are at most two. When both high \(q=9\) vertices have \(b=7\), each has only two \(R\)-neighbors and no point can receive three special incidences. When the high \(q=10\) vertex has \(b=7\), its three \(R\)-neighbors plus one \(T\)-type extra give at most two incidences per point, so there are no uncovered points.

The remaining subcases are excluded as follows.

### Case A: \(N_7=2\)

Equation (3) and the zero-excess bound force \(a=4,\epsilon_T=0\). There are ten \(R\)-only \(8\)-neighborhoods and four special \(R\)-incidences, so at most one point is uncovered. Lemma 2.2 gives a partition of \(R\) into three distinct sets. The multiplicity patterns for ten copies are \((4,4,2)\) or \((4,3,3)\). The first requires at least eight special incidences on the multiplicity-two set, but only four exist. The second has a multiplicity-four set and hence a \(K_{12}\). Contradiction.

### Case B: \(N_7=3\)

The remaining degrees are one \(9\) and twelve \(8\)'s. Equation (3) leaves \(b=7,a=2\), \(b=1,a=3\), or \(b=0,a=3\), as listed in the table.

- For \(b=7\), there are ten \(R\)-only \(8\)-sets and four special incidences. The multiplicity-two pattern \((4,4,2)\) is impossible; \((4,3,3)\) gives a \(K_{12}\).
- For \(b=1\) or \(b=0\), there are nine \(R\)-only \(8\)-sets and at most one uncovered point. The patterns are \((4,4,1)\), \((4,3,2)\), or \((3,3,3)\). The first requires at least sixteen special incidences on the multiplicity-one set, exceeding \(A=11\) or \(12\); the second gives a \(K_{12}\). In the last pattern, the three sets partition \(R\). The high vertex's \(R\)-neighborhood has size \(8\) or \(9\) and is a transversal of six or seven partitions. It must contain one of the three parts: otherwise pair-counting bounds each intersection by two, covering at most six points. That part has multiplicity three, so it and its \(G_i\) plus the high vertex form a \(K_{12}\). Contradiction.

### Case C: \(N_7=4\), two vertices of degree \(9\)

Let the high vertices be \(y,z\).

- If \(a=0\), (3) forces \(b_y=b_z=7\). There are ten \(R\)-only sets and four special incidences. No point can be uncovered, because each high vertex has only two \(R\)-neighbors. The \((4,4,2)\) pattern is impossible by the special-incidence count, and \((4,3,3)\) gives a \(K_{12}\).
- If \(a=1\), exactly one of \(b_y,b_z\) is \(7\); the other is \(c\in\{0,1\}\). There are nine \(R\)-only sets, at most one uncovered point, and \(A=12-c\). The \((4,4,1)\) pattern needs sixteen special incidences; \((4,3,2)\) gives a \(K_{12}\). In the \((3,3,3)\) pattern, the high vertex whose \(b\) is \(c\) has an \(R\)-neighborhood of size \(8\) or \(9\) and is a transversal of six or seven partitions. It must contain a part \(S_i\), and then \(S_i\cup G(S_i)\) plus that vertex is a \(K_{12}\).
- If \(a=2\), both high \(b\)'s are \(0\) or \(1\), there are eight \(R\)-only sets, and at most two points are uncovered. Lemma 2.2 gives a partition \(R=S_1\dot\cup S_2\dot\cup S_3\). Any multiplicity-four pattern gives a \(K_{12}\); the only remaining pattern is \((3,3,2)\). Call the multiplicity-two part \(S_3\). Each high vertex's \(R\)-neighborhood has size \(8\) or \(9\) and is a transversal of six or seven partitions. It must contain one of the \(S_i\); if it contains \(S_1\) or \(S_2\), the multiplicity-three group gives a \(K_{12}\). Hence both high vertices contain \(S_3\). Each is adjacent to all of \(S_3\) and all of \(G(S_3)\), which has size two. They must also be adjacent to each other: otherwise choose a nonadjacent pair from \(S_1,S_2\) outside both high neighborhoods and a point of \(T\) outside their at-most-two \(T\)-neighbors to form an independent \(5\)-set. Thus \(S_3\cup G(S_3)\cup\{y,z\}\) is a \(K_{12}\). Contradiction.

### Case D: \(N_7=4\), one vertex of degree \(10\)

Let that high vertex be \(y\).

- If \(a=1\), (3) forces \(b=7\). There are ten \(R\)-only sets and four special incidences. The \((4,4,2)\) pattern is impossible by the special-incidence count, and \((4,3,3)\) gives a \(K_{12}\).
- If \(a=2\), then \(b\in\{0,1,2\}\), there are nine \(R\)-only sets, and at most one point is uncovered. The \((4,4,1)\) pattern needs sixteen special incidences, while \(A=12-b\le12\); \((4,3,2)\) gives a \(K_{12}\). In the \((3,3,3)\) pattern the three sets partition \(R\). If \(N_H(y)\cap R\) contains one part, that part and its size-three group plus \(y\) give a \(K_{12}\). If \(b=0\) and it contains no part, each intersection is at most three and the three parts cover at most nine points, less than \(|N_H(y)\cap R|=10\). If \(b=1\) or \(2\) and it contains no part, each \(S_i\setminus N_H(y)\) has at least five vertices. For any \(i\), if \(y\) missed a vertex in \(G(S_i)\), choose a nonadjacent pair from the other two parts outside \(N_H(y)\) and a point of \(T\setminus N_H(y)\); these five vertices would be independent. Hence \(y\) is adjacent to all nine vertices in \(G(S_1)\cup G(S_2)\cup G(S_3)\). But \(y\) already has ten neighbors in \(U\), so
\[
d_H(y,W)=12+\epsilon_y-10=2+\epsilon_y\le6,
\]
a contradiction.

All cases under \(S_0=12\) are impossible. Since \(S_0\) is integral and the inherited theorem gives \(S_0\ge12\),
\[
\boxed{S_0=\epsilon_U+2\delta\ge13.}
\]
Consequently \(\delta\ge5\), because \(\epsilon_U\le4\).

## 4. Scope firewall

This is a stronger universal lower bound for the **minimum-support \(31\)-vertex/\(56\)-witness E408 Q33 boundary**. It does not exclude the remaining \(S_0\ge13\) profiles, larger witness-support sizes, E407 Q32, E408 Q32 (285-edge core), or the original \(K_{145}\) theorem. The T61 and exact-129 factor inputs remain conditional. EG617(r=12) remains OPEN / NOT_CERTIFIED.
