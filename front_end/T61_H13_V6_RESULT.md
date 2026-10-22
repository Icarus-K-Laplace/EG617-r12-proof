# T61 H13 V6 result package

Status: `SOURCE_REPORTED_PROVED / INDEPENDENT_REPLAY_PENDING_IN_CURRENT_CHAT_RUNTIME`.

This file records the latest Line-A result package supplied on 2026-10-22. It is research state, not an agent prompt.

## Reported theorem

Under the explicit T61 hereditary-cap contract, the edge layers

`E401, E402, E403, E404`

are reported `PROVED EMPTY`.

The reported uniform shell theorem is:

If a legal degree-13 pivot shell satisfies

- `q<=29`,
- `G<=7`,
- the inherited 47-core has `delta(C)>=12`,
- every missing-shell edge `uv` satisfies `t_u+t_v>=13`,

then there exists a legal degree-13 repivot `y` with

`q_y>=30`.

For the same parent graph, the generic core floor gives

`q_y<=E-375`.

Hence for `E<=404`, one has `q_y<=29`, contradiction.

The source package further reports separate treatments of the lower-q exceptional interfaces needed for E403 and E404.

## Corrections in V6

1. A previously simplified repivot equality had omitted three nonnegative correction terms. V6 restores the complete identity.
2. The state `(q,z,G)=(25,21,4)` is not a legal E401 cell: it directly violates the stated `D(14)=69` constraint.

## Certificate report

The source package reports a 127-row exact rational certificate replayed successfully.

Current chat runtime was unable to unpack/replay the uploaded ZIP, so this repository entry preserves the distinction between:

- `source package theorem status`: PROVED;
- `independent replay by this chat runtime`: PENDING.

## Front-end consequence if replayed/accepted

The active T61 H13 window contracts from

`401<=E<=408`

to

`405<=E<=408`.

This does not certify EG617 r=12 globally.
