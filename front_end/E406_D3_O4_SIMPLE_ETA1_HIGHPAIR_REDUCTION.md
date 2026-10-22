# E406 d=3 Type-A O4: eta=1 simple-four-double high-pair reduction

Status: `PROVED` reduction. The eta=1 simple-four-double branch is reduced to exactly four low-row pure profiles:

`(5,6,8,8)`, `(6,6,8,8)`, `(6,6,7,8)`, `(6,7,7,7)`.

All other eta=1 simple-four-double pure profiles are empty.

## 1. Contract

Assume

- `eta=1`, `O=4`;
- H has35 vertices, `e(H)=151`;
- total H-core excess is3;
- full-row counts are `(9,10,10,10)`;
- total partial support incidence is4;
- four distinct double-full vertices carry all four O-units.

The saturated Type-A identity gives, for every H-vertex,

`eps_x+s_D(x)=1`,

so

`eps_x<=1`.      (EPS1)

Pure classes are cliques of size at most8. Singleton-full partial carriers occur only in pure classes of size at most7.

## 2. Exact high-pair rigidity

Call a double **high** if its row-size pair is 7-7 or 7-8.

### 2.1 No 8-8 double

The standard pair-overlap lower bound is at least6 before any partial correction. Since the total H-excess is3, 8-8 doubles are impossible.

### 2.2 7-8 doubles

Let x be full to a 7-class P and an 8-class Q. Let

- a = number of missed P-vertices;
- b = number of missed Q-vertices;
- r = partial support incidence of x;
- h = H-neighbours outside P union Q.

Then

`eps_x=9+r-a-b+h<=1`.

The missing sets are completely joined. If `r>=1`, the degree inequality forces `a+b>=9+h`; every feasible `a>=1` already requires more than three pure/excess units, while `a=0` would require `b>=9`, impossible. Hence r=0.

With r=0, if `a>=1` the complete-missing-set excess lower bound again exceeds3. Therefore a=0. EPS1 then forces

`b=8`, `h=0`, `eps_x=1`.

Thus every 7-8 double satisfies

`N_H(x)=P_7`, `eps_x=1`, `r_x=0`.      (H78)

### 2.3 7-7 doubles

Let x be full to two 7-classes. The exact equation is

`eps_x=8+r-a-b+h<=1`.

If r>=1, no feasible missing-set pattern fits the three-unit total excess. Hence r=0.

If both a,b are positive, the complete-missing-set excess bound exceeds the total budget once EPS1 is imposed. Thus one of a,b is0; the other is7, h=0, and eps_x=1.

Therefore every 7-7 double has an oriented 7-hub P such that

`N_H(x)=P`, `eps_x=1`, `r_x=0`.      (H77)

Hence every high double consumes exactly one of the three H-excess units and has H-neighbourhood exactly one K7 pure class.

## 3. Two forbidden hub phenomena

### 3.1 No repeated 7-hub

Suppose distinct high doubles x,y both satisfy

`N_H(x)=N_H(y)=P`, `|P|=7`.

Then x,y are nonadjacent and anticomplete to

`U=H\(P union {x,y})`, `|U|=26`.

If U contained an independent triple, x,y would extend it to an independent5-set in C. Thus `alpha(U)<=2`.

Mantel gives

`e(U)>=C(26,2)-floor(26^2/4)=156`,

already larger than `e(H)=151`. Contradiction.

So a 7-class can be the oriented hub of at most one high double.

### 3.2 A singleton-bearing 7-row cannot be a hub

Let x be a high double with `N_H(x)=P_7`, and let w be a singleton-full partial carrier on the same 7-row.

Both are complete to `P_7 union T_7`. If xw were an edge they would form a K12 with this K10, so xw is a nonedge.

The singleton has partial incidence at least1 and eps_w<=1, hence

`d_H(w)-7 = 2+eps_w-r_w <=2`.

Delete P_7, x,w and the at-most-two outside-P_7 neighbours of w. At least24 H-vertices remain anticomplete to x,w. Their alpha is at most2, so they span at least132 edges. Adding the21 edges of P_7 gives153>151. Contradiction.

Therefore a 7-row containing a singleton cannot be the hub of a high double.

## 4. Two singleton carriers on one 7-row are impossible

Let w1,w2 be singleton-full carriers on the same 7-row.

If w1w2 is an edge, `P_7 union T_7 union {w1,w2}` is K12.

Assume they are nonadjacent. In the eta=1 O4 interface the partial-incidence distribution is either

- `(4,0,0,0)`, or
- `(3,1,0,0)`

across the four support rows (up to order). Hence among the three rows different from the common full row of w1,w2 there is at least one pure row R with zero partial incidence.

Each wi has at most two H-neighbours outside P_7. Delete P_7,w1,w2 and their outside neighbours; at least22 H-vertices remain anticomplete to w1,w2.

Choose any t in T_R. Since R has zero partial incidence, t has exactly the ten full-row H-neighbours. Therefore at least12 of the 22 vertices are also nonadjacent to t.

