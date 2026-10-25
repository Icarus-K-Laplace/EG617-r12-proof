# E407 Q32 — four-partite support-boundary terminal

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL structural reduction; E407 Q32 remains OPEN.**

## 1. Contract

Let H be the 47-vertex target core with
\[
e(H)=284,\qquad \delta(H)\ge12,\qquad \alpha(H)\le4,
\]
so its total degree excess above 12 is 4. Let \(\mathcal Q\) be the 49 selected independent 4-sets supplied by seven exact-129 non-target colors, seven sets per color. Sets in one color are disjoint; sets from distinct colors intersect in at most one vertex. Put \(U=\bigcup\mathcal Q\), \(W=V(H)\setminus U\), and \(|U|=29, |W|=18\). Let
\[
L=\overline{H[U]},\quad
\delta=|E(L)\setminus\bigcup_{Q\in\mathcal Q}\tbinom Q2|,\quad
\epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
The exact ledger is
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta,
\]
with \(\delta+\epsilon_U\le16\). The emergency-sprint transversal/excess theorem strengthens the lower bound to \(\epsilon_U+2\delta\ge9\), hence \(\delta\ge3\).

## 2. The \(\delta=16\) case is automatically four-partite

Since \(e(L)=294+\delta=310\), and \(L\) is \(K_5\)-free by \(\alpha(H)\le4\), Brouwer's second-Turán bound gives at most
\[
t_4(29)-\lfloor29/4\rfloor+1=315-7+1=309
\]
edges for a non-four-partite \(K_5\)-free graph. Thus \(L\) must be four-partite.

Every \(Q\in\mathcal Q\) is a \(K_4\) in \(L\), so it uses one point from each part. Every pair of parts must have at least 49 possible pairs. Since the part sizes sum to 29, the only possible sizes are
\[
|A|=|B|=|C|=7,\qquad |D|=8.
\]
For each pair among \(A,B,C\), the 49 blocks use 49 distinct pairs, so every such pair occurs exactly once. Hence the 91 within-part pairs of \(H[U]\) plus five cross-part pairs give
\[
e(H[U])=\binom72+\binom72+\binom72+\binom82+5=96.
\]
All five cross edges of \(H[U]\) are between \(D\) and \(A\cup B\cup C\).

The ledger forces \(\epsilon_U=0\) and \(e(H[W])=32\). Since \(\alpha(H[W])\le4\), Turán gives \(e(H[W])\ge\binom{18}{2}-t_4(18)=153-121=32\), with equality only at the balanced four-partite complement. Therefore
\[
H[W]=K_5\cup K_5\cup K_4\cup K_4.
\]
All four units of degree excess lie in \(W\). For \(x\in A\cup B\cup C\), if \(t_x=d_{H[U]}(x)-6\), then \(d_H(x,W)=6-t_x\). For \(d\in D\), \(d_H(d,W)=5-t_d\).

## 3. The five cross edges form a matching

Every vertex of \(U\) must be adjacent to all vertices of at least one component of \(H[W]\): otherwise it has a non-neighbour in each of the four clique components, and choosing one from each gives an independent 5-set with that vertex. In particular, every \(x\in U\) has at least four neighbours in \(W\), so \(t_d\le1\) for \(d\in D\).

For each small-part vertex \(x\in A\cup B\cup C\), the 49 blocks contain \(x\) exactly seven times: the pairs with each of the other two small parts are covered exactly once. The seven blocks containing \(x\) use seven distinct \(D\)-partners, because a repeated pair would violate linearity. Since \(|D|=8\), exactly one \(D\)-pair with \(x\) is unused by the witness family. Every cross edge of \(H[U]\) is an unused pair. Thus \(t_x\le1\) as well.

Consequently the five cross edges are a matching between five distinct vertices of \(D\) and five distinct vertices of \(A\cup B\cup C\). Each of those five \(D\)-vertices has exactly four neighbours in \(W\), and its \(W\)-neighbourhood is exactly one of the two \(K_4\) components.

