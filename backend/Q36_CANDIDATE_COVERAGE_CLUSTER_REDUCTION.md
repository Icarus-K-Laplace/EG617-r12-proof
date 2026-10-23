# q36 candidate coverage — regular-shell cluster reduction

Status: `PROVED REDUCTION` under the standard legal backend contract, CORE211 q36 top channel, and the q36 d4/d9 closures.

This is the first candidate-coverage theorem after `Q36_D4_COMPENSATED_CLOSURE.md` and `Q36_D9_COMPENSATED_CLOSURE.md`.

## 1. Setup

Let p be a q36 top-channel degree-13 pivot. Let

- A=N(p), |A|=13;
- R be the regular shell vertices, `g=0`;
- X=A\R be the decorated shell vertices;
- `n=|R|`, `r=|X|=13-n`.

Since q=36,

`e(M)=36-G`,

where `G=sum_(x in X)g_x>=r`.

The q36 d4/d9 closures and the atomic-defect theorem imply that every regular shell vertex has missing degree in

`{0,1,2,3,10,11,12}`.                                  (1)

## 2. Regular target graph is a cluster graph

For regular shell vertices u,v with uv a target nonedge, the all-pivot minimum-degree12 theorem gives the zero-gap relation

`N_M(u) union N_M(v)=A`,

`D_u intersect D_v=empty`.                                (2)

Suppose regular vertices u,v,w satisfy uv and vw target edges but uw a target nonedge. Then v is absent from both `N_M(u)` and `N_M(w)`, contradicting the first equality in (2).

Therefore target adjacency on R is transitive. Hence

> F[R] is a disjoint union of target cliques.

Call the clique parts `C_1,...,C_k`, with sizes `c_i`.

Choosing one vertex from each part gives an independent set in F, so `alpha(F)<=4` implies

`k<=4`.                                                     (3)

## 3. A decorated vertex sees at most one regular part

Let x in X. If x had target neighbours u in C_i and v in C_j with i!=j, then uv is a target nonedge. But x belongs to neither missing neighbourhood, contradicting

`N_M(u) union N_M(v)=A`.

Thus

> every decorated shell vertex has regular target-neighbours in at most one clique part C_i.       (4)

This assignment property is global and will be used repeatedly below.

## 4. At most one low-distance regular part

For u in a part C_i of size c_i, let t_u be the number of decorated target neighbours of u. Because u is regular,

`d_M(u)=13-c_i-t_u`.                                       (5)

Call u low if `d_M(u)<=3`, and high if `d_M(u)>=10`.

If C_i contains a low vertex u, then by (5)

`t_u>=10-c_i`.

Hence at least `10-c_i` decorated vertices are assigned to C_i by (4).

If two distinct parts C_i,C_j both contained low vertices, their required assigned decorator sets are disjoint, so

`r>=20-c_i-c_j`.

But

`r=13-sum c_l <=13-c_i-c_j`,

which would give `20<=13`, impossible.

Therefore

> all low regular vertices lie in one clique part C.        (6)

Every other regular part is high and consequently has size at most3: a part of size at least4 cannot satisfy `13-c_i-t_u>=10`.

## 5. If a low part exists, at most three regular vertices lie outside it

Let C be the unique low part and put

`f=|R\C|`.

Every u in C is missing-adjacent to all f regular vertices outside C. Since u is low,

`f<=d_M(u)<=3`.

Thus

> a q36 shell with a low regular vertex has the form
>
> `one low target clique C + at most three far/high regular vertices`.     (7)

The far vertices themselves split into clique parts of sizes at most3.

## 6. If no low part exists, there are at most two adjacent regular pivots

Assume every regular shell vertex is high. Then every regular clique part has size at most3.

For a part of size c_i, equation (5) and `d_M>=10` imply

`t_u<=3-c_i`

for every u in that part. Hence the total number of target R--X incidences is at most

`sum_i c_i(3-c_i)`.

The missing edges among regular vertices number

`m_RR=(n^2-sum_i c_i^2)/2`.

Therefore, ignoring the nonnegative missing-edge contribution inside X,

`e(M)>=m_RR + nr - sum_i c_i(3-c_i)`

`=(20n-n^2+sum_i c_i^2)/2`.                               (8)

On the other hand, `G>=r=13-n` gives

`e(M)=36-G<=36-r=23+n`.                                   (9)

For `n>=3`, since `sum_i c_i^2>=n`, the right side of (8) exceeds `23+n`:

`(20n-n^2+sum c_i^2)-2(23+n)`
`>=19n-n^2-46>0`

for every `3<=n<=12`.

This contradicts (9).

Hence

> if every adjacent regular pivot is high-distance, then `n<=2`.          (10)

## 7. Coverage consequence using CORE211 pivot abundance

`HIGH_TOP_CORE211_PIVOT_ABUNDANCE.md` gives at least seven other legal degree-13 pivots at a q36 CORE211 pivot.

Therefore every remaining q36 candidate falls into one of two structural regimes:

### Regime A — low-clique shell

There is one target clique C containing every low-distance adjacent regular pivot and at most three far/high regular shell vertices outside C.

### Regime B — shell-poor / core-rich

There are at most two adjacent regular pivots. Hence at least five of the seven guaranteed legal pivots are nonadjacent degree-13 one-spoke pivots in the 211-core.

This is the new exact candidate-coverage frontier after d4/d9 elimination.

## Boundary

This theorem does not yet close q36. The next steps are:

1. eliminate the f=3 outer layer in Regime A (partly done in `Q36_F3_FAR_LAYER_REDUCTION.md`);
2. derive and exploit the exact q-formula for the at least-five nonadjacent one-spoke pivots in Regime B.