# Global First-High-Slack Rigidity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- exact common-S joint-row overlap inequality;
- exact decoration transport and support-overlap decoration;
- lexicographic maximality of `(q,tau)`.

Purpose: classify the first genuinely higher-slack regime

`a=d`,

one unit above the universal first-overlap threshold `a=d-1`.

The theorem shows that this regime is still a one-defect system: every proper overlap has at most one unit of freedom beyond the minimum overlap cost. It treats `d=2,a=2` and `d=3,a=3` in one statement.

## 1. Setup

Let `p` be a lexicographically maximal pivot. Let `Y` be a common-missing-set family of regular owner rows with

`|S|=d`.

For each owner `y`, let `D_y` be its d-point core support.

Write

`w_v=kappa_v+e_F(v,S)`,

`w(D)=sum_(v in D) w_v`,

`mu(D)=C(d,2)-e_H(D)`,

and assume the common row allowance is

> `a=d`.                                                     (F1)

Thus

`Delta(D):=w(D)+mu(D)<=d`.                                  (F2)

The exact exchange identity gives

`q-q_D=d-Delta(D)`.                                         (F3)

Let

`s=|S intersect X|`,                                        (F4)

where `X` is the globally decorated set.

## 2. Every proper overlap has at most one slack unit

Let `D,E` be distinct support classes with proper overlap

`h=|D intersect E|`, `1<=h<=d-1`.

The joint-row inequality gives

`h(d-h)<=w(E\D)+mu(E)<=Delta(E)<=d`.                        (F5)

Define the overlap slack

`epsilon(h)=d-h(d-h)`.                                      (F6)

Because `h(d-h)>=d-1` for every proper overlap,

> `epsilon(h) in {0,1}`.                                    (F7)

More explicitly:

- `h=1` or `h=d-1` gives `epsilon=1`;
- the only additional possibility is `d=4,h=2`, where `epsilon=0`;
- for `d>=5`, no overlap size except `1,d-1` is possible;
- for `d=3`, `h=1,2` both have `epsilon=1`;
- for `d=2`, `h=1` has `epsilon=1`.

Thus the first high-slack regime is literally a one-defect overlap regime.

## 3. Support defect and shared charge are rigid

From (F5),

`h(d-h)<=Delta(E)<=d`.                                      (F8)

Hence

> `q-q_E=d-Delta(E) in {0,...,epsilon(h)}`.                 (F9)

Since `epsilon<=1`, every support participating in a proper overlap is either

- a q-plateau row; or
- an exact one-unit q-loss row.                              (F10)

Also

`w(E intersect D)`
` =Delta(E)-[w(E\D)+mu(E)]`
` <=d-h(d-h)`
` =epsilon(h)`.                                             (F11)

Therefore

> the total common-S charge on the shared core is at most one.   (F12)

If `epsilon=0`, then both supports are forced plateau rows and every shared vertex has zero charge.

## 4. Decoration converts overlap size into forced q-loss

Every support-overlap vertex is globally decorated by the exact joint decoration identity.

Suppose a support `E` is a q-plateau row. Tau-maximality gives

`|E intersect X|<=s`.                                       (F13)

Since all h shared vertices are decorated,

> a plateau overlap requires `h<=s`.                        (F14)

Consequently:

> if `h>s`, the support E cannot be plateau.                (F15)

By (F9), whenever `epsilon=1`, this forces

> `q-q_E=1`.                                                 (F16)

If `epsilon=0` and `h>s`, the overlap is impossible.         (F17)

This is the first high-slack analogue of overlap saturation: excessive decorated overlap is paid for by an exact one-unit q-loss.

## 5. Repeated supports are exact one-loss objects when they overlap

Let D be a support class used by at least two owners.

Every point of D is globally decorated by repetition.

Assume

`s<d`.                                                       (F18)

Then D cannot be a q-plateau support: equal q would replace at most s decorated missing-set vertices by all d decorated support vertices and strictly increase tau.

Therefore every owner using D satisfies

`q-q_D>=1`,

or equivalently

`Delta(D)<=d-1`.                                             (F19)

Now suppose D properly overlaps a distinct support E. Applying the overlap lower bound to D gives

`Delta(D)>=h(d-h)>=d-1`.                                    (F20)

Combining (F19)--(F20):

> `Delta(D)=d-1`,                                            (F21)
>
> `q-q_D=1`,                                                 (F22)
>
> `h(d-h)=d-1`,                                              (F23)
>
> `w(D intersect E)=0`.                                     (F24)

Therefore:

