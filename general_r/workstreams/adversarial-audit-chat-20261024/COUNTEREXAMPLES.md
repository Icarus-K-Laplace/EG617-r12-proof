# Counterexamples and Witness Families

## CE-F-001 — arbitrary-leftover affine family

### Target killed

Any stability statement asserting that all balanced colorings of `K_{r^2}` are `O(r)` or `o(r^2)` **edge recolorings** from the standard affine construction in which one color receives both of the final two parallel classes.

### Canonical witness schema

Assume an affine plane of order `r` with parallel classes

`P_1,...,P_r,Q`.

For each `i`, color every edge joining two points in one block of `P_i` by color `i`. Let

`phi:E(Q)->[r]`

be arbitrary and color each remaining `Q`-edge by `phi(e)`.

Every `(r+1)`-set contains an edge from each color `i`, because `P_i` is a partition into `r` blocks.

Thus every `phi` is a valid balanced coloring.

### Distance certificate

The number of `Q`-edges is

`m0=r*C(r,2)=r^2(r-1)/2`.

Choose `phi` so that no color receives more than `ceil(m0/r)` of these edges. Any standard single-heavy-color assignment colors all `Q`-edges with one color, so at least

`m0-ceil(m0/r)`

edges must be recolored.

This is `Theta(r^3)`, not `O(r)` and not `o(r^2)`.

### Scope

This is an infinite counterexample family for all prime-power orders and any other orders admitting an affine plane.

It does **not** refute a stability theorem whose notion of distance ignores the free `Q`-edge labels and measures only distance to the underlying net/partition skeleton.

## No graph witness yet for B

No graph satisfying the full three-anchor contract with `K<=7` has been found in Round G-001. The analytic AES closure already excludes all `r>=68`; the adversarial search target is therefore `12<=r<=67`.
