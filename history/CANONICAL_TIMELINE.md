# Canonical research timeline

This file records the reconstructed progression of the EG617 r=12 project. It is a provenance/history document, not an assertion that every historical CLOSED label remains valid. Current proof status is controlled by `ASSET_LEDGER.md` and `STATUS_POLICY.md`.

## Phase 0 — original target and first reductions

Target: prove the r=12 case of Erdős Problem 617 by excluding the relevant balanced K145 counterexample.

Early work developed least-edge colour bounds, hereditary density caps, anchor/minimum-degree reductions, K12 block packings, residual Ramsey classes, and degree-pivot shell/core bookkeeping.

Several early exact-edge targets such as a 325-edge 49-residual were later recognized as unnecessarily strong and are now RETRACTED as architectural requirements.

## Phase 1 — 49-point backend construction

For a legal `F in R(4,49)` the degree-13 pivot framework stabilized as

`49=1+13+35`,

`e(F)=91+q+e(H)`.

The shell missing graph `M`, decorations `g`, subset charge identity, and exact repivot identity became the main local-to-global machinery.

## Phase 2 — S27 / S30 / S31 structural program

S27 was retained only at its exact certified scope. S30 developed row-incidence and equality-family machinery; the old whole-profile slogans were later scope-corrected. S31 was audited under the explicit 61-point / 406-edge / minimum-degree13 parent contract and gives a degree-13 pivot with `q<=30` there.

## Phase 3 — clean lower cores

The generic core theorem was rebuilt cleanly:

`H in R(3,35) => e(H)>=211`.

At equality the degree multisets are only

- `14,12^34`,
- `13^2,12^33`.

The 23-point lower core has sharp edge floor131, with near-extremal layers used in the clean CORE211 reconstruction.

## Phase 4 — low-edge backend layers

Using CORE211 and repivot theory:

- E329 closed;
- E330 closed;
- E331 closed;
- E332 reduced to `(q,e(H))=(30,211)`.

The q29 scope was corrected to the reusable theorem

`q=29 + inherited delta(H)>=12 => exists degree-13 y with q_y>=30`,

with no `e(H)=211` premise.

Current backend frontier remains E332 q30+211; E333–E340 are a separate high-layer line.

## Phase 5 — q30 equality geometry

For E332, undecorated shell degrees4..9 are automatically profitable. The d=3 and d=10 channels force zero slack and rigid row geometry. Historical E405 q30-LIFT arguments remain templates only because their parent contract is stronger.

## Phase 6 — front-end provenance reset

The obsolete target

`K145 -> exact E325 residual`

was replaced by

`K145 -> some legitimate induced F in R(4,49)`.

Matching-transversal rigidity and genuine-block rotation were reconstructed. Eight genuine K12 blocks imply a legal 49-point residual, but block existence itself cannot be assumed.

## Phase 7 — exact outer recurrence and T61

A contextual no-extraction recurrence was rebuilt inside one fixed original graph. It uses lower-order seeds only and does not assume backend R449 emptiness.

Certified arithmetic:

- 1752 recurrence nodes;
- 144 outer stopping comparisons;
- two independent integer implementations agree.

This gives the proved dichotomy

`original least-edge colour G => legal induced R(4,49) OR embedded T61`.

The unique terminal stop is `(d,j,a,n)=(11,6,5,61)`.

## Phase 8 — T61 anchor and h12 tightening

Inside T61:

- contextual no-extraction forces `alpha(R)=5` exactly;
- anchor defect is eliminated: `z=0`, hence `N[v]` is a genuine K12;
- the outer ledger simplifies to `E+sigma+g+x6+y6=408`;
- six additional genuine K12 blocks remain in the anchor nonneighbourhood.

The generic 48-point floor first improved to309 and then, by q20 leaf-rotation, to

`R(4,48) >=310`.

The same q20 rotation one level up closes the entire T61 minimum-degree12 branch. Hence every T61 survivor has `delta(R)=13`.

## Phase 9 — T61 low h13 shell ladder

Write `E=397+s`. Every degree-13 pivot sees at most `s` units of neighbour degree-excess.

### E397

Total excess1 forces degree multiset `14,13^60`. Every degree13 pivot has zero shell decoration, so the unique degree14 vertex cannot have a degree13 neighbour. Contradiction.

### E398

Total excess3 forces `14^3,13^58`. Every low-high edge gives exact cell `(q,z,G,eC)=(23,22,1,284)`. The q23 shell missing graph is forced to `(K_{2,11}+centre edge)-one cross edge`, which has an independent11-set in `M`, contradicting `alpha(M)<=10`.

### E399

Exact q24 shell analysis eliminates `(24,22,2)` and `(24,23,1)`, closing the layer.

### E400

A uniform q25 theorem eliminates `(25,24,1)`, `(25,23,2)`, and `(25,22,3)`. Together with q23/q24, no degree13 vertex can meet any positive-excess vertex. Since total excess7 gives at most seven positive-excess vertices, no degree>=14 vertex can be supported. Thus E400 is empty.

## Current global frontier

Line A:

`T61: delta=13, 401<=E<=408`.

At E401, `s=4`, total excess9, and the new targets are q26 cells

`(26,25,1),(26,24,2),(26,23,3),(26,22,4)`

plus the q25 extension `(25,21,4)`.

Line B: eliminate E333–E340 by a uniform high-layer theorem.

Line C: eliminate E332 q30+211.

The full EG617 r=12 theorem remains NOT_CERTIFIED until both the front-end T61 obstruction and the entire legal R(4,49) backend are closed.
