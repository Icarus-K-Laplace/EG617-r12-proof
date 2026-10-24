# Round 2 — Exact \(K=8\) equality layer

## Status

**FULL CLASSIFICATION: OPEN_GAP.**  
**STRENGTHENING \(K\ge10\): NOT PROVED.**

This file records only consequences proved in Round 2. The previously certified theorem \(K\ge8\) remains unchanged. No integer profile or relaxed connector skeleton is presented as a realizable graph.

## 1. Exact support budget

Write \(x_v=d_H(v)-r\). Then \(x_v\in\mathbb Z_{\ge0}\), \(\sum_v x_v=8\), and \(x_{a_i}=0\) for the three anchors. Thus the positive-excess support has size at most eight. Up to order, its possible positive partitions are exactly
\[
\begin{gathered}
8;\ 7+1;\ 6+2;\ 6+1+1;\ 5+3;\ 5+2+1;\ 5+1+1+1;\\
4+4;\ 4+3+1;\ 4+2+2;\ 4+2+1+1;\ 4+1+1+1+1;\\
3+3+2;\ 3+3+1+1;\ 3+2+2+1;\ 3+2+1+1+1;\\
3+1+1+1+1+1;\ 2+2+2+2;\ 2+2+2+1+1;\\
2+2+1+1+1+1;\ 2+1+1+1+1+1+1;\ 1+1+1+1+1+1+1+1.
\end{gathered}
\]
These are only integer partitions. Their realizability is not implied.

For a pair connector \(z\) incident with \(a_i,a_j\), missing \(a_k\), let \(a,b\) be its nonneighbour counts in \(X_i,X_j\), let \(n_k=|N(z)\cap X_k|\), and let \(\gamma_z\) be its number of connector-neighbours. The exact degree equation is
\[
a+b=r-2-d_i-d_j+\gamma_z+n_k-x_z.
\tag{1}
\]
For every exclusive vertex \(v\in X_i\), its baseline external capacity is \(2+d_i\); every distinct forced external neighbour beyond that capacity requires one unit of \(x_v\).

## 2. The \(c=2\), \((0,0,0)\) geometry

Let the triple connectors be \(p,q\), put \(k_p=x_p,k_q=x_q\), \(\varepsilon=\mathbf1_{pq\in E(H)}\), and define \(P=\{x\in X_1\cup X_2\cup X_3:x_x>0\}\) and
\[
E_i=X_i\setminus(N(p)\cup P).
\]
Each vertex in \(E_i\) is exact, misses \(p\), and has cross-\(X\) degree at most two. There is no independent transversal among the \(E_i\), since one together with \(p\) would be an independent four-set.

### Lemma 2.1 — \(c=2\) equality is impossible for \(r\ge13\)

**Proof.** First, no \(E_i\) can be empty when \(r\ge13\). Suppose \(E_1=\varnothing\), let \(A_1=X_1\setminus N(p)\), \(m=|A_1|\ge1\), and \(S=\sum_{x\in A_1}x_x\ge m\). The connector-degree count and the same argument as the audited Empty-Part lemma give
\[
s:=\min(|E_2|,|E_3|)
\ge r-1-m-8+\varepsilon+k_q+S.
\]
For each \(x\in A_1\), the complete-bipartite nonneighbour argument gives \(x_x\ge s-2\). Hence
\[
S\ge m(S+r-3-m-8+\varepsilon+k_q)
\ge m(S+2-m)>S,
\]
where the last strict inequality follows from \(S\ge m\ge1\). Contradiction.

Now all \(E_i\) are nonempty. Counting gives
\[
\sum_i |E_i|\ge 2r-3-K+\varepsilon+k_q
=2r-11+\varepsilon+k_q\ge15.
\]
The degree-two transversal-cover lemma therefore excludes its \((1,3,3)\) and \((2,3,3)\) alternatives. Two parts, say \(E_1,E_2\), must have size at most two. The connector count gives
\[
n_1+n_2\ge 2r-8-(8-k_p-k_q)=2r-16+k_p+k_q,
\]
whereas \(n_1+n_2\le r+k_p-3-\varepsilon\). Thus \(r\le13-k_q-\varepsilon\). This rules out \(r\ge14\).

For \(r=13\), equality is forced throughout: \(k_q=\varepsilon=0\), \(n_3=0\), \(|P|=8-k_p\), all positive exclusive excesses equal one, \(P\cap X_3=\varnothing\), and \(|E_1|=|E_2|=2,\ |E_3|=11\). Every pair between \(E_1,E_2\) must be an edge: a missing pair would have to be covered by adjacency to one endpoint for all eleven vertices of \(E_3\), but each endpoint has cross-degree at most two and can cover at most four such vertices. Hence \(E_1-E_2=K_{2,2}\), saturating the external capacity of each vertex in \(E_1\cup E_2\). Equality in the preceding counts also makes \(P\) disjoint from \(N(p)\).

