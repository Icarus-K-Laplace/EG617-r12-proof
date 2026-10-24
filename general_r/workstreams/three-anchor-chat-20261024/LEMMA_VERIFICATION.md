# Independent lemma verification

Branch: workstream/general-r-three-anchor-20261024

Scope: independent re-derivation of the anchor partition, rectangle excess bounds, additivity, and the \(c=2\) empty-part argument. ARITHMETIC_AUDIT.py is a secondary finite check of local threshold/equality tables; it is not a graph search and is not used as an all-\(r\) proof.

## 1. Excess and parity

Put \(e(v)=d_H(v)-r\). Since \(\delta(H)\ge r\), every \(e(v)\) is a nonnegative integer. Also
\[
K=\sum_v e(v)=\sum_v d_H(v)-r|V(H)|=2e(H)-r(3r-1).
\]
The product \(r(3r-1)\) is even: it is even if \(r\) is even, and \(3r-1\) is even if \(r\) is odd. Thus \(K\) is even. To prove \(K\ge8\), it is enough to rule out \(K\le6\). In all subsequent budget arguments, every local excess charge is a sum of terms in this same nonnegative global sum.

## 2. Anchor partition, independently derived

Let \(A=\{a_1,a_2,a_3\}\) be pairwise nonadjacent degree-\(r\) vertices. Every vertex outside \(A\) is adjacent to at least one anchor; otherwise it and the three anchors form an independent 4-set.

For each \(i\), let \(X_i\) consist of vertices adjacent to \(a_i\) and to neither other anchor. Let \(C\) be the remaining non-anchor vertices, so every vertex of \(C\) is adjacent to at least two anchors. Write \(c=|C|\), and let \(t\) count the vertices of \(C\) adjacent to all three anchors. There are \(3r-4\) non-anchor vertices. In the sum of anchor degrees, each non-anchor contributes one incidence as a baseline; a pair connector contributes one additional incidence and a triple connector contributes two. Equivalently, the total incidence count is
\[
3r=(3r-4)+c+t.
\]
Therefore \(c+t=4\). Since \(0\le t\le c\), the only possibilities are \((c,t)=(2,2),(3,1),(4,0)\).

Each \(X_i\cup\{a_i\}\) is a clique: if two vertices of \(X_i\) were nonadjacent, together with the other two anchors they would form an independent 4-set. Hence \(|X_i|+1\le r-1\), or \(|X_i|\le r-2\). Define \(d_i=r-2-|X_i|\ge0\).

Let \(s_i\) be the number of connectors adjacent to \(a_i\). The anchor's neighbors are exactly \(X_i\) and those connectors, because the anchors are pairwise nonadjacent and no other non-anchor vertices are adjacent to \(a_i\) outside these two categories. Hence
\[
r=|X_i|+s_i,\qquad s_i=2+d_i.
\]
Counting connector-anchor incidences in two ways gives
\[
\sum_i(2+d_i)=\sum_i s_i=2c+t.
\]
Since \(c+t=4\), this yields \(\sum_i d_i=c-2\). The nonnegative integer partitions of \(c-2\), up to permutation, are exactly:
- \(c=2\): \((d_1,d_2,d_3)=(0,0,0)\);
- \(c=3\): \((0,0,1)\);
- \(c=4\): \((0,0,2)\) or \((0,1,1)\).

If \(q_i\) is the number of connectors missing \(a_i\), then \(q_i=c-s_i=c-2-d_i=d_j+d_k\). This fixes the connector-type multiset in each geometry. No step here uses \(r=12\); the only lower bound on \(r\) used later is in the case analysis.

## 3. Rectangle lemma: edge forcing and the exact charge

Let \(z\) be a pair connector adjacent to \(a_i,a_j\) and missing \(a_k\). Set
\[
A=X_i\setminus N(z),\quad B=X_j\setminus N(z),\quad a=|A|,\ b=|B|.
\]
If \(x\in A\), \(y\in B\), and \(xy\notin E(H)\), then \(z,a_k,x,y\) are pairwise nonadjacent: \(z\) misses \(a_k,x,y\), \(a_k\) misses \(x,y\) because they are exclusive to \(a_i,a_j\), and \(xy\) was assumed absent. This contradicts \(\alpha(H)\le3\). Therefore every edge between \(A\) and \(B\) is forced.

