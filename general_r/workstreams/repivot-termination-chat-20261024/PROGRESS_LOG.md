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

### Upstream assets audited

Read and used as starting assets:

- exact symbolic backend identity;
- strengthened `q<=3r-1` endpoint collapse under `K>=8`;
- `(q,tau)` potential and repeated-support strict tau loss;
- allowance localization and anchor transport;
- support/signature/sunflower machinery;
- owner-capacity formulas;
- Bridge-B transported excess;
- common-S equality B-floor;
- multicolor equality regular-clique obstruction;
- d2 one-loss common-hub theorem and charge barrier;
- common-S charge localization;
- first-high-slack decomposition.

No front extraction or anchor-excess proof was reopened.

---

## New result 1 — Exact plateau cycle identity

For every regular repivot in one fixed residual graph,

`Delta K=-2 Delta q`.

Hence K is redundant as a potential coordinate. Closed q-non-improving cycles are q-flat; closed `(q,tau)`-non-improving cycles are q/tau-flat edgewise. Repeated non-fully-decorated supports cannot occur on such a cycle.

Status: `PROVED_SYMBOLIC`.

Commit introducing potential file:

`6cdf26de92f9b3c656f4f89799ecb3490f7836af`.

---

## New result 2 — d3 frontier disappears

The equality B-floor forces every d3 local/common-S view below the top ceiling:

`q<=3r-2`, hence `a+B<=4`.

Using the declared upstream low-charge absorption (`b=2`, and `b=1,a<=4`), no d3 terminal remains.

Status: `PROVED_CONDITIONAL`.

---

## New result 3 — High Endpoint Three-Owner Theorem

Let `Y_hi` be all regular shell vertices with `d>=r-2`. Then

> `|Y_hi|<=3`

for every `r>=12`.

Core proof:

- four pairwise target-nonadjacent high owners would have pairwise-disjoint core supports by zero-gap and require `4(r-2)>3r-1` core vertices;
- therefore any four high owners span a target edge, so their internal shell missing-edge count is at most5;
- their four missing degrees force at least `4r-13` distinct shell missing edges;
- for `r>=13`, this exceeds `q<=3r-1`;
- at `r=12`, equality forces `q=35`, `G_A=0`, hereditary equality and a 10-vertex regular target clique, contradicting the multicolor equality clique obstruction.

Status: `PROVED_CONDITIONAL`.

Main commit:

`c93345b91d1f4c5bb90ffe328c2aef811e24dc86`.

---

## New result 4 — High Endpoint Bounded-Complement Reduction

Put `s=r-d in {0,1,2}` for high owners. Since there are at most three owners:

- shell high-owner interaction kernel has size at most9;
- core owner-incidence data has at most8 signatures;
- owner graph has at most3 vertices.

Thus high endpoint is an r-independent finite skeleton.

Status: `PROVED_CONDITIONAL`.

Success level impact: **Level 3 achieved**.

---

## New result 5 — Exact d2 charge identity

For every d2 common-S family,

> `W=K+2r-2+a+b`.

For a three-class one-loss common-hub subsystem, the existing charge barrier `W>=3r-2` gives

> `K+a+b>=r`.

Thus the troublesome d2 three-class branch is forced into a linearly-high excess/allowance regime.

Status: identity `PROVED_SYMBOLIC`; barrier consequence `PROVED_CONDITIONAL`.

---

## New result 6 — d0 neutral symmetry

A d0 regular repivot has `S=D=empty`, preserves H, q and tau, and is only a pivot relabelling. Contract these edges in the repivot graph.

Status: `PROVED_SYMBOLIC`.

---

## New result 7 — d1 exact exchange

For d1, `S={s}`, `D={u}`,

> `ell=q-q_y=kappa'_s-kappa_u`.

Thus d1 q-loss is exactly one-vertex excess replacement.

Status: `PROVED_SYMBOLIC`.

---

## New result 8 — Shell-Incidence Heavy-Cover Theorem

Define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Then

`sum_A t_s=2e(M)+G_A<=2q<=6r-2`.

For every regular owner y with missing set S of size d,

> `sum_{s in S} t_s=d(r+1-d)+a_y+b_y`.

Consequences:

### d1

Every missing partner has `t_s>=r`, so all d1 shell supports lie in at most5 vertices.

### d2

Every missing pair has endpoint-sum at least `2(r-1)`, so every pair meets a heavy set of at most6 vertices.

With thresholds

`P={2t>=3(r-1)}`, `|P|<=4`,

`Q={2t>=r-1}`, `|Q|<=12`,

every d2 pair is either incident with P or fully contained in Q.

Therefore all r-growing distinct d2 shell-support geometry is confined to **at most four star families**; all other pair supports lie in an at-most-twelve-vertex bounded core.

Status: `PROVED_CONDITIONAL`.

Commit:

`574d50e65bfdc7b63e9017f61609905215683f5a`.

Termination theorem updated at:

`b7c64e08eba10aff65e35b41e09d51858cc35951`.

Rigid terminal inventory updated at:

`054c80592463632fe30588e40b0cb049f42da9c4`.

---

# Current canonical endpoint inventory

- medium `4<=d<=r-3`: impossible;
- d0: quotient-neutral;
- d1: at most five shell support classes, core exchange closure open;
- d2: bounded twelve-vertex shell core plus at most four scalable heavy stars; linearly-high equality/positive-loss branch open;
- d3: eliminated;
- high d>=r-2: at most three owners, finite bounded-complement skeleton.

# Current potential status

`(q,tau)` is genuine and bounded.

K is redundant with q.

`Q2=sum kappa^2` is an exact bounded candidate third coordinate with a closed update formula, but universal monotonicity is open.

# MAIN-THEOREM IMPACT

The general backend is no longer a growing endpoint case tree. Every source of r-growing *distinct support geometry* has been eliminated except at most four d2 heavy-star systems.

No absolute sufficiently-large-r contradiction is certified yet.

# NEXT SINGLE BLOCKER

> **D2 Heavy-Star Multi-Pivot Compatibility:** for one scalable star centered at a high shell-incidence vertex, prove that simultaneous non-improvement of its owner repivots is impossible or forces a finite rigid equality skeleton. Then sum over the at most four hubs.