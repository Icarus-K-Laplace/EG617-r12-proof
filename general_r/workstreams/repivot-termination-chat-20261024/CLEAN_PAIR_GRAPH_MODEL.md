# Clean Pair Graph Model

Status: C-N1 **partially achieved**. The block system is now an exact finite combinatorial object. No nonextension contradiction is claimed.

## 1. Frozen hypotheses and notation

Assume A+B, r >= 12, and the canonical backend contract. In particular alpha(H) <= 3, omega(H) <= r-1, delta(H) >= r, K <= 2r-2, and alpha(F) <= 4. Never replace the last inequality by alpha(F) <= 3.

Let U be the union of m pairwise-disjoint clean blocks P_i = {x_i^0,x_i^1} in one fully decorated d2 plateau with allowance a=2 and zeta=0. Each P_i is a target edge. Its endpoint weights relative to the distinguished shell pair S are both 1. Thus for x in U,

w_x = kappa_x + e_F(x,S) = 1,

so e_F(x,S) is either 0 or 1 and kappa_x = 1-e_F(x,S) is either 0 or 1. Consequently d_H(x)=r+kappa_x <= r+1.

For every pair of distinct blocks P_i,P_j, the target cross graph H[P_i,P_j] is a matching. It has size 0, 1, or 2. The size-2 case is one of the two perfect matchings.

## 2. Exact interaction matrix

For i<j define M_ij as the subset of {(0,0),(0,1),(1,0),(1,1)} for which x_i^a x_j^b is a target edge. The matching condition says M_ij is a partial matching of K_2,2. There are exactly seven possible types:

- the empty set;
- one of the four singleton edge sets;
- one of the two perfect matchings.

This is the complete pairwise interaction alphabet. It records endpoint labels, not merely the edge count, so it retains the information needed for repivot transitions and clique tests.

For any selected endpoint vector a=(a_1,...,a_m) in {0,1}^m, the selected vertices form an independent set precisely when

(a_i,a_j) is not in M_ij for every i<j.

Thus the no-independent-4-transversal condition is the exact statement that no four-index restriction of these binary constraints has a satisfying assignment.

## 3. Exact 2-SAT encoding

Introduce one Boolean variable X_i for each block, with X_i=a meaning that endpoint x_i^a is selected. Every target edge x_i^a x_j^b contributes the clause

(X_i != a) OR (X_j != b).

The conjunction of these clauses is satisfiable exactly when the chosen blocks admit an independent transversal. Therefore alpha(H) <= 3 implies that for every four distinct block indices, the corresponding 2-CNF is unsatisfiable.

Equivalently, on each four-block restriction, the standard implication digraph has some variable and its negation in the same strongly connected component. This gives a finite, machine-checkable test for each four-block interaction pattern.

## 4. Four-block local audit

There are seven possible matching types on each of the six block pairs in a four-block set, hence exactly 7^6 = 117,649 labeled interaction patterns. Each pattern has 16 endpoint selections to test.

An exhaustive exact enumeration was run over all 117,649 patterns. Among patterns whose 2-CNF is unsatisfiable:

- the minimum total number of target cross edges is 6;
- exactly 160 labeled patterns attain that minimum;
- no unsatisfiable pattern with 0 through 5 cross edges exists.

Therefore every four clean blocks satisfy the local inequality

sum_{i<j, i,j in I} |M_ij| >= 6, for every four-set I.

Double-counting four-sets gives the global but relatively weak consequence

sum_{i<j} |M_ij| >= binom(m,2).

This local bound is not stronger than the asymptotic edge lower bound obtained from alpha(H[U]) <= 3 via Turan's theorem. Its value is the exact 2-SAT certificate and the finite pattern restriction, not a claimed contradiction.

### Reproduction protocol

Enumerate the seven matching types above independently for each of the six pairs. For each of the 16 binary assignments, mark it independent iff it selects no edge in any M_ij. Reject a pattern if at least one assignment survives. Record the minimum sum of |M_ij| over rejected patterns and count the patterns attaining that minimum. The search space is finite and exhaustive; this audit does not replace an all-r proof.

## 5. Saturated-interaction signed model

If every block pair has exactly two target cross edges, encode its perfect matching by b_ij in {0,1}, where x_i^a x_j^b is an edge iff a XOR b = b_ij.

An independent transversal on a set of blocks would have to satisfy

a_i XOR a_j = 1 XOR b_ij

for every pair. Fix a reference block v and define the triangle-parity graph T on the other blocks by

ij in E(T) iff b_iv XOR b_ij XOR b_jv = 1.

The no-independent-4-transversal condition implies that T is triangle-free: a triangle in T would make the four-block parity system inconsistent in the required way? More precisely, the independent-transversal equations on {v,i,j,k} are satisfiable iff all three values b_iv XOR b_ij XOR b_jv, b_iv XOR b_ik XOR b_kv, b_ik XOR b_jk XOR b_jv equal 1. Hence a triangle of parity-1 edges is exactly a forbidden independent transversal, so T is triangle-free.

A target clique transversal corresponds to an independent set in T together with the reference block. Thus omega(H) <= r-1 yields alpha(T) <= r-2. Also each clean endpoint has exactly one target neighbor in every other block plus its block mate, so its degree inside U is m; since its full core degree is at most r+1, this saturated subcase satisfies m <= r+1.

This is a genuine special-case compression, but it does not cover pair interactions of size 0 or 1 and does not eliminate m <= r+1.

## 6. A static compatible family: why local constraints alone do not close the theorem

For m=3k, create three parts A,B,C of size 2k each. Take k blocks of type AB, k of type AC, and k of type BC, with each block consisting of one vertex from each of its two named parts. Let H[U] contain:

1. all edges inside each of A, B, and C;
2. the m block edges joining the paired endpoints;
3. no other cross-part edges.

Then:

- every block is a target K2;
- two blocks of the same type have a two-edge matching as their cross graph;
- two blocks of different types have exactly one cross edge, between the endpoints in their shared part;
- alpha(H[U]) <= 3, since A,B,C are cliques;
- omega(H[U]) = 2k for k sufficiently large.

So the static block conditions, including the independent-transversal restriction and a linear clique cap, admit arbitrarily large systems. This is not asserted to extend to a full legal core: the outside vertices, exact excess budget, shell incidence and full repivot contracts are not constructed here.

## 7. Exact remaining gap

The block model proves that the static conditions do not by themselves yield an absolute bound on m. Any valid Clean Pair Nonextension proof must use at least one genuinely global input beyond the pairwise matching rule and alpha(H) <= 3, such as:

- the exact core degree and excess budget across U and H\U;
- the decorated shell-pair incidence total;
- the full legal repivot closure including the old shell pair;
- or the global clique/multicolor constraints on vertices outside U.

Status: graph model and 2-SAT formulation **PROVED_SYMBOLIC**; four-block minimum-edge audit **PROVED by exhaustive finite enumeration**; all-r nonextension **OPEN**.
