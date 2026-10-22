# E406 d11 terminal: center-shielding reduction

Status: `PROVED` under `E406_D11_THREE_STAR_BLOCKS.md`. `E406` remains `OPEN`.

Let the three 11-point star-defect blocks be `S,D,E`. Write their complement-star centers as `s0,d0,e0`, and their star leaves as `s_i,d_j,e_k`.

Known inputs:

- `e(S,D)=0`;
- `e(S,E)<=1`;
- `|D intersect E|<=1`;
- every internal nonedge of each block is exactly `center--leaf`;
- the parent has `alpha<=5`.

## 1. Six-vertex rectangle condition

For every choice of leaves `s_i,d_j,e_k`, the six vertices

`{s0,s_i,d0,d_j,e0,e_k}`

cannot be independent.

Inside each block, its center--leaf pair is a target nonedge. Every S--D cross pair is also a target nonedge. Therefore at least one target edge must occur either

- between `{s0,s_i}` and `{e0,e_k}`, or
- between `{d0,d_j}` and `{e0,e_k}`.

Equivalently, for each fixed E-leaf `e_k`, either the S--E edges hit every S-star missing pair, or the D--E edges hit every D-star missing pair.

## 2. The unique S--E edge

Since `e(S,E)<=1`, a single S--E edge hits every S-star missing pair for every E-leaf if and only if it is the center-center edge

`s0 e0`.

Indeed:

- `s0 e0` lies in every pair `{s0,s_i} x {e0,e_k}`;
- `s0 e_k` only shields the single E-leaf k;
- `s_i e0` only shields the single S-leaf i;
- `s_i e_k` shields only one cell.

Thus, unless the unique S--E edge is `s0e0`, the D--E cross graph must hit every D-star missing pair for all E-leaves except possibly one.

If `e(S,E)=0`, it must do so for every E-leaf.

## 3. Capacity consequence on D--E

Assume `d0e0` is absent. Fix an E-leaf `e_k` for which D--E must hit every D-star missing pair.

If `d0e_k` is present, the whole D-star family is hit.

Otherwise, for every D-leaf `d_j`, at least one of

`d_j e0`, `d_j e_k`

must be an edge.

Let

`x = |N(e0) intersect L_D|`,

where `L_D` is the D-star leaf set. The E-leaf `e_k` has internal E-degree9 and old-core degree12, hence at most3 neighbours outside E. Therefore

`m_D - x <= 3`,

so

`x >= m_D-3`.      (CS)

Consequently, if `x < m_D-3`, then every E-leaf requiring D-side shielding must satisfy

`d0e_k in E(R)`.

## 4. Structural trichotomy

Every surviving d11 terminal therefore satisfies at least one of the following shielding patterns:

1. **S-center shield:** the unique S--E edge is `s0e0`;
2. **D-center shield:** `d0e0` is a D--E edge;
3. **one-center-dominates-leaves:** either
   - `e0` is adjacent to at least `m_D-3` D-leaves, or
   - `d0` is adjacent to every E-leaf that is not the at-most-one leaf shielded by the exceptional S--E edge.

This is not yet a contradiction, but it removes arbitrary D--E cross geometry. The remaining d11 problem is a finite center-shield compatibility problem coupled to the exact external-degree capacities of the three star blocks.