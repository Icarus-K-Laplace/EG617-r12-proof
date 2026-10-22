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

## 2. Strong zero-gap theorem

For a missing-shell edge uv with u undecorated,

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

In particular, two undecorated endpoints cover the full 13-shell with their missing neighbourhoods and have disjoint core rows.

This reduces the total decoration to `G>=4`, with only `G=4,5,6,7,8` possible.

## 3. Decoration layers G=4 and G=5

`E332_G4_G5_CLOSURE.md` proves both layers empty by exact support counting, strong zero-gap, and pair/triangle row coverage.

## 4. Decoration layer G=6

`E332_G6_FULL_CLOSURE.md` proves the full layer empty.

The key additional lemma is that every missing-shell triangle r,s,t satisfies

`|D_r union D_s union D_t|>=24`.

The exact two-high K4 support cell then gives three pairwise-disjoint 12-sets inside a 35-core, impossible, while the no-high and one-high branches are eliminated by active/inactive support accounting.

## 5. Decoration layer G=7

The no-high branch is eliminated in `E332_G7_H0_REDUCTION.md` (which now contains the full closure).

The exact two-high `H2-G7-K4minusE` cell is eliminated by `E332_H2_G7_K4MINUSE_CLOSURE.md`: low-row multiplicity plus a q30 plateau repivot forces new decoration at least9, contradicting the universal E332 ceiling `G<=8`.

The one-high branch is eliminated in `E332_G7_H1_FULL_CLOSURE.md` by exact classification of all zero-active and one-active `(k,r)` windows, using pair-row coverage, triangle-row coverage, and one final row-multiplicity overflow in the `(k,r)=(3,8)` cell.

Hence `G=7` is empty.

## 6. Decoration layer G=8

The one-high branch is reduced to the no-high branch in `E332_G8_H1_TO_H0_REDUCTION.md`: every one-high state is either immediately contradictory or admits a legal low repivot to a `G=8,h=0` state.

For the no-high branch:

- `E332_G8_H0_K3_K6_CLOSURE.md` eliminates support sizes `k=3,4,5,6`;
- `E332_G8_H0_FULL_CLOSURE.md` eliminates `k=7,8` using active/inactive edge accounting and the pair/triangle row inequalities.

Thus `G=8` is empty.

## Conclusion

Every possible E332 q30+211 survivor is eliminated. Therefore

`E332 = EMPTY`.

Consequently every legal residual `F in R(4,49)` satisfies either

- `e(F)<=331`, already impossible, or
- `333<=e(F)<=340`.

The remaining backend obligation is exactly the high-layer interval `E333..E340`.