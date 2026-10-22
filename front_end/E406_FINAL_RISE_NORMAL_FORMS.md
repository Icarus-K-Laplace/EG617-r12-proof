# E406 q30->q31 final-rise normal forms

Status: `PROVED` for the reductions below. The distance-10 class and the d2 terminal `b=8` are `PROVED EMPTY`. `E406` itself remains `OPEN`.

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

## 1. Strengthened row-union lemma at E406

If `uv` is a missing-shell edge in either a q30 or q31 view, then

`|D_u union D_v| >= 13`,

and hence `t_u+t_v>=13`.

Proof. Suppose the row union has size at most12. Choose a 35-set `W` of core vertices disjoint from that union. Since `u,v` are target-nonadjacent and both are target-anticomplete to W, an independent4 in W would create an independent6 in the 61-point parent. Thus `W in R(3,35)` and CORE211 gives `e(W)>=211`.

Let `X=C-W`, so `|X|=12`. Since the current 47-core has minimum degree at least12,

`e(W)=e(C)-sum_X d_C(x)+e_C(X)`
`<=285-12*12+C(12,2)=207`

in the q30 view, and at most206 in the q31 view. Contradiction.

This lemma is the E406 source of the edge-weight inequality used below; it does not rely on importing the Astra-A package.

## 2. Core nonedge codegree lemma

If `u,v` are nonadjacent vertices of any inherited 47-core with minimum degree at least12, then

`|N_C(u) union N_C(v)| >= 22`.

Indeed the common nonneighbours of `u,v` form an inherited `R(2,.)` object. There cannot be24 such vertices because `R(2,24)` is empty. Hence at most23 of the other45 vertices are common nonneighbours, so the union of the two neighbourhoods has size at least22.

Writing `d_C(u)=12+epsilon_u`, `d_C(v)=12+epsilon_v`, this gives

`codeg_C(u,v) <= 2+epsilon_u+epsilon_v`.  (CN)

## 3. Distance d=10 is impossible

For `d=10`, (FR1) gives

`r_D = 44 + L`,

where

`L=epsilon_D+q_out+e_SD`.

Since `r_D<=45`, `L<=1`.

If `L=0`, then `D` induces `K10-e`, all ten vertices have old core excess0, and `q_out=e_SD=0`. The two endpoints of the unique missing edge have the other eight vertices of D as common core neighbours, contradicting (CN), which allows at most2.

For `L=1`, (FR2), `r_S<=45`, and nonnegative new-core excess force

`epsilon_D=1`, `q_out=0`, `e_SD=0`, `r_D=r_S=45`, `epsilon'_S=0`.

Thus both D and S are K10s. The ten vertices of S have new-core degree12 and therefore old row weight3.

Let `T=A\(S union {y})={t1,t2}`. Since `q_out=0`, both are regular and target-adjacent. If `a_i=e_R(t_i,S)`, then `a_1+a_2=G_p<=8`. Each regular `t_i` has old missing degree `10-a_i`; the q30 extreme-degree theorem gives `a_i in {8,7,0}`. Hence at least one, say t, has `a_t=0`.

Repivot at t. Its missing degree is again10. The same exact calculation forces its 10-row E to induce K10; the K10-e alternative is excluded by (CN). E is anticomplete to S.

D and E cannot coincide, since otherwise `D union {y,t}` is K12. Put `r=|D intersect E|`. Any common vertex has old core degree at most13, while it sees all `19-r` vertices of `D union E`, so `r>=6`. If an exclusive pair `a in D-E`, `b in E-D` were nonadjacent, the r common vertices would contradict (CN), whose upper bound is at most4. Hence all exclusive cross-pairs are edges, so `D union E` is a clique. The core clique bound gives `r>=9`; distinctness gives `r=9`, so `D union E` is K11.

Then `(D union E) union {y,t}` is a 13-set with at least `55+10+10+1=76` edges, contradicting `D(13)=67`.

Therefore `d=10` final rise is impossible.

## 4. Distance d=3: exact three-family reduction

For `d=3`, (FR1) gives

`r_D=2+epsilon_D+q_out+e_SD<=3`.

