# Progress Log — General-r Repivot Termination

## 2026-10-24 — Round 1

Branch:

`workstream/general-r-repivot-termination-20261024`

Only

`general_r/workstreams/repivot-termination-chat-20261024/`

was modified.

Upstream front extraction and anchor-excess proof were not reopened.

---

## Results 1–10 — endpoint compression package

Previously certified this round:

1. `Delta K=-2 Delta q`; closed non-improving cycles are q/tau-flat (`PROVED_SYMBOLIC`).
2. d3 frontier eliminated under A+B plus declared low-charge assets (`PROVED_CONDITIONAL`).
3. all high owners `d>=r-2` number at most three (`PROVED_CONDITIONAL`).
4. high endpoint has <=9 shell-kernel vertices / <=8 core signatures (`PROVED_CONDITIONAL`, Level 3).
5. exact d2 charge `W=K+2r-2+a+b`; three one-loss support classes imply `K+a+b>=r`.
6. d0 neutral symmetry.
7. d1 exact one-point exchange.
8. exact shell-incidence identity `t_s=d_M(s)+g_s=e_F(s,H)` and total budget `sum t_s<=6r-2`.
9. d1 <=5 shell classes; d2 support universe <=6 shell vertices / <=15 pair classes.
10. all low regular owners form a target clique; total low-owner count <=r-2.

Key earlier commits:

- potential baseline: `6cdf26de92f9b3c656f4f89799ecb3490f7836af`
- high three-owner theorem: `c93345b91d1f4c5bb90ffe328c2aef811e24dc86`
- six-point shell theorem: `009a618b431adbc162b22792d05d8b59770b873a`
- initial fixed-width termination theorem: `a62a6f132095b3d389710964297415bfdf6adf6f`

---

## Result 11 — Fixed-Class d2 Plateau Skeleton Theorem

Fix one d2 shell class `S={u,v}` and all its owners.

With

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`,

every owner has exact q-loss

`ell=a-[w(D)+mu(D)]`.

Support incidence forces

`lambda_x>=2 or w_x>=1 => x in X`.

Let `s=|S intersect X|`.

### s=0

Common-S transport forces `a=b`.

- b=0: every owner is q-flat and the entire class has at most three owners.
- b=1: at most one q-flat owner; strict rows have zero-w target-edge supports and at most three distinct support classes.

### s=1

Q-flat supports cannot repeat. Their graph is a disjoint union of at most three components, each an isolated edge or a star with at most two edges.

Hence

> `# q-flat owners<=6`.

### s=2

This is the only class in which q-flat multiplicity can scale.

Therefore:

> **the unique scalable equal-q d2 regime is a fixed fully decorated shell pair `S subset X`.**

Status: `PROVED_CONDITIONAL`.

Main file commit:

`4e84810280a91bed3b1feb4487bc348bf1625400`.

Endpoint-classification promotion:

`1ebed3f47a300c59ebfaff39991048bbb7ade1b0`.

Canonical promotion:

`267eeb5a3bf7e759e8bf1cae3d672d6051dc034a`.

---

## Result 12 — Repeated-Class Exchange Duality

For an exact `(S,D)` class of multiplicity m, repivot through one owner y.

Then:

- the other `m-1` owners become d0 exactly;
- every old d0 owner becomes a reverse `(D,S)` owner;
- the old pivot p also becomes a reverse `(D,S)` owner.

This is an exact support/neutral-population exchange, not merely a charging inequality.

Status: `PROVED_SYMBOLIC`.

Initial commit:

`18fa7cd785313fbd82624041ba81cb78e7bf6b29`.

---

## Result 13 — Genuine third potential coordinate zeta

Define

`zeta(p)=#{regular d0 owners in the current shell}`

and

> **`Phi_3=(q,tau,zeta)`.**

Zeta is bounded and is invariant under d0 neutral repivots.

For a q/tau-flat exact repeated class of multiplicity m,

`zeta(new)>=m-1`.

Therefore

> **`m>=zeta+2` gives strict `Phi_3` improvement.**

At a `Phi_3`-maximal pivot,

> **every q/tau-flat repeated class has `m<=zeta+1`.**

