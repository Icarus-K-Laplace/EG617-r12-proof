# Asymptotic Inequality Ledger

All backend formulas are under an extracted legal `4r+1` residual unless explicitly stated otherwise.

Write

- `E=e(F)`;
- `D=D_r(4r+1)=2r^2+4r+4`;
- `epsilon=D-E>=0`;
- `K=2e(H)-r(3r-1)`;
- `q=e(M)+G_A`.

## 1. Exact master conservation law

From `E=C(r+2,2)+q+e(H)`:

> **`K=6r+6-2epsilon-2q`.**

Equivalently:

> **`q+epsilon=3r+3-K/2`.**

Also `r(3r-1)` is even, so K is always even.

Consequences:

- `K>=7` iff `K>=8`;
- baseline `K>=2` gives `q<=3r+2-epsilon`;
- `K>=8` gives `q<=3r-1-epsilon`.

## 2. Main ledger

| quantity | lower | upper | scalable gap / threshold | dependency |
|---|---:|---:|---|---|
| residual order | `4r+1` | `4r+1` | exact | A_ext extraction |
| residual degree minimum | `r+1` | — | automatic for `r>=17` | extracted residual + hereditary cap |
| residual edges `E` | — | `2r^2+4r+4` | deficit `epsilon` | hereditary cap |
| core order | `3r-1` | `3r-1` | exact | residual theorem |
| core minimum degree | `r` | — | automatic for `r>=17` | extracted residual theorem |
| core excess `K` | `2` baseline; `8` for r>=68 | `2r-2` | linear window | core floor/cap + anchor |
| charge `q` | `0` | `3r+2-epsilon`; with K>=8 `3r-1-epsilon` | slope 3 | master law |
| regular support degree `d` | `0` | `r` | base `d(r+1-d)` | repivot identity |
| medium support base | `4r-12` | q ceiling | slope 4 vs 3 | endpoint collapse |
| common-S owner multiplicity `N` | `0` | hereditary `r-O(1)`; fixed-deficit multicolour `r/2+O_epsilon(1)` | slope halved | multicolour stability |
| zero signatures | `0` | `3` | O(1) | `alpha(H)<=3` |
| zero vertices | `0` | `3r-1` | no global O(1) bound | OPEN |
| d2 one-loss charge `W` | three-class `3r-2` | exact `K+2r-2+a+b` | `K+a+b>=r` | d2 barrier |
| high support complement | — | `<=2` target shell neighbours per high owner | O(1) | endpoint collapse |
| high owners | `0` | `3` | absolute O(1) | sibling repivot |
| high shell kernel | `0` | `9` | absolute O(1) | sibling repivot |
| high core signatures | `1` | `8` | absolute O(1) | sibling repivot |
| decorated shell count `tau` | `[r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2` | `r+1` | slope `1/2` for fixed epsilon | low regular clique cap + high owners<=3 |
| recurrence/extraction depth | `0` | unknown | upstream only | A_ext OPEN |
| exact terminal type count | — | not yet O(1) globally | d2 and d0/d1 remain scalable | C* OPEN |

## 3. Automatic residual contract threshold

A sibling theorem proves that if an induced `4r+1` residual with `alpha<=4`, `omega<=r-1` and the inherited cap exists, then for every `r>=17`:

- `delta(F)=r+1`;
- a legal exact pivot exists;
- `delta(H)>=r`.

The threshold comes from the `3r` exclusion using Andrasfai-Erdos-Sos:

`2r-2 > 5(3r)/8`,

which holds for `r>16`.

Thus the asymptotic front does not need a separate minimum-degree hypothesis.

## 4. Universal medium-degree slope theorem

Suppose `K>=kappa`. Then

`q<=3r+3-epsilon-kappa/2`.

For `4<=d<=r-3`:

`d(r+1-d)>=4(r-3)=4r-12`.

Hence the whole medium interval is impossible whenever

> **`r>15-epsilon-kappa/2`.**

Worst case epsilon=0:

| kappa | first r excluding all medium d |
|---:|---:|
| 2 | 15 |
| 4 | 14 |
| 6 | 13 |
| 8 | 12 |

More generally, `K>=-lambda r-O(1)` with fixed `lambda<2` still gives asymptotic medium-degree collapse.

## 5. Multicolour slope-half obstruction

At deficit epsilon, every regular target clique B satisfies

`2|B| <= r-1+2epsilon+epsilon sqrt(4epsilon+1)`.

For a common-S owner family:

> **`N <= [r-3+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon, owner capacity has slope 1/2.

For d3, the independent fixed-deficit contradiction threshold is

> **`r>11+epsilon sqrt(4epsilon+1)`.**

The sibling repivot workstream gives a stronger all-deficit common-S d3 closure under the residual/anchor setup.

## 6. Decoration-heavy terminal inequality

Low-endpoint regular shell vertices form a regular target clique, so their number is at most

`[r-1+2epsilon+epsilon sqrt(4epsilon+1)]/2`.

The stronger endpoint theorem gives at most three high regular owners. Therefore

> **`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon:

> **`tau>=r/2-O_epsilon(1)`.**

Exact repivot transport is

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.

Hence a fixed-deficit terminal with no tau-improving repivot must support a linear-size balanced decoration incidence system. This is a candidate route to a design-like rigidity theorem.

## 7. d2 synthesis target

For an exact one-loss three-class d2 terminal:

> **`K+a+b>=r`**, `b in {0,1}`.

Thus survival requires linear core excess or allowance. Any theorem

> **`K+a <= (1-c)r+O(1)`**

for fixed c>0 kills the three-class d2 terminal for all sufficiently large r.

Alternative: prove owner demand above `(1/2+c)r-O(1)` and contradict the multicolour owner capacity.

## 8. Full-colour slack

For `n=r^2+1`, if `s_i=e(G_i)-p_r(n)>=0`, then exactly

> **`sum_i s_i=r^2(r-1)/2`.**

Average slack is `C(r,2)`. Ordinary single-colour stability therefore leaves `Theta(r^2)` edits per colour; the front/design route needs a genuinely multicolour compatibility gain.
