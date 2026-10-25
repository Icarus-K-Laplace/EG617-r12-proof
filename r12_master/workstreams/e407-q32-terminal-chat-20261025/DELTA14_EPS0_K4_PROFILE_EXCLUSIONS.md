# E407 Q32: two \(\delta=14,\epsilon_U=0\) four-partite W-profiles are impossible

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained 49-witness/core contract and the stated second-Turán W-profile classification.

## 1. Contract and exact \(\delta=14\) ledger

Let \(H\) be the 47-vertex core, with
\[
e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{v\in H}(d_H(v)-12)=4.
\]
Assume the 49-block support boundary \(|U|=29, |W|=18\), and let
\(L=\overline{H[U]}\) be four-partite with parts \(A,B,C,D\) of sizes
\((7,7,7,8)\). Here \(\delta=e(L)-294=14\), so
\[
e(H[U])=98,\qquad e(H[U]\text{ within parts})=91.
\]
Thus exactly seven edges of \(H[U]\) go between \(D\) and \(A\cup B\cup C\).
Every small-part vertex has exactly one unused \(D\)-partner among the eight
possible partners, so these seven cross-edges have seven distinct small-side
endpoints. For \(d\in D\), put
\[
t_d=|N_H(d)\cap(A\cup B\cup C)|.
\]
Then \(\sum_D t_d=7\) and \(t_d\le3\).

Write \(\epsilon_v=d_H(v)-12\) and
\(\epsilon_U=\sum_{u\in U}\epsilon_u\). In this file \(\epsilon_U=0\), so
all degree excess four lies in \(W\). Hence \(\epsilon_w\le4\) for \(w\in W\),
and
\[
d_H(d,W)=5-t_d\qquad(d\in D).
\]

## 2. A non-part-saturation lemma

