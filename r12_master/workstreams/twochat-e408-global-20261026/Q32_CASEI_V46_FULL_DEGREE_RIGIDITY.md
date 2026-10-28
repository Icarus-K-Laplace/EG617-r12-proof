# E408 Q32 — Case-I v=46 degree rigidity after the 131-edge correction

Updated: 2026-10-28  
Status: **PROVED_CONDITIONAL reductions; m=9 branch CLOSED.**

## 1. Contract

Assume Case I of the registered Q32 shell split and `|U|=46`, so `W=H\U={w}`. Let `n=n_w` be the number of exact-129 colors whose Type-I special vertex is w.

`Q32_CASEI_LOW_SUPPORT_MATCHING_EXCLUSION.md` gives

`n>=m-3`, `m in {8,9,10}`.

For an exact color:

- if w is special, the source-correct Type-I degree is `9-a`, `a in {1,2,3,4}`, hence at least5;
- otherwise w lies in an ordinary color K5 and has color degree at least4.

The target residual degree is at least13.

The correct nonexact pointwise floors are now:

- m=8: three 130-edge colors, `L_8=3+3+3=9`;
- m=9: one130-edge plus one131-edge color, **`L_9=3+3=6`**;
- m=10: one132-edge color, `L_10=2`.

The m=9 correction is proved in `Q32_131_MINDEG3_V46_M9_CLOSURE.md`.

Thus at w

`13+(4m+n)+L_m <=60`.                                    (1)

## 2. m=10 is impossible

Case I gives `n>=7`. Equation (1) gives

`13+40+7+2=62>60`.

Hence m=10 is empty.

## 3. m=9 is now impossible, not a surviving equality terminal

Case I gives `n>=6`. With the corrected `L_9=6`, equation (1) gives

`13+36+6+6=61>60`.

Therefore

> **Case I / v=46 / m=9 is CLOSED.**

The older branch-local statement that m=9 survives with `n=6` and a `(130-degree3,131-degree2)` equality profile is superseded and must not be used. Its only error was the obsolete 131-edge degree-two floor; the shell-matching deductions derived after that equality are no longer load-bearing.

## 4. Remaining m=8 branch

For m=8, equation (1) is

`13+32+n+9<=60`,

so `n<=6`. Case I gives `n>=5`. Hence

> **`n in {5,6}`.**

### n=6

Equality holds in every pointwise floor in (1):

- target degree at w is exactly13;
- the six special exact colors have degree exactly5, hence their source parameter is `a=4`;
- the two non-special exact colors have degree exactly4;
- each of the three 130-edge colors has degree exactly3.

By the valid 130-edge equality theorem, w lies in an isolated color-K4 component in each of those three 130-edge colors. The three 3-neighbor sets are pairwise disjoint because an edge has a unique color.

Thus the n=6 terminal carries three pairwise-disjoint nonexact color triples through w, in addition to the exact-color constraints.

### n=5

The lower bounds sum to59, so exactly one unit of total pointwise slack remains.

There are three non-special exact colors. Their multi-outside K5s yield three pairwise-disjoint M-edges. Because every M-edge meets `S=A\B`, `|S|=3`, the three edges form a perfect matching from S to three distinct vertices of B. As in the original argument, none can be triple-shell; hence they are double-shell K5s with shell pairs

`{s_1,b_1},{s_2,b_2},{s_3,b_3}`

for distinct `b_i in B`.

Among the three 130-edge colors, at least two have degree exactly3 at w (only one global slack unit exists). Therefore w lies in at least two isolated nonexact color-K4 components, giving at least two pairwise-disjoint 3-neighbor triples in those colors.

## 5. Current Case-I v=46 frontier

- m=10: CLOSED;
- m=9: CLOSED by the corrected 131-edge minimum-degree theorem;
- m=8: OPEN with the two exact terminals `n=6` and `n=5` above.

This file uses only the 285-edge Q32 contract, source-correct Type-I degrees, valid nonexact minimum-degree/equality facts, and the Case-I shell matching theorem. No 284-edge/Q33 identity or retracted degree9 exceptional-vertex claim is used.