For \(x\in X_i\), the clique \(X_i\cup\{a_i\}\) accounts for \(|X_i|\) neighbors when including the anchor. Consequently the number of neighbors outside \(X_i\cup\{a_i\}\) is exactly
\[
d_H(x)-|X_i|=(r+e(x))-(r-2-d_i)=2+d_i+e(x).
\]
Thus its baseline external capacity is \(p_i=2+d_i\). If a known connector is adjacent to every vertex of \(X_i\), each such focus neighbor consumes one of these external slots at every vertex of \(X_i\); after \(f_i\) such known neighbors, the effective capacity is \(p_i=2+d_i-f_i\). In the applications below this is nonnegative. Any other external neighbors only strengthen the lower bound, so ignoring them is safe.

If the effective capacities on \(X_i,X_j\) are \(p,q\), each \(x\in A\) has at least \(b\) forced external neighbors in \(B\), and hence
\[
e(x)\ge(b-p)_+.
\]
Similarly, every \(y\in B\) satisfies \(e(y)\ge(a-q)_+\). Summing over the distinct vertices in \(A\) and \(B\) gives
\[
\sum_{x\in A\cup B}e(x)\ge a(b-p)_++b(a-q)_+=R_{pq}(a,b).
\]
This is a lower bound, not a sufficiency claim. An edge \(xy\) is allowed to contribute to the degree of both endpoints because \(K=\sum_v e(v)\) is a sum over vertices; the two endpoint terms are distinct. No individual vertex's excess is counted twice in this formula.

The four functions needed below are
\[
\begin{aligned}
R_{22}(a,b)&=a(b-2)_++b(a-2)_+,\\
R_{23}(a,b)&=a(b-2)_++b(a-3)_+,\\
R_{24}(a,b)&=a(b-2)_++b(a-4)_+,\\
R_{33}(a,b)&=a(b-3)_++b(a-3)_+.
\end{aligned}
\]
For positive integers \(a,b\), the zero-charge characterizations are exact:
- \(R_{22}=0\iff a\le2,\ b\le2\);
- \(R_{23}=0\iff a\le3,\ b\le2\);
- \(R_{24}=0\iff a\le4,\ b\le2\);
- \(R_{33}=0\iff a\le3,\ b\le3\).

## 4. Rectangle threshold inequalities

For any \(p,q\ge0\), \(R_{pq}(a,b)\ge a+b-p-q\). If both \(a\le q\) and \(b\le p\), the right side is nonpositive and the claim follows from \(R\ge0\). If only \(b>p\), then \(R\ge a(b-p)\ge b-p\ge a+b-p-q\) because \(a\le q\); the case only \(a>q\) is symmetric. If both thresholds are exceeded, the two terms give at least \((b-p)+(a-q)\).

The sharpened bounds follow by splitting at the two thresholds:
- \(R_{22}\ge a+b-4\) always. If \(a+b\ge5\), the case \(a,b\le2\) is impossible. If \(a\le2<b\), then \(R_{22}=a(b-2)\ge a+b-3\); the symmetric case is identical. If \(a,b\ge3\), then \(R_{22}=2ab-2a-2b\ge a+b-3\).
- \(R_{23}\ge a+b-5\) always. If \(a+b\ge6\), the zero-charge region \(a\le3,b\le2\) is impossible. For \(a\le3,b\ge3\), \(R_{23}=a(b-2)\ge a+b-4\); for \(a\ge4,b\le2\), \(R_{23}=b(a-3)\ge a+b-4\); for \(a\ge4,b\ge3\), direct expansion gives \(R_{23}-(a+b-4)=2ab-3a-4b+4\ge0\), with minimum at \((4,3)\).
- \(R_{24}\ge a+b-6\) always. If \(a+b\ge7\), \(a\le4,b\le2\) is impossible. For \(a\le4,b\ge3\), \(R_{24}=a(b-2)\ge a+b-5\); for \(a\ge5,b\le2\), \(R_{24}=b(a-4)\ge a+b-5\); for \(a\ge5,b\ge3\), \(R_{24}-(a+b-5)=2ab-3a-5b+5\ge0\), with minimum at \((5,3)\).
- \(R_{33}\ge a+b-6\) always. If \(a+b\ge7\), the region \(a,b\le3\) is impossible. For \(a\le3,b\ge4\), \(R_{33}=a(b-3)\ge a+b-4\); the symmetric case is identical. For \(a,b\ge4\), \(R_{33}-(a+b-4)=2ab-4a-4b+4\ge0\), with minimum at \((4,4)\).

The script ARITHMETIC_AUDIT.py checks these eight inequalities for all \(1\le a,b\le100\), and checks the zero-charge characterizations on the same range. The algebraic case splits above, not the finite check, prove the inequalities for all positive integers.

## 5. Additivity of rectangle charges — fully checked

