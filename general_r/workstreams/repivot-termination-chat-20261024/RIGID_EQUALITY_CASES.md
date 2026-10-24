# Rigid Equality Cases

Canonical inventory after the current endpoint/potential reductions. Assumptions: A+B, `r>=12`.

## E0. d=0 neutral pivot class — QUOTIENTED

If `d=0`, then `S=D=empty`, `H_y=H`, `q_y=q`, and `tau_y=tau`. These moves are pure pivot relabellings and are contracted in the repivot graph.

**Status:** `PROVED_SYMBOLIC`.

---

## E1. d=1 one-vertex exchange — AT MOST FIVE SHELL CLASSES

Write `S={s}`, `D={u}`. Then

`ell=q-q_y=kappa'_s-kappa_u`.

Thus q-improvement / flatness / loss is exactly comparison of the replaced core excess.

Let `t_s=d_M(s)+g_s=e_F(s,H)`. Every d1 owner satisfies `t_s>=r`. Since `sum_A t_s<=6r-2`, all d1 missing partners lie in a set

`C_1={s:t_s>=r}`

with

> `|C_1|<=5`.

Hence all d1 owners split into at most five common-S shell classes. Remaining growth is owner/core-support multiplicity inside those classes.

**Status:** shell reduction `PROVED_CONDITIONAL`; final q/tau-flat one-point core-exchange closure `OPEN`.

---

## E2. d=2 low endpoint — FINITE SHELL CLASS FAMILY, CORE MULTIPLICITY OPEN

For every d2 common-S system,

> `W=K+2r-2+a+b`,

where `b=e_M(S) in {0,1}`.

The exact-one-loss common-hub subsystem has at most three distinct core support classes. If all three occur, the pattern charge barrier gives

> `K+a+b>=r`.

### E2-S. Six-point shell support universe

Let `U_2` be the union of all shell missing sets of all d2 regular owners. Singleton transport gives, for `S={u,v}`,

`sigma_u=t_u-r+1-b>=0`,
` sigma_v=t_v-r+1-b>=0`.

Hence every active endpoint satisfies `t>=r-1`. Since `sum_A t_s<=6r-2`,

> `|U_2|<=6`.

Therefore all d2 shell missing sets belong to at most

> `C(6,2)=15`

common-S classes. There is **no** r-growing shell-support graph.

If `b=1`, both endpoints satisfy `t>=r`, so such pairs lie inside the at-most-five-point set `C_1`.

### E2-W. Weighted shell encoding

For `u in U_2`, define

`h_u=t_u-(r-1)>=0`.

For the class `S={u,v}`,

> `a_{uv}=h_u+h_v-b_{uv}`.

Thus shell allowance data is encoded by one graph `M[U_2]` on at most six vertices plus at most six integer weights.

If `m=|U_2|`,

`sum h_u <= (6-m)r+m-2`.

In the maximal case `m=6`,

`sum h_u<=4`

and the total d2 owner count is at most two. Hence the six-endpoint boundary is already fully bounded.

### E2-C. Remaining core-support terminal

Inside each of the at most fifteen fixed shell classes, owners still carry core support sets `D_y`, q-loss/transported excess, support multiplicities, and possible deep-loss blocks.

At first-high-slack:

- exact one-loss distinct support classes obey the common-hub / at-most-three-class theorem;
- loss>=2 support classes are disjoint from every distinct support class;
- repeated non-fully-decorated plateau supports are forbidden by tau-maximality.

The scalable obstruction is therefore no longer shell geometry. It is **core-support multiplicity and transported loss inside finitely many fixed shell classes**, especially the linearly-high three-class regime `K+a+b>=r`.

**Status:** shell finite-class reduction `PROVED_CONDITIONAL`; finite-class core multi-pivot elimination `OPEN`.

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
2. **E2-C:** at most fifteen d2 shell classes, each carrying a core-support / transported-loss system; three one-loss core-support classes require `K+a+b>=r`;
3. **EH:** at most three high-endpoint owners in a bounded-complement kernel;
4. **EC:** simultaneous equality cycles assembled from these pieces.

No surviving family has an r-growing number of shell-support types. The only remaining r-growth is multiplicity/excess data inside finitely many classes.