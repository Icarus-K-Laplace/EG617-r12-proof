# R0 Tracker

This tracker distinguishes numerical threshold improvement from hypothesis weakening.

## Current records

| version | theorem | hypotheses | r0 | controlling inequality | status |
|---|---|---|---:|---|---|
| v0 | no synthesized infinite-family theorem | — | infinity | missing synthesis | superseded |
| v1 | `P(r)` | original A+B+C*+D | 12 | `4(r-3)>3r-1` | CONDITIONAL_ON_ABCD |
| v2 | `P(r)` | original A+C*+D | 68 | AES threshold | CONDITIONAL + ASYMPTOTIC_ANALYTIC |
| v3 | `P(r)` | **A_ext+C*+D** | **68** | AES threshold | **current strongest minimal-hypothesis synthesis** |

Here `A_ext` only asks the front end to force an induced legal `4r+1` residual or a controlled `5r+1` design terminal. The complete residual pivot/core contract is now derived analytically for every r>=17.

Thus v2 -> v3 does **not** reduce numeric r0, but removes a load-bearing hypothesis.

## Threshold decomposition

Let the still-open upstream extraction, endpoint closure, and design stability eventually be proved above thresholds `R_ext`, `R_C`, `R_D`. The current composition gives

> **`r0=max(68,R_ext,R_C,R_D)`.**

The extracted-residual contract has its own proved threshold 17, which is already dominated by 68.

## What controls 68

Only

`2r-9 > 5(3r-1)/8`,

that is `r>67`, from the exact-three-anchor complement/AES argument.

The residual-contract theorem needs only r>=17. Medium-degree collapse needs only r>=12 once K>=8.

## Medium-degree threshold from a generic K-floor

From

`q+epsilon=3r+3-K/2`

and medium base `4r-12`, worst-case epsilon=0 gives:

| K floor | first r excluding every medium d |
|---:|---:|
| 2 | 15 |
| 4 | 14 |
| 6 | 13 |
| 8 | 12 |

## Fixed-deficit d3 threshold

The multicolour slope contradiction gives

`r > 11+epsilon sqrt(4epsilon+1)`.

This is useful as an independent asymptotic window, although the sibling common-S d3 endpoint is already closed under the stronger residual/anchor setup.

## Current numeric report

- minimal r0 with original H_B assumed: **12**;
- minimal r0 with H_B eliminated and residual contract derived: **68**;
- unconditional Problem 617 r0: **not yet finite/proved**, because extraction A_ext, endpoint C*, and design stability D remain open.

## Next threshold opportunities

1. lower three-anchor 68;
2. prove A_ext at any finite threshold (anything <=68 is numerically free at current synthesis level);
3. prove C* at any finite threshold;
4. prove D at any finite threshold.

A huge threshold in C* or D is acceptable initially; it would still create the first true infinite-family theorem once all three open components have finite thresholds.
