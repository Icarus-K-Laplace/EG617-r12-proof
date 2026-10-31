# Exact shell/core incidence and full-color audit

Date: 2026-10-31. Status: **PROVED necessary identities; equality parents excluded**.

Use the parent notation of T61_PARENT_286_EDGE_LIFT.md, temporarily assuming e(H)=286. Write epsilon_v=d_H(v)-12>=0 and eta_v=d_F(v)-13>=0. The core has total epsilon 8 and at least 39 degree-12 vertices. If h_v=d_F(v,A), then

    h_v=1+eta_v-epsilon_v>=0,
    sum_H h_v=q+z,
    sum_H eta_v=q+z-39,
    sum_A eta_a=q-z,
    sum_F eta_v=2q-39=21 (E407) or 23 (E408).

Every degree-12 core vertex requires at least one shell neighbor. The 14-set {p} union A spans 91-z edges; D(14)=69 implies z>=22. Nonnegative shell decorations give z<=q. Therefore the incidence ranges are:

|Parent equality cell|z|G|b=q+z|sum_H eta|
|---|---|---|---|---|
|E407, q30|22..30|30-z|52..60|13..21|
|E408, q31|22..31|31-z|53..62|14..23|

These ranges alone are feasible scalar ledgers, not a contradiction or a graph construction. The structural E286 theorem excludes every graph completion of them.

## Original color decomposition

There are eleven non-target colors C_j on the same 61 points. Each has alpha(C_j)<=12 and omega(C_j)<=5. The retained Brouwer/Kang-Pikhurko interface gives e(C_j)>=129. Since all colors partition 1830 edges, sum_j(e(C_j)-129)=411-E: 4 for E407, 3 for E408.

For excess s<=4 the audited pointwise floors are f(0)=4, f(1)=3 and f(s>=2)=2. Exact-cell Type-I variable degrees are precisely (5,8),(6,7),(7,6),(8,5). No universal degree-nine exceptional vertex is used. The source's floor for s=1 follows by taking a non-neighborhood of a hypothetical degree <=2 vertex: at degree 2 the 58-point induced floor is 129, so the full graph has at least 131 edges. Degrees <=1 force at least 135 edges, excluding them in all current cells. Exact s=0 uses the extremal equality classification, retained as an explicit external input.

All partitions of 3 yield minimum total non-target degree 41; all partitions of 4 yield minimum 40. Thus Delta(F)<=19 for E408 and <=20 for E407. The verifier independently checks all labeled excess allocations and this arithmetic; it does not claim to reprove the extremal classification.

Consequently h_v<=7-epsilon_v in E408 and <=8-epsilon_v in E407. E408 cannot contain a core vertex of epsilon 8. In E407 such a vertex has d_H=d_F=20, no shell neighbors, eta=7, and all other core vertices have degree 12. This exactly matches the Cell B interface below and is excluded by E286. The other excess distributions and all shell patterns are also excluded by that theorem, so no separate unproved shell-capacity assertion is needed.

Source: front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md at frozen global b0459807; see SOURCE_DEPENDENCIES.json. The source's overly compressed 24-point pair-count assertion is not used: the triple file uses the accepted R(2,24) exclusion explicitly.
