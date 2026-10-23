# K4,9 G=2 split residual — two-support and self-similar B=0 reduction

Status: `PROVED REDUCTION` under the same top-channel CORE211 / lexicographically maximal-pivot contract as `K49_PLATEAU_INDEPENDENT_REDUCTION.md`.

This continues

- `K49_PLATEAU_INDEPENDENT_REDUCTION.md`;
- `K49_G2_SPLIT_CORE_REDUCTION.md`;
- `K49_G2_SPLIT_ROW_OVERLAP.md`;
- `HIGH_LAYER_V3_JOINT_CANONICAL.md`.

It does **not** close E338--E340. It compresses the unique split-decoration K4,9 plateau residual further.

## 1. Setup

Use the unique surviving K4,9 plateau state:

- shell missing graph `M=K_(4,9)` with sides `X` (size4) and `Y` (size9);
- total decoration `G=2`, split `1+1` on two vertices of X;
- the other two X-vertices `x1,x2` are regular q=38 plateau pivots;
- their supports `D1,D2` are disjoint pure K9s of globally degree13 vertices;
- `L=H\(D1 union D2)` has size17;
- the two decorated X-rows `P,Q` have size10 and lie in L;
- every y in Y is regular and has a 4-point core row `R_y subset L`.

The previous row-overlap theorem gives, for every y,

`|R_y intersect P| + |R_y intersect Q| <= 2`.              (1)

The nine Y-vertices all have the same missing set X of size4.

## 2. Equal-or-disjoint rows imply at most two distinct Y-supports

Apply the common-S theorem from `HIGH_LAYER_V3_JOINT_CANONICAL.md` with

- d=4;
- q=38;
- `s=q-d(13-d)=38-36=2`;
- outer defect B=0 because `A\X=Y` is M-independent and undecorated.

Since

`s-B=2<d-1=3`,

any two 4-point supports `R_y,R_z` are either equal or disjoint.

Let k be the number of distinct Y-supports. They are therefore pairwise disjoint and occupy 4k points of L.

By (1), each distinct support contributes at most2 incidences to the two decorated rows P,Q. Outside their union there are `17-4k` vertices, each contributing at most2 incidences to P,Q. Since `|P|+|Q|=20`,

`20 <= 2k + 2(17-4k) = 34-6k`.

Hence

`k<=2`.                                                     (2)

## 3. One distinct support is impossible

Assume all nine Y-vertices share one 4-point support R.

At the q=38 maximal pivot, a d=4 repivot has

`q_y = 36 + P_y`,

with nonnegative defect `P_y`.

If `q_y=38`, then the exchange inserts the four vertices of R into the shell. Every vertex of R is adjacent to all nine Y-vertices in the original graph, hence has global degree greater than13. The old shell has exactly the two decorated X-vertices. Thus a q=38 exchange would strictly increase the lexicographic secondary count tau, contradicting maximality.

Therefore every such y satisfies

`q_y<=37`,

so `P_y<=1`.

Writing the exact d=4 defect as

`P_y = rho + epsilon(R) + m(R) + b`,

where `m(R)=6-e_H(R)`, gives in particular

`m(R)<=1`.

Thus `e_H(R)>=5`, so H[R] contains a target triangle.

But Y is a target K9 and every vertex of R is adjacent to every vertex of Y (R is their common core row). A target triangle in R together with Y gives a target K12, contradicting `omega(F)<=11`.

Therefore

> the nine Y-rows have **exactly two** distinct 4-point supports.

Call them R and S. They are disjoint.

## 4. Self-similarity forces e_H(D1,D2)=0

Put

`B=e_H(D1,D2)`.

We now repivot from p to the regular four-side plateau vertex x1.

Because x1 is a q=38 plateau pivot, and its inserted K9 support D1 consists entirely of globally regular vertices, the new shell has the same secondary decorated count tau=2. Hence x1 is itself lexicographically maximal.

In the x1-view the shell is

`A'={p,x2,x3,x4} disjoint_union D1`.

The first four vertices form a target K4. The set D1 is a target K9. There are no target edges between these two blocks:

- p is nonadjacent to every old-core vertex, hence to D1;
- every vertex of D1 has global degree13, internal old-core degree12, and its unique old-shell target neighbour is x1, so it is nonadjacent to x2,x3,x4.

Thus the missing shell in the x1-view is again K4,9. Its decoration is again split `1+1` on x3,x4.

The two regular four-side plateau pivots in this new view are p and x2.

- The support of p is exactly Y: p is adjacent to all Y and to no old-core vertex. Y is a pure K9 support of globally regular vertices.
- The support of x2 is exactly D2: D2 survives in the x1-core because D1,D2 are disjoint, and x2 is target-anticomplete to Y.

Therefore the same K4,9 plateau equality theorem applies in the x1-view. In particular every other shell row is disjoint from both plateau supports Y and D2.

Each vertex d in D1 is now a nine-side shell vertex. Its x1-view core row contains precisely its old-core neighbours outside D1 (it has no target neighbours in Y, because d was globally degree13 with old-shell neighbour only x1).

Disjointness from the plateau support D2 therefore gives

`N_H(d) intersect D2 = empty`

for every d in D1. Hence

> `B=e_H(D1,D2)=0`.                                        (3)

## 5. Exact residual ledger after B=0

Substituting (3) into the previous 17-point core ledger yields

`e_H(D1,L)=e_H(D2,L)=36`,

`e(H[L])=67`.

Thus the unique split-decoration K4,9 plateau residual is now constrained by

- two anticomplete pure K9 supports D1,D2;
- a 17-point remainder L with exactly67 target edges;
- each Di sends exactly36 target edges into L;
- two decorated size10 rows P,Q contained in L;
- nine size4 Y-rows contained in L;
- exactly two distinct Y-supports R,S, disjoint;
- `5<=|P intersect Q|<=10` from the previous overlap theorem.

This is the new canonical interface for the final K4,9 split residual.

## Boundary

No E338--E340 layer is declared closed here. The remaining task is the realizability/contradiction analysis of this `B=0`, two-support 17-point incidence system.