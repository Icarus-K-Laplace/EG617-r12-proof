# q36 f=2, 2K1 far, a_F=0 — full closure of the c=7 mixed d2/d3 sector

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, the low-allowance d3 theorems, row closure, CORE211, inherited D14, the all-pivot minimum-degree theorem, and `alpha(H[R])<=2`.

Together with the high-c single-class closure, this closes the entire c=7 branch.

## 1. Setup

Let c=7 and suppose at least one low row has missing degree2. Put n2>=1 and n3=7-n2. The decorated shell set X has size4.

The fixed 11-point remainder R satisfies `alpha(H[R])<=2` and total core excess at most2.

## 2. Two active d3 missing classes are impossible

Suppose two decorated vertices x,z are used by d3 rows and the other two decorated vertices y1,y2 are inactive.

For an active vertex u write

`A_u=n_u+nu_u+g_u-7`.

Since n_x+n_z=n3, the shell ledger is `G=6+n2-nu`, and the missing-edge degree sum over the active pair differs from total nu only by the active-active and inactive-inactive edges. Direct cancellation gives

`A_x+A_z = 1_(xz in M) - 1_(y1y2 in M) - g_y1-g_y2 - 1`.

Because both inactive vertices are decorated, `g_y1+g_y2>=2`, so the right side is at most `1-0-2-1=-2`.

This contradicts nonnegative allowances. Hence all d3 rows use a single active missing vertex x.

Let Y be the three inactive decorated shell vertices.

## 3. Exact inactive K3 equality

Let `nu_Y=e_M(Y)` and `G_Y=sum_(y in Y)g_y`.

The active d3 allowance is

`A=n3+nu_x+g_x-7`.

Since every missing edge of M[X] is either incident with x or lies inside Y,

`nu=nu_x+nu_Y`.

Using `G=6+n2-nu` and `n3=7-n2`, we get the exact identity

`A+G_Y=6-nu_Y`.                                           (1)

The regular/decorated missing-edge inequality for a low owner and x gives `A>=3`.

There are three inactive decorated vertices, so `G_Y>=3`. Hence (1) forces equality throughout:

> `A=3`, `nu_Y=0`, and `G_Y=3`.                            (2)

Thus Y is a target K3 and each y in Y has decoration exactly1.

Consequently

> `{p} union C union Y` is a target K11.                  (3)

## 4. K11/D14 cap and the exceptional block

For v in R let lambda_v be the number of the seven low supports containing v.

For every triple T subset R, the induced 14-point set `{p} union C union Y union T` contains the K11 from (3), the low-to-core incidence lambda(T), and e_H(T). D14 and `alpha(H[R])<=2` give

> `lambda(T)<=13` for every triple T subset R.             (4)

Choose one d2 support D={u,v}. As in the c=8/c=9 closures:

- D is a target K2;
- every regular vertex outside D is target-anticomplete to D;
- the regular vertices Q in R\D form a target clique of size at least7.

Put `B=R\Q`. Then `|B|<=4` and D subset B.

Every d3 support contains at most one Q-vertex by row closure, hence contributes at least two incidences to B.

The total support incidence on B is at least14 in every case:

- n2=1: `2+2*6=14`;
- n2>=3: all d2 rows share one repeated D, giving `2n2+2(7-n2)=14`;
- n2=2: if repeated, again14; if distinct, the second d2 support cannot meet Q by its own row-closure inequality, hence is contained in B and contributes its two incidences, again giving14.

If |B|<=3, some triple contains all B incidences and has lambda at least14, contradicting (4). Therefore

> `|B|=4`.                                                   (5)

## 5. CORE211 equality fixes B and all d3 supports contain D

Because B consists of D plus exactly two nonregular vertices b1,b2 outside D, the total core excess2 is exhausted:

- `kappa(D)=0`;
- `kappa_b1=kappa_b2=1`.

Row closure for D gives `e_H(b_i,D)<=1`, so each b_i misses at least one D-endpoint. Since every q in Q is target-nonadjacent to D, `alpha(H[R])<=2` forces b_i to be target-adjacent to every q in Q.

Now let T be a d3 support and choose regular q in Q\T. Row closure for T gives

`e_H(q,T)<=e_F(q,x)<=1`.

But q is adjacent to every vertex of `Q union {b1,b2}`. Hence T contains at most one vertex of that set, so its other two vertices are exactly the two endpoints of D.

Thus every d3 support contains D.                              (6)

## 6. Decoration overflow

A d3 repivot removes the active decorated vertex x and the two regular far vertices, but retains the three inactive decorated vertices Y. By (2) this retains exactly three units of old decoration.

Each endpoint of D lies in all n3 d3 supports and at least one d2 support. Since kappa(D)=0, each endpoint has global decoration at least n3.

Therefore any d3 repivot satisfies

`G'>=3+2n3`.                                                (7)

Every q<=36 shell has `G'<=14`.

### n2=1

Then n3=6 and (7) gives `G'>=15`, contradiction.

### n2>=3

All d2 rows share D, so each D-endpoint is adjacent to all seven low owners and has decoration at least6. Hence `G'>=3+12=15`, contradiction.

### n2=2

If the two d2 rows repeat D, the same overflow applies.

If their supports D,E are distinct, E cannot meet Q: a regular q in Q\E would have `e_H(q,E)=0` by d2 row closure but would be adjacent to any Q-vertex of E. Hence E subset B. Since E is disjoint from D, `E={b1,b2}`.

But `kappa(E)=2`, exceeding the d2 allowance1 in the `2K1,a_F=0` branch. Contradiction.

Thus n2=2 is impossible as well.

## 7. Conclusion

No c=7 mixed d2/d3 candidate exists:

> `c=7, n2>=1` is EMPTY.

The all-d3 c=7 channel was already closed by the high-c single-class normal form. Hence the entire q36 f=2, 2K1, a_F=0, c=7 layer is empty.