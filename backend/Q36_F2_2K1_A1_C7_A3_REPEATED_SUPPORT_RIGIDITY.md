# q36 f=2, 2K1 far, a_F=1 — repeated-support rigidity in c=7,A=3

Status: `PROVED` under the c=7,A=3 multiplicity-two frontier, K11/D14 incidence, row closure, CORE211, and `alpha(F)<=4`, `alpha(H[R])<=2`.

This proves that every repeated support is a target K3 and that two repeated supports cannot coexist. Hence the only remaining owner partitions are `2+1+1+1+1+1` and all singletons.

## 1. Every repeated support meets every other support

Let D be a repeated support, so r(D)=2. Full defect3 is impossible by lexicographic maximality; hence its defect is at most2.

Suppose another support E were disjoint from D.

- If `e_H(D)=1`, then `m(D)=2`, so the defect bound forces `kappa(D)=0` and `e_F(x0,D)=0`. Thus the common-S cross allowance of D is zero. A target-nonedge pair inside D together with any vertex of E gives an independent triple.
- If `e_H(D)=2`, D has one target nonedge and its cross allowance is at most1. Every vertex of E must meet that nonedge, forcing at least3 D--E target edges, contradiction.
- If `e_H(D)=3`, the cross allowance is at most2. If E is nonclique, an internal nonedge of E forces at least3 cross edges from the clique D, contradiction. If E is also a K3, then `e_H(D,E)<=2`. With `L=R\(D union E)`, |L|=6, every v in L must cover the nonedge graph K3,3 with at most two edges removed, whose minimum vertex-cover size is3. Writing `w_v=kappa_v+e_F(v,x0)`, row closure gives each cut at most w_v, hence w_v>=2 for every v in L. This yields `sum_L w_v>=12`, while CORE211 and |L|=6 give `sum_L w_v<=2+6=8`, contradiction.

Therefore every support other than D intersects D. Since five owner incidences remain outside the repeated class,

> `O_D>=5`.                                                 (1)

## 2. A repeated nonclique support is impossible

For r(D)=2, the K11/D14 support inequality is

`O_D+e_F(Y,D)+e_H(D)<=8`.                                  (2)

Suppose D is nonclique and choose a target-nonedge pair u,v in D.

For each inactive shell vertex y in the target K3 Y, if y were nonadjacent to both u and v, then

`{a,b,y,u,v}`

would be an independent5-set: the far pair a,b is a target nonedge and is target-anticomplete to Y and to the 12-point remainder R.

Hence each of the three vertices of Y must meet {u,v}; in particular

`e_F(Y,D)>=3`.                                              (3)

Using (1), (2), (3) and `e_H(D)>=1` gives

`8 >= O_D+e_F(Y,D)+e_H(D) >=5+3+1=9`,

contradiction.

Therefore

> every repeated support is a target K3.                   (4)

For such a K3, (1)--(2) force equality:

> `O_D=5`, `e_F(Y,D)=0`.                                   (5)

Thus every one of the five remaining owner incidences meets D in exactly one point.

## 3. Two repeated K3 supports cannot coexist

Assume D and E are two repeated K3 supports.

By (5) they intersect in exactly one point z. Write

`D={z,a1,a2}`, `E={z,b1,b2}`.

The proper overlap has size1, so the common-S overlap inequality costs2. Since both repeated supports have defect at most2 and internal missing count0, equality is forced in both directions.

Put `w_v=kappa_v+e_F(v,x0)`.

For b1,b2, row closure against D gives

`e_H(bi,D)<=w_bi`.

But each bi is adjacent to z because E is a K3. Hence `w_bi>=1`. The total D/E overlap equality leaves exactly2 units on the E\D side, so

`w_b1=w_b2=1`, `w_z=0`.

Symmetrically

`w_a1=w_a2=1`, `w_z=0`.

Moreover no petal bi can have another target edge into {a1,a2}, since it already uses its entire row-closure allowance1 on z. Thus the two petal pairs are target-anticomplete.

Let

`L=R\(D union E)`, so |L|=7.

For v in L, to avoid an independent triple using one petal from each anticomplete K2 pair, `N_H(v)` on the four petals must be a vertex cover of K2,2. Every minimum cover has size2 and consists of an entire side. Hence v is adjacent to both petals of D or both petals of E.

Therefore row closure forces

`w_v>=2`

for every v in L.

Summing over R gives

`sum_R w_v >= 4 + 7*2 =18`.

But globally

`sum_R w_v = kappa(R)+e_F(x0,R) <=2+12=14`,

contradiction.

Thus

> at most one repeated support class exists.                (6)

## 4. Conclusion

All support multiplicities are at most2, every repeated support is a target K3, and at most one repeated class exists.

Hence the c=7,A=3 owner partition is reduced to exactly two possibilities:

- one repeated K3 plus five singleton supports: `2+1+1+1+1+1`;
- seven singleton supports.

All partitions containing two or more repeated classes are EMPTY.