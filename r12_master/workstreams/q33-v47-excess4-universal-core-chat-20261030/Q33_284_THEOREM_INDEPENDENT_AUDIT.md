# Independent audit of the Q33 universal 284-edge theorem

Date: 2026-10-30  
Status: **PROVED** under the five graph hypotheses. No inherited density cap is required by this local theorem.

## 1. Exact statement

There is no simple graph H satisfying
\[
|V(H)|=47,\quad e(H)=284,\quad
\delta(H)\ge12,\quad\alpha(H)\le4,\quad\omega(H)\le11.
\]
The handshake identity is
\[
\sum_{v\in H}(d(v)-12)=568-564=4.
\]
Write epsilon(v)=d(v)-12. Then every epsilon is a nonnegative integer and the total budget is exactly four.

## 2. Independent four-set

At most four vertices have positive excess, so at least43 vertices have degree12. The induced graph on those vertices has maximum degree at most12. A greedy independent-set algorithm removes at most13 vertices per selected vertex, hence finds an independent set of size at least ceil(43/13)=4. Choose four such vertices I={s1,s2,s3,s4}. Every vertex in I has degree exactly12.

This proof is elementary and does not use a Turan theorem, a density cap, or a solver.

## 3. Four private cliques and the exact exceptional-set identity

For v outside I, its support is N(v) intersect I. It is nonempty, or I union {v} is an independent five-set.

Let P_i be the vertices whose support is exactly {s_i}, and let
\[
K_i=P_i\cup\{s_i\}.
\]
Each P_i is a clique: two nonadjacent vertices in P_i together with I minus {s_i} would be an independent five-set. Hence K_i is a clique. The four K_i are pairwise disjoint.

Let Z be the remaining vertices, each with support size2,3,4. Put d_i=|N(s_i) intersect Z|. Since d(s_i)=12,
\[
|K_i|=13-d_i\le11,\qquad d_i\ge2.
\]
There are43 vertices outside I and48 I-to-outside incidences, so
\[
\sum_{z\in Z}(|N(z)\cap I|-1)=5,\qquad
\sum_i d_i=|Z|+5.
\]
Each z contributes between1 and3 to the surplus five, giving 3<=|Z|<=5. The exact support patterns are:
- |Z|=3: support sizes (4,2,2) or (3,3,2), all K_i have order11;
- |Z|=4: support sizes (3,2,2,2), clique orders (10,11,11,11);
- |Z|=5: support sizes all2, clique orders (9,11,11,11) or (10,10,11,11).

The independent arithmetic verifier enumerates 9,40,48 labelled support multisets for these three values, respectively.

## 4. Universal common-neighbour capacity

This proof step was repaired to avoid the old Kang–Pikhurko invocation.

Let W be any 25-set. Suppose alpha(H[W])<=2 and let L be the complement of H[W]. Then L is triangle-free and alpha(L)=omega(H[W])<=11, so L is non-bipartite. For a shortest odd cycle of length2k+1, every outside vertex has at most k neighbours on it. Mantel on the remaining 24-2k vertices gives
\[
e(L)\le2k+1+k(24-2k)+
\left\lfloor(24-2k)^2/4\right\rfloor\le145.
\]
Thus e(H[W])>=300-145=155. But
\[
e(H[W])\le\frac12\sum_{w\in W}d_H(w)
\le\frac{25\cdot12+4}{2}=152,
\]
a contradiction. Hence no 25-set has independence number at most2.

For a nonedge uv, let R be the common non-neighbourhood of u,v. An independent triple in H[R] together with u,v is an independent five-set, so alpha(H[R])<=2. Therefore |R|<=24 and
\[
|N(u)\cap N(v)|\le3+\epsilon(u)+\epsilon(v). \tag{4.1}
\]

At most one external vertex can be complete to a fixed K10. If x,y are both complete to it and xy is an edge, there is a K12. If xy is a nonedge, they have at least ten common neighbours, contradicting (4.1), since epsilon(x)+epsilon(y)<=4 and hence the right side is at most7.

The stronger 2+epsilon(u)+epsilon(v) estimate uses the inherited density caps and is not used here.

## 5. K11–K11 two-support obstruction

Suppose z has support exactly {s_i,s_j}, and both K_i,K_j have order11. Let
\[
A=K_i\setminus N(z),\quad B=K_j\setminus N(z),\quad
a=|A|,\ b=|B|.
\]
Both are nonempty: otherwise z together with the corresponding K11 is a K12.

Every pair across A x B is an edge. A missing cross-edge, together with z and the other two vertices of I, would form an independent five-set.

The vertex z has at least22-a-b neighbours in K_i union K_j, while every x in A has its ten internal clique neighbours plus all b vertices of B; similarly for B. The charged vertex sets {z}, A, B are disjoint, and
\[
\sum_{x\in\{z\}\cup A\cup B}\epsilon(x)
\ge f(a,b)
\]
where
\[
f(a,b)=\max(0,10-a-b)+a\max(0,b-2)+b\max(0,a-2)\ge6.
\]
The exact minimum is6 at (a,b)=(2,2), so this is impossible with total excess4. No K11–K11 two-support vertex exists.

## 6. Exhaustion of |Z|=3,4,5

### 6.1 |Z|=3

The support sizes are (4,2,2) or (3,3,2), so at least one support has size2. All four private cliques are K11, contradicting Section5.

### 6.2 |Z|=4

There is one K10, call it K0, and three K11s K1,K2,K3. If a 2-support joins two K11s, Section5 applies. Otherwise the three 2-supports are z_i with support {s0,s_i}; the remaining 3-support is supported on {s1,s2,s3}.

