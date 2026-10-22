# Canonical state — 2026-10-22

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For every legitimate residual `F in R(4,49)`, a degree-13 pivot gives

`e(F)=91+q+e(H)`, with `H in R(3,35)` and clean core floor `e(H)>=211`.

Reusable assets include q27/q28/q29 repivot machinery and the reconstructed E329--E331 closures.

### Closed low backend

`E329,E330,E331,E332` are empty. E332 is complete and frozen; preferred proof assets are:

- `backend/E332_FULL_CLOSURE.md`;
- `backend/E332_H1_UNIFIED_FINAL.md`;
- `backend/E332_G8_H0_UNIFIED_CLOSURE.md`.

Therefore the legal `R(4,49)` backend obligation is exactly

`E333..E340`.

## Front-end master reduction

The certified dichotomy remains

`least-edge K145 counterexample -> induced legal R(4,49) OR embedded T61`.

The contextual recurrence is computation-certified at 1752 nodes and 144 stopping comparisons.

Repository-canonical low h13 layers run through E400. Source package V6 reports E401--E404 empty; V7 reports E405 empty. Their package evidence levels remain tracked separately.

### E406 is independently closed

Under the explicit T61 E406 hereditary-cap parent contract,

`E406 = EMPTY`.

Canonical master source:

`front_end/E406_FULL_CLOSURE.md`.

The proof chain is:

1. audited S31 gives a degree-13 pivot with `q<=30`;
2. `front_end/E406_LOW_TO_Q30_BRIDGE.md` proves every such parent contains a genuine q30 pivot;
3. `front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md` independently replays the V7 q30 theorem and proves q30 reaches q31 within at most two regular repivots;
4. the final step is an actual adjacent `q30 -> q31` edge;
5. its missing distance lies in `{1,2,3,10,11,12}`;
6. all six classes are independently proved empty by the E406 closure files.

The E406 bridge no longer depends on an unreplayed V7 black box. In particular:

- every relevant 47-core with at most288 edges has minimum degree at least12;
- q22,q23 are impossible;
- q24--q26 promote without jumping directly to q31;
- q27,q28 are impossible;
- q29 promotes exactly to q30;
- q30 hereditary promotion is independently reconstructed.

The older `E406_FULL_CLOSURE_COMPOSED.md` and `E406_BOUNDARY_BRIDGE_STATUS.md` are provenance records and are superseded by the canonical full closure.

### Active T61 frontier: E407--E408 only

V8 source-reported theorem for maximum charge `Q=30+k`, `1<=k<=3`:

- every regular missing-degree-3 neighbour satisfies `rho<=k-1`;
- the boundary family `rho=k` is excluded;
- exact excess-migration and reverse-repivot identities are supplied.

V8 explicitly leaves:

- `E407: Q_max=27`;
- `E408: Q_max in {27,28}`;
- correction-term compatibility/cycles.

Evidence status for the V8 package is `SOURCE_REPORTED / PACKAGE_PRESENT / INDEPENDENT_REPLAY_PENDING` unless a statement has a separate reconstructed proof file.

Thus the active T61 edge window is exactly

`E407,E408`.

## High backend live state

Line-B V4 reports a support-repetition theorem for maximal `(q,tau)` pivots:

- relevant distance class size9 or10;
- at least five legal neighbours share a common nonempty two-point missing set;
- D1 and zero-defect two-hub families are excluded;
- remaining necessary families `D2-A,D2-B,D2-C,D2-D,R9` have repetition lower bounds `8,8,5,7,9`.

These are necessary shell rows only, not realized graphs. `E333..E340` all remain OPEN.

## Current independent mathematical obligations

1. close T61 `E407,E408`;
2. eliminate legal `R(4,49)` layers `E333..E340`.

There is no remaining E332 or E406 obligation.

## Certification warning

EG617 r=12 remains OPEN. It may be declared proved only after both remaining obligations above are closed.