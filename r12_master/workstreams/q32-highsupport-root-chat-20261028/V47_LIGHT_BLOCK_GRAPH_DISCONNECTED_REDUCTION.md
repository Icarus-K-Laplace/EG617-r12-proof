# E408 Q32 full support — disconnected light-block graph reduction (m=10)

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural reduction; no full-support closure claimed.**

## 1. Setup

Use the pivot-neighborhood blocks (Q_1,\ldots,Q_{10}), each an independent 4-set in H, and the residual (R), (|R|=7). For each pair of blocks write
[
k_{ij}=e_H(Q_i,Q_j)-4\ge0.
]
The lower bound 4 is the registered pivot-packing lemma. Call (ij) **light** if (k_{ij}=0), and **heavy** if (k_{ij}\ge1). Let (L) be the graph on the ten block labels whose edges are the light pairs.

For each block define
[
t_i=\sum_{j\ne i}k_{ij},\qquad
y_i=\sum_{r\in R}(|N_H(r)\cap Q_i|-1).
]
Then (x=\sum_{i<j}k_{ij}), (y=\sum_i y_i), and
[
\sum_i t_i=2x,\qquad \sum_i y_i=y.
]

Each vertex in (Q_i) has at least one H-neighbor in every other block, and the block has (7+y_i) edges to R. Thus
[
\sum_{q\in Q_i}d_H(q)=36+t_i+7+y_i=43+t_i+y_i.
]
Since every (q\in Q_i) has degree at least12, put
[
s_i=t_i+y_i-5=\sum_{q\in Q_i}(d_H(q)-12)\ge0.
]
The six-unit excess ledger gives
[
\sum_i s_i=2x+y-50\le6,
\qquad
(y+2z-8)+(2x+y-50)=6.
]
In particular (s_Q:=\sum_i s_i=14-y-2z\le6), while (s_R=y+2z-8\ge0).

## 2. Component lower bound

Let S be a connected component of L with (k\le5) vertices. Every pair between S and its complement T is heavy, so each (i\in S) has at least (10-k) units in (t_i). Hence
[
s_i=t_i+y_i-5\ge5-k+y_i,
]
and
[
\boxed{s_Q\ge k(5-k)+Y_S},\qquad Y_S=\sum_{i\in S}y_i.
	ag{2.1}
]

If L had at least three connected components, at least two components would have size at most4. Their lower bounds in (2.1) sum to at least (4+4=8), contradicting (s_Q\le6). Therefore **L has exactly two components**. Their sizes must be one of
[
\boxed{1+9,\quad2+8,\quad3+7,\quad4+6,\quad5+5.}
]

The following refinements are all necessary conditions.

## 3. Component sizes 1+9

For the singleton component S, its sole block has nine heavy partners, so (t_i\ge9) and
[
s_i=t_i+y_i-5\ge4.
]
Therefore (s_Q\ge4), (s_R\le2), and
[
y+2z\le10,qquad z\le5.
]
Moreover (s_i\le6) implies
[
(t_i-9)+y_i\le2.
]
So among the nine cross pairs, the total heavy-edge multiplicity beyond the mandatory one extra edge per pair is at most two; the singleton block has (y_i\le2).

## 4. Component sizes 2+8

Here (2.1) forces (s_Q=6) and (s_R=0). The two-vertex component is a light edge. Both of its blocks have (y_i=0), (s_i=3), and (t_i=8). Thus each of their eight cross pairs is heavy with **exactly one** extra edge, i.e. exactly five H-edges.

Every block in the eight-vertex component has (s_j=0), so its internal heavy-pair weight (t_j^{T}) satisfies
[
t_j^{T}+y_j=3.
]
Let (x_T) be the total (k_{ij})-weight over heavy pairs wholly inside T. Counting the 16 cross pairs and using (x+y+z=32) gives
[
x=16+x_T,qquad 2x_T+y=24,
]
hence
[
\boxed{x_T=8+z,\quad y=8-2z,\quad z\le4.}
]
Each block in T has weighted internal heavy degree at most3, so its degree in (L[T]) is at least4.

## 5. Component sizes 3+7

Now (s_Q=6), (s_R=0). The three-vertex component must be a **light triangle**: a path would create at least one internal heavy pair and exceed the entire six-unit budget. Its three blocks have (y_i=0), (s_i=2), and each cross pair to T is heavy with exactly one extra edge.

Each block (j\in T) satisfies
[
t_j^{T}+y_j=2.
]
Counting the 21 cross pairs gives
[
x=21+x_T,qquad 2x_T+y=14,
]
so
[
\boxed{x_T=3+z,\quad y=8-2z,\quad z\le4.}
]
Every block in T has weighted internal heavy degree at most2, and therefore degree at least4 in (L[T]).

