# Q32 130-edge nonexact color: minimum degree at least three

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL** under the registered 61-point residual bounds `alpha(D)<=12`, `omega(D)<=5`, and Kang–Pikhurko Theorem 1.

## Statement

Let D be a graph on the 61-point E408 residual with

- `e(D)=130`;
- `alpha(D)<=12`;
- `omega(D)<=5`.

Then

> **`delta(D)>=3`.**

## Anti-neighborhood bound

Suppose x has degree d in `{0,1,2}`. Let N be the set of D-nonneighbors of x, so `|N|=60-d`, hence `|N| in {60,59,58}`.

Because an independent 12-set in D[N], together with x, would be an independent 13-set in D, `alpha(D[N])<=11`. Also `omega(D[N])<=5`.

Let J be the complement of D[N]. Then J is K12-free. It is not 11-partite: otherwise an 11-partition of J would partition N into eleven D-cliques, each of size at most five, covering at most55 vertices, fewer than `|N|>=58`.

Kang–Pikhurko Theorem 1 applies for all three values `n=|N| in {58,59,60}`, because `n>=11+3` and `11<=(n-1)/2`. It gives

- `n=60`: `t_11(60)=1635`, `p_11(60)=1635-5+1=1631`, so `e(D[N])>=1770-1631=139`;
- `n=59`: `t_11(59)=1581`, `p_11(59)=1581-5+1=1577`, so `e(D[N])>=1711-1577=134`;
- `n=58`: `t_11(58)=1528`, `p_11(58)=1528-5+1=1524`, so `e(D[N])>=1653-1524=129`.

## Contradiction for each low degree

- If d=0, then `e(D)>=e(D[N])>=139>130`.
- If d=1, then `e(D)>=e(D[N])>=134>130`.
- If d=2, then D has the two distinct edges from x to its neighbors in addition to all edges in D[N], so `e(D)>=2+129=131>130`.

Every case contradicts `e(D)=130`. Therefore `delta(D)>=3`. QED.

## Role in the v44 m=8 closure

This file makes explicit the first step in the local dependency chain:

`Q32_130_MINDEG3.md`  
`=> Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md` (Kang–Pikhurko Theorems 1 and 4 at (57,11))  
`=> Q32_130_NO_CORE_ONLY_DEG4.md` (Kang–Pikhurko Theorem 1 at (56,11))  
`=> V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md`.

No exceptional-vertex injectivity or degree-nine claim is used.
