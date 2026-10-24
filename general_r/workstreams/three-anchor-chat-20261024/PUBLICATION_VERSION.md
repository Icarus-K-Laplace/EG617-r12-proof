# Exact Three-Anchor Excess Theorem — publication version

## Theorem

Let \(r\ge12\). Let \(H\) be a graph on \(3r-1\) vertices satisfying
\[
\alpha(H)\le3,\qquad \omega(H)\le r-1,\qquad \delta(H)\ge r.
\]
Suppose \(a_1,a_2,a_3\) are pairwise nonadjacent vertices of degree exactly \(r\). Then
\[
\boxed{K:=2e(H)-r(3r-1)=\sum_{v\in V(H)}(d_H(v)-r)\ge8.}
\]

### Proof

Write \(e(v)=d_H(v)-r\). By the minimum-degree hypothesis, \(e(v)\ge0\) for every vertex. The integer \(r(3r-1)\) is even, so \(K=2e(H)-r(3r-1)\) is even. It is enough to rule out \(K\le6\), which we assume for contradiction.

## 1. Anchor partition

Every non-anchor vertex is adjacent to at least one of the three anchors; otherwise it and \(a_1,a_2,a_3\) form an independent 4-set.

Let \(X_i\) be the vertices adjacent to exactly \(a_i\). Let \(C\) be the set of vertices adjacent to at least two anchors, put \(c=|C|\), and let \(t\) be the number adjacent to all three anchors. There are \(3r-4\) non-anchor vertices. Counting anchor incidences, with one incidence as a baseline for each non-anchor vertex, gives
\[
3r=(3r-4)+c+t,\qquad c+t=4.
\]

For each \(i\), the set \(X_i\cup\{a_i\}\) is a clique. If two vertices of \(X_i\) were nonadjacent, those vertices together with the two anchors other than \(a_i\) would form an independent 4-set. Therefore \(|X_i|\le r-2\). Define the nonnegative deficits
\[
d_i=r-2-|X_i|.
\]
If \(s_i\) is the number of connectors adjacent to \(a_i\), then \(r=|X_i|+s_i\), so \(s_i=2+d_i\). Summing these incidences gives
\[
6+\sum_i d_i=\sum_i s_i=2c+t=c+4,
\qquad \sum_i d_i=c-2.
\]
Consequently, up to permutation, the only possibilities are
\[
(c;d_1,d_2,d_3)=(2;0,0,0),\ (3;0,0,1),\
(4;0,0,2),\ (4;0,1,1).
\]
If \(q_i\) is the number of connectors missing \(a_i\), then
\[
q_i=c-s_i=c-2-d_i=d_j+d_k.
\]
Thus the connector types are fixed in each of the four cases. This classification is exact and uses no small-\(r\) assumption.

For \(x\in X_i\), the number of neighbors outside \(X_i\cup\{a_i\}\) is exactly
\[
d_H(x)-(|X_i|-1)-1=2+d_i+e(x).
\]
Hence \(2+d_i\) is the baseline external capacity of a vertex of \(X_i\).

## 2. Rectangle and charging lemmas

### Lemma 2.1 (pair-connector rectangle)

Let \(z\) be a pair connector adjacent to \(a_i,a_j\) and missing \(a_k\). Put
\[
A=X_i\setminus N(z),\quad B=X_j\setminus N(z),\quad a=|A|,\quad b=|B|.
\]
Then \(A-B\) is complete bipartite.

**Proof.** If \(x\in A\), \(y\in B\), and \(xy\) were absent, then \(z,a_k,x,y\) would be pairwise nonadjacent: \(z\) misses all three of \(a_k,x,y\), the exclusive-block definitions make \(a_k\) nonadjacent to \(x,y\), and \(xy\) was assumed absent. This contradicts \(\alpha(H)\le3\). ∎

### Lemma 2.2 (rectangle excess charge)

Suppose the effective external capacities on the two blocks are \(p,q\). These are the baseline capacities \(2+d_i,2+d_j\), reduced by any already-known connector neighbors that are complete to the corresponding block. Then
\[
R_{pq}(a,b):=a(b-p)_++b(a-q)_+
\]
is a lower bound on the total excess of the vertices in \(A\cup B\).