In both the 2+8 and 3+7 cases,
[
s_R=0\implies d_{H[R]}(r)+b_r=2
]
for every (r\in R), where (b_r=\sum_i(|N_H(r)\cap Q_i|-1)). Hence (Delta(H[R])\le2), and (H[R]) is a disjoint union of paths, cycles and isolated vertices.

## 6. Component sizes 4+6

Equation (2.1) gives (s_Q\ge4), hence (s_R\le2) and
[
\boxed{y+2z\le10,\quad z\le5.}
]
Let (x_S) be the sum of (k_{ij}) over heavy pairs internal to S, and let (delta_{ST}=\sum_{i\in S,j\in T}(k_{ij}-1)) be the extra multiplicity beyond one on cross pairs. The 24 cross pairs are all heavy, and
[
s_S=4+2x_S+\delta_{ST}+Y_S\le6.
]
Therefore
[
\boxed{2x_S+\delta_{ST}+Y_S\le2.}
]
In particular, S has at most one unit of internal heavy-pair weight; its light graph is either (K_4) or (K_4) minus one edge. Across the 24 cross pairs, at most two extra multiplicity units are allowed beyond the mandatory one per pair.

## 7. Component sizes 5+5

There are 25 heavy cross pairs, so (x\ge25). Combining with (x+y+z=32) and (y+2z\ge8) gives
[
\boxed{y+z\le7,\quad z\ge1.}
]
Let (delta_{ST}) denote cross-pair multiplicity beyond one, and (x_S,x_T) the weighted heavy-pair sums internal to the two components. Then
[
x=25+\delta_{ST}+x_S+x_T,
]
and the six-unit budget yields
[
\boxed{2(\delta_{ST}+x_S+x_T)+y\le6.}
]
Thus there are at most three total heavy-edge multiplicity units beyond the 25 mandatory cross-pair units, and (y\le6).

## 8. Next mathematical target

The most rigid disconnected cases are 2+8 and 3+7: they spend the entire Q-excess budget, force (s_R=0), force all cross pairs to have exactly five edges, and reduce (H[R]) to a seven-vertex maximum-degree-two graph. The next step is to couple those path/cycle residual types to the unique-matching and independent-set-cover constraints across the pivot blocks.

This reduction does not close any full-support Q32 branch. The scalar slack relaxation remains feasible and is not treated as an UNSAT certificate.


## 9. New zero-slack map alignment and outer-vertex transversal cap

The detailed theorem is in `V47_ZERO_SLACK_MAP_ALIGNMENT_AND_TRANSVERSAL_BLOCKER.md`.

In the 2+8 cell, the two small blocks' residual-neighbor maps coincide after aligning their light matching. In the 3+7 cell, the three small-block maps coincide. This follows from the unordered-pair label identity forced by alpha(H)<=4 and the fact that every residual vertex has two nonneighbors that are themselves nonadjacent under Delta(H[R])<=2.

For 3+7, each outer vertex q has a nonempty common track among its neighbor labels in A,B,C. A singleton common track h forces q to be adjacent to the entire residual fiber F_h and caps its small-component extra-edge count at `3-|F_h|`. A two-track intersection means q owns all three extra edges to the small component and has no residual neighbor or other extra Q-Q incidence. Every outer block's three extra edges obey `sum_q k(q)=3`.

The normalized exact verifier checked 1,728 aligned plus 36 switch configurations and returned `V47_ZERO_SLACK_TRANSVERSAL_LOCAL_OK`. This is a new local incidence restriction, not a closure of the 2+8 or 3+7 graph cell.


## 10. Two-light matching composition in the 2+8 / 3+7 outer component

New local theorem: `V47_TWO_LIGHT_MATCHING_COMPOSITION.md`.

If A-C and B-C are light pairs (each exactly a perfect matching) and e_H(A,B)<=7, then the composed matching between A and B must be present in H[A,B]. Otherwise a missing composed edge forces its row to contain all three off-diagonal edges; the edge cap and alpha(H)<=4 then force a second independent 5-set. The proof is analytic and uses no external extremal theorem.

The exhaustive local verifier checked all 25,636 A-B bipartite graphs with 4..7 edges. The only graphs with alpha(A union B union C)<=4 are precisely those containing all four composed matching edges; counts by edge total are 1,12,66,220 for 4,5,6,7 edges. It returned `V47_TWO_LIGHT_MATCHING_COMPOSITION_EXHAUSTIVE_OK`.

In the 2+8 and 3+7 cells, every outer-block pair has at most seven H-edges because its internal heavy weight is at most three. The outer light graph on eight vertices has minimum degree at least four. Every nonadjacent block pair therefore has at least two common light neighbors, and each length-two light path forces its composed matching into the endpoint pair graph.

- A 5-edge endpoint pair has a unique perfect matching, so all common-neighbor paths must induce the same matching.
- A 6- or 7-edge pair has at most two perfect matchings, since two distinct nonidentity matchings beyond a fixed matching require at least four off-matching edges but only three are available.
- Thus any path-matching disagreement is charged to a pair with at least six edges; there are at most six such pairs because each consumes at least two units of the total outer heavy weight x_T<=12.

