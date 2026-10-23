# K4,9 G=2 split residual — singleton-support closure

Status: `PROVED` under the canonical split-residual contract from `K49_G2_SPLIT_TWO_SUPPORT_B0.md`.

This file eliminates the multiplicity partition `8+1` for the two distinct Y-supports. It closes no full edge layer by itself.

## 1. Two-support notation

Let the nine Y-rows use exactly two disjoint 4-point supports R,S in L, with multiplicities a,b and `a+b=9`.

Assume, for contradiction, that one support is singleton. Relabel so

`a=8`, `b=1`.

For a repeated d=4 support at a lexicographically maximal q=38 pivot, all four inserted support vertices are globally decorated, so plateau equality q=38 would increase tau. Hence its repivot charge is at most37. The exact d=4 defect budget therefore gives

`kappa(R)+m(R)+c_R <= 1`,

where

- `m(R)=6-e_H(R)`;
- `c_R=|R intersect P|+|R intersect Q|`.

Because R is complete to an 8-clique of Y-vertices, H[R] cannot be K4: otherwise those eight Y-vertices together with R form a target K12. Consequently

`m(R)=1`, `kappa(R)=0`, `c_R=0`,

so H[R] is exactly K4 minus one edge.

The two decorated size10 rows P,Q have twenty incidences total. The outside set `W=L\(R union S)` has size9 and can supply at most18. Hence `c_R+c_S>=2`. Since `c_R=0`, q-maximality of the singleton support forces

`c_S=2`, `kappa(S)=0`, `m(S)=0`.

Thus H[S]=K4. The common-S row-closure theorem gives

`e_H(R,S)=0`.

Moreover every vertex of W belongs to both P and Q, while the two remaining P/Q incidences lie in S.

## 2. The two S incidences must be split 1+1

Let z be the unique Y-vertex whose core row is S.

Repivot at z. Its new shell is

`{p} union (Y\{z}) union S`.

The first nine vertices `{p} union (Y\{z})` form a target K9, S is a target K4, and there are no target cross edges between these blocks. Therefore the new missing shell is again K4,9 and q=38.

Its total decoration on the four-side S is exactly the two P/Q incidences counted by `c_S=2`.

The already-proved K4,9 plateau reduction eliminates concentration of both decoration units on one four-side vertex. Hence the two incidences are on two distinct vertices of S.

Call these decorated vertices `sP,sQ`; call the other two regular vertices `s1,s2`.

## 3. The two new regular supports are exactly D1 and D2

In the z-view, s1 and s2 are the two regular four-side plateau pivots. Their supports are pure K9s of globally regular vertices.

Consider such a regular vertex s in S. In the old 211-core H,

- s has internal degree3 inside S;
- s has no neighbours in R because `e_H(R,S)=0`;
- s is not in P or Q, so it has no target neighbour among the old decorated X-vertices;
- its old core degree is12.

Thus its old external H-neighbourhood outside S has size9.

By plateau maximality this size9 support consists entirely of globally regular vertices. Every vertex of W is globally decorated because W lies in both P and Q. Therefore the support avoids W.

It also avoids R. Hence it lies in `D1 union D2`.

But D1 and D2 are anticomplete pure K9s. A target K9 contained in their union must therefore equal one whole block. The two regular supports are disjoint, so after relabelling

`N_H(s1)\S = D1`,
`N_H(s2)\S = D2`.                                         (1)

In particular s1 is anticomplete to `D2 union W`, and s2 is anticomplete to `D1 union W`.

The same plateau-row disjointness also forces the two decorated S vertices to avoid D1 and D2. Since each has old core degree12, internal S-degree3, and no R-neighbours, it follows that

`sP` and `sQ` are complete to W.                             (2)

## 4. Independent-four coverage contradiction

Let r1,r2 be the unique nonadjacent pair in the K4-minus-edge graph H[R]. Each has internal R-degree2. Because `kappa(R)=0`, both have H-degree12, hence each has exactly10 H-neighbours outside R.

We show that their combined neighbourhood must cover all27 vertices of

`D1 union D2 union W`.

Take any `d in D1`. By (1), s2 is nonadjacent to d. Also R is anticomplete to S. If d were nonadjacent to both r1 and r2, then

`{r1,r2,s2,d}`

would be an independent4-set in H, contradicting `alpha(H)<=3`. Thus every vertex of D1 is adjacent to r1 or r2.

The same argument with s1 covers D2.

For any `w in W`, s1 is nonadjacent to w by (1). Again, if w missed both r1 and r2 then

`{r1,r2,s1,w}`

would be independent. Hence every vertex of W is adjacent to r1 or r2.

Therefore

`N_H(r1) union N_H(r2)`

contains all27 vertices of `D1 union D2 union W`.

But r1 and r2 each have only10 neighbours outside R, so together they have at most20 such neighbour incidences. They cannot cover27 distinct vertices. Contradiction.

Hence the `8+1` multiplicity partition is impossible.

## 5. Surviving multiplicities

The two distinct Y-supports must both be repeated. Up to exchanging them, only

- `2+7`;
- `3+6`;
- `4+5`

remain.

This is the new residual frontier for the final K4,9 split plateau.