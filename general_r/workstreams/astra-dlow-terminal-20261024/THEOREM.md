# Uniform low-offset terminal nonextension

Date: 2026-10-24. Status: **PROVED** relative to the frozen contextual cap.
Headline: **D_LOW_PROVED for every integer r >= 221**.
The requested stronger range 67 <= r <= 220 is not fully closed here.

## 1. Complete input contract and theorem

Let r >= 67. On a vertex set V of order 5r+1, the r color graphs
F=G_0,G_1,...,G_(r-1) partition all unordered pairs. Assume:

1. alpha(F)<=5, omega(F)<=r-1, delta(F)=r+epsilon, epsilon in {0,1}.
2. alpha(G_i)<=r for each i>0, including every induced subset.
3. The contextual cap is
       2e(F) <= 5r^2+7r+18.
4. There is a target-independent triple T of degrees
       (r+epsilon, r+epsilon+e_2, r+epsilon+e_3),
   where e_2,e_3 in {0,1}. Set eta=e_2+e_3.
5. Its common open target antineighbourhood, excluding T, is W, of
   order 2r-c, with c in {2,3,4} if epsilon=0, and c in {2,...,7}
   if epsilon=1.

These are consequences or hypotheses of the specified contextual
terminal, not hypotheses of an exact star or a cover-block model.

**Theorem.** Put M=10+eta. Every such terminal satisfies

    r <= B(M)-epsilon M,
    B(m)=(3m^2+5m+2)/2 - 3 p_5(m).                    (1)

Here p_5(m) is the balanced five-clique independence floor.
In particular all low-minimum-degree windows are impossible for
r>=221, and all high-minimum-degree windows are impossible for r>=209.
Thus all specified windows are impossible for every r>=221.

The upstream implication A_ext* is NOT assumed proved. The result is
a terminal nonextension theorem. Applied to the retained synthesis
it gives A_ext*(r) => P(r) for r>=221, conditionally on that interface.

## 2. A sparse non-target color supplies a large matching

Since T is independent and anticomplete to W, alpha(F[W])<=2.
Thus J=overline(F[W]), the union of the non-target colors on W,
is triangle-free. Also every G_i[W] is triangle-free.

For completeness, Mantel's inequality follows by summing
d_J(u)+d_J(v)<=|W| over edges uv and applying Cauchy:
sum d_J(v)^2<=|W|e(J), whereas sum d_J(v)^2>=4e(J)^2/|W|.
Hence e(J)<=floor(|W|^2/4).

Every non-target graph on W has at least |W|-r=r-c edges:
choosing one endpoint of each edge produces a vertex cover, and
alpha<=r requires its minimum vertex cover to have size at least r-c.
Consequently, with t_i=e(G_i[W])-(r-c)>=0,

    sum_(i>0) t_i
      <= floor((2r-c)^2/4)-(r-1)(r-c)
       = r+floor(c^2/4)-c
      <= r+5.                                         (2)

For r>=8, r+5<2(r-1), so some color has t_i<=1.

**Sparse-color lemma.** A triangle-free graph Q on 2r-c vertices,
with alpha(Q)<=r and e(Q)<=r-c+1, contains a matching of size >=r-c.

Proof. Let tau be its minimum vertex-cover size and e=e(Q).
Then tau>=r-c, so e-tau<=1. A vertex of degree at least three would
give a cover of size at most 1+(e-3)=e-2, impossible. Thus all
components are paths, cycles, or isolates.
A cycle has length at least four and contributes
e_component-tau_component>=2, impossible. A path of at least four
edges also contributes at least two. At most one component can be a
two-edge or three-edge path; the others are isolated edges or vertices.
In every remaining path component the maximum matching size equals
the minimum vertex-cover size, directly by alternating vertices/edges.
Adding over components proves nu(Q)=tau(Q)>=r-c. QED.

Every edge in this matching is a target nonedge, and its endpoints
are disjoint. This conclusion uses actual colors, not ideal blocks.

## 3. Extend the triple to five low-degree independent anchors

For epsilon=0, write kappa(v)=d_F(v)-r>=0. The cap gives

    sum_V kappa <= 6r+18.

If every edge uv of the matching in section 2 had
kappa(u)+kappa(v)>=7, its disjoint endpoints would consume at least
7(r-c)>6r+18 whenever r>7c+18. Since c<=4, r>=67 suffices.
Thus one matching edge has endpoint excess sum at most six.

