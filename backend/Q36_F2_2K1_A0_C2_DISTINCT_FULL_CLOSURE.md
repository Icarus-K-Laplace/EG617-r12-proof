# q36 f=2, 2K1 far, a_F=0 — full closure of c=2 distinct d2 supports

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, inherited D14, common-S row closure, and `alpha(F)<=4`.

This leaves only the repeated-support c=2 star terminal.

## 1. Setup

Let C={y1,y2} and suppose their d2 supports D1,D2 are distinct. By d2 rigidity they are disjoint and satisfy

`e_H(D1,D2)<=1`.

Let X be the nine decorated shell vertices, `nu=e_M(X)`. The decoration floor gives `nu<=4`.

For a support Di put

`m_i=1-e_H(Di)`

and `k_i=e_F(Di,X)`.

The exact d2 defect gives `kappa(Di)+m_i<=1`.

The 14-point set `{p} union C union X union Di` gives, by D14,

`k_i<=nu+m_i`.                                             (1)

## 2. Each Di is a target K2

Suppose `m_i=1`, so the two endpoints of Di are target-nonadjacent.

The far pair F={a,b} is target-nonadjacent and target-anticomplete to X and Di. If some x in X were target-nonadjacent to both endpoints of Di, then

`{a,b} union Di union {x}`

would be an independent5-set.

Hence every x in X must meet Di, so `k_i>=9`. But (1) gives

`k_i<=nu+1<=5`,

contradiction.

Thus

> `H[Di]=K2` and `m_i=0` for i=1,2.                         (2)

Consequently `k_i<=nu`.

## 3. Every support endpoint must cover M[X]

Fix d in Di. If an M[X]-edge x1x2 had both endpoints target-nonadjacent to d, then

`{a,b,d,x1,x2}`

would be independent5. Therefore `N_X(d)` is a vertex cover of M[X].

If tau is the vertex-cover number of M[X], both endpoints of Di have at least tau neighbours in X, so

`k_i>=2tau`.                                                (3)

Because nu>0, tau>=1.

Combining (2)--(3),

`2tau<=nu<=4`.                                              (4)

Thus nu=1 is already impossible.

## 4. A cross-nonedge plus an uncovered X-vertex gives the contradiction

Since `e_H(D1,D2)<=1`, among the four cross pairs there exists a target-nonedge `d1d2` with `d_i in D_i`.

We show that `N_X(d1) union N_X(d2)` cannot cover X.

For nu=2 or3, (4) forces tau=1. Each support has total X-incidence `k_i<=nu`, and its two endpoints each have at least one X-neighbour. Hence any single endpoint has at most `nu-1<=2` neighbours in X. Therefore the chosen pair covers at most4 of the nine X-vertices.

For nu=4:

- if tau=2, every endpoint uses at least two X-neighbours and `k_i<=4`, so every endpoint has exactly two;
- if tau=1, every endpoint uses at least one and `k_i<=4`, so every endpoint has at most three.

Thus in all nu=4 cases the chosen pair covers at most6 vertices of X.

Hence there exists x in X target-nonadjacent to both d1 and d2.

Since the far pair is target-anticomplete to X and to both supports, the five vertices

`{a,b,d1,d2,x}`

are pairwise target-nonadjacent. This contradicts `alpha(F)<=4`.

## 5. Conclusion

No c=2 state with two distinct d2 supports exists:

> c=2 distinct-support branch is EMPTY.

Therefore the only c=2 survivor is the repeated-support `K1,4` missing-star terminal in `Q36_F2_2K1_A0_C2_REPEATED_STAR_REDUCTION.md`.