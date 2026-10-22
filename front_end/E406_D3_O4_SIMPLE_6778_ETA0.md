# E406 d=3 Type-A O4: eta=0 simple-four-double profile (6,7,7,8)

Status: `PROVED EMPTY` under the modern Type-A O4 contract.

Assumptions:

- `eta=0`, `O=4`;
- multiplicity type: four distinct double-full vertices;
- pure sizes `(6,7,7,8)`;
- `e(H)=152`, total H-core excess4;
- full-row counts `(9,10,10,10)`;
- total partial support incidence3.

Because the pure sizes sum28, there are exactly three singleton-full non-pure vertices in addition to the four doubles. Hence each singleton carries exactly one partial incidence and every double has partial count0.

Write the rows

`A=6`, `B=7`, `C=7`, `D=8`.

The eta=0 O4 interface has one 9-full row; all three partial incidences enter its support triangle.

We repeatedly use two modern rigidity facts.

## 1. Modern 7-8 rigidity

Let x be a double full to a 7-class P and the 8-class. Put a,b for its missing counts in the 7- and 8-classes and h for H-neighbours outside the two pure classes.

The exact equation is

`eps_x=9-a-b+h`.

In every Type-A survivor, `eps_x<=2`. The missing sets are completely joined. If `a>=1`, the complete-missing-set excess lower bound together with the exact degree equation exceeds the global four-unit H-excess budget. Hence

`a=0`.

Therefore every 7-8 double is complete to its 7-class. Since `eps_x<=2`, it has at most one H-neighbour outside that K7.

Call this (78-RIGID).

## 2. Same-7 singleton contradiction

Suppose x is a 7-8 double full to row B and w is a singleton full to the same 7-row B. Then both are complete to `P_B union T_B`.

If xw were an edge, `P_B union T_B union {x,w}` would be a K12. Hence xw is a nonedge.

The singleton carries exactly one partial incidence into the 9-full row. In each application below x and w have two common missed support rows, from which we choose one support vertex each. By (78-RIGID), x misses at least seven vertices of the 8-class, while w has at most `1+eps_w` H-neighbours outside P_B. The global excess budget leaves a pure 8-class vertex missed by both. These five vertices form an independent5-set.

## 3. The 6-row A is the 9-full row

The non-pure full-row requirements are

`(3,3,3,2)`.

Singletons cannot be full to A or D. The only graphical singleton split is, up to swapping B,C,

`(w_B,w_C)=(1,2)`.

The forced simple double graph is

`A-B, A-C, A-D, B-D`.

The B-D vertex is a 7-8 double and there is a singleton full to B. They have common missed rows A and C. Section2 gives an independent5 contradiction.

## 4. A 7-row B is the 9-full row

The non-pure requirements are

`(4,2,3,2)`.

### 4.1 Singleton split `(w_A,w_C)=(1,2)`

The double graph is

`A-B, A-C, A-D, B-D`.

The two C-singletons are full to the same 7-row and each has one partial neighbour in T_B.

If they were nonadjacent, choose a T_B vertex missed by both plus arbitrary vertices of T_A and T_D; this extends them to an independent5-set. Hence they are adjacent.

Then

`P_C union T_C union {w_1,w_2}`

is a K12, contradiction.

### 4.2 Singleton split `(w_A,w_C)=(3,0)`

The forced graph contains

`C-B, C-D, B-D`,

one 7-7 and two 7-8 overlaps. Their base pair costs total at least3, leaving at most one additional excess unit.

The two 7-8 vertices are complete to P_B and P_C respectively by (78-RIGID). Under the remaining budget the 7-7 overlap must be complete to one of those same K7 classes. Pair it with the corresponding 7-8 vertex.

The pair is nonadjacent by K12-freeness and has at most one total H-neighbour outside the common K7. Removing the K7, the pair, and that possible neighbour leaves at least25 H-vertices anticomplete to both. Their induced graph must have alpha at most2. Mantel then gives at least144 edges; adding the21 K7 edges yields at least165>152, contradiction.

### 4.3 Singleton split `(w_A,w_C)=(2,1)`

The double graph is 2-regular. Up to symmetry there are three cyclic orders.

