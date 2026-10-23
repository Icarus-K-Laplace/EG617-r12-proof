# q36 f=2 — two-singleton far branch with no far-decoration incidence

Status: `PROVED REDUCTION` under `Q36_F2_SHELL_LEDGER_REDUCTION.md`, CORE211, row closure, the all-pivot core minimum-degree theorem, and lexicographic q36 maximality.

This treats the branch

- far regular shell F={a,b}=2K1 (`mu=1`);
- `a_F=e_F(F,X)=0`.

It reduces the d2 rows to at most one repeated pure-K2 class and proves that d3 rows use at most two decorated missing vertices.

## 1. The 11-point alpha-two remainder

Both far vertices have shell missing degree12. Their core supports A,B therefore have size12. Since a,b are regular and target-nonadjacent, zero-gap gives

  A intersect B=empty.

Every low-clique owner y is target-nonadjacent to both a,b, so its core support D_y is disjoint from A union B.

Put

  R=H\(A union B).

Then |R|=11 and every low support lies in R.

Every vertex of R is target-nonadjacent to both a,b. Hence an independent triple in H[R] together with {a,b} would give an independent5-set in F. Therefore

  alpha(H[R])<=2.                                           (1)

## 2. Shell ledger

Let c=|C|, r=|X|=11-c. Let n2 be the number of d2 low rows and let delta=c-n2 be the number of d3 rows. Put nu=e_M(X).

The exact f=2 ledger with mu=1 and a_F=0 gives

  G=13-delta-nu
   =13-c+n2-nu.                                             (2)

Since every vertex of X is decorated,

  G>=r=11-c,

so

  nu<=n2+2.                                                  (3)

## 3. d2 support rigidity

For a d2 owner y the missing set is exactly F. The exact d2 formula is

  q_y=35+kappa(D_y)+m(D_y)+e_F(F,D_y).

But D_y lies in R, hence is target-anticomplete to F, so

  q_y=35+delta_y,
  delta_y:=kappa(D_y)+m(D_y)<=1.                            (4)

All d2 rows share the same two-point missing set F.

### Distinct d2 supports are disjoint

Suppose distinct two-point supports D,E overlap in one vertex. Proper overlap costs

  h(2-h)=1,

so equality in the common-S overlap theorem forces delta_D=delta_E=1. Thus both repivots remain at q36.

The shared support vertex has two low owners and core degree at least12, hence is globally decorated. A d2 repivot removes only the two regular far vertices and retains every old decorated shell vertex. Inserting this decorated shared vertex would strictly increase tau, contradicting lexicographic maximality.

Therefore distinct d2 supports are disjoint.                  (5)

### At most two distinct d2 support classes

For distinct disjoint d2 supports D,E, the common-S theorem gives

  e_H(D,E)<=1.

If three distinct classes existed, choose one vertex uniformly from each of the three disjoint 2-sets. The expected number of target edges among the three selected vertices is at most

  3*(1/4)<1.

Hence some choice is an independent triple in H[R], contradicting (1). Thus there are at most two distinct d2 support classes.              (6)

### Repeated d2 supports are zero-defect pure K2s

If a support D is repeated and delta_D=1, its repivot remains at q36. Both vertices of D have at least two shell owners and are therefore globally decorated. Since the d2 repivot removes no decorated shell vertex, tau strictly increases. Contradiction.

Hence every repeated d2 support has

  delta_D=0.

Thus

- H[D]=K2;
- kappa(D)=0;
- the repivot has q=35.                                      (7)

### A repeated class cannot coexist with a second d2 class

Let D be repeated and E be a different d2 support. By (7) and the common-S joint-row theorem,

  e_H(D,E)=0.

If H[E] were a target nonedge, its two vertices together with any vertex of D would form an independent triple in R. Hence E must also be a target K2.

Put L=R\(D union E), so |L|=7. For v in L, to avoid an independent triple with one vertex from each of the anticomplete K2 blocks D,E, its neighbourhood in D union E must cover all four D--E target-nonedges. The minimum vertex-cover size of K2,2 is2, hence

  e_H(v,D)+e_H(v,E)>=2.                                     (8)

Row closure for the two d2 repivots gives, because v is target-anticomplete to F,

  e_H(v,D)<=kappa_v,
  e_H(v,E)<=kappa_v.

Thus kappa_v>=1 for all seven vertices of L, contradicting the CORE211 total excess2.

Therefore, if one d2 support is repeated, it is the only distinct d2 support class.              (9)

Consequently

> either n2<=2, or all n2 d2 rows share one pure K2 support. (10)

## 4. Multiplicity cap for the repeated K2

Assume n2>=3, so by (10) all d2 rows use one repeated pure K2 support D.

Repivoting one owner gives q=35 and removes only the two regular far vertices, so all old shell decoration G is retained. Each of the two D-vertices has core degree12 and at least n2 shell owners, hence global decoration at least n2-1.

Every q35 shell has decoration total at most13 (because its missing shell has at least22 edges). Therefore

  G+2(n2-1)<=13.

Using (2),

  13-c+n2-nu+2n2-2<=13,

so

> 3n2<=c+nu+2.                                              (11)

Together with (3),

> 2n2<=c+4.                                                 (12)

In particular the all-d2 branch n2=c satisfies c<=4.       (13)

Thus no f=2,2K1,a_F=0 shell with c>=5 can have all low rows of degree2.

## 5. At most two d3 missing-set classes

For x in X missed by at least one d3 owner, let

- n_x be the number of low owners missing x;
- nu_x=d_(M[X])(x);
- L_x=n_x+nu_x+g_x.

The exact d3 formula has threshold

  L_x>=7                                                     (14)

because mu=1 and a_F=0.

Let X0={x:n_x>0}, h=|X0|. Summing over x in X0,

  sum_(X0)L_x
  <= delta+2nu+G
  =13+nu.                                                    (15)

If h>=3, (14) gives 21<=13+nu, hence nu>=8.

But (3) then gives n2>=6. Since three d3 classes require delta>=3, we have c>=n2+3>=9. Therefore r=11-c<=2 and

  nu<=C(r,2)<=1,

contradiction.

Hence

> d3 rows use at most two decorated missing vertices: h<=2. (16)

## 6. Current a_F=0 interface

Every q36 f=2 candidate with far topology2K1 and a_F=0 has:

- a fixed 11-point remainder R with alpha(H[R])<=2;
- at most two distinct d2 support classes;
- if any d2 class repeats, it is the unique d2 class, is a pure K2, and repivots to q35;
- if n2>=3, all d2 rows share that K2 and satisfy
  `3n2<=c+nu+2` and `2n2<=c+4`;
- the all-d2 subbranch has c<=4;
- all d3 rows are split among at most two common-missing-triple classes.

Thus the former arbitrary d2/d3 mixture has collapsed to at most three row families: one possible repeated K2 family plus at most two d3 families.

This file is a reduction, not a full closure of the a_F=0 branch.