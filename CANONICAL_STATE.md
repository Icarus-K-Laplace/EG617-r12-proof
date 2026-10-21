# Canonical state — 2026-10-21

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For a legitimate residual `F in R(4,49)`, current clean machinery uses a degree-13 pivot with

`e(F)=91+q+e(H)`, `H in R(3,35)`.

Clean core floor:

`e(H)>=211`.

Reusable repivot assets:

- q28 profitable repivot;
- q29 + inherited `delta(H)>=12` gives a new degree-13 pivot `q_y>=30`, without requiring `e(H)=211`.

Current lower backend frontier:

`E332 -> (q,e(H))=(30,211)`.

At `e(H)=211` the only degree multisets are `14,12^34` and `13^2,12^33`.

Line C attacks E332. Line B attacks E333–E340.

## Front-end outer theorem

The modern target is not an exact E325 residual. The proved front-end dichotomy is:

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

The contextual recurrence V1 is COMPUTATION_CERTIFIED:

- 1752 recurrence nodes;
- 144 outer stopping comparisons;
- two independent integer implementations;
- unique outer stop `(d,j,a,n)=(11,6,5,61)`.

## Tightened T61

Original T61 data:

- degree-11 anchor;
- six genuine K12 blocks in its nonneighbourhood;
- residual R of order61;
- `397<=E=e(R)<=408`;
- `delta(R) in {12,13}`;
- inherited caps and `omega(R)<=11`;
- exact ledger `E+sigma+z+g+x6+y6=408`.

New proved deductions:

1. Under contextual no extraction, `alpha(R)=5` exactly.
2. The anchor defect vanishes: `z=0`.
3. Hence `N[v]` is itself a genuine K12; there are now seven genuine disjoint target K12 blocks total. This still leaves the same 61-point residual and does not by itself produce an eighth block.
4. The outer ledger simplifies to

   `E+sigma+g+x6+y6=408`.
5. Modern CORE211 strengthens the generic R(4,48) floor to 309.
6. Therefore the T61 minimum-degree-12 row begins at E407, not E406.

Exact h12 cells now:

- E407: `(q,e(C48))=(20,309)`;
- E408: `(20,310)` or `(21,309)`.

## 309-edge 48-core equality

A 309-edge `C48 in R(4,48)` necessarily has a degree-12 pivot with

`q=20`, `e(H35)=211`.

Its 12-shell missing graph is exactly

`K_{2,r} + (10-r) isolates`, `6<=r<=10`.

The two centres have core-row size10 and decoration `10-r`; leaves have row size2 and zero decoration; isolates have row size0.

Inside the 211-core:

- every centre 10-row plus leaf 2-row is an almost-K12 (at least `64+eps` edges);
- each such 12-set captures at most one unit of the total two core-excess units;
- the two centre rows overlap in at least seven core vertices.

This is the active h12 equality geometry for Astra A.

## Remaining Line A problem

The broad outer recurrence is no longer the issue. The exact task is:

`T61 -> contradiction OR induced legitimate R(4,49)`.

Priority:

1. finish the h12 E407/E408 equality geometry;
2. attack the h13 low-excess layers E397–E405 before overusing S31/S30;
3. use S31 only at the verified E406/delta13 interface;
4. prove any T61->S30 coverage theorem explicitly.

## S30 status

For the specified row-labelled `(5,7,8,8)` branch:

- k2 singleton-triangle branch closed;
- saturation lemmas remove many k0/k1 scalar cases;
- exact remaining necessary scalar cases: 14 for k0 and 13 for k1.

They are not complete graph survivors and do not establish T61 coverage.

## Three-line split

- Line A / Astra A: tightened T61.
- Line B / Astra B: E333–E340.
- Line C: E332 q30+211.

## Certification warning

The full EG617 r=12 theorem remains OPEN. It can be certified only when the T61 bridge and all legitimate R(4,49) backend layers are closed.
