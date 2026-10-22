# E332 full closure of the G=7, h=1 branch

Status: `PROVED EMPTY`.

Assume the canonical E332 state and the uniform one-high reduction from `E332_G7_G8_H1_UNIFORM_REDUCTION.md`:

- `q=30`, `e(core)=211`;
- total decoration `G=7`;
- exactly one undecorated high shell vertex `a`;
- the high has missing degree12 and is universal in the missing shell;
- decorated set `D`, `k=|D|`;
- low regular set `L`, `|L|=12-k`;
- every low has neighbourhood `{a}` or `{a,x}` for the unique active decorated vertex `x` if one exists;
- at most one decorated vertex is low-active;
- with `r=e_M(L,D)` and `J=M[D]`, `e(J)=11-r`;
- pair-row coverage holds on every J-edge;
- every J-triangle has row-weight sum at least24.

For a decorated vertex `v`, write `t_v=d_M(v)+g_v`. If `r>0`, all low-D edges meet the unique active vertex `x`.

## 1. Zero-active states

The reduction leaves only `r=0`, `k=6` or7. Then `e(J)=11`.

### k=6

The positive decorations are a permutation of `(2,1,1,1,1,1)`. Every decorated weight is at most8. In fact any J-triangle has total row weight at most22, contradicting the triangle-row lower bound24. Thus J is triangle-free. But a triangle-free graph on six vertices has at most9 edges, while `e(J)=11`. Contradiction.

### k=7

All decorations equal1, so `t_v=d_J(v)+2`. A J-triangle would require degree sum at least18, hence all three triangle vertices would have J-degree6. Three degree6 vertices already force at least15 distinct J-edges, contradicting `e(J)=11`. Thus J is triangle-free.

For every J-edge `uv`, pair-row coverage gives `d_J(u)+d_J(v)>=8`. No vertex can have degree6: if v had degree6, its six neighbours are independent because J is triangle-free, so J would have only the six star edges. No vertex can have degree5 either: its five neighbours are independent, and with the unique non-neighbour w all remaining edges are incident with w, giving at most `5+5=10` edges. Hence every positive degree is at most4. The edge condition then forces every nonisolated vertex to have degree exactly4, but the total degree is22, not divisible by4. Contradiction.

Therefore no zero-active G=7,h=1 state exists.

## 2. One-active states: large k

The exact windows are

- `(k,r)=(7,4)`;
- `(6,4),(6,5)`;
- `(5,4),(5,5),(5,6)`;
- `(4,5),(4,6),(4,7)`;
- `(3,8)`.

Let x be the unique active decorated vertex.

### (7,4)

Here `e(J)=7`. Active weight at least12 forces x to have J-degree6, so x is J-universal and the inactive graph has one edge. Since all seven decorations equal1, the two endpoints of that inactive edge have row weight4 each, contradicting pair-row coverage12.

### (6,4)

Here `e(J)=7`. The active vertex must have J-degree5 and decoration2; all five inactive decorations equal1. The inactive graph has two edges. On an inactive edge, even the path-centre endpoint has row weight at most5 and the other at most4, below12. Contradiction.

### (6,5)

Here `e(J)=6`. If the active J-degree is5, the inactive graph has one edge; if it is4, the inactive graph has two edges and the active decoration is forced to2. In either case the total positive decoration available on the inactive endpoints is too small: a matching edge has endpoint row-weight sum at most10, and a two-edge path has centre-leaf sum at most10. Contradiction.

### (5,4)

Here `e(J)=7`. The active vertex is J-universal, has decoration3, and every inactive decoration equals1. The inactive graph has three edges. An inactive edge `uv` has `t_u+t_v=6+d_I(u)+d_I(v)` and pair coverage would require internal-degree sum at least6. A three-edge graph on four vertices has edge endpoint internal-degree sum at most4. Contradiction.

### (5,5)

Here `e(J)=6`.

