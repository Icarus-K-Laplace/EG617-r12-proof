# T61 minimum-degree-13 low-edge layers

Status: E397, E398 and E399 are `PROVED` empty; E400..E408 remain `OPEN`.

## Setup

After closure of the h12 branch, every T61 survivor has `delta(R)=13`. For any degree-13 pivot p with 13-shell and 47-core C,

`E = 91 + q_p + e(C)`, with `q_p>=22`, `e(C)>=284`.

Let `Xi(E)=2E-61*13=2E-793` be the total degree excess above13. For a degree13 pivot p, let

`G_p=sum_{a in N(p)}(d_R(a)-13)`.

Because the 14-point cap gives `z_p>=22`, writing `E=397+s` gives the reusable bound

`G_p<=s`.

Thus every degree13 vertex sees at most s units of neighbour excess.

## E397 — CLOSED

`Xi=1`, hence degree multiset `14,13^60`. Every degree13 pivot has q22, z22 and G0, so no degree13 vertex can meet the unique degree14 vertex, impossible.

## E398 — CLOSED

`Xi=3`. The neighbour-excess bound forces degree multiset `14^3,13^58`. Any low-high edge creates the exact local cell

`q=23, z=22, G=1, e(C47)=284`.

`E398_Q23_SHELL.md` classifies its shell missing graph as

`(K_{2,11}+centre edge)-one cross edge`,

whose 11 non-centre vertices are independent in M. This contradicts `alpha(M)<=10`. Hence E398 is empty.

## E399 — CLOSED

`Xi=5`, `s=2`. No excess >=3 vertex is possible, so the only excess partitions are

- `2+2+1`;
- `2+1+1+1`;
- `1+1+1+1+1`.

The exact q24 shell analysis in `E399_Q24_SHELL.md` proves both cells impossible:

- `(q,z,G)=(24,22,2)`;
- `(q,z,G)=(24,23,1)`.

Therefore any degree15 vertex is impossible, and in the all-degree14 partition no degree13 vertex can be adjacent to one or two degree14 vertices. Since a degree14 vertex cannot obtain fourteen neighbours only from the other four positive-excess vertices, the all-degree14 partition is impossible as well.

Thus E399 is empty.

## Current front-end window

`T61: delta=13, 400<=E<=408`.

The next low layer is E400, where

- `s=3`;
- total excess `Xi=7`;
- every degree13 pivot sees at most3 units of neighbour excess.

Priority: classify the exact q25 cells forced by low vertices adjacent to total neighbour excess3, and reuse the q23/q24 shell methods before invoking S31/S30.
