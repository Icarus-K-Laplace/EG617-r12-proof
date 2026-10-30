# Exhaustion of all Q33 support templates

Status: **PROVED**

Use the independent four-set I, private cliques K_i, exceptional set Z, and support incidence identities from FOUR_CLIQUE_REDUCTION.md.

The only possible values are |Z|=3,4,5. The K11–K11 support-pair obstruction and the K10 completion-capacity lemma then eliminate every case.

## 1. Case |Z|=3

All four private cliques are K11. The three support sizes sum to eight, so the support-size multiset is either

(4,2,2) or (3,3,2).

In either case at least one z in Z has support size exactly two. Both corresponding private cliques are K11. This is forbidden by K11_PAIR_EXCESS_OBSTRUCTION.md.

Thus |Z|=3 is impossible.

## 2. Case |Z|=4

There is one K10, denoted K0, and three K11s K1,K2,K3. The support sizes are (3,2,2,2).

If a 2-support vertex joins two K11 labels, the K11-pair obstruction applies. Otherwise the three 2-support vertices are exactly

z_1: {s_0,s_1},   z_2: {s_0,s_2},   z_3: {s_0,s_3},

and the 3-support vertex is supported on {s_1,s_2,s_3}.

For i=1,2,3 put

A_i=K0 minus N(z_i),  a_i=|A_i|,
B_i=K_i minus N(z_i), b_i=|B_i|.

Here a_i>=0 and b_i>=1. The independent-five blocker gives every edge between A_i and B_i.

For u in K0, each z_i either is adjacent to u or is replaced by the forced b_i neighbors in B_i. Since K0 has nine internal neighbors,

d(u)>=9+3+sum_{i:u in A_i}(b_i-1)
     =12+sum_{i:u in A_i}(b_i-1).

For v in B_i, d(v)>=10+a_i. Also d(z_i)>=21-a_i-b_i. Summing these disjoint B_i and z_i contributions together with the pointwise K0 bound gives

4 >= sum_v epsilon(v)
  >= sum_{i=1}^3 [
       max(0,9-a_i-b_i)
       + a_i(b_i-1)
       + b_i max(0,a_i-2)
     ].

For every a>=1,b>=1,

max(0,9-a-b)+a(b-1)+b max(0,a-2) >= 6.

For completeness:
- a=1 gives at least 7;
- a=2 gives at least 6;
- a>=3,b=1 gives at least 6;
- if a>=3,b>=2, the last two terms have minimum 5, attained only at (a,b)=(3,2), where the first term is 4; at every other pair those last two terms are at least 8. Thus the full expression is at least 6.

Thus no a_i can be positive. All three z_i would have to be complete to K0. This contradicts the theorem that at most one external vertex can be complete to a K10.

Therefore |Z|=4 is impossible.

## 3. Case |Z|=5, clique pattern (9,11,11,11)

The support sizes are all two. The K9 distinguished vertex has support degree four, so four of the five support pairs meet it. The remaining support pair joins two of the three K11 labels.

That pair is forbidden by the K11–K11 obstruction.

Therefore this pattern is impossible.

## 4. Case |Z|=5, clique pattern (10,10,11,11)

Call the K10 labels 1,2 and the K11 labels 3,4.

If any support pair joins 3 and 4, the K11-pair obstruction applies. Assume no such pair exists.

The support multigraph has five edges and degree sequence (3,3,2,2). Since labels 3 and 4 each have degree two and no 34 edge, there are exactly four mixed edges between {1,2} and {3,4}. The remaining edge is 12. Each K10 label is incident with two mixed edges, and each K11 label is incident with two mixed edges.

Thus the mixed edges form a 2x2 nonnegative integer matrix with every row and column sum two. Up to relabeling, there are exactly two patterns:

- **D (all ones):** [[1,1],[1,1]];
- **P (double diagonal):** [[2,0],[0,2]].

The anti-diagonal double pattern is P after relabeling.

### 4A. Pattern P: double supports

There are two distinct support points on K1-K3 and two on K2-K4 (or the relabeled pairing).

At most one external point can be complete to a fixed K10. Therefore in each doubled pair at least one support point is not complete to its K10.

For a selected noncomplete mixed support point z on a K10-K11 pair, let A be its nonneighbors in the K10, |A|=a>=1, and B its nonneighbors in the K11, |B|=b>=1. The blocker A x B is complete.

The degree bounds give

epsilon(z)+sum_A epsilon+sum_B epsilon
>= g(a,b),

where

g(a,b)=max(0,9-a-b)+a max(0,b-3)+b max(0,a-2).

For all a,b>=1, g(a,b)>=4. The minimum is four at (a,b)=(2,3). This follows by splitting a=1, a=2, and a>=3; for a>=3, the cases b=1, b=2, and b>=3 each give at least six.

The two selected support points use disjoint K10/K11 clique pairs, so their charged vertex sets are disjoint. Hence the total excess is at least 4+4=8, contradicting the total budget four.

Pattern P is impossible.

### 4B. Pattern D: all four mixed supports

There are four distinct mixed support points, one on each pair 13,14,23,24, plus the K10-K10 support point 12.

For every support edge e=ij, let z_e be its Z vertex and define

A_{i,e}=K_i minus N(z_e),   a_{i,e}=|A_{i,e}|.

The independent-five blocker makes A_{i,e} x A_{j,e} complete.

For a vertex v in K_i, let M_i(v) be the incident support edges e for which v belongs to A_{i,e}. Since |K_i|-1=12-d_i,

d(v)>=12+sum_{e in M_i(v)}(a_{j,e}-1).

The possible negative summands are exactly -1:
- at a K10 vertex, at most one can occur, from the unique K10-K10 edge; its other two incident supports go to K11s, whose missing sets are nonempty;
- at a K11 vertex, there are two incident mixed supports. If both summands are -1, the desired right-hand side below is zero; otherwise at most one negative summand occurs.

For nonnegative integer x_l and at most one additional -1, max(0,sum x_l-1)>=sum max(0,x_l-1). If both terms at a K11 vertex are -1, both sides of the required inequality are zero. Therefore, pointwise,

epsilon(v)>=sum_{e in M_i(v)} max(0,a_{j,e}-2).

Summing over the four private cliques gives

sum_{v outside Z} epsilon(v)
>= sum_{e=ij} [
     a_{i,e} max(0,a_{j,e}-2)
     +a_{j,e} max(0,a_{i,e}-2)
   ].

For a mixed edge e, write a for its K10 missing-set size and b for its K11 missing-set size. Here b>=1. Its support point has

epsilon(z_e)>=max(0,9-a-b).

If a>=1 as well, the corresponding terms in the preceding sum plus epsilon(z_e) are at least

h(a,b)=max(0,9-a-b)
       +a max(0,b-2)
       +b max(0,a-2)
       >=5.

The last inequality holds for all positive integers a,b: the minimum is five at (2,2); if one variable is 1 the value is at least six; if one is 2 and the other at least 3 the value is at least six; and if both are at least 3 the last two terms alone are at least six.

At most one of the two mixed support points incident with K1 can be complete to K1, and the same holds for K2. Hence at least two of the four mixed supports have a>=1. They are distinct support points. The pointwise incidence inequality above ensures that overlapping missing sets in a shared clique are not double-counted.

Consequently the total excess is at least 5+5=10, contradicting the total budget four.

Pattern D is impossible.

## 5. Exhaustion conclusion

Every support configuration with |Z|=3,4,5 is excluded. The finite enumerator in INDEPENDENT_VERIFIER.py independently checks the labelled support-multiset counts and the two 2x2 matrix classes; the analytic arguments above are the proof.