This is a matching-holonomy constraint to combine with the zero-slack residual-neighbor maps and the 18 residual path/cycle types. It does not close the 2+8 or 3+7 cell and is not a global UNSAT certificate.


## 11. Four-light-cycle holonomy refinement

New theorem: `V47_LIGHT_CYCLE_HOLONOMY.md`; exact verifier: `verify_v47_light_cycle_holonomy.py`.

For any four outer blocks whose four cycle pairs are light, the two diagonal pairs contain both path-composed perfect matchings by the two-light composition theorem. Since each diagonal has at most seven edges, the cycle holonomy cannot be a 4-cycle or double transposition (their matching union has eight edges). A 3-cycle forces both diagonals to have exactly seven edges, but the normalized 16-vertex graph then contains an explicit independent 5-set. Therefore every such cycle has identity or transposition holonomy only.

If holonomy is a transposition, both diagonals have at least six edges. The verifier checked all 726 normalized transposition/diagonal-extra configurations and all eight forced 3-cycle configurations; it returned `V47_LIGHT_CYCLE_HOLONOMY_EXHAUSTIVE_OK`.

In the 3+7 cell, a pair with six edges uses its full internal-heavy allowance of two at both endpoints, so those endpoints have no other internal-heavy pair. Hence any nontrivial light-cycle holonomy is supported on two disjoint high-weight diagonal pairs. This refines the previous “at most six pairs with six/seven edges” statement, but does not close the disconnected cell.


## 12. Global light-holonomy rigidity in the 3+7 cell

Added `V47_37_OUTER_LIGHT_HOLONOMY.md` and `verify_v47_37_light_graph_cycles.py`.

In the 3+7 cell, every outer block has weighted internal-heavy degree at most two, so the outer light graph has minimum degree four on seven vertices and each outer pair has at most six H-edges. Triangle consistency is immediate from the two-light matching theorem. A four-light-cycle can have only identity/transposition holonomy; a transposition would force both diagonals to have weight two, saturating the four cycle vertices' heavy budgets. Any outside block is then light to all four, and the four light triangles through it force identity, a contradiction.

For a five-cycle, either a light chord splits it into a triangle and four-cycle, or its five heavy chords saturate every cycle vertex and an outside block is a common light hub. Cycles of length six or seven must have a light chord because a chordless cycle would give a vertex at least three heavy neighbors. Induction shows every cycle of the outer light graph has identity holonomy.

The light graph is connected, so all light matchings globally align after relabeling. Any heavy pair has at least three common light neighbors; matching composition therefore forces the aligned matching into every heavy pair as well. Hence the 28 outer vertices contain four aligned K7 tracks, with at most `x_T=3+z<=7` additional cross-track edges.

The exact weighted-graph regression enumerated 22,054 heavy graphs with weighted degree at most two and total weight at most seven, checking 5,803,387 light cycles. It returned `V47_37_LIGHT_GRAPH_CYCLE_DECOMPOSITION_OK`. This tightens the 3+7 normal form but does not close that cell.


## 13. Residual-track domination in the 3+7 cell

The new theorem `V47_37_RESIDUAL_TRACK_TRANSVERSAL.md` strengthens the globally aligned K7 normal form. Every residual vertex r must be adjacent to all seven vertices of one outer track; otherwise its nonneighbor sets in all four tracks have sizes summing to at least19, and the exact four-part union bound produces an independent transversal, contradicting `alpha(H)<=4`.

The assigned track is unique, and two residual vertices assigned to the same track must be adjacent: the other three tracks each retain at least three vertices nonadjacent to both, and the three-part union bound again produces an independent transversal. Hence the track assignment partitions R into four clique fibers, with sorted sizes one of `(3,3,1,0)`, `(3,2,2,0)`, `(3,2,1,1)`, `(2,2,2,1)`.

The exact integer verifier checks all 64 four-part profiles and 35 three-part profiles, with worst four-part margin63, and returns `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`. This matches the four possible fiber-size profiles of the small-block residual map but does not yet prove that the two partitions align. The 3+7 cell remains OPEN.


## 12. RETRACTED: global matching maps from the small triangle to outer blocks

The former claim that the 4,5,5 switch theorem and cut-endpoint bound force each small-to-outer matching permutation to be constant is **RETRACTED**. The switch theorem's two extra edges hit two distinct moved small-side labels, so the old single-label cut charge is invalid. See `V47_37_SMALL_OUTER_MATCHING_RIGIDITY_RETRACTION.md`.

The local switch theorem, outer-light holonomy theorem, residual-track transversal theorem, and separate z=0,1 partition-alignment argument remain distinct proof assets. This branch remains OPEN / NOT_CERTIFIED.
