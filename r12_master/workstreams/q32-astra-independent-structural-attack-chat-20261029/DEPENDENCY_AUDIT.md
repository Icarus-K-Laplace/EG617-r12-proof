# Dependency audit

Date: 2026-10-29

## Immutable source heads read

- high-support: 433a5b39a98325f00e99650b0270d79f7753a47d.
- low-support: 9afd7c1a59056052974f9dc78933010d10e88bba.
- global root: 6e61d995a257bc854c3df2fb47d9da7bc6c6e160.

The initial high-support commit contains the new exact nonexact-gap saturation theorem. The global root audit still referred to c6500b24 and its count-vector defect; by the frozen high-support HEAD that defect was already corrected. Source parameters remain a=1,2,3,4 with (d(y),d(x))=(4+a,9-a).

## Source interfaces actually read

High-support: V47_ALL_COLOR_RESERVE; HIGH_SUPPORT_NEAR_TURAN; V47_PIVOT_NEIGHBORHOOD_PACKING; V47_Z01_TRACK_ALIGNMENT; V47_Z01_CANONICAL_RESIDUAL_ONE_FACTORIZATION; V47_Z01_RESIDUAL_SIGNATURE_INJECTIVITY; V47_Z01_PARTIAL_PROJECTION_PACKING; V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER; V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM; V47_Z01_NONEXACT_GAP_SATURATION; ROOT_DEPENDENCY_DAG; CANONICAL_STATE; RETRACTION_FIREWALL; Q32_132_MINDEG3; Q32_FULLSUPPORT_VERTEX_LABELLED_CSP; light-component, zero-slack, and outer-holonomy reduction files.

Parent: FRONTEND_BRIDGE_THEOREM; T61_NEW_LEMMAS; T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD; E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM; E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.
Global inherited source: KANG_PIKHURKO_EXACT129_SOURCE_AUDIT; Q32_CORE285_TERMINAL; CONTRACT_FIREWALL.

## New theorem dependencies

The outside-edge reserve is elementary: alpha(C)<=12, omega(C)<=5, independent track sizes, and the pivot star. Its proof uses no external extremal theorem, no source-mode enumeration, no residual projections, and no solver.

The simultaneous packing contradiction additionally uses edge ownership and e(F)-e(H)=123. The registered z=0,1 application imports the alignment proof; it does not independently replay the entire upstream light-graph classification.

The source of omega(C)<=5 is explicit: alpha(F)<=5, since a monochromatic non-target K6 would be a target-independent6-set. The source of omega(F)<=11 is different: maximality of the target K12 packing. These must not be interchanged.

## Source-level defect: target clique cap

Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md at the frozen HEAD states omega(G_C)<=5 for all twelve colors. This overrestricts color0. The actual target F has omega(F)<=11; only the eleven non-target colors have cap5. The aligned submodel imposes a target K12, so it is already inconsistent with the actual parent cap11, but its automatic K6 rejection is not a valid derivation from the relaxed core contract. Repair the target/non-target distinction before trusting any generic-model UNSAT.

The actual parent also requires alpha(F)<=5 on all61 vertices, not just alpha(H)<=4. A missing constraint makes a model a relaxation; an unjustified stronger target constraint is more serious because UNSAT need not transfer. Source implementation inspection is recorded in COUNTEREXAMPLE_SEARCH.md.

## Previously corrected or withdrawn items

- Degree-nine exceptional point / injectivity: forbidden.
- Triple special K5 placement: remains legal until independently excluded; cannot be confused with isolated triple placement.
- Eight-vertex isolated-double gadget residual: must remain covered.
- Strong gadget quota (3,4,4) requires full target degree>=13 at the relevant point. Safe unconditional core quota is (4,5,5).
- Common P is choice-dependent, not canonical.
- Pair-key uniqueness does not replace actual cross-key edge disjointness.
- Root count vectors at current high-support HEAD: m8=(8*129,130,130,130), m9=(9*129,130,131), m10=(10*129,132), target408.
- Historical small-to-outer matching rigidity was retracted; this proof does not use it.

## Root firewall

Final read-only refresh to high-support541653af1a28187d9b05ddcbcb118c5460fe3f1c: the sibling added outside-component bijection and the same aligned-cell K6 closure. These changes were inspected in full. They agree with the corresponding equality-case proof here but do not establish the uniform57-edge theorem or the broader nonempty-fiber exclusion. They also leave the all-colors K6 CSP cut unchanged. Low-support/root heads did not change.

The broader14-type exclusion additionally imports the local4,5,5 switch classification, singleton/double-track blocker, outerK7 holonomy, residual clique fibers, and exact outer degree/endpoint ledgers. The new proof explicitly distinguishes common small labels from outer labels. It excludes only cells with both fiber partitions nonempty; empty-label double-track escapes remain possible at the local level. The low-support canonical/dependency audit was read at its named HEAD without rerunning low-support casework. The latest global audit continues to mark E407 parent coverage and Q33 support promotion OPEN.

## 2026-10-30 source refresh and z4 dependency boundary

Read the full541653af..1de8a375 comparison:4cf1935ba2fc791ecde5e677e38bbe531b9cd376 adds the six z3 residual types;1de8a37556ba98ccbb8651f39a5192629453f0f1 adds the weighted-heavy-graph catalog. These are necessary structural catalogs, not closures. Our new z4 theorem imports neither catalog. It needs the same local3+7 normal form already named above, exact zero-slack residual neighborhoods at z4, delta(H)>=12, alpha(H)<=4, and the genuine parent omega(H)<=11.

The light-neighbor lemma is applied only adjacent to the explicitly forced special form; it does NOT reinstate the retracted general matching-rigidity assertion. The4,5,5 switch has its two extra endpoints in different small labels when viewed across a light outer pair. The new proof keeps those labels explicit and independently rechecks all normalized triples.

The parent full-degree bound delta(F)>=13 is not needed for the z4 theorem. It would permit the stronger (3,4,4) gadget quota only after its full-parent applicability is restored; the relaxed core alone still supports only (4,5,5). We do not silently strengthen that relaxed contract or edit sibling code.

The z4 proof closes the actual empty-class escape in C3+C4 within the registered normal form, not just a necessary scalar test. Its transfer to full Q32 is conditional on the upstream reduction proving that a candidate enters this normal form. The remaining three empty-fiber types have positive residual-incidence slack and are still open. No full-model SAT/UNSAT certificate or full-colored counterexample is supplied.

E407 Q32 reserve contradictions remain conditional on V12/parent coverage. E408 Q33 minimum-support contradiction does not prove all supports enter that boundary. Existing local orientation/parity/arithmetic checks do not certify the full graph. These theorems do not close all Q32 rows; EG617(r=12) remains OPEN / NOT_CERTIFIED.

