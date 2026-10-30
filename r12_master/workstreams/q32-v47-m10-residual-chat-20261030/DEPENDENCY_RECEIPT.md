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