**Proof.** Each \(x\in A\) has at least \(b\) external neighbors in \(B\), so \(e(x)\ge(b-p)_+\). Similarly each \(y\in B\) satisfies \(e(y)\ge(a-q)_+\). Summing over the distinct vertices in \(A\) and \(B\) gives the claim. This is a necessary lower bound, not a sufficiency assertion. Counting an edge at both endpoints is legitimate because \(K\) is the sum of the vertex excesses. ∎

The four functions needed below are
\[
\begin{aligned}
R_{22}(a,b)&=a(b-2)_++b(a-2)_+,\\
R_{23}(a,b)&=a(b-2)_++b(a-3)_+,\\
R_{24}(a,b)&=a(b-2)_++b(a-4)_+,\\
R_{33}(a,b)&=a(b-3)_++b(a-3)_+.
\end{aligned}
\]
Their zero sets are respectively \(a,b\le2\); \(a\le3,b\le2\); \(a\le4,b\le2\); and \(a,b\le3\). Indeed, since \(a,b>0\), \(R_{pq}=0\) holds exactly when both positive-part factors vanish, i.e. \(b\le p\) and \(a\le q\).

### Lemma 2.3 (threshold bounds)

For positive integers \(a,b\), writing \(s=a+b\), one has
\[
\begin{array}{ll}
R_{22}\ge s-4,& R_{22}\ge s-3\quad(s\ge5),\\
R_{23}\ge s-5,& R_{23}\ge s-4\quad(s\ge6),\\
R_{24}\ge s-6,& R_{24}\ge s-5\quad(s\ge7),\\
R_{33}\ge s-6,& R_{33}\ge s-4\quad(s\ge7).
\end{array}
\]

**Proof.** For all \(p,q\ge0\), \(R_{pq}(a,b)\ge a+b-p-q\). If neither threshold is exceeded, the right-hand side is nonpositive. If only \(b>p\), then \(R_{pq}=a(b-p)\ge b-p\ge a+b-p-q\) because \(a\le q\); the case only \(a>q\) is symmetric. If both thresholds are exceeded, the two terms are at least \(b-p\) and \(a-q\).

For the sharpened bounds, split by which thresholds are exceeded:
- \(R_{22}\): if \(a\le2<b\), then \(R_{22}=a(b-2)\ge a+b-3\); the symmetric case is identical. If \(a,b\ge3\), then \(R_{22}-(a+b-3)=2ab-3a-3b+3\ge0\), with minimum at \((3,3)\). The region \(a,b\le2\) has \(a+b\le4\), so it is excluded when \(a+b\ge5\).
- \(R_{23}\): if \(a\le3,b\ge3\), then \(R_{23}=a(b-2)\) and \(R_{23}-(a+b-4)=(a-1)(b-3)+1\ge0\). If \(a\ge4,b\le2\), then \(R_{23}=b(a-3)\) and \(R_{23}-(a+b-4)=(b-1)(a-4)\ge0\). If \(a\ge4,b\ge3\), then \(R_{23}-(a+b-4)=2ab-3a-4b+4\ge0\), with minimum at \((4,3)\). The zero-charge region has sum at most five.
- \(R_{24}\): if \(a\le4,b\ge3\), then \(R_{24}=a(b-2)\) and \(R_{24}-(a+b-5)=(a-1)(b-3)+2\ge0\). If \(a\ge5,b\le2\), then \(R_{24}=b(a-4)\) and \(R_{24}-(a+b-5)=(b-1)(a-5)\ge0\). If \(a\ge5,b\ge3\), then \(R_{24}-(a+b-5)=2ab-3a-5b+5\ge0\), with minimum at \((5,3)\). The zero-charge region has sum at most six.
- \(R_{33}\): if \(a\le3,b\ge4\), then \(R_{33}=a(b-3)\) and \(R_{33}-(a+b-4)=(a-1)(b-4)\ge0\); the symmetric case is identical. If \(a,b\ge4\), then \(R_{33}-(a+b-4)=2ab-4a-4b+4\ge0\), with minimum at \((4,4)\). The zero-charge region has sum at most six.

The same case splits, without the one-unit improvement, give the four baseline bounds \(R_{22}\ge a+b-4\), \(R_{23}\ge a+b-5\), \(R_{24}\ge a+b-6\), and \(R_{33}\ge a+b-6\). ∎

### Lemma 2.4 (additivity)

