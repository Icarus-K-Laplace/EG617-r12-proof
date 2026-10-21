# Astra A prompt — T61 h13 terminal line (V4)

You are Astra A. You own ONLY the remaining embedded T61 front-end obstruction for Erdős Problem 617, r=12.

Do not redo the certified outer recurrence. Do not attack backend E332 or E333–E340. The h12 branch and the first three h13 edge layers are now analytically closed.

## 0. Global target

The proved front-end theorem is

`hypothetical balanced K145 / least-edge colour G`

`=> induced F in R(4,49) OR embedded T61`.

Current clean reduction:

`T61 => delta(R)=13 and 400<=E<=408`.

Your sole objective is

`T61(h13, E400..408) => contradiction OR induced F in R(4,49)`.

Closing this closes Line A.

## 1. Exact T61 contract

Work in the fixed least-edge target graph G under the temporary contextual assumption that G has no induced member of R(4,49).

Proved facts:

- anchor v has degree11;
- anchor defect z=0, so N[v] is a genuine target K12;
- six additional genuine K12 blocks lie in the anchor nonneighbourhood;
- residual R has61 vertices;
- `alpha(R)=5`, `omega(R)<=11`, inherited D caps;
- `delta(R)=13`;
- `400<=E=e(R)<=408`;
- exact outer ledger

`E + sigma + g + x6 + y6 = 408`.

Do not assume E406, q30, S30 coverage, an eighth K12, Delta<=14, or generic R(4,49) emptiness.

## 2. Proved assets you should use

### A1. Generic R(4,48) floor310 and h12 closure

`C in R(4,48) => e(C)>=310`.

The T61 minimum-degree12 branch is empty by q20 leaf-rotation, so every survivor has minimum degree13.

### A2. E397, E398, E399 are empty

E397: excess1 forces `14,13^60`; every low pivot has G=0, impossible for the unique high vertex.

E398: excess3 forces `14^3,13^58`; every low-high edge gives exact q23,z22,G1 shell. Its missing graph is forced to `(K_{2,11}+centre edge)-one cross edge`, which contains an independent11-set in the shell complement, contradicting `alpha(M)<=10`.

E399: excess5. Exact q24 shell analysis proves both cells impossible:

- `(q,z,G)=(24,22,2)`;
- `(q,z,G)=(24,23,1)`.

This kills all degree15 partitions and then the all-degree14 partition. See `front_end/E399_Q24_SHELL.md`.

Hence current line is E400..E408.

### A3. General neighbour-excess bound

Write `E=397+s`. For every degree13 pivot p,

`G_p = sum_{a in N(p)}(d_R(a)-13) <= s`.

Thus for E400 (`s=3`), every degree13 vertex sees at most3 units of neighbour excess.

### A4. Shell lower contracts

For every h13 pivot:

`E = 91 + q + e(C47)`, `q>=22`, `e(C47)>=284`.

The 13-shell missing graph M satisfies:

- `alpha(M)<=10`;
- M has a 3-matching;
- each M-edge has endpoint row-weight sum at least11;
- each M-triangle has row-weight sum at least24;
- an M-K4 forces q>=30.

These were enough to classify q23 and eliminate the exact q24 cells.

## 3. Priority 1 — close E400

For E400:

- `s=3`;
- total degree excess above13 is

`Xi = 2*400 - 61*13 = 7`.

First derive the complete list of global excess partitions compatible with the neighbour-excess cap3 and degree support. Do not merely list integer partitions: eliminate any excess-k vertex that cannot obtain at least `13+k` neighbours under the cap.

Then classify the exact low-pivot shell cells. The most important cells are those with neighbour excess G=3, because then

`q>=22+3=25`,

and the 284-core floor gives `q<=25`; hence

`q=25`, `z=22`, `e(C47)=284`.

You should seek a uniform exact q25 theorem, analogous to the q23/q24 closures. Split by decoration partitions of3:

- `3`;
- `2+1`;
- `1+1+1`.

Try the same two-way shell split:

1. M triangle-free: use the mandatory 3-matching, Mantel equality/slack, matching number bounds, König cover structure, and divisibility of outside attachments.
2. M contains a triangle: use the 10-vertex outside part, K4-freeness, pair-row weights, decoration budget, and a profitable repivot at a regular degree1/2 outside vertex.

The goal is to prove the exact q25 cells impossible, not just enumerate them.

## 4. Priority 2 — parameterize E401+ rather than layer-by-layer brute force

After E400, move to `s=4,5,...` and ask whether the q23/q24/q25 proofs are instances of a common shell-stability theorem.

Preferred form:

`q = 22+r`, `G=r`, `z=22`, core=284

or

`q = 22+r`, `G=r-1`, `z=23`, etc.

Seek a theorem that either:

- forces an independent11-set in M;
- forces a profitable degree13 repivot with larger q than allowed by the fixed edge layer;
- or forces a finite normal form whose attachment count violates divisibility / matching structure.

Do not spend the main effort on S30 until the low-edge route stops yielding exact cells.

## 5. S31/S30 boundary

S31 applies only to the same residual when `E=406`, `delta=13`, with all inherited parent hypotheses. It gives a degree13 pivot with q<=30. It does not create a block.

Do not map E400..405 or E407..408 into S30 without an explicit interface theorem.

## 6. Auxiliary tasks

1. Re-run the contextual recurrence using modern seeds `R(3,35)>=211`, `R(4,48)>=310`; create a new certificate version rather than mutating the old one.
2. Audit 47-core near-extremal states at 284,285,... needed for q25+.
3. Build a small exact shell normal-form enumerator if useful, but its output must be converted into a human lemma; solver UNSAT alone is not a proof.
4. Maintain exact status labels: `PROVED`, `COMPUTATION_CERTIFIED`, `CONDITIONAL`, `OPEN`, `RETRACTED`.

## 7. Required output

Return:

- `T61_H13_MASTER_V4.md`
- `E400_CLOSURE.md`
- `Q25_SHELL_THEOREM.md`
- `E400_EXCESS_PARTITIONS.md`
- `CORE284_LOCAL_CELLS_V2.md`
- `T61_DEPENDENCY_DAG_V4.md`
- `RECURRENCE_V4_REPORT.md`
- verifier/certificates if used.

Success criterion: close E400 and preferably several subsequent layers, or reduce E400..408 to one explicit shell/core equality family substantially narrower than the current window.