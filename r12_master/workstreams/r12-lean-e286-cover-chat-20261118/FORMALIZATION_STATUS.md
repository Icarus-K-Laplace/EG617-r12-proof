# E286 support reduction

Current verified checkpoint: 5732057d5414d8b50d8fa791d5e0d3c583a3e50e, Linux CI 45607411708.
Theorem e286_actual_support_D_or_C derives the exact two remaining count vectors
from E286Hypotheses. All h4 orbits and the h5 nine-clique, P and B orbits are
excluded. The open h5 cases are D and C (frozen Sections 9 and 11–12).
E286 exclusion and the 287-edge floor remain open.

## Earlier six-orbit checkpoint

Code db9f2848d77da0e484c9ba35ee965fe8cd683230, clean Linux CI 45555580430.

Under the five original E286 hypotheses the strongest result,
e286_actual_support_six_remaining, gives actual regular independent seeds
and membership in the six final support representatives. The newly excluded
orbit is {01,012,03,23}. One h4 star and five h5 orbits remain.

The second h4 proof derives its three actual pair points, all clique sizes,
the extra-completer charge and the shared-leaf inequality. The three cases
give total excess at least 10, 13 or 11 against the exact budget 8.
See H4_SECOND_DISJOINTNESS_REVIEW.md for the distinct regions in each sum.

The build checked 334 declarations including 283 theorems. All nine
pins and all Lean source/config SHA256 values matched. The dependency audit
starts at the six-orbit theorem and traverses 385 project constants,
including private proof bodies. The only transitive axioms are propext,
Classical.choice and Quot.sound.

GATE47 retains LEVEL4. E286 exclusion, the 287-edge floor, COVER and the
original K145 MainTheorem remain open. See OPEN_BLOCKERS.md.
