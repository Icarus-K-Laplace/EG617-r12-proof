# E407 Q32: exclude every W-extension of the explicit saturated local model

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL for the explicit \((5,5,2,1,2)\) \(C_5\)-blow-up candidate only.** This is not a classification of all admissible saturated local graphs \(J\).

Dependencies: the exact 47-core degree/excess contract; \(\alpha(H)\le4\), \(\omega(H)\le11\); the explicit local model in DELTA14_SATURATED_LOCAL_MODEL.md; Brouwer's second-Turán theorem for the \(W\)-profile classification; and the independent-transversal lemma in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md.

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
Every \(u\in U\) must be complete to at least one clique part of \(H[W]\): otherwise choose one non-neighbour from each of four pairwise-antocomplete clique parts of \(W\), obtaining an independent 5-set together with \(u\).

For any clique part \(P\subseteq W\), write
\[
S_P=\{u\in U:u\text{ is adjacent to every vertex of }P\}.
\]
The clique bound gives
\[
\boxed{|S_P|\le 11-|P|.} \tag{1}
\]
These two observations drive the exclusions below.

## 2. The case \(\epsilon_U=1\) is impossible

The exact \(W\)-edge ledger gives \(e(H[W])=33\). By the retained Brouwer/Turán profile classification, there are only three cases.

### Case 2a: \(H[W]=K_3\dot\cup 3K_5\)

All four parts are pairwise anticomplete. The sets \(S_P\) cover \(U\), so (1) implies
\[
29=|U|\le \sum_P|S_P|
\le (11-3)+3(11-5)=8+18=26,
\]
a contradiction.

### Case 2b: \(H[W]=3K_4\dot\cup K_6\)

Again the four parts are pairwise anticomplete and cover \(U\) by their common-neighbour sets. Therefore
\[
29\le 3(11-4)+(11-6)=21+5=26,
\]
a contradiction.

### Case 2c: \(H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5\) plus one cross-edge

The four clique parts all have size at least four, and there is exactly one edge between two parts. Since \(\epsilon_{d_0}\le\epsilon_U=1\),
\[
|N_W(d_0)|=2+\epsilon_{d_0}\le3.
\]
By the second independent-transversal consequence proved in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md, after deleting any set of at most three vertices, the four parts still admit an independent transversal avoiding the deleted set: a single cross-edge forbids at most \(1/4\), \(1/6\), or \(1/9\) of the candidate transversals according to the distribution of the three deletions. Apply this with \(S=N_W(d_0)\). The resulting independent 4-set \(T\subseteq W\setminus N_W(d_0)\) is anticomplete to \(d_0\), so \(T\cup\{d_0\}\) is an independent 5-set, contradiction.

All three \(\epsilon_U=1\) profiles are excluded. Hence
\[
\boxed{\epsilon_U\ne1.}
\]

## 3. The case \(\epsilon_U=2\) is impossible

Now \(e(H[W])=32\). Turán equality forces
\[
H[W]=P_0\dot\cup P_1\dot\cup P_2\dot\cup P_3
=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5,
\]
with no cross-edges. If \(\epsilon_{d_0}\le1\), then \(d_0\) has at most three neighbours in \(W\), fewer than the size of every part. It is not complete to any part, contradicting the forced complete-to-a-part property. Therefore
\[
\epsilon_{d_0}=2,\qquad d_H(d_0,W)=4.
\]
All other \(U\)-vertices have excess zero, and \(d_0\) is complete to exactly one \(K_4\); call it \(P_0\). Let \(P_1\) be the other \(K_4\), and \(P_2,P_3\) the \(K_5\)'s.

Every \(u\in U\) is complete to a unique part \(Q(u)\): its \(W\)-degree is at most six, while two parts require at least \(4+4=8\) neighbours. The \(W\)-degrees are
\[
d_W(A\cup B)=6,\quad d_W(X\cup Y)=5,\quad
d_W(C\cup E)=4,\quad d_W(d_0)=4.
\]
Consequently, an \(A\)- or \(B\)-vertex assigned to a \(K_4\) has at most two edges outside its assigned part, and if assigned to a \(K_5\) has at most one.

### Lemma 3.1: no \(A\)-vertex and \(B\)-vertex can be assigned to the same part, or can use \(P_0\)

