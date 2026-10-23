# Global D2 Transversal Sharp Capacity Theorem

Status: `PROVED_ANALYTIC`.

This strengthens `GLOBAL_D2_TRANSVERSAL_CAPACITY_THEOREM.md`.

## Theorem

Let H satisfy `alpha(H)<=3`. Let

`D_1,...,D_N`

be pairwise disjoint two-point vertex sets such that

`e_H(D_i,D_j)<=1`

for all `i!=j`.

Then

> **N<=6.**

The N>=8 part follows from `GLOBAL_D2_TRANSVERSAL_CAPACITY_THEOREM.md`; only the former N=7 boundary remains to be eliminated.

## 1. N=7 transversal lower and upper bounds

Choose independently one endpoint from each D_i. For the resulting seven-point transversal T,

`alpha(H[T])<=3`.

Hence the complement of H[T] is K4-free. Turan gives

`e_H(T)>=C(7,2)-ex(7,K4)=21-16=5`.                           (1)

Let m be the number of block pairs carrying a target cross-edge. Since every pair carries at most one such edge,

`E[e_H(T)]=m/4<=21/4`.                                      (2)

Equation (1) implies the expectation is at least5, so

`m>=20`.                                                      (3)

## 2. Twenty cross-edge pairs are impossible

If m=20, then (1)--(2) force

`E[e_H(T)]=5`

while every transversal has at least5 edges. Thus every transversal has exactly5 edges.

Write the endpoint choice in block i as a bit x_i. The transversal edge count is a degree-two Boolean-cube polynomial

`f(x)=sum_(ij carrying an edge) 1[(x_i,x_j)=(a_ij,b_ij)]`.

If f were constant, take the mixed discrete difference in any pair i,j which carries an edge. Every summand except the unique ij-term vanishes; the ij indicator has nonzero mixed difference. Contradiction.

Therefore

> m cannot equal20.                                          (4)

Hence m=21: every pair of blocks carries exactly one target cross-edge.

## 3. The seven-block Boolean polynomial

Now

`E[f]=21/4=5.25`.

Since f is integer-valued and f>=5 everywhere, put

`h=f-5`.

Then h is a nonnegative integer-valued multilinear polynomial of degree at most2 on `{+1,-1}^7`, and

`E[h]=1/4`.

Therefore

`sum_x h(x)=2^7/4=32`.                                      (5)

Since every positive value of h is at least1,

`|supp(h)|<=32`.                                             (6)

## 4. Boolean-cube support lemma

We use the standard elementary fact:

> If a nonzero multilinear polynomial P on `{+1,-1}^n` has degree at most d, then P is nonzero on at least `2^(n-d)` cube points.

Proof is by induction on n. Write

`P(x',x_n)=A(x')+x_n B(x')`.

If B is identically zero, the support of P is twice the support of A and induction gives the result. If B is nonzero, then for every x' with B(x') nonzero, at least one of `A(x')+B(x')` and `A(x')-B(x')` is nonzero. Induction applied to B, whose degree is at most d-1, gives at least

`2^((n-1)-(d-1))=2^(n-d)`

such x'.

Applying this to h with n=7,d=2 gives

`|supp(h)|>=32`.                                             (7)

Together with (6), equality holds:

`|supp(h)|=32`.

Equation (5) then forces

> h(x) is exactly 0 or1 for every cube point.                 (8)

Thus

`E[h^2]=E[h]=1/4`.                                          (9)

## 5. Fourier-energy contradiction

Use the `+1/-1` endpoint coordinates. A single block-pair edge indicator has expansion

`1[(x_i,x_j)=(a,b)]`
` = (1+s_i x_i)(1+s_j x_j)/4`

for signs `s_i,s_j in {+1,-1}`.

Therefore its Fourier coefficient on the quadratic character `x_i x_j` has absolute value exactly1/4.

Because every one of the 21 block pairs carries exactly one edge, h (equivalently f) has 21 distinct quadratic Fourier coefficients, each of squared magnitude

`1/16`.

Parseval therefore gives

`E[h^2] >= 21/16`.                                          (10)

But (9) says `E[h^2]=1/4`. Contradiction.

Hence N=7 is impossible.

Combined with the preceding theorem:

> **N<=6.**                                                   (11)

## 6. Backend consequence

Any common two-point support regime that has already been reduced to

- pairwise disjoint support blocks;
- at most one target cross-edge between any two blocks;

cannot contain seven or more support classes, regardless of charge witnesses, CORE211 excess, or the E-layer label.

Thus every forced lower bound 7,8,9 in such a regime is eliminated by one witness-free theorem. The first unresolved numerical regime is six blocks, not seven.

This is strictly stronger than the earlier zero/charge-one witness capacities and is a natural reusable component of the Global Support-Compatibility theorem.

## 7. Parameterized interpretation

The proof is an instance of a general block-transversal principle:

- block size b=2;
- pair cross-density at most1/4;
- global independence number3;
- Turan lower bound on every transversal;
- Boolean-cube rigidity at the expectation boundary.

The argument does not use 35, 211, or the r=12 edge-layer numbering.