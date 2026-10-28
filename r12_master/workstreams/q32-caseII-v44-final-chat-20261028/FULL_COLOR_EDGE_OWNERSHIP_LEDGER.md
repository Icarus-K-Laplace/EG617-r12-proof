# E408 Q32 Case-II v=44 — full-color edge-ownership ledger

Date: 2026-10-28
Status: **m=9 CLOSED; m=8 reduced but OPEN.**

This ledger records only source-correct consequences. It deliberately separates proved graph constraints from weaker scalar/CSP relaxations.

## A. Common notation

`H` is the 47-point core, `U` the registered exact-color witness support, `W=H\U`, and here `|U|=44`, `|W|=3`. The shell is `A=N_F(p)`, `|A|=13`, and `O={p} union A`.

Every edge has one color. In particular, at a fixed W-point, shell-neighbour sets belonging to distinct colors are disjoint.

For an exact color C with `x_C=w in H`, source Type-I gives the C-clique

`{x_C} union (N_t\{y})`.

Because `alpha(H)<=4`, if w has no C-neighbour in A, that clique must use p; hence `pw` has color C. Therefore:

> at a fixed W-point, at most one special exact color can have zero shell degree.

This is the zero-shell special-edge obstruction.

## B. m=9 ledger — closed

At every `w in W`, corrected multiplicity gives exactly three special and six non-special exact colors.

Each non-special exact color owns at least two shell edges at w. Thus at least 12 of the 13 shell edges are already owned by the six non-special exact colors. At least two of the three special colors have zero shell degree, contradicting the zero-shell special-edge obstruction.

Hence both the all-double and one-triple m=9 branches are impossible.

## C. m=8 pointwise normal form

The pointwise baseline is

`target 13 + exact 8*4 + nonexact 3*4 =57`,

so only three slack units exist at every residual point.

At each `w in W`, `n_w in {2,3}`, and the only sorted multiplicity partitions are

