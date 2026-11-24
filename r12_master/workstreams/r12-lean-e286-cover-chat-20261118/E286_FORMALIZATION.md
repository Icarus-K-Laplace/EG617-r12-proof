# Original E286 contract and current reduction

Frozen source: frozen/E286.md, with immutable provenance in SOURCE_PROVENANCE.json.
E286Hypotheses is exactly47 vertices,286 edges, minimum degree>=12, alpha<=4,
omega<=11. The abstract theorem has no hereditary D cap.

Verified code51358b42e0406d2ae23a45594b01ece73f9998f6, CI44890957575.

The original hypotheses imply actual regular independent seeds, the private-clique
partition, surplus5 and complete membership in the ten frozen support orbits.
The finite-domain completeness proof precedes the kernel-reduced orbit check.
Actual inverse seed reindexing proves equivalence with graph neighborhoods.

Frozen Section5's two h3 orbits are now excluded:
- {0123,01,23}: disjoint pair charges6+6 exceed total excess8.
- {01,023,123}: a concentrated small-side pair charge6 and the disjoint opposite
  triple charge3 exceed total excess8. Both small-side orientations are covered
  by actual seed permutations, including equality of missing-set sizes.

The triple charge derives a local pointwise excess bound under contradiction,
chooses a smallest missing set, and proves the residual forced adjacency/capacity
contradiction. No ordered missing distribution is assumed in the private-clique
theorem. Positive missing sets follow from omega<=11; forced edges from alpha<=4.

The strongest theorem e286_actual_support_eight_remaining assumes only G and
E286Hypotheses G, and produces actual seeds and a support count vector in
e286SupportOrbitRepresentatives.tail.tail. Full source and elaborated statements
are available in the Lean files and complete CI log.

The three h4 and five h5 orbits remain. Shared-center accounting, double-pair
equality structure and the remaining terminal exclusions are open. E286Statement
is still only a target definition. LEVEL5A has not been attained.
