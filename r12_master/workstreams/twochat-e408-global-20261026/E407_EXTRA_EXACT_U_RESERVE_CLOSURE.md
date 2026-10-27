# E407 Q32 crosscut — extra exact color versus the 29-point U-edge reserve

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL E407-Q32 CONTRADICTION** under the frozen V12 minimum-support contract plus `E407_SEVEN_EXACT_COLOR_EXCLUSION.md` and the standard non-target independence bound.

This theorem is written in the E408/global workstream as an independent crosscut. The active E407 sibling remains read-only.

## 1. Frozen E407 Q32 support contract

Use the current V12 E407-Q32 terminal contract recorded by the active sibling workstream:

\[
|H|=47,\qquad e(H)=284,\qquad \alpha(H)\le4,\qquad \delta(H)\ge12,
\]

with a 29-point support set U and 49 selected independent four-sets, seven from each of seven selected exact-129 color classes.

The 49 support blocks are disjoint within a color class and pairwise linear across different selected colors. Put

\[
L_U=\overline{H[U]}.
\]

The exact frozen core ledger is

\[
\boxed{e(L_U)=294+\delta,\qquad 3\le\delta\le16.}\tag{1}
\]

Each selected support block Q is the four-core-vertex part of an isolated monochromatic exact-color K5. Therefore all six pairs inside Q are edges of L_U and all six have that selected non-target color.

Because the 49 blocks are pairwise linear, no pair of U-vertices occurs in two selected blocks. Hence their six-edge sets are pairwise disjoint and the selected system owns exactly

\[
49\cdot6=294
\]

distinct edges of L_U.

Consequently every edge of L_U not belonging to one of the seven selected support systems lies in a residual pool of size exactly

\[
e(L_U)-294=\delta\le16.\tag{2}
\]

## 2. A genuine E407 parent has an eighth exact color

`E407_SEVEN_EXACT_COLOR_EXCLUSION.md` proves from the full 61-point residual color ledger that a genuine E407 h13 T61 parent cannot have exactly seven exact-129 non-target colors.

Since the total non-target excess above129 is four, the global exact-color count m always lies in {7,8,9,10}. Excluding m=7 gives

\[
\boxed{m\ge8.}\tag{3}
\]

The V12 terminal selects only seven exact color classes. Thus (3) guarantees an exact-129 non-target color C_* which is not one of those seven selected classes.

No claim is needed about how C_* meets the shell, which Type-I components are selected, or whether it contributes an additional support block to the V12 construction.

## 3. Every non-target color needs at least 22 edges on U

For every non-target color C in the original balanced coloring,

\[
\alpha(C)\le12.
\]

Therefore also

\[
\alpha(C[U])\le12.
\]

For |U|=29, Turan's theorem applied to the complement gives the exact minimum number of C-edges on U:

\[
e_C(U)\ge p_{12}(29).
\]

The balanced 12-part partition of 29 has five parts of size3 and seven parts of size2, so

\[
p_{12}(29)
=5\binom32+7\binom22
=15+7
=22.
\]

Hence the additional exact color C_* satisfies

\[
\boxed{e_{C_*}(U)\ge22.}\tag{4}
\]

## 4. Unique edge ownership gives the contradiction

Every C_*-edge inside U is a non-target edge and therefore lies in L_U.

But C_* is distinct from all seven selected exact colors. An edge already owned by one of the 49 selected support K4s cannot also have color C_*. Thus all C_*-edges on U must lie in the residual pool from (2), whose size is at most16.

Therefore

\[
22\le e_{C_*}(U)\le\delta\le16,
\]

which is impossible.

Thus the frozen E407 Q32 V12 minimum-support terminal has no realization:

\[
\boxed{\text{E407 Q32 V12 terminal is PROVED_CONDITIONAL impossible}.}
\]

## 5. Strength and scope

The contradiction uses only:

1. the V12 frozen support contract |U|=29 with 49 pairwise-linear selected exact-color K4 blocks;
2. the exact complement-edge ledger e(L_U)=294+delta with delta<=16;
3. the independently proved full-color crosscut m>=8 from `E407_SEVEN_EXACT_COLOR_EXCLUSION.md`;
4. the universal non-target condition alpha(C)<=12;
5. Turan's theorem and unique edge ownership.

It does **not** use:

- the five individual V12 shell templates A--E;
- the new repeated-anchor transversal theorem;
- the low-delta case split;
- the Didin-dependent delta=14 theorem;
- any E408 285-edge identity;
- any Q33 support-31 identity.

Therefore it bypasses the remaining same-core labelled support-row compatibility casework entirely, provided the frozen V12 theorem really places every surviving E407-Q32 state into the stated 29-point/49-block support contract.

## 6. Promotion condition

To promote this terminal contradiction into a root r=12 proof, one must still audit the upstream implication

\[
\text{E407, h13, maximum Q32}
\Longrightarrow
\text{the frozen V12 29-point / 49-block contract}
\]

for all 554 surviving labelled V12 states, and then combine it with the already audited root reduction eliminating all other T61 branches.

Until that exhaustiveness edge is checked, the correct status is **PROVED_CONDITIONAL E407-Q32 CONTRADICTION**, not an unconditional proof of EG617(r=12).
