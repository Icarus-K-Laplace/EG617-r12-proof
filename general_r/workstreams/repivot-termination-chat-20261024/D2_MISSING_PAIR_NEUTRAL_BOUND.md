# d2 Missing-Pair / Neutral-Population Bound — RETRACTED

Status: **`DISPROVED_AS_STATED`**.

## Dependency audit

The previous argument treated the common target-nonneighbours in F of a target-nonedge pair as a clique. That is valid only if

`alpha(F)<=3`,

because two nonadjacent common nonneighbours together with the original pair form an independent 4-set.

The actual general backend hypothesis is instead

> **`alpha(F)<=4`.**

Therefore an independent 4-set is allowed, and the common-nonneighbour set need not be a clique. Consequently the following previously claimed conclusions are withdrawn:

- `kappa(D)>=zeta-1` for a target-nonedge core pair D;
- `a>=zeta` for a q-flat nonedge d2 support;
- the saturated common-nonneighbour equality template at `a=zeta`.

## What remains valid

The purely core counting identity for a nonedge pair `D={x,z}` is still valid. If C denotes the vertices of `H\D` target-nonadjacent to both x and z and

`c=|N_H(x) intersect N_H(z)|`,

then

> **`|C|=c+r-3-kappa(D)>=r-3-kappa(D)`.**

This follows only from `|H|=3r-1` and the core degrees and does not use the false global independence assumption.

Because `alpha(H)<=3`, the induced graph H[C] has independence number at most 3, but C is not forced to be a clique. Any corrected neutral-population theorem must therefore use a valid extremal bound for such a set or another compatibility identity.

## Research consequence

The nonedge-support branch in the fully decorated d2 plateau remains open. This file is kept as an explicit negative audit certificate so the invalid clique step is not reused.