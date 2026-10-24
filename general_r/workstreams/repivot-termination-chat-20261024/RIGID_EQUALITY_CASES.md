# Rigid Equality Cases

This file is the canonical inventory of configurations which can still survive after the endpoint and potential reductions. Do not reopen eliminated cases.

Assumptions: hypotheses A+B, `r>=12`, legal regular repivots.

## E0. d=0 neutral pivot class — QUOTIENTED

If `d=0`, then

`S=D=empty`.

The owner y has no shell missing neighbour and no old-core neighbour. Its repivot has

- `H_y=H`;
- `q_y=q`;
- `tau_y=tau`.

Indeed `M[A]` and decoration are unchanged after swapping the two regular pivots p and y.

Thus d0 moves are pure relabellings of the same core view. They are not genuine terminal obstructions and should be contracted in the repivot graph.

**Status:** `PROVED_SYMBOLIC`.

---

## E1. d=1 one-vertex exchange — OPEN RIGIDITY

Write

`S={s}`, `D={u}`.

For the singleton common-S representation,

`q=r+B+sigma_s`,

while

`q_y=r+B+kappa_u+e_F(s,u)`.

Since the transported excess of the new core vertex s is

`kappa'_s=sigma_s-e_F(s,u)`,

the signed q-loss is exactly

> **`ell=q-q_y=kappa'_s-kappa_u`.**

Thus d1 is a pure one-vertex excess exchange at the level of total q:

- q-improvement iff `kappa'_s<kappa_u`;
- q-flat iff `kappa'_s=kappa_u`;
- q-loss iff `kappa'_s>kappa_u`.

At a q-maximal pivot only the last two are possible. A q-flat d1 move is also tau-non-improving at a `(q,tau)`-maximal pivot.

No support-overlap case tree exists because the support has size one. The remaining obligation is to prove that a q/tau-flat exchange is a harmless symmetry or forces a stricter plateau coordinate.

**Status:** exact exchange `PROVED_SYMBOLIC`; closure `OPEN`.

---

## E2. d=2 low endpoint — UNIQUE SCALABLE TERMINAL

For every common-S d2 system,

> **`W=K+2r-2+a+b`,**

where `b=e_M(S) in {0,1}`.

The first-overlap / exact-one-loss subsystem has the already-proved common-hub classification:

- at most three distinct support classes;
- a zero-charge common hub;
- private charge-one leaves;
- private leaves pairwise target-nonadjacent.

If all three support classes occur, the charge barrier gives

`W>=3r-2`,

hence

> **`K+a+b>=r`.**

Therefore the d2 terminal inventory splits into:

### E2-A. Low scalar regime

`K+a+b<=r-1`.

Three-class common-hub equality is impossible; at most two nontrivial common-hub support classes survive.

### E2-B. Linearly high scalar regime

`K+a+b>=r`.

This is the only presently scalable equality/positive-loss terminal. It includes possible high transported excess and/or high allowance. It must be attacked by a plateau potential or a multi-pivot sum identity, not by adding more local support cases.

### E2-C. Deep-loss isolated blocks

At first-high-slack, every support with loss at least two is disjoint from every distinct support class. These are block/transversal objects, not overlap objects.

Repeated non-fully-decorated plateau supports are forbidden by tau-maximality. Hence a repeated support on an equal-(q,tau) plateau must be fully decorated on its shell partner.

**Status:** structural decomposition `PROVED_CONDITIONAL`; E2-B elimination `OPEN`.

---

## E3. d=3 endpoint — ELIMINATED

The equality B-floor removes the only allowance-five boundary. Thus

`a+B<=4`.

The pre-existing low-charge Bridge-B machinery absorbs the entire remaining d3 sector (`b=2`, and `b=1,a<=4`).

No d3 terminal remains.

**Status:** `PROVED_CONDITIONAL`.

---

## EH. High endpoint d>=r-2 — FINITE THREE-OWNER KERNEL

There are at most three high owners in the entire shell.

Put

`s_y=r-d_y in {0,1,2}`.

Every high terminal is encoded by:

- at most three labelled/unlabelled owners;
- an owner target graph on at most three vertices;
- one `s_y in {0,1,2}` per owner;
- shell target-neighbour sets of size `s_y` inside an at-most-nine-point shell kernel;
- at most eight core owner-incidence signature classes;
- integer excess/decoration data on those classes.

Thus EH is a finite structural family independent of r. It is suitable for an O(1)-skeleton analytic proof or certificate enumeration.

**Status:** reduction `PROVED_CONDITIONAL`; elimination `OPEN`.

---

## EC. Closed non-improving repivot cycles — SIMULTANEOUS EQUALITY ONLY

Every closed cycle whose moves are non-improving in `(q,tau)` is q-flat and tau-flat at every edge.

Moreover every repeated support used on such a cycle must have a fully decorated shell partner.

Therefore a genuine no-improvement cycle can only use the rigid plateau portions of E1, E2-B/E2-C, and EH. E0 is contracted and E3 is absent.

**Status:** `PROVED_SYMBOLIC` reduction; simultaneous-equality cycle elimination `OPEN`.

---

# Canonical surviving list

After quotienting/eliminating proved branches, the only terminal families that must still be killed are:

1. **E1:** q/tau-flat one-vertex exchanges;
2. **E2-B:** d2 linearly-high scalar plateau `K+a+b>=r`;
3. **E2-C:** d2 isolated deep-loss blocks;
4. **EH:** at most three high-endpoint owners in a bounded-complement kernel;
5. **EC:** cycles assembled entirely from simultaneous equality instances of the preceding families.

Only E2-B can still carry an r-growing interacting support population.