Set A_i=K0 minus N(z_i), a_i=|A_i|, and B_i=K_i minus N(z_i), b_i=|B_i|>=1. The independent-five blocker makes A_i x B_i complete.

For u in K0, each z_i either supplies one neighbour (if u is adjacent to z_i) or is replaced by all b_i vertices of B_i. The three alternatives are disjoint across i, so pointwise
\[
\epsilon(u)\ge\sum_{i:u\in A_i}(b_i-1).
\]
For v in B_i, d(v)>=10+a_i, so epsilon(v)>=max(0,a_i-2). Also d(z_i)>=21-a_i-b_i, so epsilon(z_i)>=max(0,9-a_i-b_i). Summing these disjoint B_i and z_i contributions with the pointwise K0 bound gives
\[
4\ge\sum_{i=1}^3\left[
\max(0,9-a_i-b_i)+a_i(b_i-1)+b_i\max(0,a_i-2)
\right].
\]
For every a,b>=1, the bracket is at least6 (exact minimum6 at (2,1)). Thus every a_i=0. All three distinct z_i would then be complete to K0, contradicting the K10 completion-capacity lemma.

### 6.3 |Z|=5, profile (9,11,11,11)

All five supports have size2. The K9 distinguished vertex has support degree4, so four supports meet it. The fifth joins two K11s and is forbidden by Section5.

### 6.4 |Z|=5, profile (10,10,11,11)

If a support joins the two K11s, Section5 applies. Otherwise there is one K10–K10 support and four mixed K10–K11 supports. The mixed support multiplicity matrix has every row and column sum2. Up to row/column relabelling the only two forms are
\[
P=\begin{pmatrix}2&0\\0&2\end{pmatrix},
\qquad
D=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

**Pattern P.** Each K10 has two support points to one K11; at most one can be complete to that K10, so select one noncomplete point on each of the two disjoint K10/K11 pairs. If A,B are its missing sets, a=|A|>=1, b=|B|>=1, and A x B is complete. The degree charge on {z} union A union B is at least
\[
g(a,b)=\max(0,9-a-b)+a\max(0,b-3)+b\max(0,a-2)\ge4.
\]
The two selected pairs are vertex-disjoint, so total excess is at least8, contradiction.

**Pattern D.** There are four distinct mixed supports z_e and one K10–K10 support. For every support edge e=ij, set A_{i,e}=K_i minus N(z_e), a_{i,e}=|A_{i,e}|. Every A_{i,e} x A_{j,e} is complete.

For v in K_i, let M_i(v) be the incident supports e for which v is in A_{i,e}. Because the opposite private cliques are distinct along the incident supports,
\[
d(v)\ge12+\sum_{e\in M_i(v)}(a_{j,e}-1).
\]
At a K10 vertex there is at most one negative summand, from the unique K10–K10 support; its other two supports go to K11s, whose missing sets are nonempty. At a K11 vertex there are two mixed supports; two negative summands are possible, but then the desired truncated terms are both zero. Using delta(H)>=12 and the elementary integer inequality gives pointwise
\[
\epsilon(v)\ge\sum_{e\in M_i(v)}\max(0,a_{j,e}-2).
\]
Summing over all four private cliques yields
\[
\sum_{v\notin Z}\epsilon(v)\ge
\sum_{e=ij}\left[
a_{i,e}\max(0,a_{j,e}-2)+
a_{j,e}\max(0,a_{i,e}-2)
\right]. \tag{5}
\]
For a mixed support e, let a be its K10 missing-set size and b its K11 missing-set size. Here b>=1; if e is selected noncomplete to its K10, then a>=1. Its support vertex contributes epsilon(z_e)>=max(0,9-a-b), so the edge's total charge in (5) plus epsilon(z_e) is at least
\[
h(a,b)=\max(0,9-a-b)+a\max(0,b-2)+b\max(0,a-2)\ge5.
\]
At most one of the two mixed supports incident with either K10 can be complete to that K10. Hence at least two distinct mixed supports have a>=1. They contribute at least5 each. If the two selected supports share a K11, their forced-neighbour sets lie in two distinct K10 cliques; the pointwise inequality (5) counts these as disjoint edge sets. The total excess is at least10, contradiction.

All support cases are excluded. This proves the universal 284-edge theorem.

## 7. Audit findings and repairs

1. The previous common-neighbour file claimed the stronger 2+epsilon(u)+epsilon(v) cap while presenting a proof that did not establish it without density caps. It has been replaced by the correct universal 3+epsilon(u)+epsilon(v) bound from the 25-set shortest-cycle/Mantel argument. The stronger 2+ bound is explicitly labelled as cap-dependent and unused.
2. The D-template pointwise charging is valid: multiple missing sets at one vertex correspond to distinct opposite private cliques, so forced-neighbour edge sets do not overlap. Negative increments are handled pointwise before summation.
3. The finite verifier enumerates support multisets and integer minima; it does not certify the graph theorem by failed graph search. The proof above supplies the analytic argument.
4. The degree-11 minimum-degree source uses a different 12-neighbourhood union argument; it is audited in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md.

## 8. Replay boundary

Q33_SOURCE_COMPLETE_REPLAY.py checks the finite arithmetic, support multiset counts, mixed matrices, charge minima, and (when supplied) all127 exact rational rows of the lower-order certificate. A PASS is a replay of those finite checks only. The graph theorem is established by Sections2–6, not by a SAT/ILP search.
