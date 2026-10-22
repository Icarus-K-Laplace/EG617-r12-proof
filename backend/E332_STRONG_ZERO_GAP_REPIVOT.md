# E332 strengthened zero-gap repivot theorem

Status: `PROVED`.

## Setup

Let `F in R(4,49)` have `e(F)=332`. Fix a degree-13 pivot `p`, its 13-shell `A=N_F(p)`, its 35-core `B=F-N_F[p]`, and missing graph `M=complement(F[A])`.

For `x in A`, write

- `g_x=d_F(x)-13`;
- `D_x=N_F(x) intersect B`;
- `t_x=|D_x|=d_M(x)+g_x`.

In the active E332 state we have `q=30`, `e(B)=211`, and every legal 35-core belongs to `R(3,35)` and has minimum degree at least 12.

## Theorem

Let `u in A` be undecorated, `g_u=0`, and let `v in N_M(u)`. Then repivot at `u` is legal and

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

In particular, if `v` is also undecorated, then

`N_M(u) union N_M(v)=A`

and

`D_u intersect D_v=empty`.

Thus every missing edge between two undecorated shell vertices is a zero-gap equality edge: its two missing-neighbourhoods cover the entire 13-shell, and its two core rows are disjoint.

## Proof

Because `g_u=0`,

`d_F(u)=13`,

so `u` is a legitimate new pivot. Put

`S=N_M(u)`, `D_u=N_F(u) intersect B`.

Since `|S|=|D_u|=d_M(u)`, the new 35-core is

`B_u=(B\D_u) union S`.

Fix `v in S`. Its neighbours in `B\D_u` are `D_v\D_u`. Its neighbours inside the inserted set `S` are precisely the target-neighbours of `v` inside `S`. Hence

`d_{B_u}(v)=|D_v\D_u| + |S|-1-|N_M(v) intersect S|`.

Using `|D_v|=d_M(v)+g_v` and expanding `d_M(v)` into the edge `uv`, neighbours inside `S`, and neighbours outside `S union {u}`, this becomes

`d_{B_u}(v)=|N_M(u) union N_M(v)| + g_v -1-|D_u intersect D_v|`.

The repivot core `B_u` is again in `R(3,35)`: an independent 4-set in `B_u` together with pivot `u` would be an independent 5-set in `F`, while the clique cap is inherited. Therefore the clean minimum-degree theorem gives

`d_{B_u}(v)>=12`.

Substitution yields

`|N_M(u) union N_M(v)| + g_v >= 13+|D_u intersect D_v|`.

If also `g_v=0`, the union is a subset of the 13-point shell, so its size is at most 13. Therefore equality is forced throughout:

`|N_M(u) union N_M(v)|=13`,

`|D_u intersect D_v|=0`.

This proves the theorem.

## Immediate consequences

1. Two undecorated low vertices cannot be adjacent in `M`.
2. If an undecorated degree-2 vertex `u` is adjacent to two undecorated high vertices `a,b`, then `N_M(u)={a,b}` and the zero-gap equality forces each of `a,b` to contain every shell vertex outside `{a,b}` in its missing neighbourhood.
3. The historical F-version bound `|N(u) union N(v)|+g_v>=12` is strictly strengthened here by the modern `delta>=12` core input.
