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