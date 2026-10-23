# Global Sunflower Support-Packing Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- inherited hereditary induced-edge cap;
- the canonical common-S owner clique when that base is used.

Purpose: extend hereditary support packing from pairwise-disjoint supports to the common-hub/common-pair sunflower families forced by zero-charge incidence rigidity.

## 1. Abstract setup

Let G satisfy a hereditary cap

`e_G(W)<=Dcap(|W|)`                                         (S1)

for all relevant induced vertex sets W.

Let B be a base set disjoint from the support vertices, with

`|B|=b`,
`e_G(B)=E_B`.                                               (S2)

Let

`D_1,...,D_k`

be distinct d-point support classes forming a sunflower with common core C:

`D_i=C union P_i`,                                          (S3)

where

`|C|=c`,
`|P_i|=p=d-c`,
`P_i intersect P_j=empty` for i!=j.                         (S4)

Let support D_i have owner multiplicity m_i among vertices of B, with every owner target-adjacent to all d points of D_i.

Assume the owner sets for distinct support classes are disjoint, as they are for a partition of one common-S owner family.

Let

`N=sum_i m_i`.                                              (S5)

Let `a_i>=0` denote any additional certified B--D_i target incidences beyond the dm_i owner-support edges.

## 2. Exact internal sunflower edge accounting

Write

`e_C=e_G(C)`,
`e_i=e_G(D_i)`,
`c_ij=e_G(P_i,P_j)`.                                       (S6)

Summing the internal support counts `e_i` counts every edge of the common core C exactly k times, while it occurs only once in the union.

All other edges internal to one D_i occur only once because the petals are disjoint.

Therefore the number of target edges inside the support union is exactly

> `sum_i e_i-(k-1)e_C+sum_(i<j)c_ij`.                       (S7)

## 3. Sunflower hereditary packing inequality

Consider

`W=B union C union P_1 union ... union P_k`.

Its size is

`|W|=b+c+kp`.                                               (S8)

The induced target edges include at least

- `E_B` inside B;
- `dN` owner-support edges;
- `sum_i a_i` additional certified base-support edges;
- the exact support-union contribution (S7).

Hence the hereditary cap gives

> **Sunflower support-packing inequality**
>
> `dN`
> ` + sum_i a_i`
> ` + sum_i e_i-(k-1)e_C`
> ` + sum_(i<j)c_ij`
> ` <=Dcap(b+c+kp)-E_B`.                                    (S9)

This is the common-core analogue of the pairwise-disjoint support-packing theorem.

## 4. Equality rigidity

If equality holds in (S9), every omitted possible contribution must vanish.

In particular:

- no uncertified B--petal target edges exist;
- all petal--petal cross target edges are exactly the certified c_ij values;
- the sunflower support union has exactly the stated internal edges;
- the induced set W saturates the hereditary cap.

Thus equality again becomes a full adjacency prescription.

## 5. Canonical common-S owner-clique specialization

Suppose the sunflower comes from one common-S owner family of size N.

By `GLOBAL_COMMON_S_OWNER_CLIQUE_PACKING.md`,

`B={p} union Y`

is a target `K_(N+1)`.

Hence

`b=N+1`,
`E_B=C(N+1,2)`.                                             (S10)

The canonical sunflower inequality becomes

> `dN`
> ` + sum_i a_i`
> ` + sum_i e_i-(k-1)e_C`
> ` + sum_(i<j)c_ij`
> ` <=Dcap(N+1+c+kp)-C(N+1,2)`.                             (S11)

No shell-specific dense base must be discovered.

## 6. d=3 Type-H family

For the Type-H one-loss family from `GLOBAL_D3_ONE_LOSS_PATTERN_CAPACITY.md`:

- d=3;
- c=1;
- p=2;
- the common hub C={x} has `e_C=0`;
- every support D_i is K3, so `e_i=3`;
- distinct private petal pairs are target-anticomplete, so `c_ij=0`.

Dropping extra base incidences gives

> `3N+3k`
> ` <=Dcap(N+2k+2)-C(N+1,2)`.                              (S12)

This is the canonical Type-H owner-capacity inequality.

Equality would additionally force every non-owner base vertex to be anticomplete to every private petal not already certified.

## 7. d=3 Type-P family

For the nontrivial Type-P family:

- d=3;
- c=2;
- p=1;
- the common pair is a target edge, so `e_C=1`;
- support i has private charge `t_i in {1,2}` and
  `e_i=1+t_i`;
- private petals are pairwise target-anticomplete, so `c_ij=0`.

Then

`sum_i e_i-(k-1)e_C`
` =sum_i(1+t_i)-(k-1)`
` =1+sum_i t_i`.                                            (S13)

Therefore

> `3N+1+sum_i t_i`
> ` <=Dcap(N+k+3)-C(N+1,2)`.                               (S14)

Since every t_i>=1,

> `3N+1+k`
> ` <=Dcap(N+k+3)-C(N+1,2)`.                               (S15)

This is the canonical Type-P owner-capacity inequality.

## 8. d=2 common-hub one-loss family

For the d2 one-loss family:

- d=2;
- c=1;
- p=1;
- common hub has no internal edge (`e_C=0`);
- every support is target K2, so `e_i=1`;
- private leaves are pairwise target-anticomplete.

Thus

> `2N+k`
> ` <=Dcap(N+k+2)-C(N+1,2)`.                               (S16)

This is the canonical D2/A2 one-loss sunflower capacity inequality.

## 9. Why this matters for the global bridge

The zero-charge skeleton theorem reduces boundary one-loss systems to finitely many sunflower pattern families.

The present theorem then converts each entire pattern family, regardless of its owner multiplicity partition, into one scalar hereditary inequality.

Therefore the remaining work no longer needs to enumerate partitions such as `4+3+1`, `3+3+2`, etc. Owner multiplicities enter only through their sum N within the pattern family.

This is precisely the desired transition from case-heavy repeated-support arguments to one global structural theorem.

## 10. Generalization

The sunflower packing identity (S9) is independent of r=12 and of support size d. It applies to any common-core support family under any hereditary cap function.