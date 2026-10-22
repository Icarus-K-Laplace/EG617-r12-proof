# E406 q30->q31 final-rise normal forms

Status: `PROVED` for the reductions below. The distance-10 final-rise class is `PROVED EMPTY`. `E406` itself remains `OPEN`.

This note continues `front_end/E406_Q31_COEXISTENCE_REDUCTION.md`. It is the assistant-owned E406 line and does not overlap the Astra-A E407--E408 assignment.

Assume the explicit T61 E406 contract. Let `p` be a degree-13 pivot with `q_p=30`, 47-core `C` of 285 edges, and let `y` be a legal degree-13 shell repivot with `q_y=31`, new 47-core `C'` of 284 edges. Put

- `S=N_M(y)`, `d=|S|`;
- `D=N_C(y)`, so `|D|=d`;
- `r_D=e_C(D)`, `r_S=e_R(S)`;
- `e_SD=e_R(S,D)`;
- `epsilon_D=sum_{u in D}(d_C(u)-12)`;
- `epsilon'_S=sum_{s in S}(d_C'(s)-12)`;
- `q_out=e_M(A\S)+G_{A\S}`.

The exact final-rise identities are

`r_D = 12d-C(d,2)-31 + epsilon_D + q_out + e_SD`,  (FR1)

and

`epsilon_D-epsilon'_S = 1+r_D-r_S`.  (FR2)

The old core has total internal excess `6`, the new core total internal excess `4`.

## 1. Core nonedge codegree lemma

If `u,v` are nonadjacent vertices of any inherited 47-core with minimum degree at least12, then

`|N_C(u) union N_C(v)| >= 22`.

Indeed the common nonneighbours of `u,v` form an inherited `R(2,.)` object. There cannot be24 such vertices because `R(2,24)` is empty. Hence at most23 of the other45 vertices are common nonneighbours, so the union of the two neighbourhoods has size at least22.

Writing `d_C(u)=12+epsilon_u`, `d_C(v)=12+epsilon_v`, this gives

`codeg_C(u,v) <= 2+epsilon_u+epsilon_v`.  (CN)

This lemma is repeatedly used below.

## 2. Distance d=10 is impossible

For `d=10`, (FR1) gives

`r_D = 44 + L`,

where

`L=epsilon_D+q_out+e_SD`.

Since `r_D<=45`, `L<=1`.

### 2.1 L=0 is impossible

Then `D` induces `K10-e`, all ten vertices have old core excess0, and `q_out=e_SD=0`.

The two endpoints of the unique missing edge have the other eight vertices of `D` as common core neighbours. But (CN) allows at most2 common neighbours for a nonedge whose endpoints both have excess0. Contradiction.

### 2.2 The only possible L=1 equality data

Using (FR2), `r_S<=45`, and nonnegative new-core excess, the only surviving possibility is

`epsilon_D=1`, `q_out=0`, `e_SD=0`, `r_D=r_S=45`, `epsilon'_S=0`.

Thus both `D` and `S` are K10s. The ten vertices of `S` have new-core degree exactly12 and therefore old row weight exactly3.

Let `T=A\(S union {y})={t1,t2}`. Since `q_out=0`, both `t1,t2` are regular and adjacent in the old shell. If

`a_i=e_R(t_i,S)`,

then for each `s in S` its decoration equals the number of its adjacencies to `T`, hence

`a_1+a_2=G_p<=8`.

For a regular `t_i`, its old missing degree is `10-a_i`. The q30 extreme-degree theorem forces this degree to lie in `{2,3,10}`; hence

`a_i in {8,7,0}`.

Since `a_1+a_2<=8`, at least one of the two vertices, say `t`, has `a_t=0`: it is anticomplete to `S`.

Repivot at this `t`. Its missing degree is again10. The same exact calculation shows that its 10-row `E=N_C(t)` must induce a K10. The only alternative `K10-e` equality shape is again excluded by (CN). Moreover `E` is anticomplete to `S`.

Now `D` and `E` are two K10s in the old 47-core, attached to the adjacent degree-13 shell vertices `y,t`.

They cannot be equal, because otherwise `D union {y,t}` would be a K12. Put `r=|D intersect E|`.

Any common vertex belongs to a support whose total core excess is at most1, hence has old core degree at most13. It is adjacent to all vertices of `D union E`, so

`19-r <= 13`,

and therefore `r>=6`.

If `a in D\E` and `b in E\D` were nonadjacent, they would have the `r` common vertices `D intersect E` as common core neighbours. By (CN) their common-neighbour count is at most4, since each endpoint has excess at most1. This contradicts `r>=6`.

Therefore every exclusive cross-pair is an edge, so `D union E` is a clique of size `20-r`. Since the inherited core has clique number at most11,

`r>=9`.

Distinctness gives `r<=9`, hence `r=9` and `D union E` is a K11.

Finally consider the induced13-set

`U=(D union E) union {y,t}`.

It contains at least

- 55 edges of the K11;
- 10 edges from `y` to `D`;
- 10 edges from `t` to `E`;
- the edge `yt`.

Thus `e(U)>=76`, contradicting the hereditary cap `D(13)=67`.

Hence

`d=10` final rise is impossible.

## 3. Distance d=3: exact three-family reduction

For `d=3`, (FR1) gives

`r_D=2+epsilon_D+q_out+e_SD<=3`.

Combining this with (FR2), `r_S<=3`, and nonnegative excess gives

`q_out=0`, `e_SD=0`, `r_S=3`, `epsilon'_S=0`.

Thus `S` is a K3 in the new core. The old support `D` is exactly one of

