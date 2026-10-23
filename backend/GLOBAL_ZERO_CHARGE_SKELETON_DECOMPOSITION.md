# Global Zero-Charge Skeleton Decomposition

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md`;
- common-S row closure.

Purpose: classify the incidence skeleton of the boundary one-loss subsystem. This turns the remaining overlap geometry into finitely many canonical common-core pattern families.

## 1. Setup

Let H satisfy

`alpha(H)<=r`.

Let F be a family of distinct d-point support classes arising from one common-S owner system.

Assume every support in the interacting subsystem is a boundary one-loss support:

`Delta(D)=d-1`.                                              (K1)

Assume also the loss-layer overlap conclusion:

> whenever distinct supports D,E properly overlap, every point of `D intersect E` has zero common-S charge.   (K2)

This is automatic at first high slack `a=d` by `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md`.

For a zero-charge support-union vertex v define its support-class incidence signature

`sigma(v)={D in F:v in D}`.                                 (K3)

## 2. At most r zero-charge signature classes

By `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`, zero-charge support vertices with distinct signatures are pairwise target-nonadjacent.

Hence there are at most r distinct signatures represented by zero-charge support vertices.

Let the corresponding signature classes be

`Z_1,...,Z_t`, `t<=r`.                                      (K4)

Every Z_i is a fixed common core of exactly the support classes in its signature.

## 3. Every support has a canonical zero skeleton

For a support D define

`Z(D)={v in D:w_v=0}`.                                      (K5)

If D contains one vertex of signature class Z_i, then `D in sigma(v)` for that vertex. Every other vertex of Z_i has the same signature, hence also lies in D.

Therefore

> `Z(D)` is a union of whole zero-charge signature classes.   (K6)

Equivalently there is a subset

`I(D) subseteq {1,...,t}`

such that

`Z(D)=union_(i in I(D)) Z_i`.                               (K7)

Call I(D) the **zero-skeleton pattern** of D.

Since t<=r, the number of nonempty possible zero-skeleton patterns is at most

> `2^r-1`.                                                   (K8)

For the r=12 core (`r=3`):

> at most seven nonempty zero-skeleton patterns occur.       (K9)

## 4. Supports with the same zero skeleton form a common-core sunflower

Let D,E be distinct supports with

`I(D)=I(E)=I`.                                               (K10)

Then their zero-charge sets are identical:

`Z(D)=Z(E)=C_I:=union_(i in I)Z_i`.                         (K11)

Any common vertex of D and E has zero charge by (K2). Therefore

`D intersect E subseteq C_I`.                               (K12)

Conversely every point of C_I lies in both supports by definition.

Hence

> `D intersect E=C_I`.                                      (K13)

Thus all distinct supports with one fixed zero-skeleton pattern form a sunflower with exact common core C_I and pairwise-disjoint private petals.

This is canonical: no additional case choice is involved.

## 5. Nontrivial pattern families have positive-charge private petals

Suppose one zero-skeleton pattern I is used by at least two distinct support classes.

Let u be a private petal of one support D in this pattern family.

If `w_u=0`, then u is a zero-charge support vertex with signature

`sigma(u)={D}`,                                             (K14)

because u is private to D among distinct support classes.

Then u belongs to an additional zero-charge signature class which is included in I(D) but not in the pattern of any other support E in the same family.

This contradicts `I(D)=I(E)`.

Therefore:

> every private petal in a nontrivial zero-skeleton pattern family has positive charge.   (K15)

Hence every such petal consumes at least one unit of support defect.

## 6. General density consequence

Let the common zero core of a nontrivial pattern family have size

`c=|C_I|`.                                                   (K16)

Each support has

`d-c`

private petals, all with positive integer charge by (K15). Therefore

`w(D)>=d-c`.                                                (K17)

Since the support has exact one-loss defect d-1,

`w(D)+mu(D)=d-1`,

so

> `mu(D)<=c-1`.                                              (K18)

Equivalently

> `e_H(D)>=C(d,2)-(c-1)`.                                   (K19)

Thus smaller common cores force denser supports.

This is the structural bridge from incidence signatures to hereditary edge packing.

## 7. d=3 canonical pattern families

Now specialize to d=3 and `alpha(H)<=3`.

A nontrivial pattern family cannot have common core size3, because two distinct 3-supports containing the same three-point core would be identical.

Hence only c=1 or c=2 are possible.

### Type H — common zero hub, c=1

Every support has two private petals.

By (K15), both have positive charge. Since total support defect is2,

`w(D)>=2`.

Therefore equality is forced:

> each private petal has charge1,
> `w(D)=2`,
> `mu(D)=0`,
> `H[D]=K3`.                                                 (K20)

Thus every nontrivial common-hub pattern family consists of target K3 supports with

- one zero-charge common hub;
- two private unit-charge petals per support.

### Type P — common zero pair, c=2

Every support has one private petal z with positive charge.

Equation (K18) gives

`mu(D)<=1`.                                                  (K21)

Thus every support is either

- a two-edge triple with private charge1 (`mu=1`), or
- a target K3 with private charge2 (`mu=0`).                 (K22)

Hence every nontrivial common-pair pattern family is a mixture of exactly these two dense support types.

### Type U — all-zero three-point core

A support with three zero-charge vertices has no private petal. Its pattern cannot be shared by a distinct support class, so it is a singleton pattern only.

Therefore all genuinely repeated pattern geometry is exhausted by Type H and Type P.

## 8. Four-set geometry is automatically excluded

The classical four-set triple family

`Q\{q_1},...,Q\{q_4}`

has four distinct shared core vertices, each with a different incidence signature (the unique omitted support differs).

In the one-loss subsystem all shared vertices are zero-charge.

This would create four distinct zero-charge incidence signatures, contradicting the r=3 signature capacity theorem.

Therefore:

> the full four-set family is impossible automatically.      (K23)

It need not be retained as a separate equality terminal in the r=12 one-loss bridge.

## 9. Finite skeleton theorem for r=12 d3 one-loss systems

Combining Sections3--8:

> Every d3 one-loss support system in the r=12 core is organized by at most seven zero-skeleton patterns.
>
> Every pattern used by multiple distinct support classes is exactly one of:
>
> 1. Type H: common zero hub + K3 supports with two unit-charge private petals;
> 2. Type P: common zero pair + two-edge/K3 supports with one charge1/2 private petal.
>
> Full four-set geometry is impossible.
>
> All remaining pattern classes are singletons.              (K24)

This is the desired canonical common-hub/common-pair classification derived from global invariants rather than local case enumeration.

## 10. Hereditary packing interface

For Type H, each support contributes

- 3 owner-support edges per owner;
- 3 internal target edges;
- two units of private charge.

For Type P, each support contributes

- 3 owner-support edges per owner;
- at least2 internal target edges;
- one or two units of private charge.

Therefore any large pattern family is expensive in both

- global charge Phi;
- hereditary induced-edge capacity.

`GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md` can now be applied family-by-family using the common zero core as part of the dense base or as a certified shared support core.

The remaining work is a quantitative owner-capacity theorem for Type H/P, not a new structural classification.

## 11. Generalization

Sections1--6 hold for arbitrary d and alpha(H)<=r. They show that a boundary one-loss system is controlled by at most `2^r-1` zero-skeleton patterns, each a common-core sunflower whose private petals carry positive charge.

The d3 Type-H/Type-P classification is the r=12 specialization.