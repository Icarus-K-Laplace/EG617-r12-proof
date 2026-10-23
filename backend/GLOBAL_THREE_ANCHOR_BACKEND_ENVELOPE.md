# Global three-anchor backend envelope

Status: **PROVED_ANALYTIC**, conditional only on the configuration actually producing three pairwise nonadjacent degree-12 anchors.

This is a direct corollary of `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`.

## Input

For the high-backend decomposition, the layer index `E`, pivot charge `q`, and 35-point core satisfy

`E = 91 + q + e(H)`.

The global three-anchor theorem proves that any 35-point core with

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 anchors

must satisfy

`e(H)>=213`.

## Envelope theorem

Therefore every high-backend configuration with the three-anchor property satisfies

> `q <= E-304`.

This is independent of the historical D2/R9/E-number labels.

For the active layers:

|layer E|three-anchor upper bound on q|
|---:|---:|
|334|30|
|335|31|
|336|32|
|337|33|
|338|34|
|339|35|
|340|36|

## Consequences

### E334

The delivered V7 source report forces the only remaining E334 channel to

`q=32, e(H)=211`.

Any bridge from that channel to three independent degree-12 anchors contradicts the envelope `q<=30`. The delivered V8 report states exactly such a bridge and therefore reports `E334=EMPTY`.

The graph-theoretic contradiction and the envelope are now independently proved; only package-level replay of the V7/V8 forcing bridge remains pending in this assistant session.

### E335

If an E335 residual family produces the same three-anchor structure, then automatically

`q<=31`.

Thus the `q=32/core212` channel is impossible under the three-anchor bridge. This is the natural interpretation of the source-reported V8 statement that E335 acquires a new necessary upper bound but remains open.

### E336--E340

The theorem gives immediate layer-independent target bounds without reopening the E334 case tree. The correct next question is not "which E-layer are we in?" but:

> which surviving shell/support regimes force three independent degree-12 anchors?

Any such bridge immediately places the configuration below the corresponding row of the table.

## Research programme

The high-value bridge theorem is now:

> **Three-Anchor Forcing Bridge.** Sufficiently repeated / globally compatible support systems force three pairwise nonadjacent degree-12 core anchors.

If proved for a broad class of D2/R9/high-q survivors, `GLOBAL_THREE_ANCHOR_BACKEND_ENVELOPE` converts it immediately into contradictions or sharp equality layers across E334--E340.

This is strictly preferable to separate case proofs for each E-layer.