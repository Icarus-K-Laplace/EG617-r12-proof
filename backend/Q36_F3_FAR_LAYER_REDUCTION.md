# q36 candidate coverage — f=3 far-layer reduction

Status: `PROVED REDUCTION` under `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md` and the standard q36 CORE211 / row-closure contract.

This treats the case in which the unique low regular clique C has exactly three far/high regular shell vertices outside it.

## 1. Exact f=3 shell ledger

Let F be the three far regular vertices and X the decorated shell vertices. Put

`c=|C|`, `r=|X|`.

Because the shell has13 vertices,

`c+r=10`.                                                   (1)

Every y in C is missing-adjacent to all three vertices of F. Since y is low and d4 is already excluded, its missing degree must be exactly3. Therefore y cannot miss any decorated shell vertex.

Hence

- every vertex of C is target-adjacent to every vertex of X;
- every decorated vertex is assigned to C by the cluster theorem and is therefore target-anticomplete to F.

Let

`nu=e_M(X)`

and let

`mu=e_M(F)`.

All thirty C/X-to-F cross pairs are missing, so

`e(M)=30+mu+nu`,

`G=36-e(M)=6-mu-nu`.                                       (2)

Since every vertex of X is decorated,

`G>=r=10-c`.                                                (3)

The three possible target-clique partitions of F are:

- F=K3: `mu=0`;
- F=K2 disjoint union K1: `mu=2`;
- F=3K1: `mu=3`.

## 2. F=K3 is impossible

Assume F is a target K3.

Then from (2)

`G=6-nu`.

For any y in C, its missing set is exactly F, so d=3. Its outside set is

`T=(C\{y}) union X`.

Inside T the only missing edges are those of M[X], hence

`e_M(T)=nu`,

while all decoration lies in X, so

`G_T=G=6-nu`.

Therefore the common-S outer defect is exactly

`B=e_M(T)+G_T=6`.                                          (4)

The exact q36 d3 repivot formula is

`q_y=30+B+kappa(D_y)+m(D_y)+e_F(F,D_y)`.

By (4) and q-maximality,

`q_y=36`,

and every remaining nonnegative defect vanishes:

- `kappa(D_y)=0`;
- `m(D_y)=0`;
- `e_F(F,D_y)=0`.

Thus every D_y is a target K3 of H-degree12 vertices and is target-anticomplete to F.

All C-vertices share the same missing set F. Since `q-30-B=0`, the common-S theorem gives: two distinct supports are disjoint and target-anticomplete.

We now show the supports cannot repeat. The old q36 pivot p has exactly r decorated shell vertices, namely X. Repivoting y retains all of X and removes only the three regular vertices F. Since `q_y=36`, lexicographic maximality forbids any inserted support vertex from being globally decorated.

But a support vertex has H-degree12 and is adjacent to its owner y. If the same support served two distinct vertices y,z in C, every support vertex would be adjacent to both y and z and therefore have global degree at least14, contradiction.

Hence the c vertices of C have c distinct pairwise anticomplete K3 supports.

From (2)--(3) with mu=0,

`6-nu>=10-c`,

so `c>=4+nu>=4`.

Choose one vertex from four distinct supports. They form an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> the F=K3 branch is empty.

## 3. F=3K1 is impossible

Assume the three far vertices z1,z2,z3 are pairwise target-nonadjacent.

Each zi is regular and its missing neighbourhood consists of

- the ten vertices C union X;
- the other two far vertices.

Thus

`d_M(zi)=12`,

so its core support E_i has size12.

For every pair zi,zj, the regular zero-gap theorem for a missing shell edge gives

`E_i intersect E_j=empty`.

Hence E1,E2,E3 would be three pairwise-disjoint 12-subsets of the 35-point core, requiring36 vertices. Contradiction.

Therefore

> the F=3K1 branch is empty.

## 4. The only f=3 residual: F=K2 disjoint union K1

Let a,b be the target-adjacent K2 and z the singleton.

Then `mu=2`, so

`G=4-nu`,

and (3) gives

`c>=6+nu`.                                                  (5)

The regular missing degrees are

- `d_M(a)=d_M(b)=11`;
- `d_M(z)=12`.

Let their core supports be

`E_a,E_b,E_z`,

with sizes11,11,12.

For every y in C, the zero-gap theorem applied to the missing edges ya,yb,yz gives

`D_y` disjoint from `E_a union E_b union E_z`.               (6)

Likewise z is missing-adjacent to both a and b, so

`E_z intersect E_a=empty`,
`E_z intersect E_b=empty`.                                  (7)

The vertices a,b have the same 11-point missing neighbourhood

`S=(C union X) union {z}`.

For a d11 row at q36,

`d(13-d)=22`,

and its outside set consists only of the other K2 vertex. Hence the common-S outer defect B is0 and

`s=q-22=14`.

If

`h=|E_a intersect E_b|`,

the common-S overlap theorem gives

`h(11-h)<=14`.

Thus

`h in {0,1,10,11}`.                                        (8)

But h=0 or1 is impossible: by (7),

`|E_z union E_a union E_b|`

would be respectively34 or33, leaving only1 or2 core vertices outside. Equation (6) requires every D_y to be a 3-subset of that complement, impossible because C is nonempty (indeed c>=6 by (5)).

Therefore

> `|E_a intersect E_b| in {10,11}`.                         (9)

Consequently the complement

`R=H\(E_z union E_a union E_b)`

has size

- 11 if the overlap is10;
- 12 if the overlap is11.

Every low-clique support D_y is contained in R.

Finally, for y in C the common missing set is F of size3. Its outside defect is

`B=e_M((C\{y}) union X)+G`
`=nu+(4-nu)=4`.

Thus

`q_y=30+4+kappa(D_y)+m(D_y)+e_F(F,D_y)`.

By (6) the final cross term vanishes, and q-maximality gives

> `kappa(D_y)+m(D_y)<=2`                                    (10)

for every y in C.

So every one of the at least six C-rows is a 3-subset of an 11/12-point remainder R and induces at least one target edge.

## Current f=3 frontier

Two of the three far partitions are fully eliminated. The only surviving f=3 candidate is the rigid `K2 union K1` terminal defined by

- `c>=6+nu`;
- `G=4-nu`;
- supports `(11,11,12)` with the two 11-supports overlapping in10 or11 points;
- all c low rows contained in an 11/12-point remainder;
- every low triple satisfies `kappa+m<=2`.

This is now a finite incidence/capacity problem rather than an arbitrary shell family.