# K11–K11 support-pair excess obstruction

Status: **PROVED**

Assume the five core hypotheses. Let I={s1,s2,s3,s4} be the independent degree-12 four-set and K_i the private cliques from FOUR_CLIQUE_REDUCTION.md.

Suppose z in Z has I-support exactly {s_i,s_j}, and both K_i,K_j have order 11.

Set

A=K_i minus N(z),   B=K_j minus N(z),
a=|A|,               b=|B|.

Because z cannot be complete to a K11 (otherwise z plus that K11 is a K12), a,b>=1. Also A and B exclude the distinguished vertices s_i,s_j.

## 1. Independent-five blocker

Every pair across A x B is an edge.

If x in A and y in B were nonadjacent, then

{z,x,y} union (I minus {s_i,s_j})

would be an independent five-set:

- z misses x,y by definition of A,B;
- z misses the other two distinguished vertices by its exact I-support;
- x,y each have only their own distinguished I-neighbor;
- the other two points of I are nonadjacent.

This contradicts alpha(H)<=4. Thus A x B is complete bipartite.

## 2. Degree-excess cost

The vertex z has at least 22-a-b neighbors in K_i union K_j, so

epsilon(z)>=max(0,10-a-b).

Every x in A has its ten internal K_i neighbors and all b vertices of B as neighbors. Hence

epsilon(x)>=max(0,b-2).

Similarly every y in B satisfies

epsilon(y)>=max(0,a-2).

The sets {z}, A, B are pairwise disjoint. Therefore

epsilon(z)+sum_A epsilon+sum_B epsilon
>= f(a,b),

where

f(a,b)=max(0,10-a-b)+a max(0,b-2)+b max(0,a-2).

For all positive integers a,b, f(a,b)>=6. An exact case split:

- if a=1 or b=1, f>=7;
- if a=b=2, f=6;
- if one of a,b is 2 and the other is at least 3, f>=7;
- if a,b>=3, the last two terms alone are at least
  a(b-2)+b(a-2)>=6.

Thus every K11–K11 support pair consumes at least six excess units.

But the whole graph has only four:

sum_v epsilon(v)=4.

Contradiction.

## Conclusion

**No vertex of Z can have support exactly two distinguished vertices whose private cliques are both K11.**

This is stronger than the Q32 analogue: the local obstruction costs at least 6 while the Q33 budget is only 4.