For epsilon=1, use kappa(v)=d_F(v)-(r+1)>=0. The cap gives

    sum_V kappa <= r+17.

If every matching edge had endpoint excess sum at least two, then
2(r-c)>r+17 for r>2c+17, also valid for r>=67. Therefore some edge has
endpoint excess sum at most one.

Add those two endpoints to T. The resulting set A={a_1,...,a_5} is
target-independent, because they lie in W and their pair is a
non-target edge. In BOTH branches,

    sum_(a in A) d_F(a) <= 5r+6+eta.                    (3)

No property of a chosen non-target matching is promoted to all colors.

## 4. An actual bounded kernel, not an ideal partition

Every vertex outside A has at least one target neighbor in A;
otherwise it and A would be independent of size six.

Let H be the vertices outside A with at least two neighbors in A;
write m=|H|. Let C_i consist of a_i and all vertices whose unique
neighbor in A is a_i.

Each C_i is an actual target clique. Indeed, two nonadjacent private
neighbors, together with the other four anchors, would be independent
of size six. The anchor itself is adjacent to every private neighbor.

Counting anchor incidences gives

    sum_(v outside A) (|N_F(v) intersect A|-1)
       = sum_(a in A)d_F(a) -(5r-4)
       <= 10+eta.

Each member of H consumes at least one unit, so m<=10+eta<=12.
Since |C_i|<=r-1 and the C_i partition V\H,

    5r+1-m = sum_i |C_i| <=5r-5,

hence m>=6. Define b_i=|C_i| and d_i=r-1-b_i>=0. Then

    6<=m<=10+eta<=12,   sum_i d_i=m-6,   b_i>=r-7.       (4)

There may be arbitrary target edges BETWEEN the C_i. They are neither
deleted nor assumed absent.

## 5. The kernel capacity inequality

This is proved independently, in full, in DEFECT_PROPAGATION.md.
For ANY partition into five actual target cliques C_i and a kernel H
of size m, under alpha(G_i)<=r and delta(F)>=r+epsilon, it gives

    r <= (3m^2+5m+2)/2 - epsilon m -3e_F(H).             (5)

Its proof counts only actual edges between H and V\H, once each,
and uses all non-target colors at the same time.
It does not assume any restriction on multi-block covers or cycles.

Since alpha(F[H])<=5, we have e_F(H)>=p_5(m) in the relevant range
6<=m<=12. Here is an elementary proof avoiding a further extremal
theorem dependency. Order H uniformly at random and select each
vertex preceding all its neighbors. The selected set is independent,
and has expected size sum_v 1/(d_H(v)+1). Cauchy's inequality gives

    5 >= alpha(F[H]) >= sum_v 1/(d_H(v)+1)
                       >= m^2/(2e_F(H)+m).

Thus e_F(H)>=ceil(m(m-5)/10). For m=6,...,12 these integers are
1,2,3,4,5,7,9, exactly p_5(m). Substitution into (5) yields
r<=B(m)-epsilon m.

For clarity, p_5(m) is obtained by dividing m into five parts as
equally as possible; a graph of independence at most five has at least
the number of edges in those five disjoint cliques. This is the same
standard Turan independence floor used in the canonical contract.

The complete relevant arithmetic is

|m|p_5(m)|B(m), epsilon=0|B(m)-m, epsilon=1|
|---:|---:|---:|---:|
|6|1|67|61|
|7|2|86|79|
|8|3|108|100|
|9|4|133|124|
|10|5|161|151|
|11|7|189|178|
|12|9|220|208|

Both bound columns are strictly increasing. Since m<=M=10+eta,
(1) follows. In particular r>220 excludes all possible m and both
degree branches. This proves the theorem for all integers r>=221,
not just sampled values.

## 6. Equality and logical limits

At equality in (5), all the following are necessary:
- every kernel vertex has target degree exactly r+epsilon;
- for each non-target color, all inequalities used in its independent-
  subset neighborhood count are tight;
- the kernel-edge vertex-cover bound alpha(G_i[H])>=m-e(G_i[H])
  is tight whenever used with a positive coefficient;
- every counted non-target kernel-to-clique neighborhood is represented
  by exactly one edge from the chosen independent kernel subset;
- to attain the tabulated envelope, e_F(H)=p_5(m).

These are necessary conditions, not graph existence certificates.

No assertion is made that the intervals 67<=r<=220 (low branch) or
67<=r<=208 (high branch) contain terminals. Their exclusion remains
OPEN in this package. No full EG617 theorem or unconditional A_ext*
is claimed.

