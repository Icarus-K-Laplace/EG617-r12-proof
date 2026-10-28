# E407 Q32 — delta=12 depth-3 epsilon_U=1,2 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED for epsilon_U=1,2** under the registered 309-edge Kang–Pikhurko equality model for the depth-3 augmentation branch and the published 18-vertex Brouwer/Kang–Pikhurko equality theorem where invoked. Depth-3 epsilon_U=0,3,4 remain OPEN; E407 Q32 remains OPEN.

## 1. Depth-3 equality model

After three K5-safe augmentation edges the graph `L3` has309 edges and is a balanced KP equality graph on U. Its four base parts
\[
P_1,P_2,P_3,P_4
\]
have size seven. There is an exceptional vertex x, a distinguished vertex `y in P2`, and a nonempty proper subset `A0 subset P1` of size a.

Let `H0=bar(L3)`. The original target graph H[U] is obtained from H0 by restoring three target edges. If `I_x,I_y` count restored-edge incidences at x,y, then
\[
d_W(x)=a-1+\epsilon_x-I_x,
\]
\[
d_W(y)=6-a+\epsilon_y-I_y,
\]
and
\[
\boxed{d_W(x)+d_W(y)=5+\epsilon_x+\epsilon_y-I_x-I_y\le5+\epsilon_U.}
\tag{1.1}
\]

The equality graph has `xy` as an L3-edge, so xy is a target nonedge in H0. It becomes a target edge only if one restored edge is xy. No restored edge has type P3-P4. In H0, P3 and P4 are target K7s, have no target edges between them, and x,y are target-nonadjacent to every vertex of P3 union P4.

