# Termination Theorem

## Target

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

The final contradiction theorem is **OPEN**. What is now proved is a fixed-width endpoint theorem plus a genuine third potential coordinate and a two-state classification of the repeated correction-cycle branch.

---

# Theorem A — Conditional Fixed-Width Endpoint Compression

Assume A+B and `r>=12`.

Every regular shell owner has

`d in {0,1,2,3,r-2,r-1,r}`.

Moreover:

1. d0 is neutral and quotientable;
2. d1 missing partners lie in at most five shell classes;
3. all d2 shell missing-set endpoints lie in at most six vertices, hence at most fifteen shell classes;
4. d3 is eliminated by the equality B-floor plus the declared low-charge Bridge-B absorption;
5. all high owners `d>=r-2` number at most three and form a bounded-complement kernel.

Thus the shell-side endpoint type count is absolute-constant in r.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem B — Shell-Incidence Kernel

For shell vertices

`t_s=d_M(s)+g_s=e_F(s,H)`

one has

`sum_A t_s=2e(M)+G_A<=6r-2`.

For every regular owner with missing set S of size d,

`sigma_s=t_s-(r+1-d)-m_S(s)>=0`,

`sum_{s in S}t_s=d(r+1-d)+a+b`.

Consequences:

- d1 support universe <=5;
- d2 support universe <=6, hence <=15 pair classes;
- for d2, `a_{uv}=h_u+h_v-b_{uv}`, `h_u=t_u-(r-1)`;
- if all six d2 endpoints are active, `sum h<=4` and there are at most two d2 owners total.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem C — Fixed-Class d2 Plateau Reduction

Fix one d2 shell class `S={u,v}`. Put

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`.

Every owner has exact loss

> `ell_y=q-q_y=a-[w(D_y)+mu(D_y)]>=0`.

Support incidence `lambda_x` satisfies

> `lambda_x>=2 or w_x>=1 => x in X`.

Let `s=|S intersect X|`.

- `s=0`: if b=0, the whole class has at most three owners; if b=1, at most one q-flat owner and at most three strict support types.
- `s=1`: q-flat supports are unique and form at most three star/edge components, hence at most six q-flat owners.
- `s=2`: the only regime where q-flat owner multiplicity can scale.

Therefore

> **the unique scalable equal-q d2 mechanism is a fixed fully-decorated shell pair `S subset X`.**

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem D — High Endpoint Three-Owner Reduction

All regular owners with `d>=r-2` number at most three. Their bounded-complement encoding has at most nine shell interaction vertices and eight core incidence signatures.

**Status:** `PROVED_CONDITIONAL`.

This achieves Level 3 high-endpoint reduction.

---

# Theorem E — Genuine third potential coordinate

Define

`zeta(p)=#{regular shell owners with d=0}`

and

> **`Phi_3=(q,tau,zeta)`.**

Zeta is bounded and invariant under d0 neutral relabellings.

If an exact repeated `(S,D)` class has multiplicity m, repivoting one owner makes the other `m-1` owners d0, while every old d0 owner together with p becomes a reverse `(D,S)` owner. Hence

`zeta(new)>=m-1`.

Thus on a q/tau-flat move,

> `m>=zeta+2 =>` strict `Phi_3` improvement.

At `Phi_3` maximality,

> `m<=zeta+1`.

If k distinct exact repeated classes admit `Phi_3`-flat exchanges, every one has multiplicity `zeta+1` and

> **`(k+1)(zeta+1)<=r-1`.**

**Status:** zeta monotonicity `PROVED_SYMBOLIC`; clique-capacity product bound `PROVED_CONDITIONAL`.

Full Level 4 is not yet certified because distinct-support plateau moves remain.

---

# Theorem F — Balanced Two-Chamber Correction Theorem

Suppose a repeated d2 exact class is `Phi_3`-flat. Put

`m=zeta+1`,

`C_0={p} union Z_0(p)`,

`C_1=Y_{S,D}`.

Then

`|C_0|=|C_1|=m`,

`F[C_0 union C_1]=K_(2m)`.

All pivots in C0 are d0-neutral representatives of one core state H. All pivots in C1 are d0-neutral representatives of the reverse core state

