# Unified r=12 closure in the focus/rectangle language

This file removes the last proof-engineering residue in the parameterized Exact Three-Anchor Excess proof. No historical fixed-r case table is used.

Assume throughout r=12, |H|=35, alpha(H)<=3, omega(H)<=11, delta(H)>=12, and three pairwise nonadjacent degree-12 anchors. By parity, any counterexample to K>=8 has K<=6.

We use the notation and lemmas from PROOF_ATTEMPTS.md. In particular, every exclusive block Xi is a clique, pair-connector nonneighbour sets form complete rectangles, and two nonadjacent connectors have a common-nonneighbour set which is a clique.

## Arithmetic charge facts at r=12

For positive integers a,b and connector excess k<=6, write

R22=a(b-2)_+ + b(a-2)_+,
R23=a(b-2)_+ + b(a-3)_+,
R24=a(b-2)_+ + b(a-4)_+,
R33=a(b-3)_+ + b(a-3)_+.

The only bounds used below are the following elementary threshold consequences.

1. If a+b>=9-k+gamma, then k+R23>=4+gamma.
2. If a+b>=9-k+gamma, then k+R22>=5+gamma for gamma=0,1, and is at least 8 for gamma>=2. Under k+R22<=6:
   - gamma=1 forces (k,a,b)=(6,2,2);
   - gamma=0 has a+b+k=9 except for the single possibility (k,a,b)=(6,2,2), where a+b+k=10.
3. If a+b>=8-k+gamma, then
   - k+R24>=2+gamma;
   - after one focused neighbour has consumed one X3 slot, k+R23>=3+gamma;
   - after two focused neighbours have consumed two X3 slots, k+R22>=4+gamma.
   Moreover, if gamma>=1 and k+R24<=3, the unique possibility is gamma=1, (k,a,b)=(3,4,2).
4. If a+b>=8-k+gamma, then k+R33>=2+gamma; with one incident focus slot occupied the effective R23 bound is >=3+gamma; with both occupied the effective R22 bound is >=4+gamma.

All of these follow by splitting according to whether a and b are above their capacity thresholds. No graph enumeration is involved.

---

## A. c=3, block sizes (10,10,9)

There is one triple connector w and two pair connectors u,v. The pair connectors are both incident with X3. Call one focused when it is complete to X3.

Both nonfocused is impossible: the two R23 charges are additive and cost at least 4+4=8.

Both focused is impossible: they cannot be adjacent, since X3+a3+u+v would be a 12-clique. If they are nonadjacent, their common nonneighbour set has size at least

33-[(12+k_u)+(12+k_v)-10] = 19-k_u-k_v >=13,

and is a clique, contradicting omega(H)<=11.

Hence exactly one pair connector, say u, is focused, and v is nonfocused. Let A subset X1 and B subset X3 be the v-nonneighbour rectangle. The focus of u lowers the effective X3 capacity from 3 to 2, so the rectangle is governed by R22 and

a+b>=9-k_v+gamma_v.

If gamma_v>=2, the local charge already exceeds six.

If gamma_v=1, the unique low-budget possibility is

(k_v,a,b)=(6,2,2).

All other vertices are exact and v has no X2 neighbours. Exactly one of uv,vw is an edge. Choose x in A. It is exact and its two external slots are the two vertices of B, so it is nonadjacent to both connectors other than v and to all of X2.

- If vw is a nonedge, then for every y in X2 the set {v,w,x,y} would be independent unless wy is an edge. Thus w is complete to X2, and X2+a2+w is a 12-clique.
- If vu is a nonedge, the same argument forces u to be complete to X2. But u is exact and already has its two anchor neighbours plus all nine vertices of X3, leaving only one degree slot, contradiction.

Now suppose gamma_v=0. If a+b+k_v=9, then v has no X2 neighbour. Every low-budget rectangle contains a rectangle vertex whose effective external capacity is saturated by the forced rectangle edges; in the unique local-cost-five case (k,a,b)=(5,2,2), parity leaves only one spare excess unit, so one of the four rectangle vertices is still saturated. Such a saturated vertex s is nonadjacent to w and to all of X2. Since v is also nonadjacent to w and all of X2, {v,w,s,y} forces wy for every y in X2. Again X2+a2+w is a 12-clique.

