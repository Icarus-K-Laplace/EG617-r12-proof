# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. Front extraction and anchor-excess are upstream conditional hypotheses.

## Conditional hypotheses

- **A.** Legal cores have `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; legal repivots preserve the core contract.
- **B.** `K_r>=8`.

Hence `q<=3r-1`. For `r>=12`, regular missing degrees satisfy

`d in {0,1,2,3,r-2,r-1,r}`.

The standard backend global alpha/omega caps are invoked explicitly only where stated below.

## Exact identities

`e(F)=C(r+2,2)+q+e(H)`.

`K_r=2(E-q-(2r^2+r+1))`.

`q_y=d(r+1-d)+B_y+kappa(D_y)+m(D_y)+e_F(S_y,D_y)`.

Transport:

`kappa'_z=w_z-e_H(z,D_y)`,

`kappa'_s=sigma_s-e_F(s,D_y)`.

## Proved results

### R1. q/K cycle identity — PROVED_SYMBOLIC

`K_y-K_p=-2(q_y-q_p)`.

K is redundant with q. Closed q-non-improving cycles are q-flat; closed `(q,tau)`-non-improving cycles are q/tau-flat edgewise.

### R2. d0 neutral symmetry — PROVED_SYMBOLIC

d0 repivots preserve the core, q and tau and are quotientable.

### R3. Shell-incidence budget — PROVED_CONDITIONAL

For shell `s`,

`t_s=d_M(s)+g_s=e_F(s,H)`

satisfies

`sum_A t_s=2e(M)+G_A<=6r-2`.

For a regular owner with missing set S of size d,

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`,

`sum_{s in S}t_s=d(r+1-d)+a+b`.

### R4. d1 finite shell universe — PROVED_CONDITIONAL

Every d1 missing partner has `t_s>=r`, so there are at most five d1 shell classes. Exact loss:

`q-q_y=kappa'_s-kappa_u`.

### R5. d2 Six-Point Support-Universe Theorem — PROVED_CONDITIONAL

Every endpoint of a d2 shell pair has `t>=r-1+b`. Hence the union `U_2` of all d2 shell support endpoints satisfies

`|U_2|<=6`,

so there are at most fifteen d2 shell classes.

With `h_u=t_u-(r-1)`, class allowance is

`a_{uv}=h_u+h_v-b_{uv}`.

If all six endpoints are active, `sum h<=4` and the total number of d2 owners is at most two.

### R6. Fixed-Class d2 Plateau Skeleton — PROVED_CONDITIONAL

For a fixed d2 shell class S, define

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`, `lambda_x=#{owners with x in D}`.

Every owner has

`ell=q-q_y=a-[w(D)+mu(D)]>=0`.

Incidence forces

`lambda_x>=2 or w_x>=1 => x in X`.

Let `s=|S intersect X|`.

- `s=0`: if b=0, the entire class has at most three owners; if b=1, at most one q-flat owner and at most three distinct strict support types.
- `s=1`: q-flat supports are unique and form at most three tiny star/edge components; at most six q-flat owners.
- `s=2`: the only regime where q-flat owner multiplicity can scale.

Thus the unique scalable equal-q d2 mechanism is a fixed fully decorated shell pair `S subset X`.

### R7. Genuine third coordinate zeta — PROVED_SYMBOLIC

Define

`zeta(p)=#{regular shell owners with d=0}`

and

> **`Phi_3=(q,tau,zeta)`.**

Zeta is bounded and invariant under neutral d0 repivots.

If an exact repeated `(S,D)` owner class has multiplicity m, repivoting one owner makes the other `m-1` owners d0, while all old d0 owners plus p become a reverse `(D,S)` class. Hence

`zeta(new)>=m-1`.

On a q/tau-flat move, `m>=zeta+2` strictly improves `Phi_3`. Therefore at a `Phi_3`-maximal pivot

> `m<=zeta+1`

for every q/tau-flat repeated exact class.

If equality is zeta-flat, the exchange is multiplicity-balanced.

### R8. Balanced correction-cycle capacity — PROVED_CONDITIONAL

For a `Phi_3`-flat repeated d2 class, `m=zeta+1`. The class owners, all zeta d0 owners and p form a target clique of size `2m`, hence

`m<=floor((r-1)/2)`.

If k distinct repeated exact classes simultaneously admit `Phi_3`-flat moves, then

> **`(k+1)(zeta+1)<=r-1`.**

Thus balanced repeated correction cycles have an exact neutral-population/clique-capacity tradeoff.

### R9. Missing-pair / neutral-population bound — PROVED_SYMBOLIC

For a target-nonedge core pair D, the standard common-nonneighbour argument plus p and the zeta d0 owners gives

> **`kappa(D)>=zeta-1`.**

For a q-flat d2 owner with nonedge support D,

> **`a>=zeta`.**

Hence if `a<zeta`, every q-flat d2 support must be a target edge. At equality `a=zeta`, a nonedge support collapses to a saturated common-nonneighbour template with `kappa(D)=zeta-1`, no common H target-neighbour and `e_F(S,D)=0`.

This uses the standard global `alpha(F)<=3`, `omega(F)<=r-1` backend caps.

### R10. Exact d2 common-S charge identity — PROVED_SYMBOLIC

`W=K+2r-2+a+b`.

A three-class one-loss common-hub subsystem requires `K+a+b>=r`.

### R11. d3 closure — PROVED_CONDITIONAL

The equality B-floor forces `q<=3r-2`, `a+B<=4`; the declared low-charge Bridge-B assets eliminate the remaining d3 sector.

### R12. High Endpoint Three-Owner Theorem — PROVED_CONDITIONAL

All regular owners with `d>=r-2` number at most three. Their bounded-complement encoding uses at most nine shell interaction vertices and eight core incidence signatures.

### R13. Low-owner clique lemma — PROVED_SYMBOLIC

Any two regular owners with `d<=3` are target-adjacent for `r>=12`, so together with p they form a target clique; there are at most `r-2` low owners.

## Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

The first three coordinates are genuine bounded integer coordinates; zeta has a proved strict improvement criterion on repeated q/tau plateaux.

`Q2=sum kappa^2` remains an exact bounded fourth-coordinate candidate, but universal monotonicity is not proved.

## Current theorem level

- d0: quotient-neutral.
- d1: <=5 shell classes; final core-exchange rigidity open.
- d2 shell geometry: <=6 support vertices / <=15 classes.
- d2 plateau geometry: every non-fully-decorated class is O(1)-bounded in q-flat rows; only `S subset X` can scale.
- repeated fully-decorated d2 classes: controlled by zeta; flat equality is a balanced reverse exchange satisfying the product clique bound.
- nonedge q-flat supports: require `a>=zeta` and have a rigid equality boundary.
- d3: eliminated.
- high endpoint: <=3 owners, finite bounded-complement skeleton.

## Unique next blocker

**Fully-decorated fixed-class d2 plateau compatibility.** For one shell pair `S subset X`, eliminate or rigidify (i) distinct-support q-flat systems and (ii) zeta-balanced repeated correction cycles. This is the only scalable equal-q endpoint mechanism left.