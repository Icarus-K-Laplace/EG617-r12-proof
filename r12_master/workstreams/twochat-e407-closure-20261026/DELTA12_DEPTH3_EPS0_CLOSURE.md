# E407 Q32 — delta=12 depth-3 epsilon_U=0 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered balanced 309-edge Kang–Pikhurko equality model for the depth-3 augmentation branch. Depth-3 epsilon_U=3,4 remain OPEN; E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Equality-model degree sum

In the depth-3 equality model, with exceptional vertices x,y and restored-edge incidence counts I_x,I_y,
\[
d_W(x)+d_W(y)
=5+\epsilon_x+\epsilon_y-I_x-I_y.
\]
At epsilon_U=0 this gives
\[
\boxed{d_W(x)+d_W(y)=5-I_x-I_y\le5.}
\tag{1.1}
\]

The edge xy is a target nonedge in the equality graph H0. If xy were one of the three restored target edges, it would contribute one incidence to both endpoints, so `I_x+I_y>=2` and (1.1) would give
\[
d_W(x)+d_W(y)\le3.
\tag{1.2}
\]

## 2. Universal degree-two extremal lemma at e(H[W])=36

At epsilon_U=0,
\[
e(H[W])=36.
\]

### Lemma 2.1

For any `u in U`:

1. `d_W(u)<=1` is impossible;
2. if `d_W(u)=2`, then
   \[
   H[W]=K_2\dot\cup K_5\dot\cup K_5\dot\cup K_6
   \]
   and `N_W(u)` is exactly the K2 component.

### Proof

If `d_W(u)<=1`, delete `N_W(u)`. At least17 W-vertices remain and at most36 edges remain. A 17-vertex graph with independence number at most3 has at least
\[
p_3(17)=40
\]
edges. Therefore the remainder contains an independent four-set, anticomplete to u, giving an independent five-set in H. Contradiction.

Now suppose `d_W(u)=2` and put `D=N_W(u)`. To avoid the same contradiction,
\[
\alpha(H[W\setminus D])\le3,
\]
so
\[
e(H[W\setminus D])\ge p_3(16)=35.
\tag{2.1}
\]

Every W-vertex has positive W-degree: an isolated W-vertex together with an independent four-set in the remaining 17-vertex graph (again forced because 36<40) would give an independent five-set in H[W]. Hence deleting the two vertices of D removes at least one W-edge, and
\[
e(H[W\setminus D])\le35.
\]
Equality holds. Thus the 16-vertex remainder is the extremal alpha<=3 graph
\[
K_6\dot\cup K_5\dot\cup K_5,
\]
and exactly one W-edge is incident with D. Since both points of D have positive degree, that edge joins them and neither has any edge to the 16-vertex remainder. Hence the claimed K2+K5+K5+K6 structure, with D=K2. QED.

## 3. xy cannot be restored

Lemma 2.1 implies
\[
d_W(x)\ge2,\qquad d_W(y)\ge2.
\]
If xy were restored, (1.2) would give degree sum at most three, impossible. Therefore
\[
\boxed{xy\notin E(H).}
\tag{3.1}
\]

By (1.1), at least one of x,y has W-degree exactly two; assume it is x. Lemma 2.1 forces
\[
H[W]=K_2\dot\cup K_5\dot\cup K_5\dot\cup K_6,
\qquad N_W(x)=K_2.
\tag{3.2}
\]

The other exceptional vertex y has W-degree at most three. The same component-exhaustion argument applies: if y failed to contain one whole W-component, choose one W-nonneighbour from each of the four components and together with y obtain an independent five-set. Since the only W-component of size at most three is the K2,
\[
K_2\subseteq N_W(y).
\tag{3.3}
\]

## 4. Terminal contradiction

The pair x,y is target-nonadjacent by (3.1). By (3.2)-(3.3), both are complete to the K2, while their total W-neighbourhood union has size at most five. In particular all three large components
\[
K_5\dot\cup K_5\dot\cup K_6
\]
contain common nonneighbours of x and y.

Choose one vertex from each of these three components. They are pairwise nonadjacent and anticomplete to x,y. Together with the nonadjacent pair x,y they form an independent five-set in H, contradicting alpha(H)<=4.

Therefore
\[
\boxed{
\delta=12,\ \text{non-four-partite depth3},\ \epsilon_U=0
\Longrightarrow\bot.
}
\]

## 5. Scope

The proof uses the registered depth-3 equality-model degree identity plus elementary alpha<=3 extremal bounds at n=16,17 and pure alpha(H)<=4 reasoning. It does not use Didin.

Depth-3 epsilon_U=3,4 remain OPEN. No conclusion is claimed for delta=12 four-partite U, delta<=11, five-template global compatibility, E407 Q32, or EG617(r=12).
