# h=4 star-orbit resolution: {01,02,03,123}

**Status:** PROVED (analytic, conditional only on the stated E286 support reduction and T=8 common-neighbor bound).  
**Date:** 2026-10-31.

## Contract

The four support points are \(x_1,x_2,x_3,t\), with supports
\[
\{0,1\},\quad\{0,2\},\quad\{0,3\},\quad\{1,2,3\}.
\]
The private cliques have sizes \(|K_0|=10\) and \(|K_i|=11\) for \(i=1,2,3\). For each pair point define
\[
A_i=K_0\setminus N(x_i),\qquad
B_i=K_i\setminus N(x_i),\qquad
a_i=|A_i|,\quad b_i=|B_i|.
\]
Since \(K_i\) is a \(K_{11}\), \(b_i\geq1\). The independent-five-set blocker gives \(A_i\times B_i\subseteq E(H)\).

## Shared-center excess lemma

For \(v\in K_0\), put \(S(v)=\{i:v\in A_i\}\). The vertex \(v\) has nine neighbors inside \(K_0\). It is adjacent to each \(x_i\) for which \(i\notin S(v)\), and to every vertex of \(B_i\) for each \(i\in S(v)\), by the blocker property. Since the three \(B_i\) lie in distinct leaf cliques,
\[
d(v)\geq9+3-|S(v)|+\sum_{i\in S(v)}b_i
=12+\sum_{i\in S(v)}(b_i-1).
\]
Summing over \(K_0\),
\[
\sum_{v\in K_0}\epsilon(v)\geq\sum_{i=1}^3a_i(b_i-1).
\]
This remains valid when the sets \(A_i\) overlap: the contributions at a shared vertex are added through its single degree lower bound, and the \(B_i\) are in distinct cliques.

For each \(i\), the support point has
\[
d(x_i)\geq(10-a_i)+(11-b_i)=21-a_i-b_i,
\]
and every vertex in \(B_i\) has at least \(10+a_i\) neighbors. The vertex sets \(K_0\), \(\{x_1,x_2,x_3\}\), and \(B_1\cup B_2\cup B_3\) are pairwise disjoint. Hence
\[
T\geq\sum_{i=1}^3g(a_i,b_i),
\]
where
\[
g(a,b)=\max(0,9-a-b)+a(b-1)+b\max(0,a-2).
\]
For \(a\geq1,b\geq1\), \(g(a,b)\geq6\). Indeed:
- \(a=1\): \(g=\max(0,8-b)+(b-1)\geq7\);
- \(a=2\): \(g=\max(0,7-b)+2(b-1)\geq6\);
- \(a\geq3,b=1\): \(g=\max(0,8-a)+(a-2)\geq6\);
- \(a\geq3,b\geq2\): \(a(b-1)\geq a\), \(b(a-2)\geq b\), and therefore \(g\geq\max(0,9-a-b)+a+b\geq9\).

Consequently, each nonempty \(A_i\) costs at least six units of excess. Since \(T=8\), at most one \(A_i\) can be nonempty.

## Finish the orbit

If exactly one \(A_i\) is nonempty, its term \(g(a_i,b_i)\) costs at least six. The other two pair points complete \(K_0\). They must be nonadjacent, since together with \(K_0\) an edge between them would create a \(K_{12}\). Their common neighborhood contains all ten vertices of \(K_0\), so the T=8 common-neighbor bound gives combined excess at least seven. These two support-point charges are disjoint from the six-unit charge on \(K_0\), \(B_i\), and \(x_i\). Thus \(T\geq13\), a contradiction.

If no \(A_i\) is nonempty, all three pair points complete \(K_0\) and are pairwise nonadjacent. Each pair has ten common neighbors, hence each pair of excesses sums to at least seven. Summing the three pair inequalities gives
\[
2\sum_{i=1}^3\epsilon(x_i)\geq21,
\]
so the integer sum is at least eleven, again contradicting \(T=8\).

Thus the support orbit \(\{01,02,03,123\}\) is impossible.

## Audit boundary

This note closes this one h=4 orbit. It does not certify the other support orbits, the other scalar/shared-incidence arguments, the lower-order gate, or the full \(K_{145}\) proof.
