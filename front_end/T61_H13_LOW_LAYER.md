# T61 minimum-degree-13 low-edge layers

Status: E397, E398, E399 and E400 are `PROVED` empty; E401..E408 remain `OPEN`.

## Setup

After closure of the h12 branch, every T61 survivor has `delta(R)=13`. For any degree-13 pivot p with 13-shell and 47-core C,

`E = 91 + q_p + e(C)`, with `q_p>=22`, `e(C)>=284`.

Let `Xi(E)=2E-61*13=2E-793` be total degree excess above13. For a degree13 pivot p, let

`G_p=sum_{a in N(p)}(d_R(a)-13)`.

Because the 14-point cap gives `z_p>=22`, writing `E=397+s` gives

`G_p<=s`.

Thus every degree13 vertex sees at most s units of neighbour excess.

## E397 — CLOSED

`Xi=1`, degree multiset `14,13^60`. Every low pivot has q22,z22,G0, so the unique high vertex cannot have a low neighbour, impossible.

## E398 — CLOSED

`Xi=3`, degree multiset `14^3,13^58`. Any low-high edge gives exact `(q,z,G,eC)=(23,22,1,284)`. The q23 shell classification forces an independent11-set in the shell missing graph, contradicting `alpha(M)<=10`.

## E399 — CLOSED

`Xi=5`. Exact q24 shell theorems eliminate `(24,22,2)` and `(24,23,1)`, which removes every positive-excess partition.

## E400 — CLOSED

`Xi=7`, `s=3`. The uniform theorem in `E400_Q25_SHELL.md` eliminates every exact q25 cell with shell decoration sum `G=1,2,3`:

- `(q,z,G)=(25,24,1)`;
- `(25,23,2)`;
- `(25,22,3)`.

Together with the already closed q23/q24 cells, this shows that a degree13 vertex cannot be adjacent to any positive-excess vertex in E400. Since total excess7 gives at most seven positive-excess vertices, no vertex of degree at least14 can obtain all its neighbours inside the positive-excess set. Contradiction.

Thus E400 is empty.

## Current front-end window

`T61: delta=13, 401<=E<=408`.

For E401:

- `s=4`;
- total excess `Xi=9`;
- every degree13 pivot sees at most4 units of neighbour excess;
- the next genuinely new shell level is q26.

Priority: prove a q26 shell theorem for the cells `(q,z,G)=(26,25,1),(26,24,2),(26,23,3),(26,22,4)`, while checking whether the q25 theorem extends to G=4.
