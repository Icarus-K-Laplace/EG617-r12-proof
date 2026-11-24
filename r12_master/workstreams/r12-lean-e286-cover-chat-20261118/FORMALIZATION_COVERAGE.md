# Coverage by mathematical claim

## Fully formalized

- Inherited GATE47 with its complete CoreAdmissible4 contract;68 inherited
  source/config files remain unchanged.
- The original E286 hypotheses, excess8, actual regular independent four seeds,
  private cliques, the disjoint partition and exact support surplus5.
- The cap-free25-point obstruction, common-neighbor bound
  c(x,y)<=3+epsilon(x)+epsilon(y)<=11 and K10 completion charge>=7.
- Complete ten-orbit classification, including finite-domain completeness and
  equivalence with actual graph supports under seed permutations.
- Actual pair blockers and K11/K11 local charge>=6; concentrated small-side charge>=6.
- Actual triple-K11 local charge>=3, with sorting and all capacity premises derived.
- Both h3 terminal exclusions; e286_actual_support_eight_remaining follows from
  the original five hypotheses without an extra terminal assumption.

These claims are verified at51358b4, CI44890957575. Full statements and proof
bodies, all axiom dependencies, hashes and complete CI logs are retained.

## Partially formalized

- E286 nonexistence: three h4 and five h5 support orbits remain.
- The287-edge floor: GATE47 is proved, but the <=285 and equality exclusions are open.

## Not formalized

- core47_edge_floor_287, h12/h13 terminals, AES, repivot licensing and Q classifications.
- COVER_verified and the original K145 MainTheorem.

Diagnostic enumerations are tests only. The finite support certificate is a
separate kernel proof, including a proof that its domain is exhaustive.
