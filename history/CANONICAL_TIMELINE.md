# Canonical research timeline

This file records the reconstructed progression of the EG617 r=12 project. It is a provenance/history document, not an assertion that every historical CLOSED label remains valid. Current proof status is controlled by `ASSET_LEDGER.md` and `STATUS_POLICY.md`.

## Phase 0 — original target and first reductions

Target: prove the r=12 case of Erdős Problem 617 by excluding the relevant balanced K145 counterexample.

Early work developed:

- least-edge colour formulation with `m<=870`;
- hereditary density caps `D(n)`;
- anchor/minimum-degree reductions;
- K12 block packings and residual Ramsey classes;
- degree-pivot decompositions and shell/core bookkeeping.

Several early exact-edge targets such as a 325-edge 49-residual were later recognized as unnecessarily strong and are now RETRACTED as architectural requirements.

## Phase 1 — 49-point backend construction

The degree-13 pivot framework for a legal `F in R(4,49)` was stabilized:

`49 = 1 + 13 + 35`,

`e(F)=91+q+e(H)`.

The shell missing graph `M`, decorations `g`, subset charge identity, and exact repivot identity became the central local-to-global machinery.

Historical searches initially gave an approximate edge window around 325–340 and split difficult low-q states into S27/S30/S31-style residual objects.

## Phase 2 — S27 / S30 / S31 structural program

### S27

The certified theorem retained at exact scope is:

no relevant 47-core with `e=288` and minimum degree 11.

Historical broader slogans are not used unless their hypotheses are reconstructed.

### S30

The q30/e285 triangle-row program developed exact row incidence, pure-class profiles, overlap budgets and finite normal forms. A large part of the old case tree was discovery history rather than final proof.

The currently certified `(5,7,8,8)` result is only the explicit row-labelled branch under the required singleton adjacency hypotheses. Later audit work also removed many scalar configurations without assuming the singleton triangle, but the complete profile remains OPEN.

### S31

The strict-descent theorem was eventually audited under an explicit 61-point parent contract:

`|V|=61, e=406, delta>=13, alpha<=5, omega<=11`, plus inherited density assumptions

`=> exists degree-13 pivot with q<=30`.

It is a descent theorem inside that class, not a proof that every original colouring reaches that class.

## Phase 3 — clean lower cores

The old generic CORE211 shortcut was replaced by a clean proof.

Current theorem:

`H in R(3,35) => e(H)>=211`.

At equality, total degree excess above 12 is two, hence only

- `14,12^34`,
- `13^2,12^33`.

The 23-point lower core was also sharpened:

- `R(2,23)` edge floor 131 is sharp;
- an explicit extremal family was reconstructed;
- near-extremal layers 131–134 were classified in the integration work and used to build the clean CORE211 proof.

The final manuscript must preserve the exact analytic/certificate provenance of those near-extremal classifications.

## Phase 4 — low-edge backend layers

Using CORE211 and repivot theory:

- E329 closed;
- E330 closed;
- E331 closed;
- E332 reduced to the equality state `(q,e(H))=(30,211)`.

The q29 result was scope-corrected during audit:

`q=29 + inherited delta(H)>=12 => exists degree-13 y with q_y>=30`.

This good-repivot existence theorem does NOT require `e(H)=211`. CORE211 is used separately in the fixed E331 corollary to contradict `q_y>=30`.

Current low backend frontier:

`E332 : q30 shell over an almost-12-regular 211-edge 35-core`.

Higher layers E333–E340 remain a separate high-layer stability line.

## Phase 5 — q30 equality geometry

For E332, undecorated shell degrees 4..9 are automatically profitable. The equality channels d=3 and d=10 force all repivot slack terms to vanish.

This yields rigid row systems:

- d=10: 3x10 missing-shell normal form and 10-vertex core rows;
- d=3: dual 3x10 form and degree-12 core triangles;
- repeated equality rows are expected to be equal/disjoint under exact hypotheses.

Historical E405 q30-LIFT arguments provide a template but cannot be copied directly because their parent contract is stronger.

## Phase 6 — front-end provenance reset

A major audit separated the original K145-to-residual bridge from backend closure.

Obsolete architecture:

`K145 -> exact E325 residual`.

Modern target:

`K145 -> some legitimate F in R(4,49)`.

Seven/eight genuine K12 block arguments were independently reconstructed, including matching-transversal rigidity and equality rotation.

Eight genuine blocks are sufficient to produce a legal 49-point residual, but their existence cannot be assumed.

## Phase 7 — exact outer recurrence and T61

The front-end finite recurrence was rebuilt under a contextual no-extraction assumption inside one fixed original graph. It uses lower-order seeds only, not backend R449 emptiness.

Certified arithmetic:

- 1752 recurrence nodes;
- 144 outer stopping comparisons;
- two independent integer implementations agree.

The outer bridge is now a proved dichotomy:

`original least-edge colour G => legal induced R(4,49) OR embedded T61`.

The unique terminal stop is

`(d,j,a,n)=(11,6,5,61)`.

T61 has:

- degree-11 anchor;
- six genuine K12 blocks in the anchor nonneighbourhood;
- 61-point residual R;
- `alpha(R)<=5`, `omega(R)<=11`;
- `397<=e(R)<=408`;
- `delta(R) in {12,13}`;
- exact ledger `E+sigma+z+g+x6+y6=408`.

## Phase 8 — current T61 tightening

New analytic deductions now give:

- `alpha(R)=5` under contextual no-extraction;
- anchor defect `z=0`, so `N[v]` is a genuine K12;
- modern generic `R(4,48)` floor improves from 308 to 309 using CORE211;
- the T61 minimum-degree-12 row begins at E407, not E406;
- a 309-edge R(4,48) core has an exact q20 equality shell:
  `M=K_{2,r} + isolates`, `6<=r<=10`;
- its two 10-vertex centre rows overlap in at least seven vertices inside the 211-core.

These results are recorded in `front_end/T61_NEW_LEMMAS.md`.

## Current global frontier

Line A: eliminate/extract T61.

Line B: eliminate E333–E340 by a uniform high-layer theorem.

Line C: eliminate E332 q30+211.

The full EG617 r=12 theorem remains NOT_CERTIFIED until both the front-end extraction and the entire 49-point backend are closed.