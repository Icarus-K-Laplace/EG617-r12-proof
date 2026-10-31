# h=5, (9,11,11,11) support-orbit resolution

**Status:** PROVED (analytic, conditional only on the stated E286 support reduction, the scalar blocker inequalities, and the T=8 common-neighbor bound).  
**Date:** 2026-10-31.

## Contract

The support multiset is
\[
\{01,01,02,03,23\},
\]
with \(|K_0|=9\) and \(|K_1|=|K_2|=|K_3|=11\). Let \(x,x'\) be the two \(01\) points, \(y_2,y_3\) the \(02,03\) points, and \(w\) the \(23\) point.

The \(23\) point is supported on two \(K_{11}\)s, so the \(f_{11}\) blocker inequality charges at least six units on \(w\) and its missing sets in \(K_2,K_3\). These charged vertices are disjoint from \(K_0,K_1,x,x'\), leaving at most two units of excess on those latter sets. The small-budget double-pair lemma therefore applies to \(x,x'\) on the \(K_9\)-\(K_{11}\) pair \(K_0,K_1\), and forces both \(x,x'\) to complete \(K_0\).

## At most one of \(y_2,y_3\) misses \(K_0\)

For \(i=2,3\), put
\[
A_i=K_0\setminus N(y_i),\qquad
B_i=K_i\setminus N(y_i),\qquad
a_i=|A_i|,\quad b_i=|B_i|.
\]
Here \(b_i\geq1\), since \(K_i\) is a \(K_{11}\), and \(A_i\times B_i\) is complete by the independent-five-set blocker.

For \(v\in K_0\), let \(S(v)=\{i\in\{2,3\}:v\in A_i\}\). The vertex \(v\) has eight neighbors inside \(K_0\), is adjacent to both \(01\) points, is adjacent to \(y_i\) for \(i\notin S(v)\), and is adjacent to every vertex of \(B_i\) for \(i\in S(v)\). Hence
\[
d(v)\geq8+2+(2-|S(v)|)+\sum_{i\in S(v)}b_i
=12+\sum_{i\in S(v)}(b_i-1).
\]
Summing over \(K_0\) gives
\[
\sum_{v\in K_0}\epsilon(v)\geq
a_2(b_2-1)+a_3(b_3-1).
\]
Also \(d(y_i)\geq20-a_i-b_i\), and each vertex of \(B_i\) has at least \(10+a_i\) neighbors. Since \(K_0,\{y_2,y_3\},B_2,B_3\) are disjoint,
\[
T\geq\sum_{i=2}^3g_9(a_i,b_i),
\quad
g_9(a,b)=\max(0,8-a-b)+a(b-1)+b\max(0,a-2).
\]
For all positive \(a,b\), \(g_9(a,b)\geq5\):
- \(a=1\): \(g_9=\max(0,7-b)+(b-1)\geq6\);
- \(a=2\): \(g_9=\max(0,6-b)+2(b-1)\geq5\);
- \(a\geq3,b=1\): \(g_9=\max(0,7-a)+(a-2)\geq5\);
- \(a\geq3,b\geq2\): \(a(b-1)\geq a\) and \(b(a-2)\geq b\), so \(g_9\geq\max(0,8-a-b)+a+b\geq8\).

If both \(A_2,A_3\) were nonempty, \(T\geq10\), contradicting \(T=8\). Thus at most one is nonempty.

## If exactly one misses \(K_0\)

Suppose \(A_2\neq\varnothing\) and \(A_3=\varnothing\), after relabeling. Then \(y_3\) also completes \(K_0\). Thus the two \(01\) points and \(y_3\) are three points completing \(K_0\). For \(y_2\), each vertex of \(A_2\) has eight internal neighbors in \(K_0\), these three completing-point adjacencies, and all \(b_2\) neighbors in \(B_2\). Its excess is therefore at least \(b_2-1\). The same charge \(g_9(a_2,b_2)\geq5\) applies to \(y_2,A_2,B_2\).

This five-unit charge is additive to the six-unit \(23\) blocker. Their only shared clique is \(K_2\): the opposite missing set for \(y_2\) lies in \(K_0\), while the opposite missing set for \(w\) lies in \(K_3\). At a vertex of \(K_2\) missing only one of the two support points, the other support-point adjacency gives degree at least \(11\) plus the corresponding forced-neighbor count. At a vertex missing both, the two forced-neighbor sets are disjoint, and
\[
\max(0,(a-1)+(c-1))
\geq\max(0,a-2)+\max(0,c-2).
\]
Thus the shared-leaf excess is not counted twice. We obtain \(T\geq5+6=11>8\), a contradiction. The case \(A_3\neq\varnothing\) is symmetric.

## If neither misses \(K_0\)

Then all four points \(x,x',y_2,y_3\) complete \(K_0\). The \(23\) blocker leaves at most two excess units on these four points. If any two were nonadjacent, they would have at least nine common neighbors in \(K_0\), and the T=8 common-neighbor bound would force their excess sum to be at least six. Therefore all four points must be pairwise adjacent. Together with \(K_0\), they form a \(K_{13}\), contradicting \(\omega(H)\leq11\).

Thus the support orbit \(\{01,01,02,03,23\}\) is impossible.

## Audit boundary

This note closes only this h=5 support orbit. It does not certify the other support orbits, all scalar/shared-incidence arguments, the lower-order gate, or the full \(K_{145}\) proof.
