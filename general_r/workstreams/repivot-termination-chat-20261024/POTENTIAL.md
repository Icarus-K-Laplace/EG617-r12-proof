# Repivot Potential

Conditional hypotheses: A+B. All repivots below are legal regular repivots inside one fixed residual graph F.

## 1. The first two coordinates

For a pivot p define

`q_p=e(M_p)+G_{A_p}`

and, with the global decorated set

`X={v in V(F): d_F(v)>r+1}`,

`tau_p=|A_p intersect X|`.

For `p -> y`,

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.

Therefore

`Psi_2(p)=(q_p,tau_p)`

is a bounded integer lexicographic potential.

The existing repeated-support theorem says that an equal-q repivot through a repeated support whose shell missing set is not fully decorated strictly increases tau.

---

## 2. Exact transported-excess / q duality

The backend identity in a fixed residual graph F is

`K_p=2(E-q_p-(2r^2+r+1))`.

Therefore every repivot satisfies the exact identity

> **`K_y-K_p=-2(q_y-q_p)=2(q_p-q_y)`.**

If we define the signed q-loss

`ell(p,y)=q_p-q_y`,

then

> **`Delta K=2 ell`.**

### Consequence: K is not a new potential coordinate

At fixed F, K is an affine decreasing function of q. Appending K to `(q,tau)` adds no information. Any genuine refinement must distinguish equal-q states.

**Status:** `PROVED_SYMBOLIC`.

---

## 3. Closed-cycle telescoping lemma

Consider a closed legal repivot cycle

`p_0 -> p_1 -> ... -> p_m=p_0`.

Then

`sum_i ell(p_i,p_{i+1})=sum_i(q_i-q_{i+1})=0`.

Equivalently,

`sum_i (K_{i+1}-K_i)=0`.

Hence:

### q-flat cycle rigidity

If every step is q-non-improving,

`q_{i+1}<=q_i`,

then every step is equality:

`q_{i+1}=q_i` and `K_{i+1}=K_i`.

### (q,tau)-flat cycle rigidity

If every step is lexicographically non-improving in `(q,tau)`, then the first conclusion makes q constant, after which

`tau_{i+1}<=tau_i`

around a closed cycle forces tau constant at every step.

Thus every closed non-improving cycle lies entirely on the simultaneous `(q,tau)` plateau.

Now apply repeated-support strict loss: such a cycle cannot contain an equal-q repivot through a repeated support D whose corresponding shell missing set S is not fully decorated. Therefore every repeated support used on a non-improving closed cycle must be fully decorated on both sides of the transport.

> **Plateau Cycle Rigidity Lemma.** Every closed `(q,tau)`-non-improving repivot cycle consists entirely of q-flat, tau-flat moves, and every repeated plateau support occurring on the cycle has a fully decorated shell partner.

**Status:** `PROVED_SYMBOLIC`.

This does not yet exclude all cycles, but it converts the cycle problem into simultaneous equality classification.

---

## 4. Exact candidate third coordinate: excess concentration

On an equal-q plateau, K is fixed. Define

`Q2(H)=sum_{v in H} kappa_v^2`,

where `kappa_v=d_H(v)-r>=0`.

For fixed K this is an integer satisfying

`0<=Q2<=K^2`,

so it is a legitimate bounded coordinate.

For a repivot `p -> y`, set for `z in H\D_y`

`delta_z=e_F(z,S_y)-e_H(z,D_y)`.

Then

`kappa'_z=kappa_z+delta_z`.

For `s in S_y`,

`kappa'_s=sigma_s-e_F(s,D_y)`.

Therefore the exact update is

> `Q2(H_y)-Q2(H)`
>
> `= sum_{z in H\D_y} [2 kappa_z delta_z + delta_z^2]`
>
> `  + sum_{s in S_y} [sigma_s-e_F(s,D_y)]^2`
>
> `  - sum_{u in D_y} kappa_u^2`.

No hidden asymptotic term occurs.

This makes

`Phi_3=(q,tau,Q2)`

a well-founded candidate lexicographic potential.

However monotonicity of Q2 on every non-rigid equal-(q,tau) repivot is **not proved**. In particular, transport may disperse excess rather than concentrate it.

**Status of coordinate:** exact/bounded = `PROVED_SYMBOLIC`; universal improvement = `OPEN`.

---

## 5. Why positive-loss transport is automatically accounted for

The exact relation

`Delta K=2 ell`

shows that a q-loss move necessarily raises the new-core total excess by twice the q loss. Therefore a proof that reasons only about the `K=8` plateau cannot control q-losing repivots.

Conversely, on q-flat moves `Delta K=0`, so all transported-excess identities become a redistribution problem at fixed total excess. This is precisely the regime where a concentration coordinate such as Q2, signature multiplicity, or support-overlap rank can add information.

---

## 6. Current potential theorem

What is proved:

1. `(q,tau)` is bounded and exact.
2. K is redundant with q.
3. every closed non-improving cycle is simultaneous q/tau equality.
4. repeated non-fully-decorated support cannot occur on such a cycle.
5. `Q2` is a bounded exact third-coordinate candidate with a closed update formula.

What remains:

> **Plateau Refinement Blocker.** Show that every equal-(q,tau) non-rigid move either strictly increases one explicit bounded coordinate (Q2 or a sharper signature/overlap coordinate) or belongs to one of the rigid endpoint kernels listed in `RIGID_EQUALITY_CASES.md`.
