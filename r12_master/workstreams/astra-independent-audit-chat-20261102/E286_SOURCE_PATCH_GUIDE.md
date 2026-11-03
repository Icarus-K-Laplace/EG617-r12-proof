# Withdrawn: E286 D-support source patch is not required

Date: 2026-11-03.

This file was created after a preliminary misreading of formula (5). That proposed patch is **withdrawn**.

The frozen source `r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`, Section9, already proves the pointwise clique-vertex inequality that handles all zero-missing-set cases. In support pattern D, each K10 has three support incidences, with at most one negative increment; each K11 has two incidences and the two-term shared-leaf inequality applies. Summing those pointwise charges yields formula (5) for every mixed point with positive missing sets, without requiring an additional completer of the K10.

Thus the D-case split is exhaustive as written: if one K10 has two completing mixed points, their pair costs at least7; otherwise at most one per K10 completes, so at least two of the four mixed points are noncompleting and each contributes at least5 by formula (5). The total excess would be at least10, contradicting T=8.

The separate `E286_D_SUPPORT_REPAIR.md` gives a stronger completer-existence argument, but it is redundant and should not be inserted as a required patch. No change to the frozen E286 source, SOURCE_MANIFEST, or SHA256SUMS is needed for this issue.

The correct theorem-source status is:
- ABSTRACT_286: PROVED at the analytic-reading level.
- R447_FLOOR287: PROVED from GATE47, LOW285 and EX286.
- Downstream h13 and K145 conclusions are not conditional on the withdrawn patch.

The complete explanation is in Section5 of `THEOREM_SOURCE_CROSSWALK_20261103.md`.