If two rectangles share one exclusive block and their opposite blocks are disjoint, their charges add. For a vertex \(x\) in the shared block, let the forced neighbor sets in the opposite blocks have sizes \(u,v\). These sets are disjoint. If \(p\) is the effective capacity of \(x\), then
\[
e(x)\ge(u+v-p)_+\ge(u-p)_++(v-p)_+.
\]
The second inequality follows by considering whether zero, one, or both of \(u,v\) exceed \(p\). The vertices in the opposite blocks are disjoint, so their endpoint charges also add. The argument applies if the shared block is the \(A\)-side of one rectangle and the \(B\)-side of the other, as long as the same effective capacity for that block is used.

A second additivity rule is available for two nonadjacent pair connectors missing the same anchor. Their nonneighbour supports are disjoint in both incident blocks: otherwise the two connectors, the missed anchor, and a common nonneighbour form an independent 4-set. Their charges therefore add by disjoint support.

If adjacent same-group connectors have overlapping supports, we do not add their rectangle charges. We use only the safe bound \(K\ge k_1+k_2+\max(R_1,R_2)\), where \(k_i\) are their connector excesses.

### Lemma 2.5 (common-nonneighbour clique)

If \(p,q\) are nonadjacent vertices, their common-nonneighbour set is a clique. Otherwise two nonadjacent vertices in that set, together with \(p,q\), form an independent 4-set. In particular, if \(p,q\) have at least \(m\) common neighbors, then
\[
|M(p,q)|\ge (3r-1)-2-\bigl((r+e(p))+(r+e(q))-m\bigr).
\]

## 3. Case \(c=2\): the three equal blocks

Here \(t=2\), both connectors \(p,q\) are triple connectors, and \(|X_i|=r-2\) for every \(i\). Let \(k_p=e(p)\), \(k_q=e(q)\), and \(\varepsilon=\mathbf1_{pq\in E(H)}\). Let \(P\) be the set of positive-excess exclusive vertices, and define
\[
E_i=X_i\setminus(N(p)\cup P).
\]
Each vertex in \(E_i\) is exact and nonadjacent to \(p\), so its cross-\(X\) degree is at most two. There is no independent transversal among the three \(E_i\), since such a transversal together with \(p\) would be an independent 4-set.

### Lemma 3.1 (empty-part self-consistency)

No \(E_i\) is empty.

**Proof.** By symmetry suppose \(E_1=\varnothing\). Since \(p\) cannot be complete to \(X_1\) (otherwise \(X_1\cup\{a_1,p\}\) is an \(r\)-clique), \(A_1=X_1\setminus N(p)\) is nonempty. Because \(E_1\) is empty, every vertex of \(A_1\) has positive excess. Put \(m=|A_1|\ge1\) and \(S=\sum_{x\in A_1}e(x)\ge m\).

Let \(n_i=|N(p)\cap X_i|\). From \(d(p)=r+k_p\),
\[
n_1+n_2+n_3=r+k_p-3-\varepsilon,\qquad
n_2+n_3=m+k_p-\varepsilon-1.
\]
The total exclusive excess is \(K-k_p-k_q\). The number of positive-excess exclusive vertices outside \(A_1\) is at most their total excess, \(K-k_p-k_q-S\). Hence for \(i=2,3\),
\[
|E_i|\ge (r-2)-(n_2+n_3)-(K-k_p-k_q-S)
=r-1-m-K+\varepsilon+k_q+S.
\]
With \(s=\min(|E_2|,|E_3|)\), \(S\ge m\), \(K\le6\), and \(r\ge12\), this yields
\[
s\ge r-1-K+\varepsilon+k_q\ge5.
\]

Fix \(x\in A_1\), and let \(B_i=E_i\setminus N(x)\), \(i=2,3\). The bipartite graph \(B_2-B_3\) is complete, or else \(p,x,y,z\) would be an independent 4-set. If either \(B_i\) is empty, \(x\) has at least \(s\) neighbors in that \(E_i\). If both are nonempty, maximum cross-degree two and completeness force \(|B_2|,|B_3|\le2\), so \(x\) has at least \(2s-4\ge s\) neighbors in \(E_2\cup E_3\). Therefore \(e(x)\ge s-2\).

