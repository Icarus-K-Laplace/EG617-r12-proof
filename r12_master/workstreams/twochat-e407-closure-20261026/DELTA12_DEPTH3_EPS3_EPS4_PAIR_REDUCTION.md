# E407 Q32 — delta=12 depth-3 epsilon_U=3,4 exceptional-pair reduction

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL strict reduction** under the registered balanced 309-edge Kang–Pikhurko equality model for the depth-3 augmentation branch and the recorded W-profile classification. This does not close epsilon_U=3 or 4, E407 Q32, or EG617(r=12).

## 1. Frozen depth-3 equality interface

Use the registered 309-edge equality model on U. Its exceptional pair is x,y, with restored-edge incidence counts I_x,I_y. The exact degree identity is
\[
d_W(x)+d_W(y)=5+\epsilon_x+\epsilon_y-I_x-I_y.
\tag{1.1}
\]
For epsilon_U>=1 the delta=12 low-W-degree lemma gives
\[
d_W(x),d_W(y)\ge3.
\tag{1.2}
\]
In the equality graph xy is a target nonedge; it becomes a target edge exactly when xy is one of the three restored target edges.

For epsilon_U=3 the recorded W profiles are:
- K3 dotcup K5 dotcup K5 dotcup K5, q=0;
- K4 dotcup K4 dotcup K4 dotcup K6, q=0;
- base (4,4,5,5) with one W-cross edge, q=1.

For epsilon_U=4 the only W profile is
\[
K4\dot\cup K4\dot\cup K5\dot\cup K5,
\tag{1.3}
\]
with q=0.

## 2. Pair-cover lemma when xy is not restored

Assume xy is not restored, so x,y are H-nonadjacent. Their common W-nonneighbours contain no independent triple, otherwise that triple together with x,y would be an independent 5-set in H.

For a q=0 four-clique W profile this means the common W-nonneighbour set meets at most two clique components. Equivalently
\[
N_W(x)\cup N_W(y)
\]
fully covers at least two W-components.

For the epsilon_U=3 q=1 profile (4,4,5,5)+one cross edge, the one-defect pair rule from `DELTA12_DEPTH2_EPS3_Q1_CLOSURE.md` says that if a nonadjacent core pair does not fully cover two base components, then its W-neighbourhood union has size at least 11. Since (1.1) gives at most 8 at epsilon_U=3, the defect escape is unavailable. Thus the same ordinary two-component cover conclusion holds in all epsilon_U=3 profiles.

The minimum size of two W-components is 8 in every epsilon_U=3 or 4 profile. Therefore
\[
|N_W(x)\cup N_W(y)|\ge8.
\tag{2.1}
\]

## 3. epsilon_U=3: exact exceptional-pair split

### Case 3A — xy is not restored

By (1.1),
\[
d_W(x)+d_W(y)\le8.
\]
Together with (2.1),
\[
8\le |N_W(x)\cup N_W(y)|\le d_W(x)+d_W(y)\le8.
\]
Hence equality holds throughout:
\[
\boxed{d_W(x)+d_W(y)=8,\quad N_W(x)\cap N_W(y)=\varnothing.}
\tag{3.1}
\]
Substituting into (1.1),
\[
8=5+\epsilon_x+\epsilon_y-I_x-I_y.
\]
Since \(\epsilon_x+\epsilon_y\le\epsilon_U=3\) and the incidence counts are nonnegative,
\[
\boxed{\epsilon_x+\epsilon_y=3,\qquad I_x=I_y=0.}
\tag{3.2}
\]
Thus all U-excess is concentrated on x,y, and all three restored target edges avoid x and y.

The union in (3.1) is exactly a minimum two-component cover. Therefore, up to component permutation,
- in K3+K5+K5+K5 it is K3 together with one K5;
- in K4+K4+K4+K6 it is two K4s;
- in the q=1 (4,4,5,5) profile it is the two K4 base parts.

### Case 3B — xy is restored

