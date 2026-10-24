# Rigid Equality Cases

Canonical inventory after the current endpoint/potential reductions. Assumptions: A+B, `r>=12`. The audited global backend has `alpha(F)<=4`, `omega(F)<=r-1`; the core has `alpha(H)<=3`.

## E0. d=0 neutral pivot class — QUOTIENTED

If `d=0`, then `S=D=empty`, the core, q and tau are unchanged. Neutral repivots preserve

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

### E2-P1. Fixed class with one decorated shell endpoint

If `s=1`, every q-flat support is unique. The q-flat support graph is a disjoint union of at most three components, each an isolated edge or a star with at most two edges.

Therefore

> `# q-flat owners <=6`.

### E2-P2. Fully decorated shell pair — UNIQUE SCALABLE EQUAL-q REGIME

Only

> `S subset X`

can carry an r-growing family of q-flat owners.

For a fixed class,

`ell_y=q-q_y=a-[w(D_y)+mu(D_y)]`.

This is the unique scalable d2 plateau block.

### E2-R. Exact class exchange / repeated branch

Let an exact `(S,D)` class have multiplicity m and let

`zeta=#{d0 regular shell owners}`.

The class-neutral exchange is exact:

> `zeta(new)=m-1`,
>
> `m_reverse=zeta+1`.

Thus at `Phi_3=(q,tau,zeta)` maximality a q/tau-flat class satisfies `m<=zeta+1`, with equality exactly when the move is `Phi_3`-flat.

For d2, q/tau-flat repetition forces both D and S to be fully decorated.

A `Phi_3`-flat repeated class is the Balanced Two-Chamber family:

- `m=zeta+1`;
- the class chamber and the neutral/pivot chamber each have size m;
- their union is a target `K_(2m)`;
- modulo d0 relabelling, the correction graph is exactly `H <--> H-D+S`;
- allowance is invariant and the missing bits `b` and `mu` exchange.

### E2-D. Distinct fully-decorated branch

A genuinely `Phi_3`-flat distinct exact class has multiplicity1 and therefore forces

> `zeta=0`.

For one fixed fully decorated shell pair, the distinct q-flat support graph Q satisfies:

- `a=0`: at most 3 support edges;
- `a=1`: at most 12 support edges;
- `a>=2`: `nu(Q)(a-1)<=W<=4r+9-a`;
- at `a=2`, zero-weight support vertices are at most3 and the `(1,1)` target-support subgraph has maximum degree at most3;
- support intersection controls the pairwise correction degree exactly: repeated / one-point overlap / disjoint correspond to d0 / d1 / d2 correction transitions.

The attempted allowance-independent `nu(Q)<=3` theorem is **retracted** because it assumed `alpha(F)<=3`; the actual backend has `alpha(F)<=4`.

### E2-AUDIT. Invalid nonedge-neutral claim

The earlier claim

`kappa(D)>=zeta-1`, hence `a>=zeta`

for q-flat nonedge supports is **retracted**. Its proof incorrectly treated an independent 4-set in F as forbidden. Do not use it.

### E2-C. Remaining fully-decorated terminal

The remaining d2 work is therefore:

1. distinct-support q-flat systems at allowance `a>=2`, beginning with complete closure of `a=2`;
2. elimination/further rigidity of the already-classified Balanced Two-Chamber family;
3. positive-loss rows coupled to those plateau systems.

The first-high-slack assets remain available: one-loss common-hub/at-most-three-class structure, deep-loss disjointness, and the scalar barrier `K+a+b>=r` for a three-class one-loss system.

**Status:** reductions `PROVED_CONDITIONAL` / `PROVED_SYMBOLIC`; final E2-C elimination `OPEN`.

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

Every closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. The exact zeta exchange law controls class multiplicity. A repeated `Phi_3`-flat correction component is already the two-state Balanced Two-Chamber involution.

Thus unresolved correction-cycle complexity comes from distinct-support fully-decorated d2 moves and d1 exchanges.

**Status:** reduction `PROVED_SYMBOLIC`; final elimination `OPEN`.

---

# Canonical surviving list

1. **E1:** at most five d1 shell classes with q/tau-flat one-point core exchanges;
2. **E2-D:** at most fifteen d2 shell classes, but only fully-decorated pairs can carry scalable q-flat multiplicity; the principal open branch is distinct supports with `a>=2`;
3. **E2-R:** the bounded-description Balanced Two-Chamber repeated terminal;
4. **EH:** at most three high-endpoint owners;
5. **EC:** equality cycles generated by the open d1/distinct-support pieces.

No surviving family has an r-growing number of shell-support types. The principal scalable core-support mechanism is the fully-decorated distinct d2 branch at allowance `a>=2`.