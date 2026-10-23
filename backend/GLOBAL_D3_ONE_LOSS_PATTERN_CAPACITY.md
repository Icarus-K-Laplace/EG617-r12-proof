# Global d=3 One-Loss Pattern Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: bound the canonical Type-H and Type-P pattern families arising in d3 boundary one-loss systems. This converts the remaining structural families into high owner-multiplicity repeated-support problems.

## 1. Setup

Work in the d3 one-loss subsystem:

`Delta(D)=w(D)+mu(D)=2`.                                    (C1)

By `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`, every nontrivial zero-skeleton pattern family is one of:

- **Type H:** a common zero-charge hub x and supports `D_i={x,u_i,v_i}` which are target K3s, with `w_(u_i)=w_(v_i)=1`;
- **Type P:** a common zero-charge pair `{x,y}` and supports `D_i={x,y,z_i}`, where private petal `z_i` has charge1 or2 and the support has respectively two or three internal target edges.

Private petals from distinct supports are distinct.

## 2. Type-H cross-petal anticompleteness

Let

`D_i={x,u_i,v_i}`,
`D_j={x,u_j,v_j}`

be distinct Type-H supports.

Because D_i is K3,

`u_i x` and `v_i x`

are target edges.

Apply row closure to `u_i` against support D_j. Since

`w_(u_i)=1`,

we have

`e_H(u_i,D_j)<=1`.                                         (C2)

But the edge `u_i x` is already one target edge into D_j. Hence

`u_i u_j`, `u_i v_j`

are target nonedges.                                        (C3)

The same applies to v_i.

Therefore:

> every private petal of one Type-H support is target-anticomplete to the private petals of every other Type-H support.   (C4)

## 3. Type-H class capacity

Choose one private petal from each distinct Type-H support.

By (C4), all chosen petals are pairwise target-nonadjacent.

Since `alpha(H)<=3`, there can be at most three chosen petals.

Therefore

> **Type-H capacity:** at most three distinct support classes occur in one common-hub pattern family.   (C5)

If the family carries M owner rows, some support class has owner multiplicity at least

> `ceil(M/3)`.                                               (C6)

Thus a large Type-H owner family automatically becomes a repeated-K3 problem.

## 4. Type-P common pair must be a target edge

Let the common zero pair be `{x,y}`.

Suppose first that xy is a target nonedge.

Consider any support

`D_i={x,y,z_i}`.

The support has at least two internal target edges by the Type-P classification.

Since xy is a nonedge, both target edges must be

`z_i x` and `z_i y`.                                        (C7)

This is the two-edge support case, so `w_(z_i)=1`.

If the Type-P family is nontrivial, take another support D_j. Row closure applied to z_i against D_j gives

`e_H(z_i,D_j)<=w_(z_i)=1`.                                  (C8)

But D_j contains both x and y, and (C7) already gives two target neighbours of z_i inside D_j, contradiction.

Therefore:

> a nontrivial Type-P pattern family cannot have a target-nonedge common pair.   (C9)

Hence in every nontrivial Type-P family

> `xy` is a target edge.                                    (C10)

## 5. Type-P private petals are pairwise target-nonadjacent

Let D_i and D_j be distinct supports in a nontrivial Type-P family.

Write

`t_i=w_(z_i) in {1,2}`.                                     (C11)

Because xy is a target edge and the support has

`e_H(D_i)=1+t_i`,                                           (C12)

the private petal z_i has exactly t_i target neighbours in the common pair `{x,y}`.

Indeed:

- if `t_i=1`, D_i has two internal edges: xy plus exactly one z_i--pair edge;
- if `t_i=2`, D_i is K3 and z_i sees both x,y.

Apply row closure to z_i against D_j:

`e_H(z_i,D_j)<=t_i`.                                        (C13)

But the t_i neighbours of z_i in `{x,y}` already lie inside D_j and already consume the full row-closure allowance.

Therefore

> `z_i z_j` is a target nonedge.                            (C14)

Thus all private petals of distinct Type-P supports are pairwise target-anticomplete.

## 6. Type-P class capacity

Choose the unique private petal from each distinct Type-P support.

By (C14), these petals form an independent set in H.

Hence `alpha(H)<=3` gives

> **Type-P capacity:** at most three distinct support classes occur in one common-pair pattern family.   (C15)

If the family carries M owner rows, some support class has multiplicity at least

> `ceil(M/3)`.                                               (C16)

## 7. Canonical repeated-support consequence

Every nontrivial one-loss pattern family is now capacity-bounded at three distinct support classes.

Therefore any such family with at least four owner rows contains a repeated support.

More quantitatively, for M owner rows:

> max support multiplicity `>=ceil(M/3)`.                   (C17)

Combined with `GLOBAL_REPEATED_SUPPORT_PACKING_BRIDGE.md`, the remaining contradiction becomes a dense-base hereditary multiplicity test rather than further support-pattern classification.

## 8. Structural summary

The boundary d3 one-loss system has the following canonical behavior:

- full four-set geometry is impossible by zero-charge signature capacity;
- common-hub pattern families consist of K3 supports and have at most3 classes;
- common-pair pattern families require a target-edge common pair, have private petals pairwise anticomplete, and have at most3 classes;
- all large owner multiplicity is therefore concentrated on at most3 support classes within each pattern family.

This is the quantitative form of the common-hub/common-pair equality rigidity requested for the global bridge.

## 9. Generalization

The proof uses the d3 exact defect arithmetic and `alpha(H)<=3`. The same mechanism extends to larger core independence bounds r with the class-capacity `<=r` after replacing the final independent-set bound.