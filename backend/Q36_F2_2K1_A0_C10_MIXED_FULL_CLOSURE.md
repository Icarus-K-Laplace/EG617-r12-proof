# q36 f=2, 2K1 far, a_F=0 — full closure of the c=10 mixed d2/d3 sector

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, row closure, CORE211, inherited D14, and `alpha(H[R])<=2`.

Together with `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`, this closes the entire c=10 branch.

## 1. Setup

Let c=10. Then the decorated shell set is X={x}. Let n2 be the number of d2 low owners and n3=10-n2 the number of d3 low owners.

The 11-point remainder R satisfies

`alpha(H[R])<=2`

and CORE211 gives

`sum_(v in R) kappa_v<=2`.

The ten low owners form a target K10. Together with the original pivot p they form a target K11.

For v in R let lambda_v be the number of low owners whose core support contains v.

## 2. A d2 support creates a large regular clique

Assume n2>=1 and choose one d2 support D={u,v}.

The exact d2 formula in the 2K1,a_F=0 branch gives

`q_D=35+kappa(D)+m(D)<=36`,

so

`kappa(D)+m(D)<=1`.                                        (1)

For every regular w in R\D, row closure for the d2 repivot has no shell contribution because its missing set is exactly the far pair F and every R-vertex is target-anticomplete to F. Hence

`e_H(w,D)<=kappa_w=0`.                                     (2)

Thus every regular vertex outside D is target-anticomplete to D.

The pair D itself must be a target K2. If uv were a target nonedge, then any regular w outside D would make {u,v,w} an independent triple in H[R], contradicting alpha(H[R])<=2.

Therefore

`H[D]=K2`, `m(D)=0`, `kappa(D)<=1`.                        (3)

Let Q be the set of regular vertices in R\D. Since total core excess is at most2, at most two vertices of R\D are nonregular, so

`|Q|>=7`.                                                   (4)

Moreover Q is a target clique. Indeed if q1,q2 in Q were target-nonadjacent, then either endpoint of D together with q1,q2 would form an independent triple because D is target-anticomplete to Q by (2).

Hence

> Q is a target clique of size at least7.                  (5)

## 3. Every d3 support uses at least two vertices outside Q

Let T be any d3 support. Suppose it contained two vertices q1,q2 in Q.

Since |Q|>=7, choose q in Q\T. The d3 missing set is F union {x}. The regular vertex q is target-anticomplete to F, so row closure gives

`e_H(q,T)<=e_F(q,x)<=1`.                                   (6)

But Q is a target clique and q1,q2 are both in T, so

`e_H(q,T)>=2`,

contradiction.

Therefore

> every d3 support meets Q in at most one vertex.          (7)

Put

`B=R\Q`.

By construction B contains D and at most two nonregular vertices outside D, so

`|B|<=4`.                                                   (8)

Every d3 support contains at least two vertices of B.

## 4. The K11/D14 incidence cap

Because {p} union C is a target K11, for every triple T subset R the 14-point induced subgraph

`{p} union C union T`

contains

- 55 target edges inside the K11;
- `sum_(v in T) lambda_v` low-clique-to-core edges;
- `e_H(T)` target edges inside T.

The inherited D14 cap therefore gives

`55 + lambda(T) + e_H(T) <=69`,

so

`lambda(T)+e_H(T)<=14`.                                    (9)

Since alpha(H[R])<=2, every triple spans at least one target edge. Hence for every three vertices of R,

> `lambda(T)<=13`.                                         (10)

Equivalently, the three largest lambda-values in R have sum at most13.

## 5. Incidence lower bound on B

Every d3 owner contributes at least two support incidences to B by (7).

We distinguish the possible number n2 of d2 owners.

### n2=1

The chosen d2 support contributes two incidences to B, while the nine d3 rows contribute at least18. Thus

`lambda(B)>=20`.

### n2=2

At least the chosen d2 support contributes two incidences to B, and the eight d3 rows contribute at least16. Thus

`lambda(B)>=18`.

### n2>=3

By the d2 rigidity theorem in `Q36_F2_2K1_A0_REDUCTION.md`, all d2 rows share one repeated pure K2 support D. The multiplicity bound

`3n2<=c+nu+2`

with c=10 and nu=0 gives n2<=4.

For n2=3 or4, the repeated D contributes 2n2 incidences to B and the d3 rows contribute at least 2(10-n2). Therefore

`lambda(B)>=2n2+2(10-n2)=20`.

Consequently in every mixed c=10 branch,

> `lambda(B)>=18` while `|B|<=4`.                           (11)

For four nonnegative integers with total at least18, the sum of the largest three is at least14. Therefore some triple of vertices in B has lambda-sum at least14, contradicting the universal bound (10).

## 6. Conclusion

No c=10 mixed d2/d3 candidate exists:

> `c=10, n2>=1` is EMPTY.

Combined with `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`, which closes n2=0, the entire q36 f=2, 2K1, a_F=0, c=10 layer is empty.