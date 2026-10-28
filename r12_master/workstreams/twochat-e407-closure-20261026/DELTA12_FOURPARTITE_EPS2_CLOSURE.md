# E407 Q32 — delta=12 four-partite-U epsilon_U=2 closure

Date: 2026-10-28  
Status: **PROVED / CLOSED** under the frozen `(7,7,7,8)` support kernel, the exact epsilon_U=2 W-profile list, and the support-block W-capacity theorem. No Didin input is used. E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Kernel and notation

Use
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad |T_i|=7,\quad |R|=8,
\]
from `DELTA12_FOURPARTITE_SUPPORT_KERNEL.md`.

For r in R let q=r_r be its omission weight and h_i(r) the number of target leave edges from r to T_i. Put h_r=sum_i h_i(r). Then
\[
\sum_{r\in R}q=7,
\qquad \sum_{r\in R}h_r=9,
\tag{1.1}
\]
and
\[
d_W(r)=5+\epsilon_r-h_r.
\tag{1.2}
\]
The universal low-W-degree lemma gives d_W(r)>=3 because epsilon_U>=1, hence
\[
h_r\le2+\epsilon_r.
\tag{1.3}
\]

At epsilon_U=2 the total W-excess is epsilon_W=2. The exact W profiles are:

1. `(3,4,5,6)` with no W-cross edge;
2. `(3,5,5,5)` with one W-cross edge;
3. `(4,4,4,6)` with one W-cross edge;
4. `(4,4,5,5)` with two W-cross edges.

For w in a q=0 clique component of size s, its support slack is y_w=6+epsilon_w-s. A W-cross edge only increases the W-internal degree and therefore lowers y by one at its endpoints.

We use `FOURPARTITE_SUPPORT_TRANSVERSAL_GAP.md`: if q<=2 and w is nonadjacent to r, then w is complete to one of the three T_i, except possibly when h_i(r)=2 and w is the unique degree-two W vertex carrying both W-excess units; only that one vertex may see exactly five points of T_i rather than all seven.

## 2. Full-label reuse across W components

