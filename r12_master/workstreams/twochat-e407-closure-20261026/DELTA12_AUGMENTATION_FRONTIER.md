# E407 Q32 — delta=12 non-four-partite augmentation frontier

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict reduction** under the frozen E407-Q32 support/core contract, the registered Brouwer/Kang-Pikhurko non-four-partite extremal theorem, and (for saturated depths 0/1) the same unaudited Didin alpha-critical component-count theorem used in the delta=13 saturated closures. E407 Q32 remains OPEN.

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

The 49 selected support K4s contribute 294 distinct edges of L_U, so only twelve L_U-edges lie outside the support-pair system.

## 2. Greedy K5-safe augmentation has depth at most three

Starting from L_0=L_U, repeatedly add a nonedge whose addition preserves K5-freeness. Adding edges cannot turn a non-four-partite graph into a four-partite graph: if a supergraph were four-partite, every subgraph would be four-partite under the same vertex partition.

Hence every intermediate L_j remains non-four-partite and K5-free.

The registered 29-vertex Brouwer/Kang-Pikhurko bound says a non-four-partite K5-free graph has at most 309 edges. Since L_0 has 306 edges, the process stops after

\[
\boxed{k\in\{0,1,2,3\}}
\]

augmentations. If k=3, the 309-edge graph is automatically K5-saturated: any further K5-safe edge would give a 310-edge non-four-partite K5-free graph, impossible.

Thus the non-four-partite delta=12 branch has an exact four-depth split.

## 3. Saturated depth 0 is conditionally impossible

Suppose L_0 itself is K5-saturated. Put
\[
G_0=\overline{L_0}=H[U].
\]
Then
\[
|V(G_0)|=29,\qquad e(G_0)=100,\qquad \alpha(G_0)=4,
\]
and K5-saturation of L_0 makes G_0 alpha-critical.

Under the registered Didin component-count theorem, the same argument as in `DELTA13_SATURATED_307_CONDITIONAL_CLOSURE.md` forces exactly three components
\[
G_0=K_a\dot\cup K_b\dot\cup C,
\]
with alpha(C)=2. Let J=bar(C). The 49 edge-disjoint support K4s force
\[
ab\ge49,
\qquad e(J)\ge49,
\]
and Brouwer gives
\[
e(C)\ge\lfloor c^2/4\rfloor-1.
\]
Together with
\[
a+b+c=29,
\qquad e(C)=100-\binom a2-\binom b2,
\]
the exact integer survivor set is empty.

Therefore depth 0 is **PROVED_CONDITIONAL / EXCLUDED**.

## 4. Saturated depth 1 is conditionally impossible

If exactly one safe edge is added before saturation, L_1 has 307 edges and G_1=bar(L_1) has 99 edges. The 49 support K4s are already present in L_0, hence remain in L_1, and the new safe edge is not a support edge.

The identical alpha-critical reduction gives the same inequalities with e(G_1)=99. The integer survivor set is again empty; this is exactly the arithmetic already replayed in `verify_delta13_saturated_307.py`.

Therefore depth 1 is **PROVED_CONDITIONAL / EXCLUDED**.

## 5. Depth 2 has the unique 308-edge saturated C5-blowup kernel

If exactly two safe edges e1,e2 are added before saturation, L_2 has 308 edges and G_2=bar(L_2) has 98 edges. Under the registered saturated-kernel classification,
\[
\boxed{G_2=K_7^A\dot\cup K_7^B\dot\cup\overline J,}
\]
where J is the 15-vertex triangle-free saturated C5 blow-up with cyclic part sizes `(5,5,2,1,2)` and degree sequence `7^10,6^4,4^1`.

The 49 support K4s exhaust all 49 A-B edges and all 49 J-edges of L_2. Therefore neither added edge e1,e2 can be an A-B edge or a J-edge. Both are among the fourteen support-uncovered A/B-J cross edges.

At a J-vertex z the number of such uncovered cross edges is
\[
2(7-d_J(z)).
\]
Thus no added edge can end at one of the ten degree-7 X/Y vertices. Every J-endpoint belongs to the four degree-6 vertices `C union E` or the unique degree-4 vertex d0.

Equivalently, the original H[U] is obtained from the classified G_2 by adding exactly two target edges, each joining A or B to `C union E union {d0}` and each chosen from the fourteen uncovered cross edges.

This is the **depth-2 terminal model**.

## 6. Depth 3 reaches the 309-edge Kang-Pikhurko equality model

