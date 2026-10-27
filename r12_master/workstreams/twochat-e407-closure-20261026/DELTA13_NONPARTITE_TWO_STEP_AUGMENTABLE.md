# E407 Q32 — delta=13 non-four-partite two-step augmentable reduction

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict reduction** under the frozen 49-support/core contract and the registered Brouwer/Kang–Pikhurko equality theorem. The two-step augmentable branch is reduced to four terminal W-profile families; it is not yet fully excluded.

## 1. Contract and two-step augmentation

Assume

\[
\delta=13,\qquad e(L_U)=307,\qquad L_U=\overline{H[U]}\text{ is non-four-partite}.
\]

Suppose there exist two nonedges e_1,e_2 of L_U such that

\[
L^*=L_U+e_1+e_2
\]

is still K5-free. Since four-partiteness is hereditary to subgraphs, L* is non-four-partite. It has 309 edges, exactly the Brouwer maximum on 29 vertices, so the registered Kang–Pikhurko equality theorem applies.

The 49 support K4s remain edge-disjoint in L*. The witness-packing argument from the delta=15 equality theorem excludes the unbalanced KP base profiles (6,7,7,8) and (6,6,8,8). Hence L* has the balanced base

\[
P_1,P_2,P_3,P_4,\qquad |P_i|=7,
\]

with exceptional vertex x, distinguished y in P2, and nonempty proper A0 subset P1 of size a in {1,...,6}.

In H0=bar(L*):

\[
d_{H0[U]}(x)=13-a,\qquad d_{H0[U]}(y)=6+a.
\]

The original H[U]=bar(L_U) is obtained from H0[U] by adding the two target edges e1,e2. Let I_x,I_y be the numbers of those two edges incident with x,y. Then

\[
 d_H(x,W)=a-1+\epsilon_x-I_x,
\]
\[
 d_H(y,W)=6-a+\epsilon_y-I_y,
\]
and therefore
\[
\boxed{d_H(x,W)+d_H(y,W)
=5+\epsilon_x+\epsilon_y-I_x-I_y
\le5+\epsilon_U.}
\tag{1.1}
\]

## 2. Universal three-neighbour lemma at delta=13

### Lemma 2.1

For every u in U,

\[
\boxed{d_H(u,W)\ge3.}
\tag{2.1}
\]

### Proof

At delta=13,

\[
e(H[W])=35-\epsilon_U,
\]
so J=bar(H[W]) is K5-free on18 vertices with
\[
e(J)=118+\epsilon_U\ge118.
\]

Suppose d_H(u,W)<=2 and put Z=N_H(u) cap W.
If |Z|<=1, then J[W\Z] has at least 118-17=101 edges on17 vertices, strictly more than t_3(17)=96. Hence H[W\Z] contains an independent4-set, which together with u contradicts alpha(H)<=4.

If |Z|=2, J[W\Z] has at least
\[
118-(\binom{18}{2}-\binom{16}{2})=118-33=85=t_3(16)
\]
edges. If epsilon_U>=1 the lower bound is at least86, immediately forcing an independent4-set in H[W\Z].

For epsilon_U=0, equality throughout would be necessary to avoid such a set. Then J[W\Z] is the Turan graph T_3(16), while both vertices of Z are adjacent in J to every possible incident vertex, including each other. Equivalently H[W] consists of the three clique components complementary to T_3(16) together with two H-isolated vertices. Choosing one vertex from each clique component together with the two isolated vertices gives an independent5-set in H[W], contradicting alpha(H[W])<=4.

Thus d_H(u,W)>=3 in every case. QED.

Combining (1.1) and (2.1),
\[
6\le d_H(x,W)+d_H(y,W)\le5+\epsilon_U.
\tag{2.2}
\]
In particular
\[
\boxed{\epsilon_U=0\text{ is impossible in the two-step augmentable branch}.}
\tag{2.3}
\]

## 3. W-side profiles for epsilon_U=1,2,3

For epsilon_U>=1,
\[
e(\overline{H[W]})=118+\epsilon_U\ge119,
\]
which is above the 18-vertex non-four-partite K5-free Brouwer bound 118. Hence bar(H[W]) is four-partite. Exact partition arithmetic gives:

### epsilon_U=1, e(H[W])=34

Possible target clique-part profiles:
- (3,4,5,6), no W-cross edge;
- (3,5,5,5), one W-cross edge;
- (4,4,4,6), one W-cross edge;
- (4,4,5,5), two W-cross edges.

### epsilon_U=2, e(H[W])=33

Possible profiles:
- (3,5,5,5), no cross edge;
- (4,4,4,6), no cross edge;
- (4,4,5,5), one cross edge.

