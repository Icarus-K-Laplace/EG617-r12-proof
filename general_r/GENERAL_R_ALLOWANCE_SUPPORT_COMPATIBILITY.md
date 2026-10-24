# General-r Allowance Transport and Support Compatibility

Status: **PROVED_SYMBOLIC CONDITIONAL ON THE GENERAL COMMON-S BACKEND CONTRACT**.

This file isolates the part of the r=12 machinery that is genuinely independent of the numerical value12.

## 1. Common-S setup

Assume a legal backend pivot with

- shell A of size `r+1`;
- core H with minimum degree at least r and `alpha(H)<=3`;
- a family Y of regular shell owners sharing one shell missing set S;
- `|S|=d`, `|Y|=N`;
- leftover `L=A\(S union Y)`, so

  `d+N+|L|=r+1`.

For a shell point s, let `D_s=N_H(s)`, let

`g_s=d_F(s)-(r+1)`,

and define for core vertices

`kappa_v=d_H(v)-r`.

For an owner y let `D_y=N_H(y)`.

## 2. General transport slack

For `s in S`, let

`m_L(s)=d_M(s,L)`

and define

> **`sigma_s=m_L(s)+g_s-|L|`.**

The common-S cross-budget argument gives `sigma_s>=0` whenever the legal owner-repivot minimum-degree contract holds.

## 3. Exact anchor-transport identity

After repivoting owner y, the point s moves to the new core H_y.

Its new-core degree is

`d_(H_y)(s)=d-1-m_S(s)+|D_s|-|D_s intersect D_y|`.

Because s is missing to every owner,

`|D_s|=N+m_S(s)+m_L(s)+g_s`.

Using `d+N+|L|=r+1` gives

> **`d_(H_y)(s)-r = sigma_s-|D_s intersect D_y|`.**

Since every legal repivot core has minimum degree at least r,

> **`|D_s intersect D_y|<=sigma_s`.**

Therefore

> **zero transport slack (`sigma_s=0`) makes s a degree-r anchor in every owner-repivot core and forces `D_s intersect D_y=empty` for every owner y.**

This theorem is exactly independent of r.

## 4. Exact allowance localization

Let

`B=e_M(L)+G_L`

and define the common-S ambient allowance by

`a=q-d(r+1-d)-B`.

The exact shell residual identity gives

`q-d(r+1-d)`
`=e_M(S)+e_M(L)+(G_S-e_F(S,L))+G_L`.

Since

`G_S-e_F(S,L)=sum_(s in S)sigma_s`,

we get

> **`a=e_M(S)+sum_(s in S)sigma_s`.**

Thus allowance has only two sources for every r:

1. internal shell missing edges inside S;
2. positive transport slack on S.

No r=12-specific correction remains.

## 5. Symbolic row closure and common-S charge

For a core vertex v define

`w_v=kappa_v+e_F(v,S)`.

General row closure is

> **`e_H(v,D_y)<=w_v`** for every `v notin D_y`.

If `w_v=0`, then

- `kappa_v=0`, hence `d_H(v)=r`;
- `e_F(v,S)=0`.

Thus zero common-S charge is an exact minimum-degree/anticompleteness certificate for every r.

## 6. Incidence signatures are r-independent

For a zero-charge support-union vertex v define

`sig(v)={D : v in D}`.

If zero-charge vertices u,v have different signatures, row closure forces uv to be a target nonedge.

Hence the number of distinct zero-charge signatures is at most `alpha(H)`.

Under the desired residual-core contract `alpha(H)<=3`:

> **at most three zero-charge signatures occur.**

If three occur, representatives form an independent triple of exact degree-r vertices.

Therefore the signature-diversity branch reduces immediately to the **general exact-three-anchor excess theorem**.

## 7. Collapsed-signature sunflower branch

If at most two zero signatures occur and the active supports are boundary one-loss supports,

`Delta(D)=d-1`,

then every support contains a zero-charge point and its zero set is a union of whole signature classes.

Thus every support belongs to at most

`2^2-1=3`

nonempty zero-skeleton patterns.

Supports with the same zero skeleton form exact common-core sunflowers.

For d=2, every nontrivial repeated pattern is a common-zero-hub target-K2 sunflower with one positive private petal.

For d=3, every nontrivial repeated pattern is one of the same two symbolic types as at r=12:

- Type H: one zero hub + two unit-charge private petals, support K3;
- Type P: one zero pair + one positive private petal, support a two-edge triple or K3.

This classification depends on support size and `alpha(H)<=3`, not on r.

## 8. General owner capacity interface

The geometry above feeds directly into `GENERAL_R_OWNER_CAPACITY.md`.

In the first hereditary-cap range, the asymptotic capacities are

- d2 Type D: `N<=r-3+o(1)`;
- d3 Type H/P: `N<=r-4+o(1)`.

Thus the complete support-compatibility schema is already all-r once three upstream inputs are supplied:

1. the general residual-core contract;
2. the exact-three-anchor excess theorem;
3. the hereditary cap `D_r(t)` in the induced-set range used by packing.

## 9. General support dichotomy

Conditional on those inputs:

> **General Support-Compatibility Dichotomy.** Every boundary one-loss d2/d3 common-S system either
>
> 1. produces three independent degree-r anchors; or
> 2. collapses into at most three canonical sunflower patterns with explicit hereditary owner capacities.

This is the symbolic form of the r=12 Global Support-Compatibility Master Theorem.