Now w1,w2,t are independent. Any nonedge among those at least12 common H-nonneighbours would form an independent5-set. Hence those vertices would have to form a clique of size at least12, contradicting `omega(C)<=11`.

Thus two singleton carriers cannot share a 7-row.      (S7)

## 5. Exhaustive eta=1 pure profiles

Four double vertices plus w singleton carriers give

`sum p_i =31-w`,

and `0<=w<=4`. With `p_i<=8`, the sorted possibilities are exactly:

### sum31
`(7,8,8,8)`

### sum30
`(6,8,8,8)`, `(7,7,8,8)`

### sum29
`(5,8,8,8)`, `(6,7,8,8)`, `(7,7,7,8)`

### sum28
`(4,8,8,8)`, `(5,7,8,8)`, `(6,6,8,8)`, `(6,7,7,8)`, `(7,7,7,7)`

### sum27
`(3,8,8,8)`, `(4,7,8,8)`, `(5,6,8,8)`, `(5,7,7,8)`, `(6,6,7,8)`, `(6,7,7,7)`.

We now eliminate every profile except the four stated at the top.

## 6. Three 8-classes are impossible by row-degree count

For any profile `(p,8,8,8)`, no singleton can be full to an 8-row and no 8-8 double is allowed. Hence every double edge would have to join the unique p-row to an 8-row.

If the p-row is the 9-full row, the three 8-rows require double degrees `2,2,2`, total6. If an 8-row is the 9-full row, they require `1,2,2`, total5. Four edges through the p-row supply only four 8-side incidences.

Contradiction.

Thus all five profiles

`(3,8,8,8)`, `(4,8,8,8)`, `(5,8,8,8)`, `(6,8,8,8)`, `(7,8,8,8)`

are empty.

## 7. Two 8-classes with at least one 7-class

Write the rows `A=p<=7`, `B=7`, `C=D=8` (for `(7,7,8,8)` take A=7 also).

Because C-D is forbidden and the four double edges are distinct, the row graph is obtained from the five possible edges

`AB, AC, AD, BC, BD`

by deleting exactly one edge.

The full-row count of an 8-row is1 or2 beyond its pure class. Hence:

- if the 9-full row is A or B, both 8-rows have double degree2 and the row graph is the K2,2 between `{A,B}` and `{C,D}`;
- if the 9-full row is C, then C has degree1 and D degree2, so the missing edge is AC or BC (and similarly with C,D swapped).

For `(p,7,8,8)` with p=4,5,6, every viable row-degree solution has one of exactly two forms:

1. B contains a singleton and is incident with a 7-8 edge; this is forbidden by Section3.2;
2. B has no singleton and is incident with both 7-8 edges B-C and B-D; these two edges have the same forced hub P_B, forbidden by Section3.1.

Thus

`(4,7,8,8)`, `(5,7,8,8)`, `(6,7,8,8)`

are empty.

For `(7,7,8,8)`, the same degree check shows that one singleton-free 7-row necessarily carries both of its 7-8 edges, while the other 7-row carries the unique singleton. Hence Section3.1 again gives a repeated hub. So `(7,7,8,8)` is empty.

The only two-8 profiles not covered by this high-pair argument are

`(5,6,8,8)` and `(6,6,8,8)`.

## 8. Profiles in which every double is high

In `(7,7,7,8)` and `(7,7,7,7)` every double joins rows of sizes7/8. Four doubles therefore consume at least four H-excess units by H77/H78, contradicting the exact total3.

Thus both are empty.

## 9. The remaining one-8 high profiles

### `(6,7,7,8)`

A direct row-degree check by the location of the 9-full row gives the following:

- if the 6-row is 9-full, the unique 7-8 edge is incident with a 7-row carrying a singleton -> Section3.2;
- if a 7-row B is 9-full, the possible singleton splits either
  - place two singletons on the other 7-row -> forbidden by (S7), or
  - create two high edges whose forced orientations repeat B or hit a singleton-bearing 7-row;
- if the 8-row is 9-full, every graphical split creates either a singleton-bearing 7-8 hub or a 7-7/7-8 pair forced to the same singleton-free 7-hub.

Hence `(6,7,7,8)` is empty.

### `(5,7,7,8)`

There are four singleton carriers. The same row-degree analysis is even tighter:

- when the 5-row is 9-full, every graphical split either gives a singleton-bearing 7-8 hub or a repeated 7-hub;
- when a 7-row is 9-full, the only row-degree residue not immediately a hub violation contains two singleton carriers on the other 7-row, forbidden by (S7);
- when the 8-row is 9-full, every graphical split gives a singleton-bearing 7-hub or a repeated 7-hub.

Thus `(5,7,7,8)` is empty.

## 10. Final eta=1 simple-four-double frontier

All eta=1 pure profiles are eliminated except

`(5,6,8,8)`, `(6,6,8,8)`, `(6,6,7,8)`, `(6,7,7,7)`.

These four profiles contain too few 7-8/7-7 high pairs for the hub theorem alone to close them. They are the complete remaining eta=1 simple-four-double frontier.