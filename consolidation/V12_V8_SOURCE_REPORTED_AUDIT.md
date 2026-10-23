# V12 / V8 source-reported audit

Date: 2026-10-23.

Status: **SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING**.

The user delivered two new proof packages:

- `T61_H13_V12.zip`;
- `HIGH_LAYER_BACKEND_V8.zip`.

The local archive/container executor in this assistant session is currently failing at the client level, so the packages have not yet been independently unpacked and replayed here. The statements below are therefore recorded exactly at the source-report boundary and must not be relabelled as independently certified until the package verifiers and manifests are replayed.

## T61 V12 — source-reported state

Reported results:

- **PROVED**: a new capacity inequality `Xi >= L + 2k - 2` for `k in {8,9,10}`;
- the common-K10 external pair-row union therefore carries at least 18 units of excess;
- **COMPUTATION_CERTIFIED in the delivered package**: exhaustive replay over 8,677 weight assignments and 17,957 counting states, including checks of the analytic elimination-rule hypotheses;
- **CONDITIONAL on retained lower-order seeds**: E407 maximum `Q=32` is reduced to five `rho=0` templates having a common regular `K11`;
- the first unresolved implication is whether those five templates can all be compatible with a single 284-edge core;
- no actual completion was reported;
- E407 therefore remains OPEN;
- E408 remains OPEN and the E407 elimination is not automatically transferred to E408.

Accordingly the source-level front-end frontier is:

- E407: `Q=32` OPEN, reduced to five common-regular-K11 templates;
- E408: `Q=32,33` OPEN.

No stronger status is certified by this audit.

## High backend V8 — source-reported state

Reported result:

> `E334 = EMPTY`, relative to the retained backend and accepted V7 forcing.

The reported terminal core contract is

`|H|=35, e(H)=211, delta(H)>=12, alpha(H)<=3, omega(H)<=11`.

The reported analytic mechanism is global rather than branch-by-branch:

- three independent degree-12 anchors partition the core into three large clique blocks plus at most four connector vertices;
- clique capacity forces at least two connector vertices to consume at least two units of degree excess each;
- this requires total excess at least four;
- CORE211 has total excess only

  `2*211-35*12=2`,

  giving the contradiction.

The report states that this simultaneously removes the former d3, `r=2/allowance=2`, and `r=1/allowance=3` E334 residual branches.

E335 is reported to receive a new necessary upper bound but remains OPEN. No claim is made that E335..E340 or the full EG617 theorem is closed.

## Independent analytic extraction already completed in this chat

Independently of the V8 ZIP replay, `backend/GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md` proves the graph-theoretic partition underlying the reported V8 mechanism.

For a graph with `alpha<=3`, clique number at most `Omega`, and three pairwise nonadjacent equal-degree anchors of degree `delta`, the connector set `C` satisfies

`max(ceil((3delta-n+3)/2), n-3Omega) <= |C| <= 3delta-n+3`.

For `(n,delta,Omega)=(35,12,11)`, this gives exactly `2<=|C|<=4` and the complete block-size/signature classification:

- `|C|=2`: two 3-anchor connectors, blocks `(10,10,10)`;
- `|C|=3`: one 3-anchor and two 2-anchor connectors, blocks `(10,10,9)`;
- `|C|=4`: four 2-anchor connectors, blocks `(10,10,8)` or `(10,9,9)`.

Thus the only V8-specific ingredient still awaiting package replay is the local connector-excess lemma forcing at least two connectors to have degree at least 14.

## Governance

Until replay succeeds:

- V12 package claims remain `SOURCE_REPORTED` / `CONDITIONAL` as stated above;
- V8 E334 closure remains `SOURCE_REPORTED_PROVED_RELATIVE_TO_RETAINED_BACKEND` rather than independently re-certified in this session;
- the full EG617 r=12 theorem remains `OPEN / NOT_CERTIFIED`.