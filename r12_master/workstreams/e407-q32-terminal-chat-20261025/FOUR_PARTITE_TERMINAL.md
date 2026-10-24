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

## 4. Only one endpoint split survives

Let \(k\) and \(5-k\) be the numbers of cross-edge \(D\)-endpoints whose \(W\)-neighbourhoods are the first and second \(K_4\), respectively. Up to order the possibilities are \((5,0),(4,1),(3,2)\).

- **Split \((4,1)\) is impossible.** The \(K_4\) containing four endpoints cannot be complete to \(D\), because the endpoint in the other component has no neighbours there. Each of its four vertices must instead be complete to a small part, and therefore has at least \(7+4=11\) neighbours in \(U\). A \(K_4\)-vertex has \(9+\epsilon_w\) neighbours in \(U\), so each needs \(\epsilon_w\ge2\), costing at least eight excess units, but the whole core has only four.
- **Split \((3,2)\) is impossible.** Neither \(K_4\) can be complete to \(D\), so each of its vertices must be complete to a small part. The component with three endpoints forces \(\epsilon_w\ge1\) for each of its four vertices, using all four excess units. Its vertices have exactly \(D_3\cup P_w\) as their \(U\)-neighbourhood, where \(D_3\) is the set of three endpoints and \(P_w\) is one small part. The other \(K_4\) vertices have exactly \(D_2\cup P'_w\) as their \(U\)-neighbourhood. Hence none of the three non-endpoint vertices of \(D\) is adjacent to either \(K_4\). Each such vertex has five neighbours in \(W\), so it must be complete to a \(K_5\) component. By pigeonhole, at least two of the three are complete to the same \(K_5\). Every vertex of that \(K_5\) must also be complete to a small part of size seven, giving at least nine \(U\)-neighbours, but its degree into \(U\) is exactly eight because all excess is already spent. Contradiction.
- **Therefore the split is \((5,0)\).** All five \(D\)-endpoints have the same \(K_4\) as their \(W\)-neighbourhood. That \(K_4\) cannot be complete to a small part: its four vertices would each need \(7+5=12\) \(U\)-neighbours, requiring at least three excess units apiece. It must be complete to \(D\). The remaining \(K_4\) and the two \(K_5\) components cannot be complete to \(D\), and each must be complete to a small part. These three components must use three distinct small parts, because a small-part vertex has at most six neighbours in \(W\).

## 5. Exact surviving \(\delta=16\) kernel

Any E407 Q32 completion with \(\delta=16\) must satisfy all of the following:

1. \(L\) is four-partite on parts \(7,7,7,8\), and the 49 witness blocks cover every pair between the three 7-parts exactly once.
2. \(H[U]\) has the 91 within-part edges plus a matching of five cross edges from \(D\) to the three 7-parts.
3. \(H[W]=K_5\cup K_5\cup K_4\cup K_4\), with all four excess units in \(W\).
4. The five cross-edge endpoints in \(D\) all have the same \(K_4\) as their exact \(W\)-neighbourhood; this \(K_4\) is complete to \(D\).
5. The other three \(W\)-components are each complete, vertex-by-vertex, to small parts; their small-part labels need not be assumed constant within a component without an additional proof.

This is a structural reduction, **not** a contradiction. The five V12 shell templates still need to be checked against the resulting labelled incidence design and the hub-neighbourhood requirements. In particular, no claim is made that the residual design is realizable, nor that it is impossible.
