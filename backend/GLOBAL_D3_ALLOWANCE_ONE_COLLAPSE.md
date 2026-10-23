# Global d=3 Allowance-One Collapse Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- common-S row closure and exact tau transport;
- lexicographic maximality of `(q,tau)`.

This theorem is a concrete bounded-transversal rigidity result for triple supports. It converts a many-view low-allowance problem into one high-multiplicity repeated-K3 problem.

## 1. Setup

Let H be a core on n vertices with

`alpha(H)<=3`.

Let Y be a family of N regular owner rows sharing one missing set S of size

`d=3`.

For owner y let its support be `D_y`, a three-point subset of H.

Use the standard common-S quantities

`w_v=kappa_v+e_F(v,S)`,

`mu(D)=3-e_H(D)`,

and row allowance a, so every row satisfies

`w(D_y)+mu(D_y)<=a`.

Assume

> `a<=1`,                                                     (1)

and let

`s=|S intersect X|<3`,                                       (2)

where X is the globally decorated set.

Put

`W=sum_(v in H) w_v`.                                        (3)

## 2. Distinct supports are disjoint

For two common-S supports with proper overlap r in {1,2}, the joint-row overlap theorem gives

`r(3-r)<=a`.

But

`r(3-r)=2>a`.

Therefore proper overlap is impossible.

Hence any two distinct support classes are disjoint.           (4)

## 3. At most three distinct support classes

For disjoint supports D,E, common-S row closure gives

`e_H(D,E)<=min(w(D),w(E))`
`          <=min(a-mu(D),a-mu(E))`
`          <=1`.                                             (5)

Thus the distinct support classes are pairwise-disjoint 3-blocks with at most one target cross-edge between every block pair.

By `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`, the d=3,c=1 capacity is three blocks.

Therefore

> the common-S family has at most three distinct support classes.   (6)

This conclusion is independent of N.

## 4. Every repeated class is a zero-charge target K3

Let D be a support class used by at least two owners.

Every point of D is globally decorated by support repetition.

Since `s<3`, exact tau transport shows that a D-owner cannot be a q-plateau row: repivoting it at equal q would replace only s decorated missing-set vertices by all three decorated support vertices and strictly increase tau.

Hence every owner using D has

`q_y<=q-1`.                                                  (7)

For such an owner the exact defect identity is

`q-q_y = a-[w(D)+mu(D)]`.

Using `a<=1` and (7),

`w(D)+mu(D)<=a-1<=0`.

Both terms are nonnegative, so

> `w(D)=0`, `mu(D)=0`.                                       (8)

Thus

> every repeated support class is a target K3 consisting entirely of zero-charge vertices.   (9)

Moreover every row in that repeated class loses exactly one q-unit when a=1 (and no repeated class can exist when a=0 and q-loss would exceed the available allowance).

## 5. Three classes with two repeated classes force huge global charge

Assume there are exactly three distinct support classes D,E,T and at least two of them, say D and E, are repeated.

By (9), D and E are zero-charge target K3s.

Row closure gives

`e_H(D,E)=0`.                                                (10)

Because w(D)=w(E)=0, row closure also gives

`e_H(D,T)=e_H(E,T)=0`.                                      (11)

If T were not a target K3, choose an internal target-nonedge pair u,v in T, one point d in D and one point e in E. Equations (10)--(11) show that

`{d,e,u,v}`

is an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore T is also a target K3.                             (12)

Now let z be any core vertex outside `D union E union T`.

If z were not target-complete to any of D,E,T, choose

- d in D target-nonadjacent to z;
- e in E target-nonadjacent to z;
- t in T target-nonadjacent to z.

The three support blocks are pairwise target-anticomplete by (10)--(11), so

`{z,d,e,t}`

would be an independent4-set.

Hence z must be target-complete to at least one of the three support K3s.

Applying row closure against that support yields

`3<=w_z`.                                                    (13)

There are `n-9` such outside vertices. Consequently

> `W>=3(n-9)`.                                               (14)

Therefore, whenever

> `W<3(n-9)`,                                                (15)

three distinct support classes cannot contain two repeated classes.

## 6. Multiplicity collapse

Assume (15).

By (6), there are at most three distinct support classes.

### One class

Its multiplicity is N.

### Two classes

One class has multiplicity at least

`ceil(N/2)`.

### Three classes

By Section5, at most one class is repeated. Therefore the other two classes are singletons and the repeated class has multiplicity

`N-2`.

For N>=4,

`N-2>=ceil(N/2)`.

Thus in every case

> **there exists a repeated support class of multiplicity at least `ceil(N/2)`.**   (16)

By (9), that class is a zero-charge target K3.

This proves the main collapse theorem:

> **d3 allowance-one collapse.**
> Under (1), (2), (15), any common-S family of N>=4 owners contains a zero-charge target-K3 support repeated at least `ceil(N/2)` times.   (17)

## 7. Eleven-view corollary

For N=11, (17) gives

> a zero-charge target K3 repeated at least six times.       (18)

Therefore any eleven-view d3 system satisfying the low-allowance hypotheses is no longer an eleven-case compatibility problem. It reduces to one high-multiplicity repeated-K3 support.

The remaining contradiction can be sought from a one-support hereditary packing inequality / dense-base cap, or from secondary repivot geometry.

This is precisely the desired bridge from multi-view compatibility to repeated-support rigidity.

## 8. Equality interpretation

The only way a large low-allowance triple-support family can avoid immediate disjoint-block contradiction is to concentrate many owners on one pure K3 support.

Thus the equality geometry is not arbitrary:

- support repetition is macroscopic;
- the repeated support is a zero-charge K3;
- all its owners are strict one-unit q-loss rows;
- any additional support classes are at most two and, in the three-class regime, are forced to be singletons.

This is a much smaller object for hereditary-cap analysis than the original owner-view list.

## 9. Parameterized nature

The proof uses only

- support size d=3;
- allowance a<=1;
- alpha(H)<=3;
- exact repivot/tau transport;
- a global charge threshold `W<3(n-9)`.

The numerical core size 35 and CORE211 value 211 do not enter the argument. Hence the theorem can transfer to higher-r pivot systems whenever the analogous low-allowance and charge threshold hold.