Summing over \(A_1\) gives
\[
\begin{aligned}
S&\ge m(s-2)\\
&\ge m(r-3-m-K+\varepsilon+k_q+S)\\
&\ge m(S+3-m).
\end{aligned}
\]
The last inequality uses \(r-3-K\ge3\). But
\[
m(S+3-m)-S=(m-1)S+3m-m^2
\ge (m-1)m+3m-m^2=2m>0,
\]
a contradiction. Thus \(E_1\ne\varnothing\), and symmetry proves all three parts nonempty. ∎

### Lemma 3.2 (degree-two transversal cover)

A tripartite graph with nonempty parts, maximum degree at most two, and no independent transversal either has two parts of size at most two, or has part sizes \((1,3,3)\) or \((2,3,3)\), up to permutation.

**Proof.** If fewer than two parts have size at least three, the first alternative holds. Otherwise let \(|E_2|,|E_3|\ge3\). For any \(x\in E_1\), its nonneighbour sets \(B_2\subset E_2,B_3\subset E_3\) are nonempty (otherwise \(x\) has at least three neighbors in a part) and complete bipartite (otherwise an independent transversal exists). Maximum degree two gives \(|B_2|,|B_3|\le2\), while \(d_{\rm cross}(x)\le2\) gives
\[
|E_2|+|E_3|-|B_2|-|B_3|\le2.
\]
Thus \(|E_2|+|E_3|\le6\), so both sizes equal three. The same inequality then forces \(|B_2|=|B_3|=2\). Each vertex of \(B_2\) uses both cross-degree slots on \(B_3\), so has no neighbor in \(E_1\). The unique vertex in \(E_2\setminus B_2\) must be adjacent to every vertex of \(E_1\), forcing \(|E_1|\le2\). ∎

If two parts, say \(E_1,E_2\), have size at most two, then
\[
n_1+n_2\ge2r-8-|P|\ge2r-8-(K-k_p-k_q).
\]
On the other hand \(n_1+n_2\le r+k_p-3-\varepsilon\). Hence \(r\le K+5-k_q-\varepsilon\le11\), impossible. In the exceptional \((1/2,3,3)\) patterns, \(\sum_i|E_i|\le8\), but
\[
\sum_i|E_i|\ge3r-6-(r+k_p-3-\varepsilon)-(K-k_p-k_q)
=2r-3-K+\varepsilon+k_q\ge2r-9\ge15.
\]
Thus \(c=2\) is impossible.

## 4. Case \(c=3\): two long blocks and one short block

The block sizes are \((r-2,r-2,r-3)\). There is one triple connector \(w\), and two pair connectors \(u,v\), both incident with \(X_3\). A pair connector is called focused if it is complete to \(X_3\).

If both are nonfocused, their rectangles share \(X_3\) and have disjoint opposite blocks \(X_1,X_2\), so their charges add. For a nonfocused connector of excess \(k\) and connector-degree \(\gamma\), let \(a,b\ge1\) be its nonneighbour counts in the incident long block and \(X_3\). Its degree equation gives
\[
a+b\ge r-3+\gamma-k.
\]
Its effective capacities are \((2,3)\), so
\[
k+R_{23}(a,b)\ge r-8+\gamma.
\]
The two local costs sum to at least \(2r-16\ge8\), contradiction.

If both are focused, they cannot be adjacent, since \(X_3\cup\{a_3,u,v\}\) is an \(r\)-clique. If nonadjacent, their common-neighbour set contains \(X_3\cup\{a_3\}\), of size \(r-2\). Lemma 2.5 gives
\[
|M(u,v)|\ge2r-5-e(u)-e(v)\ge2r-11>r-1
\]
for \(r\ge12\), again impossible. Thus exactly one, say \(u\), is focused.

For the nonfocused \(v\), every vertex in its \(X_3\)-rectangle already has neighbor \(u\), so the effective capacities are \((2,2)\). If \(k=e(v)\) and \(\gamma\) is its connector-degree, then
\[
a+b\ge r-3+\gamma-k,\qquad
k+R_{22}(a,b)\ge r-7+\gamma.
\]
For \(r\ge14\), this is at least seven. For \(r=13\), if \(\gamma\ge1\) it is at least seven; if \(\gamma=0\) and \(k\le5\), then \(a+b\ge5\) and the sharpened \(R_{22}\) bound again gives at least seven. The only remaining layer is
\[
k=6,\quad \gamma=0,\quad (a,b)=(2,2).
\]
The exact degree equation forces \(v\) to have no neighbor in the opposite long block. All other vertices are exact. The two long-side rectangle vertices use both external slots on the two \(X_3\)-rectangle vertices, and the latter use their three slots on those two vertices and focused connector \(u\). Choose \(x\) in the long-side rectangle and \(y\) in the opposite long block. Then \(v,w,x,y\) can fail to be independent only if \(wy\) is an edge. Thus \(w\) must see all \(r-2=11\) vertices of that block, in addition to its three anchors, impossible for the exact degree-\(13\) vertex \(w\).

