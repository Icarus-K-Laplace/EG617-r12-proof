# Full closure of the legal R(4,49) layer E332

Status: `PROVED EMPTY`.

This file is the master dependency chain for `e(F)=332`.

Let `F in R(4,49)` with `e(F)=332`. Choose a degree-13 pivot. The exact shell/core identity is

`332 = 91 + q + e(H)`.

Using the universal core floor `e(H)>=211`, the q27/q28/q29 repivot machinery, and the E332 reduction in `E329_E332_CLOSURE.md`, every survivor must satisfy

`q=30`, `e(H)=211`.

The 211-core degree multiset is either

- `14,12^34`, or
- `13^2,12^33`.

The subsequent closure is analytic.

## 1. Eliminate medium undecorated degrees

The exact repivot inequality shows every undecorated shell vertex of missing degree4 through9 is profitable. The equality analysis then eliminates the full d10 branch and the full d3 branch.

Therefore every remaining undecorated missing degree lies in

`{0,1,2,11,12}`.

There are at most two undecorated degree11/12 vertices.

## 2. Strong zero-gap and row-cover tools

For a missing-shell edge uv with u undecorated,

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

In particular, two undecorated endpoints cover the full 13-shell with their missing neighbourhoods and have disjoint core rows.

Two additional row-cover facts are used repeatedly:

1. every missing-shell triangle r,s,t satisfies

   `|D_r union D_s union D_t|>=24`;

2. every missing-shell K4 has full core row cover:

   `union_{v in K4} D_v = V(H)`.

The second statement is immediate: a core vertex outside all four rows would be nonadjacent in F to four shell vertices that are pairwise nonadjacent in F, creating an independent 5-set.

The extreme-shell reduction gives `G>=4`, with only `G=4,5,6,7,8` possible.

## 3. Decoration layers G=4 and G=5

`E332_G4_G5_CLOSURE.md` proves both layers empty by exact support counting, strong zero-gap, and pair/triangle row coverage.

## 4. Decoration layer G=6

`E332_G6_FULL_CLOSURE.md` proves the full layer empty.

The exact two-high K4 support cell gives three pairwise-disjoint 12-sets inside a 35-core, impossible, while the no-high and one-high branches are eliminated by active/inactive support accounting.

## 5. Decoration layer G=7

The no-high branch is eliminated in `E332_G7_H0_REDUCTION.md`.

The exact two-high `H2-G7-K4minusE` cell is eliminated by `E332_H2_G7_K4MINUSE_CLOSURE.md`: low-row multiplicity plus a q30 plateau repivot forces new decoration at least9, contradicting the universal E332 ceiling `G<=8`.

For the one-high branch, the preferred proof is now the unified theorem `E332_H1_UNIFIED_FINAL.md`. Once the unique high is known to be universal and there is at most one low-active decoration x, write b for the number of inactive-inactive J-edges. Pair-row coverage and the active weight give

`b<=g_x`,

`b>=k+g_x-3`.

Hence `k<=3`, collapsing all finite windows to the single `(k,r)=(3,8)` cell. That cell is killed by the row-multiplicity repivot overflow.

Therefore the entire G=7 layer is empty.

The older file `E332_G7_H1_FULL_CLOSURE.md` is retained as a detailed cross-check, but the unified inequality proof is the preferred canonical route.

## 6. Decoration layer G=8

For the one-high branch, `E332_H1_UNIFIED_FINAL.md` gives

`b<=g_x-1`,

`b>=k+g_x-4`,

so again `k<=3`. The `(3,8)` cell fails pair coverage directly, and the unique `(3,7)` terminal either overflows the decoration ceiling immediately or repivots to a legitimate `G=8,h=0` shell.

Thus it remains only to eliminate `G=8,h=0`.

The preferred proof is the unified active/inactive theorem `E332_G8_H0_UNIFIED_CLOSURE.md`.

With active set A of size m, inactive graph edge count b, active-active edge count a, and active decoration sum g_A, the exact active row-weight identity is

`W_A=22+a-b+g_A>=11m`.

If `b>0`, pair-row coverage on an inactive edge gives

`b>=1+k-3m+g_A`.

Combining the two inequalities yields

`a>=k+8m-21`.

This kills every m>=3 and forces the m=2 branch to k<=6. The remaining m=0,1,2 equality geometries are then eliminated uniformly:

- m=0 forces k=8 and contradicts pair/triangle row coverage;
- m=1 forces k>=6 and contradicts triangle capacity or triangle-free edge degree-sums;
- m=2 leaves only k=4,5,6; k=5 and6 give 23-weight missing triangles, while k=4 reduces to a K4 equality geometry. The missing-K4 row-cover lemma then puts all pair-low core rows on a 12-set, and row multiplicity forces a repivot with new decoration at least9.

Therefore `G=8,h=0` is empty, and hence the entire G=8 layer is empty.

The older files `E332_G8_H0_K3_K6_CLOSURE.md`, `E332_G8_H0_FULL_CLOSURE.md`, and `E332_G8_H1_TO_H0_REDUCTION.md` remain as detailed provenance/cross-checks; the two unified files are the preferred final proof route.

## Conclusion

Every possible E332 q30+211 survivor is eliminated. Therefore

`E332 = EMPTY`.

Consequently every legal residual `F in R(4,49)` satisfies either

- `e(F)<=331`, already impossible, or
- `333<=e(F)<=340`.

The remaining backend obligation is exactly the high-layer interval `E333..E340`.