# Global Common-S Owner-Clique Packing Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- definition of a shell missing set;
- the pivot shell/core decomposition;
- `GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md`;
- inherited hereditary edge caps.

Purpose: identify a canonical dense base available in every common-missing-set family. This removes the need to rediscover D13/D14-style bases case by case.

## 1. Common-S owners form a target clique

Let p be a pivot and A its shell.

Let Y be a family of distinct regular shell owners such that every owner y has the same shell missing set

`S_y=S`, `|S|=d`.                                           (O1)

Take two distinct owners y,z in Y.

Suppose yz were a shell missing edge.

Then

`z in S_y=S`,                                               (O2)

and by symmetry

`y in S_z=S`.                                               (O3)

But `S=S_y` is the missing-neighbour set of y and therefore does not contain y itself.

Equation (O3) says `y in S=S_y`, contradiction.

Therefore yz is a target edge.

Hence:

> **Common-S owner clique theorem**
>
> `H_F[Y]=K_N`, where `N=|Y|`.                              (O4)

## 2. Adding the pivot gives a canonical K_(N+1) base

Every shell vertex is a target neighbour of p by definition of the pivot shell.

Therefore p is target-adjacent to every owner in Y.

Combining with (O4):

> `B={p} union Y` induces a target `K_(N+1)`.                (O5)

Thus

`|B|=N+1`,
`e_F(B)=C(N+1,2)`.                                         (O6)

The core supports lie outside B because the residual core is outside the pivot and shell.

This base exists for every common-S family; no extra shell topology is required.

## 3. Immediate clique-bound consequence

If the parent graph satisfies

`omega(F)<=R`,                                               (O7)

then (O5) gives

> `N+1<=R`.                                                  (O8)

For the r=12 residual problem, `omega(F)<=11`, hence

> every common-S owner family has `N<=10`.                  (O9)

This is a useful consistency bound: any larger collection of local views cannot be a single common-S owner family and must first be decomposed into several common-S subsystems.

## 4. One-support canonical packing inequality

Let D be one d-point support class used by m owners from Y.

Every such owner is target-adjacent to every point of D, so there are at least

`dm`                                                        (O10)

forced B--D target edges.

Let

`e_D=e_H(D)`                                                 (O11)

and let `c_D>=0` count any additional certified B--D target edges beyond those m owner incidences.

Apply the hereditary cap to

`B union D`,

which has size `N+1+d`.

The induced target edges include at least

`C(N+1,2)+dm+c_D+e_D`.

Therefore:

> **Canonical common-S one-support packing inequality**
>
> `dm+c_D+e_D`
> ` <= Dcap(N+1+d)-C(N+1,2)`.                               (O12)

This is the universal D13/D14-style multiplicity inequality for a common-S family.

## 5. Repeated-support version

Assume `s=|S intersect X|<d` and D repeats (`m>=2`).

`GLOBAL_REPEATED_SUPPORT_PACKING_BRIDGE.md` gives

`e_D>=e_min(d,a)=max(0,C(d,2)-a+1)`.                        (O13)

Substituting into (O12):

> `m <= floor((Dcap(N+1+d)-C(N+1,2)-c_D-e_min(d,a))/d)`.    (O14)

Dropping c_D yields the canonical multiplicity bound

> `m <= floor((Dcap(N+1+d)-C(N+1,2)-e_min(d,a))/d)`.        (O15)

Thus once N,d,a are known, repeated-support capacity can be read off directly from the hereditary cap.

## 6. Several pairwise-disjoint support classes

Let `D_1,...,D_k` be pairwise-disjoint support classes of size d, with owner multiplicities `m_i`.

All owners lie in Y, and owner classes partition the corresponding owner subset.

Applying `GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md` with canonical base B gives

> `d sum_i m_i`
> ` + sum_i(c_i+e_i)`
> ` + sum_(i<j)e_H(D_i,D_j)`
> ` <= Dcap(N+1+kd)-C(N+1,2)`.                              (O16)

If all k supports repeat and `s<d`, use `e_i>=e_min(d,a)` to obtain

> `d sum_i m_i + k e_min(d,a)`
> ` <= Dcap(N+1+kd)-C(N+1,2)`.                              (O17)

Every known cross edge or extra owner/base incidence sharpens the bound.

## 7. Equality rigidity

If equality holds in (O12) or (O16), then the canonical base-plus-support induced set saturates the hereditary cap.

Therefore all omitted possible edges must vanish.

For one support this means:

- no additional owner from Y outside the m certified owners may be target-adjacent to D unless included in c_D;
- no additional pivot/base incidence to D exists;
- support internal density is exact.

For several supports equality also fixes all cross-support edges.

Thus the canonical owner clique turns a scalar multiplicity equality into a complete local adjacency prescription.

## 8. r=12 numerical examples

For the current residual problem,

`Dcap(n)=C(n,2)-11 p_12(n)`.

In the range `12<=n<=17`, the retained bridge gives

`p_12(n)=n-12`,

so

- `Dcap(12)=66`;
- `Dcap(13)=67`;
- `Dcap(14)=69`;
- `Dcap(15)=72`;
- `Dcap(16)=76`;
- `Dcap(17)=81`.

### d=3, a=3, N=10

The canonical base is K11 with55 edges and `N+1+d=14`.

A repeated triple has `e_D>=1`.

Hence

`3m+1<=69-55=14`,

so

> `m<=4`.                                                    (O18)

### d=2, a=2, N=10

The same K11 base and `N+1+d=13` give

`2m<=67-55=12`,

hence

> `m<=6`.                                                    (O19)

These are direct applications of one theorem, not separate D13/D14 arguments.

## 9. Interface with one-loss pattern capacity

Suppose a d3 one-loss Type-H or Type-P pattern family carries M owners.

`GLOBAL_D3_ONE_LOSS_PATTERN_CAPACITY.md` gives at most3 distinct supports in that pattern, so some support repeats at least `ceil(M/3)` times.

The canonical owner-clique inequality (O15) can then test that repetition using only

- total common-S owner count N;
- support size3;
- row allowance;
- hereditary cap.

Likewise every d2 one-loss common-hub family with M owners forces a repeated K2 of multiplicity at least `ceil(M/3)`, which can be tested by the d2 version of (O15).

This is the canonical structural-to-capacity bridge.

## 10. Generalization

The common-S owner-clique theorem is purely combinatorial and independent of r=12.

For any higher-r pivot system, if owners are defined by a common shell missing set, they again form a target clique with the pivot. The packing inequalities then use whatever hereditary cap function is available.