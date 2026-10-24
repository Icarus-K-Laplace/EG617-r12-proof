# R12 witness-packing boundary kernel and cross-branch audit

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** for the incidence ledgers and the stated extreme-kernel classification; the global terminal remains OPEN.  
Scope: synthesize current R12 branch updates without changing sibling workstreams.

## 1. Live R12 branch intake

The repository search found no separate Icarus-K-Laplace repository for this R12 sprint; the live workstreams are branches in EG617-r12-proof. This workstream read the following current branch heads before deriving the results below:

- emergency sprint: 87a58429070cffbd90991045e0375102fcc4ec0d;
- emergency sprint chat: 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd;
- ultimate closure: 28f47fb7c8f273e6a70bf19f4ee961e8023f5981;
- witness packing: 38b5dcec008903cdc3487941e7c6fa078637fbc5;
- this zero-excess workstream before this update: f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777.

Relevant read-only inputs:
- R12_WITNESS_CAPACITY_CROSSCUT.md;
- R12_ROW_TRANSVERSAL_AND_Q33_PACKING.md;
- R12_E407_Q32_COLOR_FACTOR_CROSSCUT.md;
- R12_WITNESS_OVERLAP_STAR_LEMMA.md;
- WITNESS_PACKING_INCOMPATIBILITY.md.

The cross-branch state agrees that E407 Q32 and E408 Q33 share the 47-point, 284-edge core; E408 Q32 has a 285-edge core and must not be silently folded into this excess-four ledger.

## 2. Exact-129 component facts

Under the retained T61 / Kang–Pikhurko equality contract, each exact-129 color has ten disjoint isolated K5 components. With S of size three and B a target clique of size ten:

1. At least seven K5 components avoid S.
2. At most one of these seven can contain pivot p.
3. Therefore at least six components have the labelled form {b} union Q, with b in B and Q a four-set in H.
4. Each Q is independent in H and anticomplete to b; the six B labels are distinct and the six Q sets are disjoint within the color.
5. Across distinct colors, selected Q sets intersect in at most one vertex.

Since the 284-edge core has total degree excess four, at most four core vertices have degree above 12. Consequently each exact-129 color has at least two B-labelled Q witnesses whose four vertices all have core degree exactly 12.

For an eligible shell contract with at least five B labels b satisfying k_b>=2, every exact-129 color also has at least one B-labelled Q whose label has k_b>=2: six distinct labels cannot all lie among the at most five labels with k_b<=1. Such a Q must hit at least two S rows, or Q together with its label and an unhit missing hub would be an independent six-set in F.

These statements use the corrected six-B-labelled count, not the superseded claim of seven B-labelled witnesses.

## 3. Seven-witness packing and support lower bounds

Select seven Q-sets from each exact-129 color, including the possible H-part of a component {p} union Q. Within a color these seven Q-sets are disjoint; across colors they are linear (intersections at most one vertex).

Let c be the number of exact-129 colors, let V_* be the union of selected Q-sets, v=|V_*|, and let L=bar(H[V_*]). Every Q contributes six distinct edges to L, so e(L)>=42c. Also L is K5-free because alpha(H)<=4, so e(L)<=t_4(v).

The retained Brouwer second-Turán threshold gives the following support bounds:
- E407 Q32: c>=7, hence v>=29.
- E407 Q32: if c>=8, then v>=31.
- E408 Q33: c>=8, hence v>=31.
- E408 Q33: if c>=9, then v>=32.

For the first bound, v=28 would force L=T_4(28), so H[V_*]=4K_7. The remaining 19 core vertices would then span at most 32 edges by the exact core degree budget, but alpha<=4 forces at least 36 edges. For the second and third bounds, v=30 would force L to be four-partite; each pair of parts would need at least 56 available pairs for 56 edge-disjoint Q blocks, but no partition of 30 into four part sizes satisfies all pair-product bounds.

The surviving color-count profiles are still E407 129^7,130^4 and E408 Q33 129^8,130^3. The support theorem does not eliminate either profile.

## 4. Exact incidence ledger for E407 Q32 at v=29

Assume the unresolved E407 profile c=7 and the minimal support v=29. There are exactly 49 selected Q blocks, each color class contributing seven disjoint blocks and leaving one point of V_* uncovered.

