# Joint defect propagation via bounded target-defect capacity

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status

**PROVED_ANALYTIC** under the full contextual ((5r+1))-terminal contract, for every (r\ge6212).

This closes the *terminal nonexistence* branch for sufficiently large (r) by a direct target-side counting argument. It does **not** prove the requested edge-by-edge Hub Propagation Theorem, and it does not close the separate front-end implication that every original counterexample must enter this terminal.

## 1. Contract used

Let (W) be a contextual terminal with (|W|=5r+1), target color graph (G_0), and non-target color graphs (G_1,\ldots,G_{r-1}). The inherited coloring contract gives
[
\alpha(G_0[W])\le5,\qquad \alpha(G_i[W])\le r\quad(1\le i\le r-1).
]
Let (Q_0=\bigcup_{j=1}^5 K(B_j)) be the target ideal partition supplied by the established stability theorem, so (sum_j|B_j|=5r+1).

For (r\ge1000), the established target-side defect-concentration theorem supplies a set (X\subset W) such that:
1. (|X|\le114);
2. every missing target edge inside any (B_j) has at least one endpoint in (X);
3. (G_0[B_j\setminus X]) is complete for every (j).

These are the only stability inputs used below. No exact-star reduction, ordinary-label condition, or non-target cover-network classification is assumed.

## 2. Lemma: absolute bound on the number of target-internal deletions

Write
[
x_j=|X\cap B_j|,\qquad x=|X|,\qquad
D_j=\left|\binom{B_j}{2}\setminus E(G_0)\right|.
]

For any hub (v\in X\cap B_j), there are at most four vertices (y\in B_j\setminus X) with (vy\notin E(G_0)). Otherwise five such vertices together with (v) form an independent six-set in (G_0): the five ordinary vertices form a clique by item 3, and none is adjacent to (v). This contradicts (alpha(G_0)\le5).

Every missing target edge in (B_j) either joins a hub to an ordinary vertex or joins two hubs. Therefore
[
\boxed{D_j\le4x_j+\binom{x_j}{2}.}
]
Summing over the five groups and using (sum_jx_j=x),
[
D:=\sum_jD_j
\le4x+\sum_j\binom{x_j}{2}
\le4x+\binom{x}{2}
=\frac{x(x+7)}2.
]
In particular, the coarse bound (x\le114) gives (D\le6897).

### Sharpened hub bound for the declared range

The existing cylinder estimate gives
[
x\le\Phi(r):=\frac{4(27r+15)}{H_r},\qquad
H_r=(r-26)-\frac{27r+15}{r-26}.
]
Put (t=r-26). Then
[
\Phi(r)=\frac{4t(27t+717)}{t^2-27t-717}.
]
For (t\ge6186), direct differentiation gives
[
\frac{d}{dt}\frac{t(27t+717)}{t^2-27t-717}
=\frac{-1446t^2-38718t-514089}
{(t^2-27t-717)^2}<0.
]
At (r=6212) ((t=6186)),
[
\Phi(6212)
=\frac{4\cdot6186\cdot167739}{38098857}<109.
]
Thus for every (r\ge6212), (|X|\le108), since (|X|) is an integer. Consequently
[
\boxed{D\le4\cdot108+\binom{108}{2}=6210.}
]
This is an absolute cap on *all* target-internal missing edges, not just on their endpoints or matching number.

## 3. The oversized-group contradiction

Since the five target groups have (5r+1) vertices in total, at least one group, say (B_h), satisfies
[
|B_h|\ge r+1.
]
Fix any subset (S\subseteq B_h) with (|S|=r+1).

For every non-target color (i\in\{1,\ldots,r-1\}), the inherited condition (alpha(G_i[W])\le r) implies that (G_i[S]) contains at least one edge (e_i). Because (e_i) lies inside (B_h) but has color (i\ne0), it is a missing target edge in (B_h):
[
e_i\in\binom{B_h}{2}\setminus E(G_0).
]
Edges have unique colors, so (e_1,\ldots,e_{r-1}) are pairwise distinct. Hence
[
\boxed{D_h\ge r-1.}
]

But the defect-cap lemma and the sharpened hub bound give (D_h\le D\le6210). Therefore (r-1\le6210), i.e. (r\le6211), contradicting (r\ge6212).

## 4. Theorem

> **Bounded target-defect nonextension theorem.** No contextual ((5r+1))-terminal satisfying the stated inherited coloring constraints and the established target stability/hub-concentration theorem exists for any (r\ge6212).

The proof is exact and analytic. It counts target-deleted edges by their unique actual color, so there is no duplicated charging. It does not assume a bound on the number of non-target cover blocks, and it is unaffected by a shared non-target cover edge: the contradiction occurs wholly inside one oversized target group.

## 5. What this does and does not close

**Closed:** the legal contextual terminal branch for all (r\ge6212), conditional only on the already established target stability/hub-concentration inputs.

**Not closed:** the literal multi-block Hub Propagation mechanism. It is bypassed rather than proved.

**Still open at the full Erdős Problem 617 level:** the front-end implication that every hypothetical counterexample failing ((4r+1))-residual extraction must yield this legal anchored ((5r+1))-terminal. The canonical state already marks that interface OPEN. Thus this theorem alone is not an unconditional proof of Erdős Problem 617 for all sufficiently large (r).

## 6. Adversarial audit

- **Shared edge across covers:** irrelevant to the contradiction; no cover edges are summed.
- **Hub used by many defects:** allowed; it is already included in the (inom{|X|}{2}+4|X|) cap.
- **Two hubs in one block:** their missing pair is counted among (inom{x_j}{2}).
- **Exceptional vertices in (B_h):** at most 108 globally for this range; all non-target-colored pairs inside (B_h) still count among (D_h).
- **Group size:** only (|B_h|\ge r+1) is used; no assumption that sizes are exactly (r) or (r+1).
- **Prime powers / affine planes:** no dependence.
- **Non-target (K_6)-free:** not needed for this shortcut; the proof uses the stronger-to-this-purpose inherited bound (alpha(G_i)\le r).
