# E406 d=3 Type-A O4: eta=0 simple-four-double profile (5,7,8,8)

Status: `PROVED EMPTY` under the modern E406 Type-A O4 contract.

This is a new modern closure. It does not import the historical S30 CLOSED labels.

Dependencies:

- `E406_D3_TYPEA_O4_MODERN_INTERFACE.md`;
- the pure-class clique and singleton-full-row lemmas;
- the simple-double pair-overlap bound from the audited S30 O4 arithmetic;
- `alpha(C)<=4`, `omega(C)<=11`.

We assume:

- `eta=0`;
- `O=4`;
- the multiplicity type is four distinct double-full vertices;
- pure sizes are `(5,7,8,8)`;
- `e(H)=152`, total H-core excess4;
- full-row counts are `(9,10,10,10)`;
- total partial support incidence is3.

The four doubles account for all four O-units. Since the pure sizes sum28, there are exactly three additional non-pure H-vertices. They are singleton-full partial carriers. Because total partial incidence is3, each singleton carries exactly one partial incidence and every double has partial count0.

A singleton cannot be full to an 8-class.

Let the pure rows be

`A=5`, `B=7`, `C=D=8`.

An 8-8 double is impossible because its pair-overlap excess cost is at least6>4.

## 1. Row A is the 9-full row: impossible

The non-pure full-row requirements are

`(4,3,2,2)`.

No singleton may be full to row A, because all singleton partial incidences enter the unique 9-full row in the eta=0 O4 interface. No singleton may be full to C or D. Hence all three singletons are full to B.

The double-degree requirements become

`d_A=4, d_B=0, d_C=2, d_D=2`.

But a simple graph on four row labels has maximum degree3. Contradiction.

## 2. Row B is the 9-full row

All three singleton carriers are full to A. The double-degree sequence is

`(2,2,2,2)`.

Avoiding the forbidden C-D 8-8 edge forces the unique 4-cycle

`A-C-B-D-A`

up to swapping C,D. Thus there are exactly two 7-8 doubles, `x_C` and `x_D`, both full to row B.

Let their pair-overlap costs be c_C,c_D. Each is at least1 and

`c_C+c_D<=4`.

For a 7-8 double x under this budget, any missed vertex in the 7-class would force at least four pure-vertex excess units by the complete-missing-set bound. Therefore every such x is complete to P_B.

Moreover, if c is its total local cost, the number of H-neighbours outside P_B is at most `c-1`.

The two doubles cannot be adjacent: otherwise

`P_B union T_B union {x_C,x_D}`

would be a K12.

Delete P_B, the two doubles, and all their outside-P_B neighbours. The remaining set U has size at least

`35-7-2-[(c_C-1)+(c_D-1)] >= 24`.

Both doubles are nonadjacent and anticomplete to U. Hence an independent triple in U would give an independent5-set in C. Therefore `alpha(U)<=2`.

Mantel gives

`e(U)>=C(24,2)-floor(24^2/4)=276-144=132`.

The pure class P_B is a K7, contributing21 additional H-edges disjoint from E(U). Hence

`e(H)>=132+21=153`,

contradicting `e(H)=152`.

Thus this orientation is impossible.

## 3. An 8-row is the 9-full row

Assume C is the 9-full row. The non-pure full-row requirements are

`(5,3,1,2)`.

Write w_A+w_B=3 for the singleton counts.

Simplicity forces `w_A>=2`.

### 3.1 w_A=3, w_B=0

The double-degree sequence is

`(2,3,1,2)`.

The unique simple realization avoiding C-D has edges

`A-B, B-C, B-D, A-D`.

Thus there are two 7-8 doubles B-C and B-D. The argument of Section2 applies verbatim and gives the same 24-point alpha<=2 contradiction.

### 3.2 w_A=2, w_B=1

The double-degree sequence is

`(3,2,1,2)`.

The unique simple realization avoiding C-D is

`A-B, A-C, A-D, B-D`.

Let x be the unique 7-8 double B-D, and let w be the singleton full to B.

Let c be the local pair-overlap cost of x. Since c<=4, the same 7-8 rigidity shows

- x is complete to P_B;
- x has at most `c-1` H-neighbours outside P_B.

The singleton w is complete to P_B. Its H-degree is `8+eps_w`, hence it has at most `1+eps_w` H-neighbours outside P_B.

Also xw is a nonedge, because otherwise `P_B union T_B union {x,w}` is a K12.

The global excess budget gives

`c+eps_w<=4`.

Choose a vertex `t_A in T_A`. Since A is neither a full nor partial row of w? In this orientation all singleton partial incidences enter C, so w is nonadjacent to all of T_A. The double x is full only to B,D and is also nonadjacent to T_A.

Choose `t_C in T_C` avoiding the unique partial neighbour of w. The double x is nonadjacent to all of T_C.

Thus x,w,t_A,t_C are pairwise nonadjacent.

Finally x misses at least `9-c` vertices of P_D: if b is its missing count in the 8-class, `c>=9-b`. The singleton w can have at most `1+eps_w<=5-c` neighbours in P_D. Therefore at least

`(9-c)-(5-c)=4`

vertices of P_D are nonadjacent to both x and w. Choose one such vertex v.

Since v is pure to row D, it is nonadjacent to t_A and t_C. Therefore

`{x,w,t_A,t_C,v}`

is an independent5-set in C, contradiction.

Hence the final orientation is impossible.

## 4. Conclusion

Every eta=0 modern Type-A O4 simple-four-double state with pure profile `(5,7,8,8)` is impossible.