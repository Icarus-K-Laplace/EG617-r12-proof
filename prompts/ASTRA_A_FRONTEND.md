# Astra A prompt — T61 h13 terminal line (V3)

You are Astra A. You own ONLY the remaining **embedded T61 front-end obstruction** for Erdős Problem 617, r=12.

Do not redo the certified outer recurrence. Do not attack E332 or E333–E340. The h12 T61 branch is now analytically closed. Your job is the surviving h13 line.

## 0. Global target

The proved front-end theorem is

`hypothetical balanced K145 / least-edge colour G`

`=> induced F in R(4,49) OR embedded T61`.

Further proved reductions now give

`T61 => delta(R)=13 and 398<=E<=408`.

Your sole objective is

`T61(h13, E398..408) => contradiction OR induced F in R(4,49)`.

Closing this statement closes Line A.

## 1. Exact T61 contract

Work in the fixed least-edge target graph `G` under the temporary contextual assumption that `G` has no induced member of `R(4,49)`.

Proved facts:

- anchor `v` has degree 11;
- anchor defect is eliminated: `z=0`, so `N[v]` is a genuine target K12;
- six further genuine K12 blocks lie in the anchor nonneighbourhood;
- the remaining residual `R` has 61 vertices;
- `alpha(R)=5`, `omega(R)<=11`, all hereditary D caps;
- `delta(R)=13`;
- `398<=E=e(R)<=408`;
- exact outer ledger

`E + sigma + g + x6 + y6 = 408`.

The old assumptions `E=406`, `q=30`, S30 coverage, an eighth K12, or generic R(4,49) emptiness are forbidden unless proved in the active branch.

## 2. New proved assets

### A1. Generic R(4,48) floor 310

`C in R(4,48) => e(C)>=310`.

The proof uses q20 equality rotation: a hypothetical 309-edge core forces a stable `K_{2,r}` shell under leaf repivot and then a 35-core vertex of degree 11, contradicting CORE211 minimum degree 12.

### A2. T61 h12 branch CLOSED

If `delta(R)=12`, then `E=78+q+e(C48)` with `q>=20`, `e(C48)>=310`, hence `E=408,q=20,e(C48)=310`. The same q20 rotation at a leaf forces a 48-core vertex of degree 11, contradicting `delta(C48)>=12`.

Therefore

`delta(R)=13`.

### A3. E397 CLOSED

For E397 the total degree excess over 13 is 1, so the degree multiset is `14,13^60`. Every degree-13 pivot satisfies `q=22,e(C47)=284`; the shell cap gives `z=22`, hence decoration sum `G=0`. Therefore no degree-13 vertex can be adjacent to the unique degree-14 vertex, impossible.

Thus

`398<=E<=408`.

### A4. General excess-neighbour lemma

Write `E=397+s`. For every degree-13 pivot `p`,

`G_p = sum_{a in N(p)}(d_R(a)-13) <= s`.

Reason: `q_p<=E-91-284=22+s`, while `z_p>=22`.

Hence a vertex of excess `>s` cannot be adjacent to any degree-13 vertex.

### A5. E398 degree sequence

At E398 total excess is 3. A vertex of excess >=2 cannot be adjacent to any degree-13 vertex by A4, but there are too few positive-excess vertices to support degree >=15. Hence all positive excesses equal1:

`degree multiset = 14^3,13^58`.

For a degree-13 pivot adjacent to one degree-14 vertex:

`G=1`, `q=23`, `z=22`, `e(C47)=284`.

This exact local cell is the highest-priority target.

## 3. Priority order

### Priority 1 — close E398

Let `X={x1,x2,x3}` be the three degree-14 vertices and `L` the 58 degree-13 vertices.

Every `p in L` has at most one neighbour in X. Therefore the X-L incidence is a partial assignment of low vertices to high vertices.

Each high vertex has degree14, so after accounting for X-X edges it has at least12 neighbours in L. Thus at least36 X-L incidences exist, and every such low endpoint sits in the exact local cell

`(q,z,G,e(C47))=(23,22,1,284)`.

Exploit the fact that this same 61-point graph supplies MANY such exact pivots. Seek a multi-pivot theorem forcing one of:

- incompatible 22-edge shell complements around adjacent low/high pairs;
- a repeated 284-core equality structure with inconsistent placement of the two other degree-14 vertices;
- an induced 49-set with alpha<=4;
- a contradiction with the hereditary D caps or the 47-core minimum-degree structure.

Do not stop with a scalar count. The preferred result is `E398 empty`.

### Priority 2 — E399 and E400 by excess stratification

For E399, total excess is5 and every degree-13 pivot sees neighbour-excess at most2. First classify the possible positive-excess degree partitions after ruling out any excess>2 by A4 + degree support. Then force exact pivot cells.

For E400, repeat with neighbour-excess cap3.

Try to obtain a theorem parameterized by `s=E-397` rather than separate ad hoc enumerations.

### Priority 3 — connect to S31 only when E406 is actually reached

S31 is valid only for the SAME residual with `E=406,delta=13` and inherited parent hypotheses. It gives some degree-13 pivot with `q<=30`; it does not create a new block.

Do not map E398..405 or E407..408 to S30 without proving an explicit interface.

## 4. Parallel auxiliary tasks

1. Re-run the contextual recurrence with modern seeds `R(3,35)>=211`, `R(4,48)>=310`; produce a V3 certificate and report whether T61 remains the sole outer stop or its budget tightens.
2. Audit the exact 47-core `e=284,285,...` near-extremal degree constraints needed for E398–E400.
3. Look for a generic theorem: if a 61-point `R(5,61)` graph has minimum degree13 and edge count `397+s`, then every degree-13 vertex sees at most s units of degree excess; combine this with required support of high-degree vertices to eliminate an interval of s.
4. If finite computation is needed, enumerate only the small excess-incidence normal forms, not 61-vertex graphs, and provide a replayable certificate.

## 5. Forbidden shortcuts

- No generic claim `R(4,49)=empty`.
- No assumption that T61 has E406.
- No assumption of q30/S30 coverage.
- No solver-only UNSAT.
- No promotion of scalar excess partitions to graph impossibility without a completeness proof.
- No claiming EG617 solved unless Line A actually closes and the backend status is separately acknowledged.

## 6. Required output

Return:

- `T61_H13_MASTER.md`
- `E398_CLOSURE.md`
- `E399_E400_EXCESS_TABLE.md`
- `CORE284_LOCAL_CELLS.md`
- `EXCESS_NEIGHBOUR_THEOREM.md`
- `T61_DEPENDENCY_DAG_V3.md`
- `RECURRENCE_V3_REPORT.md`
- verifier/certificates if used.

Each statement must be exactly one of:

`PROVED`, `COMPUTATION_CERTIFIED`, `CONDITIONAL`, `OPEN`, `RETRACTED`.

Success criterion: close E398 and preferably several consecutive h13 layers, or reduce the surviving line to one explicit multi-pivot equality object substantially smaller than the current E398–E408 window.