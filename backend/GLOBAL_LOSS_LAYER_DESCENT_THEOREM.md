# Global Loss-Layer Descent Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- exact common-S exchange identity;
- common-S joint-row overlap inequality;
- `GLOBAL_OVERLAP_SATURATION_THEOREM.md`.

Purpose: show that repivot q-loss is not merely a contradiction budget; it lowers the effective structural allowance of that support row. In the first-high-slack regime this automatically sends almost all rows back into the already-classified low-allowance geometry.

## 1. Setup

Let Y be a common-S owner family with support size d and common row allowance a.

For owner y with support D_y write

`Delta_y=w(D_y)+mu(D_y)`.                                   (D1)

The exact exchange identity gives

> `ell_y:=q-q_y=a-Delta_y`.                                 (D2)

Thus

> `Delta_y=a-ell_y`.                                        (D3)

We call `a-ell_y` the **effective allowance** of row y.

## 2. q-loss forbids overlap once the effective allowance drops below d-1

Suppose D_y properly overlaps a distinct support E in

`h=|D_y intersect E|`, `1<=h<=d-1`.

The joint-row theorem, applied with D_y as the constrained row, gives

`h(d-h)<=w(D_y\E)+mu(D_y)<=Delta_y`.                        (D4)

But every proper overlap satisfies

`h(d-h)>=d-1`.                                              (D5)

Therefore proper overlap requires

> `Delta_y>=d-1`,                                            (D6)

or equivalently

> `ell_y<=a-(d-1)`.                                         (D7)

Hence:

> **Loss-layer disjointness principle.**
> If
> `ell_y>a-(d-1)`,
> then D_y is disjoint from every distinct support class.    (D8)

This is row-specific and does not require a global low-allowance hypothesis.

## 3. Boundary loss forces overlap saturation

Suppose

`ell_y=a-(d-1)`.                                            (D9)

Then

`Delta_y=d-1`.                                              (D10)

If D_y properly overlaps E, equations (D4)--(D5) force equality:

> `h(d-h)=d-1`,                                             (D11)
>
> `h in {1,d-1}`,                                           (D12)
>
> `w(D_y intersect E)=0`.                                   (D13)

Thus a row exactly at the overlap-loss boundary behaves like a support in the first-overlap allowance theorem, even if the ambient common-S family has larger allowance.

This is the key descent mechanism.

## 4. First-high-slack trichotomy

Now specialize to

`a=d`.                                                       (D14)

Then the owner rows split into three structural loss layers.

### Layer 0: plateau rows, ell=0

These have effective allowance d.

If `s=|S intersect X|<d`, `GLOBAL_PLATEAU_CAPACITY_THEOREM.md` gives at most `alpha(H)` such rows; in the r=12 residual core, at most3.

### Layer 1: exact one-loss rows, ell=1

These have

`Delta_y=d-1`.                                              (D15)

If such a row properly overlaps another class, the overlap is automatically saturated:

- size1 or d-1;
- shared charge zero.

Thus every one-loss overlap lies in the equality geometry of `GLOBAL_OVERLAP_SATURATION_THEOREM.md`, even though the ambient family allowance is d.

### Layer 2+: ell>=2

These rows have

`Delta_y<=d-2`.                                             (D16)

By (D8), their supports are disjoint from every distinct support class.

Therefore:

> **First-high-slack descent trichotomy**
>
> every row is either
> 1. one of a few plateau rows;
> 2. an exact one-loss overlap-saturation row;
> 3. a higher-loss row whose support is globally isolated from all distinct support classes.   (D17)

This removes arbitrary high-slack overlap geometry from the problem.

## 5. Repeated support consequence

Assume `s<d` and a support class D repeats.

Every D-owner has `ell>=1` by tau-maximality.

If D properly overlaps a distinct class, the overlap lower bound gives `Delta(D)>=d-1`. At first high slack a=d this forces

`ell=1`, `Delta(D)=d-1`.                                    (D18)

Hence:

> a repeated support with loss at least2 is isolated from every distinct support class.   (D19)

Conversely every repeated support which participates in the support-intersection graph is automatically an exact one-loss equality support.

## 6. d=2 / allowance2 specialization

Take `d=2,a=2`.

- plateau rows: effective allowance2;
- one-loss rows: effective allowance1, and any overlap is a saturated one-point overlap with shared charge0;
- loss>=2 rows: effective allowance0 and are disjoint from every distinct support.

Thus all non-plateau D2 overlap geometry has already descended into the allowance-one equality theorem.

The genuinely new information in D2/A2 is only how the few plateau rows attach to this descended system.

## 7. d=3 / allowance3 specialization

Take `d=3,a=3`.

- plateau rows: at most3 when `s<3`;
- one-loss rows: effective allowance2; any proper overlap has size1 or2 and zero shared charge;
- loss>=2 rows: disjoint from every distinct support.

Therefore the large non-plateau part of a d3/A3 owner family is governed by the same overlap cost as the already-classified allowance-two system.

The only missing ingredient is an equality-rigidity theorem for the one-loss support-intersection components without using plateau tau constraints.

## 8. General allowance version

For arbitrary a, define the overlap-loss threshold

`ell_star=a-(d-1)`.                                         (D20)

Then:

- rows with `ell>ell_star` are support-isolated;
- rows with `ell=ell_star` are overlap-saturated with endpoint overlap and zero shared charge;
- only rows with `ell<ell_star` retain genuine overlap slack.

Thus any repivot loss automatically descends the row through a finite hierarchy of structural allowance regimes.

## 9. Significance for the global bridge

The global high-backend proof should therefore be organized by loss layer, not by edge layer:

1. bound the number of plateau rows globally;
2. classify the boundary one-loss equality components;
3. handle higher-loss rows by disjoint block-transversal / hereditary packing.

This is a direct structural route from the global gain identity to a finite equality classification.

## 10. Generalization

No r=12-specific numerical constants are used. The theorem follows from the exact exchange identity and universal overlap cost, and therefore applies to any analogous pivot/repivot system.