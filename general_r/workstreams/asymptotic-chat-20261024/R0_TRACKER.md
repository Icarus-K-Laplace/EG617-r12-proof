# R0 Tracker

This tracker distinguishes numerical threshold improvement from hypothesis weakening. A smaller r0 with more assumptions is not automatically a stronger theorem.

## Current records

| version | theorem | hypotheses | r0 | controlling inequality | status |
|---|---|---|---:|---|---|
| v0 | no synthesized infinite-family theorem | — | infinity | missing synthesis | superseded |
| v1 | `P(r)` | A+B+C*+D | 12 | `4(r-3)>3r-1` | CONDITIONAL_ON_ABCD |
| v2 | `P(r)` | A+C*+D | **68** | `2r-9>5(3r-1)/8` | CONDITIONAL_ON_ACD + ASYMPTOTIC_ANALYTIC |

Interpretation:

- v1 has the smaller numeric threshold but assumes H_B.
- v2 is the current **minimal-hypothesis asymptotic synthesis record** because H_B is derived rather than assumed.
- Relative to the pre-synthesis state, a finite H_B-free threshold has improved from `infinity` to `68`.

## Threshold decomposition

For a theorem in which the sibling hypotheses themselves have validity thresholds `R_A`, `R_C`, `R_D`, the current composition gives

> **`r0 = max(68, R_A, R_C, R_D)`.**

The pointwise theorem in `SUFFICIENTLY_LARGE_R_THEOREM.md` avoids pretending that unknown sibling thresholds are already proved.

If exact three-anchor improves to threshold `R_B<68`, the analytic composition becomes

`r0=max(13,R_B,R_A,R_C,R_D)`

for the general near-anchor reduction; if the exact theorem is proved all the way to r=12 and the existing r=12 near-anchor closure is imported, then the anchor contribution becomes 12.

## Medium-degree threshold as a function of K-floor

Using

`q+epsilon=3r+3-K/2`,

and comparing with the medium base `4r-12`, the worst-case (`epsilon=0`) endpoint-collapse thresholds are:

| K floor | endpoint-collapse r0 |
|---:|---:|
| 2 | 15 |
| 4 | 14 |
| 6 | 13 |
| 8 | 12 |

This table is useful if the anchor theorem is weakened or bypassed.

## Fixed-deficit d3 threshold

At residual deficit epsilon, the multicolour slope contradiction gives

> `r > 11 + epsilon sqrt(4epsilon+1)`.

For fixed epsilon define

`R_d3(epsilon)=floor(11+epsilon sqrt(4epsilon+1))+1`.

Examples:

- epsilon=0: r>=12;
- epsilon=1: r>=15;
- epsilon=2: r>=18;
- epsilon=3: r>=23.

(The sibling repivot closure is stronger for the common-S d3 endpoint under A+B and does not require restricting to this fixed-deficit threshold.)

## Next r0-reduction opportunities

1. **Three-anchor:** lower 68. Every improvement here lowers the H_B-free synthesis threshold until another sibling threshold dominates.
2. **Front extraction:** any finite theorem is acceptable initially; a threshold below 68 is effectively free at the current synthesis level.
3. **Design terminal:** any finite robust-stability threshold can be inserted by taking a maximum.
4. **Backend d2:** an all-large-r d2 slope contradiction need not be sharp; even r>=10^4 would immediately create a valid finite C* threshold and therefore a first true residual infinite-family theorem once A is available.

## Current numeric report

- minimum r0 with H_B assumed: **12**;
- minimum r0 with H_B eliminated analytically: **68**;
- unconditional Problem 617 r0: **not yet finite/proved**, because A, C*, D remain open.
