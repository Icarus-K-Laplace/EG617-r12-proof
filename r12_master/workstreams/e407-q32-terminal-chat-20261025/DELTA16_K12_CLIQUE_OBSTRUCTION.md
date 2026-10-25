# E407 Q32: the \(\delta=16\) endpoint kernel forces a forbidden \(K_{12}\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61 parent contract, the E407 minimum-support witness boundary, and the reverse-saturation lemma.

## 1. Frozen contract

Assume the E407 Q32 minimum-support boundary with \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), total core excess
\[
\sum_{v\in H}\epsilon_v=4,\qquad \epsilon_v=d_H(v)-12,
\]
and inherited \(\omega(H)\le11\). The latter follows because \(H\) is an induced subgraph of the retained 61-vertex parent \(F\) with \(\omega(F)\le11\).

In the \(\delta=16\) branch, the established reduction gives:
- \(U\) has four parts \(A,B,C,D\) of sizes \(7,7,7,8\) in \(L=\overline{H[U]}\);
- \(H[U]\) is complete within each part, so \(D\) induces a \(K_8\);
- \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- \(\epsilon_U=0\), so every vertex of \(U\) has core degree exactly 12;
- the five cross-edges of \(H[U]\) form a matching between five vertices \(D_{\rm end}\subset D\) and five vertices of \(A\cup B\cup C\);
- the endpoint split \((4,1)\) and \((3,2)\) has already been excluded by the four-unit excess budget.

Let \(E\) be the \(K_4\) component of \(H[W]\) that is the exact \(W\)-neighbourhood of all five vertices in \(D_{\rm end}\). Thus every \(e\in E\) is adjacent to all five vertices of \(D_{\rm end}\).

## 2. At most one vertex of \(E\) can fail to be complete to \(D\)

The reverse-saturation lemma says every \(w\in W\) is complete to exactly one of the four \(U\)-parts.

Suppose \(w\in E\) is not complete to \(D\). Then it must be complete to a small part \(P\in\{A,B,C\}\). Since \(w\) is already adjacent to the five distinct vertices of \(D_{\rm end}\), and \(|P|=7\),
\[
d_H(w,U)\ge5+7=12.
\]
But \(w\) belongs to a \(K_4\) component of \(H[W]\), so
\[
d_H(w,U)=d_H(w)-3=9+\epsilon_w.
\]
Consequently \(\epsilon_w\ge3\). Since the total excess in all of \(H\) is four, at most one vertex of \(E\) can fail to be complete to \(D\).

## 3. The one-exception case is impossible

Suppose exactly one vertex \(w_0\in E\) is not complete to \(D\). By the preceding argument, \(w_0\) is complete to a small part \(P\) and \(\epsilon_{w_0}\in\{3,4\}\). Its required \(U\)-neighbourhood has size \(9+\epsilon_{w_0}\), while \(P\cup D_{\rm end}\) already has size 12. Therefore:
- if \(\epsilon_{w_0}=3\), its \(U\)-neighbourhood is exactly \(P\cup D_{\rm end}\), so it misses all three vertices of \(D\setminus D_{\rm end}\);
- if \(\epsilon_{w_0}=4\), it has at most one additional \(U\)-neighbour beyond \(P\cup D_{\rm end}\), so it misses at least two vertices of \(D\setminus D_{\rm end}\).

Choose such a non-endpoint \(d\in D\) with \(dw_0\notin E(H)\). The other three vertices of \(E\) are complete to \(D\), hence are all neighbours of \(d\). Also \(d_H(d,W)=5\): its degree inside \(D\) is seven, it has no cross-edge in \(H[U]\), and \(d_H(d)=12\). Thus \(d\) has exactly three neighbours in \(E\) and only two neighbours outside \(E\).

This means \(d\) is not complete to the \(K_4\) component \(E\), and it cannot be complete to any other component of \(H[W]\), all of which have size at least four. But every vertex of \(U\) must be complete to at least one whole component of \(H[W]\): otherwise choose one non-neighbour from each of the four pairwise anticomplete clique components, obtaining an independent 5-set together with that vertex, contrary to \(\alpha(H)\le4\). Contradiction.

Therefore no exception exists: every vertex of \(E\) is complete to all of \(D\).

## 4. The final clique contradiction

The part \(D\) induces a \(K_8\) in \(H[U]\), and \(E\) induces a \(K_4\) in \(H[W]\). We have just proved that every cross-edge between \(D\) and \(E\) is present. Hence
\[
H[D\cup E]\cong K_{8+4}=K_{12},
\]
contradicting the inherited \(\omega(H)\le11\) bound.

Therefore the entire \(\delta=16\) four-partite boundary is **excluded** under the retained core/witness contract. This does not close \(\delta=15\) four-partite or \(\delta\le14\), and does not prove E407 Q32 or the original \(K_{145}\) theorem.
