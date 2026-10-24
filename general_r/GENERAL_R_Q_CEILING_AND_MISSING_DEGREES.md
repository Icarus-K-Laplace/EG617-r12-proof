# General-r q Ceiling and Missing-Degree Collapse

Status: **PROVED_SYMBOLIC CONDITIONAL ON THE GENERAL 4r+1 RESIDUAL-CORE CONTRACT**.

Assume r>=12 and a legal target residual F on `4r+1` vertices satisfying the inherited hereditary cap, with a degree-(r+1) pivot and core H satisfying the general residual-core contract.

## 1. Maximum residual edge layer

The hereditary target cap is

`D_r(n)=C(n,2)-(r-1)p_r(n)`.

For `n=4r+1`, the balanced r-clique partition has one part of size5 and r-1 parts of size4, so

`p_r(4r+1)=10+6(r-1)=6r+4`.

Therefore

> **`e(F)<=D_r(4r+1)=2r^2+4r+4`.**

For r=12 this is340.

## 2. Baseline core floor

By `GENERAL_R_CORE_FLOOR_AES.md`, under the core contract

`e(H)>=[r(3r-1)+2]/2`.

The exact backend identity is

`e(F)=C(r+2,2)+q+e(H)`.

Hence

`q <= 2r^2+4r+4 - C(r+2,2) - [r(3r-1)+2]/2`.

The right side simplifies to

> **`q<=3r+2`.**

Thus the r=12 high-right ceiling38 is the specialization of the structural critical value

> **`q_*(r)=3r+2`.**

## 3. Quadratic repivot base

Every regular repivot of missing degree d satisfies

`q_y>=d(r+1-d)`.

Here `0<=d<=r`, since d is the missing degree inside an `(r+1)`-point shell and the vertex itself is not counted.

At a maximum-q state under the global ceiling, any legal regular missing degree must satisfy

`d(r+1-d)<=3r+2`.

The quadratic is symmetric under `d<->r+1-d`, subject to the actual domain `0<=d<=r`.

## 4. Large-r collapse

For every `4<=d<=r-3`, concavity gives

`d(r+1-d)>=4(r-3)`.

If `r>=15`, then

`4(r-3)>3r+2`.

Therefore:

> **For every r>=15, every regular shell vertex at a legal maximal backend pivot has missing degree**
>
> **`d in {0,1,2,3,r-2,r-1,r}`.**

Thus all intermediate support sizes disappear automatically for sufficiently large r.

This is a major asymptotic simplification: the r=12 d4/d9 large-support Bridge-C phenomenon exists only because r=12 lies below the threshold15. At r=13,14 the boundary d=4 remains arithmetically possible; from r=15 onward it is forbidden by the universal q ceiling before any detailed support geometry is used.

## 5. Anchor-branch strengthening

If the desired exact three-anchor theorem `K_r>=8` is proved, then the core edge floor in the anchor branch becomes

`e(H)>=[r(3r-1)+8]/2`.

At the maximum residual edge layer this gives

> **`q<=3r-1`.**

For r=12 this is35, exactly the strengthened E-305 right-edge envelope at E=340.

Under this stronger ceiling, d=4 is already excluded for every r>=12 because

`4(r-3)>3r-1` iff `r>11`.

Hence the anchor branch would have only d<=3 / d>=r-2 endpoint geometry for the entire general range r>=12.

## 6. Strategic interpretation

The symbolic critical scale is linear in r, while the repivot base is quadratic in interior d. Therefore all sufficiently large-r complexity is automatically pushed to bounded-distance-from-endpoint support sizes.

This is exactly the asymptotic phenomenon sought in the general-r programme: fixed-width shallow endpoint layers survive, while the medium-support case tree disappears.
