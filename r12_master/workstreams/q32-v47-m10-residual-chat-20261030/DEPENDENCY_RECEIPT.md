# M10 workstream dependency receipt

## Repository isolation

Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-q32-v47-m10-residual-final-20261030  
Write directory: r12_master/workstreams/q32-v47-m10-residual-chat-20261030/  
Base commit: 1de8a37556ba98ccbb8651f39a5192629453f0f1  
Base branch: workstream/r12-q32-highsupport-root-20261028.

The requested target branch did not exist before this workstream was created. The target directory did not exist on the high-support or Astra branches before creation. All new files are restricted to the directory above.

## Read-only sibling references

High-support branch:
- branch: workstream/r12-q32-highsupport-root-20261028
- head: 1de8a37556ba98ccbb8651f39a5192629453f0f1
- ROOT_DEPENDENCY_DAG.md blob: 37a1dd404a179fe8a97fea1ce572dccf48fef36a
- HIGH_SUPPORT_NEAR_TURAN.md blob: 5dc6e156939b73e909b707a6cb41e540c3d8d657
- V47_LIGHT_BLOCK_GRAPH_DISCONNECTED_REDUCTION.md blob: f2927997d7c08dc8bf559f72ebb814f3c7a9f36b
- V47_37_OUTER_LIGHT_HOLONOMY.md blob: e8ec69f4d50e0124a48e050f5322231d9d7e88b0
- V47_RESIDUAL_INCIDENCE_COVER.md blob: d3877e61f85c26d39178f22635508ea619200608
- V47_Z01_EXACT_COLOR_RESIDUAL_GRAPH_CATALOG.md blob: 50603482f006917d4ea711c2851ae5acb01c3872
- V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md blob: 699f478fe7f295dffa6ba5f2bef2a8063919eab6
- V47_Z01_TWO_DOUBLE_SOURCE_PATTERN_AUDIT.md blob: 4984ae121f1edf09b68a2fc3c18e2bef352c0d7e
- Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md blob: 25714d9f9af244aa1af7eb4392cdea5e82b8220c
- KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md blob: b1f870023990561c563a969f6f180eb3ebc6f9af

Case-II v44 branch:
- branch: workstream/r12-q32-caseII-v44-final-20261028
- head: 9afd7c1a59056052974f9dc78933010d10e88bba
- V45_SOURCE_CORRECT_CLOSURE.md blob: c17acc7171e55246fa67226421c17ced5b8556f7
- V46_SOURCE_CORRECT_CLOSURE.md blob: a26ac7681f2613d940a7f6bf4c5408bb79a0e003
- DEPENDENCY_AUDIT.md blob: 2adcded87ae5918eac73d29b9b443e2664887313

Astra independent branch:
- actual branch: workstream/r12-astra-independent-structural-attack-20261029
- head: 99f60126fdd9c72c450475e7fd75c6c499d69df7
- source_manifest.json blob: 0594fca6f603b8d2ff9c923d864e85ee3993f2fa
- residual_types.json blob: 6b618972b73fcfc0c15abd495482c1a6ff7c5fd7
- verification_log.txt blob: 8896c97792c606122d37bd479eb55233dc98cd4a
- structural commits: d1f05a51c5f7c09e3c3e0a50db07fecdc0321739 and 99f60126fdd9c72c450475e7fd75c6c499d69df7.

## Scope of imported conclusions

- The source-correct Type-I factorization and its outside-count profiles are imported from the Kang–Pikhurko source audit and the full-support vertex-labelled CSP formulation.
- The disconnected light-component theorem is imported from the high-support branch.
- The Astra theorem is imported only as a conditional exclusion of the exact 3+7 five-property normal form.
- The aligned z=0,1 K6 result and the isolated-double audit are not generalized beyond their registered source/track contracts.
- The case-II v44/v45/v46 results concern lower support and do not close |U|=47.

No sibling branch or sibling directory was modified by this workstream.


## Additional m10 artifacts (commit be0dfe8d637bbac2e505e208249974ccb043433d)
- M10_555_TRIANGLE_AND_CROSS_GRID_SWITCH_LEMMA.md
- verify_m10_555_triangle.py
- verify_m10_555_column_states.py
- M10_SOURCE_OCCUPANCY_90.csv
- verify_m10_source_occupancy.py

SUPERSEDED: the former 5,5,5/one-column artifacts reported 1,872 and 20,788/16 states. The corrected verifier and count are recorded in the correction section below. Neither version covers the six-column cross grid or full Q32.


