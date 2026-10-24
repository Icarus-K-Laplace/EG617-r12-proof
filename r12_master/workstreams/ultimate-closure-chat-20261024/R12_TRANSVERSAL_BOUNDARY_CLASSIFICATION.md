# R12 minimum-transversal classification for the witness boundary kernels

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL necessary-structure theorem; excludes boundary parameter profiles but not the full E407/E408 terminals.**

## 1. Frozen contract and notation

Let H be the 47-vertex core with
\[
\alpha(H)\le4,\qquad d_H(x)=12+\epsilon_x,\quad \epsilon_x\ge0.
\]
For the two 284-edge boundary kernels, \(\sum_H\epsilon_x=4\). Let \(\mathcal Q\) be the selected linear family of independent 4-sets, each a K5-component witness's core part. Distinct members intersect in at most one vertex. Put \(U=\bigcup\mathcal Q\), \(W=V(H)\setminus U\), \(L=\overline{H[U]}\), and let J be the set of edges of L not covered by any selected Q. The Q-edges are pairwise edge-disjoint, so
\[
e(J)=\delta,\qquad e(H[U])=\binom{|U|}{2}-6|\mathcal Q|-\delta.
\]
The transversal theorem proved in R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md gives \(d_H(w,U)\ge7\) for every \(w\in W\).

For any \(T\subseteq U\) meeting every \(Q\in\mathcal Q\), call T a 7-transversal if \(|T|=7\).

## 2. A general packing fact: distinct 7-transversals are disjoint

In E407, there are seven selected colors, each contributing seven pairwise-disjoint Q-sets. In E408 Q33, there are eight selected colors, each contributing seven such sets.

