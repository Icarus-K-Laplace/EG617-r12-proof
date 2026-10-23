# q36 f=2 far-target-K2 — c=8 no-d2 A=3 multiplicity-four one-edge reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md`, `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, `Q36_F2_FAR_K2_C8_NO_D2_MULTISUPPORT_D17_CAPACITY.md`, common-S row closure, q36 lexicographic maximality, and `alpha(H)<=3`.

This treats one high-multiplicity channel in the corrected A=3 frontier.

## 1. Setup

All eight owners share the common missing set

`S=F union {x}`

with allowance A=3. Put `Y=X\{x}` and `rho=e_M(Y) in {0,1}`.

For a support T write

`w(T)=sum_(v in T)(kappa_v+e_F(v,S))`.

Every support satisfies

`Delta(T)=m(T)+w(T)<=3`.

A repeated support cannot use full defect3 at q36, hence every repeated support satisfies

`Delta(T)<=2`.                                               (1)

Let D be a support of owner multiplicity4 with exactly one internal target edge. Then

`m(D)=2`.

By (1), necessarily

> `w(D)=0`.                                                  (2)

## 2. Corrected D14 forces few intersecting external owners

The corrected D14 inequality is

`3*4 + O_D + e_F(Y,D) + e_H(D) <=14+rho`.

Since `e_H(D)=1`,

> `O_D+e_F(Y,D)<=1+rho`.                                    (3)

There are four owner incidences outside the multiplicity-four class. Every owner support that intersects D contributes at least one unit to O_D. Hence at least

`4-O_D >= 3-rho`

external owner incidences are carried by supports disjoint from D.      (4)

## 3. Every support disjoint from D is a K3

Because w(D)=0, common-S row closure gives zero target cross-edges from D to any disjoint support T.

The one-edge triple D contains an internal target-nonedge pair ab. If a disjoint T were nonclique, choose an internal target-nonedge pair uv in T. Then all D--T cross pairs are target nonedges, so

`{a,b,u,v}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> every support disjoint from D is a target K3.              (5)

## 4. There is only one distinct disjoint support class

Suppose E1,E2 were two distinct support classes disjoint from D. By (5), both are K3s.

For any e1 in E1 and e2 in E2, if e1e2 were a target nonedge then, using the internal target-nonedge pair ab of D and the fact that D is target-anticomplete to E1 union E2,

`{a,b,e1,e2}`

would be an independent4-set.

Hence every E1--E2 cross pair would have to be a target edge:

`e_H(E1,E2)=9`.                                             (6)

But a K3 support has non-missing common-S allowance at most its total defect, at most3. Joint row closure therefore gives

`e_H(E1,E2)<=3`,

contradicting (6).

Thus all disjoint owner incidences use one unique K3 support class E. Let its owner multiplicity be s. From (4),

> `s>=3-rho`.                                                (7)

Since s>=2, E is repeated and therefore `w(E)<=2` by (1).

## 5. Corrected D17 gives s<=3

Apply `Q36_F2_FAR_K2_C8_NO_D2_MULTISUPPORT_D17_CAPACITY.md` to the disjoint supports D,E.

Here

`e_H(D)=1`, `e_H(E)=3`, `e_H(D,E)=0`.

The D17 inequality gives

`3(4+s)+1+3+e_F(Y,D union E)<=26+rho`.

Dropping the nonnegative Y term,

`16+3s<=26+rho`,

so

> `s<=3`.                                                    (8)

Combining (7)--(8):

- if `rho=0`, then `s=3`;
- if `rho=1`, then `s in {2,3}`.                            (9)

## 6. Exact residual owner geometry

There are `4-s` owner incidences not belonging to D or E. Every one must intersect D, because E is the unique disjoint support class.

Their total overlap with D is at least `4-s`, while (3) gives `O_D<=1+rho`.

### rho=0

Then s=3. Exactly one residual owner support G remains and

`1<=|G intersect D|<=O_D<=1`.

Therefore

> `|G intersect D|=1`,
> `O_D=1`,
> `e_F(Y,D)=0`.                                              (10)

Thus the entire rho=0 multiplicity-four one-edge channel is reduced to the owner partition

> `4 + 3 + 1`,

where D is the one-edge repeated support, E is a disjoint repeated K3, and the singleton G meets D in exactly one point.

### rho=1, s=2

Two residual owner supports remain. Since each intersects D,

`O_D>=2`.

By (3), `O_D+e_F(Y,D)<=2`, hence

> `O_D=2`, `e_F(Y,D)=0`,
> and each residual owner support meets D in exactly one point.   (11)

Thus this terminal has owner partition `4+2+1+1`.

### rho=1, s=3

One residual owner support remains. It meets D in one or two points, with

`|G intersect D| + e_F(Y,D) <=2`.                           (12)

Thus this terminal has owner partition `4+3+1` with only two possible D-overlap sizes.

## 7. Current terminal list

A multiplicity-four one-edge support in corrected no-d2 A=3 can survive only in the following finite owner architectures:

1. `rho=0`: `4+3+1`, with the singleton intersecting D in exactly one point and `e_F(Y,D)=0`;
2. `rho=1`: `4+2+1+1`, both singletons intersecting D once and `e_F(Y,D)=0`;
3. `rho=1`: `4+3+1`, the singleton intersecting D in one or two points subject to (12).

No stronger closure is claimed here. The proof uses only the corrected D14 base and the genuine D17 hereditary cap.