> **a repeated support which properly overlaps another class is an exact one-loss support; its overlap size is `1` or `d-1`, and its shared core is zero-charge.**   (F25)

In particular, the exceptional `d=4,h=2` plateau overlap can never involve a repeated support when `s<d`.

## 6. Support-class intersection graph and forced loss

Let the distinct support classes be vertices of an intersection graph `Gamma`; join two classes when they properly overlap.

For a class C let `m_C` be its owner multiplicity.

Define

`M_rep=sum_(C:m_C>=2) m_C`,                                 (F26)

the total number of owners belonging to repeated support classes.

Define `Q_hi` to be the number of singleton classes C for which there exists an incident overlap edge `C--E` of size

`|C intersect E|>s`.                                        (F27)

Every owner in a repeated class has strict q-loss by (F19).

Every singleton class counted by `Q_hi` has strict q-loss by (F15)--(F16).

These owner sets are disjoint. Therefore if

`L=#{y:q_y<q}`,                                              (F28)

then

> `L>=M_rep+Q_hi`.                                           (F29)

Moreover every loss counted through an actual overlap is exactly one whenever (F25) or (F16) applies.

## 7. First-high-slack global charging inequality

Let

`Phi=sum_v lambda_v w_v + sum_y mu(D_y)`.                   (F30)

The exact support-gain identity at allowance `a=d` is

`sum_y(q-q_y)=Nd-Phi`.                                      (F31)

Every strict loss is an integer at least one, so (F29) gives

> **First-high-slack compatibility inequality**
>
> `Phi+M_rep+Q_hi<=Nd`.                                      (F32)

Hence any proposed support-incidence system with

`Phi+M_rep+Q_hi>Nd`                                         (F33)

forces a legal repivot with `q_y>q`, contradicting maximality.

This is a direct global improving-repivot criterion for the first high-slack regime.

It is complementary to the more general forced-decorated-incidence bound in `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`: (F32) uses the support-class intersection geometry to certify specific loss rows.

## 8. Equality rigidity

Suppose equality holds in (F32) and every strict loss is accounted for by (F29).

Then simultaneously:

1. every repeated-class owner loses exactly one q-unit;
2. every singleton class counted by `Q_hi` loses exactly one q-unit;
3. every other singleton owner is a plateau row;
4. every repeated support has exact defect `d-1`;
5. every repeated support that overlaps another class has overlap size `1` or `d-1` and zero shared charge;
6. every plateau overlap has size at most s;
7. any `d=4,h=2` overlap is plateau, zero-shared-charge, and requires `s>=2`;
8. all remaining freedom is confined to where the single residual charge/defect unit is placed on one-loss singleton overlap supports.

Thus a non-strict first-high-slack state is already a finite one-defect geometry rather than an arbitrary support hypergraph.

## 9. r=12 specialization: d=2, allowance2

Take

`d=2,a=2`.

Every proper overlap has `h=1` and `epsilon=1`.

Therefore:

- an overlapping support is plateau or exact one-loss;
- the shared core point has charge at most1;
- every repeated support, for `s<2`, is strict-loss;
- any repeated support which overlaps another class has exact defect1 and zero charge at the shared point;
- if `s=0`, every overlap forces both incident singleton supports to be exact one-loss rows;
- the global owner system obeys
  `Phi+M_rep+Q_hi<=2N`.

This is the common structural language for D2 allowance-two residuals, including the source-reported E334 `r=2/allowance=2` channel.

## 10. r=12 specialization: d=3, allowance3

Take

`d=3,a=3`.

Every proper overlap has `h=1` or2 and `epsilon=1`.

Therefore:

- every overlapping triple support is plateau or exact one-loss;
- total shared charge is at most1;
- every repeated triple support, for `s<3`, is strict-loss;
- a repeated support which overlaps another class has exact defect2 and zero shared charge;
- an overlap of size h>s forces an exact one-loss singleton support;
- the global owner system obeys
  `Phi+M_rep+Q_hi<=3N`.

Thus the d3 allowance-three regime is also a one-defect compatibility problem. The next theorem need only classify how the single residual unit propagates through an overlap component (common-pair / sunflower / four-set / repeated-clique geometry).

## 11. Parameterized significance

No values 35,211,333--340 appear in the theorem.

The only inputs are

- support size d;
- first-high-slack allowance a=d;
- overlap cost `h(d-h)`;
- exact support gain/loss;
- support repetition decoration;
- tau transport.

Therefore the theorem is a reusable high-slack repivot-compatibility principle and is a natural candidate for higher-r applications.