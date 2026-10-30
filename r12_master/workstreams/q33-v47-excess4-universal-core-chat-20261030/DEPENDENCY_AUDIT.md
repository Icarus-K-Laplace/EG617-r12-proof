# Independent Q33 284-edge theorem — dependency audit (updated 2026-10-30)

| Item | Required input | Status | Notes |
|---|---|---|---|
| D1 | 47 vertices, 284 edges, delta>=12, alpha<=4, omega<=11, all inherited D-caps | **PROVED** as an explicit core theorem contract | Parent derivation is in Q33_PARENT_PROMOTION_RECEIPT.md. |
| D2 | Total degree excess equals four | **PROVED** | 2*284-47*12=4. |
| D3 | Independent four-set among degree-12 vertices | **PROVED** | At least 43 regular vertices; greedy alpha bound ceil(43/13)=4. Original Turan table also replayed. |
| D4 | Four private cliques and Z support range 3..5 | **PROVED** | Exact incidence surplus five. |
| D5 | R(2,24) empty | **PROVED** | D(24)=144, 12-regularity, complement shortest-odd-cycle contradiction. |
| D6 | Common-neighbour bound and K10 completion capacity | **PROVED** | Improved bound c<=2+epsilon(u)+epsilon(v); no Kang–Pikhurko input required. |
| D7 | K11-K11 pair spends at least six excess units | **PROVED** | Exact integer minimum six at (2,2). |
| D8 | All h=3,4,5 support templates excluded | **PROVED** | Includes P/D mixed-support matrices and pointwise D incidence accounting. |
| D9 | Support multiset, matrix classes and integer minima replay | **PROVED** | Separate standard-library replay passes; it checks arithmetic only. |
| D10 | 127-row rational certificate for the separate 284-edge floor lemma | **PROVED** | Original Fraction verifier passes 127 rows; not a dependency of the 284-edge nonexistence theorem itself. |
| D11 | V11 retained minimum-degree declaration | **OPEN; NOT A DEPENDENCY** | The Q33 application now obtains delta(H)>=12 from the hereditary-cap minimum-degree theorem. |
| D12 | Full EG617(r=12) theorem | **OPEN** | Other root branches remain unresolved. |

## External theorem audit

The old COMMON_NEIGHBOR_CAPACITY.md used Kang–Pikhurko Theorem 1 at n=25,r=2. That application was numerically within the theorem's stated regime, but it is unnecessary. The source-complete replacement uses the independently proved R(2,24)=empty result and strengthens the common-neighbour cap from 3+epsilon(u)+epsilon(v) to 2+epsilon(u)+epsilon(v).

The independent-four-set lemma can be proved by the greedy bound ceil(43/13)=4; the former Turan table is retained as an arithmetic cross-check. The R(3,35) seed uses the elementary shortest-odd-cycle bound and Mantel's inequality, with Mantel's proof included in the seed audit. No non-elementary extremal theorem is load-bearing in the Q33 284-core proof after the replacement.

## Explicit non-dependencies

- Q32's 285-edge/excess-six theorem;
- V11's retained Q31/Q32/Q33 minimum-degree declaration;
- any selected 31-point / 56-witness reserve;
- any SAT/UNSAT solver result or random-search failure;
- the E334/H35 high-layer V8 package;
- the BACKEND49 49-point theorem;
- Kang–Pikhurko after the source-complete common-neighbour replacement.

The FRONTEND_LINE_A V1 archive is used only as a source container for the explicit hereditary-cap seed and the separate 127-row core-floor certificate. The lower-degree theorem is independently proved in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md.