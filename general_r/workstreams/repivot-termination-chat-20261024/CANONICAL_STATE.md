# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. Front extraction and anchor-excess are upstream conditional hypotheses.

## Conditional hypotheses

- **A (residual-core contract).** Every legal backend view has a core `H` with `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; every legal regular repivot again has a valid core with minimum degree at least r.
- **B (anchor excess).** Every legal core satisfies `K_r>=8`.

Hence

`q<=3r-1`.

For `r>=12`, no regular missing degree `4<=d<=r-3` is possible. Thus

`d in {0,1,2,3,r-2,r-1,r}`.

## Exact identities in force

`e(F)=C(r+2,2)+q+e(H)`.

`K_r=2(E-q-(2r^2+r+1))`.

For a regular repivot `p -> y`,

`q_y=d(r+1-d)+B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

Transport:

`kappa'_z=w_z-e_H(z,D_y)` for `z in H\D_y`,

`kappa'_s=sigma_s-e_F(s,D_y)` for `s in S_y`.

Potential:

`Psi_2=(q,tau)`, `tau=|A intersect {v:d_F(v)>r+1}|`.

## Proved results in this workstream

### R1. Plateau transport / cycle identity — PROVED_SYMBOLIC

`K_y-K_p=-2(q_y-q_p)`.

Thus K is affine-redundant with q. Every closed q-non-improving cycle is q-flat; every closed `(q,tau)`-non-improving cycle is q-flat and tau-flat edgewise. Repeated non-fully-decorated supports cannot occur on such a plateau cycle.

### R2. d0 neutral symmetry — PROVED_SYMBOLIC

For d=0, `S=D=empty`; the core, q, and tau are unchanged. Contract these pivot relabellings.

### R3. d1 finite shell-support reduction — PROVED_CONDITIONAL

Define shell-to-core incidence mass

`t_s=d_M(s)+g_s=e_F(s,H)`.

Globally

`sum_A t_s=2e(M)+G_A=2q-G_A<=6r-2`.

For a d1 owner with missing partner s, transport gives `sigma_s=t_s-r>=0`. Therefore every d1 missing partner has `t_s>=r`, so all d1 shell supports lie in a fixed set of at most five shell vertices. Hence there are at most five d1 common-S classes.

The exact d1 q-loss is

`ell=q-q_y=kappa'_s-kappa_u`.

Final q/tau-flat core-exchange rigidity remains open.

### R4. d2 Six-Point Support-Universe Theorem — PROVED_CONDITIONAL

For any regular owner y with missing set S of size d, singleton transport gives the pointwise identity

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`.

For d2, `S={u,v}` and `b=e_M(S)`, so

`sigma_u=t_u-r+1-b>=0`,
` sigma_v=t_v-r+1-b>=0`.

Thus **both** endpoints of every d2 shell missing pair have `t>=r-1+b`, in particular `t>=r-1`. Since total shell incidence mass is at most `6r-2`, the union `U_2` of all d2 support endpoints satisfies

> `|U_2|<=6`.

Therefore all d2 shell missing sets are among at most

> `C(6,2)=15`

pair types, independent of r. If the pair itself is missing (`b=1`), both endpoints have `t>=r` and lie in the at-most-five-point d1-heavy set.

Writing `h_u=t_u-(r-1)>=0`, every d2 shell class has exact allowance

> `a_{uv}=h_u+h_v-b_{uv}`.

If `m=|U_2|`, then

`sum_{u in U_2} h_u <= (6-m)r+m-2`.

In particular, `m=6` implies `sum h_u<=4` and the total number N of d2 owners satisfies `N<=2`.

Hence **no d2 shell-support case count grows with r**. Remaining growth can only be owner multiplicity/core-support/transported-excess data inside at most fifteen fixed shell classes.

### R5. Exact d2 common-S charge identity — PROVED_SYMBOLIC

For every d2 common-S system, with `b=e_M(S)`, allowance a, and total common-S core charge W,

> `W=K+2r-2+a+b`.

If a one-loss common-hub system has three distinct core support classes, the existing pattern barrier gives

> `K+a+b>=r`.

Thus the difficult three-class d2 branch is forced into a linearly-high excess/allowance regime.

### R6. d3 closure — PROVED_CONDITIONAL

The equality B-floor removes allowance five. Every d3 local/common-S representation has `q<=3r-2`, hence `a+B<=4`. With the declared upstream low-charge absorption, no d3 terminal remains.

### R7. High Endpoint Three-Owner Theorem — PROVED_CONDITIONAL

Let `Y_hi` be all regular shell vertices with `d_y>=r-2`. Then

> `|Y_hi|<=3`

for every `r>=12`.

Four high owners force at least `4r-13` distinct shell missing edges. This contradicts `q<=3r-1` for `r>=13`; at `r=12`, equality forces hereditary equality and a 10-vertex regular target clique, contradicting the multicolor equality clique obstruction.

### R8. High Endpoint Bounded-Complement Reduction — PROVED_CONDITIONAL

For high owners put `s_y=r-d_y in {0,1,2}`. There are at most three owners, their shell interaction kernel has at most nine vertices, and core owner-incidence has at most eight signatures. The high endpoint is an r-independent finite skeleton.

### R9. Low-Endpoint Owner Clique Lemma — PROVED_SYMBOLIC

Any two regular owners with `d<=3` are target-adjacent for `r>=12`: otherwise zero-gap would require `S_x union S_y=A`, but `|S_x union S_y|<=6<r+1`.

Hence all regular low-endpoint owners, together with the pivot p, form a target clique. Since `omega(F)<=r-1`, the total number of regular low-endpoint owners is at most

> `r-2`.

This is linear, but it supplies a global owner-count cap for finite-class pigeonhole/multi-pivot arguments.

## Current theorem level

- d0: quotient-neutral.
- d1 shell geometry: at most 5 classes; core exchange closure open.
- d2 shell geometry: at most 6 support vertices / 15 classes; no r-growing shell case tree remains. Core-support and positive-loss multiplicities inside these finite classes remain open.
- d3: eliminated.
- high endpoint: at most 3 owners, finite bounded-complement skeleton.
- global potential: `(q,tau)` exact; K redundant; `Q2=sum kappa^2` is a bounded exact candidate third coordinate but monotonicity is unproved.

## Unique next blocker

**Finite-class d2 core-support multi-pivot compatibility.** Fix one of the at most fifteen shell pairs `S={u,v}`, with known shell parameters `b`, `h_u`, `h_v`, `sigma_u`, `sigma_v`, `a=h_u+h_v-b`. Prove that a family of owners in this class which is simultaneously non-improving in `(q,tau)` either admits a strict bounded-potential refinement or collapses to a finite impossible core-support skeleton. This is now the only scalable structural blocker.