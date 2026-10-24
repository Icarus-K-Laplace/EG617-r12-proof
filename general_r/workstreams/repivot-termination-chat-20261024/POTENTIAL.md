# Repivot Potential

Conditional hypotheses: A+B. All repivots below are legal regular repivots inside one fixed residual graph F.

## 1. First two coordinates

For pivot p define

`q_p=e(M_p)+G_{A_p}`

and, with the global decorated set

`X={v in V(F):d_F(v)>r+1}`,

`tau_p=|A_p intersect X|`.

For `p -> y`,

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.

Thus `(q,tau)` is a bounded integer lexicographic potential.

---

## 2. K is redundant with q

The backend identity gives

`K_p=2(E-q_p-(2r^2+r+1))`.

Hence every repivot satisfies

> **`K_y-K_p=-2(q_y-q_p)=2(q_p-q_y)`.**

Thus K cannot be an independent potential coordinate.

On a closed repivot cycle, q-loss telescopes to zero. Therefore a closed q-non-improving cycle is q-flat edgewise; if it is non-improving in `(q,tau)`, then tau also remains flat edgewise.

Repeated non-fully-decorated support cannot occur on such a cycle.

**Status:** `PROVED_SYMBOLIC`.

---

## 3. New proved third coordinate: neutral-owner population

Define

> `zeta(p)=#{y in A_p : y is regular and d_y=0}`.

Then

> **`Phi_3(p)=(q_p,tau_p,zeta(p))`.**

This is a bounded integer lexicographic potential because `0<=zeta<=r+1`.

### d0 invariance

Repivoting through a d0 owner only swaps the two regular pivots. Every other d0 owner remains d0 and the old pivot becomes d0. Therefore

> `zeta(y)=zeta(p)`

on a d0 neutral repivot.

So zeta descends to the quotient by neutral pivot relabellings.

### Repeated-class exchange duality

Suppose y lies in an exact repeated owner class with common pair `(S,D)` and multiplicity m:

`S_x=S`, `D_x=D`

for every owner x in the class.

After repivoting through y:

- every other one of the `m-1` owners becomes d0;
- every old d0 owner becomes a reverse `(D,S)` owner;
- the old pivot p also becomes a reverse `(D,S)` owner.

Hence

> **`zeta(y)>=m-1`.**

Therefore, if the move is q-flat and tau-flat and

`m>=zeta(p)+2`,

then

> **`Phi_3(y)>_lex Phi_3(p)`.**

At a `Phi_3`-maximal pivot:

> **every q/tau-flat exact repeated class has multiplicity `m<=zeta+1`.**   (3.1)

This is a genuine monotonicity theorem, not merely a candidate coordinate.

### Equality rigidity

If `m=zeta+1` and the repivot is `Phi_3`-flat, then the `m-1` surviving owners from the repeated class account for the entire new d0 population. Simultaneously, the reverse `(D,S)` class has multiplicity at least `zeta+1=m`.

Thus a closed `Phi_3`-flat repeated-class correction cycle must satisfy exact multiplicity balance at every class exchange.

For d2, repeated support decorates both vertices of D. Tau-flatness then forces both shell endpoints in S to be decorated as well. Hence every `Phi_3`-flat repeated d2 exchange lies in the unique fully-decorated shell-pair regime.

**Status:** coordinate bounded/exact and repeated-class improvement criterion `PROVED_SYMBOLIC`; balanced-cycle elimination `OPEN`.

---

## 4. Excess concentration as a candidate fourth coordinate

On an equal-q plateau, K is fixed. Define

`Q2(H)=sum_{v in H}kappa_v^2`.

For fixed K,

`0<=Q2<=K^2`.

For `p -> y`, put

`delta_z=e_F(z,S_y)-e_H(z,D_y)`

for `z in H\D_y`. Then

`kappa'_z=kappa_z+delta_z`,

and for `s in S_y`,

`kappa'_s=sigma_s-e_F(s,D_y)`.

Therefore

> `Q2(H_y)-Q2(H)`
>
> `=sum_{z in H\D_y}[2kappa_z delta_z+delta_z^2]`
>
> ` +sum_{s in S_y}[sigma_s-e_F(s,D_y)]^2`
>
> ` -sum_{u in D_y}kappa_u^2`.

Thus

`(q,tau,zeta,Q2)`

is a well-founded candidate refinement.

Universal monotonicity of Q2 on `Phi_3`-flat moves is not proved.

**Status:** exact/bounded `PROVED_SYMBOLIC`; universal improvement `OPEN`.

---

## 5. Positive-loss transport

If `ell=q_p-q_y`, then

`K_y-K_p=2ell`.

Thus positive q-loss raises the new-core total excess. A proof restricted to the `K=8` plateau cannot control positive-loss moves.

Conversely q-flat moves preserve K, so all remaining potential work on such moves is redistribution at fixed total excess.

---

## 6. Current potential theorem

Proved:

1. `(q,tau)` is bounded and exact.
2. K is redundant with q.
3. every closed `(q,tau)`-non-improving cycle is simultaneous q/tau equality.
4. repeated non-fully-decorated support cannot lie on such a plateau cycle.
5. `zeta` is a genuine third coordinate with a proved repeated-class improvement criterion.
6. at `Phi_3` maximality, any q/tau-flat repeated class has multiplicity at most `zeta+1`; equality is a rigid reverse-class / neutral-population exchange.
7. `Q2` is an exact bounded candidate fourth coordinate.

Remaining potential blocker:

> classify `Phi_3`-flat fully-decorated d2 systems, separating (i) distinct-support systems from (ii) zeta-balanced repeated-class correction cycles, and prove either Q2 or another bounded incidence coordinate strictly improves outside a finite rigid skeleton.