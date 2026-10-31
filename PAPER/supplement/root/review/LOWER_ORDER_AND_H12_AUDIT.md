# Independent lower-order and h12 proof audit

**Audit date:** 2026-11-01  
**Status:** PROVED_CONDITIONAL (first-pass adversarial line audit; no mathematical counterexample found).  
**Scope:** Sections 4 and 7 of the manuscript, including the 23-point triangle-free classification, 35/36/37-point gates, 48-point floor, q20 shell classification, and T61 minimum-degree-12 exclusion.

This is an internal proof audit, not external human peer review or proof-assistant formalization.

## 1. Shortest-odd-cycle bound and R(2,24)

For a shortest odd cycle \(C_{2k+1}\) in a triangle-free non-bipartite graph, it is chordless. The neighbors of any exterior vertex on the cycle form an independent set of the cycle, so there are at most \(k\) such neighbors. Counting cycle edges, attachments, and exterior edges gives
\[
e(L)\leq 2k+1+k(n-2k-1)+\left\lfloor\frac{(n-2k-1)^2}{4}\right\rfloor.
\]
The stated values \(B(18)=73\), \(B(23)=122\), \(B(25)=145\) and the bound \(B(23,k)\leq119\) for \(k\geq3\) were checked arithmetically.

For \(J\in\mathcal R(2,24)\), every nonneighborhood is a clique of size at most11, so \(\delta(J)\geq12\). The hereditary cap \(D(24)=144\) forces 12-regularity. Its complement is 11-regular, triangle-free and non-bipartite. The shortest-odd-cycle degree count gives
\[
2k^2-5k+9\leq0,
\]
which has no real solution. Thus \(\mathcal R(2,24)\) is empty. The 23-vertex lower edge bound 131 follows from the same odd-cycle estimate.

## 2. The 23-vertex triangle-free classification and cost-12 lemma

The \(C_5\) reduction is valid: for \(n=23\), odd girth at least7 gives at most119 edges, so any graph with at least121 edges has a shortest \(C_5\). Removing the cycle leaves 18 vertices and at least80 edges. A non-bipartite triangle-free 18-vertex graph has at most73 edges, so the exterior is bipartite. Its part sizes and possible missing cross-edge cases are exactly \(K_{9,9}\), \(K_{8,10}\), or \(K_{9,9}\) minus one edge.

The five two-neighbor types on \(C_5\) have compatibility graph \(C_5\). The complete-bipartite type constraints yield:
- the \(122\)-edge blow-ups \((10,a,1,1,11-a)\);
- their one-edge deletions at \(121\) edges, except deletion of the edge between the two singleton classes, which violates \(\alpha\leq11\);
- the exceptional \((9,9,2,1,2)\) blow-up.

The one-singleton-neighborhood extension in the \(K_{9,9}\) minus one edge case was checked: the opposite side's one or two types leave a compatible two-neighbor type containing the singleton's existing cycle neighbor. Adding the missing cycle edge preserves triangle-freeness; independence number cannot increase.

For the cost-12 lemma, the three selected 12-sets in a regular blow-up were checked against all five maximal independent class unions. In a one-edge deletion, an independent set not containing both deleted-edge endpoints is still an independent set of the original blow-up; if it contains both endpoints, the common nonneighbor class and the listed \(P\cup\{s,t\}\) cost bounds apply. The exceptional \((9,9,2,1,2)\) case has two 12-sets of internal cost two; one intersects any maximal independent class union in at most two vertices.

## 3. The 35-, 36-, and 37-point minimum-degree gates

For \(J\in\mathcal R(3,35)\), degree at most10 is excluded by \(\mathcal R(2,24)=\varnothing\). In the degree-11 case, the complement neighborhood \(W\) has 23 vertices, is triangle-free, has independence number at most11, and has at least121 edges by \(D(23)=132\). The \(C_5\)-blow-up classification and cost-12 lemma apply. The edge \(xy\) in the remaining 11 vertices exists because otherwise those vertices together with the pivot form a target \(K_{12}\). The common \(L\)-neighborhood \(I\) is independent in \(L[W]\), and the 14-set \(T\cup\{x,y\}\) has at least
\[
66-e(L[T])+12-|T\cap I|\geq72>D(14)=69
\]
target edges. This closes the degree-11 case.

