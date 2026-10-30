# Universal nonexistence theorem for the 47-point / 284-edge Q33 core

Status: **PROVED** under the five explicit core hypotheses and inherited density caps.

## Theorem

There is no simple graph H satisfying
\[
|V(H)|=47,\quad e(H)=284,\quad \delta(H)\ge12,\quad
\alpha(H)\le4,\quad\omega(H)\le11.
\]

## Independent proof audit

Set epsilon(v)=d(v)-12. Then
\[
\sum_v\epsilon(v)=2\cdot284-47\cdot12=4.
\]
The independent-four-set lemma supplies four independent degree-12 vertices I={s_1,s_2,s_3,s_4}.

For v outside I, its I-support is nonempty, or I union {v} is an independent five-set. Let P_i be the vertices whose support is exactly {s_i}, and K_i=P_i union {s_i}. Each P_i is a clique: two nonadjacent members, together with I minus {s_i}, would be an independent five-set. Thus K_i is a clique, and the four K_i are pairwise disjoint.

Let Z be the remaining vertices, each with support size 2,3 or4. Put d_i=|N(s_i) intersect Z|. Since d(s_i)=12,
\[
|K_i|=13-d_i\le11,\qquad d_i\ge2.
\]
There are 43 vertices outside I, and 48 I-to-outside incidences. Hence
\[
\sum_{z\in Z}(|N(z)\cap I|-1)=5,\qquad
\sum_i d_i=|Z|+5.
\]
It follows that 3<=|Z|<=5 and the only clique-size/support patterns are:
- |Z|=3: (11,11,11,11), support sizes (4,2,2) or (3,3,2);
- |Z|=4: (10,11,11,11), support sizes (3,2,2,2);
- |Z|=5: (9,11,11,11) or (10,10,11,11), all support sizes two.

The source-complete common-neighbour lemma proves, using R(2,24)=empty and no external theorem,
\[
|N(u)\cap N(v)|\le2+\epsilon(u)+\epsilon(v)
\]
for every nonedge uv. Consequently at most one external vertex is complete to any K10.

If z has support exactly two distinguished vertices whose private cliques are both K11, let A,B be its non-neighbours in those cliques, with a=|A|, b=|B|. Then a,b>=1 and A×B is complete bipartite, since a missing cross-edge gives an independent five-set with z and the other two points of I. The disjoint excess charge is at least
\[
f(a,b)=\max(0,10-a-b)+a\max(0,b-2)+b\max(0,a-2)\ge6.
\]
This is impossible with total excess four. Thus no K11-K11 2-support is allowed.

### Exhaustion of |Z|=3,4,5

**|Z|=3.** The three support sizes sum to eight, so they are (4,2,2) or (3,3,2). A 2-support joins two K11 labels, forbidden by the preceding six-unit obstruction.

**|Z|=4.** There is one K10, K0, and three K11s K1,K2,K3. If no 2-support joins two K11 labels, the three 2-supports join K0 to each K_i. Let A_i=K0\\N(z_i), a_i=|A_i|, and B_i=K_i\\N(z_i), b_i=|B_i|>=1. Every A_i×B_i is complete. For u in K0, the three support points and their blockers give the pointwise bound
\[
\epsilon(u)\ge\sum_{i:u\in A_i}(b_i-1).
\]
For v in B_i, epsilon(v)>=max(0,a_i-2), and epsilon(z_i)>=max(0,9-a_i-b_i). The charged sets B_i, {z_i}, and the pointwise K0 contributions are disjoint in the incidence accounting, giving
\[
4\ge\sum_i\left[\max(0,9-a_i-b_i)+a_i(b_i-1)+b_i\max(0,a_i-2)\right].
\]
For every a,b>=1 the bracket is at least six. Thus all a_i=0, so all three z_i are complete to K0, contradicting the K10 completion-capacity lemma.

**|Z|=5, clique sizes (9,11,11,11).** The K9 label has support degree four, so four of the five 2-supports meet it. The remaining support joins two K11 labels, forbidden.

**|Z|=5, clique sizes (10,10,11,11).** If a support joins the two K11 labels, it is forbidden. Otherwise the support multigraph has one K10-K10 edge and four mixed edges, forming a 2x2 nonnegative integer matrix with every row and column sum two. Up to relabelling there are exactly two matrices:
\[
P=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
D=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

For P, at most one external point is complete to each K10, so one noncomplete support point can be selected on each doubled K10-K11 pair. For its missing-set sizes a,b>=1, the disjoint charge is
\[
g(a,b)=\max(0,9-a-b)+a\max(0,b-3)+b\max(0,a-2)\ge4.
\]
The two selected clique pairs are disjoint, so total excess is at least eight.

For D, let A_{i,e}=K_i\\N(z_e), a_{i,e}=|A_{i,e}|. The blocker A_{i,e}×A_{j,e} is complete. For v in K_i, let M_i(v) be the incident supports e for which v∈A_{i,e}. Since |K_i|-1=12-d_i,
\[
d(v)\ge12+\sum_{e\in M_i(v)}(a_{j,e}-1).
\]
At a K10 vertex at most one summand can be -1 (only the K10-K10 edge); the other two are nonnegative because the opposite K11 missing sets are nonempty. At a K11 vertex there are two mixed supports; if both summands are -1 then both truncated terms below vanish. The elementary integer inequality therefore gives pointwise
\[
\epsilon(v)\ge\sum_{e\in M_i(v)}\max(0,a_{j,e}-2).
\]
Summing over the four private cliques yields
\[
\sum_{v\notin Z}\epsilon(v)\ge
\sum_{e=ij}\left[
a_{i,e}\max(0,a_{j,e}-2)+
a_{j,e}\max(0,a_{i,e}-2)\right]. \tag{5}
\]
For a mixed support e, let a be its K10 missing-set size and b its K11 missing-set size. Its support point has epsilon(z_e)>=max(0,9-a-b). If a>=1, the corresponding terms from (5) and z_e total at least
\[
h(a,b)=\max(0,9-a-b)+a\max(0,b-2)+b\max(0,a-2)\ge5. \tag{6}
\]
At most one of the two mixed support points incident with either K10 can be complete to that K10. Thus at least two distinct mixed supports have a>=1. Their selected z_e are distinct. If they share a K11 clique, the pointwise inequality (5) counts the two forced neighbour sets in the two distinct K10 cliques separately; no edge is counted twice. The total excess is therefore at least 5+5=10, impossible.

This checks D equations (5)–(6) at the incidence level. In particular, if a vertex lies in multiple missing sets A_{i,e}, the forced neighbours lie in distinct opposite private cliques, so those edge sets are disjoint. The negative increments are controlled pointwise before summing; no excess unit or forced edge is duplicated.

All support cases are excluded. Therefore no graph H with the five stated hypotheses exists.

## Independent replay

The source verifier blob was read from the target branch. A separate standard-library replay was added as Q33_SOURCE_COMPLETE_REPLAY.py. It checks:
- D(13), D(14), D(23), D(24), D(37);
- R(2,24) cycle inequality and R(3,35) triangle-free bounds;
- all 20 C5 type-set compatibility pairs, all K9,9 singleton-extension cases, and all ten K9,9-minus-edge overlap cases;
- the 127-row certificate separately via the original exact Fraction verifier;
- the independent-four Turán table;
- 9/40/48 support-multiset counts and both mixed matrices;
- exact minima 6,6,4,5;
- D-template pointwise no-double-count inequalities.

The replay passed. It is a finite arithmetic/type check; the universal graph proof is the analytic argument above.