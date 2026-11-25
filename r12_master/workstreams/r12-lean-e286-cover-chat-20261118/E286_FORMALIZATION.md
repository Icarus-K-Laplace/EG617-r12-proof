# Original E286 contract and current reduction

Frozen source: frozen/E286.md; immutable provenance: SOURCE_PROVENANCE.json.
E286Hypotheses is exactly47 vertices,286 edges, minimum degree>=12, alpha<=4,
omega<=11. The abstract theorem has no hereditary D cap.

Code db9f2848d77da0e484c9ba35ee965fe8cd683230, clean Linux CI 45555580430.

The original hypotheses imply actual regular independent seeds, the private-clique
partition, surplus5 and complete membership in the ten frozen support orbits.
Finite-domain completeness precedes the kernel-reduced orbit check.
Actual inverse seed reindexing proves equivalence with graph neighborhoods.

The following terminal orbits are excluded:
- Section5 {0123,01,23}: disjoint charges6+6 exceed total excess8.
- Section5 {01,023,123}: concentrated small-side charge6 plus disjoint triple
  charge3. Both orientations, including tied missing-set sizes, are covered.
- Section6 {01,01,023,23}: the actual support-count fiber of size2 supplies distinct
  01 points. A point missing the K10 has a nonempty K11 missing set by omega<=11;
  alpha<=4 forces the cross-blocker edges. The actual mixed charge is at least4.
  It is disjoint from the 23 charge6, so both 01 points must complete the K10.
  Their combined excess>=7 is disjoint from the 23 charge6, again contradicting8.

The mixed scalar domain is complete: positive missing sizes a<=10, b<=11 are
derived from inclusion in the actual cliques. Kernel interval_cases/norm_num
proves (9-a-b)+a*(b-3)+b*(a-2)>=4 over Nat, where subtraction is truncated.
The zero K10 missing set is covered by the completion branch, never silently omitted.
The diagnostic script supplies no Lean assumptions or proof terms.

Frozen Section 6, second h4 orbit {01,012,03,23}: actual support fibers
give three distinct exterior witnesses. The 01 point completes K0 since
its alternative costs 4 disjoint from 6. If 03 also completes K0, the two
completers cost 7 disjoint from 6. Otherwise the extra 01 neighbor and
the shared K3 accounting give 5+6 on disjointly accounted vertices.

e286_h4_second_orbit_impossible derives this contradiction from the exact
count vector. e286_actual_support_six_remaining obtains actual seeds and
membership in the final six representatives from E286Hypotheses alone.
One h4 and five h5 orbits remain. E286Statement is open.
