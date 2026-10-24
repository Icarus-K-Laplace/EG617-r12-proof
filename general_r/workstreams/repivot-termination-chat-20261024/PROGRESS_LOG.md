# Progress Log — General-r Repivot Termination

Branch:

`workstream/general-r-repivot-termination-20261024`

Isolation:

only `general_r/workstreams/repivot-termination-chat-20261024/` is authoritative for this chat's new general-r termination results. Upstream front extraction and anchor-excess proof are not reopened.

---

# 2026-10-24 — Canonical endpoint package

## Results 1–14

Certified before the distinct-support audit:

1. `Delta K=-2 Delta q`; closed non-improving cycles are q/tau-flat.
2. d3 eliminated under A+B plus declared low-charge assets.
3. high owners `d>=r-2` number at most three.
4. high endpoint <=9 shell-kernel vertices / <=8 core signatures.
5. d2 `W=K+2r-2+a+b`; three one-loss common-hub classes imply `K+a+b>=r`.
6. d0 neutral symmetry.
7. d1 exact one-point exchange.
8. shell-incidence identity `t_s=d_M(s)+g_s=e_F(s,H)`, `sum t_s<=6r-2`.
9. d1 <=5 shell classes; d2 support universe <=6 shell vertices / <=15 pair classes.
10. all low regular owners form a target clique; total low-owner count <=r-2.
11. fixed-class d2 plateau: only fully decorated shell pair `S subset X` can scale at equal q.
12. exact repeated-class exchange duality.
13. genuine third coordinate `zeta`; exact involution `(m,zeta)->(zeta+1,m-1)`.
14. balanced repeated-class capacity and Balanced Two-Chamber Correction Theorem.

Representative commits:

- `6cdf26de92f9b3c656f4f89799ecb3490f7836af` potential baseline
- `c93345b91d1f4c5bb90ffe328c2aef811e24dc86` high three-owner theorem
- `009a618b431adbc162b22792d05d8b59770b873a` six-point shell theorem
- `4e84810280a91bed3b1feb4487bc348bf1625400` fixed d2 class theorem
- `ea26065301a37d7ab7daed8813c75c4aa843209c` zeta coordinate
- `3776325f7b6591722e79fbadf62ef8cbf908d4eb` balanced two-chamber theorem

---

# Audit correction — global alpha cap

The backend has

`alpha(F)<=4`,

while only legal cores satisfy

`alpha(H)<=3`.

Therefore any argument forbidding an independent 4-set in the full graph F is invalid.

Two earlier claims are retained only as negative audit certificates and are **not canonical**:

- `D2_MISSING_PAIR_NEUTRAL_BOUND.md`: the claimed bounds `kappa(D)>=zeta-1`, `a>=zeta` are not proved;
- `D2_DISTINCT_MATCHING_COLLAPSE.md`: the allowance-independent `nu(Q)<=3` / six-hub collapse is disproved as stated.

No current theorem uses these claims.

---

# Distinct-support d2 audit package

## Result 15 — exact correction dictionary

For two same-shell d2 owners with supports `D_i,D_j`, repivot through `D_i` gives

> `d_i(y_j)=2-|D_i intersect D_j|`.

Thus repeated / one-overlap / disjoint supports become d0 / d1 / d2 transitions.

Status: `PROVED_SYMBOLIC`.

## Result 16 — low-allowance distinct d2 reduction

For a neutral-free fully decorated distinct d2 plateau:

- `a=0`: at most3 supports;
- `a=1`: earlier coarse bound12 is sharpened to **at most9** supports;
- `a>=2`: `nu(Q)(a-1)<=W<=4r+9-a`;
- `a=2`: at most3 zero-weight support vertices; the zero-free `(1,1)` target-support graph has maximum degree3.

Status: `PROVED_CONDITIONAL`.

Source theorem: `D2_DISTINCT_SUPPORT_REDUCTION.md`, sharpened by `PLATEAU_DISTANCE_COMPRESSION.md`.

---

# 2026-10-24 — Round 2: plateau-distance compression

## NEW RESULT 17 — exact fourth potential coordinate eta

Define

`eta(p)=#{regular d1 owners x : (q_x,tau_x,zeta(x))=(q_p,tau_p,zeta(p))}`.

Then

> **`Phi_4=(q,tau,zeta,eta)`**

is a genuine bounded lexicographic potential.

For one neutral-free distinct d2 common-S plateau, let `G_S` be the support-intersection graph. One-point overlaps become d1 plateau transitions, hence

> `eta(p_D)>=deg_(G_S)(D)`.

At a `Phi_4`-maximal pivot,

> **`Delta(G_S)<=eta`.**

Therefore the class contains a pairwise-disjoint support subfamily of size at least

> **`ceil(N/(eta+1))`.**

Status: `PROVED_SYMBOLIC`.

Main commit:

`0b7bfbb3808ddcee147aceedb2683c98623748af`.

Potential promotion:

