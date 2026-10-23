# Global Fully-Decorated Support-to-One-Spoke Bridge

Status: `PROVED_ANALYTIC`.

Dependencies:

- the q32/CORE211 nine-owner fully-decorated setup;
- `GLOBAL_D3_A2_TWO_BLOCK_INCIDENCE_BUDGET.md`;
- support-repetition decoration inequality `g_v>=w_v+lambda_v-1`;
- common-S row closure;
- CORE211 `K=sum kappa=2`;
- exact CORE211 one-spoke formula and inherited D14.

Purpose: connect the final fully-decorated support-equality regime to the simultaneous one-spoke regime. This is a direct bridge between two previously separate backend proof architectures.

## 1. General q32 fully-decorated setup

Work in the nine-owner fully-decorated q32/CORE211 state after the lower-slack layers have been excluded.

Thus

- `g_r=0` for the leftover shell point r;
- common row allowance is2;
- `W<=36`;
- total 35-core decoration satisfies `G_H<=28`;
- the nine owners contribute exactly27 support incidences into the core.

Let U be the union of all owner supports.

For v in U let

`lambda_v=#{owners y:v in D_y}`.

Then

`sum_(v in U)lambda_v=27`.                                  (O1)

Let

`W_U=sum_(v in U)w_v`.

## 2. Decoration lower bound on the support union

The support-repetition decoration theorem gives

`g_v>=w_v+lambda_v-1`

for every v in U.

Summing over U:

> `g(U)>=W_U+27-|U|`.                                       (O2)

Hence the decoration outside U satisfies

`g(H\U)<=28-(W_U+27-|U|)`

and therefore

> `g(H\U)<=1+|U|-W_U`.                                      (O3)

## 3. If alpha(H[U])=3, all outside support vertices have positive common-S charge

Assume

`alpha(H[U])=3`.                                             (O4)

Take z in H\U.

If `w_z=0`, then z lies outside every support. Row closure against every support containing a given u in U gives

`zu` target-nonedge.

Thus z is target-anticomplete to U.

An independent3-set in H[U] together with z would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> `w_z>=1` for every z in H\U.                               (O5)

## 4. Undecorated outside vertices are almost all one-spoke pivots

Because z lies outside all owner supports, it has no target neighbour in the nine-owner clique Y.

In the fully-decorated shell its only possible shell target neighbours lie in `S union {r}`.

Since `g_r=0`, the exact degree identity for z is

> `g_z=w_z+e_F(z,r)-1`.                                     (O6)

By (O5), if `g_z=0` then

`w_z=1`, `e_F(z,r)=0`.                                      (O7)

Now

`w_z=kappa_z+e_F(z,S)=1`.

There are only two possibilities:

1. `kappa_z=1`, `e_F(z,S)=0`;
2. `kappa_z=0`, `e_F(z,S)=1`.

CORE211 has total excess

`sum_H kappa=2`.

Therefore at most two undecorated outside vertices are of type1.

Every other undecorated outside vertex has

- core degree12;
- exactly one target neighbour in the old shell, lying in S;
- no target neighbour r or Y.

Hence it is a legal degree13 **one-spoke pivot**.

## 5. General one-spoke count

There are `35-|U|` vertices outside U.

By (O3), at most `1+|U|-W_U` of them can carry positive global decoration.

Hence at least

`(35-|U|)-(1+|U|-W_U)`

outside vertices are undecorated.

After removing the at-most-two core-excess exceptions from Section4, the number k of legal one-spoke pivots satisfies

> **support-to-one-spoke bound**
>
> `k>=32-2|U|+W_U`.                                         (O8)

This is the main bridge theorem.

It uses no attachment classification.

## 6. The M=6, b=0 two-block equality window forces k>=14

Now specialize to a maximal disjoint support pair D,E with

`M=m_D+m_E=6`,

and no bridge owner:

`b=0`.

The two-block incidence budget gives

`e_H(D union E)<=5`.                                        (O9)

A 6-vertex graph with independence number at most2 has at least6 target edges (equivalently its complement is triangle-free and has at most9 edges).

Hence (O9), together with the ambient `alpha(H)<=3`, forces

