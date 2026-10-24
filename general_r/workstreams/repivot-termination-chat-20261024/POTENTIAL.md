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

## 2. K is redundant with q

`K_p=2(E-q_p-(2r^2+r+1))`, hence

> **`K_y-K_p=-2(q_y-q_p)`.**

Thus K cannot be an independent coordinate. Closed q-non-improving cycles are q-flat; closed `(q,tau)`-non-improving cycles are q/tau-flat edgewise.

**Status:** `PROVED_SYMBOLIC`.

## 3. Exact third coordinate: neutral-owner population

Define

`zeta(p)=#{y in A_p:y regular and d_y=0}`

and

> **`Phi_3(p)=(q_p,tau_p,zeta(p))`.**

Zeta is bounded by `r+1` and is invariant under d0 neutral pivot relabellings.

### Exact class-neutral involution

Let

`Y_{S,D}(p)={x in A_p:x regular,S_x=S,D_x=D}`

be the complete exact class containing the repivot owner y, and let

`m=m_p(S,D)`.

Then the repivot `p -> y` satisfies the exact identities

> **`zeta(y)=m-1`,**
>
> **`m_y(D,S)=zeta(p)+1`.**

Equivalently,

> **`(m,zeta) -> (zeta+1,m-1)`**

exactly, and the transformation is an involution.

Proof: the other `m-1` class owners become d0. Conversely every d0 vertex in the y-view becomes an `(D,S)` owner after the inverse repivot, so there can be no additional d0 vertices. The reverse-class statement follows symmetrically.

### Exact zeta trichotomy on a q/tau-flat class move

Because `zeta(y)=m-1`:

- `m>=zeta(p)+2` gives strict `Phi_3` improvement;
- `m=zeta(p)+1` is exactly `Phi_3`-flat;
- `m<=zeta(p)` strictly decreases the third coordinate.

Thus at `Phi_3` maximality every q/tau-flat exact class satisfies

> **`m<=zeta+1`.**

A distinct exact class has `m=1`, so every q/tau-flat distinct-class move sends

> **`zeta -> 0`.**

Hence a genuinely `Phi_3`-flat distinct-support move is possible only in the neutral-free slice

> **`zeta=0`.**

For a repeated d2 support, both support vertices are decorated; tau-flatness then forces the shell pair S to be fully decorated as well.

**Status:** `PROVED_SYMBOLIC`.

## 4. Balanced repeated branch

If a repeated d2 class is `Phi_3`-flat, then `m=zeta+1`. The class owners, all zeta d0 owners and p form a target clique of size `2m`, so

`m<=floor((r-1)/2)`.

More generally, if k exact classes simultaneously admit `Phi_3`-flat exchanges,

> **`(k+1)(zeta+1)<=r-1`.**

The exact involution furthermore collapses each balanced repeated correction orbit, modulo d0 relabellings, to the two chamber states

`H <--> H-D+S`.

Thus repeated-support cycle length is no longer a source of complexity.

## 5. Exact fourth coordinate: plateau distance-one population

Define

`eta(p)`
` = #{ x in A_p : x is regular, d_p(x)=1,`
`      (q_x,tau_x,zeta(x))=(q_p,tau_p,zeta(p)) }`.

Eta counts the degree-one neighbours of p inside the exact `Phi_3` plateau graph. It is an integer satisfying

`0<=eta<=r+1`.

Therefore

> **`Phi_4=(q,tau,zeta,eta)`**

is a genuine bounded lexicographic potential.

### Exact d2 intersection transport

Fix a neutral-free (`zeta=0`) `Phi_3`-flat d2 common-S family with distinct core supports `D_i`.

After repivot through support `D_i`, another same-class owner with support `D_j` has exact new missing degree

> **`2-|D_i intersect D_j|`.**

Hence a one-point support overlap becomes a d1 plateau transition.

If `G_S` is the support-intersection graph, every support D satisfies

> **`eta(p_D)>=deg_(G_S)(D)`.**

At a `Phi_4`-maximal pivot p,

> **`Delta(G_S)<=eta(p)`.**

Thus arbitrary d2 overlap is paid for by an already-visible d1 plateau population. A greedy independent set in `G_S` gives a pairwise-disjoint support subfamily of size at least

> **`ceil(N/(eta+1))`.**

This is the first proved fourth-coordinate control on the distinct-support plateau.

**Status:** `PROVED_SYMBOLIC`.

## 6. Candidate fifth coordinate

On an equal-q plateau K is fixed. Define

`Q2(H)=sum_{v in H}kappa_v^2`,

so `0<=Q2<=K^2`.

For `p -> y`, put

`delta_z=e_F(z,S_y)-e_H(z,D_y)` for `z in H\D_y`.

Then

`kappa'_z=kappa_z+delta_z`,

`kappa'_s=sigma_s-e_F(s,D_y)` for `s in S_y`,

and

> `Q2(H_y)-Q2(H)`
>
> `=sum_{z in H\D_y}[2kappa_z delta_z+delta_z^2]`
>
> ` +sum_{s in S_y}[sigma_s-e_F(s,D_y)]^2`
>
> ` -sum_{u in D_y}kappa_u^2`.

Thus `(q,tau,zeta,eta,Q2)` is well-founded. Universal Q2 monotonicity is still open.

## 7. Current potential theorem

Proved:

1. `(q,tau)` is bounded and exact.
2. K is redundant with q.
3. zeta is a genuine third coordinate with an exact class-exchange update law.
4. `Phi_3`-flat class exchanges are characterized by the exact multiplicity/zeta involution.
5. distinct `Phi_3`-flat moves live only at `zeta=0`.
6. balanced repeated d2 exchanges are two-chamber involutions.
7. eta is a genuine fourth coordinate measuring d1 neighbours inside the `Phi_3` plateau.
8. d2 support overlap transports exactly into eta; at `Phi_4` maximality `Delta(G_S)<=eta`.
9. Q2 is an exact bounded fifth-coordinate candidate.

The remaining potential blocker is now narrower:

> the first scalable distinct-support terminal begins at d2 allowance `a=2`; its large disjoint clean subsystem is the rigid Clean Pair-Exchange Orbit of `A2_CLEAN_PAIR_EXCHANGE_ORBIT.md`.

The next potential question is whether Q2, or a simpler block statistic of the clean pair orbit, strictly improves unless that pair design is itself impossible.