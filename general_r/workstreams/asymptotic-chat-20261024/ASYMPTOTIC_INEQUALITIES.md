# Asymptotic Inequality Ledger

All formulas are under the legal `4r+1` residual/core setup unless explicitly stated otherwise.

Write

- `E=e(F)`;
- `D=D_r(4r+1)=2r^2+4r+4`;
- `epsilon=D-E>=0`;
- `K=2e(H)-r(3r-1)`;
- `q=e(M)+G_A`.

## 1. Exact master conservation law

From

`E=C(r+2,2)+q+e(H)`

and the definition of K,

> **`K = 6r+6-2epsilon-2q`.**

Equivalently,

> **`q+epsilon = 3r+3-K/2`.**

This is the shortest synthesis identity in the backend.

Also `r(3r-1)` is always even, so

> **K is always an even integer.**

Consequences:

- `K>=7` is exactly equivalent to `K>=8`;
- the baseline core floor `K>=2` gives `q<=3r+2-epsilon`;
- `K>=8` gives `q<=3r-1-epsilon`.

## 2. Main ledger

| quantity | lower bound | upper bound | asymptotic gap / note | dependency |
|---|---:|---:|---|---|
| residual edges `E` | not globally sharp | `2r^2+4r+4` | parameterize by `epsilon` | hereditary cap |
| core edges `e(H)` | `[r(3r-1)+2]/2` baseline; `[...+8]/2` in anchor branch | `(3r^2+r-2)/2` | linear excess window | core contract; anchor for +8 |
| core excess `K` | `2` baseline; `8` for r>=68 in anchor branch | `2r-2` | width `Theta(r)` | core floor/cap; three-anchor |
| charge `q` | `0` | `3r+2-epsilon` baseline; `3r-1-epsilon` with K>=8 | linear | master law |
| regular support degree `d` | `0` | `r` | base charge `d(r+1-d)` | repivot identity |
| medium support base | `4r-12` | q ceiling | slope 4 vs slope 3 | endpoint collapse |
| common-S owner multiplicity `N` | `0` | hereditary: `r-O(1)`; fixed-deficit multicolour: `r/2+O_epsilon(1)` | multicolour halves slope | owner-capacity theorem |
| zero signatures | `0` | `3` distinct zero-charge signatures | O(1) types | alpha(H)<=3 |
| zero vertices | `0` | `3r-1` generically | no global O(1) count known | OPEN for stronger bound |
| d2 one-loss charge `W` | three-class: `3r-2` | exact `K+2r-2+a+b` | yields `K+a+b>=r` | sibling endpoint classification |
| common-nonneighbour transversal | `r-3-rho+codeg(u,v)` | `3r-1` | linear positive capacity for bounded rho | Bridge B |
| high-support complement `s=r+1-d` | `1` | `3` after endpoint collapse | O(1) | q ceiling |
| high endpoint total owners | `0` | `3` | absolute O(1) | sibling repivot |
| high shell kernel | `0` | `9` vertices | absolute O(1) | sibling repivot |
| high core signatures | `1` | `8` | absolute O(1) | sibling repivot |
| recurrence depth | `0` | unknown | no all-r bound yet | front extraction OPEN |
| exact backend terminal type count | — | not yet O(1) globally | d2 multiplicity/charge still scalable | OPEN |

## 3. Universal medium-degree slope theorem

Suppose `K>=kappa` and use the exact q ceiling

`q<=3r+3-epsilon-kappa/2`.

For every `4<=d<=r-3`,

`d(r+1-d)>=4(r-3)=4r-12`.

Hence the whole medium interval is impossible whenever

`4r-12 > 3r+3-epsilon-kappa/2`,

i.e.

> **`r > 15-epsilon-kappa/2`.**

Worst case is `epsilon=0`. For the even lower bounds relevant here:

| `kappa` | worst-case first r excluding every medium d |
|---:|---:|
| 2 | 15 |
| 4 | 14 |
| 6 | 13 |
| 8 | 12 |

Thus exact `K>=8` is not needed for asymptotic endpoint collapse: the already-proved baseline `K>=2` is enough from `r>=15` onward.

More generally, if only

`K >= -lambda r - C`

with fixed `lambda<2`, then

`q <= (3+lambda/2)r+O(1)`,

while the medium base is `4r-O(1)`, so all medium supports still disappear for sufficiently large r.

## 4. Multicolour slope-half obstruction

At residual deficit epsilon, every regular target clique B satisfies

`2|B| <= r-1+2epsilon+epsilon sqrt(4epsilon+1)`.

For a common-S owner family this gives

> **`N <= [r-3+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon the owner-capacity slope is therefore `1/2`, not `1`.

For d3, regular-clique extraction and the q budget yield the explicit contradiction threshold

> **`r > 11 + epsilon sqrt(4epsilon+1)`.**

Therefore d3 is excluded throughout any window `epsilon=o(r^(2/3))` for sufficiently large r; the sibling repivot workstream in fact closes the d3 common-S sector under A+B for every r>=12.

## 5. New d2 synthesis target

The exact one-loss three-class d2 barrier is

`K+a+b>=r`, with `b in {0,1}`.

So every surviving three-class d2 terminal must spend a linear amount of one of two resources:

- core excess K; or
- allowance a.

This is the most useful current slope split. Any theorem of the form

`K+a <= (1-c)r+O(1)`

for some fixed `c>0` would kill the three-class d2 terminal for all sufficiently large r.

A different sufficient route is to prove a majority common-S demand exceeding the multicolour slope-half owner capacity.

## 6. Front/design global slack

For the full colouring on `n=r^2+1`, with colour slacks

`s_i=e(G_i)-p_r(n)>=0`,

one has exactly

> **`sum_i s_i = r^2(r-1)/2`.**

Average slack is `C(r,2)`. Ordinary one-colour stability therefore leaves `Theta(r^2)` edits per colour; an all-large-r front/design proof needs a genuinely multicolour compatibility gain rather than a sharper one-colour estimate alone.