If \(y\in P\cap X_2\), then \(p,y\) are nonadjacent and every \(e\in E_1\) is nonadjacent to \(y\). Since \(p\) misses all of \(E_3=X_3\), the independent-four condition forces \(y\) to be adjacent to every vertex of \(E_3\), impossible because \(x_y=1\) gives external capacity three. Symmetrically \(P\cap X_1=\varnothing\), so \(k_p=8\) and \(P=\varnothing\).

Finally \(n_1=n_2=9\). The exact connector \(q\) has only ten exclusive neighbours (its degree is thirteen, of which three are anchors), so it cannot cover both nine-vertex sets \(N(p)\cap X_1\), \(N(p)\cap X_2\). Put \(T=E_3\setminus N(q)\), which is nonempty because \(|E_3|=11\) and \(q\) has only ten exclusive neighbours total. For any \(x\in N(p)\cap X_i\) not adjacent to \(q\), the independent-four condition with \(q\), a saturated vertex of the opposite small \(E\)-part, and \(y\in T\) forces \(x\) to be adjacent to every vertex of \(T\). Since \(x\) already uses one external slot on \(p\), it can cover at most one vertex of \(E_3\). If \(|T|\ge2\), this forces \(q\) adjacent to all eighteen vertices in \(N(p)\cap(X_1\cup X_2)\). If \(|T|=1\), the unique vertex of \(T\) is exact, misses \(p,q,E_1,E_2\), and has only two external slots, so at most two of those eighteen vertices can miss \(q\). In either case \(q\) would need at least sixteen exclusive neighbours, a contradiction.Thus \(c=2\) is impossible for \(r=13\) as well. \(\square\)

### Remaining \(c=2,r=12,K=8\) constraints

This is the only unresolved \(c=2\) parameter.

- If all \(E_i\) are nonempty, the exceptional \((1,3,3)/(2,3,3)\) patterns are excluded by \(\sum|E_i|\ge13\). Two parts have size at most two, and the third has size at least nine. Every cross-pair between the two small parts must be an edge: otherwise all vertices of the third part must be adjacent to one of the two endpoints, exceeding their combined cross-degree capacity \(2+2=4\). Since the two small parts have total size at least three, their sizes are \((1,2)\) or \((2,2)\). The \((1,2)\) singleton is saturated; in the \((2,2)\) case all four vertices are saturated.
- If some \(E_i\) is empty, the self-consistency inequality forces \(\varepsilon=k_q=0\). Writing \(m=|X_i\setminus N(p)|\) and \(S\) for its total excess, either \(m=1\), or \(S=m\) and the two other \(E\)-parts both have size exactly three. In the \(m=1\) branch, \(s=S+2\); if both nonneighbour sets of a positive-excess vertex in the other parts are nonempty, then \(s\le4\), while \(s\ge5\) forces that vertex to be complete to one whole \(E\)-part.

These are necessary equality-layer constraints, not a completed contradiction.

## 3. The \(c=3\), \((0,0,1)\) geometry

Both pair connectors focused on \(X_3\) are impossible as in the frozen proof. If both are nonfocused, the two rectangle charges add.

For a nonfocused connector \(v\), with excess \(k\), connector-degree \(\gamma\), opposite-long-block neighbour count \(n_2\), and \(R_{23}\) rectangle, the degree equation and threshold bounds give
\[
k+R_{23}\ge r-8+\gamma.
\]
If \(r\ge13\), the two nonfocused charges already sum to at least \(2(r-8)\ge10\). At \(r=12\), equality \(K=8\) would force each connector to have \(k=4,\gamma=0,(a,b)=(3,2)\), with zero rectangle charge and no other excess. The triple connector \(w\) is nonadjacent to both pair connectors, so it lies in their common-nonneighbour clique. The degree equation makes each pair connector miss the opposite long block. Each three-vertex long-side rectangle set is exact and already uses both external slots on its two short-side rectangle neighbours, so none of those vertices can meet \(w\). But the common-nonneighbour clique requires \(w\) to meet all of them. Contradiction. Thus the both-nonfocused branch has no \(K=8\) equality.

In the mixed-focus branch, if \(s=a+b\ge5\), the sharpened \(R_{22}\) bound gives
\[
k+R_{22}\ge r-6+\gamma+n_2.
\]
If \(s\le4\), the degree equation gives \(k+R_{22}\ge r-7+\gamma+n_2\). Hence the local cost is at least \(r-7\). For \(r\ge16\), this exceeds eight. At \(r=15\), equality \(K=8\) forces \(k=8,\gamma=n_2=0,(a,b)=(2,2)\), with all other excess zero. The focused connector and \(v\) then have at least
\[
|M(u,v)|\ge 2r-5-x_u-k-b=15>r-1=14
\]
common nonneighbours, a forbidden clique. Therefore a \(K=8\) graph in the \(c=3\) geometry, if any, must be in the **mixed-focus branch with \(r\in\{12,13,14\}\)**. Those three boundary layers remain OPEN.

## 4. The \(c=4\), deficits \((0,0,2)\) geometry

Let \(f\) be the number of connectors focused on the short block \(X_3\).

