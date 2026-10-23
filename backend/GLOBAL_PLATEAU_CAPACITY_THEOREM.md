# Global Plateau-Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- exact common-S tau transport;
- support repetition/charge decoration theorem;
- common-S row closure;
- lexicographic maximality of `(q,tau)`.

Purpose: give a universal bound on the number of q-plateau rows in a common-missing-set family. This is stronger than the earlier finite-core plateau-packing bound whenever the residual core has small independence number.

## 1. General setup

Let H be a residual core with

`alpha(H)<=r`.                                               (P1)

Let Y be a family of N regular owner rows sharing one missing set S of size

`|S|=d`.

For owner y let D_y be its d-point support.

Write

`w_v=kappa_v+e_F(v,S)`,

and let X be the globally decorated set.

Put

`s=|S intersect X|`.                                        (P2)

Assume

> `s<d`.                                                     (P3)

Let

`P=#{y in Y:q_y=q}`                                         (P4)

be the number of q-plateau owner rows.

## 2. Every plateau support contains a private clean zero-charge point

For a plateau owner y, exact tau transport gives

`tau_y-tau_p=|D_y intersect X|-s<=0`

by lexicographic maximality.

Hence

`|D_y intersect X|<=s<d`.                                   (P5)

Therefore D_y contains at least one support vertex v which is not globally decorated.

The support repetition/charge decoration theorem gives

`g_v>=w_v+lambda_v-1`,                                      (P6)

where

`lambda_v=#{z in Y:v in D_z}`.

Since v is not decorated, `g_v=0`. As `lambda_v>=1` because v lies in D_y and `w_v>=0`, equation (P6) forces

> `lambda_v=1`, `w_v=0`.                                    (P7)

Thus every plateau support contains a vertex which is simultaneously

- private to that support class;
- zero common-S charge;
- globally clean.

Call such a point a **plateau witness**.

## 3. Plateau witnesses are pairwise target-nonadjacent

Choose one plateau witness `v_y` from each plateau row.

Because `lambda_(v_y)=1`, if z is a different plateau owner then

`v_y notin D_z`.                                            (P8)

Common-S row closure applied to v_y and D_z gives

`e_H(v_y,D_z)<=w_(v_y)=0`.                                  (P9)

In particular

`v_y v_z` is a target nonedge.                              (P10)

Thus the chosen plateau witnesses form an independent set in H.

Therefore

> **Global plateau-capacity theorem**
>
> `P<=alpha(H)<=r`.                                         (P11)

For the r=12 residual cores, `alpha(H)<=3`, so

> `P<=3`.                                                    (P12)

## 4. Plateau support classes cannot repeat

The proof also shows directly that when `s<d`, a plateau support class cannot be used by two owners.

Indeed a repeated support has every support point globally decorated, while a plateau support must contain at least `d-s>=1` nondecorated support vertices.

Therefore every plateau row corresponds to a distinct singleton support class.   (P13)

Hence P is simultaneously

- the number of plateau owners;
- the number of plateau support classes.

## 5. Mandatory strict-loss count

Let

`L=N-P`                                                      (P14)

be the number of strict q-loss rows.

From (P11),

> `L>=N-r`.                                                  (P15)

In the current r=12 core,

> `L>=N-3`.                                                  (P16)

This bound is independent of

- support size d;
- row allowance a;
- support overlap geometry;
- core size n;
- the E-layer label.

It uses only the common-S structure, `s<d`, row closure and the core independence bound.

## 6. Global support-gain consequence

Let the common row allowance be a and put

`Phi=sum_v lambda_v w_v+sum_y mu(D_y)`.

The exact support-gain identity is

`sum_y(q-q_y)=Na-Phi`.                                      (P17)

Every strict loss is an integer at least1. Therefore (P15) gives

> **Plateau-capacity compatibility inequality**
>
> `Phi<=Na-(N-r)`.                                          (P18)

For r=3,

> `Phi<=Na-(N-3)`.                                          (P19)

If the left side exceeds this bound, some legal repivot must have `q_y>q`.

This is a global improving-repivot criterion with no support-case classification.

## 7. Equality rigidity

Suppose equality holds in (P18).

Then all inequalities used above are saturated:

1. `P=r` plateau rows exist;
2. their chosen witnesses form an independent r-set in H;
3. every other owner row loses exactly one q-unit;
4. every plateau row is a singleton support class;
5. each plateau support contains at least one private clean zero-charge witness;
6. all non-plateau freedom is confined to one-loss support geometry.

For r=3, equality forces exactly three plateau owners and N-3 exact one-loss owners.

Thus even the equality case is a sharply organized multi-pivot geometry.

## 8. Consequences for the r=12 backend

### E333-style large repeated families

Any common-S family with N>=7 and s<d has at least N-3 strict-loss rows before any D2 family-specific capacity theorem is used.

The old D2-A/B/C/D/R9 distinctions therefore encode additional equality data, not independent reasons for failure.

### E334 d3 eleven-view systems

If an eleven-owner d3 common-S subsystem satisfies s<3, then

> `P<=3`, `L>=8`.                                           (P20)

Thus at least eight of the eleven legal views must be strict-loss rows globally. This is a stronger starting point than treating eleven local views separately.

If additionally s=0, `GLOBAL_FIRST_HIGH_SLACK_S0_COLLAPSE.md` sharpens this further to `L>=10` at allowance3.

### First-high-slack d2/d3

For d2/A2 with s<2 and d3/A3 with s<3, the theorem applies before the one-defect overlap classification. `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md` then describes the exact geometry of the mandatory one-loss rows.

## 9. Generalization beyond r=12

The proof is already written for arbitrary core independence number r.

Whenever a higher-r pivot reduction supplies

- common-S row closure;
- exact tau transport;
- repetition/charge decoration;
- a core independence bound alpha(H)<=r,

the same theorem gives

`P<=r`.

Thus plateau capacity is a genuinely reusable structural theorem rather than an r=12 numerical accident.