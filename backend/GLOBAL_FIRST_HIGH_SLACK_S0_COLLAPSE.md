# Global First-High-Slack s=0 Collapse Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_FIRST_HIGH_SLACK_RIGIDITY.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- common-S row closure;
- exact tau transport;
- `alpha(H)<=3`.

Purpose: completely control the zero-decorated-missing-set sector at the first high-slack level `a=d`.

## 1. Setup

Let Y be a common-S owner family with

`|S|=d`,
`a=d`,
`s=|S intersect X|=0`.                                      (Z1)

Let N be the number of owner rows.

For an owner y write D for its support and

`Delta(D)=w(D)+mu(D)<=d`.

A q-plateau row satisfies

`Delta(D)=d`.                                                (Z2)

## 2. A plateau support contains no decorated core vertex

Exact tau transport gives for a plateau row

`|D intersect X|<=s=0`.

Hence

> `D intersect X=empty`.                                    (Z3)

The repetition/charge decoration theorem says that every support-union vertex with

`lambda_v>=2` or `w_v>=1`

is globally decorated.

Combining with (Z3), every point v of a plateau support must satisfy

> `lambda_v=1`, `w_v=0`.                                    (Z4)

Thus every plateau support class is a singleton class and all its support vertices are private clean zero-charge points.

## 3. Exact internal density of a plateau support

Equation (Z4) gives

`w(D)=0`.

Since the row is plateau and a=d,

`w(D)+mu(D)=d`,

so

> `mu(D)=d`.                                                 (Z5)

Equivalently

> `e_H(D)=C(d,2)-d`.                                        (Z6)

If the right side is negative, no plateau support exists.

In particular:

### d=2

`C(2,2)-2=1-2=-1`.

Impossible. Therefore

> **for d=2,a=2,s=0, no plateau owner exists.**              (Z7)

### d>=3

A plateau support is necessarily noncomplete because `mu(D)=d>0`.

Hence it contains a target-nonedge pair.

## 4. Two plateau supports are impossible

Let D,E be two distinct plateau supports.

They cannot properly overlap: every support-overlap vertex is globally decorated, contradicting (Z3).

Therefore D,E are disjoint.

Also `w(D)=w(E)=0`, so joint row closure gives

`e_H(D,E)=0`.                                                (Z8)

Each support contains a target-nonedge pair because `mu=d>0`. Choose

`{d1,d2} subset D`,
`{e1,e2} subset E`

to be target-nonedge pairs.

Equation (Z8) makes every D--E pair a target nonedge. Thus

`{d1,d2,e1,e2}`

is an independent4 in H, contradicting `alpha(H)<=3`.

Therefore

> **there is at most one plateau support class, hence at most one plateau owner.**   (Z9)

## 5. Mandatory global loss

Let

`L=#{y:q_y<q}`.

By (Z9),

> `L>=N-1`.                                                  (Z10)

For d=2, (Z7) improves this to

> `L=N`.                                                     (Z11)

The exact support-gain identity at allowance a=d gives

`Nd-Phi=sum_y(q-q_y)>=L`.

Hence

> `Phi<=N(d-1)+1`                                            (Z12)

for every d, and for d=2,

> `Phi<=N`.                                                  (Z13)

These are global compatibility bounds, not case-specific inequalities.

## 6. Equality rigidity

If equality holds in (Z10)--(Z12), then

- exactly one owner is plateau;
- all other owners lose exactly one q-unit;
- the unique plateau support is a singleton clean zero-charge class with `mu=d`;
- every other owner support has exact defect d-1.

For d=2 there is no plateau owner, so equality in (Z11)--(Z13) forces every owner to lose exactly one unit and every support to have exact defect1.

Thus the entire s=0 first-high-slack regime collapses to a one-loss equality system.

## 7. r=12 consequences

### d=2, allowance2

Every owner row is strict-loss:

`q_y=q-1` in the global equality state.

There is no plateau geometry to classify.

This removes one entire decoration sector from D2 allowance-two residuals.

### d=3, allowance3

At most one owner row can be plateau; all others are strict-loss.

If a plateau exists, it is a clean zero-charge support with

`mu=3`,

hence an independent triple.

Therefore an N-owner d3/A3 system with s=0 has

`L>=N-1`,

so for an eleven-view system

> `L>=10`.                                                    (Z14)

Thus virtually the entire eleven-view family is forced to be exact one-loss before any detailed support classification is attempted.

## 8. Generalization

The proof is parameterized in d. It uses only

- first-high-slack allowance a=d;
- zero decorated missing-set count s=0;
- support repetition/charge decoration;
- row closure;
- alpha(H)<=3.

No r=12 numerical core constant appears.