Fix \(a\in A,b\in B\). The three vertices \(d_0,a,b\) are pairwise nonadjacent. Every vertex of \(P_1,P_2,P_3\) is nonadjacent to \(d_0\). If there are two distinct parts among \(P_1,P_2,P_3\) containing a vertex nonadjacent to both \(a\) and \(b\), those two vertices together with \(d_0,a,b\) form an independent 5-set. We show this always happens in the prohibited assignment cases.

- If \(Q(a)=Q(b)=P_0\), their combined number of edges outside \(P_0\) is at most four. To leave common non-neighbours in at most one of \(P_1,P_2,P_3\), their neighbourhoods would have to cover at least two whole parts, requiring at least \(4+5=9\) edge incidences. Impossible.
- If \(Q(a)=Q(b)=P_1\), their combined extra-edge budget is four, less than the size five of each of \(P_2,P_3\). If both are assigned to \(P_2\) or both to \(P_3\), their combined extra-edge budget is two, less than the sizes of both remaining parts outside \(P_0\) and their assigned part. Thus a common non-neighbour exists in each of two parts.
- If \(Q(a)=P_0\) and \(Q(b)=P_1\), their combined extra-edge budget is at most four, less than five for each of \(P_2,P_3\). If \(Q(a)=P_0\) and \(Q(b)\in\{P_2,P_3\}\), the combined budget is at most \(2+1=3\), less than the sizes four and five of the two remaining parts. Again a common non-neighbour exists in two parts. The case with \(a,b\) reversed is symmetric.

Therefore for every \(a\in A,b\in B\), their assigned parts are distinct and neither is \(P_0\). In particular, the sets of parts used by \(A\) and by \(B\) are disjoint subsets of \(\{P_1,P_2,P_3\}\). \(\square\)

### Lemma 3.2: the \(A/B\) assignments saturate one part

By (1), the common-neighbour capacities of \(P_1,P_2,P_3\) are respectively
\[
7,\ 6,\ 6.
\]
Each of \(A,B\) has seven vertices assigned among these parts, and their part supports are disjoint by Lemma 3.1.

Neither side can use only \(P_2,P_3\) unless it uses both, since each has capacity six; two disjoint sides cannot both use the same two parts. If one side uses \(P_1\) and another part, the other side would be confined to the remaining single \(K_5\), whose capacity is only six. Thus exactly one side, say \(A\), uses \(P_1\) alone, and all seven vertices of \(A\) are assigned to \(P_1\). The seven vertices of \(B\) are assigned among \(P_2,P_3\).

### Final capacity contradiction

The four vertices in the \(C,E\) parts of the local blow-up have \(W\)-degree four, so each must be complete to a \(K_4\), namely \(P_0\) or \(P_1\). Since \(P_1\) already has seven common neighbours from \(A\), its capacity is exhausted; all four \(C,E\) vertices must be assigned to \(P_0\). The part \(P_0\) already has the common neighbours \(d_0\) and these four vertices, so its capacity of seven leaves room for at most two \(X,Y\) vertices. Part \(P_1\) has no remaining capacity. Parts \(P_2,P_3\) have combined capacity twelve, of which seven are occupied by \(B\), leaving at most five slots. Therefore the total remaining capacity for the ten \(X,Y\) vertices is at most
\[
2+0+5=7<10,
\]
contradiction. Hence
\[
\boxed{\epsilon_U\ne2.}
\]

## 4. Conclusion and scope

Combining this with the \(\epsilon_U=0\) exclusion in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md, the explicit \((5,5,2,1,2)\) \(C_5\)-blow-up local model has **no full 47-core extension for any admissible \(\epsilon_U\in\{0,1,2\}\)**.

This is a useful candidate-specific exclusion, not a solution of the saturated \(\delta=14\) branch. The earlier \(\alpha\)-critical reduction only forces \(J\) to be a 15-vertex, 49-edge, triangle-free, non-bipartite triangle-saturated graph with the witness-induced matching structure; it does not classify every such \(J\) as the explicit blow-up. Other admissible \(J\)'s remain OPEN. The \(\delta\le13\) cases, all five shell templates A–E, and the original \(K_{145}\)-to-T61 bridge also remain OPEN / NOT_CERTIFIED.