The only remaining gamma_v=0 possibility is (k,a,b)=(6,2,2), for which v has exactly one X2 neighbour y0 and every other vertex is exact. Choose x in A. Then x is saturated by B and is nonadjacent to u and X2. For every y in X2\{y0}, {v,u,x,y} forces uy. Thus exact focused u would have at least nine X2 neighbours in addition to its two anchors and nine X3 neighbours, impossible.

Therefore c=3 is impossible already at r=12.

---

## B. c=4, deficits (0,0,2), block sizes (10,10,8)

There are two connectors in each missing-anchor group; all four are incident with a3. A connector is focused when it is complete to X3.

### B1. Focus cap

Two focused connectors cannot be nonadjacent: their common nonneighbour set has size at least

33-[(12+k_p)+(12+k_q)-9] = 18-k_p-k_q >=12>11,

and hence would be a clique larger than allowed. Thus focused connectors are pairwise adjacent. Three focused connectors together with X3+a3 form a 12-clique, so the number f of focused connectors satisfies f<=2.

### B2. f=0

All four connectors are nonfocused. If neither same-group pair is adjacent, same-group rectangles have disjoint supports and all four charges add, giving K>=8.

If exactly one same-group pair is adjacent, take one connector from that adjacent pair and both connectors from the nonadjacent pair. Their rectangle charges add. The adjacent connector has gamma>=1 and local charge at least 3; the other two have charge at least 2 each. Hence K>=7.

If both same-group pairs are adjacent, every connector has gamma>=1. Any cross-group pair has additive charge at least 3+3=6. Under K<=6, every connector must attain local charge exactly three. The r=12 R24 equality is unique: gamma=1, k=3, (a,b)=(4,2). This would put excess three on all four connectors, already giving connector excess twelve. Contradiction.

### B3. f=1

One focus neighbour consumes one X3 slot, so every nonfocused rectangle is governed by effective R23 and has local charge at least 3+gamma. There are three nonfocused connectors. One lies in the same group as the focused connector and two in the other group.

The single connector from the first group has additive charge with either connector of the other group. Thus K<=6 would force all three nonfocused connectors to have gamma=0 and local charge exactly three. Then the two same-group nonfocused connectors are nonadjacent, so their supports are disjoint; all three charges add and give K>=9. Contradiction.

### B4. f=2

Two focus neighbours consume two X3 slots, so the two nonfocused rectangles are governed by effective R22 and each has local charge at least 4+gamma.

If the nonfocused pair is from different groups, their charges add and give K>=8. If they are same-group but nonadjacent, their supports are disjoint and again K>=8. Thus they are an adjacent same-group pair; the other-group pair is focused and adjacent.

For each nonfocused connector,

a+b>=9-k.

Since the two rectangles may overlap, K is at least k1+k2+max(R22_1,R22_2). The elementary R22 threshold table forces, under K<=6,

k1=k2=0, gamma1=gamma2=1,

and each rectangle has orientation (a,b)=(1,8) or (8,1), with R22=6. Equality of the union charge forces the two rectangles to have the same orientation and the same charged vertex (and, in the (8,1) orientation, the same eight-set support).

- Orientation (1,8). The common singleton x in the zero-deficit block carries all six excess units and is saturated by its eight X3 neighbours. Pick one nonfocused connector U and one focused connector V. U has no X1 neighbours and no edge to V; exact V has the two anchor neighbours, all eight X3 neighbours, and its focused-partner edge, hence at most one X1 neighbour. Choose z in X1 nonadjacent to V. Then {U,V,x,z} is independent, contradiction.

- Orientation (8,1). The common singleton y in X3 carries all six excess units and is saturated by the two focused connectors plus the eight rectangle neighbours. Pick nonfocused U and focused V. Their common nonneighbour set contains at least nine vertices of X1 and at least seven of the eight rectangle vertices in the zero block. That set must be a clique. But any such zero-block vertex is exact, already uses one external slot on y, and cannot be adjacent to nine X1 vertices. Contradiction.

