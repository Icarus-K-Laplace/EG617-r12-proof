# E407 Q32 — delta=12 depth-3 epsilon_U=4 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered balanced 309-edge Kang–Pikhurko equality model and the exact epsilon_U=4 W-profile. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Frozen interface

At epsilon_U=4,
\[
H[W]=K_4^A\dot\cup K_4^B\dot\cup K_5^C\dot\cup K_5^D.
\tag{1.1}
\]
Use the exceptional pair x,y of the depth-3 equality model and `DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md`.

If xy is not restored, the possibilities are:
- degree sum 8 with `(epsilon_x+epsilon_y,I_x+I_y)=(3,0)` or `(4,1)`, and the union is exactly the two K4 components;
- degree sum 9 with `(epsilon_x+epsilon_y,I_x+I_y)=(4,0)`.

If xy is restored, the degree sum is 6 or 7.

Every U vertex must be complete to at least one W-component. Otherwise choosing one W-nonneighbour from each of the four clique components together with the U vertex gives an independent five-set. In particular every U-to-W degree is at least four in this q=0 profile.

We also use the pair rule: if u,v are H-nonadjacent, then N_W(u) union N_W(v) contains two complete W-components. Otherwise the common W-nonneighbours contain an independent triple, giving an independent five-set with u,v.

## 2. xy restored is impossible

The reduction gives
\[
d_W(x)+d_W(y)\le7.
\]
But each exceptional vertex must contain a complete W-component and every component has size at least four. Hence
\[
d_W(x)+d_W(y)\ge8,
\]
contradiction.

Therefore xy is not restored.

## 3. Nonrestored degree-sum eight

The union N_W(x) union N_W(y) has size eight and covers two W-components. Since each exceptional vertex has degree at least four and the neighborhoods are disjoint, after relabeling
\[
N_W(x)=K_4^A,
\qquad N_W(y)=K_4^B.
\tag{3.1}
\]

### 3.1 No restored incidence at x or y

First suppose `(epsilon_x+epsilon_y,I_x+I_y)=(3,0)`. Exactly one unit of U-excess lies outside x,y, while no restored edge meets either exceptional vertex.

Every z in P3 union P4 remains H-nonadjacent to both x,y. Pairing with (3.1) forces z to be complete to K5^C or K5^D: satisfying the x-pair needs one full component other than A, satisfying the y-pair needs one full component other than B, and degree at most seven prevents simultaneous completion of A and B.

The label is unique. A cross P3-P4 pair with the same K5 label cannot cover a second W-component: only one U-excess unit exists outside x,y, so at most one of the pair can have W-degree seven; the other has degree at most six. Their total number of neighbours outside the common K5 is therefore at most three, below the size-four minimum second component. Since no restored edge has type P3-P4, same labels are impossible across the two parts.

Thus P3 and P4 are monochromatic in opposite C/D labels. A target K7 complete to a target K5 is K12, contradiction.

### 3.2 Exactly one restored incidence at the exceptional pair

Now `(epsilon_x+epsilon_y,I_x+I_y)=(4,1)`. All U-excess lies on x,y. There is exactly one restored edge incident with the exceptional pair.

If its other endpoint is not in P3 union P4, then all fourteen P3/P4 vertices remain nonadjacent to x,y and the previous binary C/D argument gives K12.

So, for a survivor, the unique exceptional restored edge must be xz0 or yz0 for a single z0 in P3 union P4. By symmetry take z0 in P3 and xz0 restored. Then
\[
d_W(z_0)=5,
\]
while every other P3/P4 vertex has W-degree at most six.

All vertices of P3\{z0} and P4 get C/D labels. Cross same-label pairs are impossible, so these six P3 vertices are monochromatic, P4 is monochromatic, and their labels are opposite. Say P3\{z0} is C and P4 is D.

The special z0 cannot have label C, else the entire target K7 P3 is complete to K5^C and gives K12. It cannot have label D, because every z0-v pair with v in P4 is a nonrestored P3-P4 pair sharing K5^D and cannot cover a second component. Hence z0 must be complete to K4^A, the component of its restored exceptional partner x.

Now consider
\[
R=P_1\cup(P_2\setminus\{y\}).
\]
All R vertices have zero excess and baseline W-degree five before restored incidences. A vertex of R cannot have C label: it is H-nonadjacent to six C-labelled vertices of P3, and a K5-labelled R vertex has W-degree exactly five and hence no restored incidence with which to repair even one such pair. Similarly no R vertex can have D label because P4 has seven D-labelled vertices. Therefore every R vertex has A or B label.

In the exact equality model, A0 subset P1 is nonadjacent to x, while P1\A0 is nonadjacent to y. The same-component pair rule therefore forces
\[
A_0\text{ to have label }B,
\qquad
P_1\setminus A_0\text{ to have label }A.
\tag{3.2}
\]
Since A0 is nonempty and proper, P1 uses both labels.

Between P1 and P2\{y} every same-label pair must be restored: two R vertices sharing a K4 label have at most two total W-neighbours outside the common K4 and cannot cover another component. But after the edge xz0 only two restored target edges remain. For a mixed 7-point P1 and an arbitrary binary colouring of the six vertices P2\{y}, the number of same-label cross pairs is at least six. Explicitly, if a points of P1 have label A and b points of P2\{y} have label A,
\[
S(a,b)=ab+(7-a)(6-b)\ge6
\]
for 1<=a<=6. Contradiction.

