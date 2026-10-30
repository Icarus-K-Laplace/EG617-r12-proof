# E407-Q32 parent promotion theorem (conditional)

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL under the retained V12 input contract and the 29-point/49-block template-to-support contract; not an unconditional E407 or EG617 proof.**

## Theorem

Let `F` be a legal T61 E407 residual with `|V(F)|=61`, `delta(F)>=13`, `alpha(F)<=5`, `omega(F)<=11`, `e(F)=407`, all registered hereditary caps, and a globally maximal regular-pivot charge `Q=32`. Assume the retained analytic inputs recorded in `T61_H13_V12/Q32_KERNEL_COVERAGE.md` C0.

Assume in addition the registered template-to-support bridge (MS-29): every legal completion of each of the five V12 templates A--E has a target-color core `H` and a common support split `H=U dot-union W` satisfying

- `|H|=47`, `e(H)=284`, `delta(H)>=12`, `alpha(H)<=4`;
- `|U|=29`, `|W|=18`;
- seven selected distinct non-target exact-129 colors, with seven selected independent four-sets `Q_{c,j} subset U` in each selected color;
- the seven blocks in one color are disjoint, and all 49 blocks are pairwise linear across colors;
- every selected block is the four-core-vertex part of an isolated monochromatic K5 component of its assigned color.

Then no such E407 Q32 completion exists.

## Proof

### 1. Exhaustive V12 terminal coverage

Under the V12 C0 hypotheses, the archive's finite necessary domain consists of nine kernel families. The recovered archive and independent replay certify:

- 8,677 kernel-weight vectors;
- 17,957 outside-type count states;
- 1,984 labelled necessary shells;
- screen partition `90 + 1,192 + 148 + 554 = 1,984`;
- all 554 OPEN survivors map to exactly one of A--E, with every allowed outside-row type rechecked.

The independent replay has zero screen mismatches and zero template-row failures. Thus every legal E407 Q32 parent covered by C0 reaches one of the five terminal templates. This is a computation-certified finite coverage statement; the analytic screen rules and retained C0 hypotheses remain conditional as stated in the source package.

### 2. The 49 selected four-sets own 294 distinct edges

For each selected exact-129 color, the retained Kang--Pikhurko equality theorem supplies ten isolated monochromatic K5 components plus an 11-vertex remainder, under its recorded `alpha<=12`, `omega<=5`, 61-vertex and 129-edge hypotheses.

Let the 14 vertices outside H be `{p} union A`, with the V12 template split `A=S dot-union B`, `|S|=3`, `|B|=10`, and B a target K10. Every monochromatic K5 component contains at least one outside-H vertex, since `alpha(H)<=4`. A K5 cannot contain p together with a shell vertex because p is target-adjacent to every vertex of A; it contains at most one B vertex because B is a target clique. Hence any K5 component containing at least two outside-H vertices must contain at least one of the three S vertices. The ten K5 components are vertex-disjoint, so at most three components can contain at least two outside-H vertices. At least seven therefore contain exactly one outside-H vertex and four H vertices. Selecting seven gives seven independent four-sets per selected exact color.

Within one color these four-sets are disjoint. Across distinct colors, two blocks cannot share a pair: that pair would be assigned two different non-target colors. Thus the 49 selected four-sets are pairwise linear and own

`49 * binom(4,2) = 294`

distinct pairs of U. Each pair is a non-target edge, so all 294 lie in `L_U = complement(H[U])`.

### 3. The 29-point complement-edge reserve is at most 310

Let `delta_U = e(L_U)-294 >= 0`, and let

`epsilon_U = sum_{u in U}(d_H(u)-12) >= 0`.

Since `|U|=29`, `|W|=18`, `e(H)=284`, and `|E(H[U])| = binom(29,2)-e(L_U) = 112-delta_U`,

`e_H(U,W) = sum_{u in U} d_H(u) - 2e(H[U])`

`= (348+epsilon_U) - 2(112-delta_U)`

`= 124+epsilon_U+2 delta_U`.

Consequently

`e(H[W]) = 284 - (112-delta_U) - (124+epsilon_U+2delta_U)`

`= 48-epsilon_U-delta_U`.

Because `alpha(H[W])<=4`, the 18-vertex graph H[W] has at least

`p_4(18) = 2 binom(4,2) + 2 binom(5,2) = 32`

edges. Therefore

`48-epsilon_U-delta_U >= 32`,

so `delta_U<=16` and

`e(L_U)=294+delta_U<=310`.

### 4. One unselected non-target color requires 22 edges

There are eleven non-target colors in total, while only seven distinct colors are selected for the support blocks. Choose an unselected non-target color D.

The original balanced coloring gives `alpha(D)<=12`: every 13-set must contain an edge of every color. Hence `alpha(D[U])<=12`. Turan's theorem gives

`e_D(U) >= p_12(29) = 5 binom(3,2) + 7 binom(2,2) = 22`.

Every D-edge in U belongs to `L_U`. Unique edge ownership makes these D-edges disjoint from the 294 selected support edges, all of which are assigned one of the other seven colors. Thus

`e(L_U) >= 294+22 = 316`,

contradicting `e(L_U)<=310`. The gap is six. QED.

## Promotion scope

This proves the E407 Q32 contradiction **conditional** on the V12 retained analytic inputs and MS-29. The finite replay establishes the exhaustive A--E mapping, not MS-29 itself. The V12 archive does not contain a derivation of `|U|=29`; that property is supplied by the separate global-root template-to-support contract. Until the minimum-support/29-point bridge is independently proved or its exact proof source is attached and audited, the correct status remains `PROVED_CONDITIONAL`, not `PROVED`.

This theorem does not close E408 Q32, E408 Q33, the other T61 energy branches, or the original K145-to-T61 root reduction.


## 5. Support-size audit beyond MS-29

The conditional theorem above uses the stronger MS-29 hypothesis |U|=29. A separate support-size argument is now available without assuming that equality. Let U_7 be the union of the 49 blocks from the seven selected exact-129 colors and v=|U_7|. The exact-129 support theorem gives v >= 29. Since the four other non-target colors each require at least p12(v) edges in U_7, the 49 selected blocks plus those four color floors give

    e(complement(H[U_7])) >= 294 + 4 p12(v).

The 47-core edge/degree ledger gives

    e(complement(H[U_7])) <= binom(v,2) - 12v + 284 - p4(47-v).

The comparison excludes v=29,30,31,32,33. At v=34 equality is possible only with the rigid structure recorded in V12_GENERAL_SUPPORT_RESERVE.md; no contradiction is yet known there. The scalar inequality does not exclude v >= 35.

Separately, the full-color crosscut E407_SEVEN_EXACT_COLOR_EXCLUSION.md gives m >= 8 under its own retained Type-I and nonexact-degree hypotheses. If U_m is the union of seven blocks from every exact color, its support is at least35 for m=8,9 and at least36 for m=10. U_m is not the same set as U_7, so this does not promote MS-29.

Promotion decision unchanged: V12 finite coverage is COMPUTATION_CERTIFIED under C0; the 29-point parent bridge remains CONDITIONAL; the E407 Q32 contradiction is not promoted to unconditional PROVED; EG617(r=12) remains OPEN / NOT_CERTIFIED.