Suppose rectangles \(A_1-B_1\) and \(A_2-B_2\) share one exclusive block and their opposite blocks are disjoint. Their forced-neighbor sets in the shared block are disjoint. For a vertex \(x\) in that shared block, let the two forced-neighbor set sizes be \(u,v\), and let \(p\) be its effective external capacity. Its excess satisfies
\[
e(x)\ge (u+v-p)_+\ge (u-p)_++(v-p)_+.
\]
The last inequality is elementary: if both \(u,v>p\), the left side is \(u+v-p\), which is at least \(u+v-2p\); if at most one exceeds \(p\), the left side is at least that one positive excess; if neither exceeds \(p\), the right side is zero. This also applies when the shared block is the \(A\)-side of one rectangle and the \(B\)-side of the other, provided the same effective capacity for that block is used in both terms.

Vertices in the two opposite blocks are disjoint, so their excess charges do not overlap. Summing the pointwise inequality on the shared block and the disjoint-side charges proves that the two \(R\)-charges add. The same proof works for any finite family of rectangles with a common block and pairwise disjoint opposite blocks.

Separately, if two nonadjacent pair connectors miss the same anchor \(a_k\), their nonneighbour supports are disjoint in each incident block: if \(x\) were a common nonneighbour in an incident \(X_i\), then the two connectors, \(a_k\), and \(x\) would be an independent 4-set. Thus their rectangle charges add by disjoint support, even when their opposite blocks are the same.

These are the only additivity principles used in the geometry closures. Where two adjacent same-group connectors can have overlapping supports, the proof does not add their rectangle charges: it uses the safe bound \(K\ge k_1+k_2+\max(R_1,R_2)\), where \(k_i\) are their connector excesses.

## 6. Empty-Part Self-Consistency Lemma — verified

**Lemma.** Under the exact three-anchor hypotheses, \(r\ge12\), and \(K\le6\), no \(E_i\) is empty in the \(c=2\) geometry.

**Setup.** Here both connectors \(p,q\) are triple connectors and all \(|X_i|=r-2\). Let \(k_p=e(p)\), \(k_q=e(q)\), and \(\varepsilon=\mathbf1_{pq\in E(H)}\). Let \(P\) be the set of positive-excess exclusive vertices, and
\[
E_i=X_i\setminus(N(p)\cup P).
\]
Every vertex of \(E_i\) is exact and nonadjacent to \(p\); its external degree is two, so its cross-\(X\) degree is at most two.

Assume \(E_1=\varnothing\). The set \(A_1=X_1\setminus N(p)\) is nonempty, because otherwise \(p\) is complete to \(X_1\) and \(X_1\cup\{a_1,p\}\) is an \(r\)-clique. Since \(E_1\) is empty, every vertex of \(A_1\) belongs to \(P\), so if \(m=|A_1|\) and \(S=\sum_{x\in A_1}e(x)\), then \(m\ge1\) and \(S\ge m\).

Let \(n_i=|N(p)\cap X_i|\). From \(d(p)=r+k_p\),
\[
n_1+n_2+n_3=r+k_p-3-\varepsilon.
\]
Since \(n_1=r-2-m\), this gives \(n_2+n_3=m+k_p-\varepsilon-1\).

The total excess on exclusive vertices is \(K-k_p-k_q\). The number of positive-excess exclusive vertices outside \(A_1\) is at most their total excess outside \(A_1\), namely \(K-k_p-k_q-S\). Therefore, for \(i=2,3\),
\[
\begin{aligned}
|E_i|
&\ge (r-2)-(n_2+n_3)-(K-k_p-k_q-S)\\
&=r-1-m-K+\varepsilon+k_q+S.
\end{aligned}
\]
Let \(s=\min(|E_2|,|E_3|)\). Using \(S\ge m\), \(K\le6\), and \(r\ge12\),
\[
s\ge r-1-K+\varepsilon+k_q\ge r-7\ge5.
\]

Fix \(x\in A_1\), and put \(B_i=E_i\setminus N(x)\), \(i=2,3\). The bipartite graph between \(B_2,B_3\) is complete: a missing edge \(yz\) would make \(p,x,y,z\) an independent 4-set. Every vertex in \(E_2\cup E_3\) has cross-\(X\) degree at most two. If one \(B_i\) is empty, \(x\) is adjacent to every vertex of that \(E_i\), hence to at least \(s\) vertices of \(E_2\cup E_3\). If both \(B_i\) are nonempty, completeness and maximum cross degree two force \(|B_2|,|B_3|\le2\); hence \(x\) has at least \((|E_2|-2)+(|E_3|-2)\ge2s-4\ge s\) neighbors in their union. In either case \(e(x)\ge s-2\).

