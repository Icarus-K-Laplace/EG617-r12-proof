# q28 / q29 repivot assets

## Status

- q28 profitable-repivot mechanism: `PROVED`.
- q29 good-repivot theorem: `PROVED`.

## Setup

For a degree-13 pivot `p` in a legitimate `F in R(4,49)`, let `A` be the 13-shell, `H` the 35-core, and `M = complement(F[A])`. For shell vertex `a`, write

`g_a = d_F(a)-13`, `t_a = d_M(a)+g_a`,

and

`q = e(M) + sum_a g_a`.

For every `S subset A`,

`q = t(S)-e_M(S)+e_M(A\S)+G_{A\S}`.

If `y in A` is undecorated (`g_y=0`), put

`d=d_M(y)`, `S=N_M(y)`, `D=N_H(y)`.

Then `d_F(y)=13`, so `y` is a legitimate new degree-13 pivot. The exact repivot identity is

`q_y-q = I_H(D)-C(d,2)-[t(S)-e_M(S)]+e_F(S,D)`.

Under `delta(H)>=12`, this yields

`q_y-q >= d(13-d)-[t(S)-e_M(S)]`.

## q29 good-repivot theorem

The theorem is intentionally stated independently of the numerical core edge count.

**Theorem.** Assume the q29 shell contract and `delta(H)>=12`. Then there exists an undecorated shell vertex `y` such that

`t(N_M(y))-e_M(N_M(y)) < d_M(y)(13-d_M(y))`.

Consequently

`d_F(y)=13` and `q_y>29` (hence `q_y>=30`).

The existence theorem does **not** assume `e(H)=211`.

The analytic proof splits the missing graph into three structural cases: it contains a `K4`; it is triangle-free; or it contains a triangle but no `K4`. In each case a profitable degree-13 repivot is forced.

## E331 corollary — separate statement

For `e(F)=331`, the global edge identity gives

`q_y = 331-91-e(H_y)`.

CORE211 implies `e(H_y)>=211`, hence every degree-13 pivot satisfies `q_y<=29`. This contradicts the q29 good-repivot theorem whenever a q29 pivot occurs.

Thus the number `211` belongs to the **E331 contradiction step**, not to the **q29 existence theorem**.

## Provenance rule

Future uses must keep these two statements separate:

1. `q=29 + delta(H)>=12 => exists degree-13 y with q_y>=30`;
2. fixed-edge-layer bounds such as `E331 => q_y<=29` use CORE211 separately.