**Lemma 2.1.** In either case, two distinct 7-transversals \(T,T'\) cannot overlap in \(s\in\{1,\ldots,6\}\) vertices.

**Proof.** Every color class consists of seven disjoint Q-sets, so each 7-transversal meets every Q in exactly one vertex. If \(|T\cap T'|=s\), then in each color class the \(7-s\) blocks whose T-vertex lies in \(T\setminus T'\) pair those \(7-s\) vertices with \(7-s\) distinct vertices of \(T'\setminus T\). Across different colors, none of these ordered pairs can repeat: a repeated pair would put the same two vertices in two distinct Q-sets, violating linearity. Thus \(c(7-s)\le(7-s)^2\), where \(c=7\) for E407 and \(c=8\) for E408. For \(s\ge1\), \(c>7-s\), contradiction. Hence distinct 7-transversals are disjoint. \(\square\)

Also, there can be at most three pairwise-disjoint 7-transversals. Four would cover 28 vertices, and every Q would have to contain one vertex from each, leaving the remaining vertex of U outside every Q, contrary to U being their union.

## 3. E407 Q32: the 49-witness boundary requires \(\delta\ge2\)

Here \(|U|=29\), \(|\mathcal Q|=49\), \(|W|=18\), and
\[
e(L)=294+\delta,\quad e(H[U])=112-\delta,\quad
e_H(U,W)=124+2\delta+\epsilon_U,
\]
where \(\epsilon_U=\sum_{u\in U}\epsilon_u\le4\). Since every \(w\in W\) has at least seven neighbours into U,
\[
N_7:=|\{w\in W:d_H(w,U)=7\}|
\ge20-2\delta-\epsilon_U. \tag{1}
\]

**Theorem 3.1.** Under the E407 boundary contract, \(\delta\ge2\).

**Proof.** Suppose \(\delta\le1\). For a 7-transversal T and x in T, the seven Q-sets containing x (one in each selected color) have pairwise-disjoint triples outside x. Those triples cover 21 of the 22 vertices in \(U\setminus T\), leaving at most one possible H-neighbour of x outside T. Also, no Q contains two vertices of T, so H[T] is K7 with at most \(\delta\) edges deleted (only J-edges can delete a pair). Since \(\delta\le1\), at least one of the at least three zero-excess vertices in T is incident to no J-edge. That vertex has at least six neighbours in H[T], hence at most six neighbours in W. Therefore at most six vertices w in W can have \(N_H(w)\cap U=T\).

Let k be the number of distinct 7-transversals arising as \(N_H(w)\cap U\) for degree-seven W-vertices. Lemma 2.1 and the four-transversal union argument give k≤3. We now exclude k=3. If T1,T2,T3 are three such transversals, put R=U\(T1 union T2 union T3), so |R|=8. Every Q contains one vertex from each T_i and one vertex from R. For r in R, let q_r be the number of the seven selected color classes in which r is the omitted vertex. Then sum_R q_r=7. For each i, r appears in \(7-q_r\) Q-sets and is paired with \(7-q_r\) distinct vertices of T_i; otherwise a pair would repeat across two Q-sets. Hence r has at most q_r H-neighbours in each T_i. It follows that
\[
d_H(r)\le d_{H[R]}(r)+\sum_{i=1}^3d_H(r,T_i)
\le7+3q_r.
\]
Since \(d_H(r)\ge12\), every \(q_r\ge2\), forcing \(\sum_Rq_r\ge16\), contradiction. Thus k≤2.

Consequently \(N_7\le6k\le12\). But (1), with \(\delta\le1\) and \(\epsilon_U\le4\), gives \(N_7\ge14\). Contradiction. Therefore \(\delta\ge2\). \(\square\)

This is a real boundary-profile exclusion: the 49 witness K4s cannot be accompanied by zero or one additional edge of L.

## 4. E408 Q33: the 56-witness boundary requires \(2\delta+\epsilon_U\ge8\)

Here \(|U|=31\), \(|\mathcal Q|=56\), \(|W|=16\), and
\[
e(L)=336+\delta,\quad e(H[U])=129-\delta,\quad
e_H(U,W)=114+2\delta+\epsilon_U,\quad
e(H[W])=41-\delta-\epsilon_U.
\]
The retained \(\alpha(H[W])\le4\) condition gives \(e(H[W])\ge p_4(16)=24\), hence \(\delta+\epsilon_U\le17\). The seven-neighbour transversal floor gives
\[
N_7:=|\{w\in W:d_H(w,U)=7\}|
\ge14-2\delta-\epsilon_U. \tag{2}
\]

**Theorem 4.1.** Under the E408 Q33 boundary contract,
\[
\boxed{2\delta+\epsilon_U\ge8.}
\]

**Proof.** Suppose \(2\delta+\epsilon_U\le7\). Then \(\delta\le3\), and (2) gives \(N_7\ge7\), so a 7-transversal T exists.

For any 7-transversal T, each of the eight selected color classes contains seven disjoint Q-sets and T hits each exactly once. For a fixed x in T, the eight triples \(Q\setminus\{x\}\) are pairwise disjoint and cover all 24 vertices of \(U\setminus T\). Thus every pair xz with x in T and z in \(U\setminus T\) lies in a selected Q and is a nonedge of H. Hence T is anticomplete to \(U\setminus T\). Also H[T] is K7 with at most \(\delta\le3\) edges deleted, so it is connected. Therefore T is a connected component of H[U].

Distinct such components are disjoint by Lemma 2.1, and there are at most three. Let k be their number. If k=3, the remaining set R has size10 and is nonempty. Any non-clique T_i has independence number at least two, so together with one vertex from each of the other two components and one vertex of R it would give an independent 5-set. Thus all three T_i must be K7s. The remaining graph R must then have \(\alpha(H[R])\le1\), so it is K10 with 45 edges. But
\[
e(H[R])=e(H[U])-63=(129-\delta)-63=66-\delta,
\]
forcing \(\delta=21\), contradicting \(\delta\le3\). Thus k is not 3.

If k=2, then each Q contains exactly one vertex from each of the two 7-components. In each of the eight selected colors, the seven Q-sets therefore define a perfect matching between their two 7-vertex sets. No pair can repeat across colors by linearity, but eight matchings require \(8\cdot7=56\) distinct pairs and there are only \(7\cdot7=49\) possible pairs. Contradiction.

If k=1, let T be the unique component and R=U\T, |R|=24. If T is not a clique, then \(\alpha(H[T])\ge2\) and \(\alpha(H[R])\le2\), requiring \(e(H[R])\ge p_2(24)=132\). But
\[
e(H[R])=e(H[U])-e(H[T])=108-\delta+j_T\le108,
\]
where j_T is the number of J-edges inside T and \(j_T\le\delta\). This is impossible. Hence T is a K7. Each x in T has exactly six neighbours inside U and therefore \(d_H(x,W)=6+\epsilon_x\). At least one x in T has \(\epsilon_x=0\), since the total core excess is four. Thus at most six vertices of W can have U-neighbourhood exactly T, giving \(N_7\le6\), contrary to \(N_7\ge7\) from (2). Therefore \(2\delta+\epsilon_U\ge8\). \(\square\)

## 5. What remains open

The new inequalities remove only the low-extra-edge boundary profiles:
- E407 Q32: \(\delta\ge2\), so \(e(L)\ge296\) for the v=29, 49-witness kernel.
- E408 Q33: \(2\delta+\epsilon_U\ge8\), jointly with \(\delta+\epsilon_U\le17\), so the boundary must carry a nontrivial amount of extra complement edges and/or degree excess inside U.

They do not exclude the remaining integer profiles, construct no graph, and do not close E407 Q32, E408 Q32, E408 Q33, or the original K145 theorem. E408 Q32 has a 285-edge core and is not covered by these 284-edge boundary calculations.
