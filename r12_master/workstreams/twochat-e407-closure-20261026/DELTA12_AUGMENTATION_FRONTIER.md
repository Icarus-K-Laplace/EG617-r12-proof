# E407 Q32 — delta=12 non-four-partite augmentation frontier

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL strict reduction. E407 Q32 remains OPEN.**

## 1. Delta=12 contract

Assume
\[
\delta=12,\qquad e(L_U)=306,
\qquad L_U=\overline{H[U]}\text{ is non-four-partite and K5-free}.
\]
Then
\[
e(H[U])=100,
\qquad 0\le\epsilon_U\le4,
\]
\[
e_H(U,W)=148+\epsilon_U,
\qquad e(H[W])=36-\epsilon_U.
\]
The 49 selected support K4s contribute 294 distinct edges of L_U, so twelve L_U-edges lie outside the support-pair system.

## 2. Greedy K5-safe augmentation depths

Repeatedly add a nonedge preserving K5-freeness. Every intermediate graph remains non-four-partite. The registered 29-vertex Brouwer/Kang-Pikhurko bound gives at most 309 edges, hence the process stops after
\[
k\in\{0,1,2,3\}.
\]

Current status:
- depth 0: PROVED_CONDITIONAL / EXCLUDED under the registered Didin+Brouwer saturated reduction;
- depth 1: PROVED_CONDITIONAL / EXCLUDED under the registered saturated reduction;
- depth 2: classified 308-edge C5-blowup kernel; epsilon_U=2 is now CLOSED; epsilon_U in {0,1,3,4} remain OPEN;
- depth 3: reaches the 309-edge Kang-Pikhurko equality model and remains OPEN.

## 3. Depth-2 kernel

At depth 2,
\[
G_2=K_7^A\dot\cup K_7^B\dot\cup\overline J,
\]
where J is the 15-vertex saturated C5 blow-up with part sizes `(5,5,2,1,2)` and degree sequence `7^10,6^4,4^1`.

The 49 support K4s exhaust all 49 A-B edges and all 49 J-edges of L2. The two restored target edges in H[U] therefore join A or B to one of the four degree-6 J vertices `C union E` or the unique degree-4 point d0.

### epsilon_U=2 — CLOSED

`DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` forces the unique W-terminal
\[
H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6,
\]
with `N_W(d0)=K4`, the two distinct restored J-endpoints having W-neighbourhood K3, and all U-excess on d0.

`DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md` eliminates this terminal using the nonadjacent-pair rule. Except for at most one shared restored-edge endpoint, every point in the two K7 components must be complete to K5 or K6. Cross-K7 nonadjacency forces opposite labels, which yields K12 or K13 and contradicts omega(H)<=11.

This closure does not use Didin. It is conditional on the registered 308-edge saturated-kernel classification.

### Remaining depth-2 cases

\[
\epsilon_U\in\{0,1,3,4\}
\]
remain OPEN. The epsilon_U=3,4 cases have four-clique W profiles and are the next preferred targets.

## 4. Depth-3 equality model

At depth 3, L3 has309 edges and the registered Kang-Pikhurko equality theorem applies. The support packing leaves the balanced equality base with four 7-parts, exceptional vertices x,y, and three restored target edges. The key retained identity is
\[
d_H(x,W)+d_H(y,W)
=5+\epsilon_x+\epsilon_y-I_x-I_y
\le5+\epsilon_U.
\]
No restored edge is of P3-P4 type.

This depth remains OPEN.

## 5. W-side profiles at delta=12

For epsilon_U>=2, J_W=bar(H[W]) has at least119 edges and is four-partite. The exact H[W] profiles are:

### epsilon_U=2
- `(3,4,5,6)`, q=0;
- `(3,5,5,5)`, q=1;
- `(4,4,4,6)`, q=1;
- `(4,4,5,5)`, q=2.

All are now eliminated inside the depth-2 branch by the unique-terminal closure.

### epsilon_U=3
- `(3,5,5,5)`, q=0;
- `(4,4,4,6)`, q=0;
- `(4,4,5,5)`, q=1.

### epsilon_U=4
- `(4,4,5,5)`, q=0.

For epsilon_U=1 the complement has118 edges and a non-four-partite Brouwer-equality W kernel remains possible. For epsilon_U=0 it has117 edges.

## 6. Universal low-W-degree lemma

Whenever epsilon_U>=1, every u in U has
\[
d_H(u,W)\ge3.
\]
This remains a principal input to the depth-2 and depth-3 terminal analyses.

## 7. Exact remaining delta=12 non-four-partite targets

1. depth2 epsilon_U=3,4;
2. depth2 epsilon_U=0,1;
3. depth3 all legal epsilon_U.

The separate delta=12 four-partite-U branch is not treated here and remains OPEN.

No E407-Q32 or EG617(r=12) closure is claimed.
