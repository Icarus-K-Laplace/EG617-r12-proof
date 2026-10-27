# E407 Q32 — delta=13 two-step augmentation: epsilon_U=1,2 closure

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict closure** under the frozen E407-Q32 core/support contract and the registered Kang–Pikhurko equality description used in `DELTA13_NONPARTITE_TWO_STEP_AUGMENTABLE.md`. This closes the epsilon_U=1 and epsilon_U=2 terminals of the two-step augmentable non-four-partite delta=13 branch. E407 Q32 remains OPEN.

## 1. Imported exact equality structure

In the balanced KP equality graph `L*` on U, the four base parts are `P1,P2,P3,P4` of size seven, with exceptional vertex `x`, distinguished `y in P2`, and nonempty proper `A0 subset P1`.

The KP construction has the edge `xy` in `L*`: the exceptional vertex x is adjacent in `L*` to y. Hence in

\[
H_0[U]=\overline{L^*}
\]

we have

\[
xy\notin E(H_0).
\tag{1.1}
\]

The original target graph on U is obtained by adding the two target edges `e1,e2` corresponding to the two augmentation edges:

\[
H[U]=H_0[U]+e_1+e_2.
\]

Thus xy can become an H-edge only if one of e1,e2 is xy.

## 2. epsilon_U=1: both surviving W profiles are impossible

The reduction theorem proves that in either epsilon_U=1 terminal,

\[
d_H(x,W)=d_H(y,W)=3,
\]

and both x and y are complete to the unique K3 component of H[W]. It also proves

\[
I_x=I_y=0,
\]

so neither added edge meets x or y. Therefore (1.1) survives in H:

\[
xy\notin E(H).
\tag{2.1}
\]

### Terminal 1: K3 dotcup K4 dotcup K5 dotcup K6, no W-cross edge

Outside the K3 there are three target clique components with no edges between distinct components. Since x and y have W-degree exactly three and are complete to the K3, they are anticomplete to all three remaining components.

Choose one vertex from each of K4,K5,K6. These three vertices are pairwise nonadjacent, and by (2.1) they are also jointly nonadjacent to x and y. Hence they together with x,y form an independent five-set in H, contradicting

\[
\alpha(H)\le4.
\]

### Terminal 2: base sizes (3,5,5,5) with one W-cross edge

Again x and y are anticomplete to all three K5 parts. Among the three K5 parts there is at most one cross edge in total. Choose one vertex from each K5 part while avoiding the two endpoints of that single cross edge when necessary. The chosen triple is pairwise nonadjacent.

Together with the nonadjacent pair x,y this again gives an independent five-set in H. Contradiction.

Therefore

\[
\boxed{\epsilon_U=1\text{ is impossible in the two-step augmentable branch}.}
\tag{2.2}
\]

## 3. epsilon_U=2: K3 dotcup 3K5 is impossible

The reduction theorem leaves only

\[
H[W]=K_3\dot\cup K_5\dot\cup K_5\dot\cup K_5,
\]

with x and y both complete to the K3 and

\[
6\le d_H(x,W)+d_H(y,W)\le7.
\tag{3.1}
\]

By the universal three-neighbour lemma, each of x,y has W-degree at least three.

First, xy is still a nonedge of H. Indeed, if one of e1,e2 were xy, then that single added edge would contribute one to both I_x and I_y, so

\[
I_x+I_y\ge2.
\]

Using the exact degree-sum identity from the reduction,

\[
d_H(x,W)+d_H(y,W)
=5+\epsilon_x+\epsilon_y-I_x-I_y
\le5+2-2=5,
\]

contradicting the lower bound six. Hence

\[
xy\notin E(H).
\tag{3.2}
\]

If the degree sum in (3.1) is six, both x and y have degree three, so both are anticomplete to all three K5 parts. Choosing one point from each K5 produces an independent triple, and with x,y an independent five-set.

If the degree sum is seven, the W-degrees are 3 and 4. The degree-three vertex is anticomplete to all three K5 parts. The degree-four vertex has exactly one neighbour outside the K3. Choose one vertex from each K5, avoiding that single extra neighbour. The resulting three W vertices are pairwise nonadjacent and anticomplete to both x and y. Together with (3.2) they again form an independent five-set.

Thus

\[
\boxed{\epsilon_U=2\text{ is impossible in the two-step augmentable branch}.}
\tag{3.3}
\]

## 4. Surviving epsilon_U=3 terminal is sharpened

The only remaining two-step terminal has

\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5,
\qquad d_H(x,W)=d_H(y,W)=4,
\]

with all U-excess on x,y and both added edges avoiding x,y. Hence xy remains a nonedge of H.

Each of x,y is complete to a K4 component. They cannot be complete to the same K4: if they were, both would be anticomplete to the other three W components, so one point from each of those three components together with x,y would be an independent five-set.

Therefore the epsilon_U=3 survivor satisfies the strictly stronger condition

\[
\boxed{x\text{ and }y\text{ are complete to the two distinct K4 components of }H[W].}
\tag{4.1}
\]

In particular x and y are anticomplete to both K5 components and to each other's saturated K4.

## 5. Updated two-step frontier

The four terminals in `DELTA13_NONPARTITE_TWO_STEP_AUGMENTABLE.md` reduce to exactly one:

- epsilon_U=1, K3+K4+K5+K6: **EXCLUDED**;
- epsilon_U=1, (3,5,5,5)+one cross: **EXCLUDED**;
- epsilon_U=2, K3+3K5: **EXCLUDED**;
- epsilon_U=3, 2K4+2K5: **OPEN**, but x and y must saturate the two different K4 parts.

No statement is made here about the separate one-step-saturated or already-saturated delta=13 forks. No E407-Q32 or EG617 closure is claimed.
