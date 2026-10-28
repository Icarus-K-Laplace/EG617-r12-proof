# E408 Q32 source-correct closure of the support |U|=45

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 285-edge Q32 contract, the corrected non-full-support multiplicity theorem, the audited Type-I factorization, and the named extremal inputs.

## Contract

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`, and `sum_H(d_H-12)=6`. Let `|U|=45` and `W=H\\U={w1,w2}`. The shell is `A`, `|A|=13`, and `O={p} union A`; `p-w` is not target-colored for `w in H`. There are `m in {8,9,10}` exact-129 non-target colors. For each exact color C, its source parameter is `a_C in {1,2,3,4}` and the special vertex has degree `9-a_C`.

The corrected multiplicity theorem gives `n_w>=m-6`, where `n_w` is the number of exact colors with special point `x_C=w`. A non-special exact color has degree at least four at w and at least two shell neighbors; if it has eleven single-outside witnesses, it has three shell neighbors. A special exact color contributes degree `4+(5-a_C)`.

The valid nonexact degree-floor sums are:

| m | nonexact edge counts | pointwise floor L_m |
|---:|---|---:|
| 8 | 130,130,130 | 12 |
| 9 | 130,131 | 7 |
| 10 | 132 | 2 |

Here the 130-edge color has minimum degree four, the 131-edge color minimum degree three, and the 132-edge color has the registered floor two. In particular `L_9=7`, not the stale upstream value six.

## Pointwise source-parameter normal form

For `A_w=sum_{x_C=w}(5-a_C)`, the 60 incident edges at w give

`60 >= 13 + 4m + A_w + L_m`.

Hence `A_w<=3,4,5` for `m=8,9,10`, respectively. Since every special incidence contributes at least one, combining with `n_w>=m-6` yields:

- `m=8`: `n_w in {2,3}`; if `n_w=2`, the parameter profile is `(4,4)` or `(4,3)`; if `n_w=3`, it is `(4,4,4)`.
- `m=9`: `n_w in {3,4}`; if `n_w=3`, the profile is `(4,4,4)` or `(4,4,3)`; if `n_w=4`, all four parameters are four.
- `m=10`: `n_w in {4,5}`; if `n_w=4`, the profile is all four or one parameter is three; if `n_w=5`, all five parameters are four.

## Zero-shell obstruction and shell count

For a source-correct Type-I exact color C with `x_C=w in H`, if w has no C-neighbor in A, then `{x_C} union (N_t minus {y})` is a C-colored K5. It cannot lie wholly in H, so one of its vertices must be outside H; since w has no C-neighbor in A, that vertex must be p. Thus `pw` has color C. Consequently, at a fixed w at most one special exact color can have zero shell degree.

Let `h_w` be the number of exact colors with eleven single-outside witnesses whose special point is not w. The `m-n_w` non-special exact colors consume at least `2(m-n_w)+h_w` of the thirteen w-A edges. Thus the number of zero-shell special colors is at least

`z_w >= 2m - n_w - 13 + h_w`.

Since `z_w<=1`, the m-subcases reduce as follows:

- `m=10`: `n_w=4` gives `z_w>=3+h_w`; `n_w=5` gives `z_w>=2+h_w`. Both contradict `z_w<=1`. Thus m=10 is impossible.
- `m=9`: `n_w=3` gives `z_w>=2+h_w`, impossible. Therefore `n_w=4` at both W-points, and `h_w=0` at both. No exact color can then have eleven witnesses: any such color would be non-special at at least one W-point. Hence all nine exact colors have ten witnesses.
- `m=8`: `n_w` is two or three. At `n_w=2`, `h_w=0`; at `n_w=3`, `h_w<=1`.

## Close m=9

For `m=9`, each W-point has four special exact colors, all with `a=4`, and the pointwise degree lower bound is tight:

`13 + 9*4 + 4 + 7 = 60`.

Therefore target degree is exactly 13, all non-special exact colors have degree four, the two nonexact colors have degrees four and three, and all exact colors are ten-witness/double type. At each w, five non-special exact colors use exactly ten shell edges. Exactly one special exact color has zero shell degree and owns `pw`; the other three special exact colors each use one shell edge. No target or nonexact color has a w-A edge, and no nonexact color owns `pw`. Thus the 130-edge color D has degree four and all neighbors in H at both w1 and w2.

This contradicts `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`, which proves that a 130-edge color cannot have two distinct degree-four vertices whose neighbors all lie in H. Therefore `|U|=45,m=9` is impossible.

## Close m=8

Let `L(w)` be the set of the three 130-edge nonexact colors D for which `d_D(w)=4` and all D-neighbors of w lie in H. We show `|L(w)|>=2` at each W-point.

If `n_w=2`, the six non-special exact colors use at least twelve shell edges. A triple-type non-special color would leave no shell edge for the two special colors, forcing two zero-shell specials, impossible. Hence the non-special colors are all double type. Exactly one special color is zero-shell and owns `pw`; the other special color uses the thirteenth shell edge. No target or nonexact color has a shell edge at w, and the nonexact colors do not own `pw`. The pointwise floor leaves at most one degree unit above the three 130-edge minima, so at least two nonexact colors have degree four and are core-only. Thus `|L(w)|>=2`.

If `n_w=3`, all three special parameters are four and the pointwise degree floor is tight. Five non-special exact colors use at least ten shell edges; the zero-shell bound forces `h_w<=1`. If `h_w=0`, all three special colors use one shell edge each; if `h_w=1`, exactly one special color is zero-shell and owns `pw`, while the other two use one shell edge each. In either case no target or nonexact color has a w-A edge. All three nonexact colors have degree four; at most one can own `pw`, so at least two are core-only degree four. Again `|L(w)|>=2`.

Both `L(w1)` and `L(w2)` are subsets of the same three 130-edge colors and each has size at least two. Their intersection is nonempty, giving a 130-edge color with two distinct core-only degree-four vertices. This contradicts `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`. Hence `|U|=45,m=8` is impossible.

## Support-45 theorem and firewall

The cases `m=8,9,10` are all excluded, so **the entire Q32 support layer `|U|=45` is CLOSED** under the registered contract.

This proof does not use exceptional-vertex injectivity or the retracted universal degree-nine assertion. It does not import the old `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` proof, which depends on that retracted injectivity claim. It does not certify the higher-support cases `|U|=46,47` or EG617(r=12) as a whole.
