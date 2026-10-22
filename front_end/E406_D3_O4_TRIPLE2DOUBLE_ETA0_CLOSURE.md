# E406 d=3 Type-A O4: eta=0 one-triple + two-double closure

Status: `PROVED EMPTY` under the modern Type-A O4 eta=0 contract.

## 0. Contract and exact hypergraph

Assume:

- H has 35 vertices, 152 edges, total H-core excess 4;
- full-row counts are `(9,10,10,10)`;
- total partial support incidence `R=3`;
- O=4 is realized by one triple-full vertex and two double-full vertices.

The row-demand / K12 argument from `E406_D3_O4_TRIPLE2DOUBLE_ETA1_CLOSURE.md` does not use eta. Therefore it applies verbatim:

- if `delta_i` marks the unique 9-full row, then the multi-full row degrees satisfy
  `m_i=2-delta_i`;
- the singleton count on row i is `s_i=8-p_i`;
- the 9-full row A has multi-degree1;
- the other rows B,C,D have multi-degree2;
- the triple is exactly BCD;
- the two doubles form a perfect matching, say AB and CD.

Since each singleton-full carrier uses at least one partial incidence and `R=3`, the total number w of singleton carriers satisfies `w<=3`.

Hence the possible pure profiles are exactly:

- w=0: `(8,8,8,8)`;
- w=1: `(7,8,8,8)`;
- w=2: `(6,8,8,8)`, `(7,7,8,8)`;
- w=3: `(5,8,8,8)`, `(6,7,8,8)`, `(7,7,7,8)`.

## 1. A local singleton-bearing 7-8 lemma

Let x be a double full to a 7-row P and an 8-row Q, and suppose the 7-row contains a singleton-full carrier u.

Let a,b be the numbers of pure nonneighbours of x in P,Q, and r the partial support incidence of x. The pair-overlap lower bound on the disjoint set consisting of x and its two missing pure sets is

`Phi = 9+r-a-b + a[b-3]_+ + b[a-2]_+`.

Assume this local excess cost is at most2.

If `a>=1`, the displayed quantity is at least5+r. Hence a=0. Thus x is complete to P and

`9+r-b <=2`,

so `b>=7+r`; in particular r<=1 and x misses at least seven Q-vertices.

The exact degree identity gives

`eps_x=9+r-b+h<=2`,

where h is the number of H-neighbours outside `P union Q`. Therefore x has at most one H-neighbour outside P.

Because x and u are both complete to `P union T_P`, the edge xu would create a K12. Hence xu is a nonedge.

There is at least one further positive local excess unit elsewhere in the eta=0 configuration under the applications below, so `eps_u<=2`. Since u is a singleton carrier, `r_u>=1`, and

`d_H(u)=9+eps_u-r_u`.

After its seven neighbours in P, u has at most three H-neighbours outside P.

The double x is full to only P and Q. Let R,S be the other two support rows. The total partial budget is3, and besides u there is at least one other singleton carrier in the only nontrivial application `(7,7,8,8)`, so `r_u<=2`. Hence in each of T_R,T_S there is a vertex missed by both x and u.

Also x misses at least seven Q-vertices while u meets at most three vertices outside P, so some `z in Q` is missed by both.

Thus

`{x,u,z,t_R,t_S}`

is an independent5-set, contradiction.

Therefore:

> A singleton-bearing 7-row cannot support a 7-8 double whose disjoint local excess cost is at most2.

## 2. Easy pure profiles

### `(8,8,8,8)`
The triple BCD is `(8,8,8)`, excluded by the triple-transversal lemma.

### `(7,8,8,8)`
If A is the 7-row, BCD is `(8,8,8)`; if A is an 8-row, BCD is `(7,8,8)`. Both are excluded.

### `(6,8,8,8)`
If A is 6, BCD is `(8,8,8)`. If A is 8, the perfect matching AB/CD necessarily contains an 8-8 double. Impossible.

### `(5,8,8,8)`
The same argument: either the triple is `(8,8,8)` or the perfect matching contains an 8-8 double.

### `(6,7,8,8)`
If A is 6, the triple is `(7,8,8)`, excluded.
If A is 7 or 8, every perfect matching avoiding 8-8 contains a 7-8 double incident with the unique 7-row.
Here w=3, so all three units of R are consumed by the three singleton carriers; every multi-full vertex has r=0.
For a 7-8 double with r=0, the pair-overlap inequality under the global four-unit excess budget forces a=0 (a>=1 costs at least5), so it is complete to the singleton-bearing P7. The same K12/independent5 argument as Section1 gives a contradiction.

### `(7,7,7,8)`
Again w=3, so multi-full vertices have r=0. Every perfect matching consists of one 7-8 and one 7-7 double. The 7-8 double is incident with a singleton-bearing 7-row and is excluded by the same local rigidity.

## 3. The only delicate profile: `(7,7,8,8)`

If A is a 7-row, the triple BCD is `(7,8,8)`, excluded.

Thus A is an 8-row. Avoiding an 8-8 double forces the perfect matching to consist of exactly two disjoint 7-8 doubles, each incident with one of the two 7-rows. Both 7-rows contain a singleton because `s_i=8-p_i=1`.

Let the disjoint local pair-overlap excess costs of the two doubles be c1,c2. The two pairs use disjoint pure classes and distinct double vertices, so their local excess budgets are disjoint. Each 7-8 pair has cost at least1, while the total H-excess is4. Therefore

`c1+c2<=4`,

and at least one of c1,c2 is at most2.

Apply the singleton-bearing 7-8 lemma from Section1 to that double. Contradiction.

Thus `(7,7,8,8)` is impossible.

## 4. Conclusion

Every eta=0 pure profile is impossible. Hence

> **ETA0 TRIPLE-DOUBLE CLOSURE. No modern Type-A d=3 O4 state with eta=0 realizes the multiplicity type one triple + two doubles.**

Together with:

- eta=0 and eta=1 simple-four-double closures;
- eta=1 one-triple/two-double closure;
- uniform two-triple closure;
- no-four-full theorem;

this closes the entire modern Type-A d=3 O4 layer.