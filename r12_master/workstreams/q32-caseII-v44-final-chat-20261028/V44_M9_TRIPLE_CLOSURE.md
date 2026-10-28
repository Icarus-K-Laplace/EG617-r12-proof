# E408 Q32 Case-II — v=44,m=9 one-triple closure

Date: 2026-10-28
Status: **CLOSED / PROVED_CONDITIONAL** under the registered source-correct Q32 contract.

Assume `|U|=44`, `m=9`, and there is one triple-type exact color `C_*`.

The general zero-shell obstruction from `V44_M9_PARAMETER_SYSTEM.md` already closes this branch, because at every `w in W` there are six non-special exact colors and each supplies at least two shell neighbors, leaving at most one shell edge for the three special exact colors.

There is also a stronger local count at each `w != x_{C_*}`. The triple color is non-special there and contributes three shell neighbors, while the other five non-special exact colors contribute at least two each. Thus all thirteen shell edges from w to A are already owned by non-special exact colors. Consequently all three special exact colors at w have zero shell degree.

For any such zero-shell special color C, the Type-I clique

`{x_C} union (N_t\{y})`

forces `pw` to have color C, since `alpha(H)<=4` and no C-neighbor of w lies in A. Three distinct exact colors cannot all own the unique edge `pw`.

Contradiction. Hence

> **one-triple (`t=1`) / `|U|=44` / `m=9` is CLOSED.**

This proof is stronger than the previous scalar consequences `e(M)>=28`, `G_A<=4`, and the forced placement of at least two core-excess units on W. Those facts are not needed.

External input: only the audited Kang--Pikhurko Type-I factorization. Computation: none.