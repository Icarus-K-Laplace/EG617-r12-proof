# Global First-High-Slack Owner-Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_FIRST_HIGH_SLACK_DECOMPOSITION.md`;
- `GLOBAL_ZERO_CHARGE_SKELETON_DECOMPOSITION.md`;
- `GLOBAL_D3_ONE_LOSS_PATTERN_CAPACITY.md`;
- `GLOBAL_D2_ONE_LOSS_PATTERN_CAPACITY.md`;
- `GLOBAL_SUNFLOWER_SUPPORT_PACKING_THEOREM.md`;
- `GLOBAL_D3_PATTERN_CHARGE_BARRIERS.md`;
- `GLOBAL_D2_PATTERN_CHARGE_BARRIER.md`;
- the retained r=12 hereditary cap `Dcap(t)=C(t,2)-11(t-12)` for `12<=t<24`.

Purpose: collapse the owner-count part of the first-high-slack equality bridge into one theorem. The result treats d2/A2 and d3/A3 by the same sunflower-packing mechanism rather than by E-layer-specific multiplicity partitions.

## 1. Canonical first-high-slack pattern families

At allowance `a=d` with `s<d`, the global decomposition theorem reduces every large interacting subsystem to exact one-loss rows.

The zero-charge skeleton theorem then shows that every nontrivial one-loss pattern family is a common-core sunflower.

For the r=12 core (`alpha(H)<=3`), the only relevant pattern families are:

1. **d=2 Type D:** one zero-charge hub and target-K2 supports `{x,u_i}`;
2. **d=3 Type H:** one zero-charge hub and target-K3 supports `{x,u_i,v_i}`;
3. **d=3 Type P:** one zero-charge target-edge pair `{x,y}` and supports `{x,y,z_i}` with private charge `t_i in {1,2}`.

Each pattern contains at most three distinct support classes.

Let

- `N` be the total number of owners in the pattern family;
- `k` be the number of distinct support classes in the pattern, so `1<=k<=3`.

The common-S owner clique gives the canonical base

`B={p} union Y=K_(N+1)`.

## 2. Hereditary cap formula

For the retained r=12 cap, whenever `12<=t<24`,

`Dcap(t)=C(t,2)-11(t-12)`.                                  (C1)

All sets used below have order at most18, so (C1) applies.

## 3. d=2 common-hub owner capacity

The sunflower packing theorem gives

`2N+k <= Dcap(N+k+2)-C(N+1,2)`.                             (C2)

For `k=1`, the right side simplifies to

`102-9N`.

Thus

`2N+1<=102-9N`,

so

`11N<=101` and

> `N<=9`.                                                     (C3)

For `k=2`, the right side is

`94-8N`,

so

`2N+2<=94-8N`,

hence

`10N<=92` and again

> `N<=9`.                                                     (C4)

For `k=3`, the right side is

`87-7N`,

so

`2N+3<=87-7N`,

hence

`9N<=84` and

> `N<=9`.                                                     (C5)

Therefore:

> **d2 first-high-slack pattern capacity:** every nontrivial d2 one-loss common-hub pattern has at most9 owners.   (C6)

If the pattern has three distinct classes, `GLOBAL_D2_PATTERN_CHARGE_BARRIER.md` additionally gives

`W>=34`                                                     (C7)

in the 35-core.

Thus at total charge `W<=33`, every d2 one-loss pattern has at most two distinct support classes while still satisfying the owner cap N<=9.

## 4. d=3 Type-H owner capacity

The Type-H sunflower inequality is

`3N+3k <= Dcap(N+2k+2)-C(N+1,2)`.                           (C8)

### k=1

The right side is

`94-8N`.

Hence

`3N+3<=94-8N`,

so

`11N<=91` and

> `N<=8`.                                                     (C9)

### k=2

The right side is

`81-6N`.

Hence

`3N+6<=81-6N`,

so

`9N<=75` and

> `N<=8`.                                                     (C10)

### k=3

The right side is

`72-4N`.

Hence

`3N+9<=72-4N`,

so

`7N<=63` and

> `N<=9`.                                                     (C11)

Therefore a Type-H pattern has at most9 owners in general.

But the three-class Type-H charge barrier is

`W>=62`                                                     (C12)

in the 35-core.

Hence whenever

`W<=61`,

`k=3` is impossible. Only `k<=2` remains, and (C9)--(C10) give

> **Type-H low-charge capacity:** `W<=61 => N<=8`.            (C13)

In particular every q32/core211 common-S subsystem satisfies `W<=37` by the charge-localization theorem, so any Type-H one-loss pattern occurring there has

> `N<=8`.                                                     (C14)

## 5. d=3 Type-P owner capacity

The Type-P sunflower theorem gives the crude but universal inequality

`3N+1+k <= Dcap(N+k+3)-C(N+1,2)`.                           (C15)

### k=1

The right side is

`94-8N`.

Thus

`3N+2<=94-8N`,

so

`11N<=92` and

> `N<=8`.                                                     (C16)

### k=2

The right side is

`87-7N`.

Thus

`3N+3<=87-7N`,

so

`10N<=84` and

> `N<=8`.                                                     (C17)

### k=3

The right side is

`81-6N`.

Thus

`3N+4<=81-6N`,

so

`9N<=77` and

> `N<=8`.                                                     (C18)

Therefore:

> **Type-P first-high-slack pattern capacity:** every nontrivial Type-P one-loss pattern has at most8 owners.   (C19)

No additional charge hypothesis is needed.

If k=3, the separate charge barrier also gives

`W>=33`,                                                     (C20)

which is useful for equality localization.

## 6. Unified d3 first-high-slack capacity

Every nontrivial d3 one-loss pattern is Type H or Type P.

Therefore, under the mild low-charge condition

`W<=61`,

both types satisfy

> **`N<=8`.**                                                 (C21)

For the low-excess backend channels of present interest, charge localization is far below61, so the effective owner capacity is uniformly eight across the entire d3 one-loss equality geometry.

This removes the need to enumerate multiplicity partitions such as

`4+3+1`, `3+3+2`, `4+2+2`, etc.

They are all subsumed by one sunflower owner-capacity theorem.

## 7. Equality windows

The theorem also identifies the only numerically sharp regimes worth further attention:

- d2, N=9;
- d3 Type H, N=8 at low charge;
- d3 Type P, N=8.

Any owner count above these thresholds is killed by hereditary packing before detailed support geometry is considered.

If equality is attained, the sunflower support-packing theorem forces all omitted base--petal and petal--petal incidences to vanish and the induced set to saturate its hereditary cap. Hence each numerical boundary is automatically a rigid adjacency geometry.

## 8. Global-bridge interpretation

The first-high-slack bridge now has the following universal form:

1. plateau rows form a bounded exceptional set (`<=3`);
2. higher-loss rows lie on isolated support blocks;
3. interacting one-loss rows decompose into zero-skeleton sunflower patterns;
4. each nontrivial pattern has at most three distinct support classes;
5. hereditary sunflower packing bounds the total owners of the whole pattern by 9 for d2 and 8 for d3 in the low-charge regime.

Thus the remaining first-high-slack task is no longer support-pattern or multiplicity classification. It is only to show that the forcing input demands more owners than these global capacities, or to exclude the finite equality windows above.

## 9. Generalization

The structural decomposition and sunflower packing are parameterized in d, the core independence bound, and the hereditary cap function.

The numerical capacities 9 and8 use the r=12 cap (C1), but the proof template transfers verbatim to higher r after substituting the corresponding cap function.