Combining this with (FR2), `r_S<=3`, and nonnegative excess gives

`q_out=0`, `e_SD=0`, `r_S=3`, `epsilon'_S=0`.

Thus S is a K3 in the new core. The old support D is either a P3 with `epsilon_D=0`, or a K3 with total `epsilon_D=1`.

Since `q_out=0`, the ten vertices `B0=A\S` are all regular and form a target clique in the old shell. Together with p they form a K11 of degree-13 vertices.

Each `s in S` has old row weight exactly10. Hence the old missing shell is bipartite between S and B0.

For `b in B0`, regularity gives `t_b=d_M(b)`. A B-side degree1 is impossible from the strengthened row-union lemma. A B-side degree2 is also impossible: its two missing neighbours lie in S and have total weight20, and the exact repivot lower bound gives `q_b-q_p>=2`, contradicting the E406 ceiling31.

Therefore every B-side vertex has missing degree0 or3. If `n0` is the number of degree0 vertices, then

`M = K_{3,r} disjoint_union n0 K1`, `r=10-n0`,

and each S-vertex has decoration `n0`. Since `G_p<=8`, `n0 in {0,1,2}`.

Thus the only possible d3 final-rise shells are

`K_{3,10}`,
`K_{3,9} disjoint_union K1`,
`K_{3,8} disjoint_union 2K1`,

with S-side decorations `0,1,2`, respectively.

## 5. Distance d=2: exact star-platform theorem

Let `S={s1,s2}` and put

- `B=A\(S union {y})`, so `|B|=10`;
- `a=e_M(S) in {0,1}`;
- `J=M[B]`, `b=e(J)`;
- `G_B=sum_{v in B} g_v`.

Since `r_S=1-a`, (FR1)--(FR2) give the exact scalar identity

`b+G_B+e_SD+epsilon'_S+a = 8`.      (D2-1)

Equivalently, if `r_i` is the number of missing edges from `s_i` to B and `g_i` its decoration, then

`r_i+g_i = 10+e_R(s_i,D)+epsilon'_{s_i}`.      (D2-2)

The 14-point cap gives `z>=22`, but the decisive information comes from the missing edges inside J.

### 5.1 J is nonempty

If `b=0`, B is a target K10. Since p and y are target-adjacent and both are complete to B, `{p,y} union B` is a K12, impossible. Hence `b>=1`.

### 5.2 Summing the E406 edge inequality

For `v in B`, write

- `j_v=d_J(v)`;
- `r_v=|N_M(v) intersect S|`.

Then its old row weight is

`t_v=j_v+r_v+g_v`.

For every J-edge uv, the strengthened row-union lemma gives `t_u+t_v>=13`. Summing over all b edges,

`13b <= sum_v j_v t_v`
`= sum_v j_v^2 + sum_v j_v r_v + sum_v j_v g_v`.

The three terms satisfy

`sum_v j_v^2 = sum_{uv in E(J)}(j_u+j_v) <= b(b+1)`,

because for every edge uv the incident edges at u or v form a subset of the b edges, so `j_u+j_v<=b+1`;

`sum_v j_v r_v <= 2 sum_v j_v =4b`;

`sum_v j_v g_v <= b G_B`.

Therefore

`13b <= b(b+G_B+5)`.

Since b>0,

`b+G_B>=8`.

But (D2-1) gives `b+G_B<=8`. Hence every inequality is equality and

`b+G_B=8`,
`a=0`,
`e_SD=0`,
`epsilon'_S=0`.      (D2-EQ)

### 5.3 Equality forces a star

Equality in the quadratic-degree bound says that for every J-edge uv,

`j_u+j_v=b+1`.

Thus every edge meets every other edge. A simple graph with matching number1 is a star or a triangle. The triangle can occur only for b=3, but here `G_B=5>0`, while equality in `sum j_v g_v<=bG_B` forces every decorated B-vertex to have J-degree exactly b=3; a triangle has maximum degree2. Hence the triangle is impossible.

Therefore

`J = K_{1,b} disjoint_union (9-b)K1`, `1<=b<=8`.