Hence the (0,0,2) geometry is impossible at r=12.

---

## C. c=4, deficits (0,1,1), block sizes (10,9,9)

Let U1,U2 be the two connectors missing a1; let V miss a2 and W miss a3. Thus U-connectors are incident with both deficit-one blocks X2,X3; V is incident with X1,X3; W with X1,X2.

A focus slot Xi (i=2,3) is occupied when some connector incident with ai is complete to Xi.

### C1. Focus collision

No two connectors can occupy the same focus slot. If two such connectors are adjacent, Xi+ai plus them is a 12-clique. If nonadjacent, their common nonneighbour set has size at least

33-[(12+k_p)+(12+k_q)-10] = 19-k_p-k_q >=13,

and is a clique, again impossible.

Thus each of the X2 and X3 focus slots has occupancy at most one.

### C2. No occupied focus slot

Then V and W are both nonfocused. Their R23 rectangles overlap only in X1 and force neighbours into the disjoint opposite blocks X3 and X2, so their charges add. Each costs at least 4+gamma, hence K>=8.

### C3. Exactly one occupied focus slot

By symmetry suppose X3 is occupied.

If V owns the slot, then W and both U-connectors are nonfocused. W has local R23 charge at least 4+gamma; each U sees one incident focus neighbour, so its effective rectangle is R23 and costs at least 3+gamma. W plus either U have additive rectangles, giving K>=7.

If a U-connector owns the X3 slot, then V and W are nonfocused. V now has effective R22 charge at least 5+gamma, while W has R23 charge at least 4+gamma. Their rectangles are additive, giving K>=9.

So one occupied slot is impossible.

### C4. Both focus slots occupied

There are four ownership patterns.

1. The same U owns both slots. Then V,W are nonfocused; each has effective R22 charge at least five, and their rectangles add.
2. Two distinct U-connectors own the two slots. Again V,W are nonfocused and give additive charge at least ten.
3. One U and one of V,W own the slots. The remaining external connector has effective R22 charge at least five and the remaining U has effective R22 charge at least four; their rectangles are additive, giving at least nine.
4. V owns X3 and W owns X2. Then U1,U2 are the only nonfocused connectors. Both incident blocks have one focus neighbour, so each U-rectangle is governed by R22 and has local charge at least 4+gamma.

Only pattern 4 needs an overlap analysis. If U1,U2 are nonadjacent, same-missing-anchor disjointness makes their charges additive, giving K>=8. Hence they must be adjacent. Exactly as in B4, K<=6 forces

k1=k2=0, gamma1=gamma2=1,

and identical equality rectangles of orientation (1,8) or (8,1), carrying all six excess units on one exclusive vertex.

- Orientation (1,8): the charged singleton x lies in X2 and is saturated by the focused connector W plus eight X3 rectangle neighbours. Exact focused V has at most one X1 neighbour, while a nonfocused U has none. Choosing z in X1 nonadjacent to V makes {U,V,x,z} independent.
- Orientation (8,1): the charged singleton y lies in X3 and is saturated by focused V plus eight X2 rectangle neighbours. Exact focused W has at most one X1 neighbour, while nonfocused U has none. Choosing z in X1 nonadjacent to W makes {U,W,y,z} independent.

Thus the (0,1,1) geometry is impossible at r=12.

---

## Conclusion

The c=2 geometry was already closed uniformly for every r>=12. Sections A, B, C close the remaining three geometries at r=12 using exactly the same focus/rectangle machinery as the r>=13 proof.

Therefore the Exact Three-Anchor Excess Theorem now has a single analytic proof for every r>=12:

> If r>=12, |H|=3r-1, alpha(H)<=3, omega(H)<=r-1, delta(H)>=r, and H contains three pairwise nonadjacent degree-r vertices, then K_r(H)>=8.

Status: PROVED_ANALYTIC / Level 4.
