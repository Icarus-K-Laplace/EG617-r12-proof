# Progress Log — Asymptotic Synthesis

## 2026-10-24 — Round 1

### Repository isolation

Created and maintained only:

`workstream/general-r-asymptotic-20261024`

under

`general_r/workstreams/asymptotic-chat-20261024/`.

### First synthesis package

Established:

1. exact conservation law
   `K=6r+6-2epsilon-2q`, equivalently `q+epsilon=3r+3-K/2`;
2. parity: K is even, so `K>=7` is equivalent to `K>=8`;
3. generic medium-degree threshold `r>15-epsilon-K_floor/2`;
4. H_B-free composition for r>=68 using near-anchor reduction plus sibling AES theorem;
5. certified small-r-only pathology list;
6. d2 scalar bottleneck `K+a+b>=r`;
7. high endpoint bounded kernel: <=3 owners, <=9 shell kernel, <=8 core signatures;
8. fixed-deficit decoration-heavy interface `tau>=r/2-O_epsilon(1)`.

### Major sibling sync: residual contract closed for r>=17

Residual-extraction sibling head:

`07cd8fb58ffd93d234b1e8b6104f939175d7fbda`.

New theorem imported:

> For every r>=17, once an induced `4r+1` residual F satisfies `alpha(F)<=4`, `omega(F)<=r-1`, and the inherited least-colour cap, then `delta(F)=r+1`; a degree-(r+1) pivot exists; its core H has `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Consequences for synthesis:

- the old core-certification part of H_A is removed;
- H_A is weakened to `H_A^ext`: **extract 4r+1 residual or controlled 5r+1 design terminal**;
- numeric r0 stays 68 because 17<68;
- this is nevertheless a strict theorem-strengthening because one load-bearing hypothesis disappears.

### Three-anchor latest sync

Latest checked head:

`a98ef900be419993e3fe63d37a0cf82fa104c455`.

It adds further constant connector-skeleton analysis, but the global theorem remains:

- proved for r>=68;
- open as a complete theorem for 12<=r<=67.

Therefore r0 does not change this round.

### Design sibling latest sync

Latest checked head remains:

`578830ff3fd9eab94f2bb5a498d90a1a303ba2e1`.

No robust `5r+1` classification theorem has yet replaced H_D.

### Current strongest theorem

**S68-v2 — CONDITIONAL_ON_Aext_C*_D + ASYMPTOTIC_ANALYTIC**:

for every r>=68,

`H_A^ext(r)+H_C*(r)+H_D(r) => P(r)`.

Neither exact residual-core minimum-degree certification nor H_B is assumed.

### Current blocker ranking

1. upstream extraction A_ext;
2. endpoint C*, especially scalable d2 and d0/d1;
3. robust design stability D;
4. three-anchor below 68 only lowers r0.

### Next highest-leverage asymptotic inequalities

Backend:

`K+a+b>=r`

for surviving three-class one-loss d2. Target any upper bound

`K+a <= (1-c)r+O(1)`

with c>0.

Potential/design interface:

`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`

and

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.

Goal: strict tau improvement unless decoration incidences collapse to a bounded-parameter design.


## 2026-10-24 — Round 2: shortest route, d2 boundary audit, C/D interface

### 1. New shortest conditional route

Replaced the primary synthesis DAG by the near-anchor route:
\[
A_{\mathrm{ext}}^*(r)\land D_{\mathrm{low}}(r)\Longrightarrow P(r),
\qquad r\ge67.
\]
This route kills the (4r+1) branch by the contextual ((k,s)=(4,1)) cap and bypasses (C^*), (H_B), and broad (H_D). It is still conditional; (A_{\mathrm{ext}}^*) and (D_{\mathrm{low}}) remain OPEN.

### 2. Imported high-layer closure

Checked current architecture branch head a922c4d7646eb8d0087bde8547562c8aace02ee2 and imported:
- Cell B high-layer exclusion for (|W|=2r-1), (delta=r+1), (r\ge16), relative to Brouwer second-Turán and the Cell-B normal form;
- Cell A high-layer exclusion for (|W|=2r-1), (delta=r+1), (r\ge25), relative to the sharp non-bipartite triangle-free extremal theorem and Brouwer second-Turán.

This closes the **high-degree top-layer interface**. It does not close the low-degree (delta=r, |W|=2r-1) case; that case is explicitly retained in (D_{\mathrm{low}}).

### 3. d2 scalar inequality adversarial audit

For even (r\ge68), froze the scalar boundary family
\[
\epsilon=0,\ a=2,\ b=0,\ K=r-2,\ B=r/2+4,\ q=5r/2+4.
\]
It satisfies:
- (q+\epsilon=3r+3-K/2);
- (q=2r-2+a+B);
- (W=K+2r-2+a+b=3r-2);
- (K=2r+10-2a-2B);
- (K+a=r).

Conclusion: (K+a\le(1-c)r+O(1)) cannot follow from the existing scalar ledger. This is not a graph counterexample; the route needs a new structural exclusion of the scalable a=2 terminal.

### 4. Owner-demand/capacity audit

The exact common-S owner capacity is
\[
N\le\left\lfloor\frac{r-3+2\epsilon+\epsilon\sqrt{4\epsilon+1}}2\right\rfloor
= r/2+O_\epsilon(1).
\]
No theorem currently forces (N>(1/2+c)r-O_\epsilon(1)). The owner-demand route remains OPEN.

### 5. Common C/D transversal-cover lemma

Added a weighted transversal-cover lemma with two exact forms:
- every transversal of disjoint groups hits an edge implies (sum e(B_i,B_j)/(|B_i||B_j|)\ge1);
- a fixed nonedge pair plus one point from each of s groups, under (alpha(G)\le s+1), gives the defect-pair version.

The clean-pair 2-SAT audit strengthens its four-block instance to six cross edges; the TD(5,r) instance yields the existing cylinder lower bound and bounded-hub concentration. The mapping is rigorous at the transversal-cover level only; no unsupported identification of the full C and D objects is made. The lemma does not yet prove clean-pair nonextension or global TD defect-chain cost.

### 6. Current blockers and provenance

- (A_{\mathrm{ext}}^*): OPEN; residual extraction branch head 7a4fb4c37cefec8d801fc7deb778568bfb24002e.
- (D_{\mathrm{low}}): OPEN; design-terminal branch head 5b4162c239d3dfad84d130c3015a0db5919228c4.
- C clean-pair endpoint: OPEN; repivot branch head 35fec3eaaab70b31e10b41065634b35b02a28e6c.
- Contextual cap plane and direct near-anchor route: architecture branch head a922c4d7646eb8d0087bde8547562c8aace02ee2.

No unconditional all-large-r theorem was obtained. Unconditional r0 remains NOT CERTIFIED.