For each v in V_*, let r_v be the number of selected Q blocks containing v, and set a_v=7-r_v. Then
\[
0\le r_v\le7,\qquad \sum_{v\in V_*}r_v=4\cdot49=196,\qquad \sum_{v\in V_*}a_v=7.
\]
Thus the seven color classes have exactly seven total omitted-point incidences across the 29-point union.

The 49 blocks contribute 294 distinct edges to L. Write
\[
e(L)=294+g,\qquad g\ge0.
\]
Since |V_*|=29, there are 406 possible pairs and
\[
e(H[V_*])=112-g.
\]
Let
\[
\epsilon_*=\sum_{v\in V_*}(d_H(v)-12),\quad 0\le\epsilon_*\le4,
\]
and let x=e_H(V_*,W), W=H\V_*, |W|=18. The exact degree sums and edge count give
\[
\boxed{x=124+\epsilon_*+2g},
\qquad
\boxed{e(H[W])=48-\epsilon_*-g}.
\]
Because alpha(H[W])<=4, Turán's complement bound gives e(H[W])>=32. Therefore
\[
\boxed{g+\epsilon_*\le16}.
\]
Every w in W must hit every selected Q block, or w plus Q would be an independent five-set in H. Each core vertex occurs in at most seven selected blocks, so d_H(w,V_*)>=7. Summing over W yields x>=126, hence
\[
\boxed{\epsilon_*+2g\ge2}.
\]

For a point v in V_*, let delta_v be the number of L-neighbours inside V_* not contributed by selected Q blocks. Then sum delta_v=2g, and the exact pointwise degree identity is
\[
\boxed{d_H(v,W)=5+\epsilon_v-3a_v+\delta_v}.
\]
For each w in W, writing T_w=N_H(w) intersect V_*, the block-incidence count gives
\[
\sum_{v\in T_w}r_v\ge49.
\]
Consequently |T_w|>=7. If |T_w|=7, every point of T_w has r_v=7 and every Q block meets T_w exactly once. This is an exact transversal condition, not just a lower bound.

The complete integer ledger for the minimal-support E407 boundary is therefore
\[
g\ge0,\quad 0\le\epsilon_*\le4,\quad
g+\epsilon_*\le16,\quad \epsilon_*+2g\ge2.
\]
It is a genuine reduction but still has multiple feasible pairs (g,epsilon_*).

## 5. Exact incidence ledger for E408 Q33 at v=31

Assume the unresolved E408 Q33 profile c=8 and the minimal support v=31. There are 56 selected Q blocks, and each color class leaves three points of V_* uncovered. Define r_v as above and a_v=8-r_v. Then
\[
0\le r_v\le8,\qquad \sum_{v\in V_*}r_v=4\cdot56=224,\qquad \sum_{v\in V_*}a_v=8\cdot31-224=24.
\]

The selected blocks contribute 336 distinct edges to L. Write e(L)=336+g, g>=0. Since there are 465 pairs on 31 vertices,
\[
e(H[V_*])=129-g.
\]
Let epsilon_* be the excess on V_*, and W=H\V_*, |W|=16. The exact budget gives
\[
\boxed{x=e_H(V_*,W)=114+\epsilon_*+2g},
\qquad
\boxed{e(H[W])=41-\epsilon_*-g}.
\]
Since alpha(H[W])<=4, e(H[W])>=24, hence
\[
\boxed{g+\epsilon_*\le17}.
\]
Every w in W hits all 56 blocks. Each core point occurs in at most eight selected blocks, so d_H(w,V_*)>=7. If it has exactly seven such neighbours, its neighbourhood consists only of points with r_v=8 and meets every Q exactly once.

The pointwise identity, with delta_v counting extra L-neighbours beyond the selected Q blocks and sum delta_v=2g, is
\[
\boxed{d_H(v,W)=6+\epsilon_v-3a_v+\delta_v}.
\]
The edge-count profile therefore confines the boundary to
\[
0\le g,\quad 0\le\epsilon_*\le4,\quad g+\epsilon_*\le17.
\]
In particular e(L)<=353, below the retained Brouwer threshold 355 that would force a 4-partite graph on 31 vertices. So the existing second-Turán theorem does not make this boundary exact; a stability or incidence argument is still needed.

