# q36 f=2 far-target-K2 topology — global d2-row reduction

Status: `PROVED REDUCTION` under `Q36_F2_SHELL_LEDGER_REDUCTION.md`, q36 lexicographic maximality, and the parent `alpha(F)<=4` contract.

This strengthens the existing far-target-K2 interface. In every layer with at least one d3 owner, there is at most one d2 row.

## 1. Setup

Use the f=2 notation from `Q36_F2_SHELL_LEDGER_REDUCTION.md` with the two far regular vertices F forming a target K2. Let C be the low target clique, |C|=c, and X the decorated shell set, |X|=11-c.

The set

`{p} union C union F`

is a target clique of size c+3, hence c<=8 from omega(F)<=11. In particular X is nonempty in every far-K2 branch.

Let n2 be the number of low owners of missing degree2 and n3=c-n2 the number of d3 owners.

## 2. Every d2 support is globally regular

If a d2 row exists, the exact d2 formula from the master f=2 ledger gives

`q_y=36+a_F+kappa(D_y)+m(D_y)+e_F(F,D_y)`

because mu=0.

q36 maximality therefore forces

- `a_F=0`;
- `kappa(D_y)=0`;
- `m(D_y)=0`;
- `e_F(F,D_y)=0`;
- `q_y=36`.

Thus D_y is a target K2 of core-degree12 vertices, target-anticomplete to F.

Distinct d2 supports are already known to be disjoint and pairwise target-anticomplete, and repeated supports are impossible.

Now use lexicographic maximality. Repivoting y removes only the two regular far vertices F. Since `a_F=0`, every decorated shell vertex in X is retained. The old shell has exactly |X| globally decorated vertices.

If either support vertex of D_y were globally decorated, the new q36 shell would contain all old decorated X plus that inserted decorated support vertex, so tau would strictly increase. Contradiction.

Hence:

> every vertex of every d2 support is globally regular.          (1)

Since such a support vertex has core degree12 and exactly its owner as a shell neighbour, global regularity also implies that it has no target neighbour in the old shell other than that owner. In particular it is target-nonadjacent to every vertex of X and to every other low owner.          (2)

## 3. Three d2 rows are impossible

Assume three d2 owners exist, with distinct supports D1,D2,D3.

The supports are pairwise disjoint and pairwise target-anticomplete. Choose one vertex ui from each Di.

Choose any far vertex f in F and any decorated shell vertex x in X. Because a_F=0,

- fx is a target nonedge;
- f is target-nonadjacent to every ui;
- by (2), x is target-nonadjacent to every ui;
- the ui are pairwise target-nonadjacent.

Therefore

`{u1,u2,u3,f,x}`

is an independent5-set in the parent graph, contradicting alpha(F)<=4.

Hence

> n2<=2.                                                     (3)

## 4. Two d2 rows cannot coexist with a d3 row

Assume n2=2 and n3>0. Let D1,D2 be the two d2 supports and choose vertices u1 in D1, u2 in D2.

Take any d3 owner y. Let x_y in X be its unique decorated missing neighbour. Then

- u1u2 is a target nonedge because the two d2 supports are target-anticomplete;
- f is target-nonadjacent to u1,u2,y,x_y for either far vertex f in F (`a_F=0` and every low owner misses F);
- y is target-nonadjacent to u1,u2 because its core support is different from D1,D2;
- yx_y is a target nonedge by definition;
- x_y is target-nonadjacent to u1,u2 by global regularity (2).

Thus

`{u1,u2,f,y,x_y}`

is an independent5-set, contradiction.

Therefore

> if n3>0, then n2<=1.                                     (4)

Equivalently:

> for every far-K2 layer with c>=3, n2<=1.                  (5)

(The only formal exception not treated by this argument is the tiny all-d2 state c=n2=2.)

## 5. Consequence for the d3-class allowance budget

If c>=3, at least c-1 low rows are d3. Existing shell counting still gives at most two d3 missing-set classes.

When two d3 classes x,z occur, summing the exact thresholds gives

`A_x+A_z <= nu-2`.

The decoration floor gives

`nu<=3+n2`

because a_F=0. Using n2<=1 from (5):

> `A_x+A_z<=2`.                                             (6)

In the no-d2 subbranch n2=0 this recovers the sharper known bound

> `A_x+A_z<=1`.                                             (7)

Hence every genuine high-c far-K2 survivor is now one of:

1. all d3 rows in one missing-set class;
2. two d3 classes with total allowance at most2;
3. one d2 row plus the remaining d3 rows, again with at most two d3 classes and total two-class allowance at most2.

This file is a reduction, not a full closure of the far-K2 topology.