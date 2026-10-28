# E408 Q32 / |U|=44, m=8 — direct no-core-only-degree-four closure

Date: 2026-10-28  
Status: **CLOSED / PROVED_CONDITIONAL** under the frozen Q32 contract, corrected multiplicity theorem, source-correct Type-I factorization, and `Q32_130_NO_CORE_ONLY_DEG4.md`.

## 1. Result

Assume `|U|=44`, `W=H\\U` has three vertices, and there are eight exact-129 colors. Then every `w in W` must lie in at least two distinct 130-edge nonexact colors D for which

`d_D(w)=4` and `N_D(w) subset H`.

But the source-correct theorem `Q32_130_NO_CORE_ONLY_DEG4.md` proves that no such vertex exists for any 130-edge nonexact color. Contradiction.

This is a shorter closure than the W-pair-rigidity / 700-edge U-pool proof in `V44_M8_CLOSURE.md`. The older proof remains an independent cross-check.

## 2. Pointwise budget

At every residual point w, the registered lower bounds are:

- target-color degree at least 13;
- degree at least 4 in each of eight exact-129 colors;
- degree at least 4 in each of three 130-edge nonexact colors.

Thus the baseline is

`13 + 8*4 + 3*4 = 57`.

The residual graph has degree 60 at every vertex, so the total pointwise surplus is at most three. A special exact incidence with source parameter a has degree `9-a = 4+(5-a)`, costing at least one surplus unit. Corrected multiplicity gives `n_w >= 8-6=2`; hence `n_w in {2,3}`.

## 3. Case n_w=2

The two special exact parameters, sorted, must be `(4,4)` or `(4,3)), because their total surplus is at most three.

The six non-special exact colors each use at least two distinct w--A edges. They therefore occupy at least twelve of the thirteen shell edges. At most one shell edge remains for the two special exact colors. The zero-shell lemma says at most one special exact color can have zero shell degree, since every zero-shell special color forces the unique edge pw to have its color.

Consequently the shell allocation is exact:

- each of the six non-special exact colors uses exactly two w--A edges;
- one special exact color uses exactly one w--A edge;
- the other special exact color uses zero w--A edges and owns pw;
- all thirteen w--A edges and pw are exact-colored;
- neither the target color nor any nonexact color has a neighbor of w in O={p} union A.

If the special profile is (4,3), the two special excesses are 1+2=3 and consume all pointwise surplus, so all three nonexact colors have degree exactly four. If the profile is (4,4), the special excess is 1+1=2, leaving at most one surplus unit, so at most one nonexact color can have degree greater than four.

In either profile, at least two of the three nonexact colors have degree four. Since none has a neighbor in O, all four neighbors of each such color lie in H. Thus at every n_w=2 point,

> `|L(w)| >= 2`,

where `L(w)={D among the three nonexact colors: d_D(w)=4 and N_D(w) subset H}`.

## 4. Case n_w=3

The three special exact incidences each cost at least one surplus unit. They exhaust the three-unit budget, forcing all special parameters to equal four. Therefore:

- target degree at w is exactly 13;
- all five non-special exact colors have degree exactly four;
- all three nonexact colors have degree exactly four.

The five non-special exact colors use at least ten w--A edges. At most one of the three special exact colors can have zero shell degree, so at least two special colors use shell edges. Exact colors consequently own at least twelve of the thirteen w--A edges.

If a special exact color has zero shell degree, it owns pw, so exact colors own at least thirteen of the fourteen w--O edges. If none has zero shell degree, all three special colors use shell edges, so exact colors own all thirteen w--A edges. In either case at most one edge from w to O can be owned by a nonexact color.

All three nonexact colors have degree four. Since at most one of them can have an O-neighbor, at least two have all four neighbors in H. Hence again

> `|L(w)| >= 2`.

## 5. Contradiction with the direct 130-edge local theorem

The local theorem `Q32_130_NO_CORE_ONLY_DEG4.md` states:

> If D is a 130-edge non-target color on the 61-point residual with `alpha(D)<=12`, `omega(D)<=5`, and `delta(D)>=4`, then no vertex w in H can satisfy `d_D(w)=4` with all four D-neighbors in H.

Its proof is analytic: the (56,11) Kang–Pikhurko bound gives at least119 D-edges in the non-neighborhood of a degree-four vertex. For a core-only vertex, the local edge budget and `alpha(H)<=4` force its neighbor graph to be `K4-e`, with exactly two external edges attached to the two missing-edge endpoints. An endpoint then has a four-neighbor graph consisting of a triangle plus an isolated vertex (three edges), contradicting the same 119-edge bound, which requires at least five edges in every degree-four neighborhood.

In the m=8 branch all three nonexact colors have exactly130 edges and minimum degree at least four, so the theorem applies to every member of L(w). But Sections 3–4 give `|L(w)|>=2` for each of the three W-points. This is impossible.

Therefore

> **E408-Q32 / `|U|=44,m=8` is CLOSED.**

The proof uses no W-pair rigidity, no 700-edge U-pool saturation, no exceptional-vertex injectivity, and no retracted universal degree-nine premise. The explicit external extremal input is Kang–Pikhurko Theorem 1 at (56,11), plus the already registered 130-edge minimum-degree-four theorem.

## 6. Scope firewall

This closes the v=44 support layer, not the entire E408-Q32 terminal. The separate m=9 proof is `V44_M9_PARAMETER_SYSTEM.md`; m=10 is excluded by the corrected multiplicity theorem. Full support `|U|=47` remains open elsewhere in the project. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
