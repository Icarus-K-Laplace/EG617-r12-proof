# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

Canonical unconditional/retained closure remains `E397..E406 = EMPTY` under the stated contracts.

Delivered V11/V12 supersede the older source-level frontier. Both packages have been independently replayed; the fresh V12 extraction passed all 28 manifest checks and reproduced the certificate. This certifies finite enumeration only, not analytic screen rules or the remaining core-completion problem.

Replay-certified finite V12 state, conditional on the retained lower-order seeds:

- E407 maximum `Q=31` is excluded by V11;
- E408 maximum `Q=31` is excluded by V11;
- V12 proves `Xi >= L + 2k - 2` for `k in {8,9,10}`;
- the common-K10 external pair-row union therefore carries at least18 units of excess;
- the fresh V12 replay verified 8,677 weight assignments and 17,957 counting states;
- E407 maximum `Q=32` is reduced to five `rho=0` templates with a common regular `K11`;
- the unresolved V12 bridge is whether those five templates can coexist with one 284-edge core;
- E408 `Q=32,33` remain OPEN.

Source-level front-end frontier:

- E407: only `Q=32` OPEN, reduced to five common-K11 templates;
- E408: `Q=32,33` OPEN.

See `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`.

## High backend — source-level layer state

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### E334

Delivered V8 source-reports `E334 = EMPTY` relative to the retained backend and accepted V7 forcing. Independent package replay remains pending.

The graph-theoretic obstruction behind that report has now been independently strengthened far beyond CORE211:

> any 35-point core with `alpha<=3`, `omega<=11`, `delta>=12` and three pairwise nonadjacent degree-12 anchors satisfies `e(H)>=213`.

Equivalently total excess `K=sum(d_H-12)>=6`.

Therefore any high-backend configuration with the three-anchor property obeys the layer-independent envelope

`q<=E-304`.

This gives the table:

- E334: q<=30;
- E335: q<=31;
- E336: q<=32;
- E337: q<=33;
- E338: q<=34;
- E339: q<=35;
- E340: q<=36.

The first surviving equality layer `K=6` is no longer an unstructured frontier:

- `c=2` has now been **fully eliminated** by a transversal-cover / exact cross-edge count theorem;
- `c=3` is reduced to exactly one bad pair-connector plus one K9-dominator, with all excess outside the bad subsystem at most1;
- `c=4,(10,10,8)` has at most two K8-dominators, and two dominators must form a saturated K11 with the small block and its anchor;
- `c=4,(10,9,9)` has at most one anchor-compatible dominator per K9.

Thus any K=6 three-anchor survivor must lie in the finite c=3/c=4 equality geometries, not in a new E-layer case tree.

Files:

- `backend/GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- `backend/GLOBAL_THREE_ANCHOR_EXCESS_LOWER_BOUND.md`;
- `backend/GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- `backend/GLOBAL_THREE_ANCHOR_BACKEND_ENVELOPE.md`;
- `backend/GLOBAL_THREE_ANCHOR_K6_C2_FULL_CLOSURE.md`;
- `backend/GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md`;
- `backend/GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- `backend/GLOBAL_THREE_ANCHOR_K6_EQUALITY_REDUCTION.md`.

### E335..E337

OPEN. The correct objective is not to replay the E334 branch tree, but to determine which survivors force three degree-12 anchors or enter the global support-compatibility contract, and then test the finite K=6 equality geometries if the three-anchor branch is tight.

## Global Support-Compatibility architecture

The strongest current analytic synthesis is `backend/GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`.

For a boundary one-loss common-S d2/d3 support system:

1. **three zero-charge incidence signatures** force three pairwise nonadjacent degree-12 anchors and hence the backend envelope `q<=E-304`;
2. **at most two signatures** force every support into at most three canonical zero-skeleton patterns;
   - d2 repeated patterns are common-zero-hub target-K2 sunflowers;
   - d3 repeated patterns are Type-H / Type-P sunflowers;
3. under the standard low-cross bounds, support matching number is at most6, yielding a support transversal of size at most12 (d2) or18 (d3);
4. hereditary packing bounds every nontrivial d2 pattern to at most9 owners and every low-charge d3 pattern to at most8 owners.

The three-signature branch has now been geometrically aligned with the three-anchor partition by `GLOBAL_ZERO_SIGNATURE_ANCHOR_ALIGNMENT_THEOREM.md`:

- each zero-signature class lies in the corresponding exclusive anchor clique;
- each class has size at most the support size d;
- therefore at most `3d` zero-charge support-union vertices exist;
- every additional support-union vertex costs at least one unit of common-S charge.

The first-high-slack layer is structurally complete by `backend/GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md`:

- plateau: at most3 singleton rows;
- one-loss: governed by the master theorem above;
- deep-loss: at most3 isolated support classes;
  - d2 multiplicity per class <=9;
  - d3 multiplicity per class <=8.

Thus D2/A2 and d3/A3 no longer contain arbitrary high-slack overlap geometry.

The unique remaining global backend bridge is:

> **forcing-to-master-contract:** prove that every surviving shell regime either triggers the three-anchor envelope directly, enters the boundary one-loss/low-cross contract, or descends to it through a finite higher-slack equality layer.

Once this bridge is available, the old D2-A/B/C/D/R9 and E334--E340 labels no longer require separate structural classifications.

## Large-support bridge correction

The fully-decorated d4/d9 branch has been corrected and strengthened.

The old interpretation 'maximal fully-decorated owner count -> K4,9' was inconsistent with `q=e(M)+G_A` and has been removed.  Full decoration gives the exact owner bound

`q>=dN+d`.

Therefore at q<=38:

- d4 fully-decorated owner count `N<=8`;
- d9 fully-decorated owner count `N<=3`.

At the maximum possible fully-decorated count there is exactly one leftover shell vertex, and

`d_M(x)+g_x<=q-36<=2`.

More generally, with t leftovers and slack

`R=q-d(14-d-t)`,

one has

`sum_(x in T)(d_M(x)+g_x)<=2R`,

so a low-defect leftover is extracted by averaging.

Files:

- `backend/GLOBAL_LARGE_SUPPORT_DECORATED_ESCAPE_THEOREM.md`;
- `backend/GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md`;
- `backend/GLOBAL_FULLY_DECORATED_MULTI_LEFTOVER_DESCENT.md`.

K4,9 remains correctly classified as a non-fully-decorated plateau/equality geometry and is already closed.

## E338..E340 current right edge

The K4,9 top-channel plateau family is empty. Low-decoration forcing gives q36=>G>=3, q37=>G>=2, q38=>G>=3; all q38,G=2 states are empty. q36 d4/d9 ceiling exchanges are empty.

q36 f=2 far-2K1 a_F=0 is CLOSED. In far-2K1 a_F=1, concurrent work continues on the higher-slack A4/A5/A6 sectors. In far-target-K2, safe retained reductions close A2 and much of A3 but A4 remains active. Shell-poor still requires a simultaneous near-Mantel/global compatibility theorem.

The preferred interpretation of all of these residuals is through the master support variables `(loss layer, zero-signature count, matching number, pattern type, owner multiplicity, hereditary cap)`, not through independent q36 case labels.

## Global state

Independently re-certified closed backend interval in this assistant session: `E329..E333`.

Source-level closed backend interval after delivered V8: `E329..E334`, relative to retained backend/V7.

Remaining obligations:

- T61 E407 Q32: five common-K11 templates versus one 284-edge core;
- T61 E408 Q32/Q33;
- backend E335..E340 through the forcing-to-master-contract bridge and finite K=6 equality windows;
- V11/V12 replay is complete; independent V8 package replay remains pending.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.