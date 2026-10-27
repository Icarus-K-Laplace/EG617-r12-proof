# V10/V11 independent replay audit — E407 maximum-Q31 interface

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL + COMPUTATION_CERTIFIED** for the E407 h13 maximum-Q31 exclusion, relative to the named lower-order/core seeds and external extremal inputs.

This audit upgrades the Q31 branch from a source-reported dependency to a directly inspected and replayed package chain. It does not claim a formal-proof-assistant certification.

## 1. Original package provenance

The original uploaded archives were materialized from the project Library and audited directly.

- `T61_H13_V10.zip`
  - archive SHA256: `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`
- `T61_H13_V11.zip`
  - archive SHA256: `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`

Fresh extraction before running any verifier gave a complete `sha256sum -c SHA256SUMS.txt` pass for every listed package asset in both archives.

The verifier programs subsequently rewrite a small number of generated JSON receipt files; byte-hash changes after execution are therefore treated as generated-output changes, not source-asset corruption. The fresh pre-run extraction is the integrity reference.

## 2. V10 exact replay

Executed from a fresh extracted V10 package:

```text
python -B verify_v10.py
```

Returned:

```text
status = COMPUTATION_CERTIFIED
labelled_cut_rows = 12
local_neighbourhood_cases = 16
row_budget_cases = 14
shell_witnesses = 1
Q31_d3_d10_incidence = PROVED
Q31_coverage = OPEN
full_graph_search = false
```

This is exactly the advertised scope: V10 does not close Q31. It analytically excludes the regular missing-degree `d=3` and `d=10` plateau branches and leaves the remaining Q31 candidate degrees to V11.

## 3. V10 analytic dependency audit

The V10 package contains the complete retained V8 exchange/flat-boundary argument in its input bundle, rather than merely citing an opaque status flag.

For a regular missing-degree-three shell neighbour y, the exchange calculation gives

\[
q_y=30+\rho+h+\kappa+b.
\]

If the parent maximum is `Q=30+k`, maximality yields

\[
\rho+h+\kappa+b\le k.
\]

The V8 flat-boundary proof then excludes the equality plateau `rho=k` by forcing `h=kappa=b=0` and deriving the prohibited shell/core incidence configuration. Hence

\[
\rho\le k-1.
\]

At maximum Q31 this is the exact plateau control consumed by V10. V10 then certifies its finite labelled-cut/local-neighbourhood/row-budget tables and derives the d3/d10 exclusions.

The bundled V6 core interface also contains the derivations needed by V10:

- genuine 47-core membership and `e(C)>=284`;
- the small-edge minimum-degree interface;
- the EDGE13 alternative used in repivot arguments.

The small Ramsey/core seeds consumed by that interface are listed as `PROVED` in the current front-end assumption ledger; they are not re-proved by this audit.

## 4. V11 exact replay

Executed from a fresh extracted V11 package:

```text
python -B verify_kernel_certificate.py
```

Returned the exact advertised kernel coverage:

```text
kernel weight assignments = 684
outside count states = 349
labelled necessary shells = 259
Family A = 252
Family B = 7
actual completed graphs claimed = 0
solver used = false
certificate SHA256 = 0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b
```

The kernel subtotals were also reproduced:

- `K4,r=0`: 348 weight states, 336 count states, 252 survivors;
- `K4,r=1`: 165, 0, 0;
- `W8,r=0`: 49, 4, 0;
- `W8,r=1`: 8, 0, 0;
- `W7_overlap,r=0`: 53, 0, 0;
- `W7_separate,r=0`: 61, 9, 7.

Thus all 259 labelled necessary Q31 shells are partitioned into the two recorded terminal families.

## 5. V11 coverage audit

`Q31_FULL_CANDIDATE_COVERAGE.md` uses the V10 d3/d10 exclusion to restrict regular shell missing degrees to

\[
\{0,1,2,11,12\}.
\]

The exact finite generator then enumerates the remaining kernel-weight and outside-count states and maps every necessary labelled shell to one of:

- Family A: nine d2 rows plus one d12 row — 252 states;
- Family B: ten d2 rows — 7 states.

No completed graph is claimed by the finite certificate. The certificate establishes finite necessary-state coverage only; impossibility of A/B is analytic.

## 6. Analytic completion contradiction

The load-bearing completion theorem `NINE_D2_SUPPORT_CAPACITY.md` was inspected directly.

It does **not** assume the d2 rows are disjoint. Instead the common-K10 pair-row capacity bounds imply:

1. row multiplicity at most two;
2. support union size at least17;
3. synchronizing the ten core degree inequalities eliminates all repeated positive-capacity support;
4. the remaining zero-capacity support graph has maximum degree at most one and is therefore a matching with at most ten edges.

Selecting one endpoint from every matching edge and every unmatched support point gives an independent set of size at least

\[
17-10=7,
\]

contradicting the T61 parent bound `alpha(R)<=5`.

The same theorem covers both V11 terminal families after the finite coverage map. Therefore no maximum-Q31 parent survives.

## 7. Promotion

Relative to:

- the genuine h13 T61 parent contract;
- the V6/V8 analytic exchange/core interfaces bundled into V10;
- the small Ramsey/core seeds currently registered as `PROVED`;
- the exact finite V10 and V11 certificates replayed above;
- the external extremal results explicitly cited by those interfaces;

the branch

\[
\boxed{E407,\ h=13,\ Q_{\max}=31}
\]

is **PROVED_CONDITIONAL impossible**, with its finite state coverage **COMPUTATION_CERTIFIED**.

This audit replaces reliance on the older label `SOURCE_REPORTED` for the V10/V11 package contents.

## 8. What is not claimed

- No SAT/ILP or heuristic solver is used by these package replays.
- The finite verifier does not prove arbitrary graph nonexistence by itself; it proves the stated finite necessary-shell coverage.
- The analytic completion proofs remain ordinary mathematical proofs with named external/core inputs, not Lean/Coq artifacts.
- This file alone does not prove EG617(r=12); it closes only the maximum-Q31 E407 interface used by the root chain.
