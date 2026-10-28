# E408 Q32 full support — two-light matching composition theorem

Date: 2026-10-28  
Status: **PROVED; exact local theorem plus exhaustive arithmetic regression.** No global Q32 closure claimed.

## 1. Theorem

Let A, B, C be pairwise disjoint independent 4-sets in a graph G with alpha(G[A union B union C]) <= 4. Assume

- e_G(A,C)=4;
- e_G(B,C)=4;
- e_G(A,B)<=7.

The two four-edge bipartite graphs are perfect matchings. Label the vertices so their edges are A_i C_i and B_i C_i for i in {0,1,2,3}. Then

> **The composed matching {A_i B_i : i=0,1,2,3} is contained in E_G(A,B).**

Equivalently, when two pivot-block pairs are light (exactly four H-edges) and the third pair has at most seven H-edges, the two light matching maps compose to a perfect matching that must be present in the third pair.

## 2. Proof

Suppose for contradiction that A_i B_i is absent for some label i.

### Step 1: all three off-diagonal edges in row i are present

For any j != i, suppose A_i B_j is also absent. Let {k,l} be the two labels other than i,j. Then

{A_i, B_i, B_j, C_k, C_l}

is an independent 5-set:
- the two A-B edges from A_i to B_i,B_j are absent by assumption;
- A_i has only its A-C matching neighbor C_i, not C_k,C_l;
- B_i,B_j have only their B-C matching neighbors C_i,C_j, not C_k,C_l;
- each block A,B,C is independent.

This contradicts alpha<=4. Hence A_i is adjacent to every B_j with j != i: its row has three off-diagonal edges.

### Step 2: every other diagonal edge is present

If some A_k B_k with k != i were absent, Step 1 applied to row k would force that row to contain all three off-diagonal edges. The two rows i,k would then contribute six edges. Each of the two remaining A-vertices must have at least one A-B neighbor; otherwise an isolated A-vertex together with all four vertices of B is an independent 5-set. Thus e(A,B)>=8, contradicting e(A,B)<=7.

Therefore A_k B_k is present for all k != i.

### Step 3: find a second missing edge in column i

If every A_k B_i for k != i were present, then the graph A-B would contain:
- the three off-diagonal edges in row i from Step 1;
- the three diagonal edges A_k B_k for k != i from Step 2;
- the three off-diagonal edges A_k B_i for k != i.

These are nine distinct edges, contradicting e(A,B)<=7. Hence there is some k != i with A_k B_i absent.

Let {j,l} be the two labels outside {i,k}. The set

{A_i, A_k, B_i, C_j, C_l}

is independent: A_iB_i and A_kB_i are absent; C_j,C_l avoid the only A-C neighbors C_i,C_k; and they avoid B_i's only B-C neighbor C_i. This is again an independent 5-set, contradiction.

Thus every composed edge A_iB_i must be present. QED.

## 3. Exact finite regression

The companion script verify_two_light_matching_composition.py enumerates every bipartite graph A-B with 4,5,6, or 7 edges (25,636 masks total), while fixing A-C and B-C to the two matching graphs. It checks every 5-subset of the 12 vertices for independence.

The exact counts with alpha<=4 are:
- 4 edges: 1 graph;
- 5 edges: 12 graphs;
- 6 edges: 66 graphs;
- 7 edges: 220 graphs.

In every such graph, all four composed matching edges are present. The counts equal binom(12,e-4): after the four required matching edges, any e-4 of the twelve nonmatching edges may be added.

This is a local finite verifier, not a solver for the 47-vertex Q32 graph.

## 4. Consequence for the m=10 disconnected 2+8 / 3+7 cells

In either cell, every outer block T_i has weighted internal-heavy degree at most three:
- 2+8: t_i^T+y_i=3;
- 3+7: t_i^T+y_i=2.

Therefore every pair of outer blocks has e_H(T_i,T_j)=4+k_ij<=7. The outer light graph L[T] has minimum degree at least four on eight vertices.

For any two nonadjacent vertices i,j of L[T], their neighborhoods are subsets of the other six vertices and each has size at least four, so they have at least two common light neighbors. For each common light neighbor k, the theorem forces the composition of the two light matching maps along i-k-j to be a perfect matching contained in H[T_i,T_j].

Consequences:
1. If e_H(T_i,T_j)=5, its unique perfect matching must equal the composed matching along every common light neighbor. Thus all length-two light paths between that pair must induce the same matching.
2. If e_H(T_i,T_j)=6 or 7, every path-composed matching must be contained in that pair graph. Such a graph has at most two perfect matchings: after fixing one matching, there are at most three extra edges, while two distinct nonidentity matchings relative to it require at least four distinct off-matching edges. Thus the common-neighbor path compositions take at most two values.
3. Every nontrivial path-matching disagreement is therefore charged to a pair with at least six H-edges. Since sum_{i<j in T} k_ij=x_T<=12, there are at most six such pairs.

This gives a concrete matching-holonomy ledger for the next finite reduction. It does not yet eliminate either disconnected cell or close Q32.

## 5. Scope firewall

The theorem uses only alpha(G)<=4, the two exact four-edge matchings, and the seven-edge upper bound on the third pair. It uses no Kang–Pikhurko result, no Type-I special-point premise, no degree-nine claim, and no exceptional-vertex injectivity.

EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
