# Live three-line research state — 2026-10-22

This is the synchronized human-readable live state for Lines A/B/C. It contains research results only, not agent prompts.

## Line A — T61 front end

Repository-canonical proved layers currently run through `E400`.

Source package V6 reports `E401..E404` empty. V7 reports `E405` empty under the explicit T61 hereditary-cap contract.

Latest package-level front-end window:

`E406, E407, E408`.

### Astra-A V8 (source-reported)

V8 reports the following new theorem for a maximum-charge pivot with

`Q=30+k`, `1<=k<=3`:

for every regular missing-degree-3 neighbour,

`rho <= k-1`.

The boundary family `rho=k` is reported analytically excluded by the common-K11 / row-triangle / repeated-repivot argument. Full excess-migration and reverse-repivot identities are included in the package.

V8 explicitly leaves `E407,E408` OPEN. Its remaining obligations are:

- `E407: Q_max=27`;
- `E408: Q_max in {27,28}`;
- global compatibility/cycles of nonzero correction terms across distinct pivots.

Evidence status: `SOURCE_REPORTED / PACKAGE_PRESENT / INDEPENDENT_REPLAY_PENDING`. See `front_end/T61_H13_V8_RESULT.md`.

### Assistant-owned E406 subline — current live frontier

The assistant-owned E406 work is deliberately disjoint from Astra A's E407--E408 assignment.

Current distance-class status:

- `d=10`: `PROVED EMPTY`;
- `d=11`: `PROVED EMPTY`;
- `d=2`: `PROVED EMPTY`;
- `d=3`: Type-B is `PROVED EMPTY`; Type-A is reduced to `O<=4`;
- `d=1`: `OPEN`, common-K11 deficit / excess-transfer system;
- `d=12`: `OPEN`, paired dense 12-block system.

Thus the surviving E406 frontier is exactly

`d1`, `d3-TypeA with O<=4`, `d12`.

Latest d3-TypeA reductions:

- complete `O=5` closure;
- every O4 state has full-row counts `(9,10,10,10)`;
- eta=0 O4: `e(H)=152`, total H excess4, `R=3`;
- eta=1 O4: `e(H)=151`, total H excess3, `R=4`;
- no four-full H vertex, so O4 multiplicity type `3+1` is impossible;
- eta=0 simple-four-double branch is **fully closed**;
- eta=1 high-pair rigidity leaves only the low-row simple profiles `(5,6,8,8)`, `(6,6,8,8)`, `(6,6,7,8)`, `(6,7,7,7)`;
- `(6,7,7,7)` is now `PROVED EMPTY` by row-degree balance plus the no-repeated-hub / no-singleton-hub theorems.

Therefore the eta=1 simple-four-double frontier is exactly

`(5,6,8,8)`, `(6,6,8,8)`, `(6,6,7,8)`.

The remaining d3-TypeA O4 work consists of:

1. those three eta=1 simple-double profiles;
2. one triple + two doubles;
3. two triples.

## Line B — high backend E333..E340

All edge layers remain `OPEN`.

V4 source package reports a support-repetition theorem for a maximal `(q,tau)` pivot:

- the relevant distance class has size9 or10;
- at least five legal neighbours share a common nonempty two-point missing set;
- single-hub family `D1` is excluded;
- the two-hub zero-defect family is excluded.

Reported remaining necessary shell families:

`D2-A`, `D2-B`, `D2-C`, `D2-D`, `R9`,

with common-missing-set repetition lower bounds `8,8,5,7,9`.

These are necessary shell rows only, not realized graphs. `E333..E340` all remain OPEN.

Evidence status for V4: `SOURCE_REPORTED / PACKAGE_PRESENT / INDEPENDENT_REPLAY_PENDING`. See `backend/HIGH_LAYER_BACKEND_V4_RESULT.md`.

## Line C — E332 q30+211

`COMPLETE AND FROZEN: E332 = EMPTY`.

## Global state

The full EG617 r=12 theorem remains OPEN.

Only two independent mathematical obligations remain:

1. finish T61 front end: `E406..E408`;
2. eliminate legal R(4,49) high backend interval `E333..E340`.
