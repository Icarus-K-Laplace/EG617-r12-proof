# Global d=2 One-Loss Pattern Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: close the structural classification of the d2 boundary one-loss subsystem arising from first-high-slack allowance2.

## 1. Setup

Work in a common-S d2 subsystem in which every interacting owner row has exact one-unit q-loss at ambient allowance2.

Thus every support D has

`|D|=2`,
`Delta(D)=w(D)+mu(D)=1`.                                    (D1)

Any proper overlap between distinct support classes has size1 and the shared core vertex has zero charge by `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md`.

## 2. Nontrivial zero-skeleton pattern families have a common hub

By `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`, support classes with the same zero-skeleton pattern form a common-core sunflower.

For d=2, a nontrivial family of distinct supports cannot have common core size2, because then the supports would be identical.

Therefore every nontrivial pattern family has common core size1:

> there is a zero-charge hub x and distinct supports
> `D_i={x,u_i}`.                                             (D2)

The private endpoints u_i are pairwise distinct.

## 3. Private endpoints have exact charge one

Because the pattern family is nontrivial, every private endpoint has positive charge by the zero-skeleton decomposition theorem.

Thus

`w_(u_i)>=1`.                                                (D3)

The hub has

`w_x=0`.                                                     (D4)

Since the total support defect is exactly1,

`w_(u_i)+mu(D_i)=1`.                                        (D5)

Both terms are nonnegative integers and (D3) holds, so equality is forced:

> `w_(u_i)=1`,                                               (D6)
>
> `mu(D_i)=0`.                                               (D7)

Therefore

> every support in a nontrivial d2 one-loss pattern family is a target K2.   (D8)

## 4. Leaves are pairwise target-nonadjacent

Take two distinct supports

`D_i={x,u_i}`,
`D_j={x,u_j}`.

Since D_i is a target K2,

`u_i x`

is a target edge.

Apply row closure to u_i against support D_j. Because

`w_(u_i)=1`,

`e_H(u_i,D_j)<=1`.                                          (D9)

But u_i already has the target neighbour x inside D_j. Hence the entire allowance is consumed and

> `u_i u_j` is a target nonedge.                             (D10)

Thus all private leaves in the common-hub family are pairwise target-anticomplete.

## 5. Class capacity

Choose the private endpoint from each distinct support class.

By (D10), these leaves form an independent set in H.

Since `alpha(H)<=3`,

> **d2 one-loss common-hub capacity:** at most three distinct support classes.   (D11)

If the pattern family carries M owner rows, some support class has owner multiplicity at least

> `ceil(M/3)`.                                               (D12)

Hence a large d2/A2 one-loss family automatically becomes a repeated-K2 problem.

## 6. Complete one-loss structural picture for d2

The boundary d2 one-loss subsystem consists of finitely many zero-skeleton pattern families.

Every nontrivial pattern family is exactly:

- one zero-charge common hub;
- at most3 target-K2 support classes;
- one private charge1 leaf per support;
- private leaves pairwise target-nonadjacent.

All other support patterns are singletons.

No additional overlap geometry exists.

## 7. Bridge to hereditary packing

Within a nontrivial pattern family, owner count M is concentrated on at most3 support classes.

Therefore some K2 support repeats at least `ceil(M/3)` times.

`GLOBAL_REPEATED_SUPPORT_PACKING_BRIDGE.md` converts this multiplicity directly into a hereditary dense-base inequality.

Thus the remaining D2/A2 problem is quantitative owner packing, not structural overlap classification.

## 8. Generalization

With `alpha(H)<=r`, the same proof gives at most r distinct support classes in one common-hub d2 one-loss pattern family.