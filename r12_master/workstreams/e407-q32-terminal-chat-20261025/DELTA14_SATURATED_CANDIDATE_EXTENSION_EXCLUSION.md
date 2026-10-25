# E407 Q32: exclude every W-extension of the explicit saturated local model

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL for the explicit \((5,5,2,1,2)\) \(C_5\)-blow-up candidate only.** This is not a classification of all admissible saturated local graphs \(J\).

Dependencies: the exact 47-core degree/excess contract; \(\alpha(H)\le4\), \(\omega(H)\le11\); the explicit local model in DELTA14_SATURATED_LOCAL_MODEL.md; Brouwer/Turán W-profile classification; and the independent-transversal lemma in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md.

## 1. Fixed local degree ledger

Let
\[
H[U]=K_7^A\dot\cup K_7^B\dot\cup \overline J
\]
be the explicit candidate, with \(J\) the blow-up of \(C_5\) with part sizes \((5,5,2,1,2)\). Its degree sequence inside \(U\) is
\[
6^{14},\quad 7^{10},\quad 8^4,\quad 10^1.
\]
The unique degree-10 vertex \(d_0\) is the singleton part of the blow-up. Thus
\[
d_H(d_0,W)=12+\epsilon_{d_0}-10=2+\epsilon_{d_0},
\qquad 0\le\epsilon_{d_0}\le\epsilon_U.
\]
Whenever \(W\) is the union of four pairwise-antocomplete clique parts, every \(u\in U\) must be complete to at least one whole part: otherwise choosing a non-neighbour from each part gives an independent 5-set with \(u\).

## 2. The case \(\epsilon_U=1\) is impossible

The exact ledger gives \(e(H[W])=33\). The retained W-profile classification leaves three cases.

### Case 2a: \(H[W]=K_3\dot\cup 3K_5\)

If \(\epsilon_{d_0}=0\), then \(d_0\) has only two W-neighbours and is not complete to any part, contradiction. Hence \(\epsilon_{d_0}=1\), all other U-excesses vanish, and \(d_0\) is complete to the \(K_3\) part \(P_0\).

Every vertex of \(C\cup E\) in the local \(J\)-blow-up has \(U\)-degree eight, hence W-degree four. It must be complete to \(P_0\), with one extra W-edge. Each \(a\in A\) or \(b\in B\) has W-degree six, so it is complete either to \(P_0\) with three extra edges or to one \(K_5\) with one extra edge. Every such assignment is unique, since a W-degree-six vertex cannot be complete to two distinct parts (the smallest sum of two part sizes is \(3+5=8\)).

**No \(A\)- or \(B\)-vertex can be assigned to \(P_0\).** Suppose \(a\in A\) is complete to \(P_0\). For any \(b\in B\):
- if \(b\) is also assigned to \(P_0\), their combined extra-edge budget outside \(P_0\) is at most six, so they cannot jointly cover two of the three \(K_5\) parts (covering any one requires five incidences, and covering two requires at least ten);
- if \(b\) is assigned to a \(K_5\), their combined extra-edge budget is at most \(3+1=4\), less than five, so each of the two other \(K_5\) parts contains a vertex nonadjacent to both.

In either case there are two distinct \(K_5\) parts with vertices \(w_i,w_j\) nonadjacent to both \(a,b\). Since \(d_0,a,b\) are pairwise nonadjacent and \(d_0\) is anticomplete to all \(K_5\) parts, \(\{d_0,a,b,w_i,w_j\}\) is an independent 5-set. Contradiction. The same argument excludes B-vertices from \(P_0\).

**No A-vertex and B-vertex can be assigned to the same \(K_5\).** Each has only one extra edge outside its assigned \(K_5\), so their combined budget is two. The other two \(K_5\) parts each retain a common non-neighbour, again giving an independent 5-set with \(d_0\).

Therefore each of \(A\) and \(B\) must be assigned among the three \(K_5\) parts, with disjoint sets of parts used by the two sides. A \(K_5\) part can receive at most six vertices from one side: seven such vertices together with that \(K_5\) would form a forbidden \(K_{12}\). Thus each of the seven vertices of \(A\) requires at least two \(K_5\) parts, and the same is true for \(B\). Their assigned part sets are disjoint, requiring at least four \(K_5\) parts, but only three exist. Contradiction.

### Case 2b: \(H[W]=3K_4\dot\cup K_6\)

Here every W-part has size at least four, but \(d_0\) has at most three W-neighbours because \(\epsilon_{d_0}\le1\). Thus \(d_0\) cannot be complete to any part, contradicting the forced complete-to-a-part property.

### Case 2c: \(H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5\) plus one cross-edge

All four clique parts have size at least four. Since \(|N_W(d_0)|=2+\epsilon_{d_0}\le3\), apply the second independent-transversal consequence from DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md: after deleting any at most three vertices, an independent transversal avoiding the deleted set still exists when there is at most one cross-edge. Let \(T\subseteq W\setminus N_W(d_0)\) be such a transversal. Then \(T\cup\{d_0\}\) is an independent 5-set, contradiction.

All three \(\epsilon_U=1\) profiles are excluded.

## 3. The case \(\epsilon_U=2\) is impossible

Turán equality forces
\[
H[W]=P_0\dot\cup P_1\dot\cup P_2\dot\cup P_3
=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5
\]
with no cross-edges. Since every \(u\in U\) must be complete to a W-part, \(d_0\) cannot have fewer than four W-neighbours. Thus \(\epsilon_{d_0}=2\), \(d_0\) is complete to one \(K_4\) part \(P_0\), and all other U-excesses vanish.

