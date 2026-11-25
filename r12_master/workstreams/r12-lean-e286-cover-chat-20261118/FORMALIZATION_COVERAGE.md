# Coverage by mathematical claim

## Fully formalized

- Inherited GATE47 with its complete CoreAdmissible4 contract;68 inherited
  source/config files remain unchanged.
- Original E286 hypotheses, excess8, actual regular independent four seeds,
  private cliques, disjoint partition and exact support surplus5.
- Cap-free25-point obstruction, common-neighbor bound
  c(x,y)<=3+epsilon(x)+epsilon(y)<=11 and K10 completion charge>=7.
- Complete ten-orbit classification, finite-domain completeness and actual
  graph equivalence under seed permutations.
- Actual K11 pair blockers and charge>=6, concentrated charge>=6 and triple charge>=3.
- Actual K10/K11 completion-or-charge4 dichotomy, with all missing-set and
  cross-edge premises derived from the original graph hypotheses.
- Multiplicity2 produces distinct actual vertices; both h3 exclusions and
  the first h4 exclusion {01,01,023,23}.
- Actual extra-completer charge5 and shared-leaf union bound.
- Second h4 exclusion and e286_actual_support_six_remaining, from the original five hypotheses.

Code db9f2848d77da0e484c9ba35ee965fe8cd683230, clean Linux CI 45555580430. Full statements, proof bodies, transitive
axioms, hashes, proof dependency trace and complete Linux CI logs are retained.

## Partially formalized

- E286 nonexistence: one h4 and five h5 support orbits remain.
- The287-edge floor: GATE47 is proved, but <=285 and equality exclusions are open.

## Not formalized

- core47_edge_floor_287, h12/h13 terminals, AES, repivot licensing and Q classifications.
- COVER_verified and the original K145 MainTheorem.

Diagnostic enumerations are tests only. The finite support certificate is a
separate kernel proof including a proof that its domain is exhaustive.
