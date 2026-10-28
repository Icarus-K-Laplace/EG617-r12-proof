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
| delta=12 non-four-partite depth 0 | PROVED_CONDITIONAL / EXCLUDED | registered saturated Didin+Brouwer reduction |
| delta=12 non-four-partite depth 1 | PROVED_CONDITIONAL / EXCLUDED | registered saturated reduction |
| delta=12 non-four-partite depth 2, eps=0..4 | **PROVED_CONDITIONAL / CLOSED** | registered 308-edge C5-blowup kernel plus terminal proofs |
| delta=12 non-four-partite depth 3, eps=0..4 | **PROVED_CONDITIONAL / CLOSED** | registered balanced 309-edge equality model plus terminal proofs |
| delta=12 four-partite, eps=4 | **PROVED / CLOSED** | support kernel + W-capacity; no Didin |
| delta=12 four-partite, eps=3 | **PROVED / CLOSED** | support kernel + W-profile/capacity; no Didin |
| delta=12 four-partite, eps=0,1,2 | OPEN | global 7,7,7,8 reuse/capacity still required |
| delta<=11 | OPEN | no legal extrapolation from delta=12/13 |

## Delta=12 non-four-partite completion

The full augmentation depth range k=0,1,2,3 is now discharged under its registered dependencies.

Depth 2 files include the eps0/1/2/3/4 terminal closures under the 308-edge kernel classification. Depth 3 files are:
- `DELTA12_DEPTH3_EPS0_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS1_EPS2_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md`;
- `DELTA12_DEPTH3_EPS3_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS4_CLOSURE.md`.

The hard epsilon_U=3 survivor in the `(4,4,4,6)` W profile is eliminated by unpacking the exact P1/P2 equality-model structure: a mixed seven-point P1 forces at least six same-label P1–P2' pairs while only three restored target edges exist.

The epsilon_U=4 equality model is eliminated by exceptional-pair component labels and restored-edge incidence capacity; the final AC/all-B branch forces at least nine same-label A-A cross pairs against only three restorations.

## Delta=12 four-partite-U kernel

`DELTA12_FOURPARTITE_SUPPORT_KERNEL.md` gives
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad (7,7,7,8),
\]
with omission weights `r_r` on R summing to seven and
\[
d_W(r)=5+\epsilon_r-h_r.
\]

### epsilon_U=4 — CLOSED

`DELTA12_FOURPARTITE_EPS4_CLOSURE.md` proves that every R point with omission at most two consumes at least one core-excess unit. At least six of the eight R points have omission <=2, forcing epsilon_R>=6>4.

### epsilon_U=3 — CLOSED

`DELTA12_FOURPARTITE_EPS3_CLOSURE.md` proves that every R point with omission at most one consumes at least one core-excess unit. The proof handles the three W profiles `(3,5,5,5)`, `(4,4,4,6)`, and the one-defect `(4,4,5,5)` profile using the W common-neighbour capacity and K12 cap. At least five R points have omission <=1, forcing epsilon_R>=5>3.

### epsilon_U=2 — OPEN; naive local extension fails

The same one-point argument cannot simply be repeated. In the `(3,4,5,6)` W profile a coarse local capacity pattern exists with a zero-omission, zero-U-excess R point: all two W-excess units may concentrate on one K3 vertex, allowing a K3–K4 repeated T-label at capacity equality while the K5 and K6 components use the other two labels. This is a route-audit witness, not a full core realization.

Therefore epsilon_U=2 requires a **global reuse theorem** across the eight R points / three T-parts, not another scalar per-R inequality.

## Minimum-slack subfrontier

The minimum `epsilon_U+2delta=9` occurs at `(3,3)` and `(4,1)`. If an independent W-four-set has total W-side slack one, `MINIMUM_SLACK_EXACT_CORE.md` forces the exact 7,7,7,8 U-kernel. The complementary no-slack-one branch remains OPEN.

## Remaining low-delta target

The exact low-delta priority is now:
1. delta=12 four-partite epsilon_U=2,1,0;
2. all delta<=11;
3. independent replacement/audit of Didin-dependent saturated branches.

The five shell templates remain a separate global same-core compatibility obligation.