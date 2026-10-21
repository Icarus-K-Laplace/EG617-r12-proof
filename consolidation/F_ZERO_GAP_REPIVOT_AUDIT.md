# F-version zero-gap repivot audit

Status: `RECOVERY_AUDIT / REUSABLE_CANDIDATE`.

## Recovered lemma

In a degree-13 shell with 35-point inherited core `B`, let `u` be an undecorated shell vertex (`g_u=0`), so repivot at `u` is legal. For a missing-shell neighbor `v in N_M(u)`, the F-version computes the degree of `v` in the repivoted core

`B_u=(B\D_u) union N_M(u)`

as

`d_{B_u}(v)=|N_M(u) union N_M(v)| + g_v - 1 - |D_u intersect D_v|`.

If every legal 35-point core has minimum degree at least 11, then

`|N_M(u) union N_M(v)| + g_v >= 12`.

In particular, if also `g_v=0`, then every missing edge between two undecorated shell vertices satisfies

`|N_M(u) union N_M(v)| >= 12`.

This is the historical `zero-gap repivot obstruction`.

## Why this matters now

The current canonical E332 branch has the stronger core input `delta(H)>=12`, so the minimum-degree licensing needed by the historical lemma is available once the repivot core is verified to remain in the same admissible class.

The lemma immediately implies that two undecorated low-degree shell vertices cannot be adjacent in the missing graph; more generally it sharply restricts any missing edge whose endpoints have regular degrees in `{1,2,11,12}`. This is directly relevant to the current E332 extreme-shell frontier

`d_M(regular) in {0,1,2,11,12}`,  `4<=G<=8`.

## Historical branch-specific material not promoted

The same F-version also closes ABAB/ABAC subbranches under a historical `s=12, nu(N)=2` classification and develops an `s=14` six-row residual problem. Those arguments depend on branch-specific normal forms and are not imported into the canonical E332 proof merely because they are labelled PROVED in the historical draft.

## Promotion requirement

Before this obstruction is used canonically, write a standalone proof in current notation and verify:

1. the repivot at every invoked `u` is genuinely degree 13;
2. the repivoted 35-point object still lies in the class to which the core minimum-degree theorem applies;
3. the formula above uses current missing-edge semantics and no retracted nonedge rule.

If these checks pass, this lemma should be moved from consolidation into `backend/` as a reusable repivot theorem.
