# E408 Q32 Case-II — v=44,m=8 normal form

Date: 2026-10-28
Status: **PROVED_CONDITIONAL normal form; m=8 is now CLOSED by `V44_M8_PAIR_RIGIDITY.md` + `V44_M8_CLOSURE.md`.**

## Frozen inputs

Work under the registered E408-Q32 contract with `|U|=44`, `W=H\U`, `|W|=3`, and `m=8` exact-129 colors.

Inputs used here:

- target residual minimum degree at least13;
- exact colors have pointwise degree at least4;
- all three nonexact colors have130 edges and minimum degree at least4;
- corrected multiplicity `n_w>=m-6=2` for `w in W`;
- source-correct Type-I special excess `5-a_C`, `a_C in {1,2,3,4}`;
- zero-shell special-edge obstruction: if `x_C=w in H` and w has no C-neighbor in A, then pw has color C, so at most one special exact color at a fixed w can have zero shell degree;
- every exact color non-special at w gives at least two shell neighbors at w.

No degree-9 exceptional point, exceptional injectivity, Case-I shell cover, Q33 identity, or E407 identity is used.

## Pointwise slack and multiplicity partitions

At every residual point,

`target 13 + eight exact 8*4 + three nonexact 3*4 =57`,

so only three pointwise slack units remain.

Each special exact incidence contributes at least one slack unit. Hence for every `w in W`,

`2<=n_w<=3`.

Since there are only eight exact special labels in total,

`sum_W n_w<=8`.

Up to permutation, the only multiplicity partitions are

> `(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

## n=3 normal form

If `n_w=3`, all slack is consumed by the three special incidences. Therefore

- special parameters are exactly `(4,4,4)`;
- target degree is exactly13;
- every non-special exact color has degree4;
- all three nonexact colors have degree4;
- with `epsilon_w=d_H(w)-12` and `r_A(w)=d_F(w,A)`, one has

`epsilon_w+r_A(w)=1`.

Five non-special exact colors own at least ten shell edges. At most one of the three special colors can have zero shell degree, so at least two special colors own shell edges. Thus exact colors own at least twelve shell edges.

## n=2 normal form

If `n_w=2`, the special parameter pair is only

> `(4,4)` or `(4,3)`.

The six non-special exact colors own at least twelve shell edges. At most one special color can have zero shell degree, so at least one special color owns a shell edge. Equality is therefore forced on all thirteen shell edges:

1. every non-special exact color owns exactly two shell edges;
2. exactly one special exact color owns exactly one shell edge;
3. the other special exact color owns zero shell edges and therefore owns pw;
4. target and nonexact colors own no w--A edge;
5. `r_A(w)=0` and `epsilon_w>=1`.

For profile `(4,3)`, all slack is already consumed, so `epsilon_w=1` and all three nonexact colors have degree4. For `(4,4)`, exactly one slack unit remains outside the special exact colors.

A non-special exact color cannot be triple-outside at an n=2 point: three shell edges from that color plus at least two from each of the other five non-special exact colors would consume all thirteen shell edges before either special color, forcing two zero-shell special colors.

## Closure interface

The normal form above is not itself the final contradiction. The closure proceeds through two further theorems:

1. `V44_M8_PAIR_RIGIDITY.md`: if a 130-edge nonexact color D is degree4 and core-only at two W-points, then their W--W edge must have color D.
2. `V44_M8_CLOSURE.md`: every W-point has at least two such nonexact colors. Therefore all three W--W edges are nonexact. This immediately kills `(2,2,2)` and `(3,2,2)` because an exact color special outside W must own a W--W edge. The remaining `(3,3,2)` branch collapses to all exact colors having `a=4`, all exact colors double type, `E_U=3`, `e_H(W)=0`, and `e(bar(H[U]))=700`. Each exact color then uses at least65 U-edges, so the three nonexact colors are forced to the 60-edge Turan equality structure `8K4 dot-union 4K3`, incompatible with their local `K5-e` W-pair rigidity cluster.

Hence

> **Case II / |U|=44 / m=8 is impossible.**

## Verification scope

`verify_v44_m8_closure_arithmetic.py` checks the finite multiplicity enumeration, the `(56,11)` arithmetic, the unique `(a,b)=(5,2)` local count, the three-color L-set combinatorics, and the final 700-edge saturation arithmetic. It does not verify the external extremal theorems or analytic graph lemmas.