### epsilon_U=3, e(H[W])=32

Only
\[
(4,4,5,5)
\]
with no cross edge.

## 4. Saturation cost and terminal reduction

When H[W] is a disjoint union of four clique parts, every u in U must be complete to one whole part; otherwise one non-neighbour from each part together with u is an independent5-set.

With one W-cross edge between parts of sizes s_i,s_j, an unsaturated u needs at least s_i+s_j-2 W-neighbours; with the listed sizes this is at least six. In the two-cross-edge (4,4,5,5) profile, an unsaturated u needs at least five neighbours, while any saturated vertex needs at least four.

### epsilon_U=1

Equation (2.2) forces
\[
d_W(x)+d_W(y)=6,
\quad \epsilon_x+\epsilon_y=1,
\quad I_x=I_y=0.
\]
Thus x and y each have exactly three W-neighbours and must both be complete to a K3 component. The profiles with minimum part size four are impossible. Therefore only:

1. H[W]=K3 dotcup K4 dotcup K5 dotcup K6, no cross edge;
2. H[W] has base clique sizes (3,5,5,5) and one cross edge.

Solving the individual degree equations gives exactly
\[
(a,\epsilon_x,\epsilon_y)=(3,1,0)
\quad\text{or}\quad(4,0,1).
\tag{4.1}
\]
Both added edges e1,e2 avoid x and y.

### epsilon_U=2

The profiles with minimum part size four are impossible because x,y would need at least eight W-neighbours in total, while (1.1) gives at most seven. Hence only
\[
\boxed{H[W]=K3\dot\cup K5\dot\cup K5\dot\cup K5}
\tag{4.2}
\]
remains. Both x and y must be complete to the K3 component. Their degree sum is six or seven.

### epsilon_U=3

The only W-profile is K4 dotcup K4 dotcup K5 dotcup K5. Both x and y must be saturated. Equation (1.1) and the minimum 4+4 force
\[
d_W(x)=d_W(y)=4,
\quad \epsilon_x+\epsilon_y=3,
\quad I_x=I_y=0.
\tag{4.3}
\]
Thus all U-excess lies on x,y and each is complete to a K4 component. Their KP parameter satisfies
\[
a=5-\epsilon_x=2+\epsilon_y,
\]
so a in {2,3,4,5} according to the split of the three excess units.

## 5. Interaction with the two added leave edges

Every P3P4 edge of the balanced KP equality graph is used by one support block, so neither added edge e1,e2 has type P3P4. By (4.1) and (4.3), in the epsilon_U=1 and epsilon_U=3 terminals neither added edge is incident to x or y. Consequently each added edge has at least one endpoint in
\[
P_1\cup(P_2\setminus\{y\}).
\]
Such an endpoint z has original
\[
d_H(z,W)=5+\epsilon_z-I_z.
\]
For epsilon_U=1 all U-excess already lies on x or y, so every such endpoint has d_H(z,W)<=4. In either surviving epsilon_U=1 W-profile it is therefore forced to be complete to the K3 component. Hence the common neighbourhood in U of that K3 contains x,y and at least one additional endpoint z.

This recovers a key ingredient of the delta=14 one-edge terminal, but now with two added leave edges. No terminal contradiction is claimed here because the W-profile (3,4,5,6) and the second added edge change the common-neighbour capacity bookkeeping.

## 6. Strict branch conclusion

The entire two-step augmentable delta=13 non-four-partite branch has been reduced to the following four terminal W-profile families:

| epsilon_U | surviving W profile | forced exceptional structure |
|---:|---|---|
| 1 | K3+K4+K5+K6, no cross | x,y complete K3; a=3 or4; e1,e2 avoid x,y |
| 1 | (3,5,5,5)+one cross | x,y complete K3; a=3 or4; e1,e2 avoid x,y |
| 2 | K3+3K5, no cross | x,y complete K3; degree sum 6 or7 |
| 3 | 2K4+2K5, no cross | d_W(x)=d_W(y)=4; all U-excess on x,y; e1,e2 avoid x,y |

The epsilon_U=0 branch is excluded.

## 7. Remaining non-four-partite fork

Starting from a 307-edge non-four-partite L_U, greedy K5-safe augmentation yields one of:

1. two-step augmentable: reduced above to four terminals;
2. exactly one augmentable edge, after which the 308-edge graph is K5-saturated;
3. L_U itself is K5-saturated at 307 edges.

No conclusion from the old delta=14 core closure is imported into cases 2 or3, because adding a leave edge changes H[U] and does not preserve the original 284-edge core. Any further use of saturated-graph structure must be purely graph-theoretic or separately rederived.