Equality in the `r_v` term implies that every nonisolated vertex of J is missing to both s1 and s2.

Apply the same summed inequality in the q31 shell. The B-induced missing graph and the B-decoration vector are unchanged, so equality is forced again: every nonisolated B-vertex is also missing to both vertices of D.

If `b>=2`, the star has a unique centre c. Equality in the decoration term forces

`g_c=8-b`

and every star leaf and every J-isolate is regular. For b=1 the seven B-decoration units may split between the two endpoints of the single edge; this is the only exceptional decoration-support case.

Thus every d2 final rise is an exact star platform, not an arbitrary two-row state.

## 6. The d2 terminal b=8 is impossible

Assume b=8. Then `G_B=0`; the centre c and all eight leaves are regular. By (D2-EQ), every nonisolated B-vertex is missing to both S vertices and both D vertices.

For each star leaf l,

- its old missing degree is3: the centre plus s1,s2;
- `t_l=3`;
- `t_c=10`, while `t_{s1}=t_{s2}=11`.

The subset charge at the leaf is exact:

`t({c,s1,s2})-e_M({c,s1,s2}) = 10+11+11-2 =30`,

and the complementary charge is zero. Hence the repivot at l cannot drop below q30. It also cannot rise to q31: a d3 final rise would, by Section 4, force all three vertices of its small side `{c,s1,s2}` to have row weight10, but `s1,s2` have weight11. Therefore every star leaf is a q30 plateau pivot.

The centre c has missing degree10, and exactly the same subset computation gives complementary charge zero, so its repivot has q at least30. It cannot have q31 because Section 3 excludes every d10 final rise. Hence c is also q30.

Now look from the q31 pivot y. The centre c is again a regular adjacent pivot of missing degree10: in the q31 shell it is missing to the eight star leaves and the two vertices of D. Thus the edge `c--y`, oriented from the q30 pivot c to q31 pivot y, is a d10 final rise, contradicting Section 3.

Therefore

`b=8` is impossible.

The d2 frontier is reduced to the seven star platforms `1<=b<=7`.

## 7. Additional d2 row-class rigidity for b>=2

Let l be a star leaf. Section 6's first argument works for every `b>=2`: l is regular of old missing degree3, the subset `{c,s1,s2}` has charge30, and a q31 rise would require all three small-side row weights to be10, whereas the two S-weights are11. Hence every star leaf has q=30.

Since l and y are adjacent and y has q31, the oriented boundary `l -> y` is itself a d3 final rise. Applying Section 4 in the l-view gives:

- the old 3-row `D_l=N_C(l)` is a target triangle;
- y is target-anticomplete to `D_l`;
- for two star leaves l,l', their rows `D_l,D_l'` are either equal or disjoint;
- a row class has size at most3.

The last two statements follow because in the l-view every non-small-side vertex is either complete or anticomplete to the small 3-side. A B-isolate of J cannot be complete to `D_l`, since its old row has size at most2. Therefore the only isolates of the l-view d3 shell are other star leaves with the same row, and the row-class size is exactly one plus the common decoration of the three row vertices, hence at most3.

There is also a useful triangle-row equality. Let `E=N_C(c)` be the centre's 10-row and let `R_i=N_C(s_i)` be the two 11-rows. For every star leaf l and i=1,2, the shell triple `{c,l,s_i}` is missing-independent and its three row sizes sum to24. The inherited triangle row-union bound is at least24, so equality forces

`E`, `D_l`, `R_i`

to be pairwise disjoint. In addition D, E, R1, R2, and every D_l are pairwise disjoint whenever the corresponding shell adjacency above says the row vertex is absent.

Thus the remaining d2 problem for b=2,...,7 is a finite row-class compatibility problem over disjoint degree-12 triangles, not a shell-shape problem.

## 8. Distance d=11: dense-block reduction and equality-star subbranch

Let T be the unique shell vertex outside `S union {y}` and put

`h=g_T+e_SD`.

Then (FR1) gives

`r_D=46+epsilon_D+h`.

Let K be the complement of `C[D]` on the 11 vertices D and `m=e(K)=55-r_D`. Thus

`m=9-(epsilon_D+h)`.

For a K-edge uv with K-degrees `rho_u,rho_v`, the common C-neighbours of u,v inside D are at least `12-rho_u-rho_v`. Applying (CN) yields

`rho_u+rho_v+epsilon_u+epsilon_v>=9`.      (D11-1)

Summing (D11-1) over the m complement edges gives

`9m <= sum rho^2 + sum rho*epsilon`
`<= m(m+1)+m epsilon_D`.

Hence `m+epsilon_D>=8`. Since `m+epsilon_D=9-h`,

`h<=1`.

Therefore every d11 final-rise state has

`g_T+e_SD<=1`,
`2<=m<=9`.

If `h=1`, then `m+epsilon_D=8` and all inequalities in the summed argument are equalities. Exactly as in the d2 proof, K has matching number1. The triangle alternative is incompatible with positive excess support when m<8, and when m=8 the excess is zero; hence in all cases the h=1 branch has

`K = K_{1,m} disjoint_union (10-m)K1`,

with all old-core excess on the star centre when `m<8` and

`epsilon_D=8-m`.

Thus the h=1 d11 branch is itself an exact dense-block star platform. The h=0 branch remains one unit less rigid and is still open.

## 9. Distance d=12: paired dense 12-block reduction

Here `q_out=0`. Equation (FR1) becomes

`r_D=47+epsilon_D+e_SD`.

Because y is complete to D, the induced13-set `D union {y}` has `12+r_D` edges. The hereditary cap `D(13)=67` gives

`47<=r_D<=55`,

and hence

`epsilon_D+e_SD<=8`.

In the new core, the inserted 12-set S satisfies

`r_S=48+e_SD+epsilon'_S`.

Likewise `S union {p}` is an induced13-set, so `r_S<=55`; therefore

`e_SD+epsilon'_S<=7`.

Thus d12 reduces to two dense 12-vertex modules with edge ranges47--55 and48--55 and only tiny cross/excess slack.

## 10. Distance d=1: common-K11 reduction

Let `D={u}`, `S={s}`. Equations (FR1)--(FR2) give

`epsilon_C(u)-epsilon_{C'}(s)=1`,

so `epsilon_C(u)>=1`.

The exact q relation gives

`t_s = 11+epsilon_C(u)+1_{su}`.

Let `T=A\{s,y}`; `|T|=11`. The thirteen vertices `{p,y} union T` contain py, both p and y are complete to T, and T itself has `C(11,2)-e_M(T)` target edges. The cap `D(13)=67` gives

`e_M(T)>=11`.

More exactly,

`G_T+epsilon_C(u)+1_{su}<=8`.

There is also a neighbourhood-transfer constraint. Put `k=epsilon_C(u)`. In the common 46-vertex part of the two cores, every old degree-12 neighbour of u must also be adjacent to s, otherwise its new core degree would fall to11. If

`A_-=N_C(u)\N_R(s)`,
`A_+=N_R(s)\N_C(u)`

inside the common core, then

`|A_-|=|A_+|+1`,
`A_-` consists entirely of positive-excess old-core vertices,

and hence

`|A_-|<=6-k`, `|A_+|<=5-k`, `1<=k<=5`.

So a d1 final rise replaces two almost identical core neighbourhoods; its discrepancy is supported entirely on the tiny excess sets of the 285/284-edge cores.

## 11. Current final-rise frontier

The original six-distance frontier `{1,2,3,10,11,12}` is now:

- `d=10`: `PROVED EMPTY`;
- `d=2`: exact star platform `K1,b` with `1<=b<=7`; for `b>=2`, star-leaf 3-rows form equal/disjoint classes of size at most3 with the triangle-row disjointness above;
- `d=3`: exactly `K3,10`, `K3,9+K1`, `K3,8+2K1`;
- `d=11`: dense 11-block; the `g_T+e_SD=1` branch is an exact complement-star platform, while the zero-slack branch remains;
- `d=12`: paired dense-12 modules;
- `d=1`: common-K11 deficit block with neighbourhood discrepancy confined to core excess.

No claim that E406 is closed is made.