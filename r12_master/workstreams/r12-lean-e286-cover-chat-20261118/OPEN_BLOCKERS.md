# Open parent obligations

E286 and the 287-edge floor passed Linux CI 45609105445 and 45610341669.
For h13 the frozen COVER lower bounds require, in each energy layer, a
regular pivot realizing the required charge. The upper bound from the floor
alone cannot give this witness. The h12 closure and original K145 root remain open.

## Historical E286 obligations

Code db9f2848d77da0e484c9ba35ee965fe8cd683230, clean Linux CI 45555580430. The current reduction leaves six support orbits.

1. The remaining h4 star {01,02,03,123} needs simultaneous center accounting,
   including zero-missing-set cases and distinct completing vertices.
2. The five h5 orbits need the small-budget double-pair lemma, K9 completion
   accounting, P/D/B exclusions and the same-K11-pair obstruction for C.
   Frozen Sections7-12 have not yet been proved in Lean.
3. Separately locate/formalize the frozen <=285 exclusion before the287-edge floor.
   GATE47 alone gives degree>=12 and hence only e>=282; it does not give e>=286.
4. The supplied COVER source proves h13 only. h12 needs its own frozen source.
   AES, repivot licensing, all Q27/Q28/Q29/Q30 classifications and Family I/II
   completeness remain unformalized. Both old/new minimum-degree conditions matter.
5. Original K145 MainTheorem is absent. No parent theorem is promoted by this checkpoint.

This is a FORMALIZATION_GAP, not evidence that the frozen mathematical proof is false.
