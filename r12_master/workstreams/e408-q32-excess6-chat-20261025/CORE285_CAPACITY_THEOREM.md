# CORE285 capacity theorem — E408 Q32 / excess six

Status: **PROVED_CONDITIONAL necessary-structure theorem** under the registered E408 outer embedding and exact-129 Type-I classification. This theorem is specific to e(H)=285 and total core excess six.

## 1. Contract and notation

Let H be a 47-vertex graph satisfying

\[
e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12.
\]

Then

\[
\sum_{x\in H}(d_H(x)-12)=570-564=6.
\]

For U⊆V(H), write v=|U| and

\[
E_U=\sum_{x\in U}(d_H(x)-12),\qquad 0\le E_U\le6.
\]

Let p_4(n) denote the minimum number of edges in an n-vertex graph with independence number at most four. By Turán's theorem applied to the complement,

\[
p_4(n)=\sum_{j=1}^{4}\binom{a_j}{2},
\]

where the a_j are the four integers ⌊n/4⌋ or ⌈n/4⌉ summing to n.

The seven-block equality system gives eleven non-target colors C with

\[
e_C(R)=129+s_C,\quad s_C\ge0,\quad \sum_Cs_C=3.
\]

Consequently m, the number of exact-129 colors, is in {8,9,10}.

## 2. Witness existence and linearity — no shell split assumed

Fix an exact-129 color C. The registered Type-I equality classification gives ten isolated K5 components in C[R], plus an 11-vertex exceptional gadget consisting of two disjoint 5-cliques and one additional vertex. Thus there are twelve pairwise-disjoint 5-cliques in C[R]: the ten isolated components and the two 5-cliques in the gadget.

Every one of these twelve 5-cliques intersects {p}∪A. Otherwise its five vertices would be independent in target H, contradicting α(H)≤4. There are only fourteen vertices in {p}∪A.

Let x be the exceptional vertex of the 11-point gadget.

- If x∉H, then x consumes one of the fourteen outside vertices without belonging to any of the twelve 5-cliques. The twelve 5-cliques use at most thirteen outside vertices, so their total number of outside vertices beyond the mandatory one per clique is at most one.
- If x∈H, the twelve 5-cliques use at most fourteen outside vertices, so the total excess beyond one per clique is at most two.

It follows in either case that at most two of the ten isolated K5 components contain two or more vertices outside H. Therefore at least eight isolated K5 components have exactly one vertex y∈{p}∪A and four vertices Q⊂H.

Because all edges of each K5 are C-colored, its four core vertices Q form an independent 4-set in H. If y∈A, Q is also anticomplete to y in F. If y=p, this is automatic because N_F(p)=A. Thus each such component supplies a valid independent-4 witness Q⊂H with a shell/pivot label y.

Across distinct isolated components of the same color, the Q sets are disjoint. Across different colors, two Q sets cannot share two vertices: the edge joining those two vertices would be assigned two different colors. Hence the full witness family is pairwise linear.

So every exact-129 color supplies at least eight witnesses, and the total number N satisfies

\[
N\ge8m.
\]

A refinement is available: if the exceptional gadget vertex x lies outside H, that color supplies at least nine witnesses, since the total excess outside vertices among the twelve K5 cliques is then at most one.

This argument does not use M[B]=∅, a d3 split, or any E407/E408 Q33 excess-four statement.

## 3. The exact 285-edge capacity inequality

Let U be the union of the N witness 4-sets, v=|U|, and W=H\\U. Because the witness family is pairwise linear, no pair of vertices occurs in two witnesses. Every witness Q is independent in H, so its six pairs are edges of the complement graph \bar H. Therefore

\[
6N\le e(\bar H[U]).
\]

The degree sum on U is

\[
12v+E_U=2e(H[U])+e_H(U,W).
\]

Using e(H)=e(H[U])+e_H(U,W)+e(H[W]) and eliminating e_H(U,W),

\[
e(H[U])=12v+E_U+e(H[W])-285.
\]

Since α(H[W])≤4, e(H[W])≥p_4(47-v). Hence

\[
\boxed{
6N\le e(\bar H[U])
\le \binom v2-p_4(47-v)-12v+285-E_U.
}
\]

Define

\[
\operatorname{Cap}_{285}(v)=\binom v2-p_4(47-v)-12v+285.
\]

Then the necessary inequality is 6N≤Cap_285(v)-E_U. The constant is 285, not 284; the total excess term is E_U with total budget six.

## 4. Exact integer boundary

The arithmetic values around the support thresholds are:

| v | 47-v | p_4(47-v) | Cap_285(v) |
|---:|---:|---:|---:|
| 27 | 20 | 40 | 272 |
| 28 | 19 | 36 | 291 |
| 29 | 18 | 32 | 311 |
| 30 | 17 | 28 | 332 |
| 31 | 16 | 24 | 354 |
| 32 | 15 | 21 | 376 |
| 33 | 14 | 18 | 399 |
| 34 | 13 | 15 | 423 |
| 35 | 12 | 12 | 448 |
| 36 | 11 | 10 | 473 |
| 37 | 10 | 8 | 499 |

Substituting N≥8m gives:

| Exact-129 colors m | Witness floor N | Required complement edges 6N | Smallest possible v |
|---:|---:|---:|---:|
| 8 | 64 | 384 | 33 |
| 9 | 72 | 432 | 35 |
| 10 | 80 | 480 | 37 |

These thresholds use E_U≥0; positive E_U can only strengthen them. If k of the m exact colors have x outside H, then N≥8m+k. Ignoring the additional subtraction E_U, this forces v≥34 for (m,k)=(8,k≥3), v≥35 for (8,k≥7), v≥36 for (9,k≥3), v≥37 for (9,k≥7), v≥38 for (10,k≥4), and v≥39 for (10,k≥8).

## 5. Exact excess allocation on the support and its complement

Let

\[
s_W=e(H[W])-p_4(47-v)\ge0,\qquad
r_U=e(\bar H[U])-6N\ge0.
\]

Here r_U counts complement edges in U not used by the witness K4s, and s_W is the edge slack over the minimum allowed by α(H[W])≤4. The derivation above gives the exact budget

\[
\boxed{E_U+r_U+s_W=\operatorname{Cap}_{285}(v)-6N.}
\]

The degree excess on W is E_W=6-E_U. Thus the total six-unit core excess is allocated exactly between U and W, while the remaining complement-edge capacity is allocated between uncovered pairs inside U and excess edges inside W.

At the minimum witness floors and minimum support sizes, the right-hand sides are 15, 16, and 19 for m=8,9,10 respectively. If more than eight witnesses occur in any exact color, subtract six for every additional witness from the corresponding right-hand side.

## 6. What this theorem does and does not prove

**Proved under the named inputs:** witness existence, pairwise linearity, the 285-edge capacity inequality, the exact integer support floors, and the support/complement excess ledger. The result covers both M[B]=∅ and M[B]≠∅ shell-support cases.

**Not proved:** that any of the surviving support sizes is realizable; that the core adjacency graph exists; that the seven outer blocks can all be completed; or that the original K145 counterexample is impossible. Those remain the next global compatibility problem.
