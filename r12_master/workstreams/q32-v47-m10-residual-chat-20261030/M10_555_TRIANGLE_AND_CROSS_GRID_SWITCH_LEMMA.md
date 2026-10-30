# M10 5,5,5 triangle classification and 4+6 cross-grid switch constraints

Date: 2026-10-30  
Status: COMPUTATION_CERTIFIED local theorem; global 4-by-6 grid remains OPEN.

## 1. Exact 5,5,5 triangle theorem

Let A,B,D be pairwise disjoint independent 4-sets with exactly five edges between each pair. Each pair graph has a perfect matching and one extra edge. Relabel A,B,D so the A-B and A-D perfect matchings are identity; write sigma in S_4 for the B-D perfect matching. Let e_AB,e_AD,e_BD be the three extra edges, each off its pair's base matching.

**Theorem.** The induced 12-vertex graph has alpha at most four exactly in these cases:

1. sigma=id: all 12^3=1,728 choices of (e_AB,e_AD,e_BD) are valid.
2. sigma=tau is a transposition: for some s in the two-point support of tau,
   
       e_AB=(s,tau(s)),
       e_AD=(tau(s),s),

   while e_BD is arbitrary among its 12 off-matching edges. This gives 24 valid configurations for each of the six transpositions, 144 total.
3. For every other sigma (3-cycles, double transpositions, and 4-cycles), no extra-edge choice is valid.

The exact normalized input space has 24*12^3=41,472 configurations. The verifier checks every one of the 792 five-subsets of the 12-vertex graph and confirms exactly 1,872 valid configurations: 1,728 identity and 144 transposition. This is an exhaustive finite classification, not a heuristic search.

## 2. Application to the 4+6 K4-e cell

In the 4+6 component split, suppose the four-block side S is K4-e. Its unique heavy pair A,B has exactly five edges; the other five pairs in S have exactly four. The six-block side T has light graph K6 minus a matching of size Z-1; its heavy pairs are exactly that matching and each has exactly five edges. The component ledger gives zero extra multiplicity on all 24 S-T pairs, so each cross pair has exactly five edges.

The internal perfect matchings on S and T align independently:
- In S, the two light 2-paths between the endpoints of the unique heavy pair force the same matching into its 5-edge pair. A 5-edge bipartite graph on 4+4 vertices cannot contain two distinct perfect matchings, because the symmetric difference of two distinct perfect matchings has at least six edges.
- In T, every pair graph (light or heavy) has a unique perfect matching: four edges for a light pair, five for a heavy pair. Every cycle in K6 minus a matching has a light chord, except a 4-cycle whose two diagonals are both missing matching pairs. In the latter case the two length-two paths force the same unique matching into each heavy diagonal. Chord induction makes every cycle holonomy trivial, so all six blocks can be relabelled with the same identity matching. Each missing pair also receives that identity matching from a common light neighbor.

Thus all internal S and T base matchings may be taken to be identity. The only remaining matching freedom is the 4-by-6 cross matrix.

For each outer block D_j, the triple A,B,D_j is a 5,5,5 triangle. Hence the A-D_j and B-D_j matchings are either equal or differ by a transposition. If they differ, the fixed extra edge e_AB determines the transposition and forces the A-D_j extra edge by the theorem above. In particular, every nontrivial A/B switch across the six columns uses the same transposition and the same orientation, because e_AB is one fixed edge.

## 3. Exact switch equations on the 4-by-6 grid

Write p_ij:[4]->[4] for the base perfect matching from row block Q_i to column block D_j, and write the unique extra edge as e_ij=(a_ij,b_ij), with a_ij a row-label and b_ij a column-label.

There are two orientations of the 4,5,5 switch theorem; they must not be conflated.

### Row direction: two small blocks, one outer block

If Q_i Q_k is a light pair and the two cross pairs Q_i D_j,Q_k D_j each have five edges, put tau=p_ij^{-1} p_kj. Either tau=id, or tau is a transposition and for some s in its support

    e_ij=(s,p_kj(s)),
    e_kj=(s,p_ij(s)).

Thus the two extra edges have the same endpoint label s on their respective small blocks.

### Column direction: one small block, two outer blocks

If D_j D_l is a light pair and Q_i D_j,Q_i D_l each have five edges, put sigma=p_ij p_il^{-1}, a permutation from D_l labels to D_j labels. Either sigma=id, or sigma is a transposition and for some s in its support

    e_ij=(p_ij^{-1}(sigma(s)),s),
    e_il=(p_ij^{-1}(s),s).

Here the two extra edges have the same endpoint label s on the two outer blocks. This is the transpose-oriented form of the same 4,5,5 theorem.

At a grid cell, all row-direction switch transpositions incident to that cell must contain its source endpoint label a_ij; all column-direction switch transpositions incident to it must contain its target endpoint label b_ij. These are separate source-side and target-side star constraints. A global single-label propagation across mixed-orientation switch components is not asserted.

## 4. One-column finite state count

Normalize e_AB=(A_0,B_1) and use the global target-label gauge p_C=id for one column. Enumerating all p_A,p_B,p_D and all off-matching extra edges subject to:
- the 5,5,5 A-B-D theorem;
- the five 4,5,5 constraints from the light pairs in S;

gives exactly 20,788 one-column local states. Of these, 20,772 have p_A=p_B and 16 have p_A!=p_B. The 16 switch states are all forced by the fixed A-B extra edge and the adjacent 4,5,5 constraints. The companion verifier also checks all 8,704 possible independent-five candidates in the five-block union (one per block, or 2+1+1+1 across four blocks); it finds none. The omitted distributions on at most three blocks are already excluded by the pair and triangle theorems. Thus every one-column state has alpha at most four on A union B union C union D union {D_j}.

This is a per-column count only. It does not impose the row-wise column-direction constraints between distinct D_j, the residual degree equations, the residual fiber maps, or the Type-I source placements.

## 5. Remaining 4+6 load-bearing interface

The K4-e 4+6 branch is now reduced to:
- one fixed heavy-pair extra edge e_AB;
- six column states from the 20,788-state local catalog;
- all column-pair compatibility constraints on the K6-minus-matching light graph;
- the exact per-vertex degree equations in each Q_i and D_j;
- the residual unique-neighbor maps and their clique fibers.

The 4-by-6 grid has not been exhausted. No contradiction or Q32 closure is claimed.
