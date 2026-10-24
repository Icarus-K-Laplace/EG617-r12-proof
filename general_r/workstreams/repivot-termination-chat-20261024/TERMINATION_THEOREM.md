# Termination Theorem

## Target

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

The final contradiction theorem is **OPEN**.

The audited backend setup is

- `alpha(F)<=4`, `omega(F)<=r-1`;
- core `H` has `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

Independent 4-sets in F are **not** forbidden. All statements below respect this distinction.

---

# Theorem A — Conditional Fixed-Width Shell Endpoint Compression

Assume A+B and `r>=12`.

Every regular shell owner has

`d in {0,1,2,3,r-2,r-1,r}`.

Moreover:

1. d0 is neutral and quotientable;
2. d1 missing partners lie in at most five shell classes;
3. all d2 shell missing-set endpoints lie in at most six vertices, hence at most fifteen shell classes;
4. d3 is eliminated by the equality B-floor plus the declared low-charge Bridge-B absorption;
5. all high owners `d>=r-2` number at most three and form a bounded-complement kernel.

Thus the **shell-side** endpoint type count is absolute-constant in r.

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

# Theorem E — Exact third potential coordinate

Define

`zeta(p)=#{regular shell owners with d=0}`

and

> **`Phi_3=(q,tau,zeta)`.**

For the complete exact class `Y_{S,D}(p)` of multiplicity m containing a repivot owner y,

> **`zeta(y)=m-1`,**
>
> **`m_y(D,S)=zeta(p)+1`.**

Thus `(m,zeta)->(zeta+1,m-1)` is an exact involution.

On a q/tau-flat move:

- `m>=zeta+2` strictly improves `Phi_3`;
- `m=zeta+1` is exactly `Phi_3`-flat;
- `m<=zeta` lowers zeta.

A distinct exact class has m=1, so every q/tau-flat distinct-class move sends zeta exactly to zero. Therefore a genuinely `Phi_3`-flat distinct-support move lies in the neutral-free slice `zeta=0`.

If k repeated exact classes simultaneously admit `Phi_3`-flat exchanges, then

> **`(k+1)(zeta+1)<=r-1`.**

**Status:** exact involution `PROVED_SYMBOLIC`; clique-capacity product bound `PROVED_CONDITIONAL`.

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

Modulo neutral relabellings, the entire repeated correction orbit is exactly

> **`H <--> H'=(H\D) union S`.**

There is no longer correction cycle in this branch.

The d2 allowance is invariant. If `b=e_M(S)` and `mu=1-e_H(D)`, the chambers exchange `b <-> mu`, and

> `kappa_H(D)-kappa_(H')(S)=b-mu`.

Thus the repeated branch is one two-state symbolic terminal with

`m<=floor((r-1)/2)`.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem G — Distinct fully-decorated d2 reduction

Work in one fixed fully decorated shell class `S subset X` on the genuine `Phi_3`-flat distinct slice `zeta=0`. Let Q be the simple graph of distinct q-flat core 2-supports.

For every support `xy`,

> `w_x+w_y+mu(xy)=a`.

For two same-shell-class owners with supports `D_i,D_j`, after repivoting through `D_i` the other owner has new missing degree

> **`2-|D_i intersect D_j|`.**

Hence repeated / one-point-overlap / disjoint supports induce d0 / d1 / d2 correction transitions respectively.

The following are proved using only valid core row-closure / `alpha(H)<=3` arguments:

- `a=0`: `|E(Q)|<=3`;
- `a=1`: `|E(Q)|<=12`;
- for `a>=2`,
  > **`nu(Q)(a-1)<=W<=4r+9-a`;**
- at `a=2`, all zero-weight support vertices number at most three, and the `(1,1)` target-support subgraph has maximum degree at most three;
- the induced hereditary capacity inequality from `D2_DISTINCT_SUPPORT_REDUCTION.md` holds in its stated range.

**Status:** `PROVED_CONDITIONAL`.

The attempted stronger claim `nu(Q)<=3` independent of allowance is **retracted**: it incorrectly used `alpha(F)<=3`. The actual backend has `alpha(F)<=4`.

---

# Theorem H — d2 scalar/core-support barrier

For every d2 common-S system,

> `W=K+2r-2+a+b`.

A three-class exact-one-loss common-hub subsystem requires

> `K+a+b>=r`.

**Status:** identity `PROVED_SYMBOLIC`; barrier `PROVED_CONDITIONAL`.

---

# Theorem I — Plateau cycle rigidity

A closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. Repeated-class edges are controlled exactly by zeta. If zeta is also flat, Theorem F collapses the repeated part to a two-state involution.

Thus the unresolved correction complexity lies in distinct-support fully-decorated d2 moves, especially allowance `a>=2`.

**Status:** `PROVED_SYMBOLIC` / `PROVED_CONDITIONAL` as above.

---

# Explicit audit retractions

The earlier `Missing-Pair / Neutral-Population Bound` is **not a theorem** under the actual backend. In particular the statements

`kappa(D)>=zeta-1`, `a>=zeta`

must not be used; they relied on treating an independent 4-set in F as forbidden.

Likewise the allowance-independent distinct-support `nu(Q)<=3` / six-hub collapse is retracted for the same reason.

---

# Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

The first three coordinates are genuine bounded integer coordinates, with an exact class-exchange law for zeta.

The bounded candidate fourth coordinate remains

`Q2=sum_{v in H}kappa_v^2`.

Universal Q2 monotonicity is open.

A fourth coordinate is now needed primarily for the fully-decorated distinct-support d2 plateau with `a>=2`.

---

# Remaining route to Level 4 / Level 5

The principal scalable branch is:

> a fixed fully decorated d2 shell pair `S subset X`, `zeta=0`, with many distinct q-flat supports and allowance `a>=2`.

The repeated part has already collapsed to the Balanced Two-Chamber family. The distinct branch is absolutely bounded for `a=0,1` and partially structured at `a=2`.

The next target is:

> **Allowance-2 Distinct-Support Closure.** Eliminate or finitely classify the max-degree-three weighted support graph at `a=2`, preferably via d1 correction transitions, row closure, or a fourth bounded potential.

A successful `a=2` theorem should then indicate the scalable mechanism for general allowance.

---

# Certified success level

- Level 1: d3 closure obtained.
- Level 2: full low-endpoint elimination not yet; shell geometry is fixed-width and non-fully-decorated d2 plateaux are O(1)-bounded.
- **Level 3: achieved** — high endpoint is a finite three-owner bounded-complement skeleton.
- Level 4: not yet achieved, but `Phi_3=(q,tau,zeta)` is a genuine three-coordinate potential with exact class-exchange dynamics.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **Fully-decorated distinct-support d2 plateau at allowance `a>=2`, beginning with complete closure of `a=2`.**