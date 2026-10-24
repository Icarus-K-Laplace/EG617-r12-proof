# Progress log

## 2026-10-24 — initial design-terminal pass

### Repository isolation

Created branch `workstream/general-r-design-terminal-20261024` from `workstream/general-r-architecture-20261024`. This workstream modifies only `general_r/workstreams/design-terminal-chat-20261024/`.

### Source archaeology completed

Read the general-r front structural source, constant dictionary, multicolor Turan stability route, affine-plane nonextension theorem, and r=12 front-end bridge / T61 / E397--E405 / S30-S31 source files.

Key archaeology verdicts:

- `61=5r+1` is exact anchor/block algebra;
- `408=3r^2-2r` is exact anchor-ledger algebra;
- `alpha=5`, `omega<=r-1` are structural at the stop;
- under contextual no-extraction, `delta>=r` is symbolic;
- r=12 `delta<=r+1`, outer defect<=11, and `z=0` do not scale.

### New analytic results — pass 1

1. **Exact terminal slack budget:** `sum_i s_i=9r+5`.
2. **Strict target gap:** `s_0>=r` using Brouwer plus Kang--Pikhurko equality classification.
3. **Non-target slack budget:** `sum_(i>0)s_i<=8r+5`; for `r>=15` some non-target color has slack at most8.
4. **Simultaneous stability:** ideal clique partitions exist with total edit distance at most `27r+15`.
5. **Block energy:** non-target total size-deviation energy at most `65r+39`.
6. **Partial RTD theorem:** after deleting at most `92r+54` ideal non-target blocks, at least `r^2-93r-54` clean blocks form partial parallel classes of a linear transversal 5-GDD.
7. **Cylinder lemma:** one internal target deletion forces a linear-size cross-edge cover; equality has one-coordinate two-owner-star form in the equal-group case.
8. **Construction search:** the naive exact `RTD(5,r)+one point` model is impossible for `r>=6`.

## 2026-10-24 — defect concentration pass

The first pass still allowed the `O(r)` correction budget to be distributed over all vertices. The hereditary density caps rule this out for target internal defects.

### Constant-width target partition

For the five Furedi target groups `B_j`, let `D` be the number of ideal internal target edges absent in the actual target graph. The inherited cap on each `B_j` gives

`D >= (r-1) sum_j(|B_j|-r)_+`.

Since Furedi gives `D<=27r+15`, for `r>=44` the total positive size deviation is at most27. As the five deviations sum to1,

> `r-26<=|B_j|<=r+27`.

Status: **PROVED_ANALYTIC**.

### Refined cylinder degree bound

Let `A` be the number of target cross-group additions. Every internal target deletion `uv` satisfies

`d_cross(u)+d_cross(v) >= H_r`,

`H_r=(r-26)-(27r+15)/(r-26)=r-53+o(1)`.

This follows by covering the four-dimensional tuple product: edges incident to `u` or `v` cover at most a `1/L` fraction, while other cross edges cover at most `1/L^2`.

Status: **PROVED_ANALYTIC**.

### Bounded hub set

For `r>=70`, define

`X={v:d_cross(v)>=H_r/2}`.

Every target internal deletion touches `X`, while total cross degree is `2A<=54r+30`. Therefore

> `|X|<=4(27r+15)/H_r=108+o(1)`.

In particular `|X|<=114` for `r>=1000`.

Outside `X`, every target ideal group is an actual target clique. Status: **PROVED_ANALYTIC**.

### Updated blocker

The target-side defect layer is no longer allowed to disperse. The remaining high-leverage task is:

> propagate the same bounded-hub concentration to the `O(r)` bad non-target blocks / pair-multiplicity defects, or derive an omitted-color `(r+1)`-set when they avoid the hub kernel.

If successful, the large-r terminal reduces to an exact large transversal-design core plus `O(1)` exceptional vertices, which is a much sharper nonextension target.

### Status

D1 remains reached conditionally. D2 is still the Chat-A interface. D3/D4 are not closed, but the large-r survivor has been reduced from arbitrary `O(r)`-defect geometry to a bounded target-hub kernel plus an `r^2-O(r)` partial resolvable TD core.


## 2026-10-24 — Hub propagation / exact-core audit (initial attempt; superseded below)

### Frozen source read

