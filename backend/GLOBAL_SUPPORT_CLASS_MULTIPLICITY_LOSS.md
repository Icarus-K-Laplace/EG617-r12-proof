# Global Support-Class Multiplicity Loss Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- exact common-S support-gain identity;
- exact tau transport;
- support repetition decoration;
- lexicographic maximality of `(q,tau)`.

Purpose: convert a bound on the number of distinct support classes directly into a mandatory total repivot loss, without inspecting individual incidence degrees.

## 1. Setup

Let Y be a common-S owner family with

- N owner rows;
- support size d;
- row allowance a;
- `s=|S intersect X|<d`.

Let the distinct support classes be

`C_1,...,C_k`

with owner multiplicities

`m_1,...,m_k`,

so

`sum_i m_i=N`.                                              (C1)

Let

`Phi=sum_v lambda_v w_v+sum_y mu(D_y)`.                     (C2)

The exact support-gain identity is

`sum_y(q-q_y)=Na-Phi`.                                      (C3)

## 2. Every repeated class forces strict loss on all its owners

If `m_i>=2`, every point of support class `C_i` is globally decorated by repetition.

Because `s<d`, an equal-q repivot through any owner of `C_i` would replace at most s decorated missing-set vertices by all d decorated support vertices, increasing tau.

Hence every owner belonging to a repeated class has

`q-q_y>=1`.                                                  (C4)

Let

`M_rep=sum_(i:m_i>=2)m_i`.                                  (C5)

Then

> `L=#{y:q_y<q}>=M_rep`.                                    (C6)

## 3. Pure class-count lower bound

Let x be the number of singleton support classes.

Then

`M_rep=N-x`.                                                 (C7)

If `N>k`, at least one class repeats, hence

`x<=k-1`.                                                    (C8)

Therefore

> if `N>k`, then
>
> `M_rep>=N-k+1`.                                           (C9)

Combining with (C6):

> `L>=N-k+1`.                                                (C10)

This lower bound depends only on owner count and distinct-class count.

## 4. Global compatibility consequence

Every strict loss is an integer at least1. By (C3) and (C10), if `N>k` then

> **Class-multiplicity compatibility inequality**
>
> `Phi+N-k+1<=Na`.                                          (C11)

Equivalently

> `Phi<=N(a-1)+k-1`.                                        (C12)

If a proposed support system violates (C11), maximality is impossible.

## 5. Capacity-to-loss transfer

Suppose an independent structural theorem gives

`k<=K`.                                                      (C13)

If `N>K`, then

> `L>=N-K+1`,                                                (C14)
>
> `Phi<=Na-(N-K+1)`.                                        (C15)

Thus every support-class capacity theorem automatically becomes a total repivot-loss theorem.

Examples of admissible inputs K include:

- a block-transversal capacity when all distinct supports are disjoint;
- a bounded-transversal rigidity theorem;
- an overlap-saturation classification which bounds the number of components/classes;
- a hereditary support-packing multiplicity classification.

This is the algebraic bridge from structural extraction to improving repivots.

## 6. Equality rigidity

Suppose equality holds in (C11).

Then:

1. exactly `k-1` support classes are singleton;
2. exactly one support class is repeated;
3. that repeated class has multiplicity `N-k+1`;
4. every owner in the repeated class loses exactly one q-unit;
5. every singleton owner is a q-plateau row;
6. the repeated support has exact defect `a-1`;
7. all other support defects equal a.

Indeed equality in (C9) forces the maximum possible number `k-1` of singleton classes, and equality in the total loss bound forces every counted loss to equal1 and every uncounted row to be plateau.

Thus the scalar equality state already collapses to one macroscopic repeated support plus singleton plateau classes.

## 7. Low-allowance applications

### d=3, a<=1

`GLOBAL_D3_ALLOWANCE_ONE_COLLAPSE.md` gives at most three distinct support classes.

Hence for N>=4,

`L>=N-2`,                                                    (C16)

and

`Phi<=Na-(N-2)`.                                             (C17)

For N=11,a=1,

> `L>=9`, `Phi<=2`.                                         (C18)

Therefore an eleven-owner allowance-one triple system has almost no total defect mass available after repetition is accounted for.

If equality holds, there is exactly one repeated zero-charge K3 support of multiplicity9 and two singleton plateau supports.

This is stronger than treating eleven views independently.

### d=2, a<=1

Whenever a D2 low-allowance theorem bounds the number of distinct support classes by K, (C14)--(C15) convert that capacity directly into a repivot-loss penalty.

## 8. First-high-slack applications

At allowance `a=d`, `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md` supplies extra forced-loss singleton classes through high decorated overlap.

The present theorem supplies the repetition part independently:

`L>=M_rep>=N-k+1` whenever N>k.

Thus first-high-slack analysis can add

- class-count repetition loss;
- high-overlap singleton loss;
- forced-decorated-incidence loss

without double-counting repeated owners.

## 9. Generalization

No r=12-specific numerical constant appears. The theorem is a direct consequence of repeated-support decoration and lexicographic maximality, so it applies to any analogous pivot/repivot system.