# Global Repeated-Support Packing Bridge

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- `GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md`;
- exact tau transport and lexicographic maximality.

Purpose: turn the generic repivot penalty for a repeated support directly into a hereditary multiplicity bound, without re-deriving D13/D14/D17 inequalities layer by layer.

## 1. Setup

Let Y be a common-S owner family with support size d and row allowance a.

Let D be one support class of owner multiplicity

`m>=2`.

Write

`w(D)=sum_(v in D)(kappa_v+e_F(v,S))`,

`mu(D)=C(d,2)-e_H(D)`,

so

`Delta(D)=w(D)+mu(D)<=a`.

Let

`s=|S intersect X|`.

Assume

> `s<d`.                                                     (R1)

Let B be any certified dense base disjoint from D with

- size b;
- exact or lower-certified edge count `E_B`;
- all m owners of D contained in B;
- each owner target-adjacent to all d vertices of D.

Let the inherited hereditary cap be

`e(B union D)<=Dcap(b+d)`.                                  (R2)

Let c>=0 denote any additional certified B--D target edges beyond the dm owner incidences.

## 2. Repetition forces one unit of repivot loss

Because D is used by at least two owners, every vertex of D is globally decorated.

If an owner using D had `q_D=q`, exact tau transport would give

`tau_D-tau_p=d-s>0`,

contradicting lexicographic maximality.

Therefore every D-owner has strict q-loss:

`q-q_D>=1`.                                                  (R3)

Using the exact row identity,

`q-q_D=a-Delta(D)`,

we obtain

> `Delta(D)<=a-1`.                                          (R4)

In particular

> `mu(D)<=a-1`,                                              (R5)

so the support has at least

> `e_H(D)>=e_min(d,a):=max(0,C(d,2)-a+1)`.                  (R6)

Thus repetition turns a dynamical repivot statement into a static internal-density lower bound.

## 3. One-support hereditary multiplicity bound

Inside `B union D`, the certified target edges include

- `E_B` inside B;
- `dm` owner-support edges;
- `c` extra B--D edges;
- at least `e_min(d,a)` internal support edges.

Therefore the hereditary cap gives

`E_B+dm+c+e_min(d,a)<=Dcap(b+d)`.                            (R7)

Equivalently

> **Repeated-support packing bound**
>
> `m <= floor((Dcap(b+d)-E_B-c-e_min(d,a))/d)`.              (R8)

Dropping c gives the universal version

> `m <= floor((Dcap(b+d)-E_B-e_min(d,a))/d)`.                (R9)

This is the abstract form of the repeated-support D13/D14 inequalities used throughout the project.

## 4. Equality rigidity

If equality holds in (R7), then both the repivot and hereditary inequalities are saturated.

Consequently:

1. every D-owner loses exactly one q-unit;
2. `Delta(D)=a-1`;
3. `mu(D)=a-1-w(D)`;
4. `e_H(D)=C(d,2)-a+1+w(D)`;
5. `B union D` saturates the hereditary cap;
6. there are no omitted B--D target edges beyond the certified dm+c terms;
7. every additional target edge incident with D must be paid for by increasing w(D) and correspondingly decreasing mu(D).

Thus a multiplicity equality is automatically a repivot-equality geometry, not just a scalar edge count.

## 5. Several disjoint repeated support classes

Let `D_1,...,D_k` be pairwise-disjoint repeated support classes, all of size d, with multiplicities `m_i>=2`.

Assume the same dense base B contains all their owners and is disjoint from the supports.

For each i, repetition gives

`e_H(D_i)>=e_min(d,a)`.                                     (R10)

Applying the global hereditary support-packing theorem to

`B union D_1 union ... union D_k`

gives

`d sum_i m_i`
` + k e_min(d,a)`
` + sum_i c_i`
` + sum_(i<j)e_H(D_i,D_j)`
` <=Dcap(b+kd)-E_B`.                                        (R11)

Hence

> `sum_i m_i`
> ` <= floor((Dcap(b+kd)-E_B-k e_min(d,a))/d)`.              (R12)

Any certified cross edge or extra base incidence sharpens this bound.

Again equality forces simultaneous saturation of all repeated-support repivot losses and the hereditary induced-edge cap.

## 6. First-high-slack simplification

At the first high-slack level

`a=d`,

we have

`e_min(d,d)=max(0,C(d,2)-d+1)=C(d-1,2)`                    (R13)

for d>=2.

Therefore any repeated d-support in the first-high-slack regime satisfies

> `e_H(D)>=C(d-1,2)`.                                       (R14)

Special cases:

- d=2,a=2: every repeated support has at least0 internal target edges; if it properly overlaps another class, `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md` sharpens it to exact defect1;
- d=3,a=3: every repeated triple support has at least1 internal target edge;
- d=4,a=4: every repeated 4-support has at least3 internal target edges.

Thus the same packing formula applies to D2/A2, d3/A3 and larger-support first-high-slack systems.

## 7. Low-allowance simplification

If `a<=d-1`, repetition gives

`e_H(D)>=C(d,2)-a+1`.                                       (R15)

For d=3,a=1 this yields

`e_H(D)>=3`,

so every repeated support is a target K3, recovering the structural conclusion of `GLOBAL_D3_ALLOWANCE_ONE_COLLAPSE.md` directly.

For d=2,a=1 it yields

`e_H(D)>=1`,

so every repeated support is a target K2.

## 8. Bridge use for multi-view systems

Suppose a multi-view compatibility theorem, block-transversal theorem, or matching-cover theorem forces one support class to have multiplicity at least M.

Then it is enough to find a dense base B for which the right side of (R9) is smaller than M.

This closes the entire multi-view branch without classifying the remaining views.

For example, `GLOBAL_D3_ALLOWANCE_ONE_COLLAPSE.md` turns an N=11 low-allowance triple-support system into a repeated zero-charge K3 of multiplicity at least6. The remaining task is no longer eleven-view compatibility; it is the one-line dense-base test

`6 > floor((Dcap(b+3)-E_B-3)/3)`.                            (R16)

If a valid base B satisfies (R16), the eleven-view system is impossible.

## 9. Generalization

The theorem uses only

- support size d;
- allowance a;
- missing-set decoration count s<d;
- exact tau transport;
- a hereditary cap function;
- a certified dense base.

It is independent of 35,211 and the E-layer labels, and therefore extends verbatim to higher-r pivot reductions once analogous hereditary caps and dense bases are available.