# E405 full closure — canonical replay

Status: `PROVED EMPTY` under the explicit T61 hereditary-cap parent contract.

This file independently reconstructs the proof body supplied in `T61_H13_V7/E405_CLOSURE.md`. It is not merely a source-result ledger.

## Parent contract

Assume a 61-vertex graph `R` with

- `e(R)=405`;
- `delta(R)>=13`;
- `alpha(R)<=5`;
- `omega(R)<=11`;
- all inherited density caps `D(n)`.

For a degree-13 pivot p use the standard 13-shell / 47-core decomposition and shell charge q.

The universal 47-core floor gives

`q<=30`.

We prove that every such parent has a pivot of charge at least31, contradiction.

## 1. No induced 36-point alpha<=3 subgraph occurs inside the parent

Suppose `H` is an induced 36-vertex subgraph with `alpha(H)<=3`.

The retained lower-order seeds give `delta(H)>=13`: first `R(2,24)` exclusion yields minimum degree at least12, and a degree-12 vertex would leave a 35-point induced object with minimum degree11, contradicting the generic `R(3,35)` minimum-degree12 theorem.

Hence

`e(H)>=234`.

The inherited cap is `D(36)=234`, so H is exactly 13-regular.

For every outside vertex x, `D(37)=237` implies

`|N_R(x) intersect H|<=3`.

There are 25 outside vertices. If three outside vertices were independent, their H-neighbourhood union would have size at most9. The remaining at least27 vertices of H contain an independent triple; otherwise any 24-subset would contradict the `R(2,24)` exclusion. The two triples would form an independent6-set in R.

Thus the outside 25-set has independence number at most2, which itself contains a forbidden 24-point `R(2,24)` object. Contradiction.

Therefore no such H exists.

## 2. Every actual 47-core has minimum degree at least11

Let C be the 47-core of any degree-13 pivot. If some vertex had core degree at most10, its core nonneighbourhood would contain at least36 vertices with independence number at most3. This contradicts Section1.

Hence every genuine 47-core satisfies

`delta(C)>=11`.

No edge-count restriction is required for this statement.

## 3. q25/q26 promote to q>=27 using only delta(C)>=11

Let p have q in `{25,26}`. For a regular shell vertex y, with missing degree d and missing neighbourhood S, write the exact repivot formula about the degree-11 baseline as

`q_y=d(12-d)+rho+h11+kappa+b`,

where all correction terms are nonnegative.

Assume every regular repivot has q_y<=26.

### Triangle channel

Fix a missing triangle T and let B be the other ten shell vertices. The exact triangle identity gives

`e_M(B)+G_B<=q-21`.

An M-edge inside B would have endpoint row-weight sum at most

`5+e_M(B)+G_B<=q-16<=10`,

contradicting the inherited missing-edge lower bound11. Hence B is M-independent.

The T--B cross count is 19 or20. Every triangle vertex must meet an undecorated degree-2 B vertex; otherwise the decoration budget makes every possible incident missing edge violate the edge-row lower bound, and one obtains an M-independent11-set.

Thus all three triangle weights are at least9. For an undecorated degree-2 B vertex y, its two missing neighbours lie on the triangle and

`t(S)-e_M(S)<=q-7`.

The repivot inequality gives

`q_y>=q+20-(q-7)=27`,

contradiction.

### Triangle-free channel

A 4-matching would force q>=28, so the missing graph has matching number3. A shortest odd-cycle analysis excludes nonbipartite graphs; hence M is bipartite.

By Konig there is a size-3 cover X and an independent 10-side Y.

A regular degree-3 vertex of Y immediately repivots to q>=27. If a regular degree-2 vertex y has cover neighbours i,j and k is the third cover vertex, the assumption q_y<=26 implies the two-neighbour charge is large, forcing

`t_k<=8-G_Y`.

But alpha(M)<=10 forces k to meet some b in Y, while

`t_b<=3+G_Y`.

Then `t_k+t_b<=11`, with equality forcing b to meet all three cover vertices and k adjacent to both i,j, creating a missing triangle, contradiction.

Therefore regular Y-vertices have degree at most1. The cross-edge count then has incompatible upper and lower bounds for q25 or q26, even after spending the full decoration budget.

Hence every q25/q26 pivot has a regular repivot with q>=27.

## 4. High-low cut forces a pivot with G>=2

Let L be the degree-13 vertices and H the positive-excess vertices, with

`Xi=sum_H(d_R(v)-13)=2E-61*13`.

For E405, `Xi=17`.

More generally for `17<=Xi<=23`, suppose every regular vertex had at most one high neighbour. If a high vertex has excess at least2 it has no regular neighbour, forcing many high vertices; if all excesses are1 then `|H|=Xi`. In either case

`16<=h=|H|<=23`.

Exact cut counting and the inherited cap on R[H] give

`e(H,L)=13h+Xi-2e(H)>=14h-2D(h)`.

The assumption that every regular vertex has at most one high neighbour gives

`e(H,L)<=61-h`.

Thus

`15h-2D(h)<=61`.

But for 16<=h<=23 the left side equals

`97-(h-19)^2>=81`,

contradiction.

Therefore some regular pivot has shell decoration total `G>=2`.

## 5. Maximum pivot charge is at least27

Let Q be the maximum q among degree-13 pivots. Such pivots exist since the average degree is below14.

Assume Q<=26. Choose the regular pivot from Section4 with G>=2. Since z>=22,

`q>=24`.

The pure `(q,z,G)=(24,22,2)` shell is excluded by the existing energy-independent q24 shell theorem. If q is25 or26, Section3 produces a regular repivot with q>=27, contradicting maximality.

Therefore

`Q>=27`.

## 6. Eliminate Q=27,28,29

At E405,

`e(C)=405-91-Q=314-Q`.

For Q in `{27,28,29}`, the core has at most287 edges and therefore the minimum-degree12 / strong row interface applies. Also

`G<=Q-22<=7`.

The uniform q<=29 hereditary shell theorem then supplies a regular repivot with charge at least30, contradicting maximality of Q.

Thus Q cannot be27,28,29.

## 7. Eliminate Q=30

The only remaining possibility is Q=30.

Apply the independently reconstructed theorem

`front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md`.

Every q30 pivot reaches a degree-13 pivot with q>=31 within at most two regular repivots.

This contradicts the universal E405 ceiling Q<=30.

Therefore no E405 parent exists.

> **T61(E405)=empty.**

## Independence from later work

This closure does not use E406, E407/E408, E332, or E333--E340. The only package-derived ingredient formerly requiring replay was the q30 hereditary theorem; it is now independently reconstructed in the repository.
