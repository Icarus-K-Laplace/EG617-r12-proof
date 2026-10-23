# q36 f=2 far-target-K2 — c=8 no-d2 corrected low-allowance reduction V2

Status: `PROVED REDUCTION` under `Q36_F2_SHELL_LEDGER_REDUCTION.md`, `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, common-S row closure, q36 lexicographic maximality, CORE211, `alpha(H)<=3`, `alpha(F)<=4`, and the parent clique bound `omega<=11`.

This supersedes the retracted aggregate `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION.md`.

## 1. Safe shell reduction

Here `c=8`, `|X|=3`, there is no d2 row, and all eight low owners are d3 rows.

The exact shell ledger is

`G=6+a_F-nu`.

For an active decorated vertex x,

`A_x=n_x+nu_x+g_x-(8+a_F)`.

The previously proved no-d2 class-sum bound gives at most two active classes and, if two occur,

`A_x+A_z<=1`.

Suppose two active classes x,z occur and y is the third decorated vertex. Since `n_x+n_z=8`, exact subtraction gives

`g_y=-2-a_F-(A_x+A_z)+(nu_x+nu_z-nu)`.

But `nu_x+nu_z-nu=1_{xz in M}<=1`, so `g_y<=-1`, contradicting `g_y>=1` because y is decorated.

Therefore

> all eight owners belong to one common d3 missing-set class. (1)

Let x be the active decorated vertex and `Y={y,z}=X\{x}`. Put

`rho=e_M(Y) in {0,1}`.

Then

`A=nu_x+g_x-a_F`,
`g_y+g_z=6-A-rho`.

Since y,z are decorated,

> `A+rho<=4`.                                                (2)

Thus `A<=4`, and `rho=1` implies `A<=3`.

## 2. Allowance zero is empty

For A=0 every support has defect0, hence is a target K3 with zero core excess and zero S-incidence.

A repeated support would repivot to q36 while retaining the two inactive decorated shell vertices and inserting three repeated/global-decorated support vertices, increasing tau. Hence all eight supports are distinct.

Proper overlap costs2>A, so supports are disjoint. Joint row closure gives zero target cross-edges between distinct supports.

Choosing one point from each of four support blocks gives an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> A=0 is EMPTY.                                              (3)

## 3. Allowance one: at most three support classes

Now let A=1.

Proper overlap is impossible, so distinct support classes are disjoint. Joint row closure gives at most one target cross-edge between two distinct classes.

If four distinct support classes existed, choose one point uniformly from each. The expected number of target edges among the six selected pairs is at most

`6*(1/9)=2/3<1`.

Hence an independent4-set exists, contradiction.

Thus

> at most three distinct support classes occur.              (4)

If a support repeats, full defect1 is forbidden by q36 lexicographic maximality; therefore every repeated support has defect0 and is a target K3 with zero common-S weight.

## 4. Correct D14 multiplicity bound

The valid far-K2 D14 base is

`B={p} union C union Y`,

with

`e(B)=55-rho`.

For a repeated defect-zero K3 support D of owner multiplicity m, the corrected support inequality is

`3m+O_D+e_F(Y,D)+3 <=14+rho`.

Dropping nonnegative terms yields

> `m<=3` if `rho=0`,
> `m<=4` if `rho=1`.                                        (5)

No false `{p} union C union F` K11 base is used.

## 5. Any three-class state is impossible

Suppose there are three distinct support classes.

Because there are eight owners and every class has multiplicity at most4, at least two classes are repeated. Let D,E be two repeated classes. They are defect-zero target K3s, and zero common-S allowance gives

- D target-anticomplete to E;
- D and E target-anticomplete to every third support class T.

If T were nonclique, choose an internal target-nonedge pair from T and one vertex from each of D,E. This is an independent4-set in H. Hence T is also a target K3.

Thus the three distinct support classes are three pairwise target-anticomplete target K3 blocks B1,B2,B3.

Let v be any of the other 26 core vertices. If v were not target-complete to any B_i, choose a target-nonneighbour of v from each block. The three blocks are pairwise target-anticomplete, so these three choices together with v form an independent4-set. Therefore v is target-complete to at least one B_i.

For an outside core vertex, row closure against that support gives

`e_H(v,B_i)<=w_v`,

where

`w_v=kappa_v+e_F(v,S)`, `S=F union {x}`.

Completeness to a K3 gives

`w_v>=3`.

Hence

`sum_H w_v >=26*3=78`.                                     (6)

On the other hand CORE211 gives

`sum_H kappa_v=2`.

The two regular far rows have total core-row size

`(11-t_a)+(11-t_b)=22-a_F`.

For the active decorated vertex x,

`d_M(x)=10-t_x+nu_x`,
`g_x=1+a_F-nu_x`,

so its core-row size is

`|D_x|=d_M(x)+g_x=11+a_F-t_x`.

Therefore total S-to-core incidence is exactly

`(22-a_F)+(11+a_F-t_x)=33-t_x<=33`.

Thus

`sum_H w_v<=2+33=35`,                                      (7)

contradicting (6).

Therefore

> no A=1 state has three distinct support classes.           (8)

## 6. rho=0 is completely impossible

When `rho=0`, (5) gives multiplicity at most3.

With at most two support classes this can carry at most6 owners, fewer than8. Three classes are excluded by (8).

Hence

> `A=1, rho=0` is EMPTY.                                    (9)

## 7. rho=1 leaves only the exact 4+4 terminal

When `rho=1`, each class has multiplicity at most4. One class cannot carry eight owners; three classes are excluded by (8). Therefore exactly two classes remain and their multiplicities must be

> `4+4`.                                                     (10)

Call the two repeated target K3 supports D,E.

They have defect0, so they are target-anticomplete to the common missing set S and target-anticomplete to each other.

Apply corrected D14 to D. Since `m=4`, `e_H(D)=3` and `rho=1`,

`12+O_D+e_F(Y,D)+3<=15`.

Hence equality forces

`O_D=0`, `e_F(Y,D)=0`.                                      (11)

The same holds for E.

Thus D and E are target-anticomplete to

- each other;
- `S=F union {x}`;
- the inactive pair Y.

Equivalently, D and E are target-anticomplete to every vertex of `F union X`.

## 8. Shell geometry forced by alpha(F)<=4

Choose any `d in D` and `e in E`. Since de is a target nonedge and both d,e are target-anticomplete to the five shell vertices `F union X`, any independent triple in the shell graph on `F union X` would combine with d,e to form an independent5-set in the parent, forbidden by `alpha(F)<=4`.

Therefore

> `alpha(F[F union X])<=2`.                                  (12)

Recall:

- F is a target K2;
- Y={y,z} is a target-nonedge because `rho=1`;
- the total number of F--X target edges is `a_F<=2`.

For each far vertex f, the triple `{f,y,z}` cannot be independent. Hence every far vertex has a target edge to at least one of y,z. This requires at least two F--Y target edges.

Since `a_F<=2`, equality is forced:

> `a_F=2`,
> `t_x=e_F(x,F)=0`,
> the two available F--X edges both lie between F and Y and cover both far vertices.   (13)

Also `{x,y,z}` cannot be independent, so x is target-adjacent to at least one of y,z. Hence

> `nu_x<=1`.                                                  (14)

Thus the sole surviving A=1 state is the exact terminal

- `rho=1`;
- owner partition `4+4` on two disjoint defect-zero K3 supports D,E;
- D,E are mutually target-anticomplete and target-anticomplete to all of F union X;
- `a_F=2`, `t_x=0`, `nu_x in {0,1}`;
- corrected D14 is saturated on both support classes.

## 9. Correct current low-allowance frontier

Under the corrected far-K2 contract:

- A=0 is EMPTY;
- A=1 is reduced to the unique `rho=1, 4+4` equality terminal above;
- A=2,3,4 remain to be audited/solved separately.

No global target-K4 prohibition and no false far-K2 K11 base is used in this file.