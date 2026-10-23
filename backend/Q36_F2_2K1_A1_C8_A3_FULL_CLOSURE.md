# q36 f=2, 2K1 far, a_F=1 — full closure of c=8, allowance three

Status: `PROVED` under `Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md`, `Q36_F2_2K1_A1_C8_A3_MULTIPLICITY3_FULL_CLOSURE.md`, common-S row closure, CORE211, inherited D14, lexicographic q36 maximality, `alpha(F)<=4`, and `alpha(H[R])<=2`.

This proves the entire c=8,A=3 layer empty.

## 1. Any repeated support is forced into one exact one-edge equality state

Multiplicity >=3 is already eliminated. Suppose D has multiplicity2. Full defect3 is impossible by lexicographic maximality, so D has defect at most2.

As in the c=7 repeated-support argument, D cannot have a disjoint support:

- if D has one internal target edge, its cross allowance is zero and any disjoint support gives an independent triple with a target-nonedge pair in D;
- if D has two internal target edges, its cross allowance is at most1 while the unique internal nonedge forces at least3 cross edges to any disjoint support;
- if D is a K3, a disjoint nonclique support again forces at least3 cross edges while the allowance is at most2; a disjoint K3 triggers the six-point `w=kappa+e(.,x0)` contradiction.

Hence all six remaining owner incidences meet D and

`O_D>=6`.                                                   (1)

The K11-minus-nu_Y D14 cap for r(D)=2 is

`O_D+e_F(Y,D)+e_H(D)<=8+nu_Y`,                             (2)

with `nu_Y in {0,1}`.

If D is nonclique, each of the two inactive shell vertices in Y must meet every internal target-nonedge of D; otherwise `{a,b,y,u,v}` is an independent5-set. Thus `e_F(Y,D)>=2`.

- If `e_H(D)=2`, (1)--(2) give at least `6+2+2=10>9`.
- If `e_H(D)=1`, they give at least9. Thus equality is possible only when `nu_Y=1`, and then exactly
  `O_D=6`, `e_F(Y,D)=2`, `e_H(D)=1`.
- If D is a K3, (1)--(2) force `nu_Y=1`, `O_D=6`, `e_F(Y,D)=0`. But nu_Y=1 means the two Y vertices are target-nonadjacent; with `e_F(Y,D)=0`, the set consisting of the far nonedge {a,b}, the Y nonedge, and any d in D is an independent5-set. Impossible.

Therefore the only repeated-support state is

> `nu_Y=1`, `e_H(D)=1`, `O_D=6`, `e_F(Y,D)=2`, `kappa(D)=e_F(x0,D)=0`.   (3)

## 2. The equality state generates a q35,z22,G13 shell

The weighted low-owner incidence on D is

`lambda(D)=2*3+6=12`.

Together with `e_F(Y,D)=2` and zero core excess/x0 incidence, the total global decoration on D is

`sum_D g_v=lambda(D)+e_F(Y,D)-3=11`.

For A=3 and nu_Y=1, the exact inactive identity gives `G_Y=2`. Repivoting one D-owner has support defect2, hence

`q'=35`, `G'=2+11=13`, `z'=22`.

Write the unique target edge of D as ab and let c be its isolated point. Direct shell counting gives the exact row weights

> `t_a=t_b=11`, `t_c=12`.                                  (4)

The six remaining owner supports each meet D exactly once. In the q35 view they become six regular d2 rows. If the original support is E_i and `d_i=E_i intersect D`, its new two-point support is `P_i=E_i\D` and its missing pair is `D\{d_i}`.

Equation (4) puts every one of these d2 rows exactly at shell threshold22.

## 3. All six d2 rows are q35 zero-defect pure K2 rows

The exact d2 identity is

`q_i=35+kappa(P_i)+m(P_i)+e_F(D\{d_i},P_i)`.

If q_i=36, then in the q35 view the repivot removes two decorated vertices of D and retains the third D-vertex plus the two decorated Y-vertices, already three old decorated vertices, equal to the original q36 tau. Hence P_i can contain no globally decorated vertex without violating lexicographic maximality.

Both P_i vertices would therefore be globally regular. Such a core support vertex has exactly its owner as shell neighbour, core excess0, and no x0/Y incidence. Returning to the original q36 view, `E_i={d_i} union P_i` would then have defect at most its internal missing count, at most2 because `alpha(H[R])<=2`, contradicting q_i=36 which requires full defect3.

Thus q_i=35 for all six rows, and threshold equality forces

