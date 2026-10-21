# Astra A prompt — T61 h13 terminal line (V5)

You own ONLY the remaining embedded T61 front-end obstruction for Erdős Problem 617, r=12.

Do not redo the certified outer recurrence. Do not attack backend E332 or E333–E340. The h12 branch and E397–E400 are now analytically closed.

## 0. Current clean target

Proved chain:

`hypothetical balanced K145 / least-edge colour G`

`=> induced F in R(4,49) OR embedded T61`

and now

`T61 => delta(R)=13 and 401<=E<=408`.

Your sole objective is

`T61(h13, E401..408) => contradiction OR induced F in R(4,49)`.

## 1. Exact T61 contract

- anchor degree11;
- anchor defect z=0, so N[v] is a genuine target K12;
- six additional genuine K12 blocks in the anchor nonneighbourhood;
- residual R has61 vertices;
- `alpha(R)=5`, `omega(R)<=11`, inherited D caps;
- `delta(R)=13`;
- `401<=E<=408`;
- exact outer ledger `E+sigma+g+x6+y6=408`.

Do not assume E406, q30, S30 coverage, an eighth K12, Delta<=14, or generic R(4,49) emptiness.

## 2. Proved shell ladder

For every degree13 pivot p:

`E=91+q+e(C47)`, `q>=22`, `e(C47)>=284`.

Writing `E=397+s`, every low pivot sees neighbour-excess

`G_p<=s`.

Already closed:

- q23 / `(z,G)=(22,1)`;
- q24 / `(22,2)` and `(23,1)`;
- q25 / `(22,3)`, `(23,2)`, `(24,1)`.

The q25 theorem uses a uniform triangle/triangle-free argument and is in `front_end/E400_Q25_SHELL.md`.

Consequently E397, E398, E399 and E400 are empty.

## 3. Priority 1 — close E401 by q26

For E401:

- `s=4`;
- total degree excess `Xi=9`;
- every degree13 pivot sees at most4 units of neighbour excess;
- every pivot has `q<=26`.

The genuinely new exact cells are

- `(q,z,G)=(26,25,1)`;
- `(26,24,2)`;
- `(26,23,3)`;
- `(26,22,4)`.

Also check whether q25 with `(z,G)=(21,4)` is possible; attempt to extend the q25 theorem from G<=3 to G=4 first.

Seek a **uniform q26 shell theorem**, not four unrelated enumerations.

### Suggested architecture

1. **Triangle-free M**
   - mandatory 3-matching;
   - 4-matching impossible by charge;
   - rule out C5/C7 odd-cycle branches using matching number and subset charge;
   - use König to obtain a size-3 cover X and independent Y of size10;
   - exploit regular Y-vertex repivots. In q25, undecorated degree2/3 Y vertices were impossible because they force a fourth cover vertex to have too little weight to meet Y. Generalize this with one extra unit of q slack.

2. **Triangle M**
   - write B=A\T, `u=e(M[B])`;
   - use triangle row coverage plus the small decoration budget to bound `u+G_B`;
   - attempt to show u=0 or u<=1;
   - classify B T-degrees and use regular degree1/2 B vertices for profitable repivots;
   - force an independent11-set in M if one triangle vertex loses all B-neighbours.

3. **Global E401 support**
   - once all low-high cells with G=1..4 are excluded, conclude no degree13 vertex can meet any positive-excess vertex;
   - total excess9 gives at most nine positive vertices, still far too few to support degrees >=14 without low neighbours.

## 4. Priority 2 — look for a parameterized theorem

Try to prove a shell-stability statement for

`q=22+r`, small r,

with `z>=22` and `G<=r`, such that every positive-decorated low-pivot cell is impossible until some explicit threshold.

The ideal outcome removes E401–E403 or more at once.

## 5. S31/S30 boundary

S31 applies only at the same residual with `E=406`, `delta=13` and its full inherited parent contract. It gives a pivot with q<=30 but does not create a block.

Do not map E401..405 or E407..408 into S30 without a proved interface.

## 6. Required output

Return:

- `T61_H13_MASTER_V5.md`
- `E401_CLOSURE.md`
- `Q26_SHELL_THEOREM.md`
- `Q25_G4_EXTENSION.md`
- `E401_EXCESS_SUPPORT.md`
- `T61_DEPENDENCY_DAG_V5.md`
- verifier/certificates if used.

Every statement: `PROVED`, `COMPUTATION_CERTIFIED`, `CONDITIONAL`, `OPEN`, or `RETRACTED`.

Success criterion: close E401 and preferably several following layers, or reduce E401..408 to one explicit equality family substantially narrower than the current window.