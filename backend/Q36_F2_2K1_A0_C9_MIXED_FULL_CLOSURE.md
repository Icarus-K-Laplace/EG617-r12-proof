# q36 f=2, 2K1 far, a_F=0 — full closure of the c=9 mixed d2/d3 sector

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, `Q36_F2_2K1_A0_LOW_ALLOWANCE_D3.md`, row closure, CORE211, inherited D14, and `alpha(H[R])<=2`.

Together with `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`, this closes the entire c=9 branch.

## 1. Setup

Let c=9 and suppose at least one low row has missing degree2. Let n2 be the number of d2 low owners and n3=9-n2 the number of d3 low owners. The two decorated shell vertices form X={x,y}. Let nu=e_M(X) in {0,1}.

The 11-point remainder R satisfies `alpha(H[R])<=2` and CORE211 gives total core excess at most2.

## 2. There is only one active d3 missing class

If both x and y are used as d3 missing vertices, write their allowances A_x,A_y as in `Q36_F2_2K1_A0_LOW_ALLOWANCE_D3.md`.

The class-sum identity gives

`A_x+A_y = nu-1 <= 0`.

Both allowances are nonnegative, hence nu=1 and A_x=A_y=0. An allowance-zero d3 class has at most2 owners, so n3<=4 and therefore n2>=5.

But for n2>=3 all d2 rows share one repeated pure K2 support and satisfy

`3 n2 <= c+nu+2 = 12`,

hence n2<=4, contradiction.

Therefore all d3 rows use a single decorated missing vertex, say x.

The other decorated vertex y is target-adjacent to every low owner: d2 rows miss only the far pair F, and d3 rows miss F union {x}. Consequently

> `{p} union C union {y}` is a target K11.

## 3. A d2 support creates a large regular clique

Choose one d2 support D={u,v}.

For every regular w in R\D, row closure for the d2 repivot gives

`e_H(w,D)<=kappa_w=0`,

because every R-vertex is target-anticomplete to the far pair F.

The pair D must be a target K2. Otherwise any regular w outside D together with the two nonadjacent endpoints of D would form an independent triple in H[R].

Let Q be the regular vertices in R\D. Since total core excess is at most2,

`|Q|>=7`.

Moreover Q is a target clique: if q1,q2 in Q were target-nonadjacent, then either endpoint of D together with q1,q2 would form an independent triple, since D is target-anticomplete to Q.

Put

`B=R\Q`.

Then `|B|<=4` and D subset B.

## 4. Every d3 support contributes at least two incidences to B

Let T be any d3 support. Suppose T contained two vertices q1,q2 in Q.

Choose q in Q\T, possible because |Q|>=7. The d3 missing set is F union {x}. Since q is regular and target-anticomplete to F, row closure gives

`e_H(q,T)<=e_F(q,x)<=1`.

But Q is a target clique, so q is adjacent to q1 and q2 and therefore `e_H(q,T)>=2`, contradiction.

Hence every d3 support meets Q in at most one vertex and contributes at least two support incidences to B.

## 5. K11/D14 incidence cap

For v in R let lambda_v be the number of the nine low owners whose support contains v.

For any triple T subset R, the 14-point set

`{p} union C union {y} union T`

contains the target K11 `{p} union C union {y}`, with55 internal target edges. It also contains

- `lambda(T)` edges from the low clique C into T;
- `e_F(y,T)` edges from y into T;
- `e_H(T)` internal target edges of T.

The inherited D14 cap gives

`55 + lambda(T) + e_F(y,T) + e_H(T) <= 69`.

Since `alpha(H[R])<=2`, every triple spans at least one target edge, so

> `lambda(T)<=13` for every triple T subset R.                 (1)

## 6. The exceptional block B always carries at least18 incidences

### n2=1

The chosen d2 support contributes2 incidences to B and the eight d3 supports contribute at least16. Thus

`lambda(B)>=18`.

### n2>=3

All d2 rows share one repeated pure K2 support D. Hence the d2 rows contribute `2n2` incidences to B and the d3 rows contribute at least `2(9-n2)`. Therefore

`lambda(B)>=2n2+2(9-n2)=18`.

### n2=2

If the two d2 rows use the same repeated support D, they contribute4 incidences to B and the seven d3 rows contribute at least14, again giving18.

Suppose instead the two d2 supports D,E are distinct. We claim E subset B.

If E contained a vertex e in Q, choose q in Q\E. The vertex q is regular. Row closure for the d2 support E gives

`e_H(q,E)<=kappa_q=0`.

But q and e both lie in the target clique Q, so `e_H(q,E)>=1`, contradiction. Hence E cap Q is empty and E subset B.

Thus the two d2 supports contribute4 incidences to B, while the seven d3 supports contribute at least14. Again

`lambda(B)>=18`.

Therefore in all mixed c=9 cases

> `lambda(B)>=18` with `|B|<=4`.                              (2)

Among at most four nonnegative lambda-values of total at least18, the largest three have sum at least14. Hence some triple T subset B satisfies `lambda(T)>=14`, contradicting (1).

## 7. Conclusion

No c=9 mixed d2/d3 candidate exists:

> `c=9, n2>=1` is EMPTY.

Combined with `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`, the entire q36 f=2, 2K1, a_F=0, c=9 layer is empty.