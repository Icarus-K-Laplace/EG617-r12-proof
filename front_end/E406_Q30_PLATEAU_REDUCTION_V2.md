# E406 q30 plateau reduction V2

Status: `PROVED` for the reductions stated here. The global q30-escape theorem is not yet claimed.

This continues `E406_Q30_GENERIC_EXTREME_REDUCTION.md` under the same explicit E406 contract and the contradiction hypothesis that q=30 is globally maximal among degree-13 pivots.

## 1. Two-high classification is generic

Let h=2 with high regular vertices a,b. The common-low counting from the generic reduction gives a regular low u adjacent in M to both a and b. Since d_M(u)=2 and t_a,t_b are 11 or12, the d=2 repivot satisfies q_u>=28; q27 and q28 are independently impossible, hence q_u>=29. Its new core has at most286 edges and therefore minimum degree at least12.

The exact repivot-core degree formula now yields the same zero-gap conclusion used in the E332 proof:

- a and b are missing-adjacent to every low and every decorated vertex;
- every low has missing neighbourhood exactly {a,b};
- there are no low-decorated missing edges.

With epsilon=1_{ab in E(M)} and J=M[D], exact shell edge counting gives

`e(J)=8-G-epsilon`.

For x in D,

`t_x=2+d_J(x)+g_x`.

If epsilon=0, every J-edge with a high gives a missing triangle, so `t_x+t_y>=13`; if epsilon=1, E406 PAIR-13 gives the same lower bound `t_x+t_y>=13` (stronger than the E332 pair bound).

The finite shell calculation therefore strengthens the E332 classification:

- G=6: epsilon=0 is impossible; epsilon=1 forces k=2 and the exact support `H2-G6-K4`;
- G=7: epsilon=1 gives e(J)=0 and an independent 11-set; epsilon=0 forces k=2 and the exact support `H2-G7-K4minusE`;
- G=8: impossible.

Thus the only two-high q30 plateau cells are

1. `H2-G6-K4`;
2. `H2-G7-K4minusE`.

## 2. G6, h=1, high degree12 is empty

Let a be the unique high regular vertex and assume d_M(a)=12. The high is universal in M. Every low has the compulsory missing edge to a and at most one additional decorated neighbour. Put r=e_M(L,D), J=M[D]. Exact counting gives

`r+e(J)=12`.

For a decorated vertex active on a low edge, PAIR-13 gives row weight at least11. The case split by k=|D| in the shell proof of `backend/E332_G6_FULL_CLOSURE.md`, Section5, uses only:

- this active-weight bound;
- positive decoration total G=6;
- pair-row coverage;
- low independence;
- exact edge count `r+e(J)=12`.

No 211-core degree multiset or 35-point capacity is used. Replaying those inequalities gives no survivor for k=3,4,5,6. Hence

`G=6,h=1,d_M(a)=12` is empty.

The remaining G6 one-high branch is therefore only high degree11.

## 3. G7, h=0 is empty

For G=7,h=0, let D be the decorated set, k=|D|, L the regular-low set, s=e_M(L,D), and J=M[D]. Then

`e(J)=23-s`,
`t(D)=53-s`.

Every active decorated vertex has weight at least11 by PAIR-13. A degree1 low forces its unique decorated neighbour to have weight at least12. A degree2 low with decorated neighbours x,y satisfies the no-rise inequality

`t_x+t_y-e_J(xy)>=22`.

Every J-triangle has row weight at least24. These are exactly the inputs of `backend/E332_G7_H0_REDUCTION.md`; its k=3,...,7 elimination is shell-level and does not use the 211-core degree multiset or 35-core capacity. Therefore

`G=7,h=0` is empty.

## 4. Universal-high input for G7/G8 one-high states

Assume h=1 and d_M(a)=12. If a low u has neighbourhood {a,x} with x decorated and t_x=11, then its d=2 repivot has q_u>=30. Since q=30 is maximal, q_u=30; the new 285-edge core has minimum degree at least12. Applying the exact repivot-core degree formula to the edge ux then forces

`t_x>=12`,

a contradiction. Thus every low-active decoration in the universal-high branch has weight at least12.

Consequently the active/inactive counting in `backend/E332_G7_G8_H1_UNIFORM_REDUCTION.md` remains valid for the universal-high E406 branch:

- there are at most one low-active decorated vertex after the two-active contradiction;
- if r>0, then k+r<=11;
- G=7 one-active states have r>=4;
- G=8 one-active states have r>=3.

The E332 terminal row-multiplicity closures are not imported wholesale; they require separate E406 verification because the core has47 rather than35 vertices.

## 5. Current q30 plateau frontier

Combining the generic reduction and the present note, a q30 global maximum with no d3/d10 root can survive only in:

- G=6, h=1 with high missing-degree11;
- exact `H2-G6-K4`;
- G=7, h=1;
- exact `H2-G7-K4minusE`;
- G=8, h=0 or1.

There is no G4 or G5 state, no G6/h0 state, no G6 one-high universal state, no G7/h0 state, and no G8/h2 state.

The next task is to replace the E332-specific 35-core terminal contradictions by the E406 47-core invariants `e(C)=285`, `delta(C)>=12`, total core excess6, and at most six core vertices with no shell incidence.
