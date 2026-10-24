# E408 exact-129 contextual blocker / duplicate theorem

Status: **PROVED_RELATIVE_TO KANG-PIKHURKO EQUALITY CLASSIFICATION**, using the exact seven-block equality system.

## 1. Only KP Type I survives the contextual clique cap

Let C be a non-target color restricted to the E408 T61 residual R, and suppose

`e_C(R)=129`.

The balanced and target-residual constraints give

- `alpha(C[R])<=12`;
- `omega(C[R])<=5`.

The Kang-Pikhurko equality classification for the 129-edge second-Turan layer allows the part-size types

- Type I: `(5^12)`;
- Type II: `(4,5^10,6)`;
- Type III: `(4,4,5^8,6,6)`.

In the color-graph complement translation, every ordinary KP part induces a clique in C[R]. Therefore Types II and III contain at least one K6 and violate `omega(C[R])<=5`.

Hence in the genuine T61 context:

> **every exact129 non-target color is KP Type I.**

Its color graph has

- ten isolated K5 components;
- one 11-point exceptional gadget U formed from two 5-point cliques plus the KP exceptional vertex x.

The gadget U has clique number exactly5.

## 2. Blockers of maximum independent12-sets

A maximum independent12-set of C[R] consists of

- one vertex from each of the ten isolated K5 components;
- an independent2-set from the exceptional gadget U.

Let X subset R meet every maximum independent12-set.

If X does not contain all five vertices of one isolated K5 component, then for every isolated component one can choose a vertex outside X. Therefore, in order to hit every maximum independent12-set, X intersect U must meet every independent2-set of C[U].

Equivalently, `X intersect U` is a vertex cover of `bar(C[U])`.

Since `omega(C[U])=5`, the maximum independent set of `bar(C[U])` has size5. Thus every such vertex cover has size at least

`11-5=6`.

Consequently:

> every blocker X of the maximum independent12-sets has size at least5;
>
> a blocker has size exactly5 iff it is exactly one of the ten isolated K5 components;
>
> every other blocker has size at least6.

## 3. Apply to one outer target K12 block

Use the E408 global decomposition

`G=7K12 dot_union R`

from `E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md`.

Fix one target block B_i and one exact129 non-target color C.

For each b in B_i, the set

`N_C(b) intersect R`

must meet every maximum independent12-set of C[R]. Otherwise a maximum independent12-set disjoint from this neighbourhood, together with b, would be a C-independent13-set.

Thus each of the twelve vertices b has a blocker neighbourhood in R.

At most ten of these twelve blocker neighbourhoods can have size5 if the total incidence is to be minimized: each size5 blocker must be one of the ten isolated K5 components, and two vertices of the same target block cannot both use the same K5 as their entire C-neighbourhood in R. Indeed, if b,b' had the same K5 blocker, then b,b' are C-nonadjacent (they lie in the same target block), while R minus that K5 contains an independent11-set; together they would form an independent13-set.

Therefore at least two block vertices have C-degree at least6 into R. Hence

`e_C(B_i,R)>=10*5+2*6=62`.

## 4. Duplicate consequence

The exact near-Latin row rule from `E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md` writes

`e_C(B_i,R)=61+r_i(C)`

with `r_i(C)>=0` the number of R-vertices whose repeated color toward B_i is C.

The preceding lower bound gives

> **`r_i(C)>=1` for every target block B_i and every exact129 color C.**

Summing over the seven target blocks,

> **`R_C=sum_i r_i(C)>=7`.**

Since an exact129 color has `s_C=0`, its global duplicate budget

`P_C+R_C+s_C=62`

therefore sharpens to

> **`P_C<=55`.**

## 5. E408 implication

The E408 residual excess satisfies

`sum_C s_C=3`,

so at least eight of the eleven non-target colors are exact129 colors.

Therefore each of the seven outer target K12 blocks spends at least eight of its 61 duplicate slots on those exact129 colors before any contribution from the remaining at-most-three nonexact colors is counted.

This is a new 145-point completion constraint not visible in the local Q32/Q33 shell equations.