For order36, a degree-12 vertex would lose one neighbor and create a 35-point graph with a degree at most11, impossible. Hence minimum degree13 and edge floor234. For order37, degree at most12 is excluded by \(\mathcal R(2,24)\), and the handshake lower bound241 exceeds \(D(37)=237\).

## 4. The 211-edge floor

If \(J\in\mathcal R(3,35)\), then \(\delta(J)\geq12\), so \(e(J)\geq210\). Equality would make the complement 22-regular and \(K_4\)-free on35 vertices. The Andrásfai–Erdős–Sós threshold for \(r=3\) is \(5n/8\); here \(22>175/8\), so the complement is 3-partite. A part has at least12 vertices and is a target clique, contradiction. Therefore \(e(J)\geq211\).

The numerical threshold and its strict inequality were checked. The exact original AES source should still be included in the final primary-source citation audit.

## 5. The 48-point minimum-degree gate and floor310

For \(J\in\mathcal R(4,48)\), degree at most10 leaves a 37-set in \(\mathcal R(3,37)\), impossible. If degree11, the 36-core has exactly234 edges by the lower bound and \(D(36)=234\); every shell row has size at most3 by \(D(37)=237\). Two nonadjacent shell vertices exist because the shell plus pivot cannot be a \(K_{12}\). Their common antineighborhood in the core has independence at most2, hence size at most23 by \(\mathcal R(2,24)=\varnothing\). Their two rows would therefore have union at least13, but each has size at most3. Thus \(\delta(J)\geq12\).

The 12-shell quantities satisfy \(e(M)\geq11\), \(\alpha(M)\leq10\), \(t_a+t_b\geq12\) on missing edges, and \(t(T)\geq24\) on missing triangles. A triangle costs at least21. In the triangle-free case, a two-matching exists; its four endpoints have \(t(S)\geq24\) and \(e_M(S)\leq4\), giving \(q\geq20\).

At equality, the four-set is \(K_{2,2}\), all eight exterior shell vertices are independent and undecorated, and the no-three-matching argument forces all attachments onto one two-vertex side. The resulting exact forms are \(K_{2,r}\) plus \(10-r\) isolates, \(6\leq r\leq10\), with hub weights10 and decorations \(10-r\), all leaves of row size2, and isolates of row size0.

The inserted-center repivot is valid without any row-disjointness assumption: a leaf pivot removes its two-point core row and inserts both old hubs. Each hub has at most10 neighbors in the old core and at most one new-core neighbor (the other hub), so its new-core degree is at most11. This contradicts the minimum-degree-12 property of the repivoted core. Therefore \(q=20\) is impossible, \(q\geq21\), and
\[
e(J)\geq78+21+211=310.
\]

## 6. T61 h12 branch

For an actual T61 residual \(F\) with \(\delta(F)=12\), the 48-core \(C\) is in \(\mathcal R(4,48)\), so \(e(C)\geq310\). The 12-shell has pair-row union at least12 from \(\mathcal R(3,37)=\varnothing\), and triangle-row union at least25 from \(\mathcal R(2,24)=\varnothing\), because the uncovered core has independence number at most2. Thus \(q\geq20\) and
\[
E=78+q+e(C)\geq408.
\]
At \(E=408\), equality forces q20 and \(e(C)=310\). Repivoting at any leaf yields another genuine 48-core in \(\mathcal R(4,48)\), hence minimum degree12, while an old hub has new-core degree at most11. Contradiction. This excludes the entire h12 branch for \(E\leq408\).

A degree-at-most11 pivot is excluded by the contextual R(4,49) full-color lemma; degree at least14 is excluded by the handshake bound. Thus the T61 minimum-degree split reduces to h13.

## 7. Machine-readable equality families

All five q20 normal forms \(r=6,7,8,9,10\) now have explicit labeled missing-graph adjacency lists in Q20_EQUALITY_ADJACENCY_LISTS.json. VERIFY_Q20_EQUALITY.py checks:
- all 12 shell vertices and the exact \(K_{2,r}\) plus isolates adjacency;
- symmetry, triangle-freeness, independence number10 and matching number2;
- \(e(M)+\sum g=20\), all row sizes and decorations;
- each of the 40 leaf repivot degree upper bounds (10 per case at most; exactly \(\sum r=40\) checks).

These finite checks certify the normal-form data, not the analytic derivation that every equality case must have that form.