- If active degree4, the inactive graph has two edges and the inactive decoration total is at most5. Every possible two-edge graph gives an endpoint row-weight sum below12.
- If active degree3, the inactive graph has three edges and active decoration at least3, so all inactive decorations equal1. Pair coverage on any inactive edge would require both endpoints to have total J-degree4; two such endpoints would force at least five inactive edges, not three.

Contradiction.

### (5,6)

Here `e(J)=5`. Active degree is2,3 or4.

- degree4 leaves one inactive edge; even concentrating all available inactive decoration on its endpoints gives row-weight sum below12;
- degree3 leaves two inactive edges; a matching or path again has endpoint sum below12 under the total decoration budget;
- degree2 leaves three inactive edges and active decoration at least3, so all four inactive decorations are1; pair coverage would require an inactive edge with both endpoints J-degree4, which is impossible with only five total J-edges.

Thus every k=5 state is impossible.

## 3. One-active states: k=4

### (4,5)

`e(J)=6`, so `J=K4`. Active weight at least12 forces active decoration at least3, leaving total decoration4 on the three inactive vertices. Those three form a J-triangle, whose total row weight is `12+4=16<24`. Contradiction.

### (4,6)

`e(J)=5`, so `J=K4-e`.

If the active vertex has degree2, the three inactive vertices form a triangle; its row-weight sum is at most15, below24.

If the active vertex has degree3, the inactive graph is a two-edge path. For either active-inactive-inactive J-triangle, the triangle inequality is equivalent to saying that the decoration on the omitted inactive leaf is nonpositive, contradicting positivity. Hence impossible.

### (4,7)

`e(J)=4`.

- active degree3 leaves one inactive edge. The triangle consisting of the active vertex and that edge would require the decorations on those three vertices to sum to at least7, leaving no positive decoration for the fourth decorated vertex.
- active degree2 leaves a two-edge path on the inactive vertices and no edge between the two active neighbours. Pair coverage on the two path edges requires `g_i+g_w>=6` and `g_j+g_w>=6`, impossible under total decoration7 and positive active decoration.
- active degree1 leaves an inactive triangle, whose row-weight sum is far below24.

Thus k=4 is impossible.

## 4. Final cell (k,r)=(3,8)

Here `J=K3`. Active weight at least12 and the inactive edge force exact decoration data:

- active decoration `g_x=1`, so `t_x=12`;
- the two inactive decorations sum6 and their row weights sum12.

Hence both missing triangles `a,y,z` and `x,y,z` have total row-size exactly24. The triangle-row union lemma forces

- `D_a,D_y,D_z` pairwise disjoint;
- `D_x,D_y,D_z` pairwise disjoint.

The strong zero-gap theorem on `ax` gives `|D_a intersect D_x|<=1`. Thus `D_y union D_z` is a 12-set disjoint from both D_a and D_x, and every active low row is disjoint from D_a and D_x, hence lies inside `D_y union D_z`.

There are eight active low rows, each of size2, giving16 incidences on a 12-set. If `m_v` is the multiplicity of a core vertex among these rows, then `sum m_v=16`; therefore

`sum m_v^2 >= 4*4 + 8*1 =24`.

So some active low row `{u,v}` satisfies `m_u+m_v>=3`.

Repivot at that degree-13 low vertex. The active decorated shell vertex x (decoration1) leaves the shell, while the two imported core vertices have global excess at least `m_u,m_v` respectively (each has core degree at least12, one base shell adjacency to y or z, and its active-low multiplicity). Thus the new shell decoration is at least

`G' >= 7-1+(m_u+m_v) >=9`.

But every E332 degree-13 pivot satisfies `q'<=30`, while every inherited shell has `z'>=22`; hence `G'=q'-z'<=8`. Contradiction.

Therefore `(k,r)=(3,8)` is impossible.

## Conclusion

No `G=7,h=1` state exists.

Together with the previously proved `G=7,h=0` closure and the exact `H2-G7-K4minusE` closure, the entire decoration layer

`G=7`

is `PROVED EMPTY`.

Thus any E332 survivor must have `G=8`, with `h=0` or `h=1`.