Read and froze the current versions of:
- `CANONICAL_STATE.md`
- `DESIGN_TERMINAL_DEFINITION.md`
- `DEFECT_CONCENTRATION.md`
- `STABILITY_THEOREMS.md`
- `NONEXTENSION.md`
- `COUNTEREXAMPLES.md`
- `R12_TO_GENERAL_SOURCE.md`
- `T61_GENERALIZATION_MAP.md`
- `PROGRESS_LOG.md`

No sibling branch or directory was modified.

### New theorem: low-incidence hub propagation

For a non-target ideal partition (Q_i=\bigcup_{a=1}^rK(C_a)), define repeated-group incidence (d_i) and missing-group incidences (m_{ij}). The exact identity is
[
\sum_{j=1}^5m_{ij}=d_i-1.
]
If a repeated-group pair (uv\subset B_j\setminus X) is missing from (G_i) and (d_i\le5), then
[
|E(G_i)\triangle E(Q_i)|\ge(6-d_i)(r-1).
]
Proof: (m_{ij}\ge1), otherwise (u,v) plus one (B_j)-point from each other block is an (i)-independent ((r+1))-set. At least (6-d_i) other group labels occur in every block. For each such label, every point in each other block must be joined in (G_i) to (u) or (v), giving ((r-1)) distinct cross-block edits per label.

Thus for (r\ge44), at most 27 colors can contain a low-incidence ((d_i\le5)) repeated-group pair away from the target hub set. Status: **PROVED_ANALYTIC**.

### Counterexample attack: high-incidence trap

An explicit one-color abstract block system was constructed for every (r\ge8):
- six 6-blocks, one singleton, one 4-block, and (r-8) 5-transversals;
- target-group sizes exactly ((r,r,r,r,r+1));
- repeated-group incidence (d_i=6);
- ideal excess (Delta_i=11), six deleted repeated-group edges and four added cross-block edges;
- actual color slack (s_i=9), edit distance (10), size energy (23), and (\alpha(G_i)\le r).

The singleton label is 1; the 4-block has labels 2,3,4,5; their four cross edges block every ((r+1))-set that doubles a missing repeated-group pair. The six repeated pairs can all be placed outside (X).

This is **not** a full terminal coloring: other colors, target cross-cover, and global pair-disjointness have not been completed. It does disprove the naive local inference that scalar stability and a one-color independence condition alone force every non-target defect to touch (X). Up to (lfloor(8r+5)/9\rfloor=\Theta(r)) such patterns fit the scalar non-target slack bound, so the high-incidence regime cannot be discarded by budget rhetoric alone.

### New assets and commits

- `HUB_PROPAGATION_THEOREM.md`: HP-LI proof and explicit high-incidence obstruction. Commit: `ac5dbeb393a661a85a13e3b24e74a2a2933f520b`.
- `MULTICOLOR_DEFECT_BUDGET.md`: exact per-color ledger and global defect accounting. Commit: `085d81cf4c5868784e231ceacd4396b84c9988b9`.
- `ROBUST_EXACT_CORE.md`: exact-core boundary and missing interface theorem. Commit: `99d8d3afb51a0bca18f4abd7dbd5424d6d81a816`.
- `NONEXTENSION_CLOSURE.md`: exact cross-pair budget and nonextension blocker. Commit: `f6e2cf8ae9dec20a8153c22b9dc6a9a3024d8d54`.

### Current blocker

The remaining task is a **global pair-disjointness / trap-completion inequality**: rule out a linear family of (d_i\ge6) local traps after enforcing that every cross-group pair has exactly one actual color, target cross edges are unavailable to non-target colors, and target internal deletions are a finite resource. Alternatively, construct a globally compatible family. No such inequality is proved yet.

### Status

- D1: conditionally reached as before.
- Low-incidence part of D3: **PROVED_ANALYTIC**.
- Full Hub Propagation: **OPEN**.
- Exact-core route: **OPEN**.
- Robust nonextension D4: **OPEN**.
- No sufficiently-large-(r) closure is claimed.


## 2026-10-24 — mandatory correction after adversarial audit

This section **supersedes the preceding initial Hub Propagation claim**.

### Withdrawn claims

1. The unconditional claim `d_i<=5 => (6-d_i)(r-1)` edits for every off-hub repeated pair is **DISPROVED as stated**. Its proof incorrectly assumed that every selected same-group pair is target-colored, overlooking hub-incident target deletions and blocks with no ordinary point of a given target group.
2. The proposed (d_i=6) singleton/4-block pattern was not a valid (\alpha(G_i)\le r) example: an independent set can double two missing repeated-group pairs and omit the special cover block. It is withdrawn.
3. Therefore the prior statement “at most 27 colors have a low-incidence off-hub pair” is withdrawn.

