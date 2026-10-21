# Astra A prompt — T61 terminal front-end line

You are Astra A. You now own ONLY the **unique remaining front-end obstruction T61** for Erdős Problem 617, r=12.

Do **not** redo the 1752-node outer recurrence, do not attack E332 or E333–E340, and do not spend the main effort on generic S30 casework. The outer reduction is already certified.

## 0. Global target

The proved front-end theorem is now:

`hypothetical balanced K145 / least-edge colour G`

`=> induced F in R(4,49) OR embedded T61`.

Your sole objective is therefore

`T61 => contradiction OR T61 contains an induced F in R(4,49)`.

Closing this statement closes Line A.

## 1. Exact T61 contract

Work in the fixed least-edge target graph `G` under the temporary contextual assumption that `G` has no induced member of `R(4,49)`.

T61 means:

- `|G|=145`, `e(G)=m<=870`, `alpha(G)<=12`, hereditary D caps;
- a minimum-degree anchor `v` has `d_G(v)=11`;
- in `U=V(G)\N[v]`, an inclusion-maximal packing contains exactly six genuine target `K12` blocks `Q1,...,Q6`;
- the remaining induced residual `R` has 61 vertices;
- `alpha(R)<=5`, `omega(R)<=11`, all inherited D caps;
- `397<=E=e(R)<=408`;
- `delta(R) in {12,13}`;
- exact outer ledger

`E + sigma + z + g + x6 + y6 = 408`,

where `sigma=870-m`, `z=55-e(G[N(v)])`, `g=sum_{a in N(v)}(d_G(a)-11)`, `x6` is block-block target edges, and `y6` block-residual target edges.

The old assumptions `E=406`, `delta=13`, `z=0`, `e(F)=325`, or `Delta(F)<=14` are forbidden unless proved in the active branch.

## 2. New proved assets — use them, independently sanity-check them

The central line has supplied the following new analytic lemmas in `front_end/T61_NEW_LEMMAS.md`.

### A1. Exact residual independence

Under no extraction,

`alpha(R)=5`.

### A2. Anchor-defect elimination

`z=0` is now analytically proved.

Proof mechanism you should verify before using: if `ab` were a missing anchor edge, the endpoint cross-degree sum into `U` is at most `z+g+1<=12`; delete their residual neighbours, find an independent 5-set in the remaining >=49 residual vertices by contextual no-extraction, and apply six-part matching-transversal rigidity to the six K12 avoiding lists. Failure of a transversal would force `x6>=75`, whereas the outer ledger gives `x6<=11`. A transversal gives an independent 13-set. Hence no anchor missing edge exists.

Consequences:

- `N[v]` is a genuine target `K12`;
- there are now seven genuine disjoint K12 blocks in the whole graph (the anchor block plus the six blocks in U);
- the residual is still 61 vertices: this alone does NOT produce the eighth block;
- the ledger becomes

`E + sigma + g + x6 + y6 = 408`.

### A3. Modern R(4,48) floor

Using CORE211,

`C in R(4,48) => e(C)>=309`.

This strengthens the old certified seed 308. Do not overwrite the old certificate without re-running it; use 309 as a new downstream theorem.

### A4. h=12 T61 row contracts

If `delta(R)=12`, then

`E=78+q+e(C48)`, `q>=20`, `e(C48)>=309`,

so

`E in {407,408}`.

Exact cells:

- `E407 => (q,e(C48))=(20,309)`;
- `E408 => (20,310)` or `(21,309)`.

The old h12 E406 channel is dead.

### A5. Exact 309-edge 48-core equality classification

For `C48 in R(4,48)` with `e(C48)=309`, every degree-12 pivot yields

`q=20`, `e(H35)=211`.

For the 12-shell missing graph `M`:

`M = K_{2,r} disjoint_union (10-r)K1`, `6<=r<=10`.

Let its two centres have 10-vertex core rows `D1,D2`. Every leaf has a 2-vertex row `P`, every isolate has row size 0. Decorations are zero except at the two centres, where each decoration is `10-r`.

For every centre-leaf missing edge, centre row and leaf row are disjoint and have union size 12.

### A6. CORE211 row rigidity inside the q20 equality

For every leaf 2-row `P` and each centre row `Di`, the 12-set `Ui=Di union P` satisfies

`e_H(Ui) >= 64 + eps(Ui)`,

