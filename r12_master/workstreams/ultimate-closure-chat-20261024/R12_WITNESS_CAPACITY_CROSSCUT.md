# R12 witness-capacity cross-cut theorem

Date: 2026-10-24  
Status: **PROVED necessary-structure theorem; terminal exclusion remains OPEN.**  
Purpose: derive constraints common to all five E407 Q32 templates and the E408 Q33/d3 exact-129 color-factor system, without assuming witness sets coincide.

## 1. Frozen contract

Let F be a 61-vertex T61 residual with alpha(F)<=5, omega(F)<=11, a regular degree-13 pivot p, shell A=N_F(p) of size13, and core H=V(F)\(A union {p}) of size47. Assume e(H)=284, delta(H)>=12, so

    epsilon(x)=d_H(x)-12 >=0,   sum_H epsilon(x)=2*284-47*12=4.

For a in A, N_H(a)=N_F(a) intersect H. For a regular shell vertex b with missing-neighbourhood T_b=N_M(b) intersect S and t_b=d_M(b)+g_b<=3, put H_b=H\N_H(b). The witness lemma gives alpha(H_b)=4.

In E407 Q32, all ten vertices B=A\S are regular and t_b=k_b=d_M(b)<=3. In E408 Q33/d3, k_b<=3 and beta+X+G_B=3, so at least seven B vertices have g_b=0 and t_b=k_b<=3; every B vertex has t_b<=6.

## 2. Universal three-shell-row support

**Lemma 2.1.** Every independent 4-set Q in H has target neighbours in at least three distinct shell rows:

    |{a in A : Q intersect N_H(a) is nonempty}| >= 3.

**Proof.** Let U={a in A: Q intersects N_H(a)}. If a,a' are both in A\U and aa' is not a target edge, then Q union {a,a'} is an independent 6-set in F, contradicting alpha(F)<=5. Thus A\U is a target clique. The pivot p is adjacent to every vertex of A, so {p} union (A\U) is a target clique of size 1+13-|U|. Since omega(F)<=11, 14-|U|<=11 and |U|>=3. ∎

This is stronger than merely saying Q_b hits every hub missing to b. A low-row witness Q_b is anticomplete to b, must hit every a in T_b, and must hit at least three shell vertices in total.

## 3. Hub vertex-cover rule

For an independent 4-set Q in H, define

    U_S(Q)={a in S : Q intersects N_H(a)}.

If Q is anticomplete to b in B, then:

1. T_b is a subset of U_S(Q), because otherwise Q union {a,b} is independent of size6 for a missing edge ab.
2. U_S(Q) is a vertex cover of M[S], because if a,a' form a missing edge and Q misses both rows, Q union {a,a'} is independent of size6.

Equivalently, U_S(Q) must cover all edges of the missing graph induced by S union {b}, with b fixed outside the cover. Therefore

    |U_S(Q)| >= tau_b,

where tau_b is the minimum number of S vertices that contains T_b and covers every edge of M[S].

The total shell support of Q is at least three by Lemma 2.1, even when tau_b is zero, one, or two.

### Consequence for the five E407 Q32 templates

The V12 row-type screen has the following necessary lower bounds on the *sum of hub-row hits* across the ten B witnesses. These are multiplicity counts (one hit means an edge a-q with q in Q_b), not counts of distinct row labels across all witnesses.

| Template | M[S] | Row types | Lower bound on sum_b tau_b |
|---|---|---|---:|
| A | empty | sizes 0,1,3; 3n0+2n1<=8 | 22 |
| B | empty | sizes 0,2,3; 3n0+n2<=8 | 22 |
| C | one edge | sizes 0,1,3; 3n0+2n1<=9 | 22 |
| D | one edge | sizes 0, two allowed pairs, 3; 3n0+na+nb<=9 | 21 |
| E | P3 | sizes 0, center singleton, ends pair, 3; 3n0+2n1+n2<=10 | 20 |

For A, B, and C the count constraints force at least respectively six, two, and at least the edge-floor-required number of full-S rows; all five templates retain the original global edge floor e(M)>=22. In D/E, the internal missing edges of S contribute one/two to e(M), respectively. These lower bounds do not alone contradict the 30-32 hub-to-core incidences: different witnesses can reuse the same shell-core edge when their independent sets overlap.

## 4. Defect-sensitive extension of independent triples

