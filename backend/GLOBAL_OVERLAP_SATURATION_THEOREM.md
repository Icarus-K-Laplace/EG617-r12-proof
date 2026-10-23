# Global Overlap-Saturation Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- exact common-S exchange identity;
- common-S joint-row overlap inequality;
- exact decoration transport;
- support-overlap decoration identity;
- lexicographic maximality of `(q,tau)`.

Purpose: identify the universal equality geometry at the first allowance level where proper support overlap becomes possible.

This theorem contains the d=2/allowance1 and d=3/allowance2 overlap regimes as special cases and is parameterized for larger support sizes.

## 1. Abstract setup

Let p be a lexicographically maximal pivot. Let Y be a common-missing-set family of regular owner rows with

`|S|=d`.

For every owner y let `D_y` be its d-point core support.

Write

`w_v=kappa_v+e_F(v,S)`,

`w(D)=sum_(v in D) w_v`,

`mu(D)=C(d,2)-e_H(D)`.

Assume the common row allowance is exactly

> `a=d-1`.                                                    (O1)

Thus every support satisfies

`w(D)+mu(D)<=d-1`.                                           (O2)

Let

`s=|S intersect X|`,                                         (O3)

where X is the globally decorated set.

## 2. Proper overlap is automatically an equality state

Let D,E be two distinct support classes with proper overlap

`h=|D intersect E|`, `1<=h<=d-1`.

The exact joint-row inequality gives

`h(d-h)<=w(E\D)+mu(E)`.                                     (O4)

On the other hand

`w(E\D)+mu(E)<=w(E)+mu(E)<=d-1`.                            (O5)

For every integer `1<=h<=d-1`,

`h(d-h)>=d-1`,                                               (O6)

with equality if and only if

`h in {1,d-1}`.                                              (O7)

Combining (O4)--(O6), every inequality is equality. Therefore

> `h in {1,d-1}`;                                            (O8)
>
> `w(E)+mu(E)=d-1`;                                          (O9)
>
> `w(E intersect D)=0`.                                      (O10)

By symmetry the same holds for D.

Since support defect equals the full allowance, both owners are q-plateau rows:

> `q_D=q_E=q`.                                               (O11)

Thus proper overlap at the first admissible allowance is never a generic configuration: it is an exact equality state.

## 3. Shared vertices are zero-charge but globally decorated

Equation (O10) says every shared support vertex has common-S charge zero.

The exact two-row decoration identity nevertheless forces every support-overlap vertex to be globally decorated.

Hence every point of `D intersect E` is simultaneously

- zero-charge in the common-S accounting;
- globally decorated because it participates in multiple support rows.   (O12)

This is the basic local signature of overlap saturation.

## 4. Tau restriction on overlap size

Because D and E are q-plateau supports, tau-maximality gives

`|D intersect X|<=s`,
`|E intersect X|<=s`.                                        (O13)

All h shared vertices are decorated by (O12), so

> `h<=s`.                                                     (O14)

Together with (O8), proper overlap is possible only when

- `s>=1` for h=1;
- `s>=d-1` for h=d-1.

Consequences:

### s=0

No proper overlap exists.                                    (O15)

### 1<=s<d-1

The only possible proper overlap size is

`h=1`.                                                       (O16)

### s=d-1

Both h=1 and h=d-1 are algebraically possible, but both remain exact plateau equality states.

## 5. The s=1 common-hub theorem

Assume

`s=1`.                                                       (O17)

Then every proper overlap has size exactly1.

Let D properly overlap E in the point x. The point x is decorated.

If D also properly overlaps a third support T at a different point y, then both x and y are decorated support vertices of the plateau support D, contradicting `|D intersect X|<=1`.

Therefore every proper overlap incident with D uses the same support point.

This propagates along any connected component of the support-intersection graph. Hence

> every nontrivial proper-overlap component is a common-hub sunflower.   (O18)

Each component has a unique core hub shared by all of its support classes.

## 6. Exact private-vertex geometry when s=1

Let D be a support in a nontrivial sunflower component, with hub x.

The hub is decorated and zero-charge.

Every private support vertex u in `D\{x}` must be globally clean: otherwise D would contain at least two decorated vertices and violate the plateau tau bound.

The global repetition/charge decoration theorem says a support-union vertex is forced decorated whenever

`lambda_u>=2` or `w_u>=1`.

Thus every private point satisfies

> `lambda_u=1`, `w_u=0`.                                     (O19)

Since the hub also has charge zero,

`w(D)=0`.                                                    (O20)

Equation (O9) therefore gives

> `mu(D)=d-1`.                                               (O21)

Equivalently every support in a nontrivial s=1 sunflower has exactly

> `e_H(D)=C(d,2)-(d-1)=C(d-1,2)`                            (O22)

target edges.

Thus the entire support component is an equality object:

- one zero-charge decorated common hub;
- d-1 private clean zero-charge vertices per support;
- exact internal edge deficit d-1;
- q-plateau on every support.

For d=3 this is exactly a one-edge triple sunflower.

For d=2 this gives target-nonedge pairs sharing one decorated hub.

## 7. Repeated support classes are separated from proper-overlap equality components

Suppose a support class D is used by at least two owners.

Then every point of D is globally decorated by support repetition.

If `s<d`, equal-q repivoting would insert d decorated support points while removing only s decorated missing-set points, so tau would strictly increase. Therefore every repeated owner has strict q-loss.

Hence

`w(D)+mu(D)<=a-1=d-2`.                                      (O23)

But every support participating in a proper overlap has full defect d-1 by (O9).

Therefore

> when `s<d`, a repeated support class cannot properly overlap any distinct support class.   (O24)

Repeated classes are isolated support blocks in the intersection hypergraph.

## 8. Structural decomposition at first-overlap allowance

At allowance `a=d-1`, the common-S support system decomposes into:

1. isolated repeated support classes of defect at most d-2;
2. exact plateau overlap components with overlap size1 or d-1;
3. when s=1, those overlap components are common-hub sunflowers with exact internal edge count `C(d-1,2)`;
4. singleton disjoint support classes.

Thus the first allowance level permitting proper overlap is already globally rigid.

This is the general mechanism behind many previously separate low-support equality cases.

## 9. Important specializations

### d=2, a=1

Proper overlap means two two-point supports share exactly one core vertex. For s=1 every nontrivial intersection component is a common-hub star of target-nonedge pairs with private clean endpoints.

Repeated two-point support classes are isolated from these stars and have defect at most0, hence are pure zero-defect target K2 supports.

This is the natural structural language for D2 allowance-one equality systems.

### d=3, a=2

For s=0 all distinct supports are disjoint.

For s=1 every nontrivial overlap component is a common-hub sunflower of exact one-edge triples with clean private petals.

Repeated classes are isolated dense triples of defect at most1.

This recovers `GLOBAL_D3_ALLOWANCE_TWO_OVERLAP_RIGIDITY.md` as a direct corollary.

### Larger d

The same theorem applies whenever the first proper-overlap allowance equals d-1. Thus future d=4 or larger support regimes can reuse the equality mechanism without re-deriving local overlap cases.

## 10. Generalization beyond r=12

No numerical value 35,211,333--340 is used.

The theorem depends only on

- support size d;
- the exact row allowance;
- joint-row overlap cost h(d-h);
- charge/repetition decoration;
- tau transport.

Therefore it is a genuinely parameterized repivot-compatibility theorem and is a natural candidate for higher-r applications.