- a P3 with `epsilon_D=0`, or
- a K3 with total `epsilon_D=1`.

Since `q_out=0`, the ten vertices

`B0=A\S`

are all regular and form a clique in the old shell. Together with the old pivot `p`, they form a K11 of degree-13 vertices.

Each `s in S` has old row weight exactly10: in the new core it has degree12, of which two edges are internal to the K3 `S`. Hence the old missing shell is bipartite between `S` and `B0`.

For `b in B0`, regularity gives `t_b=d_M(b)`. Every missing edge `sb` satisfies the row-union lower bound, so `10+t_b>=12`; therefore a B-side missing degree1 is impossible.

A B-side degree2 is also impossible. For such a `b`, its two missing neighbours lie in `S`, have total weight20 and no missing edge between them. The exact repivot lower bound gives

`q_b-q_p >= 3+epsilon_{D_b}-e_C(D_b)+e_R(S_b,D_b) >=2`,

since `|D_b|=2` and `e_C(D_b)<=1`. This would give `q_b>=32`, contradicting the global E406 ceiling31.

Therefore every B-side vertex has missing degree0 or3. If `n0` is the number of degree0 vertices, then

`M = K_{3,r} disjoint_union n0 K1`, `r=10-n0`.

The three S-side row weights are10, so each S-vertex has decoration `10-r=n0`. Therefore

`G_p=3n0`.

Since every q30 shell has `G_p<=8`,

`n0 in {0,1,2}`.

Consequently the only possible distance-3 final-rise shells are exactly

`K_{3,10}`,

`K_{3,9} disjoint_union K1`,

`K_{3,8} disjoint_union 2K1`,

with S-side decorations respectively `0,1,2` on each of the three S vertices.

For every active B-side pivot `b`, its 3-row support `D_b` is anticomplete to S and is one of

- K3 with old core excess0 if `q_b=30`;
- P3 with old core excess0 if `q_b=31`;
- K3 with total old core excess1 if `q_b=31`.

Thus the d3 problem is no longer a shell-classification problem; it is a compatibility problem for 8--10 dense 3-row supports attached to a fixed K11.

## 4. Distance d=11: dense-block reduction

Let `T` be the unique shell vertex outside `S union {y}` and let its decoration be `g_T`. Then `q_out=g_T` and (FR1) gives

`r_D=46+epsilon_D+g_T+e_SD`.

Let `K` be the complement of `C[D]` on the 11 vertices D and let `m=e(K)=55-r_D`. Thus

`m=9-(epsilon_D+g_T+e_SD)`.

For a complement edge `uv`, let `rho_u,rho_v` be the K-degrees. The number of common C-neighbours of u,v inside D is at least `12-rho_u-rho_v`. Applying (CN) yields

`rho_u+rho_v+epsilon_u+epsilon_v>=9`.

Since for a K-edge `rho_u+rho_v<=m+1`, every complement edge satisfies

`epsilon_u+epsilon_v>=8-m`.

As the old core has total excess6, `m=1` is impossible. Also `m>=1` because `D` cannot be a K11: together with y that would form a K12. Hence

`2<=m<=9`.

The displayed edge inequality implies `epsilon_D>=8-m`; substituting into the formula for m gives

`g_T+e_SD<=1`.

Therefore every d11 final-rise state is a dense 11-block whose complement has only 2--9 edges and which has at most one total unit of external decoration/cross slack.

## 5. Distance d=12: paired dense 12-block reduction

Here `q_out=0`. Equation (FR1) becomes

`r_D=47+epsilon_D+e_SD`.

Because `y` is complete to D, the induced13-set `D union {y}` has `12+r_D` edges. The hereditary cap `D(13)=67` gives

`47<=r_D<=55`,

and hence

`epsilon_D+e_SD<=8`.

In the new core, the inserted 12-set S satisfies

`r_S=48+e_SD+epsilon'_S`.

Likewise `S union {p}` is an induced13-set, so `r_S<=55`; therefore

`e_SD+epsilon'_S<=7`.

Thus d12 reduces to two dense 12-vertex modules with edge ranges 47--55 and 48--55 and only tiny cross/excess slack.

## 6. Distance d=1: common-K11 reduction

Let `D={u}`, `S={s}`. Equations (FR1)--(FR2) give

`epsilon_C(u)-epsilon_{C'}(s)=1`,

so `epsilon_C(u)>=1`.

The exact q relation gives

`t_s = 11+epsilon_C(u)+1_{su}`.

Let `T=A\{s,y}`; `|T|=11`. The thirteen vertices `{p,y} union T` contain the edge py, both p and y are complete to T, and T itself has `C(11,2)-e_M(T)` target edges. The cap `D(13)=67` therefore gives

`e_M(T)>=11`.

Equivalently the common closed-neighbourhood block of a d1 final rise must carry at least11 missing edges. More exactly, the same cap combined with the charge identity gives

`G_T+epsilon_C(u)+1_{su}<=8`.

Thus d1 is reduced to an 11-vertex common-neighbour deficit graph with at least11 missing edges and a small residual decoration/excess budget.

## 7. Current final-rise frontier

The old six-distance frontier

`{1,2,3,10,11,12}`

has now become

- `d=10`: PROVED EMPTY;
- `d=3`: exactly three `K_{3,r}` shell families, `r=8,9,10`, with 8--10 dense 3-row supports;
- `d=11`: 11-block complement has 2--9 edges and external slack at most1;
- `d=12`: paired dense-12 modules with the displayed edge/slack bounds;
- `d=1`: common-K11 deficit graph has at least11 missing edges;
- `d=2`: still requires a new invariant.

No claim that E406 is closed is made.