**Lemma 4.1.** Let b be a shell vertex with t_b<=3. Every independent set X of size at most three in H_b extends to an independent 4-set in H_b.

**Proof.** For X of size three,

    |N_H[X]| <= sum_{x in X}(d_H(x)+1)
             = 39 + sum_{x in X} epsilon(x)
             <= 43.

But |H_b|=47-t_b>=44. Hence H_b contains a vertex outside N_H[X], which extends X. The same inequality is stronger for |X|<3. ∎

A useful failure certificate for larger t_b is also immediate. If an independent triple X in H_b does not extend, then H_b is covered by its three closed H-neighbourhoods, so

    47-t_b <= 39+epsilon(X),
    t_b >= 8-epsilon(X),   epsilon(X)=sum_{x in X}epsilon(x).

Since sum_H epsilon=4, nonextension can occur only for t_b>=4 and only when X contains enough of the four units of core excess. In E408 Q33, this failure mode is restricted to decorated rows with t_b in {4,5,6}; it cannot occur for any of the at least seven undecorated B rows.

**Completion consequence.** If an isolated C-coloured K5 component has vertex set {b} union S' union X, where b is regular, S' is a set of shell hubs missing to b, and X is an independent subset of H of size at most three, Lemma 4.1 extends X to a maximum independent 4-set Q_b in H_b. The hub vertex-cover rule then forces the extension vertices to hit every hub in S'. This is a derived condition, not an assertion that the original K5 component itself contains a four-set witness.

## 5. E408 Q33: exact-129 K5-component packing

Assume the retained exact-129 factor theorem: for each non-target color C with e_C(R)=129, C[R] consists of ten isolated K5 components and an 11-vertex exceptional gadget U with alpha(C[U])=2. Also assume the seven-block one-or-two rule, so each x in R has at least one C-edge into each of the seven outer K12 blocks.

Because B is a target clique, it is independent in every non-target color C, hence |B intersect U|<=2. Therefore at least eight B vertices lie in the ten K5 components. At most three of these components can contain an S vertex (there are only three S vertices, and each K5 component is disjoint from the others). Thus at least five K5 components have the form

    {b} union Q,    b in B, Q subset H, |Q|=4,

with Q independent in H and anticomplete to b. Each such Q obeys Lemmas 2.1 and 3.1.

Since c_S=sum_{b in B} k_b>=22-beta and each k_b<=3, any selected five B labels have

    sum_selected k_b >= c_S-15 >= 7-beta.

Hence, for each exact-129 color, its at least five no-S components supply at least 7-beta hub-row-hit incidences, as well as at least three total shell-row hits per component. There are at least eight exact-129 colors because the E408 residual excess is three. Across different colors, two monochromatic K5 components can share at most one vertex: sharing two vertices would assign their common edge two different colors. Within one color the ten components are disjoint.

This is the exact cross-color witness-packing contract now available for Q33. It must be used without assuming the Q sets coincide, and without treating repeated shell-row hits across different colors as distinct target edges.

## 6. Capacity audit: what the counting does and does not close

For q in H, the number of non-target edges incident to q inside the 61-vertex residual is

    60-d_F(q) <= 47.

Each time q belongs to one of the K5 components above, it has four incident edges of that component's color inside R. These edge sets are disjoint across different colors, so q can belong to at most floor((60-d_F(q))/4)<=11 such components.

The present lower bound is 40 four-sets across at least eight exact-129 colors, with pairwise intersections at most one and each set carrying the prescribed hub-row hits. The elementary capacity upper bound of 11 memberships per core vertex is too weak by itself (40*4=160 memberships versus at most 47*11=517). Likewise, 8(7-beta) hit incidences do not exceed the crude capacity 11*sum_{a in S}t_a. **No contradiction is claimed from these scalar bounds.**

## 7. Exact remaining theorem target

The highest-value next lemma is a *labelled witness-packing incompatibility theorem* for the same 284-edge H:

- the five E407 templates: ten regular B rows with k_b<=3, each carrying an independent-4 witness Q_b in H_b, with the row-cover conditions above; or
- E408 Q33: at least five pairwise disjoint no-S K5 witness sets per exact-129 color, at least eight exact-129 colors, cross-color intersections at most one, and the row-hit budget 7-beta per color.

It must exploit the 284-edge / four-excess degree structure and the actual adjacency graph H, not merely sum the scalar incidences. Until this theorem is proved, all five E407 templates and E408 Q32/Q33 remain OPEN.