If equality is zeta-flat, the exchange is multiplicity-balanced.

Status: `PROVED_SYMBOLIC`.

Potential promotion commit:

`ea26065301a37d7ab7daed8813c75c4aa843209c`.

---

## Result 14 — Balanced correction-cycle clique capacity

For a `Phi_3`-flat repeated d2 class,

`m=zeta+1`.

Its m owners, the zeta=m-1 d0 owners and p form a target clique of size 2m. Hence

> `m<=floor((r-1)/2)`.

If k distinct exact repeated classes simultaneously admit `Phi_3`-flat exchanges, every one has multiplicity `zeta+1`, and the combined low-owner clique gives

> **`(k+1)(zeta+1)<=r-1`.**

Status: `PROVED_CONDITIONAL` on the standard backend clique cap.

Commit:

`99317c0a29549a07061fbe9d9f4831576f535aa3`.

---

## Result 15 — Missing-Pair / Neutral-Population Bound

Let D be a target-nonedge core pair. Its common H-nonneighbours form a clique and have size at least

`r-3-kappa(D)`.

The pivot and all zeta d0 owners are also common nonneighbours of D. The clique cap yields

> **`kappa(D)>=zeta-1`.**

For a q-flat d2 row with nonedge support,

`a=w(D)+1>=kappa(D)+1`,

so

> **`a>=zeta`.**

Thus if `a<zeta`, every q-flat d2 support is forced to be a target edge.

At the sharp boundary `a=zeta`, a nonedge support has the rigid equalities

- `kappa(D)=zeta-1`;
- no common H target-neighbour;
- `e_F(S,D)=0`;
- saturated common-nonneighbour clique.

Status: `PROVED_SYMBOLIC` under the standard global alpha/omega backend caps.

Commit:

`123a99b121e0bd4e48bd4be59a54c84c61edf9cd`.

---

## Canonical promotions after Results 11–15

- rigid equality inventory: `aad87161e85466baba2bb56b3c1556b06bac7047`
- current canonical state: `f2536233c1538a390a2a1175c4a9d22953eb60f2`
- current termination theorem: `7d620158674759e2da91c1accd2af569de31e0b6`

---

# Current canonical endpoint inventory

- medium `4<=d<=r-3`: impossible;
- d0: quotient-neutral;
- d1: <=5 shell classes; final q/tau-flat core exchange remains;
- d2 shell side: <=6 support vertices / <=15 classes;
- d2 plateau: every class with <=1 decorated shell endpoint has an absolute q-flat bound;
- **only fully decorated d2 shell pairs can carry scalable q-flat systems**;
- repeated fully-decorated classes are controlled by zeta; flat equality is a balanced reverse exchange satisfying `(k+1)(zeta+1)<=r-1`;
- q-flat nonedge supports require `a>=zeta` and have a rigid equality boundary;
- d3: eliminated;
- high endpoint: <=3 owners, finite bounded-complement skeleton.

# Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

Unlike the earlier Q2 proposal, zeta has a proved strict-improvement theorem on repeated q/tau plateaux.

`Q2=sum kappa^2` remains an exact bounded fourth-coordinate candidate; universal monotonicity is open.

# SCALING

The number of shell-side endpoint types is absolute-constant in r.

The only remaining scalable equal-q structure is internal to one of at most fifteen d2 shell classes and requires a fully decorated shell pair. Its repeated component is quantitatively tied to zeta; its nonedge component is tied to allowance by `a>=zeta`.

# MAIN-THEOREM IMPACT

The project has moved beyond shell endpoint compression: a nontrivial third potential coordinate is now certified, and the unique scalable d2 plateau has been split into two sharply constrained pieces:

1. distinct-support fully-decorated systems;
2. zeta-balanced repeated correction cycles.

No all-large-r contradiction is certified yet.

# NEXT SINGLE BLOCKER

> **Fully-Decorated d2 Plateau Theorem:** for one fixed `S subset X`, eliminate or rigidify the remaining distinct-support q-flat system and the zeta-balanced repeated correction cycles, ideally by a fourth bounded coordinate or a cycle-sum / hereditary-cap equality theorem.