It remains to check \(r=12\). The exact degree equation is
\[
a+b=9+\gamma+n_2-k,
\]
where \(n_2\) is the number of neighbors of \(v\) in the opposite long block. The effective capacities are \((2,2)\).

If \(\gamma\ge2\), then \(a+b\ge11+n_2-k\). If \(a+b\ge5\), the sharpened bound gives \(k+R_{22}\ge k+(a+b-3)\ge8+n_2\); if \(a+b\le4\), then \(k\ge7+n_2\), impossible. Thus \(\gamma\le1\).

If \(\gamma=1\), then \(a+b\ge10+n_2-k\). If \(a+b\ge5\), then \(k+R_{22}\ge7+n_2\); otherwise \(k\ge6+n_2\), so the only possible low-budget case is \(k=6,n_2=0,a+b=4\). Since \(R_{22}=0\) is then required, \((a,b)=(2,2)\).

If \(\gamma=0\) and \(n_2\ge1\), then \(a+b\ge10-k\). When \(a+b\ge5\), the local cost is at least \(k+a+b-3\ge7\). When \(a+b\le4\), \(k\ge6\); the only possibility is \(k=6,n_2=1,a+b=4\), and \(R_{22}=0\) forces \((a,b)=(2,2)\). If \(\gamma=0,n_2=0\), then \(a+b=9-k\); direct splitting by \(k=0,\ldots,6\) gives exactly the table below for \(k+R_{22}\le6\):
\[
\begin{array}{c|l}
k&(a,b)\\ \hline
0&(1,8),(8,1)\\
1&(1,7),(7,1)\\
2&(1,6),(6,1)\\
3&(1,5),(5,1)\\
4&(1,4),(2,3),(3,2),(4,1)\\
5&(1,3),(2,2),(3,1)\\
6&(1,2),(2,1).
\end{array}
\]
The sole local-cost-five row is \(k=5,(a,b)=(2,2)\); every other listed row has local cost six. These are all the low-budget signatures.

For the \(\gamma=1\) signature, exactly one of \(uv,vw\) is an edge. A long-side rectangle vertex \(x\) is saturated by its two \(X_3\)-rectangle edges, and has no other external neighbors. If \(vw\) is absent, then for every \(y\in X_2\), the set \(\{v,w,x,y\}\) forces \(wy\); hence \(w\) is complete to \(X_2\), creating the forbidden clique \(X_2\cup\{a_2,w\}\). If \(uv\) is absent, the same argument forces \(u\) complete to \(X_2\), impossible because exact focused \(u\) already has its two anchor neighbors and all nine \(X_3\) neighbors.

For \(\gamma=0,n_2=0\), each local-cost-six row has a saturated rectangle vertex. If \(R_{22}>0\), a positive term in \(R_{22}\) is exactly the excess needed to meet the forced rectangle degree, and all budget is already spent. In the two rows with \(k=6,R_{22}=0\), the rectangle sizes are \((1,2)\) or \((2,1)\); the singleton side has exactly two forced rectangle neighbors, filling its baseline capacity two. In the sole local-cost-five row \((k,a,b)=(5,2,2)\), parity forces \(K=6\), leaving only one excess unit beyond the listed charge, so at least one of the four rectangle vertices remains exact and saturated. A saturated vertex \(s\) is nonadjacent to \(w\) and to every vertex of \(X_2\): on the long side its rectangle neighbors fill its two external slots; on the short side its two rectangle neighbors plus focused connector \(u\) fill its three slots. Since \(v\) is nonadjacent to \(w\) and all of \(X_2\), \(\{v,w,s,y\}\) forces \(w\) adjacent to every \(y\in X_2\), yielding the same forbidden clique.