`5a8f900c2495af6840e0a484e32f9540357464e6`.

## NEW RESULT 18 — d1 scale transfer

The eta population is distributed among at most five d1 shell classes. One class has

`N_1>=ceil(eta/5)`.

In the neutral-free plateau slice its singleton supports are distinct. If c is its allowance, then under the inherited core cap `K<=2r-2`,

> **`(N_1-1)c<=3r-2`.**

If `c=0`, row closure gives `N_1<=3`.

Thus linear eta forces a linear d1 class with absolute-constant allowance.

Status: `PROVED_CONDITIONAL`.

## NEW RESULT 19 — asymptotic low-endpoint compression

If a fixed distinct d2 plateau has `N=Omega(r)`, then

- either `eta=Omega(r)`, which transfers to a linear bounded-allowance d1 class;
- or `eta=o(r)`, in which case the extracted disjoint matching tends to infinity and the d2 allowance satisfies `a=o(r)`.

Hence a scalable d2 plateau cannot simultaneously have

- linear owner multiplicity,
- linear allowance,
- and sublinear d1 correction population.

Status: `PROVED_CONDITIONAL`.

---

# 2026-10-24 — Round 3: allowance-2 rigid terminal

## NEW RESULT 20 — Allowance-2 Clean Pair-Exchange Orbit

Take any pairwise-disjoint q-flat `a=2` d2 subfamily.

At most three supports contain a zero-weight endpoint. Every other support is a clean target K2 with endpoint weights `(1,1)`.

Repivot through one clean block `D_i`. Every other disjoint clean block `D_j` remains

- d2;
- q/tau/zeta-flat;
- a target K2;
- endpoint weights exactly `(1,1)` relative to the new shell pair `D_i`.

The old shell pair becomes one reverse support of exactly one of three symbolic types:

- clean `(1,1)` target K2;
- `(0,2)` target K2;
- `(0,1)` target nonedge.

Between two clean blocks, row closure makes the target cross graph a matching of size0,1,or2.

Since the `(1,1)` support graph has maximum degree3, every unbounded a=2 branch contains an unbounded clean matching subsystem, and every linear-size branch contains a linear-size one.

Therefore the scalable a=2 blocker contains the rigid design terminal

> **clean pair-exchange design + O(1) zero-containing special blocks.**

Status: `PROVED_CONDITIONAL`.

Main commit:

`f9a75635987fcf84217b91084b3e9979108cbffb`.

Canonical promotion:

`b4b9c92709470b3f6f2b9b77ac50e4e119bf9c0b`.

Termination theorem promotion:

`b88507029e9ffd71f053f95fa3bc58d7106354d8`.

---

# Current canonical endpoint inventory

- medium `4<=d<=r-3`: impossible;
- d0: quotient-neutral;
- d1: <=5 shell classes; linear eta implies bounded-allowance d1 concentration;
- d2 shell side: <=6 support vertices / <=15 classes;
- d2 non-fully-decorated plateau: absolute q-flat bounds;
- repeated fully-decorated d2: zeta improvement or Balanced Two-Chamber terminal;
- distinct fully-decorated d2:
  - `a=0`: N<=3;
  - `a=1`: N<=9;
  - `a=2`: scalable part contains a clean pair-exchange design;
  - higher allowance: weighted matching + eta scale compression;
- d3: eliminated;
- high endpoint: <=3 owners, finite bounded-complement skeleton.

# Potential status

Current preferred potential:

> **`Phi_4=(q,tau,zeta,eta)`.**

All four coordinates are genuine bounded integers.

`Q2=sum kappa^2` is now the candidate fifth coordinate, especially on the clean pair terminal.

# SCALING

Shell-side endpoint type count is absolute-constant in r.

Repeated correction cycles are two-state.

Distinct d2 overlap is paid for by eta/d1 population.

The first genuinely scalable allowance level is now represented by one rigid local rule: clean K2 blocks with matching cross graphs, closed under pair exchange.

# MAIN-THEOREM IMPACT

The backend has advanced from "fixed-width shell cases" to a genuine four-coordinate potential plus an extracted scalable design terminal.

No all-large-r contradiction is certified yet, but arbitrary `a=2` support graphs are no longer the headline object.

# NEXT SINGLE BLOCKER

> **Clean Pair Nonextension Theorem:** rule out a sufficiently large repivot-closed clean K2 block system with matching cross graphs and no independent 4-transversal, or prove a strict fifth-coordinate improvement on it. The same mechanism should absorb the bounded-allowance d1 concentration forced by eta.

---

# 2026-10-24 — Round 4: clean-pair model, AES reduction, and terminal audit

## Result 21 — Exact block graph / 2-SAT model

Added CLEAN_PAIR_GRAPH_MODEL.md. Every block pair is one of seven partial matchings of K2,2. A selected endpoint transversal is independent exactly when its 2-CNF is satisfiable.