## 6. E407 four-partite boundary audit — no TD(4,7) conclusion

Assume L is four-partite in the E407 v=29, m=49 boundary. The witness K4s force part sizes (7,7,7,8), and every pair between any two of the three seven-point parts is used exactly once. For each pair of a seven-point part and the eight-point part, 49 of the 56 possible pairs are used; each vertex in the seven-point part has exactly one unused partner in the eight-point part.

**Important correction.** The eight-point part is not proved to contain a point unused by every witness block. A point in that part may occur in one or more Q blocks; the unused pairs form a bipartite graph with degree one on the seven-point side, not necessarily a perfect matching on both sides. Consequently:
- the 49 blocks are not certified as a TD(4,7) on 28 active points plus one unused point;
- the 21 pairs not used by Q blocks are not all incident to one distinguished point;
- no conclusion such as \(\delta\ge12\), \(\epsilon_U=16-\delta\), or \(H[W]=K_5\dot\cup K_5\dot\cup K_4\dot\cup K_4\) follows from that invalid distinguished-point assumption.

The valid general E407 boundary ledger remains
\[
e(L)=294+\delta,\quad e(H[U])=112-\delta,\quad
e_H(U,W)=124+2\delta+\epsilon_U,\quad
e(H[W])=48-\delta-\epsilon_U,
\]
with
\[
0\le\epsilon_U\le4,\quad \delta+\epsilon_U\le16,\quad
\epsilon_U+2\delta\ge2.
\]
The independently proved transversal theorem further gives \(\delta\ge2\). The four-partite E407 boundary is still OPEN.

## 7. Cross-branch audit findings

### 7.1 The m=10 witness-star dichotomy needs correction

The sibling file R12_WITNESS_OVERLAP_STAR_LEMMA.md correctly proves that m witnesses sharing x give disjoint triples P_i, alpha(H[union P_i])<=3, and e(H[union P_i])>=3*C(m,2). However, its inference
\[
e(H[U])=135\quad\text{or}\quad e(H[U])\ge144
\]
does not follow from the second-Turán theorem. If e(H[U])<=143, the complement is tripartite, but need not be complete tripartite. The valid form is H[U]=3K_10 plus g cross-part edges with 0<=g<=8. The local configuration 3K_10 plus one cross edge between vertices from distinct P_i has e(H[U])=136, alpha(H[U])=3, and leaves every P_i independent. It disproves the local dichotomy, but is not a counterexample to the full 47-core contract. A global degree/excess argument would be required to rule out g=1,...,8.

### 7.2 The eight-no-S-component claim for templates C/D/E needs an extra lemma

The sibling crosscut file's extension from seven to eight S-avoiding K5 components for templates with an edge in M[S] is not implied by that fact alone. A missing edge inside S does not force its endpoints to lie in the same K5 component of every fixed non-target color; they may occupy separate components, with their mutual edge owned by another color. The universally justified count remains seven total Q-sets and six B-labelled Q-sets per exact-129 color unless additional color-specific forcing is supplied. The support bounds in Sections 3–5 deliberately use only the safe count.

## 8. Current maximum blocker

The next step is no longer to improve scalar witness counts. It is to eliminate the two minimal-support incidence kernels:
- E407: 49 linear K4 blocks on 29 points, with the exact (g,epsilon_*) ledger above and high-k / zero-excess labels;
- E408 Q33: 56 linear K4 blocks on 31 points, with g+epsilon_*<=17, 24 total incidence deficits, high-k labels, and the outer seven-block duplicate constraints.

Any continuation must charge each edge once, account for the maximum block multiplicity of a vertex, and preserve the difference between the 284-edge Q32/Q33 core and the 285-edge E408 Q32 core. No full EG617(r=12) proof is certified.


## 9. Current E407 four-partite kernel and next attack

The four-partite E407 boundary has part sizes (7,7,7,8), with 49 linear transversal K4 blocks. The three pairs among the seven-point parts are covered completely by the witness blocks. For each seven-by-eight pair type, exactly seven pairs remain uncovered, with exactly one uncovered partner for each vertex on the seven-point side; the eight-point-side degrees of the uncovered-pair graph are not fixed by the present contract.