In the remaining one-neighbor row \(k=6,(a,b)=(2,2),n_2=1\), all other vertices are exact. A long-side rectangle vertex \(x\) is saturated and nonadjacent to \(u\) and all of \(X_2\). For every \(y\in X_2\) other than the single neighbor of \(v\), \(\{v,u,x,y\}\) forces \(uy\). This gives at least nine \(X_2\)-neighbors to exact \(u\), in addition to its two anchors and all nine \(X_3\)-neighbors, impossible. Thus \(c=3\) is closed for all \(r\ge12\).
## 5. Case \(c=4\), deficits \((0,0,2)\)

The block sizes are \((r-2,r-2,r-4)\). All four connectors are pair connectors incident with \(a_3\); two miss \(a_1\) and two miss \(a_2\). A connector is focused if it is complete to \(X_3\).

Two focused connectors cannot be nonadjacent: their common-neighbour set contains \(X_3\cup\{a_3\}\), of size \(r-3\), so
\[
|M(p,q)|\ge2r-6-e(p)-e(q)\ge2r-12>r-1.
\]
Thus focused connectors are pairwise adjacent. Three focused connectors, together with \(X_3\cup\{a_3\}\), would form an \(r\)-clique. Hence the number \(f\) of focused connectors is \(0,1,\) or \(2\).

For a nonfocused connector of excess \(k\) and connector-degree \(\gamma\), its nonneighbour counts \(a,b\ge1\) in its incident long block and \(X_3\) satisfy
\[
a+b\ge r-4+\gamma-k.
\]
With \(f\) focused connectors, its effective capacities are \((2,4-f)\), so
\[
k+R_{2,4-f}(a,b)\ge r-10+\gamma+f. \tag{5.1}
\]

### Case \(f=0\)

If neither same-missing-anchor pair is adjacent, the four charges add by Lemma 2.4 and same-anchor disjointness, giving \(K\ge4(r-10)\ge8\). If exactly one same-group pair is adjacent, take one connector from it and both connectors of the nonadjacent pair; the charges add and give
\[
K\ge(r-9)+2(r-10)=3r-29\ge7.
\]
If both same-group pairs are adjacent, any cross-group pair has additive charge at least \(2(r-9)\). This exceeds six for \(r\ge13\). At \(r=12\), \(K\le6\) forces every connector's local cost to equal three. The threshold equality for \(R_{24}\), under \(\gamma\ge1\) and \(k+R_{24}\le3\), is uniquely
\[
\gamma=1,\quad k=3,\quad (a,b)=(4,2).
\]
All four connectors would then have excess three, already giving \(K\ge12\), contradiction.

### Case \(f=1\)

The three nonfocused connectors have effective \(R_{23}\) charges, each at least \(3+\gamma\) when \(r=12\), by (5.1). One is in the same group as the focused connector and two are in the other group. Cross-group rectangles add, so \(K\le6\) would force all three local costs to equal three and all three connector-degrees to be zero. The two nonfocused connectors in the same group are then nonadjacent, so their supports are disjoint. All three rectangle charges add, giving \(K\ge9\), contradiction. For \(r\ge13\), any cross-group pair already costs at least \(2(r-9)\ge8\).

### Case \(f=2\)

If the two nonfocused connectors belong to different groups, their rectangles add; if they are in the same group but nonadjacent, same-anchor disjointness makes their charges add. In either case (5.1) gives \(K\ge2(r-8)\ge8\). Therefore they must be an adjacent same-group pair. Let their excesses be \(k_1,k_2\), and put \(m=\min(k_1,k_2)\le3\). For the connector with excess \(m\),
\[
a+b\ge r-3-m.
\]
For \(r\ge13\), this sum is at least seven, so \(R_{22}\ge a+b-3\ge r-6-m\). Consequently
\[
K\ge k_1+k_2+R_{22}\ge r-6+\max(k_1,k_2)\ge7.
\]

