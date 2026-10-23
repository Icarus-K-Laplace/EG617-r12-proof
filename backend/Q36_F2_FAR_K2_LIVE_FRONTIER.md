# q36 f=2 far-target-K2 live frontier

Status: `LIVE REDUCTION MAP`. This records proved far-K2 results only; it does not close the full q36 layer.

## 1. Global d2 reduction

`Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md` proves:

- any d2 row forces `a_F=0` and has a pure target-K2 support of globally regular core vertices;
- for `c>=3`, at most one d2 row exists;
- d3 rows use at most two decorated missing-set classes;
- if two d3 classes occur with a d2 row, their total allowance is at most2;
- with no d2 row the known sharper two-class allowance sum is at most1.

## 2. c=8 with exactly one d2 row is fully CLOSED

`Q36_F2_FAR_K2_C8_D2_REDUCTION.md` reduces the seven d3 owners to one missing-set class with

`A in {2,3,4}`.

The three allowance layers are all empty:

- `Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md` closes A=2;
- the corrected A=3 chain closes A=3, while the obsolete fixed-remainder file remains RETRACTED;
- the A=4 chain closes multiplicity>=3, all multiplicity-two internal types, and finally the all-singleton sector in `Q36_F2_FAR_K2_C8_D2_A4_ALL_SINGLETON_FULL_CLOSURE.md`.

`Q36_F2_FAR_K2_C8_ONE_D2_FULL_CLOSURE.md` aggregates these results.

Therefore

> `q36 f=2`, far-target-K2, `c=8`, exactly one d2 row is EMPTY.

## 3. c=8 no-d2: only one d3 missing-set class survives

`Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION.md` proves:

- two active d3 missing-set classes are impossible by the exact shell-decoration ledger;
- all eight owners therefore belong to one common missing-set class;
- its allowance satisfies `A<=4`;
- if the two inactive decorated shell vertices are a missing pair then `A<=3`.

The same file closes

- A=0;
- A=1.

## 4. c=8 no-d2 allowance two is fully CLOSED

`Q36_F2_FAR_K2_C8_NO_D2_A2_FULL_CLOSURE.md` proves A=2 is empty.

Main steps:

- repeated one-edge/two-edge/K3 supports are all eliminated;
- a hypothetical repeated-K3 owner partition would force three pairwise-disjoint low-weight K3 blocks and then at least 52 units of common-S weight on the remaining 26 core vertices, contradicting the global weight budget;
- hence all eight supports are singleton triples;
- their intersection components must be common-hub sunflowers of size at most3;
- at most three components exist, forcing the unique partition `3+3+2`;
- every nontrivial component then collapses to zero-weight one-edge triples, and the three components yield a core independent4.

Therefore

> `q36 f=2`, far-target-K2, `c=8`, no-d2, A=2 is EMPTY.

## 5. Current c=8 no-d2 frontier

Only

> `A=3` and `A=4`

remain.

Both are single-common-missing-set eight-owner systems. No pure-d2 support or fixed 11/12-point remainder is available, so proofs in those branches must use only the no-d2 contract.

## 6. Current far-K2 tasks

Highest priority:

1. close `c=8`, no-d2, A=3;
2. close `c=8`, no-d2, A=4;
3. once c=8 is empty, parameterize downward to `c<=7`.

The far-K2 topology remains independent of the concurrent far-2K1 work and of the Astra A/B frontiers.