Every U-vertex is complete to a unique W-part because its W-degree is at most six, whereas two parts require at least eight neighbours. Let \(P_1\) be the other \(K_4\) and \(P_2,P_3\) the two \(K_5\)'s. The W-degrees are
\[
d_W(A\cup B)=6,\quad d_W(X\cup Y)=5,\quad
d_W(C\cup E)=4,\quad d_W(d_0)=4.
\]

### Lemma 3.1: the A/B assignments are disjoint and avoid \(P_0\)

Fix \(a\in A,b\in B\). The triple \(\{d_0,a,b\}\) is independent. For any pair of distinct W-parts outside \(P_0\), if both parts contain a vertex nonadjacent to both \(a,b\), those vertices together with \(d_0,a,b\) form an independent 5-set.

The extra-edge budgets are:
- an A/B vertex assigned to a \(K_4\): at most two edges outside its assigned part;
- an A/B vertex assigned to a \(K_5\): at most one edge outside its assigned part.

If both \(a,b\) are assigned to \(P_0\), their combined extra-edge budget is at most four, insufficient to cover two of \(P_1,P_2,P_3\), which would require at least \(4+5=9\) incidences. If both are assigned to \(P_1\), their budget four is less than five for each of \(P_2,P_3\). If both are assigned to \(P_2\) or both to \(P_3\), their budget two is less than the sizes of both remaining parts outside \(P_0\) and their assigned part. If one is assigned to \(P_0\) and the other to \(P_1\), the remaining \(K_5\) parts each have size five but the budget is at most four. If one is assigned to \(P_0\) and the other to \(P_2\) or \(P_3\), the remaining part sizes are four and five but the budget is at most three. Every case gives common non-neighbours in two distinct parts, contradiction.

Hence no A/B pair can use the same W-part, and neither side can use \(P_0\). Their assigned part supports are disjoint subsets of \(\{P_1,P_2,P_3\}\).

A K4 part can be assigned at most seven vertices from one side, and a K5 part at most six, since the assigned vertices from A (or from B) form a clique. Each of A and B has seven vertices. Therefore one side, say A, is assigned entirely to \(P_1\), while B is assigned to \(P_2,P_3\). Write \(b_i\) for the number of B-vertices assigned to \(P_i\); then
\[
b_2+b_3=7,\qquad 1\le b_2,b_3\le6. \tag{1}
\]

### Lemma 3.2: the C/E vertices are assigned to \(P_0\)

Every vertex of \(C\cup E\) has W-degree four, so it must be complete to a \(K_4\), either \(P_0\) or \(P_1\). Suppose \(c\in C\cup E\) were assigned to \(P_1\). Choose any \(a\in A\), which is also assigned to \(P_1\). The vertices \(d_0,a,c\) are pairwise nonadjacent. The vertex \(c\) has no W-neighbours outside \(P_1\), and \(a\) has only two extra W-edges outside \(P_1\). Since each of \(P_2,P_3\) has five vertices, each contains a vertex nonadjacent to \(a\) and \(c\). Those two vertices together with \(d_0,a,c\) form an independent 5-set. Contradiction.

Therefore all four C/E vertices are complete to \(P_0\), and none is complete to \(P_1\).

### Lemma 3.3: every vertex in \(P_1\cup P_2\cup P_3\) is complete to A or to B

Fix \(w\in P_1\cup P_2\cup P_3\), any \(c\in C\cup E\), and \(a\in A,b\in B\). The vertices \(d_0,c\) are both complete only to \(P_0\), hence are nonadjacent to \(w\); and \(a,b,c,d_0\) are pairwise nonadjacent. If \(w\) missed at least one vertex of A and at least one vertex of B, choosing those two vertices would give the independent 5-set \(\{a,b,c,d_0,w\}\). Thus \(w\) is complete to all of A or all of B.

### Final excess contradiction

Consider \(P_2\). At least one B-vertex is assigned to \(P_3\) by (1). Such a vertex is complete to \(P_3\) and has only one extra edge outside \(P_3\), so it can be adjacent to at most one vertex of \(P_2\). Therefore at most one vertex of \(P_2\) can be complete to all of B. By Lemma 3.3, at least four vertices of \(P_2\) are complete to A. There cannot be five, since \(A\cup P_2\) would be a \(K_{12}\). Thus exactly four vertices of \(P_2\) are A-complete. The same argument applies to \(P_3\).

For each A-complete \(w\in P_i\), \(i\in\{2,3\}\), its U-degree is \(8+\epsilon_w\). It has seven neighbours in A and is adjacent to all \(b_i\) B-vertices assigned to \(P_i\), so
\[
8+\epsilon_w\ge7+b_i
\quad\Longrightarrow\quad
\epsilon_w\ge b_i-1. \tag{2}
\]
There are four such vertices in each \(P_i\). If \(b_i\ge4\), (2) forces at least \(4\cdot3=12\) W-excess units, but the entire W-excess is \(4-\epsilon_U=2\). Hence \(b_2,b_3\le3\), contradicting \(b_2+b_3=7\).

Thus \(\epsilon_U=2\) is excluded.

## 4. Conclusion and scope

Combining this with the \(\epsilon_U=0\) exclusion in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md, the explicit \((5,5,2,1,2)\) \(C_5\)-blow-up local model has **no full 47-core extension for any \(\epsilon_U\in\{0,1,2\}\)**.

This is candidate-specific, not a closure of the general saturated \(\delta=14\) branch. The earlier \(\alpha\)-critical reduction only forces \(J\) to be a 15-vertex, 49-edge, triangle-free, non-bipartite triangle-saturated graph with the witness-induced matching structure; it does not classify every such \(J\) as the explicit blow-up. Other admissible \(J\)'s remain OPEN. The \(\delta\le13\) cases, all five shell templates A–E, and the original \(K_{145}\)-to-T61 bridge also remain OPEN / NOT_CERTIFIED.
