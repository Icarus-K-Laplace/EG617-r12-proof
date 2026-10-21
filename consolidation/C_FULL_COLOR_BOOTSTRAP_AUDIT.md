# C-version full-color bootstrap audit

Status: `CANDIDATE / NON-CANONICAL / NEEDS CLEAN-ROOM REPROOF`.

This file records the strongest claim recovered from the user-supplied C-version without promoting it into the canonical theorem DAG.

## Historical claimed chain

The C-version develops a 36-point full-color bridge. Its key local target is

`P_12^full(3,36) >= 223`.

The proof sketch proceeds through a degree-12 split of a hypothetical 36-point object with at most 222 target edges. Writing the 13-point local shell as `H={v} union N(v)` and the 23-point bottom core as `U`, it introduces a small total slack `x+a+b<=2`, a triangle-free 23-point auxiliary graph `B`, and a K4-free rectangle constraint forcing the shell graph `A` into a star-like form. A separate 23-point extremal lemma is then used to eliminate the near-extremal 220--222 cases.

The C-version next invokes a non-partite Turan theorem attributed to Kang--Pikhurko and defines a full-color upper-bound function `U_a(m)`. The claimed bootstrap rule is

`B_12(a,m) > U_a(m) => F_12(a,m)=empty`.

It then records the numerical comparison

`B_12(4,49)=309 > U_4(49)=307`

and concludes

`F_12(4,49)=empty`.

Further terminal states `(5,63)`, `(6,75)`, `(7,87)`, `(8,99)` are propagated from the same mechanism.

## Why this is not yet canonical

The conclusion `F_12(4,49)=empty` is far stronger than the current accepted backend frontier. If valid, it would bypass much of the present E329--E340 analysis. Therefore it cannot be accepted from a historical `PROVED` label alone.

A clean-room promotion requires all of the following:

1. Reconstruct exact definitions of `P_12^full`, `B_12`, `U_a`, and `F_12(a,m)` and verify that the same objects are used throughout the chain.
2. Reprove the 36-point bound `P_12^full(3,36)>=223` line by line, including the 23-point extremal lemma and the star-shell reduction.
3. Verify the exact statement and inequality direction of the Kang--Pikhurko/non-partite Turan theorem used in the `DUAL` step.
4. Re-derive the numerical value `U_4(49)=307` from the verified theorem and definitions.
5. Re-derive `B_12(4,49)=309` from a source independent of the conclusion being proved, ruling out circular bootstrap dependence.
6. Verify that `B_12(4,49)>U_4(49)` really implies emptiness of the same `F_12(4,49)` class used by the modern backend.
7. Only after 1--6 succeed should the current canonical DAG be reconsidered.

## Current research judgment

The C-version is potentially valuable because the 36-point proof contains several concrete local lemmas rather than only a black-box computation. However, the decisive transition is a global full-color bootstrap, not the shell/repivot machinery currently certified in the repository.

Accordingly:

- historical source value: `HIGH`;
- immediate canonical proof value: `NONE YET`;
- audit priority: `HIGH`, because successful verification would dominate the current backend;
- current theorem status: `CANDIDATE`, not `PROVED`.

## Interaction with current proof-consolidation work

C-version does not replace the ongoing recovery of:

- CORE211;
- generic q29 good repivot;
- q27 finite topology certificate;
- E329--E331 modern closure chain.

Those remain independent proof-body obligations unless and until the full-color shortcut is independently certified.
