# E407 Q32 — open contracts

Date: 2026-10-27  
Status: **OPEN / NOT_CERTIFIED. This is the minimum remaining obligation list after the latest five-template and delta=13 four-partite advances.**

## C1. Five-template same-core labelled incompatibility — primary blocker

For each V12 template A–E, exclude a common legal E407 object satisfying simultaneously:

- |H|=47, e(H)=284, alpha(H)<=4, omega(H)<=11, delta(H)>=12, total core excess four;
- |U|=29, |W|=18 and the exact U/W edge ledger;
- 49 selected support blocks, seven per exact-129 color, disjoint within color and pairwise linear;
- every selected block is an exact-color K5 core-four-set with a genuine outside-core anchor;
- b_c in {5,6,7}, at most one selected S anchor per exact color;
- residual exact-color factor 3K5+G11;
- exact shell rows D_a, missing-edge six-set/transversal constraints;
- pointwise anchor injectivity and edge-color uniqueness;
- the four-unit core excess allocation.

New mandatory strengthening of C1:

1. A/B/C/D and E with a full B row have at least 14 actual selected hub-complete B-blocks globally.
2. If h is the number of full B rows, non-hub-complete selected B-blocks are at most C(h)=min(21,floor(9+60/h)). Hence A/C, where h>=6, have at least 16 actual selected hub-complete blocks; h=7,8,9,10 would force 18,19,20,20.
3. E with no full row is uniquely the ten-ends-pair profile and has at least 35 actual selected B-blocks hitting both P3 endpoint rows.
4. If sigma is the number of selected S-anchor occurrences and beta=e(M[S]), exact-colored S-B edges satisfy
   |E_exact(S,B)| >= max(14-beta, 7+sigma).
5. The target-excess/color-premium ledger remains live: every B vertex has target degree13 and exact seven-unit non-target premium; at least eight U points carry five or more distinct selected B-anchor block incidences.

C1 is not solved by shell-only counting; a valid contradiction must use common U/H incidence or residual exact-factor structure.

## C2. Shell-only closure is certified insufficient

`SHELL_LIST_RELAXATION_AUDIT.md` constructs a coarse label relaxation for any shell missing graph with at least fourteen edges. Therefore b_c>=5, at most one S anchor, two residual shell edges/color, and edge uniqueness do not close A–E by themselves.

## C3. Low-delta residual frontier

The delta=13 four-partite-U branch is now completely closed for epsilon_U=0,1,2,3. The new epsilon_U=0 proof is conditional only on the registered published Brouwer/Kang-Pikhurko equality theorem plus the frozen core/support contract.

Still open:

- delta=13, L_U non-four-partite;
- every delta<=12 case.

Do not extrapolate the delta=13 four-partite proof to these branches.

## C4. Delta=14 conditional dependency

The non-four-partite K5-saturated delta=14 branch remains only PROVED_CONDITIONAL because its alpha-critical reduction depends on the unaudited Didin 2026 preprint theorem. A terminal E407 proof must either discharge or replace this dependency.

## C5. Minimum-slack fork

At (delta,epsilon_U)=(3,3) and (4,1), the slack-one branch is reduced by `MINIMUM_SLACK_EXACT_CORE.md` to an exact 7,7,7,8 U-kernel. The complementary branch in which every independent W-four-set has total slack at least two remains OPEN.

## C6. V12 exhaustiveness dependency

The five templates are exhaustive only under the retained V12 analytic/lower-order screen chain. Finite replay certifies the enumeration, not every analytic screen theorem.

## C7. Original K145 bridge

Even a complete E407 Q32 closure would be one local T61 obligation. E408, backend/root obligations, and the original K145-to-T61 reduction remain separate. EG617(r=12) stays OPEN / NOT_CERTIFIED.

## Current minimum theorem sought

> **E407 Q32 Same-Core Labelled Compatibility Theorem.** Under the frozen parent contract and retained V12 screen hypotheses, none of A–E admits the strengthened selected-support system above on a legal 284-edge core.

A successful proof of this theorem plus closure of the remaining delta=13 non-fourpartite / delta<=12 local branches and the delta=14 conditional dependency would close the local E407-Q32 obligation. It would still not by itself certify the whole EG617(r=12) theorem.