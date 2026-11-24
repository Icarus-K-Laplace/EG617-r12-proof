# EG617 E286 / COVER: PARTIAL

Pending candidate (2026-11-25): E286Mixed.lean contains the actual K10/K11
mixed-pair dichotomy; kernel verification is pending. The verified milestone
below remains unchanged, with eight support orbits still open.

Verified code: 51358b42e0406d2ae23a45594b01ece73f9998f6
Successful clean Linux CI: 44890957575.

The strongest result is e286_actual_support_eight_remaining. From the original
five E286 hypotheses it derives actual regular independent seeds and a support
distribution in the last eight entries of the exhaustive ten-orbit list.
Both h3 orbits are excluded. The three h4 and five h5 orbits remain.

The proof includes exact excess8, the private-clique partition, a complete finite
support domain, actual seed reindexing, actual blocker edges, a concentrated
pair charge>=6 and a triple-K11 local charge>=3. No terminal premise is assumed.

All318 declarations and267 theorems passed actual lake builds, full #check/#print
inspection, transitive axiom audit and source/config SHA256 checks. Only propext,
Classical.choice and Quot.sound occur. All nine dependencies match their pins.
All68 inherited source/config files are unchanged. The corrected proof-body
dependency audit visits245 project constants and verifies required proof paths.

LEVEL4 GATE47 remains VERIFIED. LEVEL5A E286 nonexistence, LEVEL5B the287-edge
floor, LEVEL6A h12/h13, LEVEL6B COVER and LEVEL7 MainTheorem remain FORMALIZATION_GAP.
MainTheorem is absent. No progress percentage or complete EG617 proof is claimed.

The initial dependency audit at efda572 saw only public theorem types; its marker
is explicitly not complete dependency evidence. The corrected private-body audit
has passed and the defect is documented in DEPENDENCY_AUDIT.md.
