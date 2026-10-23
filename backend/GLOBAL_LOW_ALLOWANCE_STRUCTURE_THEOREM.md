# Global Low-Allowance Support Structure Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- `GLOBAL_OVERLAP_SATURATION_THEOREM.md`;
- exact tau transport and lexicographic maximality.

Purpose: identify the exact structural boundary between support systems that are governed by generic global compatibility and those that genuinely require new high-slack ideas.

## 1. Setup

Let Y be a common-S owner family with support size

`|D_y|=d`.

Let a be the common row allowance and write

`w(D)+mu(D)<=a`,

where

`mu(D)=C(d,2)-e_H(D)`.

Assume

`alpha(H)<=3`.

Let

`s=|S intersect X|`.

## 2. Minimum proper-overlap cost

For two distinct common-S supports D,E with proper overlap

`h=|D intersect E|`, `1<=h<=d-1`,

the joint-row theorem gives

`h(d-h)<=a`.                                                (L1)

For every proper overlap,

`h(d-h)>=d-1`.                                              (L2)

Therefore the entire low-allowance range splits at the universal threshold

> `a=d-1`.                                                   (L3)

No r=12-specific constant enters this threshold.

## 3. Strict low allowance: a<d-1

Assume

`a<d-1`.

Then (L1)--(L2) show that proper overlap is impossible.

Hence

> any two distinct support classes are disjoint.             (L4)

For disjoint supports D,E, row closure gives

`e_H(D,E)<=min(w(D),w(E))`
`          <=a`.                                            (L5)

Thus the distinct support classes form a block system with

- block size d;
- pairwise target cross-edge count at most a.

Therefore every block-transversal capacity theorem applies immediately.

Let `T(d,a)` be any certified capacity threshold for such disjoint d-blocks in a graph with independence number at most3. Then

> number of distinct support classes `<=T(d,a)`.             (L6)

There is no local support-case analysis left in this regime.

## 4. Repeated classes in the strict low-allowance regime

Suppose `s<d` and a support class D repeats.

Every point of D is globally decorated. Equal-q repivoting would therefore increase tau, so every D-owner has strict q-loss.

Hence

`w(D)+mu(D)<=a-1`.                                         (L7)

Thus repeated support classes are even lower-defect objects than singleton classes.

Combining (L6) with owner count N gives

> some support class has multiplicity at least
>
> `ceil(N/T(d,a))`.                                         (L8)

If this class repeats, (L7) applies.

Therefore a large owner family in the strict low-allowance regime automatically becomes a high-multiplicity low-defect support problem.

## 5. First-overlap allowance: a=d-1

Assume

`a=d-1`.

Then `GLOBAL_OVERLAP_SATURATION_THEOREM.md` applies.

Every proper overlap is forced to equality:

- overlap size is 1 or d-1;
- both supports are q-plateau rows;
- shared vertices have zero charge;
- shared vertices are globally decorated;
- the overlap size cannot exceed s.

Thus proper overlap is no longer a free combinatorial event: it is an equality certificate.

## 6. First-overlap geometry when s=0 or1

### s=0

No proper overlap is possible even at allowance d-1.

Hence the system falls back to the disjoint-block regime with cross allowance at most d-1.

### s=1

Every proper overlap has size1, and each nontrivial intersection component is a common-hub sunflower.

Every sunflower support has

- one zero-charge decorated hub;
- d-1 private clean zero-charge vertices;
- exact internal missing count `mu=d-1`;
- exact internal target-edge count `C(d-1,2)`.

Repeated support classes cannot belong to these components and have defect at most d-2.

Therefore the entire family decomposes into

1. isolated repeated low-defect supports;
2. exact common-hub sunflower equality components;
3. singleton disjoint supports.

This is the complete generic structure at the first-overlap threshold.

## 7. Unified low-allowance theorem

Combining Sections3--6:

> **Global Low-Allowance Structure Theorem.**
> For a common-S support family of size d under the maximal-pivot contract:
>
> - if `a<d-1`, all distinct supports are disjoint and global block-transversal capacity applies;
> - if `a=d-1`, every proper overlap is a saturated equality event and the support system decomposes into explicit overlap-equality components plus isolated repeated supports;
> - when `s<d`, every repeated class has one less unit of available defect than a singleton class.

Thus the first genuinely new support-incidence regime begins only at

> `a>=d`.                                                    (L9)

## 8. r=12 specializations

### d=2

The generic low-allowance range is

- `a=0`: strict low allowance;
- `a=1=d-1`: first-overlap equality.

So D2 allowance-zero/one systems do not require layer-specific arguments.

At a=1,s=1, nontrivial overlap components are common-hub stars of target-nonedge support pairs with clean private endpoints, while repeated supports are isolated zero-defect target K2s.

The first genuinely higher-slack D2 regime is allowance2.

### d=3

The generic low-allowance range is

- `a=0,1`: strict low allowance;
- `a=2=d-1`: first-overlap equality.

Thus d3 allowance0/1/2 systems are structurally controlled by one theorem.

The first genuinely higher-slack triple-support regime is

> `a=3`.                                                     (L10)

This identifies the allowance-three residual in the E334 source-reported frontier as a genuinely new structural threshold rather than merely another case.

## 9. Connection to the global bridge

The low-support bridge should therefore be organized by allowance threshold, not by E-layer:

### Regime A: `a<d-1`

Use disjoint block-transversal capacity + multiplicity concentration + hereditary support packing.

### Regime B: `a=d-1`

Use overlap-saturation rigidity + sunflower/repeated-block equality exclusion.

### Regime C: `a>=d`

This is the only regime requiring genuinely new high-slack compatibility theorems.

For the current r=12 backend, this collapses many nominal residual cases into just two difficult high-slack objects:

- D2 allowance2/3 type systems;
- d3 allowance3 type systems.

That is the minimal structural split suggested by the present theory.

## 10. Generalization beyond r=12

The threshold `a=d-1` comes only from the universal overlap cost `h(d-h)`.

Hence the theorem is independent of

- core size35;
- CORE211;
- edge layers333--340;
- the value r=12.

Any higher-r pivot system with the same exact support-overlap inequality inherits the same low-allowance structural boundary.