The core-budget constraints remain
\[
0\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad\epsilon_U+2\delta\ge2.
\]
The non-four-partite branch, if established separately, would satisfy the corresponding second-Turán cap; do not infer non-four-partiteness merely by excluding the complete Turán graph.

Next attack: classify the three bipartite uncovered-pair graphs and the seven-per-color parallel classes jointly, using the per-vertex degree cap and the outside-core transversal neighborhoods. No distinguished eighth point or TD(4,7) completion is assumed.

## 10. Live sibling refresh and audit update

After the initial branch intake in Section 1, the following sibling heads advanced and were reread:
- ultimate closure: 0bdce893225af4273fa5f95d68815ff79c130446;
- witness packing: 5d0e3ceab7895be1a947e46853f92bb84477f4e5.

Two additional findings are now recorded.

First, the sibling R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md has a valid transversal floor tau(Q)>=7 and valid edge-budget identities, but its claimed conclusion that L is non-four-partite is not established by ruling out only the complete four-partite graph. A four-partite L may omit cross-part edges. The E407 delta=16 corner in Section 6 is a valid four-partite subcase; Section 9 extends that analysis to the full four-partite E407 branch.

Second, R12_BETA_SENSITIVE_ZERO_EXCESS_PACKING.md claims stronger B-labelled witness floors for beta=e(M[S])=1,2,3 by using omega(M[S]) to bound the number of K5 components meeting S. The stated implication is invalid: omega(M[S]) bounds the number of S vertices that one fixed-color component may contain, not the number of distinct components that can meet S. Three S vertices may occupy three different K5 components. Without a color-specific co-location theorem, do not promote those beta-sensitive counts. The safe universal floor remains seven total S-avoiding Q sets and six B-labelled ones per exact-129 color, giving at least two zero-excess B-labelled witnesses per color.

The transversal floor itself remains usable: every vertex outside the selected witness union has at least seven neighbours into it. No terminal is certified closed.


## 11. E408 Q33 four-partite branch: a stronger transversal-capacity floor

Assume the E408 Q33 v=31 boundary and that L is four-partite. The 56 edge-disjoint Q blocks force part sizes (8,8,8,7). Write A,B,C for the three eight-point parts and D for the seven-point part.

For each pair D-A, D-B, and D-C there are exactly 56 possible pairs and 56 blocks, so every such pair occurs in exactly one Q block. Every point of D therefore occurs in eight blocks, while every point of A union B union C occurs in seven blocks. The 24 pairs not covered by Q blocks are the eight missing pairs in each of A-B, A-C, and B-C. Since L is four-partite, its extra edges beyond the 336 witness edges can only be among these 24 pairs. Thus delta=e(L)-336 counts selected extra L edges among them, and the H-edges between the three large parts number exactly 24-delta.

The core budget still gives delta+epsilon_U<=17. The exact core degree identities give:
- each point of D has degree 6 inside H[U] and hence d_H(v,W)=6+epsilon_v;
- each point of A union B union C has degree 7 plus its H-neighbours among the unrepresented pairs of the other large parts;
- x=e_H(U,W)=114+epsilon_U+2delta;
- e(H[W])=41-epsilon_U-delta.

Every w in W must hit all 56 Q blocks. If it has exactly seven neighbours in U, those seven points must all have block-incidence eight, hence they are exactly D: each Q contains one D point, and the seven points of D hit all 56 blocks. At most six W vertices can have exactly seven neighbours in U, because at least three vertices of D have epsilon_v=0 (the total core excess is only four), and each such vertex has exactly six neighbours in W. If n_7 is the number of W vertices with seven neighbours in U, then
\[
x\ge 7n_7+8(16-n_7)=128-n_7\ge122.
\]
Combining with x=114+epsilon_U+2delta yields the new necessary inequality
\[
\boxed{\epsilon_U+2\delta\ge8}.
\]
Therefore the E408 Q33 four-partite boundary must satisfy
\[
\boxed{\delta+\epsilon_U\le17,\qquad \epsilon_U+2\delta\ge8}.
\]
In particular delta cannot be 0 or 1. This does not yet eliminate the four-partite branch; it sharpens the remaining integer kernel without assuming that L is complete four-partite.


