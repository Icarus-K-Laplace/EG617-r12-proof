# CANONICAL STATE — EG617 general-r asymptotic synthesis

Updated: 2026-10-24

Branch: `workstream/general-r-asymptotic-20261024`

## Headline status

**Problem 617 is NOT proved unconditionally for all sufficiently large r.**

The strongest current synthesis theorem is:

> **S68-v2 — CONDITIONAL_ON_Aext_C*_D + ASYMPTOTIC_ANALYTIC.**
>
> For every `r>=68`, if the upstream extraction/design dichotomy `H_A^ext`, remaining endpoint terminal closure `H_C*`, and design-terminal stability/nonextension `H_D` hold at r, then `P(r)` holds.

Two formerly load-bearing hypotheses are now derived rather than assumed:

1. the complete legal residual pivot/core contract follows automatically from an extracted `4r+1` residual for every `r>=17`;
2. Exact Three-Anchor `K>=8` follows analytically for every `r>=68`.

## 1. Current strongest theorem: r>=68

`H_A^ext + H_C* + H_D => P(r)` for every `r>=68`.

Here `H_A^ext` only asks:

> force an induced `4r+1` residual with `alpha<=4`, `omega<=r-1`, inherited least-colour cap, or a controlled `5r+1` design-like terminal.

It no longer assumes `delta(F)=r+1`, an exact pivot, or `delta(H)>=r`.

## 2. Proven residual branch certification

Sibling residual-extraction theorem, head

`07cd8fb58ffd93d234b1e8b6104f939175d7fbda`:

for every `r>=17`, an extracted legal `4r+1` residual automatically has

- `delta(F)=r+1`;
- a degree-`(r+1)` pivot;
- core `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Thus the front open problem is now purely upstream extraction/stopping classification.

## 3. Hypotheses still open

### H_A^ext — OPEN
Force `4r+1` residual or controlled `5r+1` terminal.

### H_C* — OPEN
Terminal-only backend closure is enough; a universal potential is not required. Remaining content is dominated by scalable d2, plus d0/d1 and finite high skeletons.

### H_D — OPEN
Robust classification/nonextension of the `5r+1` design-like terminal. Exact affine-plane nonextension is already proved.

### H_B — no longer asymptotic hypothesis
Latest checked three-anchor head `a98ef900be419993e3fe63d37a0cf82fa104c455`; full theorem remains `PROVED_ANALYTIC` for r>=68 and open below 68.

## 4. Current minimum r0

- H_B-free, core-certification-free conditional synthesis: **68**.
- With original full H_A and H_B assumed: **12**.
- Unconditional Problem 617 r0: **not yet finite/proved**, because A_ext, C*, D remain open.

The latest residual theorem strengthens the hypotheses but does not lower numeric r0 because its threshold 17 is below 68.

## 5. Inequality controlling r0

The sole active numeric threshold is

`2r-9 > 5(3r-1)/8`

iff

`r>67`.

This is the three-anchor complement/AES threshold. Backend endpoint collapse is already valid from r>=12 once K>=8; residual certification is valid from r>=17.

## 6. Master asymptotic conservation law

Let

`epsilon=D_r(4r+1)-e(F)`

and

`K=2e(H)-r(3r-1)`.

Then

> **`K=6r+6-2epsilon-2q`**

or

> **`q+epsilon=3r+3-K/2`.**

K is always even. Hence `K>=7` is equivalent to `K>=8`.

A generic K-floor `K>=kappa` eliminates all medium supports once

`r>15-epsilon-kappa/2`.

## 7. Certified small-r-only pathologies

1. d2 concentrated `K=8,a=3,b=1` three-class state: only `r<=12`;
2. d4 / d=(r-3) medium states: gone from r>=15 using baseline K>=2, and for all r>=12 under K>=8;
3. four high owners: coarse slope contradiction from r>=13, r=12 equality separately closed;
4. balanced `(r+1)^3` near-anchor extra coarse-cover cell: only r=12;
5. d3 allowance-five/top-q frontier: fully closed under the residual/anchor setup for all r>=12;
6. d2 charge-one disjoint-support proliferation: uniformly bounded by eight, not a growing-r family.

## 8. Backend terminal boundedness

Under K>=8,

`d in {0,1,2,3,r-2,r-1,r}`.

So support-degree width is O(1).

Stronger:

- d3 common-S: closed;
- high endpoint: at most 3 owners, shell kernel <=9, core signatures <=8, hence finite bounded-complement skeleton;
- d2: still scalable, with one-loss three-class barrier `K+a+b>=r`;
- d0/d1: not yet frozen.

Therefore the **full backend exact type count is not yet proved O(1)**. The obstruction is d2 plus d0/d1, not the high endpoint.

## 9. Multicolour decoration synthesis

The near-extremal shell dichotomy bounds low regular vertices by the fixed-deficit multicolour clique capacity. Combining that with the stronger high-owner bound `<=3` gives

> **`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon,

> **`tau >= r/2-O_epsilon(1)`.**

Together with exact transport

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`,

any fixed-deficit non-improving terminal must organize linearly many decorations into a rigid incidence system.

## 10. Sibling sensitivity

For numeric r0: three-anchor threshold 68 is most sensitive.

For existence of an unconditional infinite-family theorem:

1. A_ext extraction/stopping dichotomy;
2. C* endpoint closure, especially d2;
3. D design stability;
4. lowering three-anchor below 68 is optimization only.

## 11. Next highest-leverage asymptotic inequality

The clearest scalar backend target is:

from surviving d2

`K+a+b>=r`,

prove for some fixed c>0

> **`K+a <= (1-c)r+O(1)`.**

This would kill the scalable three-class d2 terminal for all sufficiently large r.

Alternative multicolour route: force common-S owner demand `N>(1/2+c)r-O(1)` and contradict the slope-half owner capacity.

Potential/design route: combine `tau>=r/2-O_epsilon(1)` with transport to force strict improvement or a bounded-parameter design.

## Imported sibling heads used

- architecture base: `3dc54c38e13a71e8a12330c3c36b1aa1063aacaa`;
- residual extraction: `07cd8fb58ffd93d234b1e8b6104f939175d7fbda`;
- three-anchor latest checked: `a98ef900be419993e3fe63d37a0cf82fa104c455`;
- repivot termination imported: `2974fd80882a4545a3a1a569418405ec4e3bdebc`;
- near-extremal shell dichotomy: `578830ff3fd9eab94f2bb5a498d90a1a303ba2e1`.
