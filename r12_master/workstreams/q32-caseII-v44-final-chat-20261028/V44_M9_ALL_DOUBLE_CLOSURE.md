# E408 Q32 Case-II — v=44,m=9 all-double closure

Date: 2026-10-28
Status: **CLOSED / PROVED_CONDITIONAL** under the registered source-correct Q32 contract.

Assume `|U|=44`, `m=9`, and all nine exact colors are double type.

Fix any `w in W=H\U`. Exactly six exact colors are non-special at w. In every one of those six colors, w lies in a double-outside K5 and therefore has two distinct shell neighbors. Edge-color uniqueness makes the six shell-neighbor pairs disjoint, so at least twelve of the thirteen edges from w to A are already owned by non-special exact colors.

Hence among the three exact colors with special point `x_C=w`, at most one can have any shell neighbor at w. At least two special exact colors therefore have zero shell degree at w.

For a source-correct Type-I exact color C with `x_C=w`, the five vertices

`{x_C} union (N_t\{y})`

form a C-colored K5. Since `alpha(H)<=4`, this K5 cannot lie wholly in H. If w has no C-neighbor in A, the required outside-H vertex in `N_t\{y}` must be p. Thus `pw` has color C.

The same edge `pw` cannot have two different colors. Therefore two zero-shell special exact colors at w are impossible.

Contradiction. Thus

> **all-double (`t=0`) / `|U|=44` / `m=9` is CLOSED.**

No shell-edge floor `e(M)>=25`, no source parameter profile, and no U-reserve inequality is needed for the contradiction; those remain valid but redundant for this subcase.

External input: only the audited Kang--Pikhurko Type-I factorization. Computation: none.