`kappa(P_i)=0`, `m(P_i)=0`, `e_F(D\{d_i},P_i)=0`.          (5)

Hence every P_i is a pure K2 anticomplete to its missing pair.

If d_i were a or b, the missing pair would contain the isolated point c and the other edge endpoint, a target nonedge; either P_i vertex would then form an independent triple with that pair. Therefore every d_i=c.

All six induced d2 rows have common missing pair {a,b} and zero common-S allowance. Distinct P_i classes are disjoint and target-anticomplete. Two distinct classes would give an independent triple together with a. Hence all P_i coincide.

Then the original support `{c} union P_i` has multiplicity6, contradicting the multiplicity-four exclusion.

Therefore no repeated support exists.                            (6)

## 4. The all-singleton system has no q36 support

Now all eight supports are distinct singleton triples.

Suppose D has q=36. Repivoting it retains the two decorated Y vertices. Since the old q36 shell has only three decorated vertices (`x0 union Y`), D contains at most one globally decorated vertex, hence at least two clean private globally regular vertices.

Two q36 supports cannot coexist: choose one clean private vertex from each. Both are nonadjacent to Y. If they were target-nonadjacent, the far pair plus either y in Y would make an independent5-set; hence they must be adjacent. But row closure against one support forces the other clean regular vertex to be anticomplete to it. Contradiction.

So at most one support has q36; at least seven have defect at most2.

Any defect-at-most-two support cannot be disjoint from another support, by the same one-edge/two-edge/K3 case analysis used in Section1. Hence all eight supports are pairwise intersecting.

If D were the unique q36 support, all seven intersections with the low-charge supports must use D's unique possible decorated vertex z. For each proper overlap, the cost is2 and the low support has defect at most2, so equality forces `w_z=kappa_z+e_F(z,x0)=0`. The other two vertices of D are clean regular and also have w=0. Therefore D's defect is only its internal missing count, at most2, contradicting q=36.

Hence every support has q<=35. Since the supports are pairwise intersecting, the proper-overlap inequality forces defect at least2, so every support has defect exactly2. Every shared support vertex has w=0.       (7)

## 5. No support can be nonclique

Assume D is nonclique. Any shared vertex s outside D has w_s=0, so row closure against D makes s target-anticomplete to D; together with an internal nonedge of D this gives an independent triple. Therefore all globally shared vertices lie inside D. Let S be the shared set, `1<=|S|<=3`.

All eight supports are pairwise intersecting.

### |S|=1

All eight supports contain the shared point, leaving16 private incidences. This requires at least17 vertices, exceeding |R|=12.

### |S|=2

Pairwise intersection forces one shared point a to belong to all eight supports. Let the second shared point b have multiplicity k>=2. The private-incidence count is `24-(8+k)=16-k`; the 12-point capacity gives `2+16-k<=12`, hence k>=6.

A nonclique support containing both a,b has support incidence `lambda(D)=8+k+1=9+k`. Every y in Y must meet its internal target-nonedge, so `e_F(Y,D)>=2`. D14 with nu_Y<=1 gives

`lambda(D)+e_F(Y,D)+e_H(D)<=14+nu_Y<=15`.

Since e_H(D)>=1, `9+k+2+1<=15`, so k<=3, contradiction.

### |S|=3

Then the nonclique support D equals S. The private-incidence count is `24-lambda(D)`, and `3+24-lambda(D)<=12` forces `lambda(D)>=15`.

But D14 and `e_F(Y,D)>=2`, `e_H(D)>=1` give `lambda(D)<=12`, contradiction.

Thus every support is a target K3.                              (8)

## 6. Eight K3 singleton supports are impossible

Every support has defect exactly2. Shared vertices have w=0, so each support contains private vertices carrying total positive w-mass2.

For each support let S_D be its set of shared vertices. Then `|S_D|<=2` and the S_D are pairwise intersecting.

If they have no common point, they must be the edges of a triangle (with repetitions). Hence every support has exactly two shared vertices and one private vertex. The private vertex has w=2, so `kappa>=1` because `e_F(v,x0)<=1`. Eight distinct private vertices force total core excess at least8, contradicting CORE211.

If all S_D share a common point z, let k be the number of supports with a second shared point. Each such support has only one private vertex, which must have w=2 and hence kappa>=1. Therefore k<=2. The number of private vertices is

`2(8-k)+k=16-k>=14`.

Together with z this exceeds the 12 vertices of R.

Contradiction in both cases.

## 7. Conclusion

No c=8,A=3 state exists:

> `c=8, A=3` is EMPTY.