### Valid replacement results

- **Conditional ordinary-label cylinder lemma:** if some (k\ne j) has a point in (B_k\setminus X) in every block other than the block containing the missing pair (uv\subset B_j\setminus X), then (|E(G_i)\triangle E(Q_i)|\ge r-1). This proof is valid because every selected same-group pair is target-colored.
- **K6 exclusion:** since (\alpha(G_0)\le5), every non-target color graph (G_i) is (K_6)-free. Hence a full star from a vertex to a clean 5-clique ideal block is forbidden.
- **Cheap local one-color cover audit:** a (d_i=1) ideal partition with one repeated pair (uv) can be made (\alpha(G_i)\le r) at constant cost by joining (u) to a whole transversal block. But then (u\cup C\) is a (K_6) in (G_i), violating the full target-α contract. This is not a full-terminal counterexample; it identifies the missing joint constraint.
- **Exact budget identity:** (A=9r+5-\Delta_0+D-S_{\rm non}), with (A) target cross edges, (D) target internal deletions, and (S_{\rm non}=\sum_{i>0}s_i).

### Current blocker

The genuine next theorem is a **defect-chain cost theorem**: any one-block cylinder cover must create another defect to avoid a (K_6); that defect needs its own cover. Prove that the resulting chain/cycle exceeds the combined (O(r)) non-target slack and target cross-cover budget, counting each pair once. The current work does not yet prove that lower bound.

### Corrected asset commits

- Corrected `HUB_PROPAGATION_THEOREM.md`: `4c9c9b38d5e05b47108638cae1cfd93a10775c09`.
- Corrected `MULTICOLOR_DEFECT_BUDGET.md`: `d73eaecb8abc865751177ec6f79c97e2afc2474e`.
- Corrected `ROBUST_EXACT_CORE.md`: `4a12f2eb296393a86437b2c6eed6d6cbfe26dfc2`.
- Corrected `NONEXTENSION_CLOSURE.md`: `86405ff8a9a1aa5c7a3b050645d58b7db2d68318`.

Current status remains: full Hub Propagation **OPEN**; exact-core route **OPEN**; robust nonextension **OPEN**. No general-r terminal closure is claimed.


## 2026-10-24 — exact two-defect closure and target-label audit

### New rigorous local construction

Added an explicit one-color block gadget:
- one 6-block (C=K_6-uv);
- one 5-block (D=K_5-wx);
- (r-2) further clean (K_5) blocks;
- nine cross-block edges, listed in `HUB_PROPAGATION_THEOREM.md`.

The verification checks:
- (\alpha(G_i)\le r), including independent sets doubling both defective blocks;
- (K_6)-freeness by enumerating possible distributions of a 6-clique across (C,D);
- exact counts (R_i=2,A_i=9,s_i=7), edit distance (11).

This is only an abstract one-color block system; target-group labels and global edge ownership are not completed. It shows the local (alpha\le r)+(K_6)-free conditions alone do not force a third defect or a per-color slack (>8).

### Target-label obstruction

If a target hub (w\in B_j) has a target cross-star into (B_k), and (x\in B_k) lies in the same non-target ideal block as (w), then (wx) is a target-colored edge absent from that non-target color. For any other block's ordinary point (z_k\in B_k\setminus X), both (wz_k) (target star) and (xz_k) (ordinary internal target edge) are target-colored. Thus (z_k) cannot connect to either endpoint in the non-target color. A cover using only the block-to-block edges must use a hub in that group; otherwise it must invoke a multi-block barrier or another target-internal deletion.

### Multi-block barrier audit

For a fixed vertex (z), two clean (K_5) blocks (E,F), and nonneighbors (e\in E,f\in F), the 9-edge pattern (z\) to (E\setminus\{e\}), (z\) to (F\setminus\{f\}), plus (ef), blocks every choice from (E\times F) while remaining locally (K_6)-free. Hence “a blocked coordinate forces a hub” is false without restricting the allowed cross-block edges.

### Interpretation and blocker

The earlier informal defect-chain slogan is too strong. A pair of defects can close at slack 7 in the abstract local model. The full terminal may still be impossible because the target labels and unique color ownership forbid repeating these gadgets globally, but that needs a new theorem.

