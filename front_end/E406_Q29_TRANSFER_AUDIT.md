# E406 q29 transfer audit

Status: `PROVED TRANSFER`.

## Statement

Every E406 degree-13 pivot with `q=29` has a legal degree-13 repivot y with

`q_y>=30`.

## Source theorem

The standalone theorem `backend/Q29_GOOD_REPIVOT_FULL_PROOF.md` proves:

> q29 + standard inherited 13-shell contract + core minimum degree at least12
> implies an undecorated shell vertex y with q_y>29.

The numerical 35-core edge count211 is not used in that existence theorem.

Because the backend source theorem is written in the R(4,49) context while the current object is a 61-point T61 residual with a 47-point core, this note audits the actual hypotheses one by one rather than transferring by label.

## Hypothesis audit

For an E406 q29 pivot p:

1. `alpha(M)<=10`.
   An M-independent 11-set is a target K11 in the shell; with p it would form a forbidden K12 because `omega(R)<=11`.

2. `z=e(M)>=22`.
   This is exactly the inherited 14-point D-cap shell floor.

3. `nu(M)>=3`.
   This is the proved h13 shell matching lower bound used throughout the front-end low-layer proofs.

4. Missing-edge weighted lower bound.
   `E406_CORE_MINDEG_288.md` gives `delta(C)>=12` for the q29 286-edge core, and `E406_Q27_Q28_ELIMINATION.md` proves the stronger

   `t_u+t_v>=13`

   for every M-edge. The backend q29 proof requires only the weaker PAIR-12 interface.

5. Missing-triangle lower bound.
   Every M-triangle has row-weight sum at least24, the same inherited T61 shell contract used in the backend theorem.

6. Missing-K4 lower bound.
   In T61, a missing K4 has row-union size at least36, hence row-weight sum at least36. This is stronger than the K4 lower bound used by the standalone q29 proof.

7. Exact subset and repivot identities.
   These are purely local shell/core identities and hold unchanged for the 13-shell / 47-core decomposition.

8. Core minimum degree.
   q29 gives `e(C)=286`, and the modern front-end core theorem gives `delta(C)>=12`.

No step of `backend/Q29_GOOD_REPIVOT_FULL_PROOF.md` uses the global 49-vertex independence bound alpha<=4 except through the listed shell row-cover inequalities. Those inequalities are independently inherited here, with equal or stronger constants.

Therefore the standalone analytic three-case proof transfers verbatim at its actual hypothesis level.

## Conclusion

Every E406 q29 pivot has an undecorated legal repivot y with

`q_y>29`.

Since q is integral,

`q_y>=30`.

Combined with:

- `E406_LOW_Q_PROMOTION_22_26.md`;
- `E406_Q27_Q28_ELIMINATION.md`;

all E406 charge levels below30 are now independently controlled. The remaining boundary-forcing problem is purely the q30/q31 coexistence/plateau step.