At \(r=12\), the only possible overlap arithmetic under \(K\le6\) is \(k_1=k_2=0\), both connector-degrees equal one, and each rectangle has \(R_{22}=6\) with orientation \((a,b)=(1,8)\) or \((8,1)\). To see that no positive \(k_i\) survives, if one \(k_i=0\), its sum is at least nine and its \(R_{22}\)-charge is at least six, so any positive excess on the other connector exceeds the budget. If both \(k_i>0\) and both are at most four, then \(R_i\ge6-k_i\), so \(k_1+k_2+\max(R_1,R_2)\ge6+\max(k_1,k_2)>6\). If one \(k_i\ge5\), the other positive connector has excess at most four unless the connector-excess sum already exceeds six; its rectangle charge is at least \(6-k_j\), again making the total exceed six. Thus both excesses are zero. Now \(a_i+b_i\ge8+\gamma_i\). If \(\gamma_i\ge2\), then \(a_i+b_i\ge10\) and \(R_{22}\ge7\), so \(\gamma_i=1\). Each sum is then at least nine, and equality in \(R_{22}\ge6\) leaves only the two stated orientations.

The two rectangles must have identical orientation and support. If their charged singleton vertices differed, six excess units would be required on each. If the orientations differed, the six-unit charges would lie in different blocks and add. If they share the singleton but have different eight-sets, that singleton would need more than its available eight external neighbors. Since the connector excesses and rectangle charge already total six, every other vertex—including both focused connectors—is exact.

For orientation \((1,8)\), let \(x\) be the common singleton in a long block. Its six excess units and eight forced \(X_3\)-neighbors saturate its external capacity, so \(x\) has no other external neighbors. A nonfocused connector \(U\) has no neighbor in the other long block: it has two anchor neighbors, its one connector partner, all but \(x\) in its incident long block, and no neighbors in \(X_3\), totalling degree \(r=12\). A focused connector \(V\) has its two anchor neighbors, all eight \(X_3\)-neighbors, and its focused-partner edge, so it has at most one neighbor in the other long block. Choose \(z\) in that block nonadjacent to \(V\). Then \(U,V,x,z\) are pairwise nonadjacent: saturation gives \(xV,xz\notin E(H)\), the degree count gives \(Uz\notin E(H)\), and the connector-degree condition gives \(UV\notin E(H)\). Contradiction.

For orientation \((8,1)\), let \(y\in X_3\) be the common singleton. It is saturated by its eight rectangle neighbors and the two focused connectors. The nonfocused connector \(U\) has no neighbor in the other long block. For a focused connector \(V\), at least nine vertices of that other long block and at least seven of the eight rectangle vertices are common nonneighbors of \(U,V\); these vertices form a clique by Lemma 2.5. Any of the seven rectangle vertices is exact, already uses one external slot on \(y\), and therefore cannot be adjacent to nine vertices of the other long block. Contradiction. This closes the \((0,0,2)\) geometry for all \(r\ge12\).

## 6. Case \(c=4\), deficits \((0,1,1)\)

The block sizes are \((r-2,r-3,r-3)\). Let \(U_1,U_2\) be the connectors missing \(a_1\), let \(V\) miss \(a_2\), and let \(W\) miss \(a_3\). The connectors \(U_i\) are incident with both \(a_2,a_3\); \(V\) is incident with \(a_1,a_3\); \(W\) is incident with \(a_1,a_2\).

A focus slot \(X_i\), \(i=2,3\), is occupied when a connector incident with \(a_i\) is complete to \(X_i\). No slot can have two owners: if two owners are adjacent, \(X_i\cup\{a_i\}\) together with them is an \(r\)-clique; if they are nonadjacent, their common-neighbour set contains \(X_i\cup\{a_i\}\), and Lemma 2.5 gives
\[
|M(p,q)|\ge2r-5-e(p)-e(q)\ge2r-11>r-1.
\]
Thus there are \(s=0,1,\) or \(2\) occupied slots. A connector not incident with \(a_i\) might in principle also be complete to \(X_i\); such an extra adjacency only consumes more external capacity and strengthens every charge bound below, so it may be ignored in the lower bounds. In an equality case, the saturation argument itself rules out any extra such adjacency.

For \(V\) or \(W\), with no focus neighbor on its deficit-one incident block, the effective \(R_{23}\) cost is at least \(r-8+\gamma\); with that block focused, the effective \(R_{22}\) cost is at least \(r-7+\gamma\). For a nonfocused \(U_i\), zero, one, or two occupied incident slots give respectively
\[
k+R_{33}\ge r-10+\gamma,\quad
k+R_{23}\ge r-9+\gamma,\quad
k+R_{22}\ge r-8+\gamma.
\]
These follow directly from the degree relation \(a+b\ge r-4+\gamma-k\) for \(U_i\), and \(a+b\ge r-3+\gamma-k\) for \(V,W\), together with Lemma 2.3.

