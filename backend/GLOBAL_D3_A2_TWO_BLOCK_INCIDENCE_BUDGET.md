# Global d=3 A2 Two-Block Incidence Budget

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_Q32_NINE_OWNER_FULLY_DECORATED_TRANSVERSAL_REDUCTION.md`;
- `GLOBAL_D3_A2_INTERSECTING_COMPONENT_CAPACITY.md`;
- inherited cap `D(17)=81`;
- the canonical K11 base in the nine-owner fully-decorated q32 state.

Purpose: replace the remaining six-point-transversal problem by a weighted two-block incidence inequality.

## 1. Canonical maximal matching

By the preceding theorems, the final nine-owner fully-decorated support hypergraph has matching number exactly2.

Choose a maximal disjoint pair of distinct supports

`D,E`, `D intersect E=empty`.

Let their owner multiplicities be

`m_D,m_E`,

and put

`M=m_D+m_E`.

Let

`C=D union E`, `|C|=6`.

By maximality of the matching, every other support class meets C.

Partition the remaining support classes into:

- **D-side:** meets D but is disjoint from E;
- **E-side:** meets E but is disjoint from D;
- **bridges:** meets both D and E.

Let b be the total owner multiplicity carried by bridge support classes.

## 2. Every owner contributes a certified number of B--C edges

Let

`B={p} union Y union {r}=K11`

be the canonical dense base.

Owners of D or E have all three of their core neighbours in C. Hence they contribute

`3M`

target B--C edges.

A bridge support meets both D and E, so every bridge owner has at least two of its three core neighbours in C. Hence bridge owners contribute at least

`2b`

target B--C edges.

Every remaining owner lies on a D-side or E-side support and therefore has at least one core neighbour in C. There are

`9-M-b`

such owners, contributing at least that many target B--C edges.

Thus the total certified B--C owner incidence is at least

> `I_C >= 3M+2b+(9-M-b)=9+2M+b`.                            (B1)

Any r--C target edge only strengthens the estimate and is omitted below.

## 3. D17 gives the global two-block budget

Inside C, both D and E contain at least one internal target edge because every d3 support at allowance2 has `e_H>=1`.

Hence

`e_H(C)>=2`.                                                  (B2)

The induced set `B union C` has17 vertices. The inherited cap is

`D(17)=81`.

Therefore

`55 + I_C + e_H(C) <=81`.

Using (B1):

> `2M+b+e_H(C) <=17`.                                       (B3)

In particular, since `e_H(C)>=2`,

> **two-block incidence budget**
>
> `2M+b <=15`.                                               (B4)

This is a single scalar constraint on the whole residual family; it does not depend on the number of side-support classes.

## 4. Consequences

### 4.1 The maximal disjoint pair carries at most seven owners

From b>=0 and (B2)--(B3):

`2M<=15`,

so

> `M<=7`.                                                     (B5)

This strengthens the earlier pairwise hereditary bound `M<=8` by using the fact that every remaining owner must hit the maximal-matching cover C.

Hence at least

> `9-M>=2`                                                    (B6)

owners lie on support classes different from D and E.

### 4.2 High-M windows are sharply constrained

If `M=7`, then (B3) gives

`b+e_H(C)<=3`.

Since `e_H(C)>=2`,

> `b<=1`.                                                     (B7)

Thus in the M=7 window at most one owner can lie on a bridge support; every other residual owner is one-sided.

If `M=6`,

> `b+e_H(C)<=5`,

so

> `b<=3`.                                                     (B8)

If `M=5`,

> `b<=5`.                                                     (B9)

The bridge multiplicity is therefore automatically small when the maximal disjoint pair is heavy.

## 5. One-sided subfamilies are intersecting

Let L be the family consisting of D together with all D-side support classes.

Any two D-side supports must intersect: if F,G were disjoint, then F,G,E would be three pairwise-disjoint support classes, contradicting matching number2.

Every D-side support also intersects D by definition.

Therefore

> L is pairwise intersecting.                                (B10)

Similarly, E together with all E-side supports forms a pairwise-intersecting family R.

The intersecting-component capacity theorem therefore gives

> owner multiplicity on L <=8,                               (B11)
>
> owner multiplicity on R <=8.                               (B12)

More sharply, if either side has no global common hub geometry, its owner capacity is at most6.

Thus the only way the total nine-owner family can remain close to capacity is for at least one side to sit in the three-class common-hub equality regime.

## 6. Remaining bridge theorem

After (B3)--(B12), the final fully-decorated N=9 problem is reduced to:

> **Two-Block Bridge Rigidity Lemma (OPEN).**
> In the q32/CORE211 allowance-two equality state, let D,E be a maximal disjoint support pair. Under
>
> - `2(m_D+m_E)+b+e_H(D union E)<=17`;
> - pairwise-intersecting D-side and E-side families;
> - at most three zero-charge incidence signatures;
> - total common-S charge `W<=36`;
> - total core decoration `G_H<=28`;
>
> the nine-owner support system cannot be realized.

This is now the unique owner-count bridge for the fully-decorated q32 d3 equality state.

It is structurally a weighted two-block theorem, not an eleven-view or E334-specific case split.

## 7. Generalization

The incidence argument is parameterized by

- dense-base edge count;
- support size;
- maximal-matching size;
- hereditary cap.

For any higher-r analogue with a canonical dense owner base, a maximal support matching yields the same type of weighted cover budget.