For epsilon_U>=1 the delta=12 low-W-degree lemma gives
\[
d_W(u)\ge3\quad\text{for every }u\in U.
\tag{1.2}

# 2. epsilon_U=1 is impossible

Equation (1.1) and (1.2) give
\[
d_W(x)=d_W(y)=3,
\]
\[
\epsilon_x+\epsilon_y=1,
\qquad I_x=I_y=0.
\tag{2.1}
\]
Thus all U-excess lies on x,y, all three restored edges avoid x,y, and xy remains a target nonedge.

The W ledger is
\[
e(H[W])=35.
\]
Exactly as in `DELTA12_DEPTH2_EPS1_CLOSURE.md`, the complement J_W is a non-four-partite 118-edge K5-free equality graph, hence H[W] is one of the five explicit KP equality kernels.

That file proves the six-deletion lemma: deleting any set of at most six vertices from any of the five kernels leaves an independent triple.

But
\[
|N_W(x)\cup N_W(y)|\le6.
\]
Delete this union. An independent triple remains and is anticomplete to both x and y. Together with the nonadjacent pair x,y it gives an independent five-set in H, contradicting alpha(H)<=4.

Therefore
\[
\boxed{\epsilon_U=1\text{ is impossible at depth3}.}
\tag{2.2}
\]

# 3. epsilon_U=2: preliminary reductions

Now
\[
6\le d_W(x)+d_W(y)\le7.
\tag{3.1}
\]
The edge xy cannot be restored. If xy were one of the three restored target edges, then it contributes one incidence to both x and y, so `I_x+I_y>=2`; (1.1) would give
\[
d_W(x)+d_W(y)\le5+2-2=5,
\]
contradicting (3.1). Hence
\[
xy\notin E(H).
\tag{3.2}
\]

For epsilon_U=2 the W ledger gives `e(H[W])=34`. The exact four-partite-complement arithmetic leaves four target W profiles:

1. `K3 dotcup K4 dotcup K5 dotcup K6`, no cross edge;
2. base `(3,5,5,5)` with one W-cross edge;
3. base `(4,4,4,6)` with one W-cross edge;
4. base `(4,4,5,5)` with two W-cross edges.

At least one of x,y has W-degree at most three.

In the one-cross profile with minimum base size four, a vertex not complete to a base component needs at least six W-neighbours; a saturated vertex needs at least four. Thus a degree-at-most-three x/y is impossible. In the two-cross `(4,4,5,5)` profile, an unsaturated vertex needs at least five neighbours and a saturated vertex at least four, again impossible.

Therefore only profiles 1 and2 remain.

# 4. The `(3,5,5,5)+one-cross-edge` profile is impossible

Any vertex of W-degree three or four satisfying alpha(H)<=4 must be complete to the K3 base component:

- degree three can only saturate K3;
- degree four cannot saturate a K5;
- if it were unsaturated, the single-cross-edge saturation cost is at least `3+5-2=6`.

Hence both x and y are complete to K3. Their total number of W-neighbours outside K3 is at most one by (3.1).

Outside K3 lie three K5 base parts and at most one cross edge. Choose one vertex from each K5, avoiding the at most one extra x/y neighbour and the endpoints of the single cross edge when necessary. The resulting three vertices are pairwise nonadjacent and anticomplete to x,y.

Together with the nonadjacent pair x,y they form an independent five-set, contradiction.

# 5. The no-cross `K3+K4+K5+K6` profile

Both x,y must be complete to one W-component.

If both are complete to K3, their union has at most one further W-neighbour by (3.1). Choose one point from each of K4,K5,K6 avoiding that one neighbour. Together with x,y this gives an independent five-set.

Thus the only remaining possibility is, up to swapping x,y,
\[
N_W(x)=K_3,
\qquad N_W(y)=K_4,
\tag{5.1}
\]
with degrees 3 and4.

Equality in the upper bound of (3.1) now forces
\[
\epsilon_x+\epsilon_y=2,
\qquad I_x=I_y=0.
\tag{5.2}
\]
So all U-excess lies on x,y and all three restored edges avoid them.

Take any `z in P3 union P4`. It has no excess. Since no restored edge has type P3-P4,
\[
d_W(z)=6-I_z\le6.
\tag{5.3}
\]
Also z remains H-nonadjacent to both x and y.

The pair `(x,z)` forces z to be complete to one of `K4,K5,K6`; the pair `(y,z)` forces z to be complete to one of `K3,K5,K6`. Because `d_W(z)<=6`, z cannot simultaneously cover K3 and K4. Hence every z is complete to K5 or K6. Since 5+6>6, the label is unique.

Each of P3 and P4 is a target K7. If all seven points of one part had label K5, that K7 together with K5 would form K12; if all had label K6 it would form K13. Therefore each P3 and P4 uses both labels.

Choose `u in P3` and `v in P4` with the same label, say K5. They are H-nonadjacent because no restored edge has type P3-P4. Each has at most one W-neighbour outside K5. Among the other three W-components K3,K4,K6 choose one vertex from each avoiding those at most two outside neighbours. These three vertices are pairwise nonadjacent and anticomplete to u,v.

Together with the nonadjacent pair u,v they form an independent five-set, contradiction.

Thus profile 1 is impossible as well.

## 6. Conclusion

\[
\boxed{
\delta=12,\ \text{non-four-partite depth3},\ \epsilon_U\in\{1,2\}
\Longrightarrow\bot.
}
\]
under the registered 309-edge KP equality model.

Depth3 epsilon_U=0,3,4 remain OPEN.

## 7. Dependency audit

The epsilon1 proof uses the published 18-vertex Brouwer/Kang-Pikhurko equality theorem through the already audited five W-kernels and six-deletion lemma.

The epsilon2 proof uses the registered W-profile/saturation arithmetic, the balanced 309-edge U equality model, pure alpha/omega constraints, and the fact that no restored edge has type P3-P4.

Neither terminal proof uses Didin. No claim is made for the remaining depth3 epsilons, delta=12 four-partite-U, delta<=11, five-template compatibility, E407 Q32, or EG617(r=12).