Thus the entire degree-sum-eight branch is impossible.

## 4. Nonrestored degree-sum nine: exceptional component classification

Now
\[
\epsilon_x+\epsilon_y=4,
\qquad I_x=I_y=0,
\tag{4.1}
\]
so all U-excess lies on x,y and every other U vertex has zero excess.

The exceptional degrees are 4 and 5. Each contains a full W-component and their union covers two components. Up to swapping component names, there are only two primary types:

1. **AB type:** the two exceptional primary components are the two K4s A and B. The degree-five neighborhood may contain one additional point.
2. **AC type:** one exceptional neighborhood is exactly K4^A and the other exactly K5^C.

The AB type is eliminated exactly as in Section 3.1. Every P3/P4 vertex is forced to a C/D K5 label, cross same labels are impossible, and P3,P4 become opposite monochromatic K5 labels, giving K12.

It remains to exclude the AC type. Fix
\[
N_W(x)=K_4^A,
\qquad N_W(y)=K_5^C.
\tag{4.2}
\]

Every P3/P4 vertex is H-nonadjacent to x,y and has W-degree at most six. The two pair rules force it to be complete to either K4^B or K5^D. Call these labels B and D.

A cross D-D pair is impossible. A cross B-B pair is possible only in the sharp configuration where both vertices have W-degree six and their two outside neighbours are complementary 2-subsets of K4^A. Thus D can occur on at most one side, both sides contain B, and all cross B-labelled vertices have zero restored incidence with fixed complementary A-two-sets across P3/P4.

## 5. AC type with a D-labelled P-vertex

Assume D occurs, say in P3. Then no R vertex can have D label. Indeed an R vertex complete to K5^D must have W-degree exactly five and therefore restored incidence zero; it is H-nonadjacent to the D-labelled P3 vertex and cannot repair their same-label pair.

No R vertex can have B label either, because P4 contains B-labelled vertices and an R B-neighborhood has at most one point outside K4^B, while a P B-neighborhood has at most two; their union cannot complete a second component, and an R B vertex has at most one restored incidence, far fewer than the seven P4 incidences if P4 is all B. More directly, since one side has no D-D allowance, the opposite side is entirely B, so any R B label would require restoration to every vertex of that side.

Thus every R vertex has label A or C.

The equality-model exceptional adjacencies now force
\[
A_0\subset P_1\text{ to label }C,
\qquad
P_1\setminus A_0\text{ to label }A.
\tag{5.1}
\]
Indeed A0 is nonadjacent to x with A-label, while P1\A0 is nonadjacent to y with C-label. Hence P1 is a genuinely mixed binary A/C set.

Every same-label pair between P1 and P2\{y} must be one of the three restored edges. For a mixed seven-point P1 and six arbitrary binary labels on P2\{y}, the same-label count is at least six, as in Section 3.2. Contradiction.

Therefore D does not occur in P3 or P4.

## 6. AC type with all P3/P4 vertices B-labelled

Now every P3 and P4 vertex is B-labelled. Cross B-B compatibility forces every one of these fourteen vertices to have W-degree exactly six and restored incidence zero, with one fixed complementary pair of A-two-sets across the two P-parts.

The exceptional vertices also have restored incidence zero. Hence all six restored-edge endpoint incidences lie in
\[
R=P_1\cup(P_2\setminus\{y\}).
\tag{6.1}
\]

An R vertex has baseline W-degree five. A C- or D-labelled R vertex needs all five vertices of its K5 component and therefore has restored incidence zero. A B label is impossible against the fourteen B-labelled P vertices. Consequently every restored endpoint in R must be A-labelled. Since an A-labelled R vertex must keep at least the four A vertices, it can have restored incidence at most one.

Thus the three restored edges have six distinct A-labelled endpoints, with at least three in P1 and at least three in P2\{y}; all restored edges lie between these two base parts because L3 has no within-part edges.

But every A-A cross pair must be restored: without restoration, two A-labelled R vertices have at most two total neighbours outside their common K4 and violate the pair rule. With at least three A-labelled vertices on each side there are at least
\[
3\cdot3=9
\]
same-label cross pairs, whereas only three restored edges exist. Contradiction.

Thus the AC type is impossible.

## 7. Conclusion

Every epsilon_U=4 depth-3 branch is impossible. Therefore
\[
\boxed{
\delta=12,\ \text{non-four-partite depth3},\ \epsilon_U=4
\Longrightarrow\bot.
}
\]

Together with the existing epsilon_U=0,1,2,3 depth-3 closures, this closes the entire **delta=12 non-four-partite depth-3 augmentation layer**, conditional on the registered equality-model classification.

The separate delta=12 four-partite-U branch and all delta<=11 remain open. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

## 8. Dependencies

This proof uses:
1. the registered balanced 309-edge Kang–Pikhurko equality model with its exact P1/P2/P3/P4,x,y,A0 adjacencies;
2. the exact epsilon_U=4 W profile K4+K4+K5+K5;
3. the low-W-degree lemma and the exact exceptional-pair reduction;
4. pure alpha(H)<=4 and omega(H)<=11 component/pair rules.

No Didin-dependent saturated theorem is used in the terminal arguments.