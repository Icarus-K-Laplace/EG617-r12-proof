# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The latest work has materially strengthened the exact-129 / selected-support join, but no one of the five V12 shell templates A–E has yet been globally excluded against the same 284-edge core.

## Frozen core/support contract

Under the retained T61/V12 E407-Q32 boundary:

\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12,
\]
\[
\sum_{x\in H}(d_H(x)-12)=4.
\]

There is a support set \(U\subset H\), \(|U|=29\), with \(W=H\setminus U\), \(|W|=18\), and 49 independent 4-set support blocks, seven in each of seven exact-129 color classes. Blocks are disjoint within a color class and pairwise linear across colors.

Put
\[
L_U=\overline{H[U]},\quad \delta=e(L_U)-294,\quad \epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
Then
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad e(H[W])=48-\epsilon_U-\delta,
\]
with
\[
3\le\delta\le16,\quad \delta+\epsilon_U\le16,\quad \epsilon_U+2\delta\ge9,\quad 0\le\epsilon_U\le4.
\]
Every feasible profile has \(\alpha(H[W])=4\).

## Contract classes

1. **Pure graph:** the 47-core ledger, U/W split, degree/excess identities, and consequences using only the stated graph bounds.
2. **Labelled exact-129:** the seven exact-129 colors, their selected support K5 components, anchor labels, component factorization, and edge-color uniqueness.
3. **External-input dependent:** exact-129 Type-I factorization and extremal classifications retain their registered external theorem hypotheses; the delta=14 saturated branch additionally depends on the unaudited Didin 2026 preprint theorem.
4. **Original-problem bridge:** the T61/V12 boundary and five-template exhaustiveness remain conditional on the parent reduction/lower-order seed chain. This workstream does not certify the full K145 bridge.

## Current exact-129 selected-component structure

For each exact-129 color c, the seven selected support blocks are seven isolated color-c K5 components
\[
Q_{c,j}\cup\{a_{c,j}\},\qquad Q_{c,j}\subset U,\quad |Q_{c,j}|=4,
\]
with seven distinct anchors \(a_{c,j}\in\{p\}\cup A\). Their complement is exactly
\[
\{u_c\}\cup W\cup((\{p\}\cup A)\setminus A_c^{sel})=3K_5\dot\cup G_{11}.
\]

### New anchor theorem

Let \(B\) be the ten-vertex shell clique and
\[
b_c=|A_c^{sel}\cap B|.
\]
Then
\[
\boxed{b_c\in\{5,6,7\}.}
\]
The old b=3 and b=4 residual branches are therefore vacuous.

If \(b_c=5\), then the selected anchors are exactly
\[
\{p,s_c\}\cup B_c,\qquad s_c\in S,\ |B_c|=5.
\]
For every exact color, at most one selected S-anchor occurs. Across all seven colors at least 35 of the 49 selected support-block occurrences are B-anchored and at most seven are S-anchored.

File: `SELECTED_B_ANCHOR_FLOOR.md`.

## New shell-color localization theorem

For every exact-129 color c,
\[
\boxed{e_c(M[A\setminus A_c^{sel}])\ge2.}
\]
Thus each exact color owns at least two shell missing edges whose endpoints are both unselected by that color. The seven exact colors consume at least fourteen distinct shell missing edges.

File: `SHELL_COLOR_EDGE_LOAD.md`.

## Route audit: shell-only Hall/SDR is insufficient

The two constraints above do not by themselves close any V12 template. For every shell missing graph with at least fourteen edges one can satisfy the coarse shell-label relaxation by assigning each exact color the allowed anchor type \(\{p\}\cup6B\) and two distinct unselected shell edges. Since all five V12 templates have a stronger edge floor, shell-only list matching cannot yield the terminal contradiction.

File: `SHELL_LIST_RELAXATION_AUDIT.md`.

Therefore the primary live global blocker is a **same-core labelled support-row incompatibility theorem**, not another shell-only scalar count.

## Five-template selected high-k consequences

Using \(b_c\ge5\) and the audited row floors, the actual selected 49-block system has at least the following high-k B-anchor occurrences:

| Template | per exact color | across seven colors |
|---|---:|---:|
| A | >=1 k=3 | >=7 |
| B | >=3 k>=2 | >=21 |
| C | >=1 k=3 | >=7 |
| D | >=2 high-k | >=14 |
| E | no positive floor from anchor intersection alone | 0 |

For A/C these selected blocks are hub-complete; B/D blocks hit at least two S rows. The older auxiliary no-S component-witness bounds remain valid under their recorded row-transversal dependencies, but they are not substituted for the actual selected 49 blocks.

## Low-delta frontier

- delta=16: excluded.
- delta=15: four-partite and non-four-partite branches excluded under registered contracts.
- delta=14: four-partite branch excluded; non-four-partite saturated branch only PROVED_CONDITIONAL because of the Didin dependency.
- delta=13: four-partite epsilon_U=1,2,3 branches currently registered as excluded under their stated profile contracts; four-partite epsilon_U=0 remains open; non-four-partite remains open.
- delta<=12: open.

No low-delta status was silently changed by the new exact-color theorems.

## Minimum-slack branch

The previous exact-core reduction remains live: if a minimum-slack profile contains an independent W-four-set of total W-side slack one, U becomes exactly four-partite with sizes (7,7,7,8), with three K7 parts and an R=K8 part. The complementary branch in which every independent W-four-set has slack at least two remains open.

## Current unique highest-leverage theorem target

> Prove that no V12 template A–E can realize, on the same H and U, seven exact-color classes of selected K5 components satisfying b_c in {5,6,7}, at most one selected S-anchor per color, the D_a row-transversal constraints, support-block disjointness/linearity, the residual 3K5+G11 factor, and the four-unit core excess ledger.

This is stricter than the previous label-join target because the actual selected-anchor family is now heavily constrained.

## Repository provenance

Historical Rounds 1–12 are preserved in parent commit `3b336b34b8540da89f4dac6589d056ac48bcfe10` and its ancestors. New substantive commits:

- `f2f991695a23b30c26a90070d7c2d1ab25b9d4f8` — selected B-anchor floor five;
- `d9478df06e1952e89f3a799dbed8ada41e441454` — two residual shell edges per exact color;
- `12ff5bfe8c631b7514f534bf0fbdfc1b0424aa92` — shell-only list relaxation audit.

No claim of E407 closure is made.
