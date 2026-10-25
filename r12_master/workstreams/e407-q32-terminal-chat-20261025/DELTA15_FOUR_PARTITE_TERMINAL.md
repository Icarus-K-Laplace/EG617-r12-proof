# E407 Q32: \(\delta=15\) four-partite boundary

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL structural reduction; one \(W\)-profile remains OPEN.**

## 1. Frozen contract and exact ledger

Assume the E407 Q32 support-boundary contract with 49 linear independent 4-set witnesses on \(U\), \(|U|=29\), \(|W|=18\), \(e(H)=284\), \(\alpha(H)\le4\), \(\omega(H)\le11\), and \(\delta(H)\ge12\). Suppose
\[
L=\overline{H[U]}
\]
is four-partite and \(\delta=e(L)-294=15\).

The 49 witness \(K_4\)'s force the part sizes of \(L\) to be \(7,7,7,8\); write the parts as \(A,B,C,D\). Every pair between two of \(A,B,C\) is used exactly once by the 49 witnesses. Each small-part vertex appears in seven blocks and has seven distinct \(D\)-partners, so it has exactly one unused \(D\)-partner. Consequently each small vertex is incident to at most one cross edge of \(H[U]\). The six cross edges of \(H[U]\) all join \(D\) to \(A\cup B\cup C\), and their six small-side endpoints are distinct.

Let \(t_d=d_{H[U]}(d)-7\) for \(d\in D\). Then
\[
\sum_{d\in D}t_d=6,\qquad 0\le t_d\le 2.
\]
The core ledger gives
\[
e(H[U])=97,\quad e_H(U,W)=154+\epsilon_U,\quad
e(H[W])=33-\epsilon_U,\quad \epsilon_U\in\{0,1\}.
\]