If two H-nonadjacent W vertices w,w' are complete to the same T_i, then
\[
|N_U(w)\cap N_U(w')|\ge7.
\]
The W common-neighbour capacity theorem gives
\[
y_w+y_{w'}\ge7.
\tag{2.1}
\]

In each of the three profiles with W-cross edges, every **nonadjacent** cross-component pair has y-sum at most six even after both W-excess units are placed on that pair:

- `(3,5,5,5)`: base cross-component maximum 3+1=4, plus two excess =6;
- `(4,4,4,6)`: base maximum 2+2=4, plus two =6;
- `(4,4,5,5)`: base maximum 2+2=4, plus two =6.

Therefore a full T-label may occur in two different W-components only on the endpoints of an actual W-cross edge. In the no-cross `(3,4,5,6)` profile, a repeated full label is possible only between K3 and K4 vertices whose two excesses sum to two.

We also use the K12 cap: if a W clique component has s vertices and its r-nonneighbours are all complete to one T7, at most four of those s vertices may be nonneighbours of r. Thus every full-labelled K5 contributes at least one r-neighbour and every full-labelled K6 contributes at least two.

## 3. Local lemma for q<=2 and epsilon_r=0

Let r in R satisfy
\[
q\le2,\qquad \epsilon_r=0.
\tag{3.1}
\]
Then d_W(r)=5-h_r<=5 and h_r<=2.

### 3.1 The three W-cross-edge profiles are impossible

Consider first `(3,5,5,5)` with one W-cross edge.

If r is complete to a W-component, then:
- a full K3 costs three neighbours and each of the three K5 components requires at least one further neighbour, total at least six;
- a full K5 costs five and the other K5 components force additional neighbours.
So d_W(r)>=6, contradiction.

Assume no component is complete to r. All four components contain r-nonneighbours. Apart from the unique possible five-point partial-label vertex, full labels cannot repeat across components except at the single W-cross edge. A label shared across that edge can occur only on its two endpoints: another occurrence in either incident component would form a nonadjacent same-label cross pair. The three K5 components each have at least four full-labelled r-nonneighbours unless the unique partial vertex lies there; but the partial vertex can only have W-internal degree two, hence lies in the K3, not in a K5. Thus each K5 requires a component-exclusive full label. The three labels are exhausted by the three K5 components, leaving no valid full label for the K3 nonneighbours. If h_r=2 the partial exceptional K3 vertex can use a five-point label, but d_W(r)=3 and the three K5 components already require one neighbour each, leaving the other two K3 vertices as full-labelled nonneighbours with no available label. Contradiction.

The `(4,4,4,6)` profile has no possible five-point partial-label vertex because every W vertex has W-internal degree at least three. With no full component, four nonempty components must be covered by three full labels and the only possible cross-component label sharing is the one physical cross edge. If a shared label uses that edge, each incident component can have only its endpoint in that shared label; any further nonneighbours need component-exclusive labels. The K6 has at least four nonneighbours and therefore requires an exclusive label. Counting the remaining K4 components forces a fourth label, impossible. If a component is full, a K4 plus the mandatory two K6 neighbours already costs six, while a full K6 costs six. Contradiction.

For `(4,4,5,5)` with two W-cross edges, again no five-point partial exception exists. A full component costs at least six after the two K5 mandatory-neighbour contributions. If no component is full, any label spanning two components consists exactly of the endpoints of one physical cross edge. Such a shared label cannot serve as the bulk label of either component. Covering four nonempty components with only three labels therefore requires both cross edges to be used as two shared singleton labels; the third label can be bulk-exclusive to at most one component. At least three components then have only one nonneighbour, which costs at least
\[
(4-1)+(4-1)+(5-1)=10
\]
r-neighbours, far above d_W(r)<=5. Contradiction.

Hence none of the three W-cross-edge profiles admits (3.1).

### 3.2 Rigidity in the no-cross `(3,4,5,6)` profile

A full W-component again gives d_W(r)>=6: a full K3 still requires one neighbour in K5 and two in K6; a full K4/K5/K6 costs at least as much. Hence every W-component contains an r-nonneighbour.

There are four components and only three T-labels, so some full label must repeat across components unless the unique partial five-point exception is used. By Section 2 the only possible full-label repetition is between K3 and K4, and the two vertices involved must carry both W-excess units between them.

If h_r=2, then d_W(r)=3. The only possible partial label is a K3 vertex carrying both W-excess units. The K5 and K6 already force at least one plus two neighbours, consuming all three neighbours. Thus every K3 and K4 vertex is a nonneighbour. The two ordinary K3 vertices require full labels; K5 and K6 require two distinct full labels; K4 requires a third. No label remains for an ordinary K3 vertex without producing a forbidden cross-component full-label repetition. Contradiction.

If h_r=1, there is no five-point partial exception and d_W(r)=4. A repeated K3-K4 label is necessary. If the two excess units are split between a unique K3/K4 pair, all other two K3 and three K4 vertices must be r-neighbours; together with one K5 and two K6 neighbours this already exceeds four. If both excess units lie on a K4 vertex, the other three K4 vertices plus the K5/K6 mandatory neighbours give at least six. If both lie on a K3 vertex, the other two K3 vertices plus the K5/K6 mandatory neighbours give five. Contradiction.

Therefore h_r=0 and d_W(r)=5. The same count shows the only possible excess placement is:

- one K3 vertex w* carries both W-excess units;
- w* and all four K4 vertices are complete to one common T7;
- the other two K3 vertices are r-neighbours;
- exactly one K5 vertex is an r-neighbour, with the other four K5 vertices complete to a second T7;
- exactly two K6 vertices are r-neighbours, with the other four K6 vertices complete to the third T7.

Indeed if the excess is split over a K3/K4 pair, five other K3/K4 vertices are forced to be neighbours and the total neighbour cost is at least eight; if both excesses lie on K4, the cost is at least six. Only concentration on one K3 gives the exact degree-five pattern.

We have proved the local rigidity statement
\[
\boxed{
q\le2,\ \epsilon_r=0
\Longrightarrow
\begin{cases}
H[W]=K_3+K_4+K_5+K_6,\\
h_r=0,\\
\text{the unique capacity-equality pattern above holds.}
\end{cases}}
\tag{3.2}
\]

## 4. Global omission/target-incidence contradiction

Because the eight omission weights are nonnegative integers summing to seven, at most two R points can have q>=3. Hence at least six points satisfy q<=2.

Only two U-excess units exist in the entire U. Therefore among those at least six low-omission points, at least four have epsilon_r=0. By (3.2), each such point has
\[
h_r=0.
\]
Let Z be the set of R points with q<=2 and epsilon_r=0. Thus
\[
|Z|\ge4,
\qquad \sum_{r\in Z}h_r=0.
\tag{4.1}
\]

If |Z|>=5, the remaining at most three R points must carry all nine target leave edges. But by (1.3),
\[
\sum_{r\notin Z}h_r
\le2|R\setminus Z|+\sum_{r\notin Z}\epsilon_r
\le6+2=8,
\]
contradiction. Therefore
\[
\boxed{|Z|=4.}
\tag{4.2}
\]

All four remaining R points must have h_r>0; if one had h_r=0, only three points would carry the total nine and the same `<=8` bound would apply.

Among these four active points, at most two can have positive epsilon_r. Hence at least two active points have epsilon_r=0. By (3.2), an epsilon-zero point with q<=2 would have h_r=0, contradicting activity. Therefore at least two active points satisfy
\[
q\ge3.
\]
The other two active points have h_r>0, hence q>=1. Consequently
\[
\sum_{r\in R}q
\ge3+3+1+1=8,
\]
contradicting the exact omission sum seven.

Thus no epsilon_U=2 four-partite core exists:
\[
\boxed{
\delta=12,\ L_U\text{ four-partite},\ \epsilon_U=2
\Longrightarrow\bot.
}
\]

## 5. Dependency audit

The proof uses only:
1. the exact `(7,7,7,8)` four-partite support kernel and omission/target-leave identities;
2. the exact epsilon_U=2 W-profile list;
3. the pure support transversal gap lemma in `FOURPARTITE_SUPPORT_TRANSVERSAL_GAP.md`;
4. the W common-neighbour capacity theorem;
5. the universal d_W(r)>=3 low-W-degree lemma;
6. pure alpha(H)<=4 and omega(H)<=11 reasoning.

No Didin theorem and no non-four-partite augmentation classification is used. The delta=12 four-partite epsilon_U=0,1 branches remain open.