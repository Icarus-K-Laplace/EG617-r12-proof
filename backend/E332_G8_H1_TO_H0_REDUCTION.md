# E332 reduction of the G=8, h=1 branch to G=8, h=0

Status: `PROVED`.

Assume the canonical E332 state with `G=8` and exactly one undecorated high shell vertex. By `E332_G7_G8_H1_UNIFORM_REDUCTION.md`, the high vertex `a` has missing degree12 and is universal in the missing shell; at most one decorated vertex is low-active.

Write `D` for the decorated set, `k=|D|`, `L` for the low regular set, `r=e_M(L,D)`, and `J=M[D]`. Then

`e(J)=10-r`.

If `r=0`, all decorated vertices are inactive. If `r>0`, all low-D edges meet one active decorated vertex x.

We use pair-row coverage on J-edges and the triangle-row lower bound24.

## 1. Zero-active states are empty

The reduction leaves `k in {5,6,7,8}` and `e(J)=10`.

### k=5

`J=K5`. Any decorated triangle has row-weight sum at most21 because two positive decorations lie outside it. This contradicts the triangle-row lower bound24.

### k=6

The total decoration8 leaves at least three positive decoration units outside any triangle. Hence for a J-triangle the three vertex decorations sum at most5, while their J-degree sum is at most15. The triangle row-weight sum is therefore at most23. Thus J is triangle-free, but a triangle-free graph on six vertices has at most9 edges, not10.

### k=7

There is exactly one decoration2 vertex and all others have decoration1. A triangle not containing the special vertex would require all three J-degrees6, forcing more than10 edges. A triangle containing it would require degree sum at least17, hence at least two triangle vertices have degree6; two degree6 vertices already force at least11 distinct edges. Thus J is triangle-free.

For an edge between two ordinary vertices, pair coverage requires degree sum at least8; for an edge incident with the unique decoration2 vertex, degree sum is at least7. A triangle-free 10-edge graph cannot have degree6. If it has degree5, the standard neighbourhood argument forces the whole graph to be K2,5, where one of the two degree5 vertices is ordinary and has edges to degree2 ordinary vertices, violating the degree-sum condition. Hence maximum degree is at most4. Every ordinary vertex of degree2 or3 could only be adjacent to the unique special vertex, impossible, so ordinary degrees lie in `{0,1,4}`. Total degree20 forces exactly four ordinary degree4 vertices. Their 16 incident degree units would require at least six edges among those four vertices, contradicting triangle-freeness. Hence k=7 is impossible.

### k=8

All decorations equal1. Any J-triangle would require the degree sum of its three vertices to be at least18. The three triangle vertices would then have at least15 distinct incident edges, contradicting `e(J)=10`. So J is triangle-free.

Pair coverage now gives `d_J(u)+d_J(v)>=8` on every edge. In a triangle-free graph on8 vertices one always has `d(u)+d(v)<=8` on an edge, so equality holds everywhere. Fix an edge uv. The disjoint neighbourhoods of u and v partition all other six vertices, yielding a bipartition of all8 vertices; moreover every neighbour of u must have complementary degree and hence be adjacent to the entire opposite part. Therefore J is complete bipartite. But a complete bipartite graph with part sizes summing8 cannot have exactly10 edges. Contradiction.

Thus every zero-active G=8,h=1 state is empty.

## 2. One-active states except (k,r)=(3,7) are empty

The exact windows are

- k=3, r=7 or8;
- k=4, r=4,5,6,7;
- k=5, r=3,4,5,6;
- k=6, r=3,4,5;
- k=7, r=3,4.

Let x be the unique active decoration.

For k=7, total decoration8 gives one extra unit only. The active-weight condition forces x to have J-degree5 or6; the inactive graph has one edge, whose endpoint row-weight sum is at most8. Pair coverage fails. Thus k=7 is empty.

For k=6, the active-weight condition leaves at most two inactive J-edges. With total decoration8, every possible matching/path inactive edge has endpoint row-weight sum at most10. Pair coverage fails. Thus k=6 is empty.

For k=5, the possible inactive graphs have one to three edges. The active-weight condition consumes enough decoration that every inactive edge would require either endpoint degree sum8 (forcing two J-universal vertices and more total edges than available) or decoration beyond the total budget8. Thus all r=3,4,5,6 are empty.

For k=4:

- r=4 gives J=K4 and the inactive triangle has row-weight sum at most16<24;
- r=5 leaves an inactive triangle or a two-edge configuration whose pair inequalities exceed the decoration budget;
- r=6 leaves at most two inactive edges and pair coverage fails;
- r=7 likewise leaves one/two-edge inactive graphs with insufficient endpoint weight.

Hence k=4 is empty.

For `(k,r)=(3,8)`, J is a two-edge path. Independence of the nine-low set plus the two inactive decorated vertices forces the inactive-inactive edge to be present, so the active vertex is a leaf. Pair coverage on the inactive edge forces all but one decoration unit onto the inactive pair, leaving active decoration1; then the active row weight is11, contradicting the strengthened zero-gap lower bound12 for a low-active decorated vertex.

Therefore only `(k,r)=(3,7)` remains.

## 3. Exact terminal (k,r)=(3,7)

Here `J=K3`. Let x be active and y,z inactive. Exact weight accounting gives

- `g_x=2`, `t_x=12`;
- `g_y+g_z=6`, `t_y+t_z=12`.

Hence the missing triangles `a,y,z` and `x,y,z` both have total row-size exactly24. The triangle-row equality forces

- `D_a,D_y,D_z` pairwise disjoint;
- `D_x,D_y,D_z` pairwise disjoint.

Strong zero-gap on ax gives `1<=|D_a intersect D_x|<=2`, so the complement of `D_a union D_x` consists of the 12-set `D_y union D_z` plus at most one extra core vertex.

Every one of the seven active low rows has size2 and is disjoint from both `D_a` and `D_x`, hence lies in that 12- or 13-point complement.

Choose an active low row whose two endpoints lie in `D_y union D_z`; such a row exists unless the possible extra core vertex occurs in all seven rows, in which case its global excess alone already makes the repivot decoration exceed8. For an endpoint v in `D_y union D_z`, if its active-low multiplicity is m_v then its global degree excess is at least m_v.

Repivot at such an active low. The old active decoration x of size2 leaves the shell. If the two imported endpoints have total global excess at least3, the new shell has

`G' >= 8-2+3 =9`,

contradicting the universal E332 bound `G'<=q'-22<=8`.

Therefore any non-contradictory repivot must import exactly two units of excess, one from each endpoint. In particular both imported endpoints are decorated in the new shell. The retained old regular vertices have new missing degree at most2, and the old pivot has new missing degree2. Hence the new shell has

`G'=8` and `h'=0`.

Thus the terminal G=8,h=1 state either contradicts the decoration ceiling immediately or produces a legitimate G=8,h=0 E332 pivot.

## Conclusion

Every G=8,h=1 survivor yields a G=8,h=0 survivor. Therefore, for the purpose of eliminating E332, it is sufficient to eliminate the single remaining family

`G=8, h=0`.