## 12. E408 Q33 four-partite branch: exclude epsilon_U+2delta=8,9

Continue under the four-partite E408 setup of Section 11. Let
\[
S_0=\epsilon_U+2\delta,
\qquad x=114+S_0.
\]
Section 11 gives S_0>=8. We now prove the stronger necessary condition
\[
\boxed{S_0\ge10}.
\]

Suppose S_0 is 8 or 9. Let k be the number of W vertices with exactly seven neighbours in U. Section 11 proves that each such neighbourhood is exactly D, the seven-point part. Since every W vertex has at least seven neighbours in U,
\[
x\ge 7k+8(16-k)=128-k.
\]
As x=114+S_0 and k<=6, this forces k=6 when S_0=8, and k in {5,6} when S_0=9. The remaining 10 or 11 vertices therefore have neighbourhood size 8 or 9 only:
- S_0=8: ten vertices of size 8;
- S_0=9, k=6: nine of size 8 and one of size 9;
- S_0=9, k=5: eleven of size 8.

For a hitting set T of size 8 or 9, the block-incidence structure gives a simple classification. If T omits a point d in D, then the eight blocks containing d must be hit by vertices in A union B union C; pair uniqueness means at least eight such vertices are required. Thus a size-8 hitting set omitting D lies entirely in A union B union C, and a size-9 hitting set omitting D contains at most one point of D. If no one of the three large parts were fully contained in T, pair uniqueness at a missing point of each large part would force each large-part intersection to have size at most one (for |T|=8) or at most two (for |T|=9), too few to reach the required total size. Hence every size-8 or size-9 hitting set either contains all of D or contains an entire large part A, B, or C.

At least three vertices of D have zero excess, so each has exactly six neighbours in W. The k vertices with neighbourhood D already use all k of these incidences. Therefore at most 6-k additional W vertices can have a neighbourhood containing D. Since there are 16-k vertices outside the size-7 class, at least
\[
(16-k)-(6-k)=10
\]
of them must have neighbourhood equal to a full large part.

It remains to bound how many W vertices can be adjacent to a given large part G. For each pair of large parts, the eight pairs not used by Q blocks form a perfect matching: each vertex of either large part occurs in seven blocks, so exactly one of its eight possible partners is omitted. Thus each vertex of G has two potential H-neighbours in the other large parts, one from each of the two missing-pair matchings. The delta extra L-edges can affect at most delta vertices of G, so at least 8-delta vertices of G retain both H-neighbours. Since the excess sum in U is epsilon_U=S_0-2delta, at least
\[
8-\delta-\epsilon_U=8+\delta-S_0
\]
of these vertices have zero excess. Under S_0 in {8,9}, delta>=2 (otherwise epsilon_U=S_0-2delta>4), so this number is at least one. Such a vertex has core degree 12, degree 7+2=9 inside U, and therefore exactly three neighbours in W. Every W vertex whose neighbourhood contains the full group G is adjacent to this vertex, so at most three W vertices can have G as their full-group neighbourhood.

There are three large parts, hence at most nine W vertices can have a full-large-part neighbourhood. This contradicts the ten required above. Therefore
\[
\boxed{\epsilon_U+2\delta\ge10}
\]
in the E408 Q33 four-partite branch.

This closes the S_0=8 and S_0=9 layers only. The remaining four-partite integer kernel has S_0>=10, delta+epsilon_U<=17; it is still OPEN.


At the equality boundary S_0=10, the same argument leaves only one incidence pattern. If k<=5, at least ten of the remaining W vertices have size-8/9 full-large-part neighbourhoods, exceeding the capacity of nine. If k=6 but the remaining ten vertices have two size-9 neighbourhoods rather than one size-10 neighbourhood, all ten are again full-large-part neighbourhoods, impossible. Thus the only unexcluded equality pattern is:
- k=6 vertices have neighbourhood exactly D;
- nine vertices have size-8 neighbourhoods equal to large parts, exactly three assigned to each of A,B,C;
- one vertex w_* has a size-10 hitting set containing no entire part.

