# General-r Endpoint Support Collapse

Status: **PROVED_SYMBOLIC CONDITIONAL ON THE GENERAL q-CEILING BACKEND CONTRACT**.

By `GENERAL_R_Q_CEILING_AND_MISSING_DEGREES.md`, for every r>=15 a legal regular shell missing degree satisfies

`d in {0,1,2,3,r-2,r-1,r}`.

Now consider a common-S owner class with missing/support size d and N owners. If L is the leftover shell set,

`d+N+|L|=r+1`.

Hence

> **`N<=r+1-d`.**

For the high endpoint sizes:

- d=r-2 => `N<=3`;
- d=r-1 => `N<=2`;
- d=r => `N<=1`.

Therefore no high-endpoint common-S class can carry owner multiplicity growing with r.

Consequently:

> **For r>=15, every common-S family whose owner demand is unbounded in r must have `d<=3`.**

Thus the scalable support-compatibility problem for all sufficiently large r reduces automatically to

- d0/d1 local one-spoke/trivial-support geometry;
- d2 repeated-pair systems;
- d3 repeated-triple systems.

The d2/d3 systems are precisely the support sizes already covered by the symbolic zero-signature/sunflower/owner-capacity machinery.

This is a second asymptotic simplification beyond the disappearance of medium support sizes: even the surviving high endpoint sizes are bounded-owner exceptions.
