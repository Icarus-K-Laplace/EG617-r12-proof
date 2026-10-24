# Low-Degree Near-Anchor Top-Layer Closure

**Status:** PROVED_SYMBOLIC relative to the exact W-local Cell A/B normal form.  
**Range:** r ≥ 25.  
**Purpose:** close the remaining delta=r, |W|=2r−1 interface left open by the high-degree Cell A/B edge-count proofs.

## 1. Contract

Let F be the target graph of a hypothetical contextual 5r+1 terminal with
- alpha(F) ≤ 5;
- omega(F) ≤ r−1;
- the full balanced-colouring constraints, so every non-target colour graph has independence number at most r;
- an independent target triple T={x,y,z} with degree pattern (r, ≤r+1, ≤r+1);
- common target anti-neighbourhood W of T with |W|=2r−1.

Because delta(F)=r in this branch, each of the three anchor degrees is in {r,r+1} and at most two anchors have degree r+1.

The exact W-local theorem GENERAL_R_NEAR_ANCHOR_2R_MINUS1_NORMAL_FORM.md gives exactly two cases:

- **Cell A:** all non-target colours on W are near-perfect matchings; the set of vertices isolated in at least one such matching has size at most five.
- **Cell B:** the non-target union on W is S(K_(r−1,r−1)); the ordinary colours are near-perfect matchings and one exceptional colour is the subdivided-factor colour.

We use only these W-local normal forms, not the separate high-degree edge-count contradictions.

## 2. Pointwise target-degree bound into W

Let O=V(F)\W, so |O|=3r+2.

### Cell A

For each non-target matching colour, an outside vertex o must send at least one edge of that colour into W to keep alpha(G_i)≤r. The only one-edge certificate is an edge to that colour's isolated vertex; otherwise two edges covering a matching edge are needed. Since at most five W-vertices are isolated in any non-target colour and each edge o-w has only one colour, at most five colours can use the one-edge certificate. Hence
\[
\#\{\text{non-target-colour edges from }o\text{ to }W\}
\ge5+2((r-1)-5)=2r-7,
\]
so
\[
d_F(o,W)\le(2r-1)-(2r-7)=6.
\]

### Cell B

There are r−2 ordinary matching-plus-isolate colours and one exceptional subdivided-factor colour. At most one ordinary colour can use the single edge to the common isolate w; every other ordinary colour needs two edges, and the exceptional colour needs at least one. Thus at least
\[
1+2((r-2)-1)+1=2r-4
\]
non-target edges from o to W are necessary, giving
\[
d_F(o,W)\le(2r-1)-(2r-4)=3.
\]

Therefore in either cell,
\[
\boxed{d_F(o,W)\le6\quad\text{for every }o\notin W.}
\]

## 3. The complement on O is K4-free

We claim alpha(F[O])≤3 for r≥25.

If Q⊂O were a target-independent 4-set, its target neighbourhood in W would have size at most 4·6=24. Hence at least
\[
|W|-24=2r-25>r-1
\]
vertices of W would be target-nonadjacent to every vertex of Q. Since omega(F[W])≤r−1, those vertices cannot form a target clique; choose a target-nonadjacent pair u,v among them. Then Q∪{u,v} is a target-independent 6-set, contradicting alpha(F)≤5.

Thus alpha(F[O])≤3, so J=overline{F[O]} is K4-free.

## 4. Every vertex outside T∪W sees at least one anchor

Put O'=V(F)\(T∪W), so |O'|=3r−1.

Fix o∈O'. Suppose o is target-nonadjacent to all three anchors. For every target-nonedge uv inside W, the six-set T∪{o,u,v} would be target-independent unless o were target-adjacent to u or v. Therefore N_F(o,W) is a vertex cover of J_W=overline{F[W]}.

But
\[
\tau(J_W)=|W|-\alpha(J_W)
=|W|-\omega(F[W])\ge(2r-1)-(r-1)=r.
\]
Consequently d_F(o,W)≥r, contradicting the pointwise bound d_F(o,W)≤6 for r≥25.

Hence every o∈O' is target-adjacent to at least one anchor in T.

## 5. Duplicate-incidence budget

Let d_x,d_y,d_z be the three anchor degrees. Since each lies in {r,r+1}, write
\[
d_x+d_y+d_z=3r+k,\qquad k\in\{0,1,2\}.
\]
All anchor-target edges go into O', because T is independent and W is the common anti-neighbourhood. Every vertex of O' has at least one anchor neighbour, so the total number of duplicate anchor incidences is
\[
D=(d_x+d_y+d_z)-|O'|=(3r+k)-(3r-1)=k+1\le3.
\]
If m_2 vertices of O' see exactly two anchors and m_3 see all three, then
\[
m_2+2m_3=D,
\qquad
H:=2m_2+3m_3=2D-m_3\le2(k+1),
\]
where H is the total number of anchor incidences at multiply-attached vertices.

For t∈T, let h_t be the number of its neighbours in O' that are also adjacent to at least one other anchor. Its unique-anchor neighbourhood U_t has size d_t−h_t.

## 6. Unique-anchor neighbours form a clique

Take any two vertices u,v∈U_x. Both are target-nonadjacent to y,z, so in J they are adjacent to y,z. Also yz∈E(J), because T is target-independent.

If uv were an edge of J, then {u,v,y,z} would form a K4 in J, impossible. Therefore uv is a target edge. It follows that U_x∪{x} is a target clique, and similarly for y,z.

Since omega(F)≤r−1,
\[
d_t-h_t+1\le r-1,
\qquad h_t\ge d_t-r+2.
\]
Thus h_t≥2 for an anchor of degree r and h_t≥3 for an anchor of degree r+1. Summing over T,
\[
H=\sum_{t\in T}h_t
\ge2(3-k)+3k=6+k.
\]
But §5 gave H≤2(k+1)=2k+2. Hence
\[
6+k\le2k+2\quad\Longrightarrow\quad k\ge4,
\]
contradicting k∈{0,1,2}.

## 7. Theorem

> **Low-degree top-layer nonextension.** For every r≥25, no contextual 5r+1 terminal with delta(F)=r can have an independent near-anchor triple of degree pattern (r,≤r+1,≤r+1) whose common target anti-neighbourhood has size 2r−1.

Together with the high-degree Cell A/B exclusions, this closes the entire |W|=2r−1 interface for all r≥25.

This is a terminal-interface theorem, not an unconditional Erdős Problem 617 proof: the front-end extraction interface and the lower-offset cases remain open.