For each \(d\in D\), the independence-number condition forces \(d\) to be complete to a whole \(W\)-part. Since the smallest allowed \(W\)-part has size three and \(d_H(d,W)=5+\epsilon_d-t_d\), this gives \(t_d\le2\). In every profile with minimum part size four, \(t_d\le1\) except that the unique excess-one \(D\)-vertex may have \(t_d=2\).
Here \(\epsilon_U=\sum_{u\in U}(d_H(u)-12)\). The \(W\)-side clique-part profiles from NON_FOUR_PARTITE_TERMINAL.md are:
- \(\epsilon_U=0\): \(K_3\cup K_5^3\), \(K_4^3\cup K_6\), or \(K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge;
- \(\epsilon_U=1\): \(K_4\cup K_4\cup K_5\cup K_5\).

## 2. Saturation lemmas

**Lemma 2.1 (every \(U\)-vertex meets a whole \(W\)-part).** If \(H[W]\) is a disjoint union of clique parts, every \(u\in U\) is complete to at least one whole \(W\)-part. Otherwise one non-neighbour of \(u\) from each of the four parts would form an independent 5-set with \(u\).

If \(H[W]\) has the single cross edge between two \(K_4\) parts, the same conclusion holds for any \(u\) with \(d_H(u,W)\le5\): if \(u\) were not complete to any part, its non-neighbour sets in the two endpoint \(K_4\)'s would have to be the singleton cross-edge endpoints, forcing at least \(3+3=6\) neighbours in \(W\).

**Lemma 2.2 (no-whole-part alternatives).** Under the six-cross-edge contract, if \(w\in W\) is not complete to any of \(A,B,C,D\), then either
\[
d_H(w,U)\ge13,
\]
or there is a unique \(d\in D\) with \(t_d=2\), and two vertices \(a_1,a_2\) in one small part \(P\) such that
\[
N_H(w,U)=(P\setminus\{a_1,a_2\})\cup(D\setminus\{d\}),
\qquad d_H(w,U)=12.
\]
In the exceptional case, \(d\) is adjacent in \(H[U]\) to both \(a_1,a_2\), and \(w\) is nonadjacent to \(d\). In particular, if every \(d\in D\) has \(t_d\le1\), then a no-whole-part vertex has at least 13 \(U\)-neighbours.

**Proof.** Let \(A',B',C',D'\) be the non-neighbour sets of \(w\) in the four parts; all are nonempty. For each \(d\in D'\), every triple in \(A'\times B'\times C'\) must contain a cross edge to \(d\), or that triple together with \(d,w\) would be an independent 5-set. Equivalently, at least one of \(A',B',C'\) must be contained in the cross-neighbourhood of \(d\), so one such set has size at most \(t_d\le2\).

If a small non-neighbour set is a singleton, or if two small non-neighbour sets have size at most two, counting vertices outside these non-neighbour sets and using the small-side degree cap one gives at least 13 neighbours of \(w\). The only way to have fewer is for exactly one small non-neighbour set to have size two, the other two small non-neighbour sets to be the full 7-parts, and \(D'=\{d\}\). Then \(d\) must be adjacent to both vertices of that size-two set. The neighbourhood of \(w\) in \(U\) consists of the other five vertices of that small part and all seven vertices of \(D\setminus\{d\}\), so it has exactly 12 vertices. \(\square\`

## 3. The \(\epsilon_U=1\) branch is impossible

Now \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), and the total excess in \(W\) is only three. Lemma 2.2 rules out a no-whole-part vertex unless it is a \(K_4\)-vertex \(w\) with \(\epsilon_w=3\) in the exceptional 12-neighbour pattern. That exceptional pattern is impossible here: its unique \(d\in D\) has \(t_d=2\) and \(W\)-neighbourhood a \(K_4\) not containing \(w\); all seven vertices of \(D\setminus\{d\}\) are adjacent to \(w\), and each must then be adjacent to every vertex of \(w\)'s \(K_4\)-part (a degree-four \(D\)-vertex is complete to that part; a degree-five one is complete to that part plus one extra). The other three vertices of that \(K_4\) have zero excess, cannot be complete to \(D\), and would have at least seven \(D\)-neighbours plus a full small part, impossible. Thus every \(w\in W\) is complete to a \(U\)-part.

At least five distinct \(D\)-vertices have a cross edge in \(H[U]\). Every such vertex has exactly four \(W\)-neighbours and is therefore adjacent to all four vertices of one \(K_4\) part. (If the unique excess vertex is in \(D\) and has \(t_d=2\), it too has \(W\)-degree four; if it has \(t_d=1\), the other five endpoints still have degree four.)

Among the two \(K_4\) parts, one therefore has at least three such \(D\)-vertices. Call this part \(C\), and let \(k\ge3\) be the number of \(D\)-vertices adjacent to every vertex of \(C\). If \(C\) were complete to all of \(D\), then \(D\cup C\) would be a forbidden \(K_{12}\). Otherwise each \(w\in C\) is not complete to \(D\), so Lemma 2.2 and the three-unit \(W\)-excess budget force it to be complete to a small \(U\)-part. It then has at least \(7+k\ge10\) \(U\)-neighbours, whereas a \(K_4\)-vertex has \(9+\epsilon_w\) \(U\)-neighbours. Thus every one of the four vertices of \(C\) requires \(\epsilon_w\ge1\), exceeding the total \(W\)-excess three. Contradiction.

Hence **\(\epsilon_U=1\) is excluded**.

## 4. Two of the three \(\epsilon_U=0\) profiles are impossible

Here all \(U\)-vertices have degree 12 and \(W\) has total excess four.

### 4.1. \(H[W]=K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge

Every \(D\)-endpoint has four \(W\)-neighbours, and Lemma 2.1 forces these to be exactly one of the two \(K_4\) parts. Six endpoints are distributed across those two parts, so one part \(C\) has \(k\ge3\) endpoint neighbours. It cannot be complete to \(D\), or \(D\cup C\) would be \(K_{12}\).

Here every \(d\in D\) has \(t_d\le1\), so Lemma 2.2 implies that a vertex of \(C\) with no whole \(U\)-part has at least 13 \(U\)-neighbours and hence \(\epsilon_w=4\); the other three vertices of \(C\) would then have zero excess but, being adjacent to at least \(k\ge3\) endpoints and not complete to \(D\), would need at least \(7+k\ge10\) \(U\)-neighbours.

### 4.2. \(H[W]=K_4^3\cup K_6\)

Each of the six \(D\)-endpoints has \(W\)-degree four and is complete to a \(K_4\) part. Each of the three non-endpoint \(D\)-vertices has \(W\)-degree five and must also be complete to a \(K_4\) part plus one extra \(W\)-vertex; it cannot be complete to the \(K_6\) part. For the three \(K_4\) parts \(C_1,C_2,C_3\), let \(n_i\) count the \(D\)-vertices adjacent to all of \(C_i\). Every \(D\)-vertex is counted once, so
\[
n_1+n_2+n_3=9.
\]
No \(C_i\) can be complete to \(D\), as that would give a \(K_{12}\). Put \(C_i\) aside if \(n_i\ge3\). Every vertex of such a part must be complete to a small \(U\)-part: a no-part vertex would require excess four by Lemma 2.2, leaving the other three vertices of \(C_i\) with degree 12 but at least \(7+n_i\ge10\) \(U\)-neighbours. Consequently each vertex of \(C_i\) requires
\[
\epsilon_w\ge n_i-2.
\]
A no-part exception in a part with \(n_i\le2\) is also impossible: since the other two \(n_j\)'s sum to at least seven, one is at least four, and all four vertices of that part would require at least two excess units each. Thus no exception occurs in any \(C_i\), and the total excess satisfies
\[
\sum_{w\in W}\epsilon_w
\ge4\sum_{i=1}^3\max(0,n_i-2)\ge12,
\]
because \(n_1+n_2+n_3=9\). This contradicts the actual total excess four.

Therefore the only \(\epsilon_U=0\) profile not excluded by these arguments is
\[
\boxed{H[W]=K_3\cup K_5\cup K_5\cup K_5.}
\]

## 5. The remaining \(K_3\cup K_5^3\) profile forces a \(K_{11}\)

Let \(C_0\) denote the \(K_3\) part. For every \(d\in D\), \(t_d\le2\). If \(t_d>0\), then \(d\) has \(5-t_d\le4\) \(W\)-neighbours and must be complete to \(C_0\), the only \(W\)-part of size at most four. A \(t_d=0\) vertex has five \(W\)-neighbours; if it is adjacent to any vertex of \(C_0\), it must be complete to all of \(C_0\), since it cannot then be complete to a disjoint \(K_5\) part.

Suppose \(C_0\) is not complete to \(D\). By the all-or-none observation, its common \(D\)-neighbourhood has size \(h\le7\), and \(h\ge3\) because the six cross edges have maximum \(D\)-degree two. Every \(w\in C_0\) is not complete to \(D\). It cannot fail to be complete to every \(U\)-part: Lemma 2.2's argument would produce a non-neighbour \(d\in D\) with \(t_d>0\), but such a \(d\) is complete to \(C_0\). Thus each \(w\in C_0\) is complete to a small \(U\)-part, giving at least \(7+h\) \(U\)-neighbours. Since a \(K_3\)-vertex has \(10+\epsilon_w\) \(U\)-neighbours, this requires \(\epsilon_w\ge h-3\). Summing over the three vertices of \(C_0\) and using total excess four gives \(h\le4\).

At least four vertices of \(D\) are then nonadjacent to \(C_0\). Each has \(t_d=0\), hence five \(W\)-neighbours, and must be complete to one of the three \(K_5\) parts. By pigeonhole, two are complete to the same \(K_5\). That \(K_5\) cannot be complete to \(D\) (otherwise it creates a \(K_{13}\)). Nor can one of its vertices be a no-whole-part exception: that exceptional pattern would require a \(D\)-vertex \(d\) with \(t_d=2\), while the \(K_5\)-vertex would be adjacent to all of \(D\setminus\{d\}\); since \(\sum t_d=6\), another \(D\)-vertex has positive \(t\) and is complete to \(C_0\), hence cannot be adjacent to this \(K_5\)-vertex. Thus every vertex of that \(K_5\) is complete to a small \(U\)-part, and its two \(D\)-neighbours then force at least nine \(U\)-neighbours. Every \(K_5\)-vertex has \(8+\epsilon_w\) \(U\)-neighbours, so all five vertices require positive excess, contradicting the total excess four.

Therefore \(C_0\) **is complete to \(D\)**, and
\[
H[D\cup C_0]\cong K_{11}.
\]
This is allowed by \(\omega(H)\le11\), so it is a structural reduction, not yet a contradiction.

## 6. Exact ledger for the surviving profile

In the surviving case:
- \(\epsilon_U=0\), \(H[W]=K_3\cup K_5^3\), and \(C_0\) is complete to \(D\);
- \(\sum_{d\in D}t_d=6\), with \(t_d\in\{0,1,2\}\);
- each \(d\in D\) has exactly \(2-t_d\) neighbours in \(W\setminus C_0\), so there are exactly \(16-6=10\) edges from \(D\) to the three \(K_5\) parts;
- each \(w\in C_0\) has exactly \(2+\epsilon_w\) neighbours in \(A\cup B\cup C\), so there are \(6+\epsilon_{C_0}\) edges from \(C_0\) to the small parts;
- every \(K_5\)-vertex is complete to one small \(U\)-part (it cannot be complete to \(D\), which would create \(K_{13}\); the possible no-part exception would force adjacency to all but one \(D\)-vertex, including another positive-\(t_d\) vertex that is complete to \(C_0\)); its off-label degree is \(1+\epsilon_w\). Of the \(15+\epsilon_{K_5}\) off-label incidences across the three \(K_5\)'s, ten go to \(D\), leaving \(5+\epsilon_{K_5}\) edges to the small parts;
- if \(k_A,k_B,k_C\) count the full-part labels among the 15 \(K_5\)-vertices, then \(k_A+k_B+k_C=15\), and \(k_P\le5\) if \(P\) contains a cross-edge endpoint, \(k_P\le6\) otherwise. No \(K_5\) part can have all five vertices labelled to the same small part, as that would create \(K_{12}\).

## 7. The remaining \(K_3\cup K_5^3\) profile is impossible

For each small part \(P\in\{A,B,C\}\), let \(k_P\) be the number of vertices in the three \(K_5\) parts of \(H[W]\) that are complete to \(P\). Every \(K_5\)-vertex has exactly one such full-part label, so
\[
k_A+k_B+k_C=15.
\]
The \(K_3\) vertices are complete to \(D\), and each has only \(2+\epsilon_w\le6\) neighbours in the small parts, so none is counted among the \(k_P\).

If \(P\) contains a cross-edge endpoint \(u\), then \(d_H(u,W)=5\). Since every vertex labelled \(P\) is adjacent to all of \(P\), this gives \(k_P\le5\).

Now suppose \(P\) contains no cross-edge endpoint. Every \(u\in P\) then has \(d_H(u,W)=6\). If \(k_P=6\), all six labelled vertices are exactly \(N_H(u,W)\) for every \(u\in P\). By \(\alpha(H)\le4\), this six-set must contain a whole \(W\)-clique part. It contains no \(K_3\)-vertex, so it must contain an entire \(K_5\) part. All five vertices of that \(K_5\) would then be labelled \(P\), making \(P\cup K_5\) a forbidden \(K_{12}\). Hence \(k_P\le5\) also when \(P\) has no cross-edge endpoint.

Thus every \(k_P\le5\), and the sum identity forces
\[
k_A=k_B=k_C=5.
\]
There are six cross-edge endpoints, so choose one, \(u\in P\). It has exactly five \(W\)-neighbours, and those are precisely the five vertices labelled \(P\). Again \(\alpha(H)\le4\) forces this neighbourhood to contain a whole \(W\)-clique part. It cannot be the \(K_3\), whose vertices are labelled \(D\); it must be a \(K_5\) part. All five vertices of that \(K_5\) are labelled \(P\), so \(P\cup K_5\cong K_{12}\), contradicting \(\omega(H)\le11\).

Therefore the final \(K_3\cup K_5^3\) profile is also impossible. Together with Sections 3–4, this excludes the entire \(\delta=15\) four-partite branch under the retained core/witness contract. The remaining E407 Q32 cases have \(\delta\le14\), and E407 Q32 overall remains **OPEN / NOT_CERTIFIED**.
