# C-version source map

Status: `HISTORICAL_SOURCE_MAP`.

Source reviewed: user-supplied `EG617 r12_C版`, pages 1--118.

## Executive classification

The C-version is **not** primarily a source for the current q27/q29/CORE211 backend. It develops an older, largely separate `full-color dual bootstrap / terminal ladder` architecture.

The strongest historical claim in this source is a route to

`F_12(4,49)=empty`

via a 36-point full-color bridge and a non-partite Turan/Kang--Pikhurko input. Because this conclusion would collapse a major part of the current canonical backend, it is recorded as a **high-value candidate theorem requiring clean-room re-audit**, not as a canonical proved result.

## Page map

### pp. 1--24: early general-r / block-production program

Contains:
- least-colour / near-Turan reduction;
- initial block-production bottleneck;
- a historical `r=12,d=8,j=3` checkpoint;
- explicit warning that scalar shell closure alone is insufficient.

These pages are discovery history, not current canonical proof.

### pp. 25--48: CP-04 / CP-05 fiber architecture

Contains:
- residual fibre construction over three 12-vertex blocks;
- lower bounds such as per-block residual incidence >=104;
- triple-certified and double-certified edge counts;
- a Hall-fibre / doubled-vertex circuit lemma;
- an attempted independent-transversal route.

Useful as a source of possible front-end combinatorial lemmas, but this architecture is not currently in the canonical T61 bridge.

### pp. 49--72: CP-06 / CP-07 / CP-08

Key historical assets:
- 23-point bottom-core normalization;
- a `36-point bridge` architecture;
- a claimed theorem `P_12^full(3,36) >= 223`;
- a 23-point extremal lemma for a triangle-free graph with alpha <= 11;
- a star-shell reduction for the near-extremal 220--222 cases.

This is the critical segment to audit if one wants to recover the C-version shortcut.

### pp. 73--96: terminal bootstrap mechanism

Contains:
- a Kang--Pikhurko/non-partite Turan input;
- a `DUAL` upper-bound construction;
- a claimed implication `B_12(a,m) > U_a(m) => F_12(a,m)=empty`;
- historical derivation of `F_12(4,49)=empty` from `B_12(4,49)=309` versus `U_4(49)=307`;
- propagation to higher `(a,m)` terminal states.

This segment is **not accepted canonically** until all definitions, inequality directions, and the external theorem are verified independently.

### pp. 97--118: continued terminal ladder

Contains:
- claimed closures `(5,63)`, `(6,75)`, `(7,87)`, `(8,99)`;
- successive minimum-degree / dual-bootstrap eliminations;
- a new bottleneck near `(9,111)`.

These are historical downstream consequences of the same bootstrap mechanism and inherit its audit status.

## Relationship to current proof-consolidation gaps

- `CORE211`: not supplied here in the modern 35-point form.
- `q27 Type I/II`: not the main subject; A/B remain the relevant recovery sources.
- `generic q29 good repivot`: not supplied in the modern form.
- `E329--E331`: not supplied as the modern low-backend closure chain.

Therefore C-version does **not** directly close the current listed proof-body gaps.

## High-priority audit target extracted from C

The only C-version route worth potentially promoting into the modern proof is the shortcut chain

`P_12^full(3,36) >= 223`

plus the full-color dual bootstrap leading to

`F_12(4,49)=empty`.

If independently verified, this would be much stronger than a local historical curiosity and would require a redesign of the current canonical proof DAG. Until then it remains `CANDIDATE / NON-CANONICAL`.
