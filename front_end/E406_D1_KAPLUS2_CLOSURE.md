# E406 d=1 final-rise: closure of the k+a=2 boundary

Status: `PROVED EMPTY` for every d1 q30->q31 final rise with `k+a=2`, under the explicit E406 boundary contract and the already proved d3 final-rise closure.

Dependencies:

- `E406_D1_MATCHING2_REDUCTION.md`;
- E406 PAIR-13;
- q30/q31 regular-degree restriction;
- full d3 final-rise closure;
- `alpha(R)<=5`, `omega(R)<=11`.

Notation follows `E406_D1_MATCHING2_REDUCTION.md`. Thus `J=M[T]`, `|T|=11`, `nu(J)=2`, and X is the four-endpoint vertex cover of a fixed maximum matching. Put U=T\X, so U is J-independent.

Assume `k+a=2`.

The base identity is

`m+G_T=17`.

For the four cover vertices,

`sum_X h = m+e_J(X)+G_X
         =17+e_J(X)-G_U`.

The two matching edges give `sum_X h>=22`. Hence

`e_J(X)-G_U>=5`.

Since `e_J(X)<=6`, only the following cover geometries can occur:

1. `J[X]=K4`, `G_U=0`, `sum_X h=23`;
2. `J[X]=K4-e`, `G_U=0`, `sum_X h=22`;
3. `J[X]=K4`, `G_U=1`, `sum_X h=22`.

Case 3 is impossible immediately: on K4, summing PAIR-11 over all six edges gives

`3 sum_X h >=66`.

At `sum_X h=22` equality holds on every edge, so every pair of integer h-values would have sum11, forcing all four values to be 11/2.

We close Cases 1 and 2 below.

## 1. K4 cover

Here `sum_X h=23`. Since every K4 edge has h-sum at least11, the only possible multiset is

`{5,6,6,6}`.

Indeed a minimum at most4 forces total at least25, while minimum at least6 forces total at least24.

Let x0 be the h=5 vertex. For every other x in X,

`h(x0)+h(x)=11`.

PAIR-13 in the old p-shell therefore forces both exchanged-endpoint indicators to be1 on each such edge. Consequently s is target-nonadjacent to every vertex of X. The same argument in the new y-shell forces u to be target-nonadjacent to every vertex of X.

The four vertices X are pairwise target-nonadjacent because J[X]=K4. Thus `X union {s}` is an independent5-set.

Their old-core row sizes are

`6,7,7,7,13`,

whose sum is40. Hence among the47 old-core vertices there are at least seven vertices nonadjacent to all five members of `X union {s}`. Any such vertex extends this independent5 to an independent6, contradicting `alpha(R)<=5`.

Therefore the K4 cover is impossible.

## 2. K4-e cover

Let A,B be the nonadjacent pair in J[X], and C,D the remaining two vertices. Because `sum_X h=22` and the two matching edges are tight, the five J-edge inequalities force

`h_A=h_B=11-t`,
`h_C=h_D=t`,

for some integer `6<=t<=9`.

Every J-edge joining a low vertex to a high vertex has h-sum11. Hence PAIR-13 forces both old and new endpoint indicators to equal1 on all four such edges. Therefore s and u are each target-nonadjacent to all four cover vertices.

### 2.1 t=6,7,8

The three vertices A,C,D form a J-triangle, hence a target-independent triple. Together with s they form an independent4-set.

Their old-core row-size sum is

`(12-t)+(t+1)+(t+1)+13 = 27+t`.

Therefore their common old-core nonneighbourhood has size at least

`47-(27+t)=20-t`,

namely at least14,13,12 for `t=6,7,8`.

If this common nonneighbourhood were a clique, it would contain K12, contradicting `omega<=11`. Hence it contains a nonedge pair. Adding that pair to the independent4 produces an independent6, contradiction.

Thus `t=6,7,8` are impossible.

### 2.2 t=9

Now

`h_A=h_B=2`, `h_C=h_D=9`.

The low cover vertices A,B have internal J-degree2, so they have no J-neighbours in U and carry no decoration. Since `G_U=0`, every U-vertex is regular.

All cover-to-U J-edges are therefore incident with C or D. Let z in U be incident with C. In the old shell,

`t_C=h_C+1=10`.

The regular-degree restriction gives `t_z=d_M(z)<=3`. PAIR-13 on Cz forces `t_z=3`. Because z can meet only C,D inside J, this means

- z is J-adjacent to both C and D;
- z is missing-adjacent to s.

Applying the same argument in the q31 shell shows that z is also missing-adjacent to u.

Thus every U-vertex incident with the cover has old missing neighbourhood exactly `{C,D,s}` and new missing neighbourhood exactly `{C,D,u}`.

For such z the old subset charge is

`t_C+t_D+t_s-e_M({C,D,s})
 =10+10+13-3
 =30.

Hence repivoting z from p has q at least30. It cannot have q31, because that would be a d3 final rise, already proved impossible. Therefore z is a q30 plateau pivot.

But y is target-adjacent to z, and in the y-view z has missing degree3 with small side `{C,D,u}`. Reversing the exchange, the edge z->y is therefore itself a d3 q30->q31 final rise, contradicting the complete d3 closure.

So no cover-to-U J-edge can exist.

Yet the cross-edge count is

`m-e_J(X)=12-G_T`.

The total shell-decoration bound is at most8, while s itself has positive decoration in the k+a=2 branch, so `G_T<=7`; hence the cross-edge count is at least5. Contradiction.

Therefore the K4-e cover is impossible.

## 3. Conclusion

Every d1 final rise with `k+a=2` is impossible.

Together with `E406_D1_MATCHING2_REDUCTION.md`, the only remaining d1 exchange parameters are

`k=1`, `a=0`.

Equivalently:

- the exchanged-out old-core vertex u has old core degree13;
- the exchanged-in vertex s has new-core degree12;
- su is a target nonedge;
- `nu(M[T])=2`.
