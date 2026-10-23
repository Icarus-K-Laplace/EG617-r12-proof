# Global d=3 A2 Two-Component Exact Reduction

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_LOW_CHARGE_COMPONENT_CAPACITY.md`;
- `GLOBAL_D3_A2_INTERSECTING_COMPONENT_CAPACITY.md`;
- `GLOBAL_D3_A2_M6_ALL_BRIDGE_CLOSURE.md` (hence maximal disjoint-pair weight `M<=5`);
- zero-charge incidence-signature theorem;
- common-S row closure;
- `alpha(H)<=3`, `W<=36`.

Purpose: replace the entire two-connected-component support regime in the final fully-decorated nine-owner state by one exact four-support weighted skeleton.

## 1. Component graph setup

Let the vertices of the support-intersection graph be the distinct support classes; two classes are adjacent when they intersect.

The final fully-decorated nine-owner support hypergraph has matching number exactly2.

Assume its support-intersection graph has two connected components `C1,C2`.

Supports from different components are disjoint.

If one component contained two disjoint support classes, those two together with any support from the other component would form a matching of size3.

Therefore:

> each connected component is pairwise intersecting.          (T1)

By the low-charge intersecting-component theorem, each component carries at most6 owners.

## 2. A three-class component cannot coexist with another component

Consider a component containing three distinct support classes.

The intersecting-component taxonomy leaves only three structural types.

### 2.1 Three-class global common hub

This geometry is impossible at `W<=36` by `GLOBAL_D3_A2_LOW_CHARGE_COMPONENT_CAPACITY.md`.

### 2.2 Three-class no-global-core geometry

Such a component uses three distinct zero-charge incidence signatures.

Any support in the second component contains at least one zero-charge vertex: if all three support vertices had positive integer charge then its support charge would be at least3, contradicting row defect at most2.

That zero-charge vertex has an incidence signature disjoint from all support classes of the first component, hence a fourth zero signature.

But at most three zero signatures exist under `alpha(H)<=3`.

Contradiction.

### 2.3 Three-class global common pair

Let the common zero pair be `{x,y}` and let the three supports be

`D_i={x,y,z_i}`, i=1,2,3.

The private petals z_1,z_2,z_3 are pairwise target-nonadjacent.

Take any core vertex v belonging to any support of the second component. The components are support-disjoint, so v lies outside each D_i.

If v were target-nonadjacent to all three private petals, then

`{v,z_1,z_2,z_3}`

would be an independent4-set, contradiction.

Hence v is target-adjacent to at least one z_i. The common pair x,y is zero-charge and lies outside every support of the second component, so it is target-anticomplete to v; equivalently the only possible target edge from v into D_i is vz_i.

Row closure against D_i therefore gives

`w_v>=1`.

Thus every vertex of every support in the second component has positive integer charge. Any 3-support there has total charge at least3, contradicting row defect at most2.

Therefore a three-class common-pair component also cannot coexist with another component.

Combining the three cases:

> **In a two-component support system, each component has at most two distinct support classes.**   (T2)

## 3. A 1-class plus 2-class split is impossible

Suppose one component has one support class and the other has two.

A single support class carries at most4 owners by the K11+D14 support packing bound.

A two-class pairwise-intersecting component carries at most5 owners by the intersecting-component theorem.

To reach the total owner count9, the capacities must both be saturated:

- the single class has multiplicity4;
- the two-class component has total multiplicity5, so one of its classes has multiplicity at least3.

Supports from different components are disjoint. Hence these two classes form a disjoint pair carrying at least

`4+3=7`

owners.

But all `M>=6` maximal-disjoint-pair windows are already closed; every remaining state satisfies

`M<=5`.

Contradiction.

Therefore:

> both components contain exactly two support classes.        (T3)

## 4. Exact owner multiplicities

Each two-class intersecting component carries at most5 owners.

The two component owner totals are positive and sum to9, so they must be

`4` and `5`.

Consider the four-owner component. If its class multiplicities were `(3,1)`, then its maximum class has weight3. The five-owner component necessarily has a class of multiplicity at least3. These two classes are disjoint across components, producing a disjoint-pair weight at least6, impossible.

Hence the four-owner component has exact multiplicities

> `(2,2)`.                                                    (T4)

The five-owner component has two positive class multiplicities summing to5. Its maximum must be3, since a value4 combined with either multiplicity2 from the other component would again give a disjoint pair of weight6.

Therefore its exact multiplicities are

> `(3,2)`.                                                    (T5)

Thus the only two-component residual is:

> **Exact two-component skeleton**
>
> - four distinct support classes;
> - two intersecting supports with multiplicities `(2,2)`;
> - two intersecting supports with multiplicities `(3,2)`;
> - every support in one pair is disjoint from every support in the other pair.   (T6)

## 5. Remaining structural choice

A two-class intersecting component has a global zero core equal to the intersection of its two supports. Its size is either

- one: common-hub type;
- two: common-pair type.

No no-global-core case exists for only two classes.

Hence the entire two-component problem has been reduced to four type combinations

`hub/hub`, `hub/pair`, `pair/hub`, `pair/pair`

on the exact weight skeleton `(2,2) | (3,2)`.

This is the next and final two-component bridge; no owner-multiplicity case split remains.