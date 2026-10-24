# Global three-anchor backend envelope

Status: **PROVED_ANALYTIC**, conditional only on the configuration actually producing three pairwise nonadjacent degree-12 anchors.

This is now a direct corollary of `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`.

## Input

For the high-backend decomposition, the layer index `E`, pivot charge `q`, and 35-point core satisfy

`E = 91 + q + e(H)`.

The sharpened global three-anchor theorem proves that any 35-point core with

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 anchors

must satisfy

> `K=sum_v(d_H(v)-12)>=8`,

or equivalently

> `e(H)>=214`.

The proof is fully graph-theoretic: the partition theorem gives connector count `c in {2,3,4}`; K=4 and K=6 equality layers are eliminated by global connector/excess compatibility, transversal-cover counting, dense-base missed-mass inequalities and exceptional-cost additivity.

## Envelope theorem

Therefore every high-backend configuration with the three-anchor property satisfies

> **`q <= E-305`.**

This is independent of the historical D2/R9/E-number labels.

For the active layers:

|layer E|three-anchor upper bound on q|
|---:|---:|
|334|29|
|335|30|
|336|31|
|337|32|
|338|33|
|339|34|
|340|35|

## Consequences

### E334

The delivered V7 source report forces the only remaining E334 channel to `q=32,e(H)=211`.  Any bridge to three independent degree-12 anchors now violates the much stronger envelope `q<=29`.  Delivered V8 source-reports exactly such a bridge and hence `E334=EMPTY` relative to the retained backend/V7 forcing.

The graph-theoretic three-anchor contradiction is independently proved; package-level replay of the V7/V8 forcing bridge remains a separate audit obligation.

### E335

Any E335 residual state in the three-anchor branch satisfies

> `q<=30`.

Thus all E335 channels with q at least31 are automatically excluded once the three-anchor bridge is established.  E335 itself remains OPEN because the forcing-to-three-anchor/master-contract bridge is not yet exhaustive.

### E336--E340

The same theorem gives the layer-independent bounds

- E336: `q<=31`;
- E337: `q<=32`;
- E338: `q<=33`;
- E339: `q<=34`;
- E340: `q<=35`.

No E334 connector case tree needs to be reopened.

## Research programme

The high-value backend bridge is now:

> **Forcing-to-Master-Contract Theorem.** Every surviving maximal-pivot shell either
>
> 1. produces three distinct zero-charge signatures and hence three pairwise nonadjacent degree-12 anchors, entering `q<=E-305`; or
> 2. collapses to at most two zero signatures and enters `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`; or
> 3. lies in a controlled higher-slack equality layer that descends to one of the preceding two regimes.

Once this bridge is exhaustive, the historical E335--E340 labels no longer require independent structural classifications.

This is strictly preferable to separate layer-by-layer proof trees.