## Correction — 5,5,5 theorem and one-column catalog

The former 1,872-count 5,5,5 classification and 20,788-state one-column catalog are retracted. Corrected artifacts:
- M10_555_CLASSIFICATION_RETRACTION.md
- M10_555_TRIANGLE_AND_CROSS_GRID_SWITCH_LEMMA.md
- verify_m10_555_triangle.py
- verify_m10_555_column_states.py

Exact replay: 41,472 5,5,5 inputs, 2,124 valid (1,728 identity; 66 per transposition); corrected one-column catalog 20,842 (20,772 aligned, 70 switched). Six-column compatibility remains OPEN.


## Z=4 two-aligned pattern-10 closure (commit f30ccce5f7faa2c07498709dfbf808a74937f1cd)
- M10_Z4_TWO_ALIGNED_PATTERN10_EXCLUSION.md
- verify_m10_z4_two_aligned_cut.py

The proof excludes only the exact two-aligned/four-A-only-switched matching pattern under F=(3,2,2,0). It does not promote the entire 4+6 cell.


## 6. General 4+6 K4-e, Z=4 global closure — 2026-10-30

New theorem: M10_K4E_Z4_GLOBAL_GRID_CLOSURE.md  
Independent local verifier: verify_m10_k4e_z4_grid_reduction.py  
Commit: 5b96f62a59eda62471ee35aa7c1fa1bf40965a55

### Imported mathematical inputs

1. The exact 4+6 scalar ledger, K4-e small-side reduction, outer heavy matching, and pointwise degree equations are in M10_DENSE_COMPONENT_CORE_LEMMA.md.
2. The two-light matching-composition theorem is imported read-only from high-support branch workstream/r12-q32-highsupport-root-20261028, file V47_TWO_LIGHT_MATCHING_COMPOSITION.md, blob a1cff87818214a0f60872da132a559b4f778e36d.
3. The zero-slack residual-map alignment lemma is also recorded read-only in that high-support branch, file V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md, blob 483c0e699cd91769994f58abb64fb66c30af9d7b.
4. The corrected 4,5,5 switch theorem and corrected 5,5,5 classifier are in M10_555_TRIANGLE_AND_CROSS_GRID_SWITCH_LEMMA.md. The former fixed-transposition 5,5,5 classifier remains retracted and is not used.
5. The parent clique cap omega(H)<=11 is an inherited input, not a consequence of the 285-edge core alone: the 61-point T61 residual has omega<=11 in the root promotion audit, and H is its induced 47-vertex core. The proof uses this only for the final K12 contradictions.

### Exact scope

Closed: the entire disconnected 4+6, K4-e, Z=4 slice, across both residual graphs C7 and C3 dot-union C4, all residual clique-fiber maps, and all six-column cross matching/extra-edge grids.

Still OPEN: the K4 small-component branch; K4-e with Z=1,2,3; other component sizes; connected L; full-support m=10 Q32 overall; EG617(r=12).

### Verification boundary

The verifier checks the pair/triple necessary local cell catalog, the 930 outer-light cut shapes, and the normalized corrected-5,5,5 endpoint branch used in the proof. It is not a full 4-by-6 SAT solver and not a 47-vertex Q32 SAT/UNSAT certificate. The global grid contradiction is analytic in the theorem file.


Clarification update: the theorem text's matching-holonomy and row-switch endpoint derivations were made explicit in commit b2920dad7f5f8b7f3d61d43af8ac80edf2517664. Current workstream head after this correction is recorded by the branch ref; full-support m=10 Q32 remains OPEN / NOT_CERTIFIED.


## 7. Exact verifier execution and final artifact identities

The committed verifier source was fetched and executed independently; all assertions passed. Verifier blob SHA: e9f186db5a66d10b4f8c664fe6b30fe974e50288.

The global theorem file was clarified after its initial publication to spell out triangle-generated matching holonomy and the row-switch endpoint formula. Its current blob is de1c9378d4c477f5ca5c7fd04d4dc96fbaeebfb9. The workstream branch also contains the status-note reconciliation that identifies the K4-e, Z=4 slice as closed while retaining full-support m=10 Q32 as OPEN / NOT_CERTIFIED.


Proof simplification receipt: the A/B switch contradiction in Section 7.2 was reduced to two 4,5,5 consequences and the outer cap c_j(k')<=1. The corrected 5,5,5 theorem remains load-bearing only for rowwise identity/transposition compatibility; its six-case endpoint replay is an additional regression.