with `eps(Ui)<=1`, so `Ui` is missing at most `2-eps(Ui)` of its 66 possible edges.

The two centre rows satisfy

`|D1 intersect D2| >= 7`.

If an equality row captures positive core excess, the sharpened inequality often forces overlap at least 8.

The 211-core degree multiset is only

- `14,12^34`, or
- `13^2,12^33`.

## 3. Priority order

### Priority 1 — kill the h=12 branch completely

Start from the exact E407 double-equality tower:

`R61(E407,h12) -> outer q20 + C48(E309) -> inner q20 + H35(E211)`.

Exploit the `K_{2,r}` shell classification, the two nearly complete 10-rows, overlap >=7, the 2-row leaf geometry, and the R(2,23) near-extremal common-nonneighbour cores.

Try to prove one of:

- the two 10-rows must overlap so much that a forbidden target clique appears;
- repeated leaf rows force too much degree in the 211-core;
- the total core excess 2 cannot support all `Ui` near-clique equalities;
- the exact R(2,23) 131-edge / near-extremal classification forces incompatible row complements;
- a repivot/rotation produces a legal 49-set.

Then handle E408, first its `(q,eC)=(21,309)` subchannel using the same inner 309 classification, then `(20,310)`.

Do not stop after killing one r value; seek a uniform theorem for r=6..10.

### Priority 2 — h=13 low-edge regime

For `delta(R)=13`,

`E=91+q+e(C47)`, `q>=22`, `e(C47)>=284`.

Use total degree excess above 13:

`Xi = 2E - 61*13 = 2E-793`.

In particular:

- E397: Xi=1, degree multiset is `14,13^60`, and every degree-13 pivot is exact `(q,eC)=(22,284)`;
- E398: Xi=3, with many degree-13 pivots and only `(22,285)` / `(23,284)` cells;
- continue by small-excess stratification before invoking large S30 machinery.

Seek a **multi-pivot equality theorem**: many degree-13 pivots in the same 61-point graph must satisfy incompatible shell/core equality contracts.

### Priority 3 — only then use S31/S30

The audited S31 theorem is valid only when the SAME residual has

`E=406`, `delta=13`

(and the full inherited parent contract). It gives a degree-13 pivot with `q<=30`; it does not create a new block.

Do not map arbitrary T61 states into S30. Any T61->S30 interface must be proved explicitly.

## 4. High-value auxiliary tasks

1. Re-run the contextual recurrence with modern seeds `R(3,35)>=211` and `R(4,48)>=309`. Report whether any outer bound or stop changes. Preserve the old certificate; produce a new V2 certificate rather than mutating history.
2. Audit the exact R(2,23) 131-edge and 132–134 near-extremal classifications and apply them to the 23-point common-nonneighbour sets arising from A6.
3. Build a finite **analytic normal-form table**, not a graph brute-force search, for the h12 q20 equality families indexed by r=6..10 and the two CORE211 degree multisets.
4. If finite computation is necessary, produce a small independent verifier and a certificate whose semantics can be restated as a short mathematical lemma.

## 5. Forbidden shortcuts

- No generic claim `R(4,49)=empty`.
- No assumption that the eighth K12 exists.
- No claim that z=0 itself closes T61: it only creates a seventh genuine block total.
- No solver-only UNSAT.
- No promotion of scalar S30 cases to graph classifications.
- No use of historical CLOSED labels without exact hypotheses.
- No claiming EG617 solved unless the output actually proves T61 empty/extractable and states precisely what remains on the backend.

## 6. Required output

Return a package containing:

- `T61_MASTER_THEOREM.md`
- `T61_H12_CLOSURE.md`
- `T61_H13_STATE_TABLE.md`
- `R448_Q20_EQUALITY.md`
- `R223_INTERFACE.md`
- `T61_DEPENDENCY_DAG.md`
- `ASSUMPTION_LEDGER_V2.md`
- `RECURRENCE_V2_REPORT.md`
- verifier/certificates if used.

Each statement must have exactly one status:

`PROVED`, `COMPUTATION_CERTIFIED`, `CONDITIONAL`, `OPEN`, `RETRACTED`.

Your success criterion is: **close T61 entirely, or reduce it to one smaller mathematically explicit equality object than the current two-row terminal.** Do not stop after a cosmetic case reduction.