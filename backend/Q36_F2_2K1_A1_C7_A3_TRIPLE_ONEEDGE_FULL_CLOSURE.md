# q36 f=2, 2K1 far, a_F=1 — full closure of the multiplicity-three one-edge support branch

Status: `PROVED` under `Q36_F2_2K1_A1_C7_A3_MULTIPLICITY_RIGIDITY.md`, `Q36_F2_2K1_A1_C7_A3_TRIPLE_Q35_EQUALITY.md`, row closure, inherited D14, and `alpha(H[R])<=2`.

This removes the nonclique multiplicity-three state from the c=7,A=3 terminal.

## 1. Start from the exact q35 equality shell

Let D be a multiplicity-three support in the one-edge equality form. Write the unique target edge of H[D] as `ab`, and let `c` be the isolated vertex of H[D].

By `Q36_F2_2K1_A1_C7_A3_TRIPLE_Q35_EQUALITY.md`:

- `kappa(D)=0`;
- D is target-anticomplete to x0 and to Y;
- the four remaining owner supports E_i each meet D in exactly one point, counted with owner multiplicity;
- repivoting one D-owner produces a q35 shell with `z=22`, `G=13`;
- the four remaining owners are regular d2 shell vertices.

For a remaining owner with original support E_i, put

`d_i = the unique point of E_i intersect D`,
`P_i = E_i\D`.

The exact viewpoint transport gives that in the q35 shell its missing pair is

`S_i=D\{d_i}`

and its new two-point core support is exactly `P_i`.

## 2. Exact shell weights on D

In the q35 shell the three D-vertices have decorations

`g_d=lambda_d-1`,

where `lambda_d` is the number of the seven original low supports containing d. The three multiplicity-three D-owners contribute three to every lambda_d, while the four remaining owners contribute one incidence each to D in total.

For an endpoint d of the unique target edge ab, its q35 shell missing degree is

`d_M(d)=9-n_d`,

where n_d is the number of remaining owner incidences through d. Hence

`t_d=d_M(d)+g_d=(9-n_d)+(2+n_d)=11`.

For the isolated point c,

`d_M(c)=10-n_c`,

so

`t_c=(10-n_c)+(2+n_c)=12`.

Therefore

> `t_a=t_b=11`, `t_c=12`.                                  (1)

## 3. Every one of the four d2 rows has zero defect

Take one of the four d2 rows.

If its shared point is c, its missing pair is {a,b}. Since ab is a target edge, `e_M({a,b})=0`, and

`t_a+t_b-e_M({a,b})=22`.

If its shared point is a, its missing pair is {b,c}. Since bc is a target nonedge, `e_M({b,c})=1`, and

`t_b+t_c-1=11+12-1=22`.

The case shared point b is symmetric.

Thus for every remaining owner the exact d2 repivot identity has its shell term exactly at the nonprofitability threshold22. Consequently

`q_i=35 + kappa(P_i)+m(P_i)+e_F(S_i,P_i)`.

But q_i is the intrinsic charge of that degree-13 owner. In the original q36 maximum view its charge is at most36. If q_i were36, then in the q35 view the repivot would retain the three decorated Y-vertices and the one D-vertex outside S_i. That retained D-vertex is globally decorated because D has multiplicity3. Hence the new q36 shell already contains four old decorated vertices before inserting P_i.

Lexicographic maximality of the original q36 pivot has tau=4, so P_i cannot contain a globally decorated vertex in a q36 repivot. Thus both vertices of P_i would be globally regular.

A globally regular core vertex in P_i has only its owner among the low shell neighbours and has zero core excess and no x0/Y/far incidence. Hence for E_i={d_i} union P_i the original common-S defect would be exactly its internal missing-edge count. Since `alpha(H[R])<=2`, E_i is not independent, so that defect is at most2, contradicting q_i=36 (which would require full defect3 in the c=7,A=3 parent).

Therefore every one of the four owners actually has

> `q_i=35`.                                                  (2)

Returning to the exact d2 identity at threshold22, (2) forces

> `kappa(P_i)=0`, `m(P_i)=0`, `e_F(S_i,P_i)=0`.             (3)

Thus every P_i is a pure target K2 and is target-anticomplete to its missing pair S_i.

## 4. The shared point must be the isolated point c

Suppose `d_i=a`. Then `S_i={b,c}`. By (3), both vertices of P_i are target-nonadjacent to b and c.

But bc is a target nonedge in D. Hence either vertex of P_i together with {b,c} is an independent triple in H[R], contradicting `alpha(H[R])<=2`.

Similarly `d_i=b` is impossible.

Therefore for every one of the four remaining owners

> `d_i=c`.                                                   (4)

Then `S_i={a,b}`, and (3) says every P_i is a pure K2 target-anticomplete to both a and b.

## 5. All four petal K2s must coincide

All four d2 rows now have the same missing pair {a,b} and zero common-S allowance.

Hence the common-S theorem says any two distinct P_i support classes are either equal or disjoint, and distinct classes are target-anticomplete.

If two distinct classes P,Q existed, choose u in P and v in Q. Then uv is a target nonedge. Also a is target-nonadjacent to every vertex of P and Q by (3). Therefore {a,u,v} is an independent triple in H[R], contradiction.

Thus all four rows have the same two-point support P.

But then the original support

`{c} union P`

is used by all four remaining owners. It has multiplicity4, contradicting the already proved multiplicity-four exclusion in `Q36_F2_2K1_A1_C7_A3_MULTIPLICITY_RIGIDITY.md`.

## 6. Conclusion

The multiplicity-three one-edge equality state is impossible.

Therefore in the c=7,A=3 terminal:

> every multiplicity-three support, if any, must be a target K3.

The only remaining multiplicity-three owner partitions are those involving this clique state, e.g. 3+2+2 and 3+2+1+1; partitions with maximum multiplicity at most2 remain separate.