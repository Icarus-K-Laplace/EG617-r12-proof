# E407 Q32 — low-delta terminal table

Date: 2026-10-28  
Status: **Current audited frontier. E407 Q32 remains OPEN / NOT_CERTIFIED.**

Let
\[
L_U=\overline{H[U]},\quad \delta=e(L_U)-294,\quad
\epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
The exact ledger is
\[
e(H[U])=112-\delta,\qquad
e(H[W])=48-\epsilon_U-\delta,\qquad
e_H(U,W)=124+\epsilon_U+2\delta.
\]
Retained inequalities:
\[
3\le\delta\le16,\quad0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad\epsilon_U+2\delta\ge9.
\]
Every feasible profile has alpha(H[W])=4.

## Current mathematical status

| Branch | Status | Dependency / remaining issue |
|---|---|---|
| delta=16 | EXCLUDED | registered endpoint/kernel proof |
| delta=15 | EXCLUDED under registered contracts | four-partite + non-four-partite closures |
| delta=14 four-partite | EXCLUDED | exact profile closures |
| delta=14 saturated non-four-partite | PROVED_CONDITIONAL | Didin 2026 dependency not independently discharged |
| delta=13 | PROVED_CONDITIONAL / CLOSED | complete registered ledger; saturated subproofs retain Didin dependency |
| delta=12 four-partite U | OPEN | no complete terminal classification yet |
| delta=12 non-four-partite depth 0 | PROVED_CONDITIONAL / EXCLUDED | registered Didin+Brouwer saturated reduction |
| delta=12 non-four-partite depth 1 | PROVED_CONDITIONAL / EXCLUDED | registered saturated reduction |
| delta=12 non-four-partite depth 2, eps=2 | **PROVED_CONDITIONAL / CLOSED** | 308-edge C5 kernel + new pair-rule/K12 terminal contradiction |
| delta=12 non-four-partite depth 2, eps=0,1,3,4 | OPEN | full-core extensions remain |
| delta=12 non-four-partite depth 3 | OPEN | 309-edge equality terminal |
| delta<=11 | OPEN | no legal extrapolation from delta=12/13 |

## New depth-2 epsilon_U=2 closure

The previous reduction forced
\[
H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6,
\]
with one J-point d0 satisfying `N_W(d0)=K4`, two restored J-endpoints c1,c2 satisfying `N_W(ci)=K3`, and all U-excess concentrated on d0.

The new closure labels every vertex in the two K7 components, except possibly one shared restored-edge endpoint, by the W-component K5 or K6 that it must completely see. The nonadjacent-pair common-nonneighbour rule forces opposite labels across the two K7 components. Clique number at most 11 then produces K12 or K13 in every endpoint case.

Files:
- `DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md`
- `DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md`
- `verify_delta12_depth2_eps2_terminal_closure.py`

The new closure does not invoke Didin; its external input is the registered 308-edge saturated-kernel classification.

## Minimum-slack subfrontier

The minimum `epsilon_U+2delta=9` occurs at `(3,3)` and `(4,1)`. If an independent W-four-set has total W-side slack one, `MINIMUM_SLACK_EXACT_CORE.md` forces the exact 7,7,7,8 U-kernel. The complementary branch in which every independent W-four-set has slack at least two remains OPEN.

## Remaining low-delta target

Highest priority is now delta=12 depth-2 epsilon_U=3,4, followed by depth-3 and the delta=12 four-partite-U branch. Delta<=11 remains untouched.

The five shell templates remain a separate global same-core compatibility obligation.
