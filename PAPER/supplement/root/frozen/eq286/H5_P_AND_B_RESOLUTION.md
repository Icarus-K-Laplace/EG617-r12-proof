# h=5 patterns P and B: disjoint blocker and small-budget proofs

**Status:** PROVED_CONDITIONAL (analytic, conditional only on the E286 support reduction, scalar blocker inequalities, shared-leaf accounting, and the T=8 common-neighborhood bound).  
**Date:** 2026-11-01.

## Pattern P: \(\{01,02,02,13,13\}\)

The clique sizes are \(10,10,11,11\). Let \(x,x'\) be the two points supported on \(02\), and \(y,y'\) the two points supported on \(13\).

First, each doubled pair has a noncompleting point. If both \(x,x'\) completed \(K_0\), they would be nonadjacent and have all ten vertices of \(K_0\) as common neighbors, forcing \(\epsilon(x)+\epsilon(x')\geq7\). The other doubled pair costs at least four if it has a noncompleting point (by \(f_{10,11}\geq4\)), and at least seven if both points complete \(K_1\). These charges are disjoint, so the total would exceed eight. The same argument applies with the pairs reversed.

Choose one noncompleting point \(x\) from the \(02\) pair and one noncompleting point \(y\) from the \(13\) pair. Their blocker charges are disjoint: the first uses only \(x\), \(K_0\), and \(K_2\); the second uses only \(y\), \(K_1\), and \(K_3\). Each costs at least four, so
\[
T\geq f_{10,11}(a_x,b_x)+f_{10,11}(a_y,b_y)\geq8.
\]
Since \(T=8\), equality holds in both scalar inequalities. Thus
\[
(a_x,b_x)=(a_y,b_y)=(2,3),
\]
and all excess is concentrated on the two selected support points: every vertex of their missing sets and both companions have zero excess.

The companion \(x'\) must complete \(K_0\). It cannot complete \(K_2\), which is a \(K_{11}\); if it also failed to complete \(K_0\), its own \(f_{10,11}\) blocker would require at least four excess units, but all excess has already been used by \(x,y\). Now any vertex \(v\) in the two-vertex missing set \(A_x\subset K_0\) has nine neighbors inside \(K_0\), all three vertices of \(B_x\subset K_2\) as neighbors by the blocker property, and \(x'\) as a neighbor because \(x'\) completes \(K_0\). Hence \(d(v)\geq9+3+1=13\), contradicting \(\epsilon(v)=0\). Pattern P is impossible.

## Pattern B: \(\{01,01,02,13,23\}\)

The \(23\) point is supported on two \(K_{11}\)s, so its \(f_{11}\) blocker costs at least six. The remaining total excess on \(K_0,K_1\) and the two \(01\) points is at most two. The small-budget double-pair lemma therefore forces the two \(01\) points to complete opposite \(K_{10}\)s; call the point completing \(K_0\) by \(z_0\).

Let \(x\) be the \(02\) point. Its missing set \(B_2\) in \(K_2\) is nonempty, since \(K_2\) is a \(K_{11}\). There are two cases.

- If \(x\) does not complete \(K_0\), its missing sets \(A_0\subset K_0\) and \(B_2\subset K_2\) are both nonempty. The point \(z_0\) is an additional \(K_0\)-completer, so the mixed-diamond inequality charges at least five on \(x,A_0,B_2\). This charge adds to the six-unit \(23\) blocker by shared-leaf accounting on \(K_2\): the opposite missing sets lie in the distinct cliques \(K_0\) and \(K_3\), and the pointwise inequality prevents double-counting vertices in the shared leaf.
- If \(x\) completes \(K_0\), then \(x,z_0\) are two distinct \(K_0\)-completers. They are nonadjacent, since an edge between them together with \(K_0\) would form a \(K_{12}\). Their common neighborhood contains all ten vertices of \(K_0\), so \(\epsilon(x)+\epsilon(z_0)\geq7\). This is disjoint from the six-unit \(23\) blocker.

Either case forces \(T\geq11>8\). Pattern B is impossible.

## Audit boundary

These arguments close only patterns P and B. They use the separately stated small-budget double-pair lemma, scalar blocker minima, and shared-leaf accounting; they do not replace the remaining proof audits for the other support orbits or the lower-order gates.