The restored edge xy contributes one restored incidence at each endpoint, so
\[
I_x+I_y\ge2.
\]
Equation (1.1) and epsilon_U=3 give
\[
d_W(x)+d_W(y)\le5+3-2=6.
\]
By (1.2) the sum is at least 6. Thus
\[
\boxed{d_W(x)=d_W(y)=3.}
\tag{3.3}
\]
Equality in (1.1) forces
\[
\boxed{\epsilon_x+\epsilon_y=3,\qquad I_x+I_y=2.}
\tag{3.4}
\]
The edge xy itself already accounts for these two incidences, hence
\[
\boxed{I_x=I_y=1,}
\tag{3.5}
\]
and the other two restored target edges avoid x and y. Again all U-excess lies on the exceptional pair.

Therefore epsilon_U=3 is reduced to exactly two exceptional-pair kernels: the nonrestored disjoint 8-cover case (3A), or the restored (3,3)-degree case (3B).

## 4. epsilon_U=4: exact arithmetic kernels

Now H[W]=K4+K4+K5+K5.

### Case 4A — xy is not restored

The pair-cover lemma gives union size at least 8, while (1.1) gives degree sum at most 9. Hence
\[
d_W(x)+d_W(y)\in\{8,9\}.
\]
If the sum is 8, then
\[
\epsilon_x+\epsilon_y-(I_x+I_y)=3,
\]
so the only possibilities are
\[
\boxed{(\epsilon_x+\epsilon_y,I_x+I_y)\in\{(3,0),(4,1)\}.}
\tag{4.1}
\]
Moreover the union has size exactly 8, the two neighborhoods are disjoint, and their union is exactly the two K4 components.

If the sum is 9, then
\[
\boxed{\epsilon_x+\epsilon_y=4,\qquad I_x=I_y=0.}
\tag{4.2}
\]
Thus all U-excess lies on x,y and all restored edges avoid them. The union has size 8 or 9; if 8, the neighborhoods overlap in exactly one point and cover the two K4s, while if 9 they are disjoint and cover either K4+K5 or the two K4s plus one additional W point.

### Case 4B — xy is restored

Now I_x+I_y>=2 and (1.1) gives degree sum at most 7. By (1.2),
\[
d_W(x)+d_W(y)\in\{6,7\}.
\]
If the sum is 7, then
\[
\boxed{\epsilon_x+\epsilon_y=4,\qquad I_x+I_y=2.}
\tag{4.3}
\]
Hence all U-excess lies on x,y and xy is the only restored edge incident with the exceptional pair.

If the sum is 6, then
\[
\boxed{(\epsilon_x+\epsilon_y,I_x+I_y)\in\{(3,2),(4,3)\},}
\tag{4.4}
\]
and necessarily d_W(x)=d_W(y)=3.

These are the complete arithmetic exceptional-pair possibilities at epsilon_U=4 under the registered equality model.

## 5. Consequence for the low-delta frontier

The current delta=12 non-four-partite frontier is now:
- depth 0: conditionally excluded under its registered saturated input;
- depth 1: conditionally excluded under its registered saturated input;
- depth 2: **all epsilon_U=0,1,2,3,4 closed** under the registered 308-edge kernel classification;
- depth 3: epsilon_U=0,1,2 closed; epsilon_U=3,4 reduced to the exceptional-pair kernels above.

The separate delta=12 four-partite-U branch remains open, as do delta<=11.

## 6. Dependency audit

This reduction uses:
1. the registered balanced 309-edge Kang–Pikhurko equality model for depth 3;
2. the exact W-profile list at delta=12;
3. the low-W-degree lemma d_W(u)>=3 for epsilon_U>=1;
4. pure alpha(H)<=4 reasoning for a nonadjacent exceptional pair;
5. for the epsilon_U=3 q=1 profile only, the already-proved one-defect pair rule from the depth-2 q=1 analysis.

It does not use the Didin-dependent saturated classification inside the terminal pair arguments. It does not close depth3 epsilon_U=3,4, the delta=12 four-partite-U branch, delta<=11, the five-template compatibility theorem, E407 Q32, or EG617(r=12).