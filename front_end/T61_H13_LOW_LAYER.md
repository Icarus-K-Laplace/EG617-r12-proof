# T61 minimum-degree-13 low-edge layers

Status: E397 and E398 are `PROVED` empty; E399..E408 remain `OPEN`.

## Setup

After closure of the h12 branch, every T61 survivor has

`delta(R)=13`.

For any degree-13 pivot p with 13-shell and 47-core C,

`E = 91 + q_p + e(C)`.

The shell floor is `q_p>=22`; the audited 47-core floor is `e(C)>=284`.

Let

`Xi(E)=2E-61*13=2E-793`

be total degree excess above13. For a degree13 pivot let

`G_p=sum_{a in N(p)}(d_R(a)-13)`.

The 14-point cap gives at least22 missing shell edges, so `q_p=z_p+G_p` with `z_p>=22`. Therefore, writing `E=397+s`,

`G_p<=s`.

Thus every degree13 vertex sees at most s units of neighbour excess.

## E397 — CLOSED

Here `Xi=1`, so the degree multiset is `14,13^60`.

Every degree13 pivot has q22 and a 284-edge core; hence z22 and G0. Thus no degree13 vertex can be adjacent to the unique degree14 vertex, impossible because that degree14 vertex needs14 neighbours.

Therefore E397 is empty.

## E398 — CLOSED

Here `Xi=3`. The neighbour-excess bound with s=1 first forces every positive-excess vertex to have excess1, hence degree multiset

`14^3,13^58`.

Any degree14 vertex has at least12 degree13 neighbours. Choose such a low neighbour p. Then the pivot data are forced:

`q=23`, `z=22`, `G=1`, `e(C47)=284`.

The exact q23 shell classification is proved in `E398_Q23_SHELL.md`: the shell missing graph M is forced to

`(K_{2,11}+centre edge)-one cross edge`,

with degree multiset `12,11,2^10,1`.

Its 11 non-centre vertices are independent in M, so `alpha(M)>=11`. But because the pivot p is adjacent to every shell vertex and `omega(R)<=11`, the shell complement must satisfy `alpha(M)<=10`; otherwise an independent11-set in M is a target K11 inside the shell and p completes a forbidden target K12.

Contradiction. Therefore E398 is empty.

Hence the current T61 window is

`399<=E<=408`, `delta=13`.

## General local excess bound — PROVED

For `E=397+s`, every degree13 pivot satisfies

`G_p<=s`.

Consequently a vertex of excess greater than s cannot be adjacent to any degree13 vertex. This is the main tool for E399+.

## E399 first reduction — PROVED

For E399, `s=2` and total excess is

`Xi=5`.

No vertex can have excess>=3: such a vertex cannot be adjacent to any degree13 vertex, while the entire positive-excess set has at most five vertices, far too few to supply degree at least16.

Thus positive excesses are only 1 or2. The only possible global degree-excess partitions are

- `2+2+1`  -> degree multiset `15^2,14,13^58`;
- `2+1+1+1` -> `15,14^3,13^57`;
- `1+1+1+1+1` -> `14^5,13^56`.

For a degree13 pivot adjacent to a degree15 vertex, its neighbour excess already equals2, so

`G=2`, `q=24`, `z=22`, `e(C47)=284`.

This exact q24 / single-decoration-2 cell is the preferred next target. If it is impossible, the first two partitions disappear and E399 reduces to the five-degree14 case.

For a degree13 pivot adjacent to two degree14 vertices, the same exact cell occurs with `G=2` distributed as `1+1`.

The next active task is therefore an exact q24 shell classification with z22 and total decoration2, split into the single-g2 and double-g1 channels.
