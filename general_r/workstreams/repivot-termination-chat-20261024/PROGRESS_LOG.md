# Progress Log — General-r Repivot Termination

## 2026-10-24 — Round 1

### Branch/workstream isolation

Created branch:

`workstream/general-r-repivot-termination-20261024`

from

`workstream/general-r-architecture-20261024`.

Only files under

`general_r/workstreams/repivot-termination-chat-20261024/`

were modified.

### Upstream assets used as starting assets

- exact symbolic backend identity;
- strengthened `q<=3r-1` endpoint collapse under `K>=8`;
- `(q,tau)` potential and repeated-support strict tau loss;
- allowance localization / anchor transport;
- support/signature/sunflower machinery;
- owner-capacity formulas;
- Bridge-B transported excess;
- common-S equality B-floor;
- multicolor equality regular-clique obstruction;
- d2 one-loss common-hub theorem and pattern charge barrier;
- common-S charge localization;
- first-high-slack decomposition.

No front extraction or anchor-excess proof was reopened.

---

## Result 1 — Plateau transport / closed-cycle rigidity

`Delta K=-2 Delta q`.

K is redundant as a potential coordinate. Closed q-non-improving cycles are q-flat; closed `(q,tau)`-non-improving cycles are q/tau-flat edgewise. Repeated non-fully-decorated supports cannot occur on such a cycle.

Status: `PROVED_SYMBOLIC`.

Potential commit:

`6cdf26de92f9b3c656f4f89799ecb3490f7836af`.

---

## Result 2 — d3 frontier disappears

Equality B-floor forces

`q<=3r-2`, `a+B<=4`.

The declared low-charge Bridge-B assets absorb the remaining d3 sector.

Status: `PROVED_CONDITIONAL`.

---

## Result 3 — High Endpoint Three-Owner Theorem

For all `r>=12`, the total number of regular owners with `d>=r-2` is at most three.

Proof uses four-owner core packing / missing-edge count; `r>=13` dies from `4r-13>3r-1`; the `r=12` equality boundary forces a 10-vertex regular target clique and is killed by the multicolor equality regular-clique obstruction.

Status: `PROVED_CONDITIONAL`.

Commit:

`c93345b91d1f4c5bb90ffe328c2aef811e24dc86`.

---

## Result 4 — High bounded-complement kernel

For high owners, `s=r-d in {0,1,2}`. Since there are at most three owners:

- shell interaction kernel <=9 vertices;
- core owner-incidence <=8 signatures;
- owner graph <=3 vertices.

Status: `PROVED_CONDITIONAL`.

Success level: **Level 3 achieved**.

---

## Result 5 — Exact d2 common-S charge identity

For every d2 common-S family,

`W=K+2r-2+a+b`.

If an exact-one-loss common-hub subsystem has three distinct core support classes, the upstream charge barrier gives

`K+a+b>=r`.

Status: identity `PROVED_SYMBOLIC`; three-class consequence `PROVED_CONDITIONAL`.

---

## Result 6 — d0 neutral symmetry

A d0 repivot preserves H, q and tau and is only pivot relabelling. Contract it.

Status: `PROVED_SYMBOLIC`.

---

## Result 7 — d1 exact one-point exchange

For d1, `S={s}`, `D={u}`,

`ell=q-q_y=kappa'_s-kappa_u`.

Status: `PROVED_SYMBOLIC`.

---

## Result 8 — Shell-incidence identity

Define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Then

`sum_A t_s=2e(M)+G_A<=2q<=6r-2`.

For any regular owner y with shell missing set S, `|S|=d`, and `b=e_M(S)`, singleton transport gives pointwise

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`,

and summed

`sum_{s in S}t_s=d(r+1-d)+a_y+b_y`.

Status: `PROVED_SYMBOLIC` plus A+B for the global numerical cap.

---

## Result 9 — Strong d1/d2 finite shell-support theorem

This **supersedes** the earlier weaker four-star decomposition.

### d1

Every d1 missing partner has `t_s>=r`; all d1 shell support points lie in at most five vertices. Hence <=5 d1 shell classes.

### d2

For `S={u,v}` and `b=e_M(S)`, pointwise slack gives

`t_u,t_v>=r-1+b`.

Therefore every endpoint of every d2 shell missing pair lies in a common set `U_2` with

> `|U_2|<=6`.

Hence all d2 shell supports belong to at most

> `C(6,2)=15`

classes. There is **no r-growing d2 shell-support graph**.

With `h_u=t_u-(r-1)`, each class has exact shell allowance

`a_{uv}=h_u+h_v-b_{uv}`.

If `m=|U_2|`,

`sum h_u <= (6-m)r+m-2`.

For `m=6`, `sum h_u<=4` and the total d2 owner count is at most two.

Status: `PROVED_CONDITIONAL`.

Strong shell-incidence file commit:

`009a618b431adbc162b22792d05d8b59770b873a`.

Canonical promotion:

`dba4a666a3e06682248112d20a6515d092250fbf`.

Rigid-terminal promotion:

`57d7e62fcc68fcbf5b1eceeb70827b279296160e`.

Termination-theorem promotion:

`a62a6f132095b3d389710964297415bfdf6adf6f`.

---

## Result 10 — Low-Endpoint Owner Clique Lemma

For `r>=12`, any two regular owners with `d<=3` are target-adjacent. Otherwise zero-gap requires `S_x union S_y=A`, while the union has size at most six and `|A|=r+1>=13`.

Thus all regular low-endpoint owners together with p form a target clique, so there are at most `r-2` such owners by `omega(F)<=r-1`.

Status: `PROVED_SYMBOLIC`.

---

# Current canonical endpoint inventory

- medium `4<=d<=r-3`: impossible;
- d0: quotient-neutral;
- d1: <=5 shell classes; q/tau-flat one-point core exchange remains;
- d2: <=6 shell support vertices and <=15 shell classes; remaining difficulty is owner/core-support/transported-loss multiplicity inside these fixed classes;
- d3: eliminated;
- high `d>=r-2`: <=3 owners, finite bounded-complement skeleton.

Thus **no surviving endpoint has an r-growing number of shell-support types**.

# Potential status

`(q,tau)` is genuine and bounded.

K is redundant with q.

`Q2=sum kappa^2` is an exact bounded third-coordinate candidate with a closed update formula; universal monotonicity remains open.

# MAIN-THEOREM IMPACT

The user's core design goal has been achieved at the shell-support level: case count now decreases/collapses to absolute constants rather than growing with r.

What is not yet proved is an all-large-r contradiction. The remaining scalability is multiplicity and core-support/excess data inside finitely many common-S classes.

# NEXT SINGLE BLOCKER

> **Finite-Class d2 Core Multi-Pivot Compatibility:** fix one d2 shell pair `S={u,v}` with its exact parameters `b,h_u,h_v,sigma_u,sigma_v,a`; prove that simultaneous non-improving owners in this class either improve a bounded plateau coordinate or collapse to a finite impossible core-support skeleton. Then combine across at most fifteen classes.