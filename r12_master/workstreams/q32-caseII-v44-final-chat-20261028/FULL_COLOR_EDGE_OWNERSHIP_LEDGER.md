# E408 Q32 Case-II v=44 — full-color edge-ownership ledger

Date: 2026-10-28
Status: **m=9 CLOSED; m=8 CLOSED. Therefore the entire Case-II |U|=44 layer is CLOSED (m=10 was inherited closed).**

This ledger records the source-correct ownership mechanisms that actually carry the closure.

## A. Common contract

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`, and total target core excess is six.

`U` is the registered support of core-four witnesses coming from the twelve Type-I factor K5s of exact-129 colors. Here `|U|=44`, so `W=H\U` has three vertices. The shell is `A=N_F(p)`, `|A|=13`, and `O={p} union A`.

Every edge has a unique color.

For an exact color C with `x_C=w in H`, source Type-I gives the C-clique

`{x_C} union (N_t\{y})`.

If w has no C-neighbor in A, this K5 cannot lie wholly in H because `alpha(H)<=4`; its outside vertex must therefore be p. Hence pw has color C.

> **Zero-shell special-edge obstruction:** at a fixed W-point, at most one special exact color can have zero shell degree.

## B. m=9 ownership closure

Corrected multiplicity gives exactly three special and six non-special exact colors at every W-point.

Each non-special exact color owns at least two shell edges, so the six non-special colors own at least twelve of the thirteen shell edges. Therefore at least two of the three special exact colors have zero shell degree.

The zero-shell obstruction allows at most one.

Contradiction.

Thus both m=9 branches are closed:

- all-double `t=0`;
- one-triple `t=1`.

The earlier scalar shell floors and `(4,4,4)/(4,4,3)` parameter list are valid but no longer load-bearing.

## C. m=8 pointwise ownership normal form

The pointwise floor is

`target13 + exact32 + nonexact12 =57`,

so only three slack units remain.

For every W-point `n_w in {2,3}`, and the only multiplicity partitions are

`(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

At n=2:

- special parameters are `(4,4)` or `(4,3)`;
- six non-special exact colors own exactly twelve shell edges;
- one special exact color owns the thirteenth shell edge;
- the other special exact color has zero shell degree and owns pw;
- target and all nonexact colors own no edge from w to O;
- at least two of the three nonexact colors are degree4 and core-only.

At n=3:

- special parameters are `(4,4,4)`;
- all three nonexact colors have degree4;
- exact colors own at least thirteen of the fourteen edges from w to O, so at least two nonexact colors are core-only.

## D. 130-edge local and pair rigidity

For a 130-edge nonexact color D, if `w in W` has degree4 and all four D-neighbors in H, then the four-neighbor set induces

`K4-e`

in D. The unique missing pair is a target edge.

The stronger pair theorem `V44_M8_PAIR_RIGIDITY.md` says:

> if two W-points u,v are both degree4/core-only in the same 130-edge color D, then uv must have color D.

The proof uses the exact 119-edge anti-neighborhood equality and Kang--Pikhurko equality classification at `(56,11)`.

Define

`L(w)={D among the three 130-edge colors: d_D(w)=4 and N_D(w) subset H}`.

Every W-point satisfies `|L(w)|>=2`. Therefore any pair of W-points has a common D in its two L-sets, and pair rigidity forces their edge to be nonexact.

> **All three W--W edges are nonexact in every m=8 multiplicity partition.**

## E. Immediate closure of (2,2,2) and (3,2,2)

If an exact color has its special point outside W, then it must own a W--W edge:

- if the special point is in O, all three W-points lie in the unique double-outside factor;
- if the special point is in U, the three W-points occupy two multi-outside factors, so two share a factor.

The partition `(2,2,2)` has two exact colors special outside W, and `(3,2,2)` has one.

Both contradict the fact that every W--W edge is already nonexact.

## F. Final (3,3,2) ownership collapse

All exact special points now lie on W.

The unique n=2 point cannot have profile `(4,3)`, because then its L-set has size3 and would intersect an n=3 L-set in at least two colors, assigning two colors to one W--W edge. Therefore it has `(4,4)` and `|L|=2`.

The same edge-uniqueness argument gives `|L|=2` at both n=3 points. It follows that every W-point has core excess exactly one. Since all W--W edges are nonexact,

`E_U=3`, `e_H(W)=0`,

and therefore

`e(bar(H[U]))=703-3=700`.

Every exact color has source parameter `a=4`. Its two non-special W-points have degree4 in that exact color, hence lie in two distinct isolated double-outside K5 factors. The special gadget factors `N_s,N_t` are single-outside.

Inside U, each exact color owns at least

- 60 edges from ten single-outside witness K4s;
- 2 edges from the U-pairs in the two isolated double factors;
- 3 cross-gadget edges `y--P` because `y in U` and at least three vertices of the four-set P lie in U.

Thus

`e_C(U)>=65`.

Eight exact colors use at least520 U-edges. Three nonexact colors use at least `3*60=180`. This exactly saturates the 700-edge complement pool.

Hence every nonexact color has exactly60 U-edges, so Turan equality gives

`D[U]=8K4 dot-union 4K3`.

But each nonexact color occurs in exactly two W L-sets. The corresponding two W-points form the central pair in a local D-colored `K5-e`; among the other three vertices are U-points c,a,b with

`ca,cb in E(D)` and `ab notin E(D)`.

That cannot occur in a disjoint union of clique components.

Contradiction.

Thus `(3,3,2)` is closed.

## G. Final v=44 ownership verdict

- m=10: inherited CLOSED by corrected support multiplicity;
- m=9: CLOSED by the zero-shell special-edge obstruction;
- m=8: CLOSED by 130-color pair rigidity plus U-pool saturation.

Therefore

> **Case II / |U|=44 is CLOSED for every m in {8,9,10}.**

Since inherited Case I already closes `|U|=44`, the whole Q32 support layer `|U|=44` is removed from the global frontier.

## H. External theorem / verifier scope

External ingredients used by the m=8 pair step:

- Kang--Pikhurko Theorems 1 and4 at `(56,11)`;
- the source-audited exact-129 Type-I construction;
- the inherited 130-edge minimum-degree-four theorem;
- ordinary Turan equality on44 vertices.

`verify_v44_m8_closure_arithmetic.py` checks only finite arithmetic and the three-color L-set combinatorics. It does not verify the external theorems or the analytic graph lemmas.