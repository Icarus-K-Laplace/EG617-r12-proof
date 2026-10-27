# E407 Q32 — low-delta terminal table

Date: 2026-10-27  
Status: **Current audited frontier. No new low-delta closure is claimed by the latest exact-color results.**

Let L_U=bar(H[U]), delta=e(L_U)-294, and epsilon_U=sum_{u in U}(d_H(u)-12). The exact ledger is

\[
e(H[U])=112-\delta,\qquad
e(H[W])=48-\epsilon_U-\delta,\qquad
e_H(U,W)=124+\epsilon_U+2\delta.
\]

Retained inequalities:
\[
3\le\delta\le16,\qquad 0\le\epsilon_U\le4,\qquad
\delta+\epsilon_U\le16,\qquad
\epsilon_U+2\delta\ge9.
\]
Every feasible row has alpha(H[W])=4.

## Exact feasible epsilon_U values

| delta | epsilon_U |
|---:|---|
| 3 | 3,4 |
| 4 | 1,2,3,4 |
| 5–12 | 0,1,2,3,4 |
| 13 | 0,1,2,3 |
| 14 | 0,1,2 |
| 15 | 0,1 |
| 16 | 0 |

There are 56 integer profiles. The checked-in arithmetic verifier records the exact edge counts for every pair.

## Current mathematical status

| Branch | Status | Dependency / remaining issue |
|---|---|---|
| delta=16 | EXCLUDED | four-partite endpoint/kernel analysis and forbidden K12 |
| delta=15, four-partite | EXCLUDED | W-profile saturation / endpoint argument |
| delta=15, non-four-partite | EXCLUDED UNDER REGISTERED KP CONTRACT | second-Turan equality reduction |
| delta=14, four-partite, epsilon_U=0,1,2 | EXCLUDED | exact profile closures; some classification steps use Brouwer/Turan equality |
| delta=14, non-four-partite, augmentable | EXCLUDED UNDER REGISTERED EXTREMAL CONTRACT | augmentable-edge reduction |
| delta=14, non-four-partite, K5-saturated | PROVED_CONDITIONAL | alpha-critical reduction depends on unaudited Didin 2026 preprint theorem |
| delta=13, four-partite, epsilon_U=1 | EXCLUDED | no-cross and all recorded cross-edge profiles, including Round 31 |
| delta=13, four-partite, epsilon_U=2 | EXCLUDED under stated profile contract | no-cross plus (4,4,5,5)+one-cross-edge closure |
| delta=13, four-partite, epsilon_U=3 | EXCLUDED | exact 32-edge W profile / no-cross closure |
| delta=13, four-partite, epsilon_U=0 | OPEN | W edge count 35; no exhaustive terminal classification |
| delta=13, non-four-partite | OPEN | no complete classification at e(L_U)=307 |
| delta<=12 | OPEN | no legal extrapolation from delta=13 classifications |

## Minimum-slack subfrontier

The minimum value epsilon_U+2delta=9 occurs at (delta,epsilon_U)=(3,3) and (4,1). The W-side total slack is seven.

If an independent W-four-set has total slack one, the current exact-core theorem forces U to be exactly four-partite with parts (7,7,7,8), with three target K7 parts and an R=K8 part. The two profiles are then reduced to the finite omission/class-size kernels recorded in `MINIMUM_SLACK_EXACT_CORE.md`.

The complementary branch — every independent W-four-set has total slack at least two — remains OPEN.

## Interaction with the new exact-color theorems

`SELECTED_B_ANCHOR_FLOOR.md` and `SHELL_COLOR_EDGE_LOAD.md` hold uniformly across every feasible delta row under the labelled exact-129 factor contract. They do not by themselves delete any row of this table. Their value is to strengthen the global shell/support join that must be imposed on every surviving low-delta core.

No local profile exclusion is promoted to an E407 shell-template closure without the global labelled compatibility theorem.
