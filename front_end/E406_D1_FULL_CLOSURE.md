# E406 d=1 final-rise: full closure

Status: `PROVED EMPTY` under the explicit E406 q30->q31 boundary contract.

Dependencies:

- `E406_D1_MATCHING2_REDUCTION.md`;
- `E406_D1_KAPLUS2_CLOSURE.md`;
- complete d2 and d3 final-rise closures;
- E406 PAIR-13 and the regular-degree restriction;
- hereditary `alpha<=5`, `omega<=11`.

The preceding files reduce every d1 final rise to the unique exchange type

`k=1`, `a=0`,

where the exchanged-out old-core vertex has old core degree13, the exchanged-in vertex has new-core degree12, and the exchanged pair is a target nonedge.

Let `J=M[T]` on the common 11 shell vertices. A maximum matching has size2. Let X be the four endpoints of a fixed maximum matching and U=T\X. Then X is a vertex cover and U is J-independent.

Write `e=e_J(X)` and `G_U=sum_{u in U} g_u`. The base identity is

`m+G_T=18`.

The two matching edges and PAIR-11 give

`sum_X h>=22`,

while exact cover accounting gives

`sum_X h=18+e-G_U`.

Hence

`e-G_U>=4`.

The previously closed 5-edge and 6-edge cover branches leave only

`e=4`, `G_U=0`, `sum_X h=22`.

Thus every remaining U-vertex is regular and J[X] is a 4-edge graph on four vertices containing a matching of size2. Up to isomorphism there are only two possibilities:

- a 4-cycle C4;
- a paw (triangle plus pendant edge).

We eliminate both.

## 1. C4 cover

Let the cycle vertices be x1,x2,x3,x4 in order. Summing PAIR-11 over the four cycle edges gives

`2 sum_X h >=44`.

Since `sum_X h=22`, every edge is tight:

`h_i+h_{i+1}=11`.

Thus h alternates between two integers r and 11-r.

Because `G_U=0`, every U-vertex is regular. A cover-to-U J-edge must satisfy PAIR-13 in both the q30 and q31 shells. Since a regular U-vertex has missing degree at most3, any cover endpoint of such an edge must have h at least9.

The low alternating value is at least the internal J-degree2, so the only possible alternating pair is

`2,9,2,9`.

The four tight cycle edges force every cover vertex to be missing-adjacent to both exchanged endpoints s and u. Hence the two h=9 vertices have old and new row weight10.

A regular U-vertex cannot be J-adjacent to only one h=9 vertex: then its full row weight is at most2 and PAIR-13 fails. Therefore every active U-vertex is adjacent in J to both h=9 vertices and is missing-adjacent to both s and u. Its old missing degree is3.

The two h=9 vertices are opposite in C4, so they are not J-adjacent. Thus the old missing side for such a U-vertex consists of the two high cover vertices plus s, with exactly two internal missing edges. Its subset charge is

`10+10+12-2=30`.

Therefore its q-value is at least30. It cannot be31 because d3 final rise is already closed; hence it is q30.

In the q31 y-shell the corresponding small side is the same two cover vertices plus u. The exchanged shell row of u has weight13, so the reverse subset charge is

`10+10+13-2=31`.

Hence the oriented edge from this q30 pivot back to y is a d3 q30->q31 final rise, contradiction.

Therefore no cover-to-U J-edge exists. But

`m-e = (18-G_T)-4 >=7`

because the total shell-decoration budget is at most8. Contradiction.

So the C4 cover is empty.

## 2. Paw cover

Let A be the degree3 vertex of the paw, B,C the other triangle vertices, and D the pendant vertex joined only to A. Put

`h_A=a, h_B=b, h_C=c, h_D=d`.

The four J-edge inequalities are

`a+b>=11`, `a+c>=11`, `b+c>=11`, `a+d>=11`,

and

`a+b+c+d=22`.

Since `(a+d)+(b+c)=22`, both corresponding inequalities are equalities:

`a+d=11`, `b+c=11`.

Tightness forces every one of A,B,C,D to be missing-adjacent to both s and u.

A regular U-vertex can meet only a cover vertex with h at least9. From the equalities and the internal-degree lower bounds, the only possibilities with any cross-edge are `a=9` or `a=10` (after using the B/C symmetry).

### 2.1 a=9

The triangle A,B,C is a J-triangle, hence target-independent. Together with s it is an independent4-set.

Its old-core row-size sum is

`(a+1)+(b+1)+(c+1)+12 = a+26 =35`.

Hence its common old-core nonneighbourhood has size at least12. If that set were a clique it would contain K12, impossible; otherwise a nonedge pair inside it extends the independent4 to an independent6. Contradiction.

Thus a=9 is impossible.

### 2.2 a=10

Then d=1. The pendant vertex D has no cover-to-U edge and carries no decoration. No B/C vertex with h<9 can meet U.

First consider a regular U-vertex z adjacent in J only to A. PAIR-13 forces z to be missing-adjacent to s and u. In the old shell its small missing side is `{A,s}` with row weights11 and12 and one internal missing edge, so the subset charge is22. Hence z has q at least30; d2 final-rise closure excludes q31, so z is q30. In the q31 shell the reverse small side `{A,u}` has row weights11 and13 and one internal missing edge, giving charge23. Thus z->y is a d2 q30->q31 final rise, contradiction.

The only possible second high cover vertex occurs when one of B,C has h=9. If z is adjacent to both A and that h=9 vertex, PAIR-13 again forces z to be missing-adjacent to s and u. Its old small side has size3 and charge30; therefore z is q30, while the reverse y-view has charge31. Hence z->y is a d3 final rise, contradiction.

Thus no regular U-vertex can meet the cover at all.

But again the cover-to-U edge count is at least7. Contradiction.

So the paw cover is empty.

## 3. Conclusion

Both possible 4-edge matching covers are impossible. Therefore

> **Every d=1 q30->q31 final-rise boundary is impossible.**

The E406 final-rise frontier is now reduced to the single distance class d=12.