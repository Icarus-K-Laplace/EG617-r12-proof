# Progress Log — General-r Repivot Termination

## 2026-10-24 — Round 1

Branch:

`workstream/general-r-repivot-termination-20261024`

Only

`general_r/workstreams/repivot-termination-chat-20261024/`

was modified. Upstream front extraction and anchor-excess proof were not reopened.

---

## Results 1–10 — endpoint compression package

Certified this round:

1. `Delta K=-2 Delta q`; closed non-improving cycles are q/tau-flat.
2. d3 eliminated under A+B plus declared low-charge assets.
3. high owners `d>=r-2` number at most three.
4. high endpoint <=9 shell-kernel vertices / <=8 core signatures.
5. d2 `W=K+2r-2+a+b`; three one-loss support classes imply `K+a+b>=r`.
6. d0 neutral symmetry.
7. d1 exact one-point exchange.
8. shell-incidence identity `t_s=d_M(s)+g_s=e_F(s,H)`, `sum t_s<=6r-2`.
9. d1 <=5 shell classes; d2 support universe <=6 shell vertices / <=15 pair classes.
10. all low regular owners form a target clique; total low-owner count <=r-2.

Earlier key commits:

- `6cdf26de92f9b3c656f4f89799ecb3490f7836af` potential baseline
- `c93345b91d1f4c5bb90ffe328c2aef811e24dc86` high three-owner theorem
- `009a618b431adbc162b22792d05d8b59770b873a` six-point shell theorem
- `a62a6f132095b3d389710964297415bfdf6adf6f` initial fixed-width termination theorem

---

## Result 11 — Fixed-Class d2 Plateau Skeleton

For one fixed d2 shell pair S:

`ell=a-[w(D)+mu(D)]`.

If `s=|S intersect X|`:

- s=0: b=0 gives <=3 owners total; b=1 gives <=1 q-flat owner and <=3 strict support types;
- s=1: q-flat support graph has <=3 components, each an isolated edge or <=2-edge star; <=6 q-flat owners;
- s=2: unique regime where q-flat multiplicity can scale.

Therefore only a fully decorated shell pair `S subset X` can support a scalable equal-q d2 system.

Status: `PROVED_CONDITIONAL`.

Commits:

- `4e84810280a91bed3b1feb4487bc348bf1625400` theorem
- `1ebed3f47a300c59ebfaff39991048bbb7ade1b0` endpoint classification
- `267eeb5a3bf7e759e8bf1cae3d672d6051dc034a` canonical promotion

---

## Result 12 — Repeated-Class Exchange Duality

An exact `(S,D)` class of multiplicity m transforms under one owner repivot as follows:

- the other `m-1` owners become d0;
- all old d0 owners become reverse `(D,S)` owners;
- p itself becomes a reverse `(D,S)` owner.

Status: `PROVED_SYMBOLIC`.

Commit: `18fa7cd785313fbd82624041ba81cb78e7bf6b29`.

---

## Result 13 — Genuine third potential coordinate zeta

Define

`zeta=#{regular d0 owners}`,

`Phi_3=(q,tau,zeta)`.

Zeta is bounded and d0-invariant. For a q/tau-flat repeated exact class of multiplicity m,

`zeta(new)>=m-1`.

Hence

> `m>=zeta+2` gives strict `Phi_3` improvement.

At `Phi_3` maximality every q/tau-flat repeated class satisfies

`m<=zeta+1`.

Status: `PROVED_SYMBOLIC`.

Potential commit: `ea26065301a37d7ab7daed8813c75c4aa843209c`.

---

## Result 14 — Balanced repeated-class capacity

A `Phi_3`-flat repeated d2 class has

`m=zeta+1`.

Its owners, the zeta d0 owners and p form a target `K_(2m)`, so

`m<=floor((r-1)/2)`.

If k repeated exact classes simultaneously admit `Phi_3`-flat exchanges,

> `(k+1)(zeta+1)<=r-1`.

Status: `PROVED_CONDITIONAL`.

Commit: `99317c0a29549a07061fbe9d9f4831576f535aa3`.

---

## Result 15 — Missing-Pair / Neutral-Population Bound

For a target-nonedge core pair D,

> `kappa(D)>=zeta-1`.

