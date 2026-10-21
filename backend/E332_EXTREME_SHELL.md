# E332 extreme-degree shell reduction

Status: `PROVED` for the reductions below. This is the active Line C object after the complete d3/d10 closures.

## Setup

Assume the E332 q30+211 state. The d3 and d10 branches are already proved empty, while undecorated degrees4..9 are profitable. Hence every undecorated shell vertex has missing degree only

`0,1,2,11,12`.

Write

- `G=sum g`, so `0<=G<=8`;
- `z=e(M)=30-G`, so `22<=z<=30`;
- H = set of undecorated high vertices of missing degree11 or12;
- L = set of undecorated low vertices of missing degree0,1,2;
- D = decorated vertices.

Let `h=|H|`, `k=|D|`, `l=|L|`; then `h+k+l=13` and `k<=G`.

Pair-row coverage on every missing edge implies two low undecorated vertices cannot be adjacent in M, since their row-weight sum is at most4<12. Thus L is independent in M.

---

## 1. At most two undecorated high vertices — PROVED

### No triangle of high vertices

Suppose three high regular vertices form an M-triangle T. Their weights are at least11 each, so `t(T)>=33`.

The exact subset identity gives

`30 = t(T)-3 + e(M[A\T]) + G_{A\T}`.

Therefore equality is forced:

- every vertex of T has weight exactly11;
- `M[A\T]` has no edges;
- every vertex outside T is undecorated.

No further high vertex can lie outside T. The ten outside vertices are therefore low regular, each of degree at most2.

But each triangle vertex has missing degree11, with two neighbours inside T, so it sends nine missing edges outside. Hence the outside degree sum is27, while ten low vertices can contribute at most20. Contradiction.

Thus the high-regular induced graph is triangle-free.

### h>=5 impossible

A degree11/12 shell vertex has at most one non-neighbour in the entire 12-vertex remainder of the shell. Hence inside H every high vertex has degree at least `h-2`.

For h>=5 this minimum degree is incompatible with triangle-freeness (already for h=5, Mantel gives average degree at most 2.4 while the minimum degree would be at least3). Hence `h<=4`.

### h=4 impossible

Triangle-freeness and minimum degree2 force the high-induced graph to be C4. Every high vertex then has exactly two high neighbours and must be adjacent in M to all nine outside vertices in order to reach missing degree11; degree12 is impossible.

Consequently every outside vertex has missing degree at least4. Since undecorated degrees3..10 are all excluded, all nine outside vertices would have to be decorated. This requires `G>=9`, contradicting `G<=8`.

### h=3 impossible

The high-induced graph cannot have only one edge, because an isolated high vertex could have at most ten outside neighbours and would fail to reach missing degree11. Thus the triangle-free high-induced graph is a path P3.

The two endpoints must have degree11 and be adjacent to all ten outside vertices. The middle high vertex has two high neighbours and therefore at least nine outside neighbours. Hence

`z >= 2 + 10 + 10 + 9 =31`,

contradicting `z<=30`.

Therefore

`h<=2`.

---

## 2. Decoration budget satisfies G>=4 — PROVED

Since L is independent and each low vertex has missing degree at most2, all edges of M lie either inside `R=H union D` or between L and R.

Put `r=|R|=h+k`. Then

`z <= 2(13-r) + C(r,2)`.

Also `r<=h+G<=G+2`.

The shell condition `alpha(M)<=10` implies `r>=3`.

For `G=0,1,2,3`, the maximal possible right side at `r=G+2` is respectively too small for `z=30-G`:

- G=0: r<=2 contradicts alpha(M)<=10;
- G=1: `z<=23<29`;
- G=2: `z<=24<28`;
- G=3: `z<=26<27`.

Hence

`G>=4`.

So the only remaining decoration totals are

`G in {4,5,6,7,8}`.

---

## 3. The G=4 layer has exact support counts — PROVED

For G=4 we have `z=26`, `r<=6`.

The edge upper bound above forces `r>=5`.

If `r=5`, the bound is attained exactly:

- all eight low vertices have missing degree2;
- R induces K5.

The total shell row-weight is `sum t=60-G=56`. The low vertices contribute16, so `t(R)=40`.

For every `v in R`, the four-set `R\{v}` is an M-K4. K4 row coverage forces weight at least35, while the subset identity with q30 forces weight at most36. Thus

`35 <= 40-t_v <=36`,

so `4<=t_v<=5` for every v in R. Summing gives `t(R)<=25`, contradiction.

Therefore `r=6`.

Since `h<=2` and `k<=G=4`, equality is forced:

`h=2, k=4, l=7`.

Thus any surviving G=4 shell has exactly

- two undecorated degree11/12 vertices;
- four decorated vertices carrying total decoration4, hence each decoration1;
- seven undecorated low vertices of degree0,1,2.

This is the first exact cell of the remaining extreme-degree problem.

## Current Line C target

After the d3/d10 closures and the reductions above, E332 can only survive in an extreme shell with

- `G in {4,5,6,7,8}`;
- at most two undecorated degree11/12 vertices;
- every other undecorated vertex of degree0,1,2;
- for G=4 specifically, exact support counts `(h,k,l)=(2,4,7)`.

The next attack should eliminate G=4 using the dense six-vertex support and low-to-high edge weights, then continue G=5..8 or derive a uniform support theorem.
