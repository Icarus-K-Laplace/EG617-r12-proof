# Clean Pair Nonextension — Current Theorem and Obstruction Ledger

Status: **OPEN**. The work below is a genuine structural reduction, not a proof that every sufficiently large clean pair terminal is impossible.

## 1. Contract

Assume A+B and r >= 12. Work inside one legal core H with

|H| = 3r-1, alpha(H) <= 3, omega(H) <= r-1, delta(H) >= r,

and inherited excess cap K = sum_v (d_H(v)-r) <= 2r-2. Globally alpha(F) <= 4, not 3.

Let U be m disjoint clean blocks P_i={x_i^0,x_i^1} from the a=2, zeta=0 d2 plateau. Every P_i is a target K2; every inter-block target graph is a matching. For every x in U, w_x=1 and therefore kappa_x in {0,1}, so d_H(x) <= r+1.

## 2. Complement formulation

Let G = complement of H[U]. Since alpha(H) <= 3, G is K4-free.

Each block P_i is an independent pair in G. Since H[P_i,P_j] is a matching with at most two edges, G[P_i,P_j] has at least two edges. In particular, every x in P_i has at least one G-neighbor in every other block, giving

d_G(x) >= m-1.

There is a second, degree-based bound. The graph H[U] has 2m vertices, and d_H[U](x) <= d_H(x) <= r+1. Hence

d_G(x) = 2m-1-d_H[U](x) >= 2m-r-2.

Therefore

delta(G) >= max(m-1, 2m-r-2).                                    (2.1)

## 3. High-density conditional reduction via Andrasfai-Erdos-Sos

The Andrasfai-Erdos-Sos theorem states that a K4-free n-vertex graph with minimum degree greater than 5n/8 is 3-partite; this is the r=3 case of the classical threshold (3r-4)n/(3r-1). See Andrasfai, Erdos and Sos, *On the connection between chromatic number, maximal clique and minimal degree of a graph*, Discrete Mathematics 8 (1974), DOI 10.1016/0012-365X(74)90133-2.

If

m >= ceil(4r/3 + 3),

then

2m-r-2 > 5m/4 = 5(2m)/8.

By (2.1), G is 3-partite. Thus U can be partitioned into three sets A,B,C, each independent in G and therefore a clique in H. The clique cap gives

|A|, |B|, |C| <= r-1,

so

2m <= 3(r-1), or m <= floor(3(r-1)/2).                         (3.1)

Also, at most one entire block can lie inside any one part: if two blocks both lay wholly in the same independent part of G, then G would have zero cross edges between those blocks, contradicting |G[P_i,P_j]| >= 2. Hence all but at most three blocks meet two distinct parts.

This is a nontrivial high-density structure theorem, but it is not a contradiction. The interval

ceil(4r/3+3) <= m <= floor(3(r-1)/2)

is nonempty for sufficiently large r. The theorem leaves open systems in that interval and says nothing decisive for m < 4r/3+3.

## 4. Static obstruction to a stronger claim

The three-clique-plus-block-matching family in CLEAN_PAIR_GRAPH_MODEL.md shows that a large clean block system can satisfy:

- pairwise matching cross graphs;
- alpha(H[U]) <= 3;
- omega(H[U]) linear in m and below r-1 for a broad range m <= 3(r-1)/2.

This is a local model only, not a full legal-core counterexample. It disproves the proposed shortcut that the block matching and independent-transversal constraints alone force m=O(1).

## 5. What the global closure still has to do

The remaining route must exploit the fact that the blocks sit in a core of size 3r-1, while each clean endpoint has degree exactly r or r+1 and the total excess is at most 2r-2. The old shell pair S also has a fixed incidence total:

sum_{s in S} e_F(s,H) = 2r+b, with b in {0,1}.

A complete proof must count the edges from U to O=H\U and the excess of O without double-counting. The elementary inequalities currently available do not force a contradiction: their leading quadratic terms meet at the Turan scale, and the static construction above shows why a naive density argument is insufficient.

## 6. Precise status

- Exact block graph and complement model: **PROVED_SYMBOLIC**.
- Four-block 2-SAT constraint and minimum of six cross edges: **PROVED by exhaustive finite enumeration**.
- High-density 3-partite reduction for m >= ceil(4r/3+3): **PROVED_CONDITIONAL**, using the legal-core contract and the cited AES theorem.
- Absolute bound on m: **OPEN**.
- Clean Pair Nonextension: **OPEN**.
- New all-large-r contradiction: **NONE**.
