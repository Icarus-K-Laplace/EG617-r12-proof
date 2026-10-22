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

In every Type-A survivor, `eps_x<=2`. The missing sets are completely joined. If `a>=1`, the pure-set excess lower bound together with the above degree equation already exceeds the global four-unit H-excess budget. Hence

`a=0`.

Therefore every 7-8 double is complete to its 7-class. Since `eps_x<=2`, it has at most one H-neighbour outside that K7.

We call this (78-RIGID).

## 2. Same-7 singleton contradiction

Suppose x is a 7-8 double full to row B and w is a singleton full to the same 7-row B. Then both are complete to `P_B union T_B`.

If xw were an edge, `P_B union T_B union {x,w}` would be a K12. Hence xw is a nonedge.

The singleton carries exactly one partial incidence into the 9-full row. Therefore, whenever there are two support rows different from B and from the 8-row of x which x and w both miss, one may choose one vertex from each. By (78-RIGID), x misses at least seven vertices of the 8-class, while w has at most `1+eps_w` H-neighbours outside P_B. The global excess budget leaves enough common missed pure vertices to choose a fifth vertex. This produces an independent5-set.

The applications below spell out the required rows explicitly.

## 3. The 6-row A is the 9-full row

The non-pure full-row requirements are

`(3,3,3,2)`.

Singletons cannot be full to A (their partial incidence enters T_A) or to D (size8). Thus the singleton distribution is `(w_B,w_C)=(1,2)` or `(2,1)`; the extreme `(0,3)/(3,0)` choices make a simple double graph impossible.

Up to swapping B,C, the unique viable double graph is

`A-B, A-C, A-D, B-D`.

The B-D vertex is a 7-8 double and there is a singleton full to B. They both miss rows A and C (the singleton only has one partial neighbour in T_A). Choose

- a vertex of T_A missed by the singleton;
- any vertex of T_C;
- a pure P_D vertex missed by both.

The last choice exists because the 7-8 double misses at least seven P_D vertices, while the singleton has at most `1+eps_w` outside-P_B neighbours and the total excess is4.

Together with the double and singleton these vertices form an independent5-set. Contradiction.

## 4. A 7-row B is the 9-full row

The non-pure requirements are

`(4,2,3,2)`.

### 4.1 Singleton split (1,0,2,0)

If `w_A=1,w_C=2`, the double graph is again

`A-B, A-C, A-D, B-D`.

But the two C-singletons are full to the same 7-row and each has one partial neighbour in T_B.

If they were nonadjacent, choose a T_B vertex missed by both plus arbitrary vertices of T_A and T_D; this extends them to an independent5-set. Hence they must be adjacent.

Then

`P_C union T_C union {w_1,w_2}`

is a K12, contradiction.

### 4.2 Singleton split (3,0,0,0)

The forced double graph contains

`C-B, C-D, B-D`

among its edges, i.e. one 7-7 and two 7-8 overlaps. The three pair-overlap costs have base total at least3, leaving at most one excess unit beyond their equality patterns.

The two 7-8 vertices are complete to P_B and P_C respectively by (78-RIGID). The 7-7 overlap, under the remaining budget, must be complete to one of those two K7 classes. Pair it with the corresponding 7-8 vertex.

Those two vertices are nonadjacent (otherwise the common `P_7 union T_7` gives K12) and have at most one total outside-neighbour beyond the common K7 under the four-unit budget. Removing the common K7, the pair, and that outside neighbour leaves at least25 H-vertices anticomplete to both. Their induced graph must have alpha at most2, otherwise the pair extends an independent triple to an independent5-set.

Mantel gives at least144 edges on those25 vertices; adding the21 edges of the common K7 yields at least165>152, contradiction.

### 4.3 Singleton split (2,0,1,0): the 2-regular case

The double graph is a 4-cycle. Up to symmetry there are three cyclic orders.

Two of them contain a 7-8 double on the C-D pair. Since there is a singleton full to C, Section2 gives an immediate independent5 contradiction.

The only remaining cyclic order has edges

`A-C, C-B, B-D, D-A`.

Let z be the C-B 7-7 overlap and x the B-D 7-8 overlap.

The 7-8 vertex x is complete to P_B.

The 7-7 overlap z has local pair cost at most3 (x already costs at least1). Under `eps_z<=2`, its only possible low-cost forms are:

- z is complete to P_B;
- z is complete to P_C;
- the exact symmetric missing pattern `(3,3)`, with `eps_z=2` and no outside H-neighbour.

If z is complete to P_B, pair z with x. They are nonadjacent by K12-freeness. Their common nonneighbourhood inside `P_C union P_D`, after deleting their at-most-three outside neighbours, has at least12 vertices, all also nonadjacent to any chosen T_A vertex. Thus an independent edge there would create an independent5-set with z,x,T_A, so those at least12 vertices would have to form a clique, contradicting `omega(C)<=11`.

If z is complete to P_C, pair z with the singleton full to C and apply the same-row singleton contradiction.

If z has the `(3,3)` missing pattern, it has no outside H-neighbour. Pair z with the singleton full to C. Choose one vertex each from T_A and T_D. The singleton has at most two H-neighbours outside P_C under the remaining excess budget, while z misses three vertices of P_B, so a P_B vertex missed by both exists. These five vertices are independent, contradiction.

Thus the 2-regular case is impossible.

## 5. The 8-row D is the 9-full row

The non-pure requirements are

`(4,3,3,1)`.

The only graphical singleton distributions are, up to swapping B,C:

### 5.1 `(w_A,w_B,w_C)=(1,1,1)`

The double graph is

`A-B, A-C, A-D, B-C`.

Let z be the B-C 7-7 overlap. There are singletons full to both B and C.

Every low-cost 7-7 form either is complete to one of P_B,P_C or has a two-sided missing pattern with no outside neighbour. In the first case use the singleton on the same 7-row; in the second use one of the two singletons, together with vertices of T_A,T_D and a common missed pure vertex, to obtain an independent5-set exactly as in Section4.3.

### 5.2 `(w_A,w_B,w_C)=(2,1,0)`

The forced graph is

`A-B, B-C, B-D, A-C`.

The B-D vertex is a 7-8 double and there is a singleton full to B. Section2 gives an immediate independent5 contradiction. The symmetric `(2,0,1)` case is identical.

No other singleton distribution gives a simple degree sequence.

## 6. Conclusion

All row orientations and singleton distributions are impossible. Therefore the modern eta=0 Type-A O4 simple-four-double profile `(6,7,7,8)` is empty.