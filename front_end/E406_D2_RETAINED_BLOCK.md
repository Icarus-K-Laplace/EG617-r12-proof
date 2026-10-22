# E406 d=2 final-rise retained-block theorem

Status: `PROVED` for the reduction below. This does not close d=2 or E406.

Assume the E406 final-rise contract

`q_p=30 -> q_y=31`

from `E406_Q31_COEXISTENCE_REDUCTION.md`, with `d_M(y)=2`. Use the notation of `E406_FINAL_RISE_NORMAL_FORMS.md`.

Let

- `S={s1,s2}` be the old missing-neighbour pair of y;
- `D={u1,u2}=N_C(y)` be the exchanged core pair;
- `T=A\(S union {y})`, so `|T|=10`;
- `e=e_M(T)`;
- `h=G_T`;
- `e_S=e_R(S)` and `e_D=e_C(D)`, each in `{0,1}`;
- `epsilon'_S=sum_(s in S)(d_C'(s)-12)`;
- `e_SD=e_R(S,D)`.

## 1. The retained-block charge is at most8

The exact forward/reverse exchange identities specialize to

`e+h = 7 + e_S - epsilon'_S - e_SD`.   (D2-1)

The 12-set `{p,y} union T` is `K12` with exactly e missing internal T-edges. Since `omega(R)<=11`, `e>=1`. Therefore

`1 <= e+h <= 8`.   (D2-2)

In particular

`e<=8`, `h<=8-e`.

Hence at least

`10-h >= e+2`

vertices of T are undecorated degree-13 vertices in BOTH the q30 and q31 shell views.

## 2. Exact S-T and D-T target-edge budgets

Let

`A=e_R(S,T)`, `B=e_R(D,T)`.

The old q30 shell has missing-edge count

`z = 2 + (1-e_S) + (20-A) + e
   = 23-e_S-A+e`,

so its decoration sum is

`G = 30-z = 7+e_S+A-e`.

Since `G<=8`,

`A <= 1+e-e_S`.   (D2-3)

The new q31 shell similarly has

`z' = 2 + (1-e_D) + (20-B) + e
    = 23-e_D-B+e`,

hence

`G' = 31-z' = 8+e_D+B-e`.

Since `G'<=9`,

`B <= 1+e-e_D`.   (D2-4)

There is also a vertexwise form. The 12-set

`X={p,y} union T`

contains `66-e` target edges. The hereditary 13-point cap is67, so every outside vertex has at most `e+1` target neighbours in X.

A vertex of S is adjacent to p and not y, hence has at most e target neighbours in T. A vertex of D is adjacent to y and not p, hence also has at most e target neighbours in T.

Thus each individual S- or D-vertex has T-degree at most e.

## 3. Joint old/new extreme-degree restriction on retained regular vertices

Take an undecorated `t in T`. Put

- `r_t=d_{M[T]}(t)`;
- `a_t=d_R(t,S)`;
- `b_t=d_R(t,D)`.

Its old and new shell missing degrees are

`d_old(t)=r_t + (2-a_t)`,

`d_new(t)=r_t + (2-b_t)`.

Both shell views have q in `{30,31}` and 47-core minimum degree at least12. Therefore the E406 extreme-degree theorem applies in both views:

`d_old(t),d_new(t) in {0,1,2,3,10,11,12}`.

Since `0<=r_t<=8`, this forces

`r_t in {0,1,2,3,8}`.   (D2-5)

Moreover:

- if `r_t=3`, then necessarily `a_t=b_t=2`; t is target-complete to both S and D;
- if `r_t=2`, then `a_t>=1` and `b_t>=1`;
- if `r_t=8`, then necessarily `a_t=b_t=0`; t is target-anticomplete to both S and D.

There are no undecorated T-vertices of internal missing degree4,5,6,7.

Writing `n_i` for the number of undecorated T-vertices with `r_t=i`, the cross-edge budgets (D2-3)--(D2-4) give the useful aggregate inequality

`2 n_2 + 4 n_3 <= A+B <= 2+2e-e_S-e_D`.   (D2-6)

## 4. Interpretation

The d=2 final-rise problem is now a finite joint-labelled 10-vertex deficit graph problem:

- the retained graph M[T] has only 1--8 edges;
- it has at least e+2 undecorated vertices;
- every undecorated vertex has M[T]-degree only 0,1,2,3 or8;
- degree3 vertices must be complete to both exchanged pairs S,D;
- degree8 vertices must be anticomplete to both pairs;
- the total S-T and D-T target incidences satisfy the sharp budgets above.

These are necessary structural conditions, not an existence classification.

The next useful step is not to enumerate arbitrary 10-vertex graphs. It is to classify the possible low-edge deficit quotients under (D2-5)--(D2-6), then apply the exact two-row support identities to the surviving quotient families.