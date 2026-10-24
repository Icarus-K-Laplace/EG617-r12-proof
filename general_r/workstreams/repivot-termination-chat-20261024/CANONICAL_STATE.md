# Canonical State — General-r Repivot Termination

Branch: `workstream/general-r-repivot-termination-20261024`

Scope: backend termination only. Front extraction and anchor-excess are upstream conditional hypotheses.

## Conditional hypotheses

- **A.** Legal cores have `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`; legal repivots preserve the core contract.
- **B.** `K_r>=8`.

The symbolic backend setup additionally has

- `alpha(F)<=4`;
- `omega(F)<=r-1`.

**Important audited distinction:** the global independence cap is `alpha(F)<=4`, not `alpha(F)<=3`. Arguments forbidding independent 4-sets in F are invalid and are not part of the canonical state. Independent 4-sets are forbidden only when all four vertices lie in a legal core H, where `alpha(H)<=3`.

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

For the complete exact class `Y_{S,D}(p)` of multiplicity m containing a repivot owner y, the exchange is exact:

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
- `a=1`: at most **9** distinct q-flat supports (sharpening the earlier coarse bound12);
- for `a>=2`, matching number satisfies the valid weighted bound
  `nu(Q)(a-1)<=W<=4r+9-a`;
- the `a=2` branch reduces to at most three zero-weight support vertices plus a maximum-degree-three `(1,1)` target-support subgraph;
- a hereditary owner/support capacity inequality is available in its stated induced-set range.

The stronger allowance-independent matching-three claim has been **retracted** because it incorrectly assumed `alpha(F)<=3`.

### R15. Exact fourth coordinate eta / intersection-to-d1 transport — PROVED_SYMBOLIC

Define

`eta(p)=#{regular d1 shell owners x with (q_x,tau_x,zeta(x))=(q_p,tau_p,zeta(p))}`.

Then

> **`Phi_4=(q,tau,zeta,eta)`**

is a bounded integer lexicographic potential.

For one neutral-free distinct d2 common-S plateau, let `G_S` be the support-intersection graph. The exact pair-set exchange gives

`d_i(y_j)=2-|D_i intersect D_j|`.

Hence one-point overlaps become d1 plateau transitions. At a `Phi_4`-maximal pivot,

> **`Delta(G_S)<=eta`.**

Therefore the fixed class contains a pairwise-disjoint q-flat support subfamily of size at least

> **`ceil(N/(eta+1))`.**

So d2 overlap complexity is no longer independent: it is charged to the d1 plateau population.

### R16. d1 scale-transfer inequality — PROVED_CONDITIONAL

The eta population lies in at most five d1 shell classes. One class has size

`N_1>=ceil(eta/5)`.

In the neutral-free plateau slice its singleton core supports are distinct. If c is that d1 class allowance, then

`N_1 c<=K+r+c`.

Under the inherited hereditary core cap `K<=2r-2`,

> **`(N_1-1)c<=3r-2`.**

If `c=0`, row closure gives `N_1<=3`.

Hence a linear eta population forces a linear d1 class with absolute-constant allowance.

### R17. Allowance-2 Clean Pair-Exchange Orbit — PROVED_CONDITIONAL

Inside any pairwise-disjoint q-flat `a=2` d2 subfamily, at most three supports contain a zero-weight endpoint. Every other support is a clean target K2 with endpoint weights `(1,1)`.

If a clean support `D_i` is used for repivot, every other disjoint clean support `D_j` remains

- d2;
- q/tau/zeta-flat;
- a target K2;
- endpoint weights exactly `(1,1)` relative to the new shell pair `D_i`.

Thus the large clean subsystem is repivot-closed under exchanging the distinguished shell pair with any clean core pair.

Between two clean blocks the target cross graph is a matching of size0,1,or2. Consequently every scalable `a=2` branch contains a large rigid terminal of the form

> **clean pair-exchange design + O(1) zero-containing special blocks.**

This is the first genuinely scalable design terminal extracted from the backend.

## Explicit retractions from the canonical theory

The file `D2_MISSING_PAIR_NEUTRAL_BOUND.md` is retained as a negative audit certificate. Its claimed consequences

`kappa(D)>=zeta-1` and `a>=zeta`

are **not validly proved** under the actual global cap `alpha(F)<=4` and must not be used.

Likewise `D2_DISTINCT_MATCHING_COLLAPSE.md` is marked `DISPROVED_AS_STATED`; its claimed `nu(Q)<=3` and six-hub collapse are not canonical results.

## Potential status

Current preferred potential:

> **`Phi_4=(q,tau,zeta,eta)`.**

All four coordinates are genuine bounded integers. Eta controls support overlap by converting one-point d2 overlaps exactly into d1 plateau transitions.

`Q2=sum kappa^2` remains an exact bounded fifth-coordinate candidate, but universal monotonicity is not proved.

## Current theorem level

- d0: quotient-neutral.
- d1: <=5 shell classes; any linear eta concentration has bounded allowance; final d1 core-exchange rigidity remains open.
- d2 shell geometry: <=6 support vertices / <=15 classes.
- d2 plateau geometry: every non-fully-decorated class is O(1)-bounded in q-flat rows; only `S subset X` can scale.
- repeated fully-decorated d2 classes: either improve zeta or collapse to the Balanced Two-Chamber family.
- distinct fully-decorated d2 classes: `a=0,1` absolutely bounded; d2 overlap is controlled by eta; `a=2` contains a large repivot-closed clean pair design; higher allowance obeys weighted matching compression.
- d3: eliminated.
- high endpoint: <=3 owners, finite bounded-complement skeleton.

## Unique next blocker

**Clean Pair Nonextension / bounded-allowance d1 terminal.** Prove that a sufficiently large repivot-closed clean K2 pair system with matching cross graphs and no independent 4-transversal is incompatible with the hereditary/clique/multicolor constraints, or else derive a fifth-coordinate improvement. In parallel this same theorem should absorb the bounded-allowance d1 concentration forced by eta.