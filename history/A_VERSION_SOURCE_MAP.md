# A-version source map

Status: provenance index only. This file records where useful proof bodies occur in the user-supplied A-version PDF sequence (`EG617 r12推进_1-764`). It does not upgrade any theorem status by itself.

## Source bundle

A-version consists of contiguous page ranges 1--764, supplied as PDF chunks.

## High-value proof locations identified

### q=27 lower-floor/equality pipeline

Global pages approximately 683--702 contain the corrected 13-shell finite system and equality classification setup. The shell constraints explicitly include:

- `ab in E(M) => t_a+t_b >= 12`;
- `K3 => sum t >= 24`;
- `K4 => sum t >= 35`;
- `z >= 22`;
- `alpha(M) <= 10`;
- `K5 not subset M`.

The old A-version then reports `q<=26` infeasible and derives `q>=27`. At `q=27`, only `z=24` and `z=27` survive, producing exactly

- `M ~= K_{3,8} + 2 K1`, with decorations `g=(1^3,0^10)`;
- `M ~= K_{3,9} + K1`, with `g=0`.

This equality classification depends on finite computation in the A-version and must not be relabelled analytic without a replayable modern certificate.

### q=27 analytic repivot closure

Global pages approximately 703--722 contain the analytic closure of both equality types. The argument uses universal repivot charge control plus row-multiplicity/duplicate-row forcing.

Type II (`K_{3,9}+K1`) is repivoted and forced back into the same equality family; row-overlap constraints force the three heavy rows to coincide, after which repivot creates too many isolates, contradiction.

Type I (`K_{3,8}+2K1`) yields row-equivalence classes of size 2 or 3. Since eight light rows must partition into such classes, a class of size 2 exists; repivoting there forces Type II, already impossible.

This proof body is a strong candidate for clean-room reconstruction as `backend/Q27_TYPE_I_II_FULL_PROOF.md`.

### historical q29 closure

Global pages around 586 onward contain the old q29 closure through a large `delta(L)=20/21` deletion tree. This is historical discovery material. It is not the same theorem as the modern generic q29 good-repivot result and must not be substituted for it.

### Universal Core Theorem (historical exact-325 architecture)

Global pages 742--754 approximately contain an analytic theorem:

`K4 not subset L, alpha(L)<=11, delta(L)>=20 => e(L)<=388`.

The proof reduces the maximum degree to 23/24, eliminates both cases, and obtains the edge upper bound. Combined with the old exact-325 identity `e(L_p)=361+q_p`, this gives `q_p<=27` for every degree-13 pivot.

This is a valid-looking analytic asset under its explicit hypotheses, but it belongs to the older exact-325 residual architecture. It is not the modern `CORE211` lower bound and must remain scope-separated.

## Scope warnings

1. Old boxed `CLOSED` labels are not proof status by themselves.
2. The A-version contains a retracted arithmetic value `z=15`, corrected later to `z=14`.
3. The q=27 lower-floor step is finite-computation dependent in A-version.
4. The Universal Core Theorem depends on `delta(L)>=20`, which belongs to the old exact residual contract and is not a generic property of current `R(4,49)` backends.
5. q29 historical deletion-tree closure is not the modern generic q29 theorem.

## Consolidation priority

1. Recover the analytic q27 Type I/II repivot closure.
2. Extract the exact A-version dependencies and rewrite them standalone.
3. Keep the q=27 finite classification certificate separate from the analytic repivot proof.
4. Archive the Universal Core Theorem as a conditional/historical theorem unless the modern proof DAG explicitly licenses its hypotheses.
