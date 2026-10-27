# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

Historical detail is preserved in prior commits. This file records the current frontier after the selected-anchor, shell-load, full-row-capacity, and delta=13 epsilon_U=0 closure rounds.

## Frozen core/support contract

\[
|H|=47,\ e(H)=284,\ \alpha(H)\le4,\ \omega(H)\le11,\ \delta(H)\ge12,
\qquad \sum_{x\in H}(d_H(x)-12)=4.
\]
There is U subset H with |U|=29 and W=H\U with |W|=18. There are 49 independent support blocks, seven in each of seven exact-129 colors, disjoint within color and pairwise linear.

With
\[
L_U=\overline{H[U]},\quad \delta=e(L_U)-294,\quad
\epsilon_U=\sum_{u\in U}(d_H(u)-12),
\]
we have
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta,
\]
\[
3\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad \epsilon_U+2\delta\ge9,
\]
and every feasible profile has alpha(H[W])=4.

## Exact selected-component structure

Every support block Q is the H-four-set of a selected isolated exact-color K5 component Q union {a(Q)}, with anchor a(Q) in {p} union A. Anchors are distinct within a color and pointwise injective through U.

For exact color c, let b_c be the number of selected B anchors. Then
\[
\boxed{b_c\in\{5,6,7\}}.
\]
At most one selected S anchor occurs per exact color, and at least 35 of the 49 selected block occurrences are B-anchored. Deleting the seven selected K5s leaves exactly `3K5 + G11` in that exact color.

## Five-template global forcing now registered

### Actual selected hub-complete blocks

If the shell template has a full B row f (k_f=3), every selected B-anchored block that is not hub-complete must meet D_f. Since |D_f|=3 and same-color selected blocks are disjoint, each exact color has at least b_c-3>=2 actual selected hub-complete blocks.

Templates A/B/C/D always have a full row; E either has a full row or else its row equations force all ten B rows to be the P3 ends-pair type. Therefore:

- A/B/C/D and E with n3>=1: at least 14 actual selected hub-complete blocks globally;
- E with n3=0: at least 35 actual selected B-blocks hit both P3 endpoint rows.

### Full-row linearity capacity

If h is the number of full B rows and N_bad is the global number of selected B-blocks that are not hub-complete, pairwise support linearity plus pointwise anchor injectivity gives
\[
\boxed{N_{bad}\le C(h):=\min\{21,\lfloor9+60/h\rfloor\}.}
\]
Hence
\[
N_{hub}^{sel}\ge B_{sel}-C(h),\qquad B_{sel}=\sum_c b_c\ge35.
\]
In particular A and C have h>=6, so
\[
\boxed{N_{hub}^{sel}\ge16\quad\text{in A and C}.}
\]
For h=7,8,9,10 the corresponding floors are 18,19,20,20.

### Exact shell cross-load with S anchors

Let sigma be the number of selected S-anchor occurrences among the seven exact colors and beta=e(M[S]). Every exact color owns at least one exact-colored S-B shell edge; a color with a selected S anchor owns at least two. Thus
\[
\boxed{|E_{exact}(S,B)|\ge\max\{14-\beta,\ 7+\sigma\}.}
\]
The first term is the previously registered exact shell-edge bound, the second is the new residual-factor refinement.

Primary files: `SELECTED_SUPPORT_HUB_COMPLETENESS.md`, `FULL_ROW_LINEARITY_CAPACITY.md`, `S_ANCHOR_CROSS_LOAD_REFINEMENT.md`.

## Low-delta frontier — new closure

The delta=13, epsilon_U=0, four-partite-U branch is now excluded under the registered Brouwer/Kang-Pikhurko equality theorem.

Reduction:
- e(H[W])=35, so J=bar(H[W]) is K5-free on18 vertices with 118 edges;
- J cannot be four-partite because no four positive clique sizes summing18 have total target clique-edge count35;
- 118 is exactly the non-four-partite Brouwer bound, so KP equality leaves only five W kernels:
  (3,4,5,5;a=1,2) and (4,4,4,5;a=1,2,3).

Closure:
- epsilon_U=0 implies every U vertex has a W neighbour, so every D-to-small H[U] cross-degree is <=4;
- any W vertex not complete to a U part must have d_H(w,U)>=10;
- low W vertices (U-degree<=9) therefore carry one of four U-part labels;
- equal labels force a target W-edge by the registered nonadjacent-pair common-neighbour inequality;
- omega(H)<=11 gives label capacities 4,4,4,3, so at least three W vertices must be high;
- the four-unit W excess budget permits only a short list of high sets in each KP kernel, and every remaining low graph needs at least five labels or strands the exceptional x vertex.

Therefore
\[
\boxed{\delta=13,\ L_U\text{ four-partite is completely excluded for }\epsilon_U=0,1,2,3.}
\]
Files: `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`, `DELTA13_EPS0_KP_KERNEL_CLOSURE.md` and their finite replay scripts.

## Current low-delta status

- delta=16: excluded.
- delta=15: four-partite and registered non-four-partite branches excluded.
- delta=14: four-partite excluded; saturated non-four-partite branch remains conditional on the unaudited Didin dependency.
- delta=13: **all four-partite epsilon_U=0,1,2,3 branches excluded**; non-four-partite remains OPEN.
- delta<=12: OPEN.

## Contract classes / firewall

1. Pure graph: core/U/W ledgers, alpha/omega bounds, support linearity consequences.
2. Labelled exact-129: selected K5 anchors, b_c in {5,6,7}, residual `3K5+G11`, exact shell colour ownership.
3. Published external extremal input: Brouwer/Kang-Pikhurko where explicitly cited, including the new delta=13 epsilon_U=0 equality reduction.
4. Conditional external input: the delta=14 saturated branch still depends on the unaudited Didin 2026 preprint theorem.
5. Parent bridge: V12 template exhaustiveness and the original K145-to-T61 chain remain separate dependencies.

## Current unique highest-leverage blocker

> Prove that none of V12 templates A–E can realize the strengthened selected-support system on one legal 284-edge core, using the actual hub-complete selected blocks, full-row linearity capacity, exact S-B colour load, U/W support multiplicities, residual `3K5+G11`, and four-unit core excess.

Independently, the remaining low-delta core frontier is delta=13 non-four-partite and delta<=12.

## Latest substantive commits

- `49d86aee7a4c89400fffd94b5616845281257d13` — actual selected hub-complete support blocks + S-anchor cross-load theorem.
- `5e6d6d311860a412dccab1a5b0a7b2d513d28f1b` — full-row linearity capacity; A/C hub-complete floor raised to16.
- `ffc2b514fe66ce5cfa6a3f9202cc857454e9fd45` — delta=13 epsilon_U=0 reduced to five KP W-kernels.
- `fa73d6b2e81c7c501c03bb5cfa5244ca0c0ff9a5` — all five kernels excluded; delta=13 four-partite branch fully closed.

No E407-Q32 or EG617 closure is claimed.