## 4. Every W-vertex is complete to one whole U-part

This reverse saturation is needed before allocating the endpoint split. Fix \(w\in W\), and put \(T=N_H(w)\cap U\). Since a \(K_5\)-component vertex has \(8+\epsilon_w\) neighbours in \(U\), and a \(K_4\)-component vertex has \(9+\epsilon_w\), with total excess four, \(|T|\le13\).

Suppose \(T\) contains no whole part. Then each of \(A'=A\setminus T\), \(B'=B\setminus T\), \(C'=C\setminus T\), \(D'=D\setminus T\) is nonempty. For every \(d\in D'\), every triple \((a,b,c)\in A'\times B'\times C'\) must contain an \(H\)-edge from \(d\) to one of \(a,b,c\); otherwise \(\{a,b,c,d,w\}\) is an independent 5-set. The only cross edges of \(H[U]\) are the five \(D\)-to-small-part edges, and each \(d\) is incident to at most one. Thus at least one of \(A',B',C'\) must be a singleton containing that unique neighbour of \(d\).

There cannot be two singleton sets among \(A',B',C'\): then \(T\) contains six vertices from each of two 7-parts, while the third small part still has a non-neighbour, leaving at least seven vertices in \(D'\). But each \(d\in D'\) would have to use one of the two singleton vertices as its unique cross-edge neighbour, and each small vertex is incident to at most one cross edge. This gives \(|D'|\le2\), contradiction. Three singleton sets would require \(|T|\ge18\), also impossible.

So exactly one of \(A',B',C'\) is a singleton, say \(A'=\{a\}\). Every \(d\in D'\) must be adjacent to \(a\), so \(|D'|\le1\); since \(D'\ne\varnothing\), it is a singleton \(\{d\}\). The size bound \(|T|\le13\) now forces
\[
T=(A\setminus\{a\})\cup(D\setminus\{d\}),\qquad |T|=13,
\]
and \(ad\in E(H)\). Hence \(w\) is a \(K_4\)-component vertex with excess four; all other vertices of \(W\) have excess zero. The four \(D\)-endpoints other than \(d\) are all adjacent to \(w\), so their exact \(W\)-neighbourhood is the \(K_4\)-component containing \(w\). The fifth endpoint \(d\) has the other \(K_4\) as its \(W\)-neighbourhood.

Take another vertex \(w'\) in the same \(K_4\) as \(w\). It is adjacent to those same four \(D\)-endpoints and nonadjacent to \(d\). If \(w'\) had no whole \(U\)-part in its neighbourhood, the argument above would force its neighbourhood to be \((P\setminus\{p\})\cup(D\setminus\{d\})\) for a 7-part \(P\), hence to have 13 \(U\)-neighbours. But \(w'\) has excess zero and therefore exactly nine \(U\)-neighbours. If instead \(w'\) has a whole \(U\)-part, it cannot be \(D\) because \(w'd\notin E(H)\); a small part plus the four \(D\)-endpoints gives at least \(7+4=11\) \(U\)-neighbours, again impossible. Contradiction.

Therefore every \(w\in W\) is adjacent to all vertices of at least one \(U\)-part. Since \(|N_H(w)\cap U|\le13<14\), it is adjacent to all vertices of exactly one part.

## 5. All endpoint splits are impossible

Let \(k\) and \(5-k\) be the numbers of cross-edge \(D\)-endpoints whose exact \(W\)-neighbourhoods are the first and second \(K_4\), respectively. Up to order the possibilities are \((5,0),(4,1),(3,2)\). Every \(w\in W\) is complete to exactly one \(U\)-part by Section 4. A \(K_4\)-vertex has exactly \(9+\epsilon_w\) neighbours in \(U\); a \(K_5\)-vertex has exactly \(8+\epsilon_w\). Also, every \(u\in U\) must be complete to at least one of the four clique components of \(H[W]\), or choosing one non-neighbour from each component would give an independent 5-set.

- **Split \((4,1)\) is impossible.** The \(K_4\) containing four endpoints cannot be complete to \(D\), because the endpoint in the other component is not adjacent to it. Each of its four vertices must therefore be complete to a small part, giving at least \(7+4=11\) neighbours in \(U\). Each needs \(\epsilon_w\ge2\), so the total excess would be at least eight, above four.
- **Split \((3,2)\) is impossible.** Neither \(K_4\) can be complete to \(D\), so every vertex in each is complete to a small part. The component with three endpoints gives each of its four vertices at least \(7+3=10\) neighbours in \(U\), forcing \(\epsilon_w\ge1\) at all four vertices. This uses all four excess units. No non-endpoint \(D\)-vertex can be adjacent to either \(K_4\): adjacency to a vertex of the 3-endpoint component would force at least \(7+3+1=11\) \(U\)-neighbours and hence excess at least two; adjacency to a vertex of the 2-endpoint component would force at least \(7+2+1=10\) \(U\)-neighbours and positive excess, but the budget is already spent. Each non-endpoint \(D\)-vertex has five \(W\)-neighbours, all in the two \(K_5\) components. Since it must be complete to a whole \(W\)-component, it is complete to one of those \(K_5\)'s. Two of the three non-endpoint vertices therefore share a \(K_5\). Every vertex of that \(K_5\) is not complete to \(D\), so it is complete to a small part; together with the two \(D\)-neighbours it has at least nine \(U\)-neighbours. A \(K_5\)-vertex has exactly \(8+\epsilon_w\) \(U\)-neighbours, so each of the five vertices would need positive excess, contradicting the total excess four.
- **Split \((5,0)\) is impossible.** Let \(C_0\) be the \(K_4\) that is the exact \(W\)-neighbourhood of all five \(D\)-endpoints. Every \(w\in C_0\) is adjacent to those five endpoints. If \(w\) were not complete to \(D\), reverse saturation (Section 4) would force it to be complete to a small part \(P\), so it would have at least \(7+5=12\) \(U\)-neighbours. Since \(d_H(w,U)=9+\epsilon_w\), this requires \(\epsilon_w\ge3\). At most one vertex of \(C_0\) can be such an exception; the other three vertices must be complete to \(D\).

  Suppose an exception \(w_0\) exists. If \(\epsilon_{w_0}=3\), its \(U\)-neighbourhood is exactly \(P\) together with the five endpoint vertices, so it is adjacent to none of the three non-endpoint vertices of \(D\). If \(\epsilon_{w_0}=4\), it has only one further \(U\)-neighbour beyond those 12, so it is adjacent to at most one non-endpoint \(D\)-vertex. In either case, at least two non-endpoint vertices \(d\in D\) are adjacent to exactly the other three vertices of \(C_0\). Such a \(d\) has exactly five \(W\)-neighbours (seven neighbours in \(D\), no cross edge in \(H[U]\), and total degree 12): three in \(C_0\) and two outside. It is not complete to \(C_0\), and two neighbours outside cannot make it complete to any other \(W\)-component, each of which has size at least four. This contradicts the requirement that every \(u\in U\) be complete to a whole \(W\)-component. Hence no exception exists: all four vertices of \(C_0\) are complete to \(D\).

  But \(D\) is a clique of size eight in \(H[U]\), \(C_0\) is a clique of size four in \(H[W]\), and all edges between them are present. Thus \(H[D\cup C_0]\cong K_{12}\), contradicting the retained \(\omega(H)\le11\) contract.

## 6. Terminal conclusion for the \(\delta=16\) branch

All three endpoint splits are impossible. Therefore the \(\delta=16\) four-partite support-boundary case is **EXCLUDED** under the frozen E407 Q32 core/witness contract.

This is not a closure of E407 Q32 overall. The remaining boundary cases include \(\delta=15\) four-partite and \(\delta\le14\) (both four-partite and non-four-partite where arithmetically possible). The five shell templates and the upstream \(K_{145}\)-to-T61 bridge remain OPEN.