The current headline gap is now:
> **Target-labelled global cover inequality:** lower-bound the total cost of all hub-block defects and multi-block barriers across (r-1) colors, enforcing the exact target star labels, internal deletion set, and unique edge ownership.

### Asset commits

- `HUB_PROPAGATION_THEOREM.md`: `9cb35aa9c56ec46ad4060adebb45cdd47d78b019`.
- `MULTICOLOR_DEFECT_BUDGET.md`: `7f07536987f2596e785c1b9ccc01635ccf430061`.
- `NONEXTENSION_CLOSURE.md`: `4c985aacea3ebf48f61461ddef7baeae46e89190`.
- `CANONICAL_STATE.md`: `d3dff82ce38e7016e04915278132bf5578f629fd`.

Full Hub Propagation, exact core, and robust nonextension remain **OPEN**. No global counterexample or general-r closure is claimed.


## 2026-10-24 — target-star permutation constraint

### Conditional symbolic theorem

Under the canonical hub-star regime, each of the five target groups has a hub (a_j), an internal target nonneighbor (y_j), and a full target cross-star to (B_{f(j)}), with (f(j)\ne j). The target independence cap (\alpha(G_0)\le5) forces
[
\boxed{f\text{ is a derangement permutation on the five groups}.}
]
Proof: if two distinct groups (j,k) target-star to the same group (ell), select the two internal nonedges (a_jy_j,a_ky_k), omit (B_\ell), and choose one ordinary point from each of the two remaining groups. The resulting six-set has no target edge.

If the oversized group has a second hub (b_h) with its own internal nonneighbor and full target star, its destination must equal (f(h)); otherwise the same collision construction applies to (b_h) and the hub from the group mapping to that destination.

Status: **PROVED_CONDITIONAL** on the canonical full-star model. Under the current explicit target-hub bounds, ordinary representatives exist for all sufficiently large (r).

### Triangle obstruction

The two hubs in the oversized group must be target-adjacent: if they were nonadjacent and share destination (B_{f(h)}), they plus an ordinary point in that group and one point from each of three groups outside ({h,f(h)}) would form a target-independent 6-set.

If both oversized-group hubs and their common destination representative lie in the same non-target ideal block, their three pairwise edges are all target-colored, so they form an independent triple in that block. In a single-cover-block correction model, omitting the cover block and choosing one point from each other block yields an independent ((r+1))-set. Therefore that configuration requires either:
- the two hubs be split across ideal blocks;
- the block containing both hubs omit the common destination group (a nontransversal defect); or
- at least a multi-block cover network, whose cost remains OPEN.

### New implication

The target cross-correction map cannot be an arbitrary star cluster. It must be a 5-cycle or a disjoint 2-cycle plus 3-cycle at the group level. This excludes the cheapest target-star clustering pattern and gives a finite structural state space for the next hub-block incidence classification.

### Asset commit

- `HUB_PROPAGATION_THEOREM.md`: `0c00f7715f84e7ea776e0059eed34d265d908c4d`.

The abstract two-defect gadget from the previous pass remains valid only without target labels; it is not a global terminal counterexample. Full Hub Propagation and robust nonextension remain **OPEN**.


### Follow-up asset synchronization — target-star constraint

- `HUB_PROPAGATION_THEOREM.md`: `0c00f7715f84e7ea776e0059eed34d265d908c4d`.
- `CANONICAL_STATE.md`: `c130416dcd08dea33d2f3d02618bc9b1b88c879b`.
- `NONEXTENSION_CLOSURE.md`: `66f7207947aad4d2e713ac9e8c34d76da36570b6`.
- `MULTICOLOR_DEFECT_BUDGET.md`: `155dc60bafa978342444c7dcb06e685eebba7e7f`.

The full-star permutation result is conditional on the target-star reduction; no claim is made that every terminal has already been reduced to that form. The target-star block triangle obstruction is also conditional on the single-cover-block model. These restrictions are now explicit in the canonical state and nonextension analysis.


### Exactness qualification for the destination map

The destination-injectivity lemma has been tightened: it assumes the **exact hub-star model**, meaning every target cross-group edge is contained in the specified stars and there are no extra target cross edges that could hit the witness six-set. The current (O(r)) target cross-edge budget does not by itself prove exactness. A robust version allowing exceptional cross edges remains OPEN.

Corrected commit:
- `HUB_PROPAGATION_THEOREM.md`: `8f99c7c48fab62810930253fe27903f2db5bfd75`.
