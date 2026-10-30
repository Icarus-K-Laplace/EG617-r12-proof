# Q33 284-edge theorem — dependency audit (source-complete update)

Date: 2026-10-30

| ID | Statement | Status | Exact dependency boundary |
|---|---|---|---|
| D1 | No 47-vertex graph with e=284, delta>=12, alpha<=4, omega<=11 | **PROVED** | Universal analytic proof in Q33_UNIVERSAL_284_NONEXISTENCE.md; no density cap required |
| D2 | Total degree excess is four | **PROVED** | Handshake: 2*284-47*12=4 |
| D3 | Independent four-set of degree-12 vertices exists | **PROVED** | At least43 regular vertices; greedy degree-12 independent-set bound |
| D4 | Four private cliques and exact Z support incidence | **PROVED** | alpha<=4, omega<=11, four-set degrees exactly12 |
| D5 | K11-K11 2-support costs at least six excess | **PROVED** | Independent-five blocker and disjoint vertex charge |
| D6 | All h=3,4,5 support templates excluded | **PROVED** | h=4 pointwise K10 charge; h=5 P/D mixed matrices and pointwise no-double-count proof |
| D7 | Universal common-neighbour bound c<=3+epsilon(u)+epsilon(v) | **PROVED** | Shortest odd cycle plus Mantel on a 25-set; five graph hypotheses only |
| D8 | At most one external vertex completes a K10 | **PROVED** | K12 if adjacent; otherwise at least10 common neighbours contradict D7 and total excess4 |
| D9 | Minimum-degree source gate J in R(4,47), e<=286 => delta>=12 | **PROVED** | Inherited D-caps plus R(2,24), R(3,35), R(3,36), R(3,37) seed chain |
| D10 | R(3,35) seed delta>=12 and e>=210 | **PROVED** | Full 121/122 neighbourhood classification and D(14),D(23) contradiction |
| D11 | R(3,36) delta>=13/e>=234; R(3,37) empty | **PROVED** | Induced-subgraph transport from D10 and R(2,24) |
| D12 | Degree10 in R(4,47) forces e>=289 | **PROVED** | Exact ten-neighbour degree-sum; does not assume N(v) is a clique |
| D13 | Degree11 in R(4,47) forces e>=287 | **PROVED** | 35-core floor210, missing shell edge, common row union>=12, shell charge>=11 |
| D14 | Every R(4,47) graph has e>=284 | **PROVED** | D9 plus the private-clique lemma for total excess<=2 |
| D15 | 127-row rational certificate | **COMPUTATION_CERTIFIED** | Both original verifiers rerun from extracted archive: 32+95 rows; maxima 773/1089 and39/44; see CLEAN_ROOM_REPLAY_20261030.md |
| D16 | E408 / Qmax=33 parent contradiction | **PROVED_CONDITIONAL** | E408 h13 parent contract, exact q=33 pivot, inherited density caps; no V11 dependency |
| D17 | V11 retained minimum-degree declaration | **OPEN / NOT USED** | Its broader analytic package remains separate and is not a premise here |
| D18 | Strict 285-edge floor for R(4,47) | **PROVED** | 284-edge private-clique floor + e<=286 minimum-degree gate + universal 284-edge nonexistence; see R447_STRICT_285_FLOOR.md |
| D19 | E408/h13 every degree-13 pivot has q_p<=32; Q_max<=32 | **PROVED_CONDITIONAL** | Exact E408 pivot identity and induced R(4,47) contract; no V11 or support-promotion dependency |
| D20 | Full EG617(r=12) theorem | **OPEN** | E408 Q32, E407 Q32 and original front-end parent coverage remain live |

## External theorem audit

No Kang–Pikhurko theorem is used in D1–D16. The previous common-neighbour argument's 2+epsilon bound was cap-dependent; it is not used by the universal core theorem. The source-complete replacement proves the weaker but sufficient 3+epsilon bound using only alpha<=4, omega<=11 and total excess4.

Mantel's inequality is proved by the edge-degree/Cauchy argument in the source audit. No unproved Ramsey number is used. The 121/122 triangle-free neighbourhood classification is reproduced in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md with its exact five-cycle type cases.

## Exact finite replay

The actual clean-room execution and archive/source SHA256 checks are recorded in CLEAN_ROOM_REPLAY_20261030.md. The 127-row certificate is not a dependency of the minimum-degree implication D9; it belongs to the separate total-excess<=2 core-floor lemma.

- Q33_SOURCE_COMPLETE_REPLAY.py checks density-cap arithmetic, shortest-cycle bounds, the 121/122 extension costs, degree10/11 inequalities, support-multiset counts, matrix classes, and the exact minima 6,6,4,5.
- With --certificate it checks all127 rational rows using Fraction arithmetic.
- The original verify_completion.py was run from both identical retained archive paths. Both reported EXACT_CERTIFICATE_VERIFIED, rows=127.
- The independent Q33 finite support verifier checks only arithmetic/support-shape facts. It does not replace the analytic proof.

## Explicit non-dependencies

- Q32's 285-edge/excess-six core theorem;
- V11's retained minimum-degree declaration or its kernel-completion claims;
- a universal Type-I assumption;
- a K6-free or omega(H)<=5 condition;
- a degree-nine exceptional-vertex premise;
- any SAT/ILP UNSAT output or random-search failure;
- BACKEND49_FIRST_PRINCIPLES_AUDIT_V1;
- HIGH_LAYER_BACKEND_V8;
- Kang–Pikhurko after the elementary common-neighbour replacement.

## Parent promotion boundary

The strict 285-edge floor upgrades the E408/h13 pivot bound to Q_max<=32 under the exact T61 parent contract. It does not close E408 Q31 or Q32, does not close E407 Q32, and does not prove EG617(r=12) globally.