For \(w\in W\), let \(D'=\{d\in D:wd\notin E(H)\}\). Let
\(A',B',C'\) be the non-neighbour sets of \(w\) in the three small parts.
If \(w\) is not complete to any of \(A,B,C,D\), all four sets are nonempty.
For each \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain
an \(H[U]\)-edge to \(d\), or that triple together with \(d,w\) would be an
independent 5-set. Therefore at least one of \(A',B',C'\) is contained in
\(N_H(d)\cap(A\cup B\cup C)\), and has size at most \(t_d\le3\).

Distinct vertices of \(D'\) must be assigned distinct small parts: a small
vertex has at most one cross-edge in \(H[U]\). Thus \(|D'|\le3\). If
\(|D'|\ge2\), the total number of non-neighbours of \(w\) in \(U\) is at most
\[
2+3+3+7=15,
\]
or at most \(3+3+3+3=12\) if \(|D'|=3\). In either case
\[
d_H(w,U)\ge14. \tag{1}
\]
Consequently, if \(w\) lies in a \(K_4\) component of \(H[W]\) and has at
least two non-neighbours in \(D\), it must be complete to a whole \(U\)-part:
indeed \(d_H(w,U)\le12-3+\epsilon_w=9+\epsilon_w\le13\).
Since it is not complete to \(D\), it must be complete to one of \(A,B,C\).

We also use the one-missing-\(D\)-vertex version. If \(|D'|=1\), with
\(D'=\{d\}\), the same transversal argument gives
\[
d_H(w,U)\ge14-t_d. \tag{2}
\]
Indeed, one small-part non-neighbour set has size at most \(t_d\), and the
other two have size at most seven.

## 3. W-profile \((4,4,5,5)\) with two cross-edges: excluded

Assume
\[
H[W]=K_4\cup K_4\cup K_5\cup K_5
\]
plus two edges between distinct clique parts.

Because \(\epsilon_U=0\), \(d_H(d,W)=5-t_d\). A \(D\)-vertex with \(t_d\ge2\)
would have at most three \(W\)-neighbours. Such a vertex cannot block every
independent transversal of the four clique parts: two cross-edges can do so
only with at least five \(W\)-neighbours (the only minimum case is a \(2+3\)
neighbour split across two \(K_4\)'s). Thus \(t_d\le1\) for all \(d\). Since
\(\sum_D t_d=7\), exactly seven vertices of \(D\) have \(t_d=1\), and one
has \(t_d=0\).

Each of the seven \(t_d=1\) vertices has exactly four \(W\)-neighbours.
A degree-four vertex must be complete to a whole \(W\)-clique part, and
therefore its \(W\)-neighbourhood is exactly one of the two \(K_4\)'s. Let
\(n_1,n_2\) count these seven labelled \(D\)-vertices in the two \(K_4\)
neighbourhood classes, so \(n_1+n_2=7\).

- If \(n_1,n_2\ge2\), one class has \(k=\max(n_1,n_2)\ge4\). Every vertex
  \(w\) of that \(K_4\) has at least two \(D\)-non-neighbours. By (1), it is
  complete to a small \(U\)-part. It also has at least \(k\) neighbours in
  \(D\), so
  \[
  9+\epsilon_w\ge d_H(w,U)\ge7+k,
  \qquad \epsilon_w\ge k-2\ge2.
  \]
  All four vertices of this \(K_4\) would consume at least eight excess
  units, exceeding the total four.

- If the split is \(6+1\), consider the \(K_4\) receiving six \(D\)-vertices.
  Every one of its vertices has at least six \(D\)-neighbours and misses the
  exact-neighbourhood \(D\)-vertex in the other \(K_4\). If it has at least
  two \(D\)-non-neighbours, (1) forces a whole small-part neighbourhood and
  hence \(\epsilon_w\ge4\). If its only \(D\)-non-neighbour is the outside
  endpoint, then (2), with \(t_d=1\), gives \(d_H(w,U)\ge13\), again forcing
  \(\epsilon_w\ge4\). Thus all four vertices require at least four excess
  units each, impossible.

- If the split is \(7+0\), all seven \(t_d=1\) vertices have the same \(K_4\)
  as their exact \(W\)-neighbourhood. If the remaining \(t_d=0\) vertex is
  adjacent to all four vertices of that \(K_4\), the core contains a
  \(K_{8+4}=K_{12}\), forbidden by \(\omega(H)\le11\). Otherwise choose a
  vertex \(w\) of that \(K_4\) not adjacent to the \(t_d=0\) vertex. This
  vertex has seven \(D\)-neighbours and a \(D\)-non-neighbour with no
  small-part cross-edges. It cannot be a no-whole-part exception, and a whole
  small part would give at least \(7+7=14\) neighbours in \(U\), contradicting
  \(d_H(w,U)\le13\).

All endpoint splits are impossible. Hence this W-profile is excluded.

## 4. W-profile \((4,4,4,6)\) with one cross-edge: excluded

Assume
\[
H[W]=K_4\cup K_4\cup K_4\cup K_6
\]
plus one edge between two clique parts. As above, \(t_d\le1\), so seven
vertices of \(D\) have \(t_d=1\), each with exact \(W\)-neighbourhood one
of the three \(K_4\) parts; the eighth has \(t_d=0\) and five \(W\)-neighbours.

Let \(n_1+n_2+n_3=7\) be the endpoint counts in the three \(K_4\) parts.

- If the maximum endpoint load is \(k=4\) or \(5\), at least two exact-neighbourhood \(D\)-vertices lie outside that \(K_4\). By (1), every vertex of the loaded \(K_4\) is complete to a small \(U\)-part and requires \(\epsilon_w\ge k-2\); the four vertices therefore consume at least eight excess units.

- If \(k=6\), the one exact-neighbourhood endpoint outside the loaded \(K_4\) has \(t_d=1\). For each \(w\) in the loaded component, either \(D'\) has at least two vertices, forcing a small-part neighbourhood, or \(D'\) is that single \(t_d=1\) vertex, in which case (2) gives \(d_H(w,U)\ge13\). Either way \(\epsilon_w\ge4\), impossible for all four vertices.

- If \(k=7\), the remaining \(t_d=0\) vertex has five \(W\)-neighbours. With one \(W\)-cross-edge it must be complete to a \(K_4\) plus one extra neighbour. If that \(K_4\) is the loaded component, \(D\) and the component form a forbidden \(K_{12}\). Otherwise at least one vertex of the loaded component misses the \(t_d=0\) vertex; it then cannot be a no-whole-part exception and would need seven \(D\)-neighbours plus a whole small part, giving at least 14 \(U\)-neighbours, impossible.

- Otherwise the only profile is \((3,2,2)\), up to permutation. In the \(K_4\) receiving three endpoints, every vertex has at least four \(D\)-non-neighbours and must be complete to a small \(U\)-part. It has three \(D\)-neighbours, so \(\epsilon_w\ge1\). The four vertices use all four excess units. For a vertex in either other \(K_4\), the two endpoint neighbours and zero excess imply \(d_H(w,U)=9\), so it cannot be incident to the extra \(W\)-edge: otherwise its \(U\)-degree would be eight, too small for a whole small part plus its two \(D\)-neighbours. Likewise the high-load \(K_4\) cannot contain an endpoint of that edge: the endpoint would require \(\epsilon_w\ge2\), while the other three vertices require at least one each, for a total of at least five excess units. Thus no endpoint of the unique cross-edge can lie in any \(K_4\) part. But every cross-edge between the four clique parts must meet a \(K_4\) part, since there is only one \(K_6\) part. Contradiction.

Therefore this W-profile is also excluded.

## 5. Scope

This closes two \(\delta=14,\epsilon_U=0\) four-partite W-profiles. It does
**not** close the remaining \(\delta=14\) four-partite profiles with a \(K_3\)
part, any \(\delta\le13\) branch, any of the five shell templates globally, or
E407 Q32 overall. The proof is conditional on the retained 49-witness support
boundary and the listed W-profile classification.
