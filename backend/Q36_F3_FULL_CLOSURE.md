# q36 candidate coverage — full closure of the f=3 far layer

Status: `PROVED` under `Q36_F3_FAR_LAYER_REDUCTION.md`, `Q36_F3_K21_TERMINAL_STRENGTHENING.md`, and `Q36_F3_K21_SUPPORT_CLASS_COLLAPSE.md`.

This closes the entire f=3 branch of the q36 low-clique regime.

## 1. Only the K2+K1 terminal remained

The earlier far-layer reduction already eliminated

- far target K3;
- far target 3K1.

The unique residual had far shell `F={a,b,z}` with

- `ab` a target edge;
- z target-nonadjacent to both a,b;
- core rows A,B,Z of sizes11,11,12;
- Z disjoint from A and B;
- `h=|A intersect B| in {10,11}`.

Put

`R=H\(A union B union Z)`.

Then

- `|R|=11` when h=10;
- `|R|=12` when h=11.

Every low-clique support lies in R.

The support-class collapse proves that every hypothetical survivor has exactly two distinct disjoint 3-supports D1,D2 contained in R, with

- each H[D_i] having at least two target edges;
- `kappa(D_i)+m(D_i)<=1`;
- `e_H(D1,D2)<=1`.

The multiplicities no longer matter for the final contradiction.

## 2. The remainder R has independence number at most2

The shell pair a,z is a target nonedge.

By definition R is disjoint from both A=N_H(a) and Z=N_H(z). Hence every vertex of R is target-nonadjacent to both a and z.

If H[R] contained an independent triple, that triple together with `{a,z}` would form an independent5-set in F, contradicting `alpha(F)<=4`.

Therefore

> `alpha(H[R])<=2`.                                        (1)

Mantel in the complement gives

- if |R|=11,
  `e_H(R)>=C(11,2)-floor(11^2/4)=55-30=25`;
- if |R|=12,
  `e_H(R)>=C(12,2)-floor(12^2/4)=66-36=30`.

Thus

> `e_H(R)>=25` for h=10, and `>=30` for h=11.             (2)

## 3. Row closure gives a conflicting upper bound

Every vertex of R is outside the three far core rows A,B,Z. Hence it has no target shell neighbour in F={a,b,z}.

For v in R write `kappa_v=d_H(v)-12`. CORE211 gives

`sum_H kappa_v=2`,

so in particular

`kappa(R)<=2`.                                              (3)

Let

`L=R\(D1 union D2)`.

Then |L| is5 when |R|=11 and6 when |R|=12.

Apply row closure for a low-clique repivot whose support is D_i. For v in L,

`e_H(v,D_i)<=kappa_v+e_F(v,F)=kappa_v`,

because R is target-anticomplete to F. Summing over L,

`e_H(D_i,L)<=kappa(L)`.

Therefore

`e_H(D1,L)+e_H(D2,L)<=2kappa(L)<=4`.                       (4)

Now bound all edges of H[R].

- each D_i contributes at most3 internal edges;
- `e_H(D1,D2)<=1`;
- the two support-to-L cuts contribute at most4 by (4);
- L contributes at most `C(|L|,2)` edges.

Hence

### h=10, |R|=11, |L|=5

`e_H(R)<=3+3+1+4+C(5,2)=21`,

contradicting the lower bound25 in (2).

### h=11, |R|=12, |L|=6

`e_H(R)<=3+3+1+4+C(6,2)=26`,

contradicting the lower bound30 in (2).

Thus the K2+K1 terminal is impossible.

## 4. f=3 conclusion

All three possible far target partitions are now empty:

- K3: closed in `Q36_F3_FAR_LAYER_REDUCTION.md`;
- 3K1: closed there;
- K2+K1: closed above.

Therefore

> no q36 top-channel low-clique survivor has three far/high regular shell vertices.

Equivalently, in the q36 low-clique regime the remaining far count satisfies

`f<=2`.

The shell-poor/core-rich branch remains separate and still requires simultaneous one-spoke stability.