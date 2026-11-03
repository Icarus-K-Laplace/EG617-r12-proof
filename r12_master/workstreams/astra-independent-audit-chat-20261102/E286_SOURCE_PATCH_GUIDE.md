# Required source patch for E286 D-support closure

Target frozen source (do not edit in this audit branch):
`r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`

Target section: **Section 9, “Eliminate P and D”**, immediately after the paragraph establishing the pointwise D accounting and before the paragraph beginning “If one K10 has two completing mixed points...”.

## Why a patch is required

The existing D-case conclusion assumes that each K10 has at least one mixed point completing it. Formula (5) only gives a five-unit charge to a noncompleting mixed point when an additional point completing the same K10 is available. The frozen text does not prove existence of such a completer. The zero-completer possibility is therefore not covered by the displayed final case split.

## Inserted lemma

Insert the complete lemma and proof from `E286_D_SUPPORT_REPAIR.md`, under the heading:

**Lemma (each K10 has a mixed completer).** In support pattern D={01,02,03,12,13}, each of K0 and K1 is completed by at least one of its two incident mixed support points.

For K0, write P=z01, A=z02, B=z03. Assume for contradiction that neither A nor B completes K0. The K10/K10 point P has three exhaustive possibilities:

1. **P misses both K10s.** The three scalar blockers f10,10(P), f10,11(A), f10,11(B) charge at least2+4+4=10. Their common K0 charge is pointwise additive; the opposite missing sets lie in distinct cliques and the three support points are distinct.
2. **P completes K1 but misses K0.** The two mixed blockers A,B charge at least8. Equality under T<=8 forces both unique (2,3) minima, with all excess on A,B and zero excess on clique vertices and P. P's zero excess forces |A0|>=8. The two K0 missing sets A2,A3 must avoid A0, hence both equal K0\A0, a 2-set. A vertex in that common set has at least 9 internal K0 neighbors, the neighbor P, and all three vertices in each of B2,B3, giving degree at least16, contradiction.
3. **P completes K0.** Then P is an additional K10-completer for both noncompleting mixed points A,B. Formula (5) charges at least5 to each. Their shared K0 center charges are pointwise additive, and the opposite missing sets and support points are disjoint, so T>=10.

Thus at least one of A,B completes K0. By symmetry, at least one of z12,z13 completes K1.

The full derivation, including the pointwise degree inequalities for overlapping missing sets, is already written in `E286_D_SUPPORT_REPAIR.md`; use that file as the authoritative insertion text rather than this summary.

## After integrating

1. Update the frozen E286 theorem source in a new proof revision (do not rewrite the historical frozen commit).
2. Update the E286 source-workstream `SHA256SUMS.txt`.
3. Update the integration `SOURCE_MANIFEST.json` to the new E286 source commit/blob.
4. Regenerate the root `SHA256SUMS.txt` and update all affected receipts.
5. Rerun the E286 verifier and the root verifier from a clean checkout.
6. Re-run the 28-node theorem-to-source crosswalk against the new commit.

Until these steps are complete, the strict 287-edge floor and final K145 theorem should be described as conditional on this repair, not as fully self-contained in frozen snapshot `c5f05f...`.
