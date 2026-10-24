# Rigid Equality Cases

Canonical inventory after the current endpoint/potential reductions. Assumptions: A+B, `r>=12`, plus the standard global alpha/omega caps when explicitly invoked.

## E0. d=0 neutral pivot class — QUOTIENTED

If `d=0`, then `S=D=empty`, the core, q and tau are unchanged. Neutral repivots also preserve

`zeta=#{d0 regular shell owners}`.

They are pure pivot relabellings and are contracted.

**Status:** `PROVED_SYMBOLIC`.

---

## E1. d=1 one-vertex exchange — AT MOST FIVE SHELL CLASSES

For `S={s}`, `D={u}`,

`q-q_y=kappa'_s-kappa_u`.

Every d1 missing partner has shell-to-core incidence `t_s>=r`, while `sum_A t_s<=6r-2`; hence all d1 shell supports lie in at most five vertices/classes.

**Status:** shell reduction `PROVED_CONDITIONAL`; final q/tau-flat one-point core-exchange closure `OPEN`.

---

## E2. d=2 — FINITE SHELL FAMILY, UNIQUE SCALABLE PLATEAU

### E2-S. Six-point shell support universe

All d2 shell missing-set endpoints lie in one set `U_2` with

`|U_2|<=6`.

Hence there are at most fifteen d2 shell classes `S={u,v}`. Writing

`h_u=t_u-(r-1)`,

each class has exact allowance

`a_{uv}=h_u+h_v-b_{uv}`.

There is no r-growing shell-support graph.

### E2-P0. Fixed class with no decorated shell endpoint

Let `s=|S intersect X|=0`.

Common-S transport forces `a=b`.

- `b=0`: every owner is q-flat and there are at most three owners total.
- `b=1`: at most one q-flat owner; all strict rows have zero-w target-edge supports, with at most three distinct strict support classes.

So this regime is fixed-width.

### E2-P1. Fixed class with one decorated shell endpoint

If `s=1`, every q-flat support is unique. The q-flat support graph is a disjoint union of at most three components, each an isolated edge or a star with at most two edges.

Therefore

> `# q-flat owners <=6`.

So this regime is also fixed-width.

### E2-P2. Fully decorated shell pair — UNIQUE SCALABLE EQUAL-q REGIME

Only

> `S subset X`

can carry an r-growing family of q-flat owners.

For a fixed class, with

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`,

every owner has

`ell_y=q-q_y=a-[w(D_y)+mu(D_y)]`.

This is the unique scalable d2 plateau block.

### E2-R. Repeated q/tau-flat class — zeta controlled

Define

`zeta=#{d0 regular shell owners}`

and potential

`Phi_3=(q,tau,zeta)`.

If an exact `(S,D)` class has multiplicity m and one row is q/tau-flat, repivoting it makes the other `m-1` owners d0. Hence

`zeta(new)>=m-1`.

At `Phi_3` maximality,

> `m<=zeta+1`.

If equality is zeta-flat, then the old d0 population together with the old pivot becomes a reverse `(D,S)` class of multiplicity at least m, while the other `m-1` old class owners become exactly the full new d0 population. Thus equality is a multiplicity-balanced correction exchange.

For d2, q/tau-flat repetition forces both D and S to be fully decorated.

### E2-N. Nonedge support branch — neutral-population excess bound

If a q-flat core support D is a target nonedge, the common-nonneighbour clique argument gives

> `kappa(D)>=zeta-1`.

Therefore

> `a>=zeta`.

So if `a<zeta`, every q-flat support must be a target edge. At the sharp nonedge boundary `a=zeta`, one gets the rigid equalities

- `kappa(D)=zeta-1`;
- no common H target-neighbour of the two support vertices;
- `e_F(S,D)=0`;
- a saturated common-nonneighbour clique containing p and all d0 owners.

### E2-C. Remaining fully-decorated core-support terminal

The only scalable d2 work left is therefore:

1. distinct-support q-flat systems with `S subset X`;
2. `zeta`-balanced repeated-class correction cycles;
3. positive-loss rows coupled to those plateau systems.

The old first-high-slack assets remain available inside these blocks: one-loss common-hub / at-most-three-class structure, deep-loss disjointness, and the scalar barrier `K+a+b>=r` for a three-class one-loss system.

**Status:** all reductions above `PROVED_CONDITIONAL` / `PROVED_SYMBOLIC`; final E2-C elimination `OPEN`.

---

## E3. d=3 endpoint — ELIMINATED

Equality B-floor gives `a+B<=4`; the declared low-charge Bridge-B machinery absorbs the remaining d3 sector.

**Status:** `PROVED_CONDITIONAL`.

---

## EH. High endpoint d>=r-2 — FINITE THREE-OWNER KERNEL

There are at most three high owners total. With `s_y=r-d_y in {0,1,2}`, every high terminal has an at-most-nine-point shell kernel and at most eight core owner-incidence signature classes.

**Status:** reduction `PROVED_CONDITIONAL`; final elimination `OPEN`.

---

## EC. Closed non-improving cycles

Every closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. Appending zeta gives a genuine third coordinate on repeated-class exchanges: any closed `Phi_3`-non-improving cycle containing such exchanges must be zeta-flat there, hence multiplicity-balanced.

Thus the repeated-support part of a correction cycle is no longer arbitrary: it must alternate exact support/neutral-population exchanges with matched multiplicities.

**Status:** reduction `PROVED_SYMBOLIC`; balanced-cycle elimination `OPEN`.

---

# Canonical surviving list

Only the following remain:

1. **E1:** at most five d1 shell classes with q/tau-flat one-point core exchanges;
2. **E2-C:** at most fifteen d2 shell classes, but only fully-decorated pairs can carry scalable q-flat multiplicity; their remaining subbranches are distinct-support systems and zeta-balanced repeated correction cycles;
3. **EH:** at most three high-endpoint owners;
4. **EC:** simultaneous equality cycles assembled from these finite endpoint blocks.

No surviving family has an r-growing number of shell-support types. The unique scalable equal-q mechanism is now the fully-decorated fixed-class d2 core-support system.