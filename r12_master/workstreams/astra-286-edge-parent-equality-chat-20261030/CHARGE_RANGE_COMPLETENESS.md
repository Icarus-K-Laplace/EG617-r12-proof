# Charge coverage: direct bounds versus retained source coverage

Date: 2026-10-31. Status: **direct upper range PROVED; independent full lower-charge coverage OPEN**.

## Bounds that do not assume a maximum pivot

For every degree-13 pivot, D14 yields q>=z>=22. The new floor 287 gives q<=29 for E407 and q<=30 for E408. Hence Q=max q_p lies in 22..29 or 22..30 respectively. These are exhaustive necessary intervals, not claims of realization. No nonmaximum pivot is discarded: the same interval holds pointwise. Existence of a regular pivot follows from delta(F)=13.

## What the source texts actually establish and what is retained

|Source read at frozen revision|Content relevant to coverage|Limit in this audit|
|---|---|---|
|T61_H13_LOW_LAYER.md and V7_RESULT.md|Low-charge promotion and q30 plateau promotion are reported; V7 promotes q25/26 to >=27 and q30 to >=31 within its hypotheses.|Original complete low-range classification/package proof is not reproduced in these repository summaries.|
|V8_RESULT.md|For Q=30+k, k=1..3, a regular missing-degree-3 neighbor has rho<=k-1.|This is a conditional high-Q theorem, not Q>=31. The source itself says low maxima remain obligations.|
|V9_CANONICAL_AUDIT.md|Under R(2,24) empty, R(2,23) floor131 and R(3,35) minimum degree12/floor211, excludes Q27 both energies and Q28 E408; states remaining frontier {31,32}/{31,32,33}.|The audit records 19 q28 types and package replay; their full source certificates and earlier promotion coverage were not re-executed here. Treat the asserted exact frontier as a retained theorem, not as a newly proved lower bound.|
|V10_CANONICAL_AUDIT.md|At Q31 excludes regular shell missing degrees 3 and 10; keeps {0,1,2,11,12}. Gives a shell-only witness.|Does not prove Q>=31 or parent completion; new core floor excludes the witness completion directly.|
|V11_SOURCE_AUDIT.md and global V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md|Q31 finite coverage, including nine degree-two rows and capacity 7>alpha(F)=5, is recorded with retained seed dependencies.|High-Q elimination does not fill low-Q coverage. Original archives are not replayed in this workstream.|
|V12_SURVIVOR_COVERAGE.md and V12_GENERAL_SUPPORT_RESERVE.md on V12 branch|554 survivors map to A--E; support reserve excludes union sizes29..33, leaves34 and larger unresolved without further bridge.|No Q lower bound. MS-29 is not proved by the shell enumeration; it is unnecessary for our replacement E407/q32 exclusion.|

The files actually read and their blob IDs are recorded in SOURCE_DEPENDENCIES.json. No ZIP was found by a local recursive ZIP-name search of the attachments directory; no Library tool is exposed in this session. Repository reports of previous independent replay are accurately attributed to those reports.

## Complete honest status over the direct remaining intervals

|Energy|Q values|This workstream's status|
|---|---|---|
|E407|22,23,24,25,26|Not independently excluded here; require complete historical low-range/promotion proof.|
|E407|27|Excluded relative to the retained V9 seed/classification theorem.|
|E407|28,29|Require historical full-frontier/promotion coverage; no lower-bound inference from E286.|
|E407|>=30|Excluded directly by the new core floor.|
|E408|22,23,24,25,26|Not independently excluded here; require complete historical low-range/promotion proof.|
|E408|27,28|Excluded relative to the retained V9 seed/classification theorem.|
|E408|29,30|Require historical plateau/promotion coverage; q30 would be e(H)=287, not a 286-edge contradiction.|
|E408|>=31|Excluded directly by the new core floor.|

## Conditional shortest full-energy closure

Define COVER as the retained theorem that every genuine h13 parent in these energies has E407 Q in {31,32} or E408 Q in {31,32,33}, with all its historical seed/classification/promotion hypotheses. Under COVER, both energy layers are CLOSED: the new upper bounds 29 and 30 contradict every allowed value. This is a valid PROVED_CONDITIONAL consequence, with COVER explicitly exposed. It is not an independent certification of COVER or the whole EG617 root.

## Repivot and other interfaces

The exact signed identity is q_y-q_p=h-eta+kappa-m. Around a closed legal walk it gives sum(h+kappa)=sum(eta+m), not vanishing of each correction. The retracted zero-defect-cycle shortcut is not used. A maximizing pivot can have neighbors of smaller charge; the pointwise core floor remains valid on all of them.

h12 has a 48-point core and a distinct shell identity and source dependency chain (T61_H12_CLOSURE.md). Nothing in the 47-point theorem substitutes for that chain. Source closures for energies397..406 remain their existing theorems; E406/S31 supplies an upper-charge pivot interface for E406 only and no E407/E408 lower bound. Energies outside407/408 and the global balanced-coloring reduction require their original contracts. No root file or sibling status is changed.
