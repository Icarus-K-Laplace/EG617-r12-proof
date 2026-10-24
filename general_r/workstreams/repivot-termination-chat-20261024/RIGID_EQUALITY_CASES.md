# Rigid Equality Cases

Canonical inventory after the current endpoint/potential reductions. Assumptions: A+B, `r>=12`.

Audited caps:

- global residual `alpha(F)<=4`, `omega(F)<=r-1`;
- every legal core `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Do not forbid independent 4-sets in F.

---

## E0. d0 neutral class — QUOTIENTED

`S=D=empty`; core, q and tau are unchanged. Neutral repivots are pivot relabellings. Zeta is invariant inside a neutral chamber.

**Status:** `PROVED_SYMBOLIC`.

---

## E1. d1 one-point exchange — BOUNDED SHELL TYPES

All d1 missing partners lie in at most five shell singleton classes.

For `S={s}`, `D={u}`,

`q-q_y=kappa'_s-kappa_u`.

Define eta as the number of d1 owners on the exact `(q,tau,zeta)` plateau. Eta is the fourth potential coordinate.

If eta is linear, one of the five d1 classes has linear size. In the neutral-free slice its singleton supports are distinct and, for class allowance c,

> `(N_1-1)c<=3r-2`

under the inherited core cap. Hence every linear d1 terminal has O(1) allowance.

**Status:** shell/scale reduction `PROVED_CONDITIONAL`; bounded-allowance d1 terminal `OPEN`.

---

## E2. d2 — FINITE SHELL FAMILY

All d2 shell missing-set endpoints lie in a six-point universe, hence at most15 shell pair classes.

For one fixed class S,

`ell=q-q_y=a-[w(D)+mu(D)]`.

Only a fully decorated shell pair

> `S subset X`

can carry an r-growing q-flat family.

---

## E2-R. Repeated fully-decorated branch — TWO CHAMBERS

For exact multiplicity m and neutral population zeta,

> `zeta(new)=m-1`,
>
> `m_reverse=zeta+1`.

At `Phi_3=(q,tau,zeta)` maximality, `m<=zeta+1`.

Equality `m=zeta+1` is exactly the Balanced Two-Chamber terminal:

- two chambers of size m;
- their union is a target `K_(2m)`;
- modulo neutral relabellings the correction orbit is
  > `H <--> H-D+S`;
- allowance is invariant;
- the shell/core missing indicators exchange.

**Status:** `PROVED_CONDITIONAL`.

---

## E2-D. Distinct fully-decorated branch — FOURTH COORDINATE

A genuine `Phi_3`-flat distinct class lies at

> `zeta=0`.

For supports `D_i,D_j`, repivot through `D_i` gives exact correction degree

> `2-|D_i intersect D_j|`.

Thus one-point overlap becomes a d1 plateau transition.

Define

`eta(p)=#{regular d1 owners x on the same (q,tau,zeta) plateau}`.

Then

> **`Phi_4=(q,tau,zeta,eta)`**

is bounded. If `G_S` is the support-intersection graph, at `Phi_4` maximality

> `Delta(G_S)<=eta`.

Hence a class of N supports has a disjoint subfamily of size at least

> `ceil(N/(eta+1))`.

**Status:** `PROVED_SYMBOLIC`.

---

## E2-L0 / E2-L1. First two allowance layers — CLOSED

For a distinct fully-decorated q-flat class:

- `a=0 => N<=3`;
- `a=1 => N<=9`.

The a=1 bound uses only row closure and `alpha(H)<=3`: every support contains a zero-weight endpoint, there are at most three zero signatures/zero vertices, and each zero-hub signature has at most three leaves.

**Status:** `PROVED_CONDITIONAL`.

---

## E2-A2. First scalable allowance — CLEAN PAIR DESIGN

At `a=2`, non-clean q-flat support types contain a zero-weight endpoint. In any pairwise-disjoint subfamily, at most three supports are non-clean.

Every other block is a clean support:

- target K2;
- endpoint weights `(1,1)`.

If `D_i,D_j` are disjoint clean blocks, repivot through `D_i` leaves `D_j` exactly clean relative to the new shell pair:

- still d2;
- still q/tau/zeta-flat;
- still a target K2;
- still weights `(1,1)`.

Thus a large clean matching is repivot-closed under pair exchange.

Between two clean blocks, row closure makes the target cross graph a matching of size0,1,or2.

The old shell pair becomes one of only three reverse-support types:

1. clean `(1,1)` target K2;
2. `(0,2)` target K2;
3. `(0,1)` target nonedge.

Therefore the scalable a=2 equality family is the rigid terminal

> **Clean Pair-Exchange Design + O(1) special zero-containing blocks.**

The zero-free `(1,1)` support graph has maximum degree3, so every unbounded a=2 family contains an unbounded clean matching subsystem; every linear-size family contains a linear-size one.

**Status:** extraction `PROVED_CONDITIONAL`; nonextension `OPEN`.

---

## E2-HIGHER. Higher distinct allowance

For `a>=2`, any disjoint q-flat subfamily of size nu satisfies

> `nu(a-1)<=W<=4r+9-a`.

Together with the eta matching extraction, high allowance cannot coexist with both a linearly large d2 class and sublinear d1 correction population. If a linear d2 class has `eta=o(r)`, then `a=o(r)`; if eta is linear, it transfers to a bounded-allowance d1 terminal.

**Status:** `PROVED_CONDITIONAL`.

---

## E2-AUDIT. Retracted claims

The following are not canonical:

- `kappa(D)>=zeta-1` / `a>=zeta` for nonedge supports;
- allowance-independent `nu(Q)<=3` / six-hub collapse.

Both relied on incorrectly treating `alpha(F)<=4` as `alpha(F)<=3`.

---

## E3. d3 — ELIMINATED

Equality B-floor gives `a+B<=4`; the declared low-charge Bridge-B machinery closes the sector.

**Status:** `PROVED_CONDITIONAL`.

---

## EH. High endpoint — THREE-OWNER KERNEL

All regular owners with `d>=r-2` number at most3. Their bounded-complement encoding has at most9 shell interaction vertices and at most8 core owner-incidence signatures.

**Status:** reduction `PROVED_CONDITIONAL`; final incompatibility `OPEN`.

---

## EC. Non-improving cycles

Every closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise.

- repeated edges collapse via zeta to the Balanced Two-Chamber involution;
- distinct d2 overlap is charged to eta/d1;
- the first scalable distinct flat component contains the Clean Pair-Exchange Design.

Thus long unstructured correction cycles no longer survive.

**Status:** reduction `PROVED_SYMBOLIC` / `PROVED_CONDITIONAL`.

---

# Canonical surviving terminal list

1. **E1:** bounded-allowance d1 singleton-exchange systems in at most5 shell classes;
2. **E2-R:** Balanced Two-Chamber repeated terminal;
3. **E2-A2:** Clean Pair-Exchange Design plus O(1) special blocks;
4. **E2-HIGHER:** eta/matching-compressed higher-allowance distinct systems;
5. **EH:** at most3 high-endpoint owners.

The single highest-value blocker is now:

> **Clean Pair Nonextension Theorem:** eliminate a sufficiently large repivot-closed clean K2 block system with matching cross graphs and no independent 4-transversal, or force a fifth potential coordinate to rise.