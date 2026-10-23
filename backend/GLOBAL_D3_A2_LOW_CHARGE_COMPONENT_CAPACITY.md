# Global d=3 A2 Low-Charge Intersecting-Component Capacity

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_INTERSECTING_COMPONENT_CAPACITY.md`;
- common-S row closure;
- `alpha(H)<=3`;
- the fully-decorated q32 charge bound `W<=36`.

Purpose: sharpen the coarse eight-owner intersecting-family bound in the actual q32 fully-decorated equality channel. The only coarse eight-owner geometry is a three-class global-common-hub family, but such a family already forces far more than 36 units of common-S charge.

## 1. Existing taxonomy

Every pairwise-intersecting d3 support family at allowance2 is one of:

1. global common pair;
2. global common zero hub;
3. no global zero core.

The existing theorem gives owner capacities

- common pair: at most6;
- common hub: at most8;
- no global zero core: at most6.

Thus only the three-class global-common-hub geometry can exceed6 owners.

## 2. Three-class common-hub geometry

Let the three distinct support classes be

`D_i={x} union P_i`, `i=1,2,3`,

where x is the common zero-charge hub and each private pair P_i has two vertices.

From the intersecting-component classification:

- every P_i induces a target K2;
- private pairs from distinct support classes are target-anticomplete;
- every private pair carries total charge at least1;
- at most two support classes can be Z-type, so at least one is H-type and carries private charge2.

Hence the six private petals contribute at least

> `1+1+2=4`                                                   (L1)

units of common-S charge.

The pattern union has seven vertices.

## 3. Every outside core vertex has charge at least two

Take

`z in H\({x} union P_1 union P_2 union P_3)`.

If z were not target-complete to any private pair P_i, choose from each P_i a petal target-nonadjacent to z.

The three chosen petals are pairwise target-nonadjacent because distinct private pairs are cross-anticomplete.

Together with z they form an independent4-set, contradicting `alpha(H)<=3`.

Therefore z is target-complete to at least one P_i.

Since z lies outside support D_i, common-S row closure gives

`e_H(z,D_i)<=w_z`.

Completeness to the two petals already contributes two target neighbours in D_i, so

> `w_z>=2`.                                                    (L2)

There are `35-7=28` outside vertices. Hence

`W>=4+2*28=60`.                                               (L3)

This contradicts the fully-decorated q32 bound

`W<=36`.

Therefore the three-class global-common-hub geometry is impossible in the actual equality channel.

## 4. Sharpened capacity

The remaining intersecting geometries already have owner capacity at most6.

Hence:

> **Low-charge intersecting-component capacity theorem.**
> In the q32 fully-decorated allowance-two state with `W<=36`, every pairwise-intersecting support family carries at most
>
> `6`
>
> owner rows.                                                 (L4)

Moreover, any six-owner intersecting component is necessarily either

- a three-class global-common-pair equality family; or
- one of the no-global-core three-class equality families.

It is never a three-class common-hub family.

## 5. Support-intersection graph consequence

The final nine-owner support hypergraph has matching number2.

If its support-intersection graph has two connected components, each component must be pairwise intersecting: otherwise two disjoint supports in one component together with any support from the other component would form a matching of size3.

Therefore each component has owner weight at most6 by (L4).

Since the total owner count is9, the only component-weight splits are

`3+6`, `4+5`, `5+4`, `6+3`.

A six-owner component is forced into one of the sharp three-class non-hub equality geometries above.

This converts the two-component residual into a global zero-signature compatibility problem rather than a multiplicity partition problem.

## 6. Generalization

The charge-barrier argument depends only on a small core independence number and a bound on total common-S charge. In any analogous pivot system, a three-class common-hub component forces every outside core vertex to pay at least two charge units.