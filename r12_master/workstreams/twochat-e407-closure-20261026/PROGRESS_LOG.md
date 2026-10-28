# Progress log — E407 Q32 two-chat closure workstream

Date: 2026-10-28  
Branch: `workstream/r12-twochat-e407-closure-20261026`

Historical Rounds 1–38 are preserved in prior commits. E407 Q32 remains OPEN / NOT_CERTIFIED.

## Round 39 — depth-3 epsilon_U=3 exceptional-pair terminal

Files:
- `DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md`;
- `DELTA12_DEPTH3_EPS3_CLOSURE.md`;
- `verify_delta12_depth3_eps3_eps4_pair_reduction.py`.

The exact 309-edge equality model reduces epsilon_U=3 to restored/nonrestored exceptional-pair kernels. The hard nonrestored `(K4,K4,K4,K6)` survivor forces P3/P4 to use one common K4 W-label with complementary two-subsets of an exceptional K4. Unpacking the exact P1/P2/x/y/A0 equality-model adjacencies then forces P1 to use both binary exceptional labels. A mixed seven-point P1 against six P2' points has at least six same-label cross pairs, while only three restored target edges exist. Contradiction.

Status: depth3 epsilon_U=3 **PROVED_CONDITIONAL / CLOSED** under the registered 309-edge equality classification.

## Round 40 — depth-3 epsilon_U=4 terminal

Files:
- `DELTA12_DEPTH3_EPS4_CLOSURE.md`;
- `verify_delta12_depth3_eps3_eps4_terminal.py`.

Restored xy is impossible because both exceptional vertices must contain a complete W-component of size at least four while their total W-degree is at most seven. In the nonrestored branch, exceptional component types are reduced to AB or AC. AB gives a binary K5 label contradiction/K12. AC either has a D-labelled P vertex, forcing a mixed P1 binary count of at least six same-label pairs versus three restorations, or all P3/P4 vertices use B; then all six restored endpoint incidences lie in R and force at least 3x3=9 A-A cross pairs versus three restorations.

Status: depth3 epsilon_U=4 **PROVED_CONDITIONAL / CLOSED**.

Together with the earlier epsilon_U=0,1,2 closures, the entire **delta=12 non-four-partite depth3 layer is closed** under the registered equality-model dependency. Combined with closed depths0–2, the full delta=12 non-four-partite branch is conditionally discharged.

## Round 41 — delta=12 four-partite epsilon_U=4

File: `DELTA12_FOURPARTITE_EPS4_CLOSURE.md`.

For R omission weight q<=2, the three anticomplete T7 parts leave three sets A_i of size at least five. Every W-nonneighbour of r must be complete to one A_i. Cross-component reuse of an A_i would create at least five common U-neighbours, exceeding the W-pair capacity at epsilon_W=0. Thus r is complete to a W component. K12 capacity sharpens this to d_W(r)>=max(4,6-h_r), and the exact identity d_W(r)=5+epsilon_r-h_r yields epsilon_r>=1. At least six of eight R points have omission <=2, forcing epsilon_R>=6>4.

Status: four-partite epsilon_U=4 **PROVED / CLOSED**, no Didin.

## Round 42 — delta=12 four-partite epsilon_U=3

File: `DELTA12_FOURPARTITE_EPS3_CLOSURE.md`.

For omission q<=1, each A_i has size at least six. In the two q=0 W profiles, the one available W-excess unit leaves every cross-component same-label pair below the six-common-neighbour capacity threshold, so some W component is complete to r. In the one-defect `(4,4,5,5)` profile, the only possible repeated label across all four nonempty components would be the unique W-cross-edge endpoints, which itself costs at least six r-neighbours. In all cases d_W(r)>=6-h_r, hence epsilon_r>=1. At least five R points have q<=1, forcing epsilon_R>=5>3.

Status: four-partite epsilon_U=3 **PROVED / CLOSED**, no Didin.

## Round 43 — epsilon_U=2 route audit

The naive per-R extension is **not** valid. In the `(3,4,5,6)` W profile, a coarse local capacity pattern exists for an omission-zero, U-excess-zero R point with d_W=5: both W-excess units can concentrate on one K3 vertex, allowing that K3 vertex and a K4 to reuse one T7 label at exact W-pair capacity, while four nonneighbours in K5 and four in K6 use the other two labels. This is not a full core realization, but it defeats the attempted one-point theorem.

Therefore epsilon_U=2 requires a global reuse theorem across all eight R points / three T-parts. No closure is claimed for epsilon_U=2,1,0.

## Current exact frontier

1. delta=12 four-partite epsilon_U=2,1,0;
2. all delta<=11;
3. five-template same-core labelled incompatibility A–E;
4. independent replacement/audit of Didin-dependent saturated branches;
5. parent V12/K145 bridge remains separate.

E407 Q32 remains OPEN / NOT_CERTIFIED.