# q36 f=2, 2K1 far, a_F=1 — full elimination of multiplicity >=3 in c=8,A=3

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, and `alpha(H[R])<=2`.

This proves that every support class in the c=8,A=3 layer has multiplicity at most2.

## 1. Multiplicity four is impossible

Let D have multiplicity4. The K11-minus-nu_Y D14 cap gives

`12 + O_D + e_F(Y,D)+e_H(D) <=14+nu_Y`,

where `nu_Y in {0,1}`. Hence

`O_D+e_F(Y,D)+e_H(D)<=2+nu_Y<=3`.

A repeated support has defect at most2: full defect3 would repivot to q36 while retaining both decorated inactive vertices Y and inserting three decorated support vertices, increasing tau beyond the old value3.

If another support E were disjoint from D, then:

- for nonclique D, an internal nonedge forces at least3 D--E cross edges, while D's cross allowance is at most1 (one-edge D) or at most2 (two-edge D);
- for clique D, any nonclique E again forces at least3 cross edges, while the allowance is at most2;
- if both D,E are K3s, the standard K3,3-minus-at-most-two-edges argument on the six-point remainder gives `sum w>=12>8`, impossible.

Thus every remaining owner support intersects D. Four owner incidences remain, so `O_D>=4`, contradicting the displayed D14 upper bound3. Therefore multiplicity4 is impossible.

## 2. Multiplicity-three classification

Let D have multiplicity3. D14 gives

`O_D+e_F(Y,D)+e_H(D)<=5+nu_Y`.                 (1)

The repeated-support defect is at most2.

### e_H(D)=2 or3

If `e_H(D)=2`, the cross allowance is at most1. A disjoint support is impossible because D's unique target nonedge requires at least3 cross edges. Thus all five remaining owner incidences intersect D, giving `O_D>=5`, while (1) gives `O_D<=3+nu_Y<=4`, contradiction.

If `e_H(D)=3`, the cross allowance is at most2. A disjoint nonclique support is impossible by the same three-cross-edge argument, and a disjoint K3 is impossible by the standard six-point w-mass contradiction. Thus again `O_D>=5`, while (1) gives `O_D<=2+nu_Y<=3`, contradiction.

### e_H(D)=1

Now m(D)=2, so the defect bound forces

`kappa(D)=0`, `e_F(x0,D)=0`.

Any disjoint support would be target-anticomplete to D by row closure and would form an independent triple with a nonedge pair in D. Hence `O_D>=5`.

Equation (1) now forces the unique equality possibility

- `nu_Y=1`;
- `O_D=5`;
- `e_F(Y,D)=0`;
- `e_H(D)=1`.

Thus every one of the five remaining owner incidences meets D exactly once.

## 3. The equality state produces a saturated q35 shell

The weighted support incidence is

`lambda(D)=3*3+5=14`.

Every D-vertex has core excess0 and no shell adjacency to x0, Y or the far pair beyond its low owners. Hence

`sum_D g_v=lambda(D)-3=11`.

Repivot one D-owner. The support defect is2, so q'=35. The two inactive decorated vertices Y are retained and have total decoration2 (because `nu_Y=1` and A=3 force `G_Y=2`). Therefore

`G'=2+11=13`.

Since every q35 shell has at least22 missing edges, `q'=z'+G'` forces

`z'=22`.

The new shell has a ten-point base `B={p} union (C\{owner}) union Y` whose only internal target nonedge is the Y-pair. The five remaining owners each see exactly one point of D.

Let the unique target edge of D be ab and let c be its isolated point.

As in the c=7 equality shell, the shell row weights on D are exactly

`t_a=t_b=11`, `t_c=12`.                                  (2)

Indeed an edge endpoint with n remaining owner incidences has missing degree `9-n` and decoration `2+n`, while the isolated point has missing degree `10-n` and the same decoration formula.

## 4. The five induced d2 rows are zero-defect pure K2 rows

For any of the five remaining owners, let d_i be its unique intersection point with D and put `P_i=E_i\D`.

In the q35 view its missing pair is `D\{d_i}` and its two-point core support is exactly P_i.

By (2), in every case the shell threshold is exactly22:

- if d_i=c, the missing pair is {a,b} and `11+11=22`;
- if d_i=a or b, the missing pair consists of one edge endpoint and c and has one shell missing edge, giving `11+12-1=22`.

Thus

`q_i=35+kappa(P_i)+m(P_i)+e_F(D\{d_i},P_i)`.

Suppose q_i=36. In the q35 view the repivot removes two decorated vertices of D and retains the third D-vertex plus both decorated Y-vertices, already three old decorated vertices. Lexicographic maximality of the original q36 pivot has tau=3, so P_i could contain no globally decorated vertex.

Hence both P_i vertices would be globally regular. A globally regular core support vertex has exactly its owner as shell neighbour, core excess0, and no x0/Y incidence. Returning to the original q36 view, the support `E_i={d_i} union P_i` would then have defect at most its internal missing count, which is at most2 because `alpha(H[R])<=2`. But q_i=36 in the original common-S formula requires full defect3. Contradiction.

Therefore every induced d2 row has q_i=35, and equality at threshold22 forces

`kappa(P_i)=0`, `m(P_i)=0`, `e_F(D\{d_i},P_i)=0`.        (3)

So every P_i is a pure target K2 target-anticomplete to its missing pair.

## 5. All five rows must pass through the isolated point

If d_i=a, then the missing pair is {b,c}, which is a target nonedge. By (3), both vertices of P_i are target-nonadjacent to b,c, creating an independent triple with {b,c}. Impossible. The case d_i=b is symmetric.

Thus every d_i=c. All five induced d2 rows have the same missing pair {a,b} and zero common-S allowance.

Different P_i support classes are therefore disjoint and target-anticomplete. If two distinct classes existed, choose one vertex from each and add a; since a is target-nonadjacent to both classes, this is an independent triple.

Hence all five P_i coincide. Then the original support `{c} union P_i` has multiplicity5, contradicting the already proved multiplicity-four exclusion.

## 6. Conclusion

No multiplicity-three support exists, and multiplicity four is impossible. Therefore

> every support in the c=8,A=3 layer has multiplicity at most2.