Exhaustive finite audit checked all 7^6 = 117,649 labelled four-block patterns and all 16 assignments per pattern. An unsatisfiable four-block restriction needs at least six target cross edges; 160 labelled patterns attain this minimum. This is a local finite result, not an all-r theorem.

## Result 22 — High-density AES reduction

Added CLEAN_PAIR_NONEXTENSION.md. For U the union of m clean blocks, G=overline(H[U]) is K4-free and

delta(G) >= max(m-1, 2m-r-2).

For m >= ceil(4r/3+3), the Andrasfai-Erdos-Sos theorem makes G 3-partite. Thus U is covered by three target cliques and m <= floor(3(r-1)/2). The surviving interval remains linear and nonempty.

Status: PROVED_CONDITIONAL. Clean Pair Nonextension itself remains OPEN.

## Result 23 — d1 terminal exact transition

Added D1_TERMINAL_ABSORPTION.md. A fixed singleton class of allowance c and multiplicity N is closed under one-point exchange, with

kappa'_{u_j}=c-e_H(u_i,u_j), w'_{u_j}=c.

Known bounds: c=0 implies N<=3; c>=1 implies N<=r-2; (N-1)c<=3r-2. Linear eta forces c=O(1), but not N=O(1).

Status: exact transition / scale transfer PROVED_CONDITIONAL; final d1 absorption OPEN.

## Result 24 — Q2 universal-monotonicity claim retracted

Added FIFTH_COORDINATE_AUDIT.md. The exact Q2 increment is retained, and clean endpoints contribute a_z-b_zi. No sign follows from the clean weight equation.

More decisively, a reversible Phi4-flat repivot has a Phi4-flat reverse move and the Q2 increments have opposite signs. Therefore “every nontrivial Phi4-flat move strictly increases Q2” is DISPROVED_AS_STATED. Q2 may select a maximal representative but cannot itself eliminate the terminal.

## Result 25 — canonical closure ledger

Added TERMINATION_CLOSURE.md and promoted the exact statuses to CANONICAL_STATE.md and TERMINATION_THEOREM.md. The previous a=1 d2 bound was also reconciled: the canonical bound is N<=9, not the older coarse 12.

Actual commits in this round:

- D2 allowance-one audit: cb7e273cba267e35b56303047a80101572ca6ac0
- CLEAN_PAIR_GRAPH_MODEL.md: c5f6a275d2ac47af94474751a785d410af06fb8b
- CLEAN_PAIR_NONEXTENSION.md: 2ab7ef93e92c9a50ee19a864855daf761af1a4a9
- D1_TERMINAL_ABSORPTION.md: 122dac7a970be5d9139bd89e4fe47e3283f54304
- FIFTH_COORDINATE_AUDIT.md: 0972805e9eceaad2ec415853cb85423785dab592
- TERMINATION_CLOSURE.md: 9001213208e298a229b99a41b59d7ade56f96a27
- CANONICAL_STATE.md promotion: 60bd693fa33a5c33d1db0db5254d1fa700c3db2c
- TERMINATION_THEOREM.md promotion: 9eba15de98a3c32186bea7b8b1db9bcaa80e11ee

## Current outcome

C-N1 is partially achieved. C-N2, C-N3, C-N5 and C-N6 remain OPEN. The proposed universal C-N4 strict-Q2 route is DISPROVED_AS_STATED. No new all-large-r contradiction and no finite r0 are certified.

Next useful work: derive a no-double-counting inequality coupling U, the outside core H\\U, the old shell-pair incidence total 2r+b, and the global excess cap. Do not enlarge the case tree without such an inequality.


### Round 4 follow-up audit

The block-model verifier is now embedded in CLEAN_PAIR_GRAPH_MODEL.md. The signed full-matching subcase was clarified: the triangle-parity graph must be triangle-free, because a parity-1 triangle would produce an independent transversal on four blocks.

The canonical blocker language was corrected: universal strict Q2 increase is not merely unproved; it is impossible on every reversible Phi4-flat edge. Q2 may remain a tie-breaker, but terminal elimination must be structural or use a genuinely directed operation.

Follow-up commits:

- embedded exhaustive verifier: 4424460ddb23d53b4ded7a056c528d34a47002e2
- signed-parity wording audit: d9641f2a2e07817c2ed9f0cecf8c2246639ff291
- canonical Q2/blocker correction: 02d644bf5dafce51a7572146c8fbae6f85391c09
- termination theorem Q2/blocker correction: 2439aa8a0d45f184fc5fc6286d96292a8df2f6da

No all-large-r contradiction is certified.


Allowance-one summary audit follow-up: the final summary line in D2_DISTINCT_SUPPORT_REDUCTION.md was also corrected from 12 to 9. Commit: d7fde7ad56f90288e0c2e19f70f6f78eaf0eeda0.

The final CLEAN_PAIR_GRAPH_MODEL.md blob includes the embedded exhaustive checker and signed-parity wording audit (latest content commit d9641f2a2e07817c2ed9f0cecf8c2246639ff291).
