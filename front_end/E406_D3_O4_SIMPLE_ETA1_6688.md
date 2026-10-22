# E406 d=3 Type-A O4: eta=1 simple-four-double profile (6,6,8,8)

Status: `PROVED EMPTY` under the modern eta=1 O4 simple-four-double contract.

Assume:

- pure sizes `(6,6,8,8)`;
- four distinct double-full vertices carry all four O-units;
- `e(H)=151` and total H-core excess is3;
- full-row counts are `(9,10,10,10)`;
- total partial support incidence is4;
- every H-vertex satisfies `eps<=1`;
- 8-8 double-full edges are impossible.

Let the two 6-rows be A,B and the two 8-rows be C,D.

Because the pure sizes sum28, there are exactly three singleton-full partial carriers. No singleton can be full to an 8-row, so they lie on A,B. Any two singleton carriers on the same 6-row are adjacent: if two such carriers were nonadjacent, each is full to the common support triangle, and in each of the other three pairwise anticomplete support triangles one can choose a vertex missed by both; this gives an independent5-set. Consequently `P_6 union T_6` together with the singleton carriers is a clique, so a 6-row carries at most two singletons. Thus the singleton split is `(1,2)`.

Call B the 6-row carrying two singleton carriers `w1,w2`.

## 1. B must meet a 6-8 double

Suppose B met no 8-row by a double edge. Since the four double edges are distinct, B could then meet only A, so its double degree is at most1.

If B is not the 9-full row, its non-pure full-row demand is `10-6=4`; after the two singleton carriers its double degree must be2, contradiction.

Hence B would have to be the 9-full row, with double degree1. Then A is a 10-full row and carries the remaining one singleton, so its double degree is3. Therefore A is joined by double edges to B,C,D. Since C,D are both 10-full 8-rows and carry no singleton, each requires double degree2. They already have one edge to A; the only edge that could raise both degrees simultaneously is C-D, but 8-8 doubles are forbidden. Contradiction.

Hence B is incident with at least one 6-8 double x.

## 2. A 6-8 double on a two-singleton 6-row is rigid

Let Q be the 8-class joined to B by x. Put

- `a=|P_B\N_H(x)|`;
- `b=|Q\N_H(x)|`;
- `r` = partial support incidence of x;
- `h` = H-neighbours of x outside `P_B union Q`.

The exact degree identity is

`eps_x = 8+r-a-b+h <=1`.

The two missing pure sets are completely joined. Every vertex of `P_B` already has five pure-clique neighbours and the two mandatory singleton neighbours `w1,w2`; hence before excess it has only two H-neighbour slots outside those fixed seven. Every Q-vertex also has only two external H-slots before excess. Therefore the total H-excess on x and the two missing pure sets is at least

`h + 8+r-a-b + a[b-2]_+ + b[a-2]_+`.

The global H-excess is3. If `a>=1`, the displayed lower bound is at least4 (for a=1 it is at least5; for a=2 it is at least4; larger a is stronger). Hence `a=0`.

Then `eps_x<=1` implies `b>=7`. Thus

- x is complete to all six vertices of `P_B`;
- x misses at least seven of the eight Q-vertices;
- x has at most one H-neighbour outside `P_B`.

## 3. x must be adjacent to both singleton carriers

Fix `w in {w1,w2}` and assume `xw` is a nonedge.

The total partial support incidence is4. Besides w there are two other singleton carriers, each using at least one partial incidence. Hence

`r_x+r_w <=2`.

Let R,S be the two support rows different from B and the 8-row Q of x. Since x and w together have at most two partial support incidences total, in each of the K3 rows `T_R,T_S` there exists a vertex missed by both; call them `t_R,t_S`.

The singleton w has H-degree

`d_H(w)=9+eps_w-r_w <=9`.

It is complete to the six vertices of `P_B` and adjacent to the other same-row singleton. Hence it has at most two further H-neighbours outside `P_B`. Since x misses at least seven Q-vertices, there exists `z in Q` nonadjacent to both x and w.

The pure vertex z is anticomplete to `T_R` and `T_S`, and the four support triangles are pairwise anticomplete. Therefore

`{x,w,z,t_R,t_S}`

is an independent5-set, contradiction.

Thus x is adjacent to both w1 and w2.

But w1w2 is an edge, and x,w1,w2 are all complete to `P_B union T_B`. Hence

`P_B union T_B union {x,w1,w2}`

is a clique of size

`6+3+3=12`,

contradicting `omega(C)<=11`.

Therefore no eta=1 simple-four-double `(6,6,8,8)` state exists.