# Rigid Equality Cases

Canonical inventory after the current endpoint/potential reductions. Assumptions: A+B, `r>=12`.

## E0. d=0 neutral pivot class — QUOTIENTED

If `d=0`, then `S=D=empty`, `H_y=H`, `q_y=q`, and `tau_y=tau`. These moves are pure pivot relabellings and are contracted in the repivot graph.

**Status:** `PROVED_SYMBOLIC`.

---

## E1. d=1 one-vertex exchange — FIVE SHELL CLASSES, CORE RIGIDITY OPEN

Write `S={s}`, `D={u}`. Then

`ell=q-q_y=kappa'_s-kappa_u`.

Thus q-improvement / flatness / loss is exactly comparison of the replaced core excess.

The shell-incidence heavy-cover theorem adds a global restriction. Let

`t_s=d_M(s)+g_s=e_F(s,H)`.

Every d1 owner satisfies `t_s>=r`. Since `sum_A t_s<=6r-2`, all d1 missing partners lie in one set

`C_1={s:t_s>=r}`

with

> **`|C_1|<=5`.**

Hence all d1 owners split into at most five shell common-S classes. The only remaining d1 growth is owner/core-support multiplicity inside those five classes.

**Status:** exact exchange + five-class shell reduction `PROVED_CONDITIONAL`; final plateau/core-support closure `OPEN`.

---

## E2. d=2 low endpoint — FOUR-STAR SCALABLE TERMINAL

For every common-S d2 system,

> **`W=K+2r-2+a+b`,**

where `b=e_M(S) in {0,1}`.

The exact-one-loss common-hub subsystem has at most three distinct core support classes. If all three occur, the charge barrier gives

> **`K+a+b>=r`.**

The shell-incidence theorem gives a second, independent global compression. Every d2 shell missing pair `{s,t}` satisfies

`t_s+t_t>=2(r-1)`.

Therefore every pair meets the fixed heavy set

`C_2={v:t_v>=r-1}`, `|C_2|<=6`.

More sharply, with

`P={v:2t_v>=3(r-1)}`, `|P|<=4`,

`Q={v:2t_v>=r-1}`, `|Q|<=12`,

every d2 shell support either

1. is incident with P, hence belongs to one of at most four star systems; or
2. is entirely contained in Q, hence belongs to a bounded at-most-twelve-vertex core.

Thus the terminal inventory is:

### E2-A. Bounded shell core

All support pairs lie inside Q. The shell support graph has O(1) vertices and finitely many combinatorial types.

### E2-B. Heavy stars

At most four centers in P may carry r-growing families of distinct support leaves. This is now the **only** source of unbounded d2 shell-support diversity.

Within a common-S/core-support one-loss component, a three-class terminal additionally requires `K+a+b>=r`.

### E2-C. Deep-loss isolated core-support blocks

At first-high-slack, loss>=2 core support classes are disjoint from every distinct core support class. They are block/transversal objects.

Repeated non-fully-decorated plateau core supports are forbidden by tau-maximality.

**Status:** four-star/bounded-core reduction `PROVED_CONDITIONAL`; E2-B multi-pivot elimination `OPEN`.

---

## E3. d=3 endpoint — ELIMINATED

The equality B-floor removes allowance five, giving `a+B<=4`; the declared low-charge Bridge-B assets absorb the remaining d3 sector.

**Status:** `PROVED_CONDITIONAL`.

---

## EH. High endpoint d>=r-2 — FINITE THREE-OWNER KERNEL

There are at most three high owners total. With `s_y=r-d_y in {0,1,2}`, every high terminal has an at-most-nine-point shell kernel and at most eight core owner-incidence signature classes.

**Status:** reduction `PROVED_CONDITIONAL`; elimination `OPEN`.

---

## EC. Closed non-improving cycles — SIMULTANEOUS EQUALITY ONLY

Every closed `(q,tau)`-non-improving cycle is q-flat and tau-flat edge-by-edge; every repeated core support on it has a fully decorated shell partner.

**Status:** `PROVED_SYMBOLIC`; simultaneous-equality cycle elimination `OPEN`.

---

# Canonical surviving list

Only the following remain:

1. **E1:** at most five d1 shell classes, with q/tau-flat one-point core exchanges;
2. **E2-A:** finite d2 shell-support core on at most twelve vertices;
3. **E2-B:** at most four scalable d2 heavy-star systems, with the linearly-high scalar branch `K+a+b>=r` when three one-loss core-support classes occur;
4. **E2-C:** isolated deep-loss core-support blocks;
5. **EH:** at most three high-endpoint owners;
6. **EC:** simultaneous equality cycles assembled from these pieces.

The only r-growing *distinct shell-support geometry* is E2-B: at most four weighted stars.