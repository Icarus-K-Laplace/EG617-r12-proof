# E407 Q32: eliminate the last augmentable-edge terminal at \(\delta=14\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61/49-witness contract, the Brouwer/Kang–Pikhurko reduction, and \(\omega(H)\le11\).

This closes the augmentable-edge branch left by DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md. It does not address a \(K_5\)-saturated \(L\) with no augmentable nonedge.

## 1. Frozen terminal contract

Assume the unique terminal from the preceding reduction:
- \(L=\overline{H[U]}\) is non-four-partite with \(e(L)=308\), and an augmentable nonedge \(uv\) gives the balanced Kang–Pikhurko graph \(L'=L+uv\);
- \(P_1,P_2,P_3,P_4\) are the four base parts of \(L'\), each of size seven; \(A\subset P_1\), \(|A|=a\in\{3,4\}\); \(y\in P_2\) and \(x\notin P_1\cup\cdots\cup P_4\) are the KP exceptional vertices;
- the original \(H[U]=\overline L\) is the complement of \(L'\) plus the edge \(uv\), and its only edges between the four \(P_i\) are the \(a\) edges \(yA\) and the one edge \(uv\);
- \(\epsilon_U=1\), \(H[W]=C_0\dot\cup C_1\dot\cup C_2\dot\cup C_3\), where \(C_0\cong K_3\) and \(C_i\cong K_5\) for \(i=1,2,3\), with no edges between components;
- \(x,y\), and an endpoint \(z\in P_1\cup(P_2\setminus\{y\})\) of \(uv\), are complete to \(C_0\), with \(d_H(x,W)=d_H(y,W)=3\) and \(d_H(z,W)=4\);
- the unit of \(U\)-excess lies at \(x\) if \(a=3\), or at \(y\) if \(a=4\). The total excess on \(W\) is three.

For every \(u\in U\), the exact degrees into \(W\) are therefore at most six: \(x,y\) have degree three, \(z\) has degree four, the other \(P_1,P_2\) vertices have degree five (apart from the other endpoint of \(uv\), if it lies there), and \(P_3,P_4\) vertices have degree six (or five at the other endpoint).

## 2. The four common-neighbour sets partition \(U\)

For \(i=0,1,2,3\), let
\[
S_i=\{u\in U:u\text{ is adjacent to every vertex of }C_i\},\qquad n_i=|S_i|.
\]
Every \(u\in U\) belongs to at least one \(S_i\): otherwise choose one non-neighbour of \(u\) from each of the four pairwise anticomplete clique components, obtaining an independent 5-set with \(u\). No \(u\) can belong to two sets, because that would require at least \(3+5=8\) neighbours in \(W\), while \(d_H(u,W)\le6\). Hence
\[
\boxed{n_0+n_1+n_2+n_3=29.} \tag{1}
\]

Write \(E_i=\sum_{w\in C_i}\epsilon_w\), where \(\epsilon_w=d_H(w)-12\). Then \(E_0+E_1+E_2+E_3=3\).

## 3. Common-neighbour capacity for a saturated \(K_5\)

Call \(w\in W\) U-part-saturated if it is complete to one of \(P_1,\ldots,P_4\). Each \(P_j\) is a \(K_7\) in \(H[U]\).

**Lemma 3.1.** If all five vertices of \(C_i\cong K_5\) are U-part-saturated, then
\[
\boxed{n_i\le4+E_i.} \tag{2}
\]

**Proof.** Label each \(w\in C_i\) by a part \(P(w)\) to which it is complete. Since \(d_H(w,U)=8+\epsilon_w\), its number of neighbours outside its label part is exactly \(1+\epsilon_w\), and the total extra-edge load is \(5+E_i\).

No \(u\in S_i\) can have all five labels equal to the part containing \(u\), because that would make \(C_i\cup P_j\) a \(K_{12}\), contrary to \(\omega(H)\le11\). Thus every \(u\in S_i\) consumes at least one extra edge, giving \(n_i\le5+E_i\).

Equality is impossible. If \(n_i=5+E_i\), every common neighbour would consume exactly one extra edge. Therefore four of the five labels must equal the part containing each such vertex, and all of \(S_i\) must lie in the unique part \(P^*\) appearing at least four times; the fifth label belongs to another part. That fifth-labelled vertex would need one extra edge to every vertex of \(S_i\), i.e. \(5+E_i\) extra edges, but it has only \(1+\epsilon_w\le1+E_i\). Contradiction. Since \(n_i\) is integral, \(n_i\le4+E_i\). \(\square\)

## 4. Common-neighbour capacity for \(C_0\cong K_3\)

We have
\[
\boxed{n_0\le10\quad\text{if }E_0\le2,\qquad n_0\le11\quad\text{if }E_0=3.} \tag{3}
\]

If all three vertices of \(C_0\) are U-part-saturated, label them by their complete \(P_j\). Each has \(10+\epsilon_w\) neighbours in \(U\), hence extra load \(3+\epsilon_w\); the total load is \(9+E_0\). If the labels are not all equal, each common neighbour consumes at least one extra edge, so \(n_0\le9+E_0\). If all labels equal \(P_j\), then \(P_j\subseteq S_0\) and every additional common neighbour consumes three extra edges, giving
\[
n_0\le7+\left\lfloor\frac{9+E_0}{3}\right\rfloor.
\]
Combining these bounds with the minimum-degree bound \(n_0\le\min_{w\in C_0}(10+\epsilon_w)\) gives (3).

If a vertex \(w\in C_0\) is not U-part-saturated, then \(w\) is adjacent to \(y\) (since \(y\in S_0\)), so the \(yA\) star cannot block an independent transversal of its four non-neighbour sets in \(P_1,\ldots,P_4\). The only remaining cross-edge \(uv\) would have to block every transversal by itself, forcing singleton non-neighbour sets at its endpoints and at least \(6+6=12\) neighbours in \(U\). Thus \(\epsilon_w\ge2\); because \(E_0\le3\), another \(C_0\)-vertex has excess zero, so \(n_0\le10\). This completes (3).

## 5. Unsaturated \(K_5\)-vertices and their capacity

**Lemma 5.1.** If \(w\in C_i\cong K_5\) is not U-part-saturated, then \(\epsilon_w\ge1\). If \(a=3\), then \(\epsilon_w\ge2\), unless \(\epsilon_w=3\) in the exceptional mixed pattern below.

**Proof.** Let \(A_j=P_j\setminus N_H(w)\), all nonempty. Every tuple in \(A_1\times A_2\times A_3\times A_4\) must contain an edge of \(H[U]\), or it together with \(w\) is an independent 5-set.

The cross-edge set is the star \(yA\) plus the single edge \(uv\). If the star covers every tuple, necessarily \(A_2=\{y\}\) and \(A_1\subseteq A\), so \(N_H(w,U)\) contains
\[
R=(P_1\setminus A)\cup(P_2\setminus\{y\}),\qquad |R|=13-a.
\]
Thus \(d_H(w,U)\ge13-a\), which gives \(\epsilon_w\ge5-a\).

If the star does not cover every tuple, the single edge \(uv\) must cover all tuples not covered by the star. Checking the part-pair of \(uv\):
- for \(uv\) of type \(P_1P_2\), the only mixed pattern below 12 neighbours is \(uv=pq\), with \(p\in A\), \(q\in P_2\setminus\{y\}\), \(A_1=\{p\}\), and \(A_2=\{y,q\}\). It forces at least \(6+5=11\) U-neighbours;
- for any other part-pair, either the edge alone must block all transversals (requiring at least six neighbours in each endpoint part, hence at least 12 total), or the mixed star/edge pattern costs at least 12.
Thus outside the star-only case, \(d_H(w,U)\ge11\); equality can occur only in the displayed \(P_1P_2\) mixed pattern. Since \(d_H(w,U)=8+\epsilon_w\le11\), that pattern has \(d_H(w,U)=11\) and \(\epsilon_w=3\). \(\square\)

**Lemma 5.2.** If \(C_i\cong K_5\) contains an unsaturated vertex, then
\[
\boxed{n_i\le7.} \tag{4}
\]

Indeed, Lemma 5.1 gives that vertex positive excess. Since \(E_i\le3\), at least one other vertex \(w_0\in C_i\) has excess zero and is U-part-saturated. It has exactly seven neighbours in its label part \(P_j\) and one extra neighbour outside. The unsaturated vertex misses at least one vertex of \(P_j\), so
\[
S_i\subseteq N_H(w,U)\cap N_H(w_0,U)
\]
has at most six vertices from \(P_j\) and at most one outside \(P_j\). Thus \(n_i\le7\).

## 6. Exclude every excess allocation

Let \(k\) be the number of \(K_5\) components containing an unsaturated vertex.

### Case I: \(k=0\)

All three \(K_5\) components satisfy Lemma 3.1, so
\[
n_1+n_2+n_3\le12+(E_1+E_2+E_3)=15-E_0.
\]
If \(E_0\le2\), (3) gives \(n_0+n_1+n_2+n_3\le10+15-E_0\le25\). If \(E_0=3\), then all \(E_i=0\) for \(i=1,2,3\), so the total is at most \(11+12=23\). Both contradict (1).

### Case II: \(k=1\), star-only unsaturated vertex

Let \(C_i\) be the unsaturated component. By Lemma 5.1, \(E_i\ge5-a\ge1\), and (4) gives \(n_i\le7\). The other two \(K_5\) components are saturated, so
\[
n_j+n_\ell\le8+E_j+E_\ell=11-E_0-E_i.
\]
Since \(E_0\le2\), (3) gives \(n_0\le10\). Therefore
\[
n_0+n_i+n_j+n_\ell
\le10+7+11-E_0-E_i
\le27,
\]
contradicting (1).

### Case III: the exceptional mixed pattern

The mixed pattern in Lemma 5.1 forces \(E_i=3\), hence \(E_0=E_j=E_\ell=0\). By (3), (4), and Lemma 3.1,
\[
n_0+n_i+n_j+n_\ell\le10+7+4+4=25,
\]
again contradicting (1).

### Case IV: \(k\ge2\)

This is possible only for \(a=4\), and all unsaturated vertices must be star-only; the mixed pattern would consume all three W-excess units. Each such vertex has \(R=(P_1\setminus A)\cup(P_2\setminus\{y\})\) in its U-neighbourhood.

No endpoint of \(uv\) that lies in \(P_1\cup P_2\) can lie in \(R\): such an endpoint has W-degree four, but a vertex of \(R\) adjacent to two different unsaturated \(K_5\) components would have at least two such neighbours plus all three neighbours in \(C_0\). Since the leave has no \(P_3P_4\) edge and \(uv\) is not incident to \(y\), the only remaining type is \(P_1P_3\) or \(P_1P_4\), with the \(P_1\) endpoint in \(A\). Thus \(R\), \(x\), \(y\), and \(z\) are disjoint.

Every vertex of \(R\) has W-degree five and is adjacent to a vertex in each of two distinct \(K_5\) components. It cannot be complete to either such component, nor to a third \(K_5\); by the unique-component property it must be complete to \(C_0\). Therefore \(n_0\ge |R|+3=12\). But two unsaturated components use at least two W-excess units, so \(E_0\le1\), and \(C_0\) has a zero-excess vertex of U-degree ten. Hence \(n_0\le10\), contradiction.

All cases are impossible. Therefore the last augmentable-edge terminal is excluded.

## 7. Conclusion and scope

The entire **augmentable-edge subcase** of the non-four-partite \(\delta=14\) branch is now excluded under the retained contracts. The only remaining \(\delta=14\) non-four-partite possibility is that \(L\) is \(K_5\)-saturated (no nonedge can be added while preserving \(K_5\)-freeness). That saturated branch, \(\delta\le13\), all five shell templates A–E, and the original \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.
