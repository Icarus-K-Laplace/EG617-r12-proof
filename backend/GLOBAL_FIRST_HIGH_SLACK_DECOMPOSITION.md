# Global First-High-Slack Decomposition Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`;
- `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md`;
- `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md`;
- support repetition decoration and exact tau transport.

Purpose: give a complete layer decomposition of a common-support system at the first genuinely high-slack level `a=d`.

## 1. Setup

Let H satisfy

`alpha(H)<=r`.

Let Y be a common-S owner family with

`|S|=d`,
`a=d`,
`s=|S intersect X|<d`.                                      (A1)

For owner y define its q-loss

`ell_y=q-q_y>=0`                                             (A2)

and support defect

`Delta_y=w(D_y)+mu(D_y)=d-ell_y`.                           (A3)

Let

- `Y_0={y:ell_y=0}`;
- `Y_1={y:ell_y=1}`;
- `Y_+={y:ell_y>=2}`.

These are the plateau, one-loss and higher-loss layers.

## 2. Plateau layer is globally bounded

By `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`,

> `|Y_0|<=r`.                                                (A4)

For the r=12 residual core,

> `|Y_0|<=3`.                                                (A5)

Each plateau row belongs to a distinct singleton support class and contains a private clean zero-charge witness.

Thus the plateau layer is a bounded exceptional set, independent of the total owner count.

## 3. One-loss layer descends exactly to first-overlap allowance

For y in Y_1,

`Delta_y=d-1`.                                               (A6)

Suppose its support D_y properly overlaps a distinct support E in h points.

The joint-row overlap theorem gives

`h(d-h)<=Delta_y=d-1`.

But every proper overlap costs at least d-1. Therefore equality holds:

> `h(d-h)=d-1`,                                             (A7)
>
> `h in {1,d-1}`,                                           (A8)
>
> `w(D_y intersect E)=0`.                                   (A9)

Hence every proper overlap incident with a one-loss row is already an overlap-saturation equality event.

The ambient allowance d has disappeared from its local structure: the row behaves exactly like a support at allowance d-1.

## 4. Higher-loss layer is support-isolated

For y in Y_+,

`Delta_y<=d-2`.                                              (A10)

A proper overlap would require defect at least d-1, impossible.

Therefore

> every support of a row in Y_+ is disjoint from every distinct support class.   (A11)

Thus all higher-loss rows lie on globally isolated support classes.

Different owners may share one isolated repeated support class, but that class has no proper intersection with any other class.

## 5. Repeated support classes

Let D be a support class of multiplicity at least2.

Because s<d, every D-owner has strict q-loss.

If D properly overlaps a distinct class, Section3 forces

> every D-owner has `ell=1`,                                (A12)
>
> `Delta(D)=d-1`,                                           (A13)
>
> every shared overlap core has charge zero.                (A14)

If instead some D-owner has loss at least2, Section4 forces

> D is isolated from every distinct support class.          (A15)

Therefore every repeated support class belongs to exactly one of two structural types:

1. **boundary repeated class:** exact one-loss, overlap-saturated;
2. **deep-loss repeated class:** support-isolated.

There is no third repeated-support geometry.

## 6. Global decomposition

Combining Sections2--5:

> **First-High-Slack Decomposition Theorem.**
> A common-S support system with `a=d` and `s<d` decomposes into:
>
> 1. at most r singleton plateau rows;
> 2. a one-loss subsystem in which every proper overlap is an endpoint-overlap saturation event with zero shared charge;
> 3. a higher-loss subsystem consisting of support classes disjoint from every distinct class.
>
> Repeated support classes either lie in the one-loss equality subsystem or are isolated deep-loss blocks.   (A16)

For the r=12 core, the first part contains at most3 rows.

## 7. Global gain consequence

Let N be total owner count and P=|Y_0|.

Since every non-plateau row loses at least one unit,

`sum_y ell_y>=N-P>=N-r`.                                    (A17)

Thus

`Phi=sum_y Delta_y=Nd-sum_y ell_y`

satisfies

> `Phi<=N(d-1)+r`.                                          (A18)

For r=3,

> `Phi<=N(d-1)+3`.                                          (A19)

Any higher-loss rows sharpen the inequality by their excess loss beyond1.

## 8. d=2 / allowance2

For d=2:

- plateau layer: at most3 rows in general, and zero rows when s=0 by `GLOBAL_FIRST_HIGH_SLACK_S0_COLLAPSE.md`;
- one-loss supports have defect1; every proper overlap is one-point with zero shared charge;
- loss>=2 supports have defect0 and are disjoint from every distinct support.

Therefore the unresolved D2/A2 geometry is exactly a one-loss graph of support pairs plus isolated zero-defect blocks, with only a bounded plateau exception.

## 9. d=3 / allowance3

For d=3:

- plateau layer: at most3 rows;
- one-loss supports have defect2; proper overlaps have size1 or2 and zero shared charge;
- loss>=2 supports have defect at most1 and are disjoint from every distinct support.

When s=0 there is at most one plateau row, so at least N-1 owners are in the descended layers.

When s=1, `GLOBAL_FIRST_HIGH_SLACK_S1_SUNFLOWER_RIGIDITY.md` shows every plateau intersection component has at most two support classes.

Thus the only large interacting subsystem is the exact one-loss / defect-two support system.

## 10. The unique remaining first-high-slack bridge

After this theorem, there is only one genuinely nontrivial structural problem at allowance a=d:

> **One-Loss Component Rigidity Problem (OPEN).**
> Classify common-S support systems in which every interacting support has exact defect d-1, every proper overlap has size1 or d-1 with zero shared charge, and the core has small independence number.

All other rows are either a bounded plateau exception or disjoint support blocks handled by block-transversal / hereditary packing.

For r=12 this single problem simultaneously contains

- the D2 allowance-two equality geometry;
- the d3 allowance-three equality geometry.

Solving it would replace two major families of backend case analysis by one theorem.

## 11. Generalization

The decomposition is valid for arbitrary core independence bound r and uses no 35/211/E-layer constants. It is therefore a reusable pivot-compatibility theorem for any higher-r reduction with the same exact exchange and overlap identities.