For a q-flat d2 row with nonedge support,

> `a>=zeta`.

Thus `a<zeta` forces every q-flat d2 support to be a target edge. At `a=zeta`, the nonedge support is a saturated common-nonneighbour equality template.

Status: `PROVED_SYMBOLIC` under standard global alpha/omega caps.

Commit: `123a99b121e0bd4e48bd4be59a54c84c61edf9cd`.

---

## Result 16 — Balanced Two-Chamber Correction Theorem

The zeta-balanced repeated correction-cycle branch collapses completely modulo d0 relabelling.

Let a `Phi_3`-flat repeated exact d2 class have multiplicity

`m=zeta+1`.

Define

`C_0={p} union Z_0(p)`,

`C_1=Y_{S,D}`.

Then

- `|C_0|=|C_1|=m`;
- `F[C_0 union C_1]=K_(2m)`;
- all pivots in C0 represent the same core state H;
- all pivots in C1 represent the same reverse state `H'=(H\D) union S`;
- moves inside a chamber are d0-neutral;
- moves between chambers are the same S/D core exchange.

Therefore, modulo neutral pivot relabelling,

> **the entire repeated correction orbit is the two-state involution `H <--> H'`.**

No long repeated correction cycle remains.

Additional exact invariants:

- forward and reverse d2 allowance are equal: `a'=a`;
- shell/core missing indicators exchange `b <-> mu`;
- exchanged-pair excess obeys
  `kappa_H(D)-kappa_(H')(S)=b-mu`.

Status: `PROVED_CONDITIONAL`.

Main theorem commit:

`3776325f7b6591722e79fbadf62ef8cbf908d4eb`.

Canonical promotion:

`3a575c96b18925744c99fd0c9b9721e575736af3`.

Termination theorem promotion:

`776c7bc566620cb21e5319e5e00ca673f8fd6089`.

---

## Other current canonical commits

- rigid equality inventory: `aad87161e85466baba2bb56b3c1556b06bac7047`
- canonical state before Result 16: `f2536233c1538a390a2a1175c4a9d22953eb60f2`
- canonical state including Result 16: `3a575c96b18925744c99fd0c9b9721e575736af3`

---

# Current canonical endpoint inventory

- medium `4<=d<=r-3`: impossible;
- d0: quotient-neutral;
- d1: <=5 shell classes; final q/tau-flat core exchange remains;
- d2 shell side: <=6 support vertices / <=15 classes;
- all d2 classes with <=1 decorated shell endpoint have absolute q-flat bounds;
- only fully decorated d2 shell pairs can carry scalable q-flat systems;
- repeated fully-decorated branch: either zeta improves, or the branch is the single Balanced Two-Chamber symbolic family;
- q-flat nonedge supports require `a>=zeta` and have a rigid equality boundary;
- d3: eliminated;
- high endpoint: <=3 owners, finite bounded-complement skeleton.

# Potential status

Current preferred potential:

> `Phi=(q,tau,zeta,...)`.

Zeta is a proved third coordinate on repeated q/tau plateaux. `Q2=sum kappa^2` remains an exact bounded fourth-coordinate candidate.

# SCALING

Shell-side endpoint type count is absolute-constant in r.

The repeated correction-cycle branch no longer has cycle-length complexity: it is a two-state symbolic family.

The only remaining scalable **new combinatorial** structure is many distinct q-flat core 2-supports inside one fully decorated d2 shell class.

# MAIN-THEOREM IMPACT

This round reached the user's desired fixed-width philosophy at the shell level and partially at the core-support level:

- high endpoint: <=3 owners;
- d1/d2 shell support types: absolute constants;
- non-fully-decorated d2 plateau: absolute q-flat bounds;
- repeated fully-decorated correction cycles: two-state family;
- only distinct-support fully-decorated d2 plateau remains genuinely scalable.

No all-large-r contradiction is certified yet.

# NEXT SINGLE BLOCKER

> **Fully-Decorated Distinct-Support d2 Plateau Theorem:** for one fixed `S subset X`, prove that a `Phi_3`-maximal family of many distinct q-flat core 2-supports either improves a fourth bounded coordinate or collapses to a finite weighted support skeleton. After that, the remaining terminals are the finite distinct-support skeleton and the Balanced Two-Chamber block.