For this equality pattern, delta is in {3,4,5} and epsilon_U=10-2delta. The exceptional hitting set T_*=N_H(w_*) intersect U cannot contain all of D, since at least three zero-excess points of D are already saturated by the six size-7 vertices. If T_* contains s points of D, then s<=2 and it must contain at least eight points from A union B union C, because every unselected d in D has eight blocks that must be hit by distinct large-part points. In particular, the only remaining four-partite equality kernel is a single size-10 non-group transversal interacting with the six D-neighbourhood vertices and the three-per-large-group size-8 classes. This is still OPEN, but is substantially narrower than the original shell/core incidence system.


## 13. E408 Q33 four-partite branch: independent exclusion of S0=9 and S0=10

This section supersedes the preliminary “S0=10 residual kernel” statement at the end of Section 12. It gives a shorter proof of the stronger bound S0>=11. The proof does **not** use the selected-pair count in the sibling S0=10 note; that count is not valid as written because a selected pair that is not in a Q block may be an H-edge, not necessarily an extra L-edge.

### 13.1 The degree-seven neighborhood class is a clique

Retain the four-partite E408 Q33 setup of Section 11: L has parts A,B,C of size eight and D of size seven; the 56 witness blocks cover every D–A, D–B, and D–C pair exactly once. Between each pair of large parts, the eight pairs not used by Q blocks form a perfect matching. Since H is the complement of L on U, every H-edge between two large parts belongs to that matching, so each vertex has at most one H-neighbour in each other large part.

Let
\[
W_7=\{w\in W:|N_H(w)\cap U|=7\},\qquad k=|W_7|.
\]
Every w in W_7 has \(N_H(w)\cap U=D\): a 7-set hitting all 56 blocks must consist of points of block-incidence eight, and precisely the seven D points have that incidence.

There is an independent triple \(a\in A,b\in B,c\in C\). Choose any a; at most one vertex of B is H-adjacent to a, so choose b nonadjacent to a. Each of a and b has at most one H-neighbour in C, so choose c nonadjacent to both. If two vertices \(w,w'\in W_7\) were nonadjacent, then \(w,w',a,b,c\) would be an independent five-set: both w and w' are anticomplete to A∪B∪C. This contradicts \(\alpha(H)\le4\). Therefore W_7 is a clique.

The set D is also a clique, and every vertex in W_7 is adjacent to every vertex in D. Hence H contains a clique of size \(7+k\). A counterexample to EG617 cannot contain a monochromatic K13, so \(\omega(H)\le12\) and
\[
\boxed{k\le5}. \tag{13.1}
\]

This uses only the universal counterexample constraint \(\omega(H)\le12\), not the stronger \(\omega(H)\le11\) premise used in some sibling lemmas.

### 13.2 A size-eight or size-nine transversal contains D or a full large part

Let T⊂U hit every witness block and have size eight or nine. If T does not contain all of D, choose d∈D\\T. Its eight witness blocks require eight distinct selected vertices from A∪B∪C, since each selected large-part point occurs in at most one block containing d. Thus T has at most one D point and at least eight large-part points.

Suppose no large part is fully contained in T. For any omitted point a∈A, the seven blocks containing a must be hit by selected vertices outside A. The at-most-one selected D point can hit at most one of these blocks, and each selected point in B∪C can hit at most one, by pair uniqueness. Hence
\[
|T\cap A|\le |T|-7\le2.
\]
The same holds for B and C, so T contains at most six large-part points, contradiction. Therefore
\[
\boxed{\text{every 8- or 9-point transversal contains all of D or a full part A,B,C.}} \tag{13.2}
\]

### 13.3 Capacity of full-large-part neighborhoods

Write \(S_0=\epsilon_U+2\delta\), so
\[
e_H(U,W)=114+S_0.
\]
For a large part G∈{A,B,C}, each of its eight vertices has seven H-neighbours within G and exactly two potential H-neighbours in the other large parts (one along each unused-pair matching). If a vertex v∈G has no incident extra L-edge from J, both potential cross-pairs are H-edges, so \(d_H(v,U)=9\).

