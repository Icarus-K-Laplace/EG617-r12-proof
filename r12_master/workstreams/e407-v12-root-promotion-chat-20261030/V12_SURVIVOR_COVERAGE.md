# V12 survivor coverage and five-template mapping

Date: 2026-10-30

The archive screen leaves 554 OPEN labelled necessary shells. The independent verifier checks every survivor, not a sample.

## Unique survivor assignment

| Template | Survivors | Kernel composition | Candidate incidences (not survivor count) |
|---|---:|---|---:|
| A | 30 | I3 30 | 237 |
| B | 54 | I3 54 | 342 |
| C | 24 | W7_separate 24 | 184 |
| D | 226 | W6_different 142, W7_separate 84 | 1009 |
| E | 220 | W7_separate 98, W8 122 | 1190 |
| **TOTAL** | **554** | | **2962** |

Each of the 554 survivors has exactly one template label. A survivor may have multiple regular degree-3/rho-zero candidate vertices; the last column counts those candidate incidences and must not be confused with the number of survivors.

## Full row checks

For every regular degree-3/rho-zero candidate y in every OPEN survivor, the verifier checks:
1. the three-point missing neighborhood S has the exact induced graph and weight profile for A, B, C, D, or E;
2. W=A\\S has exactly ten vertices, all regular;
3. W is missing-independent;
4. every w in W has its missing neighborhood inside S in the exact allowed row family for that template;
5. the template row-count inequality in Q32_KERNEL_COVERAGE.md is satisfied.

All candidate row checks passed: **0 failures**.
All 554 survivors have one unique template label: **554/554**.
The independently recomputed screen rule agrees with every archive screen record: **0 mismatches**.

## Scope boundary

This closes the finite mapping edge from V12 OPEN survivors to the five necessary templates. It does not prove simultaneous 47-core completion impossible. The V12 archive itself labels C8 (the simultaneous labelled 47-core completion implication) OPEN and reports zero completed parent graphs. The U-reserve crosscut can eliminate these templates only if the separate 29-point/49-block support contract applies to every legal completion.

The lossless per-survivor assignment is stored as inclusive index ranges in `V12_SURVIVOR_TEMPLATE_RANGES.json`; its counts sum to 554.