`(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

- `n=3`: special parameters are exactly `(4,4,4)`; target degree is13; all five non-special exact colors and all three nonexact colors have degree4; `epsilon_w+r_A(w)=1`.
- `n=2`: special parameters are `(4,4)` or `(4,3)`.

At an n=2 point, six non-special exact colors consume at least12 shell edges. At least one of the two special colors must use a shell edge, while at most one may have zero shell degree. Therefore equality holds throughout:

- each of the six non-special exact colors owns exactly two shell edges;
- one special exact color owns exactly one shell edge;
- the other special exact color owns zero shell edges and therefore owns `pw`;
- target and all three nonexact colors own no edge from w to A;
- `epsilon_w>=1`.

For profile `(4,3)`, all pointwise slack is consumed by the two special exact colors, so `epsilon_w=1`, all six non-special exact colors have degree4, and all three nonexact colors have degree4.

## D. New 130-edge degree-four local rigidity at an n=2 point

Let D be one of the 130-edge nonexact colors, and suppose `w` is an n=2 W-point at which `d_D(w)=4`.

Since all 13 shell edges at w and the edge pw are exact-colored, all four D-neighbours of w lie in H. Write

`S=N_D(w)`, `|S|=4`,

and let N be the 56 D-nonneighbours of w among the remaining 60 vertices.

### D.1 Lower bound inside N

Because w is D-nonadjacent to every vertex of N, `alpha(D[N])<=11`; otherwise an independent12-set in D[N] together with w would give an independent13-set in D. Also `omega(D[N])<=5`.

Put `J=bar(D[N])`. Then J is K12-free and cannot be 11-partite: an 11-partition of J would cover N by eleven D-cliques, each of size at most5, hence at most55 vertices.

For `(n,r)=(56,11)`, Kang--Pikhurko Theorem1 gives

`p_11(56)=t_11(56)-floor(56/11)+1`.

Here the balanced 11-partite Turan graph has part sizes `6,5^10`, so

`t_11(56)=C(56,2)-[C(6,2)+10*C(5,2)]`

`=1540-(15+100)=1425`,

and hence

`p_11(56)=1425-5+1=1421`.

Therefore

`e(D[N]) >= C(56,2)-1421 =119`.

### D.2 Exact neighbourhood structure

Write

`a=e_D(S)`, `b=e_D(S,N)`.

The total edge count 130 gives

`4+e(D[N])+a+b=130`,

so `a+b<=7`.

Every vertex of S has D-degree at least4 by the 130-edge minimum-degree theorem. Each already has the edge to w, hence

`2a+b >= 4*3 =12`.

If `a=6`, then S is a D-colored K4 and `{w} union S` is a D-colored K5 wholly inside H, contradicting `alpha(H)<=4`. Thus `a<=5`.

Combining

`a+b<=7`, `2a+b>=12`, `a<=5`

forces equality:

> `a=5`, `b=2`, `e(D[N])=119`.

Moreover `2a+b=12`, so every vertex of S has exactly three D-neighbours in `S union N` in addition to w. Hence:

- `D[S]=K4-e` for one missing pair `{u,v}`;
- u and v each have exactly one D-edge into N;
- the other two vertices of S have no D-edge into N.

Finally the missing pair uv must be a target edge. If uv had any non-target color, then every pair in `{w} union S` would be a target non-edge: wS are D-edges, five pairs of S are D-edges, and uv would also be non-target. This would be a target-independent 5-set in H, again contradicting `alpha(H)<=4`.

Therefore:

> **Every degree-four 130-color at an n=2 W-point has a four-neighbour set inducing `K4-e` in that nonexact color, with the unique missing edge forced to be a target edge.**

For an n=2 `(4,3)` point this applies simultaneously to all three 130-edge colors. Their four-neighbour sets are pairwise disjoint (the twelve incident edges at w have different color ownership), so the local core contains three disjoint target edges, one forced inside each four-set.

For an n=2 `(4,4)` point there is only one unused slack unit. Hence at least two of the three nonexact colors still have degree exactly4 and satisfy this rigidity theorem.

## E. Exact-color special-location geometry for m=8

Let an exact color C have its special point outside W.

### E.1 Special point outside H

If `x_C in O`, the twelve factor K5s contain the remaining 13 outside-H vertices. Since every factor K5 must meet O, exactly one factor K5 is double-outside and the other eleven are single-outside.

Every W-point is non-special for C, hence must lie in the unique multi-outside factor K5. Its core capacity is exactly three vertices, so that factor contains all three W-points. Therefore C colors all three W--W edges.

Consequently at most one exact color can have its special point outside H.

### E.2 Special point in U

If `x_C in U`, all three W-points are non-special. A triple-type H-special color has only one multi-outside K5 and that triple-outside K5 has only two core slots, so it cannot accommodate all three W-points. Therefore an exact color special in U must be double type.

Its two double-outside K5s must cover all three W-points, so at least two W-points lie in the same double-outside K5. Hence C owns at least one W--W edge.

### E.3 Consequences for multiplicity partitions

Let `S=sum_W n_w` be the number of exact colors special on W.

- `(2,2,2)`: S=6, so two exact colors are special outside W. They cannot include an outside-H special color, because such a color would own all three W--W edges while the other outside-W color (necessarily U-special double type) must own at least one W--W edge. Thus both are U-special double types, and they must own distinct W--W edges.
- `(3,2,2)`: S=7, so one exact color is special outside W. It is either U-special double type (owns at least one W--W edge) or outside-H special (owns all three W--W edges).
- `(3,3,2)`: S=8, so every exact color is special on W. Any H-special triple-type color must be special at the unique n=2 W-point; moreover there can be at most one such triple color, because two would both place the other two W-points in their unique triple-outside K5 and would both try to own the same W--W edge.

## F. Shell-factor relaxation is feasible — no false UNSAT claim

The n=2 shell conditions alone do **not** close m=8. In particular, for the `(2,2,2)` partition one can assign the six non-special colors at each W-point to six pairwise-disjoint shell pairs, respecting:

- at most two double-outside factor pairs per H-special double color;
- repeated use of the same pair only by the same color;
- pairwise disjointness of the two factor pairs of one color;
- W--W edge ownership when two W-points lie in the same factor K5;
- two U-special colors using distinct W--W edges.

Thus a scalar/matching-only SAT relaxation is satisfiable. Any m=8 closure must use additional graph structure: the 130-edge degree-four rigidity above, the 285-edge six-excess core, stronger U-reserve structure, or the outer seven-block completion system.

No abstract shell assignment is promoted to a graph realization.

## G. Outer seven-block interface

The proved E408 equality system gives, for every non-target color C,

`P_C+R_C+s_C=62`.

Every exact129 color has `s_C=0`, and the proved exact blocker theorem gives `R_C>=7`, hence `P_C<=55`.

For m=8 these constraints remain necessary but, by themselves, do not contradict the local m=8 normal forms. No seven-block UNSAT claim is made without a complete completion argument.

## H. External theorem usage / computation scope

External theorem used in Section D: Kang--Pikhurko Theorem1 at `(56,11)`; its arithmetic is shown explicitly. The previously proved 130-edge `delta>=4` theorem is also used.

A finite arithmetic check confirms the only m=8 multiplicity partitions are `(2,2,2),(3,2,2),(3,3,2)`. An abstract shell-pair backtracking check found feasible assignments for the scalar/factor-level `(2,2,2)` relaxation. This check is **not** a graph existence verifier and is used only to prevent an invalid scalar UNSAT claim.