Summing over \(A_1\),
\[
S\ge m(s-2)\ge m(r-3-m-K+\varepsilon+k_q+S)\ge m(S+3-m).
\]
The last step uses \(r-3-K\ge3\) and \(\varepsilon,k_q\ge0\). But
\[
m(S+3-m)-S=(m-1)S+3m-m^2
\ge(m-1)m+3m-m^2=2m>0,
\]
contradicting \(S\ge m(S+3-m)\). Thus \(E_1\ne\varnothing\). The argument is symmetric in the three blocks, so every \(E_i\) is nonempty.

**Verdict: VERIFIED.** No hidden \(r=12\) assumption occurs; the exact point used is \(r\ge12\), \(K\le6\).

## 7. Degree-two transversal-cover lemma and its missing details

Let the tripartite graph on nonempty \(E_1,E_2,E_3\) have maximum degree at most two and no independent transversal. If fewer than two parts have size at least three, two parts have size at most two. Otherwise, suppose \(|E_2|,|E_3|\ge3\). For any \(x\in E_1\), its nonneighbour sets \(B_2\subseteq E_2,B_3\subseteq E_3\) are nonempty (otherwise \(x\) has at least three cross-neighbors in one part) and form a complete bipartite graph (otherwise an independent transversal exists). Maximum degree two gives \(|B_2|,|B_3|\le2\), while \(d_{\rm cross}(x)\le2\) gives
\[
|E_2|+|E_3|-|B_2|-|B_3|\le2.
\]
Thus \(|E_2|+|E_3|\le6\), so both sizes equal three. The same inequality then forces \(|B_2|=|B_3|=2\). The two vertices of \(B_2\) each use both cross-degree slots on \(B_3\), so they have no neighbors in \(E_1\). The unique vertex in \(E_2\setminus B_2\) must therefore be adjacent to every vertex of \(E_1\), forcing \(|E_1|\le2\). Thus the only exceptional size patterns are \((1,3,3)\) and \((2,3,3)\).

If two parts, say \(E_1,E_2\), have size at most two, then
\[
|X_i|=r-2\le |E_i|+n_i+|P\cap X_i|
\]
implies
\[
n_1+n_2\ge2r-8-|P|\ge2r-8-(K-k_p-k_q).
\]
But \(n_1+n_2\le n_1+n_2+n_3=r+k_p-3-\varepsilon\). Hence \(r\le K+5-k_q-\varepsilon\le K+5\le11\), a contradiction. In the exceptional \((1/2,3,3)\) patterns, \(\sum_i|E_i|\le8\), whereas direct counting gives
\[
\sum_i|E_i|\ge 3r-6-(r+k_p-3-\varepsilon)-(K-k_p-k_q)
=2r-3-K+\varepsilon+k_q\ge2r-9\ge15.
\]
This closes \(c=2\) without the unexplained connector-budget step in the earlier short proof.

## 8. Boundary arithmetic cross-checks

The script ARITHMETIC_AUDIT.py independently enumerates the exact local degree equations and \(K\le6\) relaxations for the delicate \(r=12,13\) cases:
- \(c=3,r=12\): the only local low-budget signatures are the 19 rows printed by the script; the only local-cost-five signature is \((k,\gamma,a,b,n_2)=(5,0,2,2,0)\), and the only one-neighbor exception is \((6,0,2,2,1)\).
- \(c=3,r=13\): the only mixed-focus low-budget signature is \((k,\gamma,a,b,n_2)=(6,0,2,2,0)\).
- \(c=4,(0,0,2),r=12\): the only adjacent-connector local equality with \(\gamma\ge1\) and \(k+R_{24}\le3\) is \((k,\gamma,a,b)=(3,1,4,2)\).
- \(c=4,r=12\): the only arithmetic overlap relaxations have \(k_1=k_2=0\), \(\gamma_1=\gamma_2=1\), and each rectangle oriented \((1,8)\) or \((8,1)\). Mixed orientations are not actual \(K=6\) configurations: their six-unit charges lie on distinct vertices and add to at least twelve. If the orientation is the same but the charged singleton differs, the same contradiction applies; if the singleton is shared but the eight-set differs, that singleton would need more than its available external eight slots. Thus the two rectangles must have identical orientation and support.
- The \(r=13\) c=4 overlap inequalities give a strict \(K\ge7\) lower bound, so no boundary row remains.

These finite checks support the case audit; they do not replace the displayed algebraic inequalities or the structural contradictions.

## 9. Scope limitation

No full graph-level SAT/ILP search on \(3r-1\) vertices was run. No Z3, OR-Tools, or PySAT backend was installed in the execution environment, and a direct encoding of all independent 4-set and \(K_r\)-avoidance constraints is far larger than the local arithmetic search. No claim of exhaustive graph search or computation-certified theorem is made. The analytic proof is the certification basis.
