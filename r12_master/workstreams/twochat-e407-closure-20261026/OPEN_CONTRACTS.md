# E407 Q32 — open contracts

Date: 2026-10-28  
Status: **OPEN / NOT_CERTIFIED.**

## C1. Five-template same-core labelled incompatibility — primary global blocker

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

Mandatory strengthened consequences already proved:
1. A/B/C/D and E with a full B row have at least 14 actual selected hub-complete B-blocks globally.
2. A/C have at least 16 actual selected hub-complete blocks by full-row linearity capacity.
3. E with no full row is the ten-ends-pair profile and has at least 35 actual selected B-blocks hitting both P3 endpoint rows.
4. With sigma selected S-anchor occurrences and beta=e(M[S]), exact-colored S-B edges obey |E_exact(S,B)|>=max(14-beta,7+sigma).

Shell-only counting is already certified insufficient; a valid contradiction must use the common U/H incidence and/or the residual exact-color factor.

## C2. Low-delta frontier

Closed / conditional layers:
- delta=16: closed;
- delta=15: closed under registered contracts;
- delta=14 four-partite: closed;
- delta=14 saturated non-four-partite: PROVED_CONDITIONAL on unaudited Didin 2026;
- delta=13: PROVED_CONDITIONAL / CLOSED under the full registered ledger;
- delta=12 non-four-partite depth0/depth1: conditionally excluded under registered saturated-kernel inputs;
- delta=12 non-four-partite depth2 epsilon_U=2: **PROVED_CONDITIONAL / CLOSED** by `DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md`.

Still open:
- delta=12 four-partite U;
- delta=12 non-four-partite depth2 epsilon_U in {0,1,3,4};
- delta=12 non-four-partite depth3;
- all delta<=11.

Do not extrapolate the depth2 epsilon_U=2 terminal argument to the other epsilons without deriving their W-terminal data first.

## C3. Minimum-slack fork

At (delta,epsilon_U)=(3,3) and (4,1), the slack-one branch is reduced by `MINIMUM_SLACK_EXACT_CORE.md` to an exact 7,7,7,8 U-kernel. The complementary branch in which every independent W-four-set has total slack at least two remains OPEN.

## C4. Didin dependency

The non-four-partite K5-saturated delta=14 branch and some saturated depth reductions remain conditional on the unaudited Didin 2026 component-count theorem. The new delta12 depth2 epsilon_U=2 terminal closure itself does **not** use Didin.

## C5. V12 / parent bridge

The five templates are exhaustive only under the retained V12 analytic/lower-order screen chain. Finite replay certifies the enumeration, not every analytic screen theorem.

Even complete E407 Q32 closure would not certify EG617(r=12): E408, backend/root obligations, and the original K145-to-T61 reduction remain separate.

## Current highest-priority theorem targets

1. close delta=12 depth2 epsilon_U=3,4 and then epsilon_U=0,1;
2. close delta=12 depth3 and four-partite-U;
3. prove the A–E same-core labelled compatibility theorem;
4. replace/audit Didin before any unconditional local E407 claim.
