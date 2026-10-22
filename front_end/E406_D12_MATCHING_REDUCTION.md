# E406 d=12 final rise: matching-number reduction

Status: `PROVED` reduction. The d12 class remains open.

Consider a q30 -> q31 d12 final rise. Use the notation of `E406_FINAL_RISE_NORMAL_FORMS.md`.

The old q30 shell is `{y} union S`, with `|S|=12` and y missing-adjacent to every vertex of S. The new q31 shell is `{p} union D`, with `|D|=12` and p missing-adjacent to every vertex of D.

## 1. Old S-block weighted complement

Let

`K_S = complement of R[S]`,
`m=e(K_S)`,
`rho_v=d_{K_S}(v)`.

For `v in S`, let `g_v` be its old-shell decoration and put

`h_v=rho_v+g_v`.

The old shell charge is

`30 = 12 + m + G`,

so

`m+G=18`.

Hence

`sum_{v in S} h_v = 2m+G = m+18`.      (S-WEIGHT)

For every edge uv of K_S, the two shell row weights are

`t_u=1+h_u`, `t_v=1+h_v`.

The E406 PAIR-13 row-union lemma gives

`t_u+t_v>=13`,

therefore

`h_u+h_v>=11`.      (S-EDGE)

### Matching bound

If K_S contained a matching of size4, summing (S-EDGE) over the four disjoint edges would require at least44 units of h-weight on eight distinct vertices. But by (S-WEIGHT),

`sum h = m+18 <=36`,

since `m<=18`.

Therefore

`nu(K_S)<=3`.

The case `nu(K_S)=1` is also impossible. A simple graph with matching number1 is a star or a triangle. Here the 13-point cap already gives `m>=11`, so the only possibility would be the spanning star `K_{1,11}`. Its eleven leaves are pairwise target-adjacent in R[S]; together with the old pivot p, which is target-adjacent to every shell vertex, they form a K12. Contradiction.

Thus

`nu(K_S) in {2,3}`.      (S-MATCH)

## 2. Three-matching forces regular d1 shell vertices

Assume `nu(K_S)=3` and fix a maximum matching. Its six endpoints carry at least33 total h-weight by (S-EDGE).

The six unmatched vertices therefore carry total h-weight at most

`(m+18)-33 = m-15 <=3`.

Every nonzero h is a positive integer. Hence at least three unmatched vertices satisfy h=0.

For such a vertex s,

`rho_s=0`, `g_s=0`.

So s is a regular K_S-isolate. In the old q30 shell it is missing only to y and has row weight1.

The local d12 bookkeeping gives, vertexwise,

`g_s = epsilon'_{s} + e_R(s,D)`.

Thus h=0 implies

`epsilon'_s=0`, `e_R(s,D)=0`.

Let v be the unique old-core neighbour of s. Since s has no D-neighbour, `v notin D`.

Repivoting at s removes v from the old 285-edge core and inserts y. Because y has exactly twelve old-core neighbours, all in D, and v is outside D, y enters with degree12. Therefore

`q_s-30 = epsilon_C(v)`.

Global maximality gives `q_s<=31`, so

`epsilon_C(v) in {0,1}`.

Hence every regular K-isolate is exactly one of:

- a q30 d1 plateau supported by an old degree12 core vertex;
- a q31 d1 final-rise pivot supported by an old degree13 core vertex.

Thus the `nu=3` d12 branch automatically generates at least three one-swap pivots of this exact type.

## 3. New D-block

Apply the same argument in the q31 shell. Let

`K_D = complement of C[D]`,
`m_D=e(K_D)`,
`g'_u` the new-shell decorations,
`h'_u=d_{K_D}(u)+g'_u`.

The q31 charge gives

`m_D+G'=19`,

and therefore

`sum_{u in D} h'_u = 2m_D+G' = m_D+19 <=38`.

Every K_D-edge again satisfies

`h'_u+h'_v>=11`.

A matching of size4 would require44 total weight, impossible. Matching number1 again forces the spanning star K1,11 (because m_D>=11), whose eleven target-clique leaves together with pivot y form a K12.

Therefore

`nu(K_D) in {2,3}`.      (D-MATCH)

If `nu(K_D)=3`, the six unmatched vertices have total h'-weight at most

`m_D+19-33 = m_D-14`.

In particular this produces many zero-weight regular isolates whenever m_D is near its lower range; these are q31 one-swap plateau vertices with degree12 support in the common core.

## 4. Consequence

A d12 final rise is no longer an arbitrary pair of dense 12-blocks. Both complement blocks have matching number exactly2 or3:

`nu(K_S),nu(K_D) in {2,3}`.

Moreover the old-side `nu=3` branch forces at least three exact d1/plateau one-swap pivots. This links the remaining d12 frontier directly to the remaining d1 frontier.