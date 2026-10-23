# K4,9 G=2 split residual — full closure

Status: `PROVED` under the top-channel CORE211 / lexicographically maximal-pivot contract used by the preceding K4,9 reductions.

This closes the final residual left by

- `K49_PLATEAU_INDEPENDENT_REDUCTION.md`;
- `K49_G2_SPLIT_CORE_REDUCTION.md`;
- `K49_G2_SPLIT_ROW_OVERLAP.md`;
- `K49_G2_SPLIT_TWO_SUPPORT_B0.md`;
- `K49_G2_SPLIT_SINGLETON_SUPPORT_CLOSURE.md`.

It closes the K4,9 plateau family itself, not the whole E340 layer.

## 1. Canonical final residual

The previous reductions prove that any surviving split-decoration K4,9 plateau has:

- old pivot `p`;
- shell missing graph `M=K_(4,9)` with four-side X and nine-side Y;
- total decoration `G=2`, split `1+1` on two four-side vertices;
- exactly two distinct disjoint 4-point core supports `R,S subset L` used by the nine Y-rows;
- both supports repeated;
- support multiplicities `a,b>=2` with `a+b=9`;
- each repeated support is a pure target K4.

The last point follows from q-maximality. For a repeated d=4 support T, all four inserted support vertices are globally decorated, so a q38 plateau exchange would increase the lexicographic secondary potential. Hence its repivot charge is at most37. The exact q38 d=4 defect formula gives

`kappa(T)+m(T)+c_T <=1`,

where `m(T)=6-e_H(T)` and `c_T` is its decorated four-side incidence count.

The two supports together must carry the two non-W decorated-row incidences, so each has `c_T=1`. Therefore

`kappa(T)=m(T)=0`,

and both `H[R]` and `H[S]` are K4.

Equivalently, after the singleton branch has been eliminated, the only multiplicity partitions were

`2+7`, `3+6`, `4+5`.

## 2. A 14-point density contradiction

Let `Y_R` be the subset of Y whose core row is R, and put `a=|Y_R|`. Exchange R and S if necessary so that

`a>=ceil(9/2)=5`.

Consider the 14-point induced set

`T={p} union Y union R`.

Its target edges are counted exactly as follows.

1. `p` is adjacent to every vertex of Y because Y lies in the shell of p:

   `e(p,Y)=9`.

2. Y is a target K9 because the old missing shell is K4,9:

   `e(Y)=C(9,2)=36`.

3. R is a target K4:

   `e(R)=6`.

4. A vertex `y in Y_R` has core row exactly R, so it is adjacent to all four vertices of R. A vertex in the other Y-group has core row S, disjoint from R, hence has no target neighbour in R. Therefore

   `e(Y,R)=4a`.

There are no p--R target edges because R lies in the old core.

Hence

`e(T)=9+36+6+4a=51+4a`.

Since `a>=5`,

`e(T)>=71`.

But the inherited 14-point cap is

`D(14)=69`.

Contradiction.

Therefore no split-decoration G=2 K4,9 plateau exists.

## 3. Full K4,9 plateau conclusion

The earlier independent K4,9 reduction already excluded

- `G=0`;
- `G=1`;
- `G=2` concentrated on one four-side vertex.

The only surviving case was G=2 split as `1+1`, and Sections 1--2 eliminate it.

Thus:

> At a lexicographically maximal top-channel pivot with q in {36,37,38}, no missing shell `K_(4,9)` with all decoration on the four-side and total decoration `G in {0,1,2}` can survive as a plateau state.

In particular the formerly unique q38 split residual is empty.

## Boundary

This theorem removes the complete K4,9 plateau family from the E338--E340 right-edge program. It does **not** assert that every q36--q38 survivor has missing shell K4,9, so E338, E339 and E340 remain OPEN.