If three K5-safe edges e1,e2,e3 can be added, then
\[
L_3=L_U+e_1+e_2+e_3
\]
has 309 edges and is non-four-partite K5-free. The registered Kang-Pikhurko equality theorem applies.

As in the delta=13 equality reduction, the 49 support K4 packing excludes the unbalanced equality bases, leaving the balanced base
\[
P_1,P_2,P_3,P_4,
\qquad |P_i|=7,
\]
with exceptional vertex x, distinguished y in P2, and a nonempty proper A0 subset P1.

Let H0=bar(L_3). If `I_x,I_y` count the three restored target edges incident with x,y, then the original H[U]=H0+e1+e2+e3 satisfies
\[
d_H(x,W)=a-1+\epsilon_x-I_x,
\]
\[
d_H(y,W)=6-a+\epsilon_y-I_y,
\]
and hence the same key sum identity
\[
\boxed{d_H(x,W)+d_H(y,W)
=5+\epsilon_x+\epsilon_y-I_x-I_y
\le5+\epsilon_U.}
\tag{6.1}
\]

Every P3-P4 edge of the equality graph belongs to the support packing, so none of e1,e2,e3 is of type P3-P4.

This is the **depth-3 equality terminal model**.

## 7. W-side arithmetic at delta=12

Let J_W=bar(H[W]). Then
\[
e(J_W)=117+\epsilon_U.
\]
For `epsilon_U>=2`, this is at least 119, above the 18-vertex non-four-partite Brouwer bound 118. Therefore J_W is four-partite, so H[W] is a four-clique base with a small cross-edge defect.

Exact profiles are:

### epsilon_U=2
- `(3,4,5,6)`, q=0;
- `(3,5,5,5)`, q=1;
- `(4,4,4,6)`, q=1;
- `(4,4,5,5)`, q=2.

### epsilon_U=3
- `(3,5,5,5)`, q=0;
- `(4,4,4,6)`, q=0;
- `(4,4,5,5)`, q=1.

### epsilon_U=4
- `(4,4,5,5)`, q=0.

For epsilon_U=1 the complement has exactly 118 edges, so a non-four-partite Brouwer-equality W kernel remains possible. For epsilon_U=0 it has 117 edges. These two low-epsilon cases must not be silently treated as four-partite.

## 8. Universal low-W-degree lemma for epsilon_U>=1

At delta=12, every u in U satisfies
\[
\boxed{d_H(u,W)\ge3\quad\text{whenever }\epsilon_U\ge1.}
\tag{8.1}
\]

Indeed, if Z=N_H(u) cap W has size at most one, then deleting Z from J_W leaves more than the 3-partite Turan number on at least 17 vertices, giving a K4 in J_W and hence an independent H-four-set avoiding Z.

If |Z|=2, then
\[
e(J_W[W\setminus Z])\ge117+\epsilon_U-33=84+\epsilon_U.
\]
For epsilon_U>=2 this exceeds t_3(16)=85. For epsilon_U=1 equality throughout is necessary to avoid a K4; then J_W[W\setminus Z]=T_3(16) and both deleted vertices must be joined in J_W to every possible incident edge. Equivalently H[W] is three clique components on sixteen vertices plus two H-isolated vertices, which already contains an independent five-set. Contradiction.

Thus (8.1) holds.

In the depth-3 equality branch, (6.1)+(8.1) immediately imply
\[
\epsilon_U\ne0,
\]
and for epsilon_U=1 force
\[
d_W(x)=d_W(y)=3,
\quad \epsilon_x+\epsilon_y=1,
\quad I_x=I_y=0.
\]
This is the first terminal rigidity for the next round.

## 9. Exact remaining delta=12 non-four-partite targets

After this reduction, only two model families remain:

1. **Depth 2:** the classified 308-edge C5-blowup saturated kernel, with exactly two restored target edges chosen from its fourteen uncovered A/B-J cross edges.
2. **Depth 3:** the balanced 309-edge Kang-Pikhurko equality kernel, with exactly three restored target edges, none of type P3-P4.

Depths 0 and 1 are conditionally excluded under the registered Didin+Brouwer ledger.

The next proof task is to eliminate these two full-core extension families using the W profiles, pair common-nonneighbour rule, support-edge ownership, clique-number 11, and the four-unit H excess budget.

No claim is made for the separate delta=12 four-partite-U branch in this file, and no E407-Q32 closure is claimed.
