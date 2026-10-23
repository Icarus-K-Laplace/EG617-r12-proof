# q36 ceiling exchanges: compensated K4,9 normal form

Status: `PROVED` under the standard legal `R(4,49)` backend contract, the all-pivot 35-core minimum-degree12 theorem, and a lexicographically q-maximal top-channel pivot.

This theorem concerns only q36 ceiling pivots and regular shell exchanges of missing degree 4 or 9. It does not close E338 by itself.

## 1. Setup

Let `F` be a legal 49-point residual and let `p` be a degree-13 pivot with

- shell `A=N(p)`, |A|=13;
- 35-core `H`;
- `q=36`;
- `e(H)=211`, hence every core has minimum degree at least12.

Let `M` be the missing graph on A. Take a regular shell vertex `y` with

`d=|S|=d_M(y) in {4,9}`,

where `S=N_M(y)`, `T=A\(S union {y})`, and `D=N_H(y)`.

By `HIGH_RIGHT_EDGE_ATOMIC_DEFECT_THEOREM.md`, q36 maximality forces

`rho=h=kappa=b=0`.

In particular

- `e_M(T)=0`;
- `G_T=0`;
- H[D] is a clique;
- every vertex of D has H-degree12;
- `e_F(S,D)=0`.

## 2. Generic regular--missing-edge inequality

For any `s in S`, compare the old and y-repivot cores. Exactly as in the strengthened zero-gap calculation,

`d_(H_y)(s)=|N_M(y) union N_M(s)|+g_s-1-|D_y intersect D_s|`.

Since every legal repivot core has minimum degree at least12,

`|N_M(y) union N_M(s)|+g_s >= 13+|D_y intersect D_s|`.      (1)

Let `a_s` be the number of target neighbours of s in T. Because `N_M(y)=S`, the only vertices absent from `S union N_M(s)` are exactly those `a_s` target neighbours in T. Thus

`|N_M(y) union N_M(s)|=13-a_s`.

Substituting into (1),

`g_s >= a_s+|D_y intersect D_s| >= a_s`.                    (2)

## 3. Exact compensation

Put

`c=sum_(s in S) a_s = e_F(S,T)`,

and `m=e_M(S)`.

Because `e_M(T)=0` and y is missing exactly to S,

`e(M)=d+d(12-d)-c+m`.

For d=4 or9,

`d(13-d)=36`,

so

`e(M)=36-c+m`.                                               (3)

All decoration lies in S because y is regular and `G_T=0`. Hence, by (2),

`G=sum_(s in S)g_s >= c`.

But q=36 and (3) give

`36=e(M)+G=36-c+m+G`,

so

`G=c-m`.

Therefore equality is forced throughout:

- `m=0`;
- `G=c`;
- for every s in S, `g_s=a_s`;
- for every s in S, `D_y intersect D_s=empty`.

Thus S is a target clique, T union {y} is a target clique, and the shell missing graph is obtained from the complete bipartite graph between these two blocks by deleting exactly c cross missing edges. Those deleted missing edges are target edges, and their row counts are exactly the decorations on S.

Equivalently:

> every q36 d4/d9 zero-defect ceiling exchange is a compensated `K_(4,9)` shell.

## 4. All-or-nothing decoration on the S-side

Assume `G>0` and suppose some `s in S` were regular. Then `g_s=a_s=0`.

Since `e_M(S)=0`, the missing neighbourhood of s is exactly

`{y} union T`,

whose size is `13-d`, again either9 or4.

Thus s is itself a complementary d9/d4 regular ceiling exchange. The atomic-defect theorem at q36 forces its `rho_s=0`.

But the outside set for the s-exchange is `S\{s}`. Since `G>0` and s is regular, at least one vertex of `S\{s}` is decorated. Therefore

`rho_s >= G_(S\{s}) >0`,

contradiction.

Hence:

> if G>0, every vertex of S is decorated.

Consequently

- in the d=4 orientation, all four vertices on the 4-side are decorated;
- in the d=9 orientation, all nine vertices on the 9-side are decorated.

The case G=0 is the exact `K_(4,9)` plateau already closed by `K49_G2_SPLIT_FULL_CLOSURE.md` (its earlier G=0 subcase).

## 5. D14 bound

The induced 14-set `{p} union A` has

`13 + (78-e(M)) = 91-e(M)`

target edges. Since `e(M)=36-G`, this is

`55+G`.

The inherited cap `D(14)=69` therefore gives

`G<=14`.                                                     (4)

Thus the only compensated survivors left by this theorem satisfy

- d4: `4<=G<=14`, with all four 4-side vertices decorated;
- d9: `9<=G<=14`, with all nine 9-side vertices decorated.

## Boundary

No edge layer is closed here. The d9 family is eliminated separately in `Q36_D9_COMPENSATED_CLOSURE.md`; the d4 family is reduced further in `Q36_D4_COMPENSATED_DYNAMICS.md`.