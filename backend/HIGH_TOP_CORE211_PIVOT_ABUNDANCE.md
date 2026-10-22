# High backend top-q CORE211 legal-pivot abundance

Status: `PROVED`.

This theorem is independent of the current Astra-B E333 repeated-support assignment. It targets the top-charge channels of E338--E340.

## Setup

Let F be a legal 49-point residual with minimum degree13. Take a degree-13 pivot p with 13-shell A and 35-core H. Write

`e(F)=91+q+e(H)`

and shell decoration total

`G=sum_{a in A}(d_F(a)-13)`.

Assume p is in a top-charge CORE211 channel:

`e(H)=211`.

Then the 211-core degree multiset is either

- Type I: `(14,12^34)`;
- Type II: `(13^2,12^33)`.

The shell-core incidence total is

`R=sum_A t_a = 2e(M)+G = 2q-G`.

A shell vertex is an adjacent legal pivot exactly when its decoration is zero. Hence the number A0 of adjacent legal pivots satisfies

`A0 >= max(0,13-G)`.

## Core legal pivots

For a core vertex v, let r_v be its number of target neighbours in the shell A.

If `d_H(v)=12`, global minimum degree13 gives `r_v>=1`, and v is itself a legal degree-13 pivot exactly when `r_v=1`.

### Type I

There are34 degree-12 core vertices. If h of them have `r_v>=2`, then these34 vertices alone consume at least `34+h` shell incidences. Therefore the number N0 of degree-12 core legal pivots satisfies

`N0 >= max(0,68-R)=max(0,G+68-2q)`.

These are nonadjacent one-spoke legal pivots: each has exactly one target neighbour in A.

### Type II

There are33 degree-12 core vertices. The same argument gives

`N0 >= max(0,66-R)=max(0,G+66-2q)`.

The two internal degree-13 core vertices may create additional zero-spoke legal pivots when their shell incidence is zero; they are not needed for the lower bound.

## Uniform top-q consequences

The total number L of other legal degree-13 pivots is at least `A0+N0`.

For q=36:

- Type I: `L>=9`;
- Type II: `L>=7`.

Hence uniformly `L>=7`.

For q=37:

- Type I: `L>=7`;
- Type II: `L>=5`.

Hence uniformly `L>=5`.

For q=38:

- Type I: `L>=5`;
- Type II: `L>=3`.

Hence uniformly `L>=3`.

Therefore

- an E338 pivot in the top channel `(q,e(H))=(36,211)` has at least7 other legal pivots;
- an E339 pivot in `(37,211)` has at least5;
- an E340 pivot in `(38,211)` has at least3.

## Structural dichotomy

The bounds are stronger than a mere pivot count. If the shell carries large decoration and therefore has few adjacent legal pivots, the deficit is automatically converted into nonadjacent one-spoke legal pivots in the 211-core. Thus every top-q plateau has either many adjacent exchanges or many nonadjacent one-spoke exchanges.

This is intended to feed the exact nonadjacent-pivot identities from the high-layer package. It closes no E338--E340 layer by itself.
