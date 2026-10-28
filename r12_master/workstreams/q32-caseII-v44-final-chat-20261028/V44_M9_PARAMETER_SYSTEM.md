# E408 Q32 Case-II — v=44,m=9 zero-shell special-edge obstruction

Date: 2026-10-28
Status: **PROVED_CONDITIONAL** under the registered E408-Q32 / source-correct Kang--Pikhurko Type-I contract.

## Frozen inputs

We use only:

- `|H|=47`, `alpha(H)<=4`;
- `O=V(F)\H={p} union A`, with `|A|=13` and `p` target-adjacent to every vertex of `A`;
- `|U|=44`, `W=H\U`, `|W|=3`;
- `m=9` exact-129 colors;
- every exact color has source-correct Type-I form `10 isolated K5 dot-union G11`;
- inside `G11`, the special point is `x_C`, one special 5-part is `N_t`, and `y in N_t`; in the original color graph C, `N_t` is a C-clique and `x_C` is C-adjacent to every vertex of `N_t\{y}`;
- the corrected multiplicity theorem: every `w in W` is special for exactly three exact colors, hence is non-special for exactly six exact colors; for every exact color with `x_C != w`, the point `w` lies in a multi-outside K5 and therefore has at least two distinct C-neighbors in the shell `A`.

No degree-9 exceptional vertex, injectivity, Case-I shell cover, Q33 identity, or E407 identity is used.

## Lemma 1 — zero shell degree forces the pivot edge

Let C be an exact color with `x_C=w in H`. If

`N_C(w) cap A = empty`,

then the edge `pw` has color C.

### Proof

In the source-correct Type-I gadget, `N_t` is a C-colored K5 and `x_C` is C-adjacent to all four vertices of `N_t\{y}`. Hence

`K={x_C} union (N_t\{y})`

is itself a C-colored K5.

A C-colored K5 is target-independent. Since `alpha(H)<=4` and `x_C=w in H`, K cannot be contained in H. Thus at least one vertex of `N_t\{y}` lies in `O={p} union A`.

Every vertex of `N_t\{y}` is C-adjacent to w. Under the hypothesis `N_C(w) cap A=empty`, none of these outside-H vertices can lie in A. Therefore one of them must be p, and hence `pw` is a C-edge. QED.

## Corollary 2 — at most one zero-shell special color at a fixed W-point

Fix `w in W`. The edge `pw` has one unique color in the original edge-coloring. Therefore among all exact colors with `x_C=w`, at most one can satisfy `N_C(w) cap A=empty`.

## Lemma 3 — six non-special exact colors consume at least twelve shell edges

Fix `w in W`. Exactly six exact colors have `x_C != w`.

For each such color C, the corrected multi-outside theorem places w in a C-colored K5 containing at least two shell vertices. Hence w has at least two C-neighbors in A.

For distinct exact colors these shell-neighbor sets are disjoint, because each edge `wa` has a unique color. Consequently the six non-special exact colors occupy at least twelve of the thirteen shell edges from w to A.

Therefore at most one shell edge at w remains available to the three exact colors with `x_C=w`. In particular at least two of those three special exact colors have zero shell degree at w.

## Theorem 4 — v=44,m=9 is impossible

By Corollary 2, at most one special exact color at w can have zero shell degree. By Lemma 3, at least two special exact colors at w must have zero shell degree. Contradiction.

Thus

> **Case II / |U|=44 / m=9 is impossible.**

In fact the proof does not use Case II at all, so it excludes every source-correct Q32 realization with `|U|=44,m=9` once the corrected multiplicity theorem is available.

## Relation to the requested parameter profiles

The later 130-edge minimum-degree-four theorem sharpens the pointwise special-parameter profiles to `(4,4,4)` or `(4,4,3)`. The present contradiction is stronger: it closes the branch before those two profiles need to be distinguished.

## External theorem usage

Only the already source-audited Kang--Pikhurko Type-I equality description is imported. No new external theorem is invoked here.

## Computation

None. The contradiction is a direct edge-ownership argument on the 13 shell edges incident with one W-point.