- **\(f=0\):** for \(r\ge14\), the standard pairwise additive lower bounds exceed eight. At \(r=13\), the only way to reach total eight is for both same-group connector pairs to be adjacent and each selected cross-group local cost to equal four. The equality case of the \(R_{24}\) threshold then forces connector excess four on each selected connector, already using all eight units, while the other cross-group rectangle has positive charge; contradiction. At \(r=12\), if neither same-group pair is adjacent, equality forces all four connectors to have excess two, zero connector-degree, and \((a,b)=(4,2)\) rectangles. Same-group supports are disjoint, and cross-group overlap in \(X_3\) is impossible by its capacity four. Thus the four short-block nonneighbour sets partition \(X_3\), and each exact \(X_3\)-vertex would have three connector neighbours plus four forced rectangle neighbours, exceeding capacity. So a remaining \(K=8\) candidate at \(r=12,f=0\) must have at least one same-group connector adjacency. This latter subcase remains OPEN.
- **\(f=1\):** no \(K=8\) equality exists for \(r\ge13\). At \(r=13\), each nonfocused connector costs at least four; if the same-group pair is nonadjacent, all three rectangle charges add, and if adjacent, both members have connector-degree at least one and the sharpened \(R_{23}\) bound makes the pair's safe overlap charge at least six, while a cross-group rectangle adds at least four. For \(r\ge14\), a cross-group pair alone costs at least ten. The \(r=12,f=1\) layer remains OPEN: the original \(K\le6\) closure does not exclude an adjacent same-group overlap with two units of additional budget.
- **\(f=2\):** for \(r\ge15\), the overlap lower bound gives \(K\ge r-6+\max(k_1,k_2)\ge9\). At \(r=14\), equality eight forces \(k_1=k_2=0\), \(\gamma=1\), and identical \(R_{22}\) supports of orientation \((10,1)\) or \((1,10)\), with all excess eight on the singleton vertex. Both orientations are impossible by external-incidence counting: the opposite long block has twelve exact vertices and needs 24 external incidences, but the rectangle vertices and the two focused connectors can supply at most twelve. Therefore only \(r=12,13\), \(f=2\), remain OPEN.

## 5. The \(c=4\), deficits \((0,1,1)\) geometry

Let \(s\) be the number of occupied focus slots. The focus-owner patterns already ruled out in the frozen proof remain over budget for \(K=8\).

- **\(s=0\):** the two \(V,W\) rectangle charges add to at least \(2(r-8)\). At \(r=12\), equality would force both connectors to have excess four, connector-degree zero, and zero-charge \((3,2)\) rectangles. The common-nonneighbour clique of \(V,W\) then forces each short-side rectangle vertex to meet both disjoint opposite-side rectangles, exceeding its external capacity three. For \(r\ge13\), the bound already exceeds eight.
- **\(s=1\):** no \(K=8\) equality exists. If \(V\) owns \(X_3\) at \(r=12\), the \(W\) rectangle costs at least four. If \(U_1,U_2\) are nonadjacent, their same-anchor charges are disjoint and each costs at least three, giving total at least ten. If they are adjacent, their safe overlap charge is at least five: when both connector excesses are at most three, each sharpened local cost is at least five; if one excess is at least four, either the other connector has positive excess (so their connector-excess sum is at least five) or its zero-excess rectangle has charge at least five. Adding \(W\)'s rectangle gives at least nine. If a \(U_i\) owns the slot, the additive \(V,W\) costs already total at least nine. For \(r\ge13\), the additive pair lower bounds exceed eight.
- **\(s=2\):** only the pattern with \(V\) owning \(X_3\) and \(W\) owning \(X_2\) can survive the local lower bounds. The two \(U\)-connectors are adjacent and nonfocused. For \(r\ge15\), the overlap inequality gives \(K\ge r-6+\max(k_1,k_2)\ge9\). At \(r=14\), equality eight forces an identical \((10,1)\) or \((1,10)\) \(R_{22}\) support and all eight units on its singleton; the opposite size-12 block again needs 24 external incidences but can receive at most twenty-two from the rectangle vertices and the two focus connectors. Thus only \(r=12,13\), \(s=2\), the \(V/W\) ownership pattern remain OPEN.

## 6. Current equality-layer verdict

The following is proved:
\[
K=8\quad\Longrightarrow\quad r\le14.
\]
More precisely, any remaining \(K=8\) configuration must belong to one of these strata:

| Geometry | Remaining parameter stratum |
|---|---|
| \(c=2,(0,0,0)\) | \(r=12\), either empty-part exceptional layer or the \((1,2)/(2,2)\) transversal-cover layer |
| \(c=3,(0,0,1)\) | \(r=12,13,14\), exactly one pair connector focused |
| \(c=4,(0,0,2)\) | \(r=12,f=0\) with a same-group adjacency; (r=12,f=1); or (r=12,13,f=2) |
| \(c=4,(0,1,1)\) | \(r=12,13,s=2\), \(V/W\) own the two deficit-one focus slots |

This table is a **necessary-condition classification**, not a classification of realizable graphs. These remaining strata have not been fully eliminated or constructed. Accordingly, the exact \(K=8\) layer is still **OPEN_GAP**, and \(K\ge10\) is not claimed.
