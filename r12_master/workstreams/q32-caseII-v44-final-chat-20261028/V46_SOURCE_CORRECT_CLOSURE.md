# E408 Q32 source-correct closure of the support |U|=46

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 285-edge Q32 contract, corrected multiplicity, source-correct Type-I structure, and the named extremal inputs.

## Contract and pointwise bounds

Assume `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`, total core excess six, and `|U|=46`. Then `W={w}`. The number m of exact-129 colors is in {8,9,10}. The corrected multiplicity theorem and the pointwise degree floors give:

- m=8: `n_w in {2,3}` and `L_8=12`;
- m=9: `n_w in {3,4}` and `L_9=7`;
- m=10: `n_w in {4,5}` and `L_10=2`.

Here `n_w` counts exact colors whose special point is w, and `L_m` is the sum of the valid nonexact minimum-degree floors. The source degree is `9-a=4+(5-a)`, with `a in {1,2,3,4}`.

For a special exact color C with no C-neighbor of w in A, the source Type-I K5 argument forces `pw` to have color C. Therefore at most one special exact color can have zero shell degree at w.

Let `h_w` count exact colors with eleven witnesses whose special point is not w. The `m-n_w` non-special exact colors use at least `2(m-n_w)+h_w` of the 13 w-A edges. Hence the number z_w of zero-shell special colors satisfies

`z_w >= 2m - n_w - 13 + h_w`, while `z_w<=1`.

## m=10 is impossible

The only pointwise multiplicities are n_w=4 or5. For n_w=4, `z_w>=3+h_w`; for n_w=5, `z_w>=2+h_w`. Both contradict `z_w<=1`.

## m=9 is impossible

n_w=3 gives `z_w>=2+h_w`, impossible. Thus n_w=4, and the shell inequality forces `h_w=0` and exactly one zero-shell special color.

The pointwise degree sum is tight:

`13 + 9*4 + 4 + 7 = 60`.

So all four special exact colors have a=4 and degree five; the five non-special exact colors have degree four; the nonexact colors have degrees four and three; and the target degree is 13. Since h_w=0, all five non-special exact colors are double type and use exactly ten shell edges. The four special exact colors use the remaining three shell edges: one has zero shell degree and owns `pw`, and the other three each use one shell edge. No target or nonexact color has a w-A edge, and no nonexact color owns `pw`.

Therefore the 130-edge nonexact color has degree four at w and all four neighbors in H. This contradicts `Q32_130_NO_CORE_ONLY_DEG4.md`.

## m=8 is impossible

### If n_w=2

The six non-special exact colors use at least twelve shell edges. If any were eleven-witness type, there would be no shell edge left for either special color, forcing two zero-shell special colors. Thus h_w=0. Exactly one special color has zero shell degree and owns `pw`; the other uses the thirteenth shell edge. No target or nonexact color has a shell edge or owns `pw`.

The pointwise degree floor is `57+A_w`, where `A_w=sum_{x_C=w}(5-a_C)` is either two or three. Thus the three 130-edge colors have degree at least four, with at most one total unit of slack above their three degree-four floors. At least two of them have degree exactly four; because they have no A- or p-neighbor, their four neighbors lie in H. This contradicts `Q32_130_NO_CORE_ONLY_DEG4.md`.

### If n_w=3

All three special parameters are four, so the pointwise degree sum is tight:

`13 + 8*4 + 3 + 12 = 60`.

Five non-special exact colors use at least ten shell edges. The zero-shell bound gives `h_w<=1`. If h_w=0, all three special exact colors use one shell edge each. If h_w=1, exactly one special exact color has zero shell degree and owns `pw`, and the other two use one shell edge each. In either case all thirteen w-A edges are owned by exact colors, so no nonexact color has an A-neighbor at w. All three 130-edge colors have degree four at w; at most one can own `pw`, so at least two have all four neighbors in H. This again contradicts `Q32_130_NO_CORE_ONLY_DEG4.md`.

## Support-46 theorem and scope

All three values m=8,9,10 are excluded. Therefore **the entire Q32 support layer `|U|=46` is CLOSED** under source-correct premises.

This proof does not use exceptional-vertex injectivity or the retracted universal degree-nine claim. It does not close full support `|U|=47`, which is now the remaining Q32 support terminal. The graph-theoretic no-core-only lemma remains conditional on the registered full-residual bounds `alpha(D)<=12`, `omega(D)<=5` for the 130-edge color.
