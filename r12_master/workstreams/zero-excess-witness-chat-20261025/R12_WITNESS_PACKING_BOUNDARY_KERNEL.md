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

## 6. Further closure of one E407 boundary corner

Consider the extreme E407 pair g=16, epsilon_*=0. Then e(L)=310. The retained second-Turán theorem forces L to be four-partite. Since 49 Q blocks are edge-disjoint K4s, every pair of parts must have product at least 49. The only possible part sizes are (7,7,7,8).

The 49 Q blocks then form a transversal design TD(4,7) on 28 active vertices: all pairs between the four seven-point groups occur exactly once. The extra point z in the eight-point part occurs in no selected Q block. The five missing edges of L (equivalently, the five H-edges crossing parts) must all be incident to z, because every pair between active groups already belongs to a Q block. Hence
\[
H[V_*]=K_7\dot\cup K_7\dot\cup K_7\dot\cup K_8
\]
plus five extra edges, all incident to z. The point z has degree 12 already inside V_*, so it has no neighbour in W.

Also e(H[W])=32, so equality holds in the Turán complement bound and
\[
H[W]=K_5\dot\cup K_5\dot\cup K_4\dot\cup K_4.
\]
For a zero-excess vertex w in a K5 component, |N_H(w) intersect V_*|=8; for one in a K4 component, that size is 9. Every such neighbourhood hits all TD(4,7) blocks. A hitting set of size 8 or 9 must contain exactly one whole seven-point group: if it contained no whole group, then for each group i the selected points in the other three groups would have to number at least seven, forcing every group intersection to have size at most one (for size 8) or at most two (for size 9), impossible by total size.

If every one of the four W-clique components contains a zero-excess vertex, choose one from each. Their full-group labels must be four distinct groups: otherwise one group is unlabelled, and the four chosen vertices have only 1+1+2+2=6 extra neighbours in total, leaving a point of that seven-point group nonadjacent to all four; this creates an independent five-set. Thus under this additional condition, all zero-excess vertices within each W component have a fixed group label, and the four components are labelled by a permutation of the four groups.

This extreme corner is not yet contradictory. In particular, the case where all four excess units are concentrated on one K4 component requires separate handling before the group-label conclusion can be applied to all four components. The TD(4,7) corner is a finite incidence kernel to attack, not a claimed closure.

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


## 9. General four-partite E407 boundary: eliminate delta=12,13

The E407 boundary audit must retain both possibilities: L may be four-partite or non-four-partite. The following analysis treats the four-partite branch directly rather than inferring non-four-partiteness by excluding only the complete Turan graph.

Assume L is four-partite. The 49 edge-disjoint Q blocks force part sizes (7,7,7,8). The blocks cover every pair between any two of the three seven-point parts, and every pair between a seven-point part and the seven used points of the eight-point part. Exactly one point z in the eight-point part is unused by all Q blocks. All 294 witness edges lie between the active 28 points; the only possible additional L edges are z-to-active-point edges. Therefore
\[
\delta=e(L)-294=d_L(z,U\setminus\{z\}).
\]
The complement H[U] consists of four cliques of sizes 7,7,7,8, plus 21-delta H-edges from z to the active 28 points. In particular,
\[
d_{H[U]}(z)=7+(21-\delta)=28-\delta.
\]
Since every core degree is at most 16, delta>=12.

Combining this with the already proved boundary budget delta+epsilon_U<=16 gives
\[
\epsilon_U\le16-\delta.
\]
But z itself has excess at least
\[
\epsilon_z\ge d_{H[U]}(z)-12=16-\delta.
\]
Hence equality holds throughout:
\[
\boxed{\epsilon_U=\epsilon_z=16-\delta}.
\]
All excess inside U is concentrated at z, z has no neighbour in W, the remaining excess is
\[
\epsilon_W=\delta-12,
\]
and
\[
e(H[W])=32,\qquad H[W]=K_5\dot\cup K_5\dot\cup K_4\dot\cup K_4.
\]
Thus the four-partite branch has delta in {12,13,14,15,16}.

For a zero-excess w in W, its neighbourhood T_w=N_H(w) intersect U has size 8 if w lies in a K5 component of H[W], and size 9 if it lies in a K4 component. It hits all 49 Q blocks. As shown in Section 6, every hitting set of size 8 or 9 contains a unique whole seven-point TD group plus respectively one or two extra points.

If delta=12 or 13, then epsilon_W is 0 or 1, so every W clique component contains a zero-excess vertex. The group-label argument in Section 6 applies. For delta=12, both K5 components are entirely zero-excess; for delta=13, at least one K5 component is entirely zero-excess. In either case its five vertices all have the same seven-point group label, so together with that group they form a K12, contradicting omega(H)<=11. Therefore
\[
\boxed{\text{if L is four-partite, then delta}\ge14.}
\]

At delta=14, epsilon_W=2, and each K5 component must contain one positive-excess vertex; those two units are forced one into each K5 component. Since each such vertex has a nine-point hitting set, its full group must differ from the group label of the four zero-excess vertices in that K5 component, or a K12 appears. At delta=15, epsilon_W=3 and each K5 still requires at least one positive-excess vertex. At delta=16, epsilon_W=4; the only case in which the four-component group-label argument is unavailable is when all four positive-excess vertices occupy one K4 component. That exceptional branch remains OPEN.

This is a strict reduction of the E407 four-partite boundary, not its closure. The non-four-partite branch remains separately OPEN and must not be inferred from ruling out the complete four-partite graph.

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