At most \(\delta\) vertices of G are incident to J, because every J-edge has at most one endpoint in G. At most \(\epsilon_U\) vertices of G have positive excess. Therefore at least
\[
8-\delta-\epsilon_U=8+\delta-S_0
\]
vertices in G have zero excess and no incident J-edge. For \(S_0=9\), the core budget and \(\epsilon_U\le4\) force \(\delta\in\{3,4\}\), so this lower bound is \(\delta-1\ge2\). For \(S_0=10\), they force \(\delta\in\{3,4,5\}\), so it is \(\delta-2\ge1\).

Each such vertex v has \(d_H(v,U)=9\) and total degree 12, so it has exactly three neighbours in W. Thus for each large part G, at most three vertices of W can have a U-neighbourhood containing all of G. Across A,B,C, there are at most nine W vertices with a full-large-part neighborhood.

For any fixed set of at least three zero-excess vertices in D, each has exactly six W-neighbours: its degree inside U is six, and its total degree is 12. Every W vertex whose U-neighbourhood contains all of D is adjacent to all these vertices. Since k members of W_7 already do so, there can be at most \(6-k\) additional such W vertices. Combined with (13.2), among W vertices with U-degree eight or nine, all but at most \(6-k\) must have a full-large-part neighborhood.

### 13.4 Exclude S0=9

If \(S_0=9\), then \(x=e_H(U,W)=123\). Since every W vertex has U-degree at least seven and all but the k vertices in W_7 have degree at least eight,
\[
123=x\ge7k+8(16-k)=128-k.
\]
By (13.1), k≤5, so equality forces k=5. The other eleven W vertices must all have U-degree exactly eight, since their total U-degree is \(123-35=88=11\cdot8\).

At most \(6-k=1\) of these eleven neighborhoods can contain all of D. By (13.2), at least ten must contain a full large part. But the capacity bound in Section 13.3 allows at most three per large part, hence at most nine in total. Contradiction. Thus S0≠9. The same inequality and k≤5 already exclude S0≤8, so \(S_0\ge10\).

### 13.5 Exclude S0=10

If \(S_0=10\), then x=124. The same inequality gives k≥4; with k≤5, only k=4 or k=5 are possible.

- If k=4, the other twelve vertices have total U-degree \(124-28=96\), so all twelve have U-degree eight.
- If k=5, the other eleven have total U-degree \(124-35=89\), so ten have U-degree eight and one has U-degree nine.

In either case, at least ten vertices have U-degree eight or nine. At most \(6-k\le2\) of these can have a U-neighbourhood containing all of D. By (13.2), at least ten must have a full-large-part neighborhood. The capacity bound allows at most nine, contradiction.

Therefore
\[
\boxed{S_0=\epsilon_U+2\delta\ge11}
\]
throughout the four-partite E408 Q33 minimum-support boundary.

### 13.6 Audit of the sibling pair-count proof

The sibling file R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.md correctly identifies the possible degree pattern \((7^6,8^9,10)\) if S0=10 and k=6, but its final selected-pair inequalities in the s=1 and s=2 cases are not justified. A pair of selected large-part vertices that is not contained in a Q block need not be an extra L-edge: it can instead be an H-edge, because four-partiteness of L does not mean L is complete four-partite. The independent clique-capacity proof above avoids this invalid inference and still excludes S0=10 under the retained core contract.

Scope remains the four-partite, minimum-support E408 Q33 kernel only. The non-four-partite branch, other support sizes, E408 Q32, E407, and the original K145 bridge remain OPEN / NOT_CERTIFIED.


## 14. E407 Q32 49-witness boundary: exclude delta=2

This strengthens the general E407 boundary from \(\delta\ge2\) to
\[
\boxed{\delta\ge3}.
\]
No four-partite assumption is used.

### 14.1 At most two 7-transversals; each supports at most six W vertices

Let \(\mathcal Q\) be the 49-block family on U, with seven color classes of seven disjoint Q-blocks each. A 7-transversal is a 7-set meeting every Q block.

Two distinct 7-transversals cannot overlap: if they overlap in s∈{1,…,6} points, then in each of the seven colors the \(7-s\) blocks indexed by the first transversal's exclusive points pair them with distinct exclusive points of the second; pairwise linearity forbids any such pair from repeating across colors, requiring \(7(7-s)\le(7-s)^2\), impossible.