Two contain a C-D 7-8 double. Since there is a singleton full to C, Section2 closes them.

The only remaining cycle has

`A-C, C-B, B-D, D-A`.

Let z be the C-B 7-7 overlap and x the B-D 7-8 overlap. Then x is complete to P_B.

Since x already costs at least one excess unit, the 7-7 overlap has local cost at most3. Under `eps_z<=2`, the only possibilities are:

- z complete to P_B;
- z complete to P_C;
- exact missing pattern `(3,3)` with `eps_z=2` and no outside H-neighbour.

If z is complete to P_B, z and x are nonadjacent by K12-freeness. Their total outside-P_B neighbourhood has size at most3. Hence at least12 vertices of `P_C union P_D` are common nonneighbours of z and x. They are also all nonadjacent to a chosen vertex of T_A. If two of those 12 vertices were nonadjacent, they together with z,x,T_A would form an independent5-set. Thus the 12 vertices would have to form a clique, contradicting `omega(C)<=11`.

If z is complete to P_C, pair z with the singleton full to C and apply Section2.

If z has missing pattern `(3,3)`, it has no outside H-neighbour and is nonadjacent to the C-singleton. Choose one vertex each from T_A and T_D. The remaining global excess after `eps_z=2` is at most2, so the singleton has at most two H-neighbours outside P_C. Since z misses three P_B vertices, some P_B vertex is missed by both. It is also nonadjacent to T_A,T_D. These five vertices are independent, contradiction.

## 5. The 8-row D is the 9-full row

The non-pure requirements are

`(4,3,3,1)`.

The only graphical singleton distributions are, up to swapping B,C,

- `(w_A,w_B,w_C)=(1,1,1)`;
- `(2,1,0)`;
- `(2,0,1)`.

### 5.1 Split `(1,1,1)`

The forced graph is

`A-B, A-C, A-D, B-C`.

Let z be the B-C 7-7 overlap, and let w_B,w_C be the singletons full to B,C.

The local 7-7 cost is at most4 and `eps_z<=2`. Up to swapping B,C, every possible low-cost missing pattern is one of

- `(0,7)` with outside count0 or1;
- `(0,6)`;
- `(1,5)`, `(1,6)`, `(1,7)`;
- `(2,4)`;
- `(3,3)`;
- `(3,4)`;

all with outside count0 except the first `(0,7)` option.

If z is complete to P_B, use w_B; if z is complete to P_C, use w_C. In either case z and that singleton are nonadjacent by K12-freeness. Choose support vertices in T_A and T_D (the singleton has only one partial neighbour in T_D). The opposite pure 7-class contains enough vertices missed by z and by the singleton because the local cost of z plus the singleton excess is at most4. This gives an independent5-set.

It remains only the two-sided patterns. For `(2,4)` or `(3,4)` use the singleton corresponding to the side with the smaller pure missing set only if necessary; the opposite missing set has size4 while that singleton has at most one outside-pure neighbour because z's local cost is already4. Hence a common missed pure vertex exists and the same T_A/T_D construction gives an independent5-set. The symmetric forms are identical.

For `(3,3)`, z has `eps_z=2` and no outside H-neighbour. If w_Bw_C is a nonedge, then z,w_B,w_C are independent. Their common missed row A supplies a T_A vertex. The two singletons have together at most four outside-pure neighbours under the remaining two-unit excess budget, so among the eight vertices of P_D there is a vertex missed by both; this gives an independent5-set.

If w_Bw_C is an edge, use z with w_B. The edge to w_C already consumes one of w_B's outside-P_B slots. Since z misses three vertices of P_C and the remaining excess is at most2, some P_C vertex is missed by w_B as well. Together with suitable vertices of T_A and T_D this again gives an independent5-set.

Thus split `(1,1,1)` is impossible.

### 5.2 Split `(2,1,0)`

The forced graph is

`A-B, B-C, B-D, A-C`.

The B-D vertex is a 7-8 double and there is a singleton full to B. Section2 gives an independent5 contradiction. The symmetric `(2,0,1)` case is identical.

## 6. Conclusion

Every row orientation and singleton distribution is impossible. Therefore the modern eta=0 Type-A O4 simple-four-double profile `(6,7,7,8)` is empty.