# Hypothesis Sensitivity

## 1. If H_B only proves K>=7

No loss. `K=2e(H)-r(3r-1)` is always even, so `K>=7` is equivalent to `K>=8`.

## 2. How weak can the anchor floor be for endpoint collapse?

The exact law is

`q+epsilon=3r+3-K/2`.

If `K>=kappa`, the full medium interval `4<=d<=r-3` disappears once

`r>15-epsilon-kappa/2`.

Worst case epsilon=0:

- K>=2: r>=15;
- K>=4: r>=14;
- K>=6: r>=13;
- K>=8: r>=12.

Thus Exact Three-Anchor is much stronger than needed merely to reduce to endpoint width O(1).

More generally `K>=-lambda r-O(1)` with fixed `lambda<2` still gives asymptotic medium-degree disappearance.

## 3. Original delta(H)>=r-C weakening question is now largely bypassed

The residual-extraction sibling proves something stronger and cleaner: for every r>=17, once a legal `4r+1` residual with the inherited cap is extracted, the exact contract follows automatically, including `delta(H)>=r`.

Therefore the asymptotic synthesis no longer needs to negotiate a weakened `delta(H)>=r-C` hypothesis at all. The front target should be weakened **upstream**, not locally:

> extract the legal `4r+1` residual, or classify the `5r+1` stop.

This is a major reduction of H_A.

## 4. Does H_C need a universal repivot potential?

No. H_C* only needs terminal closure after existing reductions:

- medium d gone;
- d3 common-S closed;
- high endpoint bounded by a finite kernel;
- remaining d0/d1, scalable d2, and bounded high skeletons closed or improving.

A theorem valid only at lexicographically maximal/terminal pivots is enough.

## 5. Sensitivity of r0 to H_B

The full three-anchor theorem is analytic for r>=68. Therefore H_B is not an asymptotic assumption above 68.

The value 68 comes solely from

`2r-9 > 5(3r-1)/8`.

Any improvement to threshold R_B changes the anchor contribution to r0 immediately.

## 6. Sensitivity to the front end

The old front hypothesis combined two tasks:

1. obtain a legal `4r+1` residual;
2. certify the exact pivot/core minimum-degree contract.

Task 2 is now **PROVED_ANALYTIC for r>=17**. Hence the only open front hypothesis `A_ext` is task 1, together with the alternative controlled `5r+1` stopping classification.

If A_ext is proved for all r>=50, it costs nothing numerically at the present synthesis threshold because 50<68. If only for r>=R_ext>68, the final threshold becomes at least R_ext.

## 7. Sensitivity to H_D

Exact affine-plane nonextension is already proved. The missing D is a stability/classification result taking a general `5r+1` stop to an exact or robustly nonextendable design class.

Any finite threshold is initially acceptable.

## 8. Current sensitivity ranking

For **existence** of the first unconditional infinite-family theorem:

1. `A_ext` — force `4r+1` residual or controlled `5r+1` terminal;
2. `C*` — close d2/d0/d1 and bounded high terminals;
3. `D` — close design terminal;
4. three-anchor below 68 — only threshold optimization, not existence above 68.

For the **numerical value of r0** in the current conditional theorem, the three-anchor AES threshold 68 is the active bottleneck.

## 9. Highest-leverage weakened targets

Any one of the following is sufficient progress without demanding sharp constants:

- A_ext at any finite threshold;
- d2 upper bound `K+a <= (1-c)r+O(1)` for some c>0;
- common-S owner demand `N>(1/2+c)r-O(1)` to beat multicolour owner capacity;
- terminal-only decoration potential theorem;
- robust design stability producing two orthogonal/cross-intersecting clique partitions.


## 10. Round 2: shortest-route sensitivity

The shortest conditional composition is now
\[
A_{\mathrm{ext}}^*(r)\land D_{\mathrm{low}}(r)\Longrightarrow P(r),
\qquad r\ge67.
\]
It bypasses (H_B), (C^*), and the broad (H_D) classification. The only downstream requirement is to exclude the finite-offset near-anchor terminal family after the direct (5r+1) extraction theorem.

The remaining (D_{\mathrm{low}}) contract is:
- (delta=r): (|W|\in\{2r-4,2r-3,2r-2,2r-1\});
- (delta=r+1): (|W|\in\{2r-7,\ldots,2r-2\}).

The high-degree (|W|=2r-1) layer is closed for (r\ge25); the low-degree (delta=r, |W|=2r-1) layer remains open.

## 11. d2 inequality verdict

The proposed (K+a\le(1-c)r+O(1)) is **not derivable from the current scalar identities**. For even (r\ge68), the exact scalar family
\[
(\epsilon,a,b,K,B,q)=(0,2,0,r-2,r/2+4,5r/2+4)
\]
satisfies the master identity, d2 charge equality, inherited K cap, q ceiling, and the recorded K upper bound, while (K+a=r). This is not a graph counterexample, but it rules out the scalar-only strategy. A structural restriction on the scalable a=2 clean-pair terminal is necessary.

## 12. Owner-demand route verdict

For a common-S family, the multicolour capacity is
\[
N_{\mathrm{capacity}}\le\frac{r-3+2\epsilon+\epsilon\sqrt{4\epsilon+1}}2
=\frac r2+O_\epsilon(1).
\]
The desired (N_{\mathrm{required}}>(1/2+c)r-O_\epsilon(1)) has **not** been proved. Existing sunflower capacities have slope one and do not contradict linear demand. Do not report this route as closed.

## 13. Common C/D interface

The weighted transversal-cover lemma now applies exactly to:
- four clean pair blocks in C (strengthened by the finite 2-SAT result to six cross-edges per four-block subsystem);
- a target-missing pair plus four other target groups in D (the cylinder lower bound and bounded-hub consequence).

This is a rigorous common counting interface, not an identification of the two structures. The clean-pair linear interval and D defect-chain budget remain open. The core common-S pivot system continues to use its own exact repivot and owner-capacity identities.

## 14. Highest-leverage blocker

For the **first unconditional infinite-family theorem**, (A_{\mathrm{ext}}^*) is the highest global gate: without the contextual 4r+1/5r+1 dichotomy, neither the residual nor the near-anchor terminal branch is guaranteed. It is not the only open theorem; (D_{\mathrm{low}}) is the independent downstream blocker once the terminal is reached.
