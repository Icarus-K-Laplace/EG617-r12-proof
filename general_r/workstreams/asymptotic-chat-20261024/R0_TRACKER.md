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


## v4 — S67-low near-anchor route (2026-10-24)

| version | theorem | hypotheses | r0 | controlling threshold | status |
|---|---|---|---:|---|---|
| v4 | P(r) | A_ext* + D_low | 67 | direct near-anchor extraction inside the 5r+1 terminal | CONDITIONAL_ON_Aext_Dlow |

This is a **different route**, not a numeric improvement of the same hypothesis set as S68-v2. It replaces the broad C*+D endpoint assumptions with the narrower D_low near-anchor terminal contract and bypasses the exact three-anchor hypothesis H_B.

Threshold accounting:
- residual 4r+1 branch: impossible once r ≥ 17, with contextual cap gap (3r−13)/2;
- 5r+1 terminal direct near-anchor extraction: r ≥ 67, relative to Liu–Ren–Wang 2025 (classical AES fallback r ≥ 71);
- high-degree top layer |W|=2r−1: Cell B excluded for r ≥ 16, Cell A for r ≥ 25;
- low-degree top layer delta=r, |W|=2r−1: now PROVED impossible for r≥25 by LOW_DEGREE_TOP_LAYER_CLOSURE.md; remaining offsets stop at 2r−2.

Thus the shortest conditional numeric threshold is now **67**. The unconditional Problem-617 threshold remains **NOT CERTIFIED** because A_ext* and D_low are open.

The d2 scalar inequality audit is also frozen: the family K=r−2, a=2, b=0, epsilon=0, B=r/2+4, q=5r/2+4 is consistent with all currently recorded scalar bounds and has K+a=r. It is not a legal graph counterexample, but no scalar-only proof of a strict sub-r margin can be valid.


## v5 — forced-hub low-offset reduction (2026-10-24)

- Bounded-W-incidence conditional: if d_F(o,W)<=B for all outside vertices, D_low follows for r>=7+4B. Status: PROVED_CONDITIONAL.
- Unconditional structural consequence: every surviving low-offset terminal has max_o d_F(o,W)>=floor((r-j)/4)+1. Status: PROVED_ANALYTIC.
- D_low and A_ext* remain OPEN; unconditional Problem 617 r0 remains NOT CERTIFIED.
- If B=6 were established, the conditional D_low threshold would be r>=31, below the existing S67-low threshold, but B=6 has not been proved for the lower offsets.
- The inequality 2r-9 > 5(3r-1)/8 has exact integer threshold r>=68. It controls the separate K>=8 route, not S67-low.
