# CORE285 capacity theorem — E408 Q32 / excess six

Status: **PROVED_CONDITIONAL necessary-structure theorem** under the registered E408 outer embedding and Kang–Pikhurko Type-I equality classification. This theorem uses e(H)=285 and total core excess six throughout.

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

Fix an exact-129 color C. The registered Type-I equality classification gives ten isolated K5 components in C[R], plus an 11-vertex exceptional gadget consisting of two disjoint 5-cliques and one additional vertex. Thus C[R] contains **twelve pairwise-disjoint 5-cliques**: the ten isolated components and the two 5-cliques in the gadget. The latter two are cliques even though they are not isolated components.

Every one of these twelve 5-cliques intersects O={p}∪A. Otherwise its five vertices would be independent in target H, contradicting α(H)≤4. Let x be the exceptional vertex of the gadget.

- If x∉H, then x consumes one of the fourteen outside-H vertices without belonging to any of the twelve 5-cliques. The twelve cliques use at most thirteen outside-H vertices, so their total number of outside vertices beyond the mandatory one per clique is at most one. At least eleven of the twelve cliques have exactly one outside-H vertex.
- If x∈H, the twelve cliques use at most fourteen outside-H vertices, so there are at most two extra outside vertices beyond one per clique. At least ten of the twelve cliques have exactly one outside-H vertex.

Therefore every exact-129 color supplies at least ten pairwise-disjoint 4-sets Q⊂H obtained by removing the unique outside-H vertex from one of these 5-cliques. Since the five vertices form a C-clique, Q is independent in target H. If the outside vertex is a∈A, Q is also anticomplete to a in F; if it is p, anticompleteness is automatic because N_F(p)=A.

If x∈H and both extra outside vertices lie in the same 5-clique, that clique has three shell vertices; those three vertices form a triangle in M. In this case eleven of the twelve cliques have exactly one outside-H vertex. Hence **any exact-129 color with x∉H or with a three-shell-vertex K5 supplies at least eleven witnesses**.

Within one color, the witness sets are disjoint. Across different colors, two witness sets cannot share two core vertices, since their common edge would be assigned two colors. Thus the combined witness family is pairwise linear and

\[
\boxed{N\ge10m.}
\]

The witness construction does not assume M[B]=∅, does not assume a d3 shell split, and does not import an excess-four core theorem.

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

Then 6N≤Cap_285(v)-E_U. The constant is 285, not 284; the total excess term is E_U with total budget six.

## 4. Exact integer support boundaries

| v | 47-v | p_4(47-v) | Cap_285(v) |
|---:|---:|---:|---:|
| 37 | 10 | 8 | 499 |
| 38 | 9 | 6 | 526 |
| 39 | 8 | 4 | 554 |
| 40 | 7 | 3 | 582 |
| 41 | 6 | 2 | 611 |
| 42 | 5 | 1 | 641 |
| 43 | 4 | 0 | 672 |
| 44 | 3 | 0 | 703 |

Using only N≥10m, the capacity inequality by itself gives:

| Exact-129 colors m | Witness floor N | Required complement edges 6N | Capacity-only floor on v |
|---:|---:|---:|---:|
| 8 | 80 | 480 | 37 |
| 9 | 90 | 540 | 39 |
| 10 | 100 | 600 | 41 |

There is also a stronger, immediate within-color bound: one exact-129 color already contributes ten disjoint 4-sets, so v≥40. Combining it with the capacity bound gives the preliminary support floors before the triple-pair refinement in §6:

\[
\boxed{v\ge40\text{ if }m=8\text{ or }9;\qquad v\ge41\text{ if }m=10.}
\]

If any exact-129 color supplies eleven witnesses, those eleven sets are disjoint and v≥44. In particular, if v≤43, every exact-129 color supplies exactly ten witnesses; its exceptional vertex x lies in H, and the two extra outside vertices must lie in two different K5 cliques, each with two shell vertices. Those two shell pairs are disjoint edges of M. Their edges have distinct colors across exact colors, so this low-support regime also carries at least 2m distinct, color-labelled edges of M.

## 5. Exact excess allocation on the support and its complement

Let

\[
s_W=e(H[W])-p_4(47-v)\ge0,\qquad
r_U=e(\bar H[U])-6N\ge0.
\]

Here r_U counts complement edges in U not used by witness K4s, and s_W is the edge slack over the minimum allowed by α(H[W])≤4. The exact budget is

\[
\boxed{E_U+r_U+s_W=\operatorname{Cap}_{285}(v)-6N.}
\]

The degree excess on W is E_W=6-E_U. Thus the six-unit core excess is allocated between U and W, while the remaining complement-edge capacity is allocated between uncovered pairs inside U and excess edges inside W.

At the minimum support floors with the minimum witness counts, the boundary budgets are:

| m | v | N | Cap_285(v)-6N | Exact budget |
|---:|---:|---:|---:|---|
| 8 | 40 | 80 | 102 | E_U+r_U+s_W=102 |
| 9 | 40 | 90 | 42 | E_U+r_U+s_W=42 |
| 10 | 41 | 100 | 11 | E_U+r_U+s_W=11 |

### Additional exact normal form at m=10, v=41

Each of the ten exact colors has ten disjoint witness 4-sets covering 40 of the 41 support vertices, leaving exactly one omitted point per color. Let k_u be the number of exact colors whose witness class omits u; then Σ_{u∈U}k_u=10. Let r_u be the number of unused complement edges incident to u, so Σr_u=2r_U. Pair counting gives

\[
d_{H[U]}(u)=10+3k_u-r_u,
\]
\[
d_H(u,W)=2+(d_H(u)-12)-3k_u+r_u\ge0.
\]

The global edge ledger also gives e_H(U,W)=74-E_U-2s_W, while summing the pointwise formula gives e_H(U,W)=52+E_U+2r_U. These are equivalent to E_U+r_U+s_W=11. This is a strict finite terminal form, not a contradiction.

## 6. Low-support triple-pair capacity theorem

The separate file LOW_SUPPORT_TRIPLE_PAIR_CAPACITY.md proves a stronger support floor using the two three-point core parts of the double-shell (K_5) cliques. If (v<44), every exact color has exactly ten one-outside cliques, two double-shell cliques, and (x_C\in H). The two core triples and (x_C) partition (W\dot\cup O_C), where (W=H\setminus U), (|W|=47-v), and (|O_C|=v-40). Every pair of (W)-vertices used by one of these triples is a distinct non-target edge, so the total pair load is at most (inom{|W|}{2}). The exact boundary costs for (v=40,41,42,43) are respectively 6, 4, 2, 1 per color, while the available pair counts are 21, 15, 10, 6. Since there are at least eight exact colors, every boundary is impossible. Thus the global support floor is now **(v\ge44)**, uniformly over both shell-support branches.

At (v=44), (|W|=3). Pair uniqueness further implies at most three colors have (x_C\in O_C), and at least (m-3) colors split the two vertices of (W\setminus\{x_C\}) one per triple. This is a strict normal-form reduction, not closure.

## 7. What this theorem does and does not prove

**Proved under the named inputs:** witness existence, pairwise linearity, the 285-edge capacity inequality, exact integer support floors, the support/complement excess ledger, and the low-support component allocation described above. The result covers both M[B]=∅ and M[B]≠∅ shell-support cases.

**Not proved:** that any surviving support profile is realizable; that the 47-core graph exists; that the seven outer blocks can all be completed; or that the original K145 counterexample is impossible. Those remain the next global compatibility problem.