### Case \(s=0\)

Both \(V,W\) are nonfocused. Their rectangles share \(X_1\) and have disjoint opposite blocks \(X_2,X_3\), so their charges add. Each costs at least \(r-8\), giving \(K\ge2(r-8)\ge8\).

### Case \(s=1\)

By symmetry suppose \(X_3\) is occupied. If \(V\) owns it, then \(W\) has no focus on \(X_2\) and costs at least \(r-8\), while each \(U_i\) has one occupied incident slot and costs at least \(r-9\). The rectangle of \(W\) and either \(U_i\) share \(X_2\) and have disjoint opposite blocks, so
\[
K\ge(r-8)+(r-9)=2r-17\ge7.
\]
If a \(U_i\) owns \(X_3\), then \(V\) has one focus neighbor on \(X_3\) and costs at least \(r-7\), while \(W\) costs at least \(r-8\). Their rectangles add over shared block \(X_1\), giving \(K\ge2r-15\ge9\). Thus \(s=1\) is impossible.

### Case \(s=2\)

There are four ownership patterns:
1. the same \(U_i\) owns both slots;
2. the two distinct \(U_i\) own the two slots;
3. one \(U_i\) and one of \(V,W\) own the slots;
4. \(V\) owns \(X_3\) and \(W\) owns \(X_2\).

In patterns 1 and 2, both \(V,W\) have a focus neighbor on their deficit-one block, so their additive \(R_{22}\) costs are each at least \(r-7\); the total exceeds six. In pattern 3, the remaining external connector costs at least \(r-7\), and the remaining \(U_i\), with both incident slots occupied, costs at least \(r-8\); their rectangles add and the total exceeds six. Thus only pattern 4 remains.

In pattern 4, both \(U_i\) are nonfocused and have one focus neighbor on each incident block, so their effective capacities are \((2,2)\). If they are nonadjacent, their same-missing-anchor supports are disjoint and their charges sum to at least \(2(r-8)\ge8\). Hence they are adjacent. For each, \(\gamma\ge1\) and
\[
a+b\ge r-3-k.
\]
If \(r\ge13\), choose the smaller excess \(m\le3\). Then \(a+b\ge r-3-m\ge7\), so
\[
K\ge k_1+k_2+R_{22}\ge r-6+\max(k_1,k_2)\ge7.
\]

At \(r=12\), the same overlap analysis as in Section 5 shows that the only possible arithmetic signatures have \(k_1=k_2=0\), connector-degrees one, and identical \((1,8)\) or \((8,1)\) rectangles. Their excesses and the rectangle charge already total six, so every other vertex, including \(V,W\), is exact.

For orientation \((1,8)\), the singleton \(x\in X_2\) is saturated by the focused connector \(W\) and its eight \(X_3\)-rectangle neighbors. The nonfocused \(U_i\) has no \(X_1\)-neighbors by its exact degree count. The focused connector \(V\) has at most one \(X_1\)-neighbor, so choose \(z\in X_1\) nonadjacent to \(V\). Saturation makes \(x\) nonadjacent to \(V,z\); the connector-degree condition makes \(U_i\) nonadjacent to \(V\); and the degree count makes \(U_i\) nonadjacent to \(z\). Together with the defining rectangle nonedge \(U_ix\), the set \(\{U_i,V,x,z\}\) is independent, contradiction.

For orientation \((8,1)\), the singleton \(y\in X_3\) is saturated by the focused connector \(V\) and its eight \(X_2\)-rectangle neighbors. The exact focused connector \(W\) has at most one \(X_1\)-neighbor, so choose \(z\in X_1\) nonadjacent to \(W\). Saturation gives \(yW,yz\notin E(H)\); \(U_i\) has no \(X_1\)-neighbors and is nonadjacent to \(W\); and \(U_i y\notin E(H)\) by the rectangle. Thus \(\{U_i,W,y,z\}\) is an independent 4-set, contradiction.

This closes the \((0,1,1)\) geometry for all \(r\ge12\).

## 7. Conclusion

The four possible anchor geometries have all been excluded under \(K\le6\). Since \(K\) is an even nonnegative integer, it follows that
\[
K=2e(H)-r(3r-1)\ge8.
\]
The theorem is proved for every \(r\ge12\). No external graph theorem and no computation-certified graph enumeration is used.
