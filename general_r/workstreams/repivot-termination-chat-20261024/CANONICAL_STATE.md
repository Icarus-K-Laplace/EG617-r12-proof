# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. Front extraction and anchor-excess are upstream conditional hypotheses.

## Conditional hypotheses

- **A (residual-core contract).** Every legal backend view has a core `H` with `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; every legal regular repivot again has a valid core with minimum degree at least r.
- **B (anchor excess).** Every legal core satisfies `K_r>=8`.

Hence `q<=3r-1`. For `r>=12`, no regular missing degree `4<=d<=r-3` is possible, so

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

## Proved results

### R1. Plateau transport / cycle identity — PROVED_SYMBOLIC

`K_y-K_p=-2(q_y-q_p)`. Hence K is affine-redundant with q. Every closed q-non-improving cycle is q-flat; every closed `(q,tau)`-non-improving cycle is q-flat and tau-flat edgewise. Repeated non-fully-decorated supports cannot occur on such a plateau cycle.

### R2. d0 neutral symmetry — PROVED_SYMBOLIC

For d=0, `S=D=empty`; H, q and tau are unchanged. Contract these pivot relabellings.

### R3. Global shell-incidence budget — PROVED_CONDITIONAL

For `s in A`, define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Then

`sum_A t_s=2e(M)+G_A=2q-G_A<=6r-2`.

For any regular owner with missing set S of size d,

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`

for every `s in S`, and

`sum_{s in S}t_s=d(r+1-d)+a+b`.

### R4. d1 finite shell-support reduction — PROVED_CONDITIONAL

Every d1 missing partner satisfies `t_s>=r`; hence all d1 shell supports lie in at most five vertices/classes. For `S={s}`, `D={u}`,

`q-q_y=kappa'_s-kappa_u`.

Final q/tau-flat one-point exchange rigidity remains open.

### R5. d2 Six-Point Support-Universe Theorem — PROVED_CONDITIONAL

For a d2 shell pair `S={u,v}` with `b=e_M(S)`, both endpoints satisfy

`t_u,t_v>=r-1+b`.

Thus the union `U_2` of all d2 shell support endpoints has

> `|U_2|<=6`,

and there are at most

> `C(6,2)=15`

d2 shell classes, independent of r.

Writing `h_u=t_u-(r-1)`, every class has exact allowance

`a_{uv}=h_u+h_v-b_{uv}`.

If `m=|U_2|`, then

`sum h_u<=(6-m)r+m-2`.

At `m=6`, `sum h_u<=4` and the total d2 owner count is at most two.

### R6. Fixed-Class d2 Plateau Skeleton — PROVED_CONDITIONAL

Fix one d2 shell class `S={u,v}` and all its owners Y. Put

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`, and `lambda_x=#{y:x in D_y}`.

Every owner has exact loss

> `ell_y=q-q_y=a-[w(D_y)+mu(D_y)]>=0`.

Support incidence forces

> `lambda_x>=2 or w_x>=1 => x in X`.

Let `s=|S intersect X|`.

- **s=0:** common-S transport forces `a=b`. If `b=0`, every owner is q-flat and `|Y|<=3`. If `b=1`, there is at most one q-flat owner; strict support types are at most three.
- **s=1:** q-flat supports cannot repeat. Their graph is a disjoint union of at most three components, each an isolated edge or a star with at most two edges. Hence there are at most six q-flat owners.
- **s=2:** this is the only class in which q-flat owner multiplicity can scale with r.

Therefore the unique scalable equal-q d2 regime is

> **a fixed shell pair `S subset X` whose two shell endpoints are both globally decorated.**

The exact class defect sum is

`sum_y ell_y = Na - sum_x lambda_x w_x - sum_y mu(D_y)`.

For `s<=1`, if `F0` is the q-flat owner count, `F0<=6`, so

`sum_x lambda_x w_x + sum_y mu(D_y) <= N(a-1)+F0`.

### R7. Exact d2 common-S charge identity — PROVED_SYMBOLIC

For every d2 common-S system,

> `W=K+2r-2+a+b`.

If a one-loss common-hub subsystem has three distinct core support classes, the existing pattern barrier gives

> `K+a+b>=r`.

### R8. d3 closure — PROVED_CONDITIONAL

The equality B-floor removes allowance five. Every d3 local/common-S representation has `q<=3r-2`, hence `a+B<=4`. With the declared upstream low-charge absorption, no d3 terminal remains.

### R9. High Endpoint Three-Owner Theorem — PROVED_CONDITIONAL

Let `Y_hi` be all regular shell vertices with `d_y>=r-2`. Then

> `|Y_hi|<=3`

for every `r>=12`.

Four high owners force at least `4r-13` distinct shell missing edges. This contradicts `q<=3r-1` for `r>=13`; at r=12 equality forces hereditary equality and a 10-vertex regular target clique, contradicting the multicolor equality clique obstruction.

### R10. High Endpoint Bounded-Complement Reduction — PROVED_CONDITIONAL

For high owners put `s_y=r-d_y in {0,1,2}`. There are at most three owners, their shell interaction kernel has at most nine vertices, and core owner-incidence has at most eight signatures. The high endpoint is an r-independent finite skeleton.

### R11. Low-Endpoint Owner Clique Lemma — PROVED_SYMBOLIC

Any two regular owners with `d<=3` are target-adjacent for `r>=12`; otherwise zero-gap would require `S_x union S_y=A`, but the union has size at most six. Hence all regular low-endpoint owners together with p form a target clique, so there are at most `r-2` low owners.

## Current theorem level

- d0: quotient-neutral.
- d1: <=5 shell classes; core exchange closure open.
- d2 shell geometry: <=6 support vertices / <=15 classes.
- d2 q-flat geometry: every non-fully-decorated fixed class has an absolute q-flat bound; only a fully decorated shell pair can carry scalable q-flat multiplicity.
- d3: eliminated.
- high endpoint: <=3 owners, finite bounded-complement skeleton.
- global potential: `(q,tau)` exact; K redundant; `Q2=sum kappa^2` is an exact bounded third-coordinate candidate but monotonicity is unproved.

## Unique next blocker

**Fully-decorated fixed-class d2 plateau compatibility.** Fix one d2 shell pair `S={u,v} subset X`. Prove that a scalable family of q-flat owners with core 2-supports `D_y` either yields a strict bounded-potential refinement or collapses to a finite impossible repeated-support / incidence skeleton. This is now the only scalable equal-q d2 mechanism.