> `alpha(H[D union E])=3`.                                  (O10)

Thus alpha(H[U])=3 as well, and Sections3--5 apply.

The remaining three owner rows lie on one-sided support classes meeting `D union E`.

Any support vertex outside D union E which is shared by two distinct support classes would be a proper-overlap point and therefore have zero common-S charge. By (O5), no support-union vertex outside D union E can have zero charge.

Hence private petal sets of distinct one-sided support classes are disjoint.

Each owner support has size3 and meets D union E in at least one point, so a distinct one-sided support introduces at most two new core vertices. There are at most three distinct one-sided support classes because they carry only three owners.

Therefore

`|U|<=6+6=12`.                                               (O11)

Every introduced private support vertex has positive integer charge. If P is the number of private support-union vertices outside D union E, then

`|U|=6+P`,
`W_U>=P`.                                                    (O12)

Substituting into (O8):

`k>=32-2(6+P)+P`
` =20-P`.

Since `P<=6`,

> `k>=14`.                                                    (O13)

Thus every M=6,b=0 survivor automatically creates at least fourteen legal one-spoke pivots.

## 7. Every such one-spoke anti-neighbourhood carries at least17 decoration units

Let v be any one-spoke pivot, with unique shell target neighbour `s in S`, support

`D=N_H(v)`, `|D|=12`,

and anti-neighbourhood

`Z=H\(D union {v})`, `|Z|=22`.

The exact CORE211 one-spoke formula and D14 give universally

> `q_v>=22+g_s+g(D)`.                                       (O14)

The current pivot is q32-maximal, so `q_v<=32`. Therefore

`g(D)<=10-g_s`.                                              (O15)

The one-spoke vertex itself is undecorated, so

`g(Z)=G_H-g(D)`.

In the fully-decorated N=9 state

`G_H=26+m+c`,

while every s in S is decorated and therefore `g_s>=1`.

Hence

`g(Z)>=26+m+c-(10-g_s)`

and therefore

> `g(Z)>=17`.                                                 (O16)

So the M=6,b=0 equality window forces a simultaneous family of at least14 twenty-two-point anti-neighbourhoods, each carrying at least17 units from a global decoration budget of at most28.

## 8. Quantitative overlap consequences

Let the k>=14 one-spoke anti-neighbourhoods be `Z_1,...,Z_k`.

Then

`sum_i g(Z_i)>=17k`.                                        (O17)

Since total core decoration is at most28, some decorated core vertex lies in at least

> `ceil(17k/28)`                                             (O18)

of the anti-neighbourhoods.

For k=14 this is at least9.

At k=14, splitting decoration into unit tokens, the total coverage is at least238 over at most28 tokens. Convexity gives the sharp pair-intersection lower bound

`sum_(i<j) g(Z_i intersect Z_j)>=896`,                        (O19)

because the minimum occurs with fourteen tokens of multiplicity9 and fourteen of multiplicity8.

Hence some pair satisfies

> `g(Z_i intersect Z_j)>=10`.                                (O20)

Likewise

`sum_(i<j<l)g(Z_i intersect Z_j intersect Z_l)>=1960`,       (O21)

so some triple intersection carries at least6 decoration units.

Thus the final two-block equality window is a very high-codegree multi-pivot object, not three local attachment cases.

## 9. Unified frontier

The remaining contradiction can now be stated without attachment enumeration:

> **High-Codegree One-Spoke Compatibility Lemma (OPEN).**
> A CORE211 core cannot contain at least14 one-spoke legal pivots whose 22-point anti-neighbourhoods each carry at least17 units of decoration from a global budget at most28, while satisfying the exact q32 repivot identities and the shell-label triangle-cover constraints.

Proving this lemma closes the entire `M=6,b=0` fully-decorated two-block window at once.

This is the same multi-pivot object as the q36 shell-poor regime, but with much stronger numerical parameters (`14,17,28` instead of `5,11,28`).

## 10. Generalization

Equation (O8) is parameterized by core order, total owner incidence, core excess and global decoration budget. It is therefore reusable whenever a fully-decorated support equality state leaves many low-charge vertices outside the support union.
