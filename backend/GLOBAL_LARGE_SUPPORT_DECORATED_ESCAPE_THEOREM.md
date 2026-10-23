# Global Large-Support Decorated-Escape Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`;
- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- common-S owner-clique theorem;
- exact shell identity `q=e(M)+G_A`;
- the inherited shell floor `e(M)>=22` in the legal r=12 49-point backend;
- the already-proved q36--q38 K4,9 plateau closure for the final maximal-owner corollary.

Purpose: reorganize the large-support q36--q38 analysis around one structural dichotomy. The former K4,9 family appears naturally as the unique maximal-owner fully-decorated escape geometry rather than as an isolated shell case.

## 1. General high-right setup

Let p be a maximum-q pivot in the r=12 49-point backend.

Let Y be a common-S owner family with support/missing size

`d in {4,9}`.

Assume

`q<=38`.

For a common-S row the base exchange term is

`d(13-d)=36`

for both d=4 and d=9.

The common row allowance is

`a=q-36-B`,

with `B>=0`.

Therefore

> `a<=2`.                                                     (L1)

For d in {4,9},

> `a<=2<d-1`.                                                (L2)

Thus every such family lies strictly below the first overlap threshold.

Let

`s=|S intersect X|`

be the number of globally decorated vertices in the common missing set.

## 2. Non-fully-decorated regime

Assume

`s<d`.                                                       (L3)

Then `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md` applies.

Hence:

1. plateau owner rows are singleton support classes and there are at most3 of them;
2. every strict-loss support is disjoint from every distinct support class;
3. two distinct strict supports have at most
   `a-1<=1`
   target cross-edge.

Thus the strict layer is a family of pairwise-disjoint d-blocks with cross allowance at most1.

## 3. At most three distinct strict support classes

Suppose four distinct strict support classes existed.

Choose one point uniformly from each block. Since each block pair has at most one target cross-edge, the expected number of target edges in the four-point transversal is at most

`6/d^2`.

For `d>=4`,

`6/d^2<=6/16<1`.                                             (L4)

But every four-point transversal lies in H with `alpha(H)<=3`, so it must contain at least one target edge.

Contradiction.

Therefore:

> **number of distinct strict support classes <=3.**          (L5)

Combining with plateau capacity:

> **every non-fully-decorated d4/d9 common-S family has at most six distinct support classes.**   (L6)

All owner multiplicity beyond these six classes is therefore repeated-support multiplicity and is subject to the global repivot/hereditary packing theorem.

## 4. The only escape from the subcritical decomposition

The proof above uses only the condition `s<d` beyond the general q ceiling.

Therefore the only way a d4/d9 common-S family can avoid the bounded-plateau / isolated-block structure is

> **fully-decorated missing set:** `s=d`.                     (L7)

This is the canonical decorated-escape regime.

It is not an arbitrary shell case: every point of S consumes at least one unit of shell decoration.

The inherited shell floor gives

`G_A=q-e(M)<=38-22=16`.                                      (L8)

Hence a fully-decorated d-support already consumes at least d of at most16 decoration units.

In particular:

- d=9 consumes at least9 units;
- d=4 consumes at least4 units.

## 5. Owner-count geometry in the escape regime

Common-S owners are disjoint from S inside the 13-shell. Therefore

> `N=|Y|<=13-d`.                                             (L9)

The maximal owner counts are

- d=4: `N<=9`;
- d=9: `N<=4`.

Suppose equality holds in (L9), so

`N=13-d`.

Then the shell has no leftover vertices:

`A=S disjoint_union Y`.

Every owner misses every point of S and is target-adjacent to every other owner. Hence the shell missing graph consists exactly of all Y--S edges plus possible edges internal to S.

If the fully-decorated escape is at the zero-extra-missing plateau in which S itself has no additional missing edge, the shell missing graph is exactly

> `K_(d,13-d)`.                                               (L10)

For d=4 or9 this is the same bipartite graph

> **`K_(4,9)`.**                                              (L11)

Thus K4,9 is the unique maximal-owner fully-decorated large-support escape geometry.

## 6. Relation to the already-killed K4,9 plateau

The q36--q38 backend work independently proved that, at a lexicographically maximal top-channel CORE211 pivot, the relevant K4,9 plateau family with the allowed decoration budget is impossible.

The present theorem explains its conceptual role:

> it is not a separate exceptional shell topology;
> it is the maximal-owner equality state left after the general subcritical support theorem has removed every non-fully-decorated large-support family.

Therefore the old K4,9 closure should appear in the final paper as an equality-case exclusion of the global decorated-escape theorem.

## 7. d=10 low-q analogue

The same logic applies to d=10 rows at q<=33.

The base term is

`10*(13-10)=30`.

Hence

`a<=3<d-1=9`.                                                (L12)

If `s<10`, the subcritical decomposition applies.

Strict supports have pairwise cross allowance at most2. Four disjoint 10-blocks would have transversal expected target-edge count at most

`6*2/100=0.12<1`,

contradicting `alpha(H)<=3`.

So again there are at most three distinct strict supports.

If `s=10`, the missing set is fully decorated and owner count is automatically

`N<=3`.                                                       (L13)

Thus d10 also fits the same bounded-block / fully-decorated escape dichotomy.

## 8. Unified large-support statement

For the large-support regimes relevant to the high backend:

> **Large-Support Decorated-Escape Theorem.**
>
> Whenever the q ceiling places a common-S d-support family below the first overlap threshold (`a<=d-1`), exactly one of the following occurs:
>
> 1. `s<d`: the family consists of at most three singleton plateau supports plus at most three distinct pairwise-disjoint low-cross strict support classes;
> 2. `s=d`: the entire missing set is globally decorated and the owner count is bounded by the shell complement size `13-d`.
>
> At d=4/9 with maximal owner count, Alternative2 produces the K4,9 equality geometry.   (L14)

This replaces much of the large-support case split by one structural theorem.

## 9. Remaining large-support bridge

After (L14), the only genuinely new large-support problem is no longer arbitrary q36/q37/q38 shell classification.

It is:

> classify **non-maximal fully-decorated escape states** (`s=d`, `N<13-d`) and show that their decoration budget/core support packing either creates an improving repivot or embeds into one of the already-killed maximal equality geometries.

This is the unique large-support bridge left by the theorem.

## 10. Generalization

The proof uses symbolically:

- shell size h;
- support size d;
- q ceiling through the allowance a;
- core independence number3;
- shell decoration budget;
- common-S owner count `N<=h-d`.

The same decorated-escape dichotomy applies to higher-r reductions whenever the support system lies below its first overlap threshold.