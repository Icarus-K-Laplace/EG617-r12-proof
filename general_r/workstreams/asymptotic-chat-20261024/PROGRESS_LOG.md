# Progress Log — Asymptotic Synthesis

## 2026-10-24 — Round 1

### Repository isolation

Created branch:

`workstream/general-r-asymptotic-20261024`

from architecture head `3dc54c38e13a71e8a12330c3c36b1aa1063aacaa`.

Only this workstream directory is modified.

### Imported sibling state

1. Three-anchor sibling commit `0c226d78e39e3da2a594f8a6121a864d2efa09ea`:
   - exact three-anchor excess `K>=8` proved analytically for all `r>=68`;
   - threshold is exactly the AES inequality `2r-9>5(3r-1)/8`.

2. Repivot sibling commit `2974fd80882a4545a3a1a569418405ec4e3bdebc`:
   - d3 common-S endpoint closed;
   - high endpoint strengthened to at most 3 total owners;
   - shell high-interaction kernel at most 9;
   - at most 8 core incidence signatures;
   - d2 exact one-loss identity `W=K+2r-2+a+b`;
   - three-class d2 terminal requires `K+a+b>=r`.

3. Architecture fixed-deficit multicolour stability:
   - owner/regular-clique capacity has slope 1/2 for fixed epsilon;
   - d3 contradiction threshold `r>11+epsilon sqrt(4epsilon+1)`.

4. Exact affine-plane model:
   - nonextension by one vertex is already proved; the open design task is stability/classification, not the final exact extension contradiction.

### New synthesis results in this workstream

#### S1. Exact q-deficit conservation law packaged

With `epsilon=D_r(4r+1)-e(F)`,

`K=6r+6-2epsilon-2q`,

hence

`q+epsilon=3r+3-K/2`.

Also K is always even.

This immediately implies that a hypothetical `K>=7` theorem is identical to `K>=8`.

#### S2. General endpoint-collapse threshold

If `K>=kappa`, every medium degree disappears once

`r>15-epsilon-kappa/2`.

Worst-case thresholds:

- K>=2: r>=15;
- K>=4: r>=14;
- K>=6: r>=13;
- K>=8: r>=12.

Therefore exact anchor excess is not required merely to get bounded endpoint width.

#### S3. First H_B-free infinite-family composition

For every r>=68,

`H_A(r)+H_C*(r)+H_D(r) => P(r)`.

Proof: if `K<=7`, parity gives `K<=6`; near-anchor reduction gives exact degree-r anchors; sibling AES theorem forces `K>=8`. Hence H_B is derived rather than assumed. The residual then has `q<=3r-1` and enters the already reduced endpoint family.

Status: **CONDITIONAL_ON_A_C*_D + ASYMPTOTIC_ANALYTIC**.

This is not an unconditional solution.

#### S4. Certified small-r-only states

- concentrated d2 `K=8,a=3,b=1` three-class state: only `r<=12`;
- d4 / d=(r-3) medium states: gone for r>=15 from baseline K>=2, and for all r>=12 under K>=8;
- four high owners: slope contradiction for r>=13; r=12 equality separately closed;
- balanced `(r+1,r+1,r+1)` near-anchor coarse exception: only r=12;
- d3 common-S: globally closed under A+B, not an asymptotic pathology.

#### S5. d2 resource-split target

Every one-loss three-class d2 terminal must satisfy

`K+a+b>=r`.

Hence a sufficiently-large-r closure follows from any uniform theorem

`K+a <= (1-c)r+O(1)`

with c>0, or from a majority owner-demand theorem beating the multicolour slope-half capacity.

### Cross-workstream update during this round

A new architecture-side theorem appeared at commit `578830ff3fd9eab94f2bb5a498d90a1a303ba2e1`:

- low-endpoint regular shell vertices form one regular target clique;
- fixed-deficit multicolour stability bounds that clique by roughly r/2;
- high regular vertices are O(1);
- therefore a fixed-deficit shell is decoration-heavy.

Combining that theorem with the stronger sibling bound `|R_high|<=3` improves its decoration lower bound to

> **`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon this is

> **`tau >= r/2-O_epsilon(1)`.**

This is the next potential/rigidity interface: a terminal shell must contain linearly many decorated vertices, so any no-improvement state must organize a linear decoration incidence system.

### Current blocker ranking

1. H_A front extraction/core certification;
2. H_C* d2 plus d0/d1 and bounded-high terminal closure;
3. H_D robust design stability/nonextension;
4. three-anchor below 68 only affects r0, not existence of an asymptotic theorem conditional on A/C*/D.

### Next highest-leverage inequality

Try to convert the decoration-heavy estimate

`tau >= r/2-O_epsilon(1)`

and exact transport

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`

into a strict repivot improvement unless decoration incidences form an O(1)-parameter design. In parallel, attack d2 through the scalar target `K+a <= (1-c)r+O(1)`.
