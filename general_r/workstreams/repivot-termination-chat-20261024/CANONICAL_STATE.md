# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. Front extraction and anchor-excess are upstream conditional hypotheses.

## Conditional hypotheses

- **A.** Legal cores have `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; legal repivots preserve the core contract.
- **B.** `K_r>=8`.

The symbolic backend setup additionally has

- `alpha(F)<=4`;
- `omega(F)<=r-1`.

**Important audited distinction:** the global independence cap is `alpha(F)<=4`, not `alpha(F)<=3`. Arguments forbidding independent 4-sets in F are invalid and are not part of the canonical state.

Hence `q<=3r-1`. For `r>=12`, regular missing degrees satisfy

`d in {0,1,2,3,r-2,r-1,r}`.

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

`t_s=d_M(s)+g_s=e_F(s,H)`,

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

### R7. Genuine third coordinate zeta / exact class-neutral involution — PROVED_SYMBOLIC

Define

`zeta(p)=#{regular shell owners with d=0}`

and

> **`Phi_3=(q,tau,zeta)`.**

For the complete exact class `Y_{S,D}(p)` of multiplicity m containing the repivot owner y, the exchange is exact:

> **`zeta(y)=m-1`,**
>
> **`m_y(D,S)=zeta(p)+1`.**

Thus `(m,zeta)->(zeta+1,m-1)` is an involution.

On a q/tau-flat move:

- `m>=zeta+2` strictly improves `Phi_3`;
- `m=zeta+1` is exactly `Phi_3`-flat;
- `m<=zeta` lowers the third coordinate.

In particular, an exact distinct class (`m=1`) sends `zeta` exactly to zero. A genuinely `Phi_3`-flat distinct-support move therefore lies in the neutral-free slice `zeta=0`.

### R8. Balanced repeated-class capacity — PROVED_CONDITIONAL

A `Phi_3`-flat repeated d2 class has `m=zeta+1`. Its owners, all zeta d0 owners and p form a target clique of size `2m`, hence

`m<=floor((r-1)/2)`.

If k distinct repeated exact classes simultaneously admit `Phi_3`-flat moves, then

> **`(k+1)(zeta+1)<=r-1`.**

### R9. Balanced Two-Chamber Correction Theorem — PROVED_CONDITIONAL

For a `Phi_3`-flat exact repeated d2 class, let

`C_0={p} union Z_0(p)`, `C_1=Y_{S,D}`.

Then `|C_0|=|C_1|=m=zeta+1` and `F[C_0 union C_1]=K_(2m)`.

Modulo d0-neutral pivot relabellings, the entire repeated correction orbit has only two states:

> **Chamber 0:** core H, exact class `(S,D)` on C1;
>
> **Chamber 1:** core `H'=(H\D) union S`, exact reverse class `(D,S)` on C0.

Thus every balanced repeated correction cycle collapses to

> **`H <--> H'`.**

The allowance a is invariant. If `b=e_M(S)` and `mu=1-e_H(D)`, the chambers exchange `b <-> mu`, and

`kappa_H(D)-kappa_(H')(S)=b-mu`.

### R10. Exact d2 common-S charge identity — PROVED_SYMBOLIC

`W=K+2r-2+a+b`.

A three-class one-loss common-hub subsystem requires `K+a+b>=r`.

### R11. d3 closure — PROVED_CONDITIONAL

The equality B-floor forces `q<=3r-2`, `a+B<=4`; the declared low-charge Bridge-B assets eliminate the remaining d3 sector.

### R12. High Endpoint Three-Owner Theorem — PROVED_CONDITIONAL

All regular owners with `d>=r-2` number at most three. Their bounded-complement encoding uses at most nine shell interaction vertices and eight core incidence signatures.

### R13. Low-owner clique lemma — PROVED_SYMBOLIC

Any two regular owners with `d<=3` are target-adjacent for `r>=12`, by the zero-gap relation: nonadjacency would require `S_x union S_y=A`, impossible when both support sizes are at most3. Hence together with p they form a target clique; there are at most `r-2` low owners.

### R14. Distinct fully-decorated d2 low-allowance reduction — PROVED_CONDITIONAL

For a fixed fully decorated d2 shell class in the genuine `Phi_3`-flat distinct slice (`zeta=0`), let Q be the graph of distinct core supports. Then

- exact transition identity: after repivot through support `D_i`, another same-class support `D_j` has new missing degree `2-|D_i intersect D_j|`;
- `a=0`: at most 3 distinct q-flat supports;
- `a=1`: at most 12 distinct q-flat supports;
- for `a>=2`, matching number satisfies the valid weighted bound
  `nu(Q)(a-1)<=W<=4r+9-a`;
- the `a=2` branch reduces to at most three zero-weight hubs plus a maximum-degree-three `(1,1)` target-support subgraph;
- a hereditary owner/support capacity inequality is available in its stated induced-set range.

The stronger allowance-independent matching-three claim has been **retracted** because it incorrectly assumed `alpha(F)<=3`.

## Explicit retractions from the canonical theory

The file `D2_MISSING_PAIR_NEUTRAL_BOUND.md` is retained as a negative audit certificate. Its claimed consequences

`kappa(D)>=zeta-1` and `a>=zeta`

are **not validly proved** under the actual global cap `alpha(F)<=4` and must not be used.

Likewise `D2_DISTINCT_MATCHING_COLLAPSE.md` is marked `DISPROVED_AS_STATED`; its claimed `nu(Q)<=3` and six-hub collapse are not canonical results.

## Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

The first three coordinates are genuine bounded integer coordinates; zeta has an exact update law on every exact class exchange.

`Q2=sum kappa^2` remains an exact bounded fourth-coordinate candidate, but universal monotonicity is not proved.

## Current theorem level

- d0: quotient-neutral.
- d1: <=5 shell classes; final core-exchange rigidity open.
- d2 shell geometry: <=6 support vertices / <=15 classes.
- d2 plateau geometry: every non-fully-decorated class is O(1)-bounded in q-flat rows; only `S subset X` can scale.
- repeated fully-decorated d2 classes: either improve zeta or collapse to the Balanced Two-Chamber family.
- distinct fully-decorated d2 classes: `a=0,1` absolutely bounded; `a>=2` remains the principal scalable branch, with weighted matching/hereditary constraints.
- d3: eliminated.
- high endpoint: <=3 owners, finite bounded-complement skeleton.

## Unique next blocker

**Fully-decorated distinct-support d2 plateau for allowance `a>=2`.** The repeated branch is already two-chamber. The valid next step is to close the `a=2` max-degree-three support graph or prove a general weighted matching/row-closure compression without assuming `alpha(F)<=3`.