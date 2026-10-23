# Global First-High-Slack s=1 Plateau-Sunflower Rigidity

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: classify the q-plateau equality components in the first-high-slack regime `a=d` when exactly one missing-set vertex is decorated.

## 1. Setup

Let Y be a common-S support family with

`|S|=d`,
`a=d`,
`s=|S intersect X|=1`.                                      (S1)

Consider only support classes whose owner rows are q-plateau rows.

Let Gamma be their proper-intersection graph.

## 2. Plateau overlap has size one

By `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md`, a plateau overlap of size h requires

`h<=s=1`.

Therefore every proper overlap between plateau support classes has

> `h=1`.                                                     (S2)

Every shared core point is globally decorated.

## 3. Every plateau intersection component is a common-hub sunflower

Let a plateau support D properly overlap E in the core point x.

Because x is decorated and a plateau support contains at most s=1 decorated support vertex, D cannot properly overlap another support T at a different core point y: y would also be decorated, giving two decorated points in D.

Thus all proper overlaps incident with D use the same point x.

This propagates through each connected component of Gamma.

Hence

> every nontrivial plateau-intersection component is a common-hub sunflower.   (S3)

Let x be its common hub.

Distinct supports in the component have pairwise-disjoint private petal sets.

## 4. Private vertices are clean zero-charge points

Let D be a support in such a component.

The hub x is globally decorated.

Every private point u in `D\{x}` must be globally clean, because D is plateau and already contains the unique allowed decorated support point.

But the repetition/charge decoration theorem says a support-union point is forced decorated whenever

`lambda_u>=2` or `w_u>=1`.

Therefore every private point satisfies

> `lambda_u=1`, `w_u=0`.                                     (S4)

The shared-charge bound in `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md` gives

> `w_x<=1`.                                                  (S5)

Thus

`w(D)=w_x`.                                                  (S6)

## 5. Exact internal support density

Because D is a q-plateau row at allowance a=d,

`w(D)+mu(D)=d`.                                              (S7)

Using (S6),

`mu(D)=d-w_x`.                                               (S8)

Hence

> `e_H(D)=C(d,2)-d+w_x`.                                    (S9)

Since `w_x in {0,1}`, every support in the component has one of two exact internal edge counts.

The hub charge w_x is a global vertex quantity, so all supports in the same sunflower component have the same internal edge count.

## 6. d=2 specialization

Take d=2.

Equation (S9) gives

`e_H(D)=1-2+w_x=w_x-1`.

Nonnegativity of the internal edge count forces

> `w_x=1`,
> `e_H(D)=0`.                                                (S10)

Thus every plateau support in a nontrivial d2 component is a target-nonedge pair `{x,u}` with

- common hub x of charge1;
- private leaf u of charge0;
- xu a target nonedge.

Let there be three such supports with private leaves u1,u2,u3.

For any i!=j, ui lies outside support `{x,uj}` and has charge0, so row closure gives

`e_H(ui,{x,uj})=0`.

Thus all four vertices

`{x,u1,u2,u3}`

are pairwise target-nonadjacent, an independent4, contradicting `alpha(H)<=3`.

Therefore

> **d=2,a=2,s=1 plateau-star capacity: at most two support classes.**   (S11)

## 7. d=3 specialization: hub charge zero is impossible

Take d=3.

Equation (S9) becomes

`e_H(D)=3-3+w_x=w_x`.                                       (S12)

Suppose `w_x=0`. Then every support in the component has zero internal target edges.

A nontrivial component contains at least two supports

`D_1={x,u1,v1}`,
`D_2={x,u2,v2}`.

All four private points have charge0. Row closure makes every private point of one support target-anticomplete to the other support. Inside each support, the private pair is also a target nonedge because the support has zero internal edges.

Hence

`{u1,v1,u2,v2}`

is an independent4 in H, contradiction.

Therefore

> `w_x=1`.                                                   (S13)

By (S12), every support is an exact one-edge triple.

## 8. d=3 specialization: at most two plateau supports

Suppose a d3 plateau sunflower component contains three supports

`D_i={x,u_i,v_i}`, `i=1,2,3`.

Each support has exactly one internal target edge.

Therefore in each D_i at least one private petal, call it z_i, is target-nonadjacent to the hub x.

For i!=j, z_i has charge0 and lies outside D_j. Row closure gives

`e_H(z_i,D_j)=0`.

In particular the z_i are pairwise target-nonadjacent.

Thus

`{x,z_1,z_2,z_3}`

is an independent4, contradiction.

Hence

> **d=3,a=3,s=1 plateau-sunflower capacity: at most two support classes.**   (S14)

## 9. The exact two-support d3 terminal

Suppose exactly two plateau supports survive:

`D_1={x,u1,v1}`,
`D_2={x,u2,v2}`.

Both are exact one-edge triples and all four petals have charge0.

If in both supports the unique target edge were incident with x, then each private pair `{u_i,v_i}` would be a target nonedge.

Row closure across supports makes every point of the first private pair target-anticomplete to the second support and vice versa. Therefore

`{u1,v1,u2,v2}`

would be an independent4.

Consequently

> in any surviving two-support plateau component, at least one support has its unique target edge between its two private petals.   (S15)

No stronger exclusion is claimed here.

## 10. Structural conclusion

At first high slack `a=d` with `s=1`, the q-plateau proper-overlap geometry is not an arbitrary support hypergraph.

It is a common-hub sunflower whose private vertices are clean and whose internal density is fixed by the single hub charge.

For the two r=12 low-support regimes:

- `d=2,a=2`: every plateau component has at most two support classes;
- `d=3,a=3`: every plateau component has at most two support classes, hub charge exactly1, and every support is an exact one-edge triple.

Thus any larger first-high-slack owner system must obtain its size from repeated/strict-loss classes or from multiple disjoint components, both of which are controlled by global loss and block-transversal packing.

## 11. Generalization

Sections2--5 are valid for arbitrary d. The small component-capacity conclusions in Sections6--9 use `alpha(H)<=3` and specialize to d=2,3.

This gives a reusable equality-rigidity template for higher-r systems once the corresponding core independence bound is known.