# WITHDRAWN — beta-sensitive zero-excess component count

Date: 2026-10-25  
Status: **WITHDRAWN after live sibling-branch audit.** Do not use the earlier beta-dependent counts in this file.

The invalid step was treating omega(M[S]), the maximum number of S vertices that can lie in one non-target K5 component, as an upper bound on the number of distinct K5 components meeting S. It is not: two S vertices that are allowed to share a component may still lie in separate components. Thus the only universal count from |S|=3 is at least seven components avoiding S and at least six B-labelled components after allowing one pivot component.

The corrected theorem is in R12_EXACT129_ZERO_EXCESS_COMPONENT_PACKING.md. The safe consequences are at least two zero-excess B-labelled witnesses per exact-129 color (14 in E407; 16 in E408 Q33), and at least three hub-complete B-labelled witnesses per color when a full row exists. For template E with no full row, six witnesses per color hit both P3 endpoints.

The full EG617(r=12) theorem remains OPEN / NOT_CERTIFIED.
