# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 one-edge terminal closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`, row closure, CORE211, inherited D14, q36 lexicographic maximality, and `alpha(H[R])<=2`.

This eliminates the last multiplicity-three one-edge equality terminal from the A=3 branch.

## 1. Equality setup

Let D={a,b,c} be a multiplicity-three support with exactly one internal target edge ab, so c is isolated in H[D]. The A=3 reduction gives exactly

- `O_D=4`;
- `e_H(D)=1`;
- `kappa(D)=0`;
- `e_F(F union {x},D)=0`;
- the D-repivot has q=35.

There are exactly four external d3 owner incidences. Since every external support intersects D and O_D=4, each of the four external supports E_i meets D in exactly one vertex.

Let Y=X\{x} be the two inactive decorated shell vertices.

## 2. The q35 shell is D14-saturated

The allowance identity for c=8,A=3 gives

`nu_x+g_x=4`.

The original shell ledger is

`G=7-nu`,

where `nu=e_M(X)=nu_x+e_M(Y)`. Therefore the decoration retained on Y is

`G_Y=G-g_x=3-e_M(Y)`.                                      (1)

The weighted low-owner incidence on D is

`lambda(D)=3*3+4=13`.

Since D has zero core excess and no F/x incidence, its total global decoration is

`sum_D g_v = lambda(D)+e_F(Y,D)-3 = 10+e_F(Y,D)`.          (2)

After repivoting a D-owner, the new q35 shell contains Y and D, hence

`G' = G_Y + sum_D g_v = 13+e_F(Y,D)-e_M(Y)`.              (3)

Every shell has at least22 missing edges, so q'=35 implies G'<=13. Therefore

`e_F(Y,D)<=e_M(Y)`.                                        (4)

If e_M(Y)=1 but e_F(Y,D)=0, take the target-nonedge pair Y, a target-nonedge pair from the one-edge triple D, and either vertex of the pure d2 block D0. The d2 block is target-anticomplete to Y and to every d3 support, producing an independent5-set in the parent graph. Hence in that case e_F(Y,D)>=1.

Thus equality holds in (4), and in every case

> `G'=13`, `z'=22`.                                         (5)

Direct shell counting gives the three D-row weights

> `t_a=t_b=11`, `t_c=12`.                                  (6)

## 3. The four external supports all meet D at c and induce pure K2s

Fix an external support E and write `d=E intersect D`, `P=E\{d}`.

Because D and E are distinct common-S triples with one-point overlap, the proper-overlap cost is2. Hence E has defect at least2 and its intrinsic pivot charge is q_E>=35.

Suppose q_E=36. Repivoting E from the original q36 shell removes x and retains the two inactive decorated vertices Y. The shared point d lies in the repeated support D and is globally decorated. Thus three decorated vertices are already present after the exchange. Lexicographic maximality forces both vertices of P to be globally regular.

A globally regular core vertex in P has core excess0 and exactly its owner as shell target neighbour, hence contributes no F/x incidence. Since d itself has zero core/F/x contribution, the original support defect of E is then at most its internal missing count, which is at most2 because alpha(H[R])<=2. This contradicts q_E=36, which requires defect3.

Therefore

> q_E=35 and the defect of E is exactly2.                   (7)

Let `s(P)=kappa(P)+e_F(F union {x},P)`. Since D has zero such weight, the overlap equality gives

`s(P)+m(E)=2`.                                               (8)

Row closure against the repeated support D, summed over P, gives

`e_H(P,D)<=s(P)=2-m(E)=e_H(E)-1`.                          (9)

Now write `e_P=e_H(P)` and `k=e_H(d,P)`, so `e_H(E)=e_P+k`. Since `e_H(P,D)>=k`, (9) yields

`k<=e_P+k-1`,

hence `e_P=1`. Equality in (9) then forces

- P is a target K2;
- P is target-anticomplete to D\{d}.                         (10)

If d=a or d=b, then D\{d} is a target-nonedge pair containing c and the other endpoint of ab. Any vertex of P together with that pair would be an independent triple in R, contradicting alpha(H[R])<=2.

Therefore

> every external support has the form `E_i={c} union P_i`,
> where each P_i is a target K2 target-anticomplete to {a,b}. (11)

## 4. c is adjacent to every petal vertex

Let u be any vertex appearing in some P_i.

We have

- ac is a target nonedge;
- au is a target nonedge by (11).

If cu were also a target nonedge, then {a,c,u} would be an independent triple in R, impossible.

Hence

> c is target-adjacent to every petal vertex.                (12)

Thus every E_i={c,u,v} is itself a target K3.

## 5. Distinct petal pairs must intersect

Suppose P_i and P_j are disjoint.

For E_j, defect2 and m(E_j)=0 imply

`kappa(P_j)+e_F(F union {x},P_j)=2`,

because c has zero core/F/x weight.

Apply row closure against support E_i to the two vertices of P_j. Their two target edges to c already consume this entire two-unit row-closure budget. Therefore

`e_H(P_i,P_j)=0`.                                           (13)

But a is target-nonadjacent to every petal vertex by (11). Choosing one vertex from each P_i,P_j together with a gives an independent triple in R, contradiction.

Therefore

> the four 2-sets P_1,...,P_4 are pairwise intersecting.     (14)

## 6. D14 incidence contradiction

For a petal vertex u let r_u be its multiplicity among the four pairs P_i.

The common core vertex c belongs to

- the three owners of D;
- all four external supports.

Hence its low-owner support multiplicity is

`lambda_c=7`.

Take one external support E_i={c,u,v}. The 14-point set

`{p} union C union F union E_i`

contains the target K11 `{p} union C union F`, so D14 gives

`55 + (7+r_u+r_v) + e_H(E_i) <=69`.

By (12), E_i is a K3, so e_H(E_i)=3. Thus

> `r_u+r_v<=4` for every petal pair uv=P_i.                 (15)

On the other hand, any multiset of four pairwise-intersecting 2-subsets has some member uv with

`r_u+r_v>=5`:

- if all pairs have a common point, that point has multiplicity4 and its partner has multiplicity at least1;
- otherwise the underlying simple pairwise-intersecting family is a triangle; with four pairs one edge is repeated, and the two endpoint multiplicities of that repeated edge sum at least6.

This contradicts (15).

## 7. Conclusion

The multiplicity-three one-edge q35 equality terminal is impossible.

Together with `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md`, every multiplicity-three support is eliminated from the c=8, one-d2, A=3 branch.