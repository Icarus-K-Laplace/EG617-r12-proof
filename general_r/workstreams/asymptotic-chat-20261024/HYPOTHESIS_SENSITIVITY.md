# Hypothesis Sensitivity

The purpose of this file is to identify which sibling theorem is genuinely load-bearing for an infinite-family result and which assumptions can be weakened asymptotically.

## 1. What if H_B only proves K>=7?

No loss at all.

`K=2e(H)-r(3r-1)` is always even because `r(3r-1)` is even for every integer r. Therefore

> **`K>=7` is equivalent to `K>=8`.**

Hence a theorem stated as `K>=7` would give the identical q ceiling `q<=3r-1-epsilon`.

## 2. What if the anchor lower bound is weaker?

The exact conservation law is

`q+epsilon=3r+3-K/2`.

For a constant even lower bound `K>=kappa`, medium supports disappear at worst when

`r>15-kappa/2`.

Thus:

- `K>=2` already suffices for endpoint collapse from r>=15;
- `K>=4` from r>=14;
- `K>=6` from r>=13;
- `K>=8` from r>=12.

Conclusion: **Exact Three-Anchor Excess is not needed for the asymptotic disappearance of medium d.** Its real value is downstream: it tightens the endpoint charge budget and activates the currently proved d3/common-S termination machinery.

## 3. How weak can an asymptotic K-floor be?

If

`K >= -lambda r - O(1)`

for a fixed `lambda<2`, then

`q <= (3+lambda/2)r+O(1)`.

Since every medium support has base at least `4r-O(1)`, all medium supports still disappear for all sufficiently large r.

So a positive constant anchor bound is far stronger than what is needed merely to obtain bounded endpoint width.

## 4. What if extraction only gives delta(H)>=r-C?

Using only the handshake lemma, `delta(H)>=r-C` gives roughly

`K >= -C(3r-1)`.

This corresponds to lambda about `3C`. The medium-support criterion lambda<2 then fails for every integer `C>=1`.

Therefore the naive weakening `delta(H)>=r-C` is **not sufficient by itself** through minimum degree alone. A weakened extraction theorem can still work if it supplies a stronger global edge floor, specifically any bound implying

`K>=-lambda r-O(1)` with `lambda<2`.

This identifies the right relaxed target: preserve an edge-excess floor, not necessarily exact minimum degree at every vertex.

## 5. Is a complete global repivot potential H_C really necessary?

No.

For the asymptotic synthesis theorem it is enough to prove a local terminal-closure statement after taking a lexicographically maximal legal pivot:

1. medium d is already gone;
2. d3 common-S is already closed under A+B;
3. high endpoint is already a finite bounded-complement skeleton (`<=3` owners, shell kernel `<=9`, core signatures `<=8`);
4. only d0/d1, scalable d2 plateau/equality/positive-loss states, and the finite high skeleton need terminal contradiction/improvement.

Thus `H_C*` is strictly weaker than constructing a universal scalar/lexicographic potential valid on every intermediate state.

## 6. How sensitive is r0 to H_B?

The sibling three-anchor workstream proves H_B analytically for every `r>=68`. Therefore H_B is not an asymptotic hypothesis above 68.

The current `68` comes solely from

`2r-9 > 5(3r-1)/8`,

which is equivalent to `r>67`.

Any improvement of the three-anchor threshold from 68 to `R_B` immediately changes the synthesis threshold to `max(R_B, thresholds of A/C*/D)`.

If exact three-anchor is eventually proved for all r>=12, the backend anchor contribution to r0 becomes 12.

## 7. How sensitive is the theorem to H_A?

H_A is currently more serious than H_B. The algebraic origins of `4r+1` and `5r+1` are already exact, but the all-r contextual recurrence and `delta(H)>=r` certification are open.

If H_A were proved only for `r>=50`, it would still be fully sufficient for the present asymptotic theorem, because the current B-elimination threshold is 68. In other words, an extraction theorem with a bad but finite threshold below 68 does not change current r0 at all.

Even a much larger extraction threshold `R_A` is acceptable: the theorem becomes `r>=max(68,R_A,...)`.

## 8. How sensitive is the theorem to H_D?

The exact affine-plane nonextension theorem is already proved for every admissible affine-plane order. What remains is a robust classification/stability theorem saying that the `5r+1` terminal produced by the front end is forced into that exact or nonextendable design class.

Therefore H_D is a **classification/stability** bottleneck, not an exact-extension bottleneck.

A coarse sufficiently-large-r stability result is enough; no sharp finite-r classification is required for the headline target.

## 9. Current sensitivity ranking

For the first unconditional all-large-r theorem, the present order of leverage is:

1. **H_A front extraction / core certification** — indispensable and completely open asymptotically;
2. **H_C* d2+d0/d1+bounded-high terminal closure** — residual backend bottleneck;
3. **H_D robust design-terminal classification/nonextension** — needed for the non-residual front branch;
4. **H_B exact three-anchor below 68** — no longer an asymptotic blocker because r>=68 is already proved.

## 10. Highest-leverage weakened targets

Rather than demanding the strongest sibling statements, any of the following would materially advance the infinite-family theorem:

- front extraction with any finite threshold `R_A`;
- endpoint closure only for d0/d1/d2 plus the finite high kernel, not a global potential theorem;
- a d2 inequality `K+a <= (1-c)r+O(1)` for some `c>0`;
- a common-S owner-demand lower bound `N>(1/2+c)r-O(1)` in the fixed-deficit branch;
- robust design stability sufficient to obtain two orthogonal or cross-intersecting clique partitions.
