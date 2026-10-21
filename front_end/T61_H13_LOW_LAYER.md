# T61 minimum-degree-13 low-edge layers

Status: mixed; the E397 layer is `PROVED` empty, higher layers remain `OPEN`.

## Setup

After closure of the h12 branch, every T61 survivor has

`delta(R)=13`, `397<=E<=408`.

For any degree-13 pivot `p`, with 13-shell and 47-core `C`,

`E = 91 + q_p + e(C)`.

The shell floor is `q_p>=22`; the audited 47-core floor is `e(C)>=284`.

Let the total degree excess above 13 be

`Xi(E)=2E-61*13=2E-793`.

For a degree-13 pivot, shell decoration sum is

`G_p=sum_{a in N(p)}(d_R(a)-13)`.

Because the 14-point cap forces at least 22 missing shell edges,

`q_p=z_p+G_p`, `z_p>=22`.

Thus

`G_p <= q_p-22 <= E-397`.

This gives a useful general local excess bound:

> Every degree-13 vertex sees total neighbour excess at most `E-397`.

## E397 closure — PROVED

Assume `E=397`. Then

`Xi=1`,

so the degree multiset is necessarily

`14,13^60`.

For every degree-13 pivot `p`,

`397 = 91 + q_p + e(C_p)`

with `q_p>=22`, `e(C_p)>=284`. Therefore equality holds:

`q_p=22`, `e(C_p)=284`.

Since `z_p>=22` and `q_p=z_p+G_p`, we also have

`z_p=22`, `G_p=0`.

Hence every neighbour of every degree-13 vertex has degree exactly 13.

But the unique degree-14 vertex must have 14 neighbours, all among the other 60 vertices, which all have degree 13. Any such incident edge would make that degree-14 vertex a positive-excess neighbour of a degree-13 pivot, contradicting `G_p=0`.

Therefore no E397 T61 residual exists.

So the h13 edge window improves to

`398<=E<=408`.

## General excess-neighbour corollary — PROVED

Write `E=397+s`, `s>=0`. Then every degree-13 vertex `p` satisfies

`sum_{a in N(p)}(d_R(a)-13) <= s`.

In particular, a vertex of excess strictly larger than `s` cannot be adjacent to any degree-13 vertex.

This immediately implies for E398 (`s=1`) that every positive-excess vertex must have excess exactly 1: a vertex of excess at least 2 would have to take all of its neighbours among positive-excess vertices, but the total global excess is only 3 and hence there are at most two other positive-excess vertices, far fewer than its degree at least 15.

Therefore any E398 survivor has exact degree multiset

`14^3,13^58`.

This degree-sequence reduction is `PROVED`; elimination of E398 remains `OPEN`.

For an E398 degree-13 pivot:

- if it has no degree-14 neighbour, then `G_p=0` and `q_p` is 22 or 23;
- if it has one degree-14 neighbour, then `G_p=1`, so `q_p>=23`; because `q_p<=23`, necessarily `q_p=23`, `z_p=22`, and the 47-core has exactly 284 edges.

Thus every cross edge from a degree-14 vertex to a degree-13 vertex places the low endpoint into an exact `(q,z,e(C))=(23,22,284)` local cell.

This is the active next target for the h13 line.