`H'=(H\D) union S`.

Modulo neutral relabellings, the entire repeated correction orbit is therefore exactly

> **`H <--> H'`.**

No longer correction cycle exists in this branch.

The d2 allowance is invariant:

> `a_reverse=a_forward`.

If

`b=e_M(S)`, `mu=1-e_H(D)`,

then the two chambers exchange

`b <-> mu`

and the exchanged-pair excess satisfies

> `kappa_H(D)-kappa_(H')(S)=b-mu`.

Thus the repeated correction-cycle problem is compressed to one symbolic two-chamber terminal family with

`m<=floor((r-1)/2)`.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem G — Missing-Pair / Neutral-Population Bound

For a target-nonedge core pair D, its common H-nonneighbour clique has size at least

`r-3-kappa(D)`.

Adding p and all zeta d0 owners and using the global clique cap gives

> **`kappa(D)>=zeta-1`.**

If D supports a q-flat d2 owner of allowance a, then

> **`a>=zeta`.**

Hence if `a<zeta`, every q-flat d2 support is a target edge.

At `a=zeta`, a nonedge support has the rigid boundary

- `kappa(D)=zeta-1`;
- no common H target-neighbour;
- `e_F(S,D)=0`;
- saturated common-nonneighbour clique.

**Status:** `PROVED_SYMBOLIC` under the standard global alpha/omega caps.

---

# Theorem H — d2 scalar/core-support barrier

For every d2 common-S system,

> `W=K+2r-2+a+b`.

A three-class exact-one-loss common-hub subsystem requires

> `K+a+b>=r`.

**Status:** identity `PROVED_SYMBOLIC`; barrier `PROVED_CONDITIONAL`.

---

# Theorem I — Plateau cycle rigidity

A closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. Repeated-class edges are controlled by zeta. When zeta is also flat, Theorem F shows that the repeated part of the cycle has only two quotient states.

Therefore the only correction-cycle complexity not already collapsed to a two-state involution must come from **distinct-support fully-decorated d2 moves**.

**Status:** `PROVED_SYMBOLIC` / `PROVED_CONDITIONAL` as above.

---

# Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

The first three coordinates are genuine bounded integer coordinates, and zeta has a proved strict-improvement theorem on repeated q/tau plateaux.

The exact bounded candidate fourth coordinate remains

`Q2=sum_{v in H}kappa_v^2`.

Universal Q2 monotonicity is open.

A fourth coordinate is now needed primarily for the **distinct-support fully-decorated d2 plateau**. The repeated branch is already a single symbolic two-chamber terminal.

---

# Remaining route to Level 4 / Level 5

The only scalable source of new combinatorial complexity is:

> a fixed fully decorated d2 shell pair `S subset X` with many **distinct** q-flat core 2-supports.

The repeated part has already collapsed to the Balanced Two-Chamber family. Nonedge supports require `a>=zeta`; below that threshold only target-edge supports survive.

The next target is therefore:

> **Fully-Decorated Distinct-Support Theorem.** For a fixed decorated pair S, every `Phi_3`-maximal family of distinct q-flat supports either admits a strict fourth-coordinate improvement or collapses to a finite weighted support skeleton.

After that theorem, only two bounded symbolic terminals remain to kill:

1. the finite distinct-support skeleton;
2. the Balanced Two-Chamber Correction Block.

A hereditary/equality contradiction for those terminals would yield the desired all-large-r theorem.

---

# Certified success level

- Level 1: d3 closure obtained.
- Level 2: full low-endpoint elimination not yet; all non-fully-decorated d2 plateau classes are O(1)-bounded.
- **Level 3: achieved** — high endpoint is a finite three-owner bounded-complement skeleton.
- Level 4: not yet achieved, but `Phi_3=(q,tau,zeta)` is a genuine three-coordinate potential with a proved repeated-support improvement theorem.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **Fully-decorated distinct-support d2 plateau theorem.** The repeated correction-cycle branch has been compressed to a single two-chamber symbolic terminal; distinct q-flat supports are the only remaining scalable combinatorial mechanism.