There cannot be three pairwise-disjoint 7-transversals \(T_1,T_2,T_3\). They would leave R=U\\(T_1∪T_2∪T_3) of size eight. Every Q would contain one point from each T_i and one point from R. Let q_r be the number of colors whose seven-block class omits r. Since each color covers 28 of the 29 U-points, \(\sum_{r\in R}q_r=7\). For each r, in the \(7-q_r\) colors where r is covered, its pairs with each T_i are distinct by linearity, so r has at most q_r H-neighbours in each T_i. Therefore
\[
d_H(r)\le 7+3q_r.
\]
Since \(d_H(r)\ge12\), each q_r≥2, giving \(\sum_R q_r\ge16\), contradiction. Thus there are at most two distinct 7-transversals that occur as W-neighbourhoods.

For a fixed 7-transversal T, let \(W_T=\{w\in W:N_H(w)\cap U=T\}\). The set W_T is a clique: choose any Q containing x∈T; because T hits every block and each color class has seven disjoint blocks, Q meets T exactly once, so Q\\{x} is an independent triple in U\\T. Every vertex in W_T is anticomplete to U\\T. If two W_T vertices were nonadjacent, they plus that triple would form an independent five-set, contradicting \(\alpha(H)\le4\).

Each w∈W_T has \(d_H(w,W)=12+\epsilon_w-7=5+\epsilon_w\). If \(|W_T|\ge7\), the clique W_T forces every w∈W_T to have \(\epsilon_w\ge1\), so the total core excess would be at least seven, contradicting \(\sum_H\epsilon_x=4\). Hence \(|W_T|\le6\), and the total number N_7 of degree-seven W-neighbourhoods satisfies
\[
\boxed{N_7\le12}. \tag{14.1}
\]

### 14.2 The delta=2 equality pattern is impossible

For the E407 boundary,
\[
e_H(U,W)=124+2\delta+\epsilon_U,\qquad
N_7\ge20-2\delta-\epsilon_U.
\]
If \(\delta=2\), (14.1) implies
\[
12\ge N_7\ge16-\epsilon_U.
\]
Since \(\epsilon_U\le4\), this forces \(\epsilon_U=4\), \(N_7=12\), and \(\epsilon_W=0\). There must be exactly two 7-transversals \(T_1,T_2\), each supporting six vertices of W with that U-neighbourhood.

Each \(W_{T_i}\) is a K6. Its vertices have degree five inside W because \(\epsilon_W=0\) and each has exactly seven U-neighbours; hence they have no W-neighbours outside their own K6.

Each T_i must contain at least one J-edge: otherwise T_i is a K7 in H, and together with the K6 \(W_{T_i}\) would give a monochromatic K13. Since \(\delta=2\), there is exactly one J-edge inside each T_i and no J-edge elsewhere.

The 49 Q-blocks use every pair in \(T_1\times T_2\) exactly once, so H has no edges between T_1 and T_2. Put \(R=U\\(T_1∪T_2)\), so |R|=15. Every Q has one point in each T_i and two points in R. For any x∈T_i, the seven Q-blocks containing x use 14 distinct vertices of R, because a repeated x–r pair would violate linearity. Exactly one x–r pair is therefore uncovered by all Q-blocks. Since all J-edges are already inside T_1 and T_2, that uncovered pair is an H-edge. Thus each x∈T_i has exactly one H-neighbour in R.

Now take any x∈T_i not incident to its unique J-edge. It has six H-neighbours inside T_i, one H-neighbour in R, and all six vertices of \(W_{T_i}\) as H-neighbours. Therefore \(d_H(x)\ge13\), so \(\epsilon_x\ge1\). Each T_i has five such non-endpoints, giving at least ten units of core excess, contradicting the total excess four.

Therefore \(\delta\ne2\), and the already-proved \(\delta\ge2\) yields
\[
\boxed{\delta\ge3}
\]
for the full E407 Q32 v=29 / 49-witness boundary, whether L is four-partite or not.

This still does not eliminate the boundary: \(\delta=3,\ldots,16\) remain subject to the joint core-budget constraints.
