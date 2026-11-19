# Coverage by mathematical claim

This file reports logical coverage, not a percentage or a declaration-count score.

## Fully formalized

- Inherited GATE47, including the original CoreAdmissible4 contract: verified
  code2b4b74f, CI44139599116. Its68 inherited source/config files remain unchanged.
- E286 degree sum572, excess8, exceptional support at most8, and actual regular
  independent four seeds. The five abstract E286 hypotheses are unchanged.
- The cap-free25-point alpha2 obstruction, correct common-neighbor bound
  c(x,y)<=3+epsilon(x)+epsilon(y)<=11, and K10 completion excess charge7.
- Actual private cliques, their disjoint partition with the multiple-support set,
  exact surplus5, and complete actual support count classification into ten orbits.
- Actual pair-blocker forced edges; K11/K11 local six-unit charge; impossibility
  of two complementary K11 pair supports. These are verified at86e9970,
  CI44498020540, with complete types, axiom audit and source hashes.

## Partially formalized

- E286 support terminal elimination. Oriented seed realization and the first
  canonical count-orbit exclusion are VERIFIED at90130d8, CI44498770093.
  The nine-remaining-orbits theorem is proved from the original hypotheses.
  The other terminal exclusions
  and shared-center/triple-K11 charge arguments are not yet formalized.
- The287-edge floor has its inherited degree gate, but still needs both the
  <=285 exclusion and E286 equality exclusion. Neither is assumed as a premise.

## Not formalized

- E286 nonexistence itself; core47_edge_floor_287.
- h12/h13 terminals, AES dependency, Q27/Q28/Q29/Q30, repivot licensing,
  COVER_verified, and original K145 MainTheorem.

All diagnostic enumerations are tests only. The complete support certificate
is separately proved inside Lean, including its finite domain completeness.
No custom mathematical axiom or unproved terminal proposition is introduced.
