# Termination Theorem

## Target

The intended final statement is:

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

The final contradiction theorem is **OPEN**. The endpoint classification is fixed-width and a genuine third potential coordinate is now proved on the repeated-support plateau.

---

# Theorem A — Conditional Fixed-Width Endpoint Compression

Assume A+B and `r>=12`.

Every regular shell owner has

`d in {0,1,2,3,r-2,r-1,r}`.

Moreover:

1. d0 is neutral and quotientable;
2. d1 missing partners lie in at most five shell vertices/classes;
3. all d2 shell missing-set endpoints lie in at most six vertices, hence at most fifteen shell classes;
4. d3 is eliminated by the equality B-floor plus the declared low-charge Bridge-B absorption;
5. all high owners `d>=r-2` number at most three and form a bounded-complement kernel.

Thus

> **the number of shell-side endpoint support types is bounded by an absolute constant independent of r.**

There is no r-growing shell-support case tree.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem B — Shell-Incidence Kernel

For shell vertices

`t_s=d_M(s)+g_s=e_F(s,H)`

one has

`sum_A t_s=2e(M)+G_A<=2q<=6r-2`.

For every regular owner with shell missing set S of size d,

` sigma_s=t_s-(r+1-d)-m_S(s)>=0 `

for each `s in S`, and

` sum_{s in S}t_s=d(r+1-d)+a+b `.

Consequences:

- d1 support universe size <=5;
- d2 support universe size <=6, hence <=15 pair classes;
- for a d2 class `S={u,v}`, with `h_u=t_u-(r-1)`, allowance is
  `a=h_u+h_v-b`;
- if the d2 support universe has all six vertices active, then `sum h<=4` and there are at most two d2 owners total.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem C — Fixed-Class d2 Plateau Reduction

Fix one d2 shell class `S={u,v}` and all owners Y in that class. Put

`w_x=kappa_x+e_F(x,S)`, `mu(D)=1-e_H(D)`,

and let a be the class allowance.

Every owner has exact loss

> `ell_y=q-q_y=a-[w(D_y)+mu(D_y)]>=0`.                       (C1)

Let `lambda_x=#{y:x in D_y}`. Support incidence gives

> `lambda_x>=2 or w_x>=1 => x in X`.                         (C2)

Write `s=|S intersect X|`.

### s=0

Common-S transport gives `a=b`.

- b=0: every owner is q-flat and the entire class has at most three owners;
- b=1: at most one q-flat owner and at most three distinct strict support classes.

### s=1

Q-flat supports cannot repeat. Their support graph has at most three components, each an isolated edge or a star with at most two edges. Hence

> `# q-flat owners<=6`.

### s=2

This is the only regime in which q-flat owner multiplicity can scale with r.

Therefore

> **the unique scalable equal-q d2 mechanism is a fixed fully-decorated shell pair `S subset X`.**

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem D — High Endpoint Three-Owner Reduction

All regular owners with `d>=r-2` number at most three.

With `s_y=r-d_y in {0,1,2}`, their shell interaction lies in an at-most-nine-point kernel and core owner-incidence uses at most eight signatures.

**Status:** `PROVED_CONDITIONAL`.

This achieves Level 3 high-endpoint reduction.

---

# Theorem E — Genuine third potential coordinate

Define

`zeta(p)=#{regular shell owners with d=0}`

and

> **`Phi_3=(q,tau,zeta)`.**

Zeta is bounded, integer-valued, and invariant under neutral d0 pivot relabellings.

Let y belong to an exact repeated `(S,D)` owner class of multiplicity m. Repivoting through y makes the other `m-1` class owners d0, while every old d0 owner together with the old pivot becomes a reverse `(D,S)` owner. Hence

`zeta(y)>=m-1`.

Therefore, on a q/tau-flat move,

> **if `m>=zeta(p)+2`, then `Phi_3(y)>Phi_3(p)`.**            (E1)

At a `Phi_3`-maximal pivot,

> **every q/tau-flat exact repeated class has `m<=zeta+1`.** (E2)

If equality is zeta-flat, then the exchange is multiplicity-balanced: the other `m-1` old class owners become exactly the full new d0 population and the reverse `(D,S)` class has multiplicity at least m.

For d2, such a repeated q/tau-flat exchange necessarily lies in the fully-decorated shell-pair regime.

Using the low-owner clique cap, if k exact repeated classes simultaneously admit `Phi_3`-flat exchanges, then every one has multiplicity `zeta+1` and

> **`(k+1)(zeta+1)<=r-1`.**                                  (E3)

In particular a balanced repeated class has

`m<=floor((r-1)/2)`.

**Status:** zeta coordinate and repeated-class improvement `PROVED_SYMBOLIC`; clique-capacity bound `PROVED_CONDITIONAL` on the standard backend clique cap.

This is the first proved refinement beyond `(q,tau)` in this workstream. It does not yet establish a globally strict potential on every plateau move, so full Level 4 remains open.

---

# Theorem F — Missing-Pair / Neutral-Population Bound

Let D be a target-nonedge core pair. Its common target-nonneighbours in H number at least

`r-3-kappa(D)`

and form a target clique. The pivot p and all zeta d0 owners are also common nonneighbours of D. The global clique cap therefore yields

> **`kappa(D)>=zeta-1`.**                                    (F1)

If D is the support of a q-flat d2 owner in a fixed class of allowance a, then

`a=w(D)+1>=kappa(D)+1`,

so

> **`a>=zeta`.**                                             (F2)

Thus:

> **if `a<zeta`, every q-flat d2 support must be a target edge.**

At the sharp boundary `a=zeta`, a nonedge support has a rigid saturated common-nonneighbour template: `kappa(D)=zeta-1`, no common H target-neighbour, and no target edge from S to D.

**Status:** `PROVED_SYMBOLIC` under the standard global alpha/omega backend caps.

---

# Theorem G — d2 scalar/core-support barrier

For every d2 common-S system,

> `W=K+2r-2+a+b`.

A three-class exact-one-loss common-hub subsystem requires

> `K+a+b>=r`.

Thus the historical difficult d2 branch is forced into a linearly-high scalar regime, but its shell class is now one of at most fifteen fixed classes.

**Status:** identity `PROVED_SYMBOLIC`; barrier consequence `PROVED_CONDITIONAL`.

---

# Theorem H — Plateau Cycle Rigidity

For a closed legal repivot cycle,

`sum Delta q=0` and `sum Delta K=0`.

A closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. Appending zeta, every repeated-class edge of a closed `Phi_3`-non-improving cycle must also be zeta-flat, hence multiplicity-balanced and subject to (E3).

Thus repeated-support correction cycles have become rigid balanced exchange systems rather than arbitrary support repetitions.

**Status:** `PROVED_SYMBOLIC`; complete balanced-cycle elimination `OPEN`.

---

# Potential status

Current preferred potential:

> **`Phi=(q,tau,zeta,...)`.**

The first three coordinates are genuine bounded integer coordinates. Zeta has a proved strict-improvement theorem on repeated q/tau plateaux.

A candidate fourth coordinate is

`Q2=sum_{v in H}kappa_v^2`,

whose exact update is recorded in `POTENTIAL.md`. Universal Q2 monotonicity is not proved.

A fourth coordinate is needed only after the reductions above, specifically for:

1. distinct-support fully-decorated d2 plateau systems;
2. zeta-balanced repeated d2 correction cycles.

---

# What remains for Level 4 / Level 5

After Theorems A-H, the only scalable equal-q endpoint mechanism is:

> a fixed d2 shell pair `S subset X`, carrying either
> - a distinct-support q-flat system, or
> - zeta-balanced repeated support classes satisfying `(k+1)(zeta+1)<=r-1`.

Nonedge q-flat supports additionally require `a>=zeta`; below that threshold only target-edge supports survive.

Everything else is either quotient-neutral, O(1)-bounded, eliminated, or part of the at-most-three-owner high kernel.

The next theorem should therefore be narrower than the previous finite-class statement:

> **Fully-Decorated d2 Plateau Theorem.** For a fixed decorated shell pair `S subset X`, every `Phi_3`-maximal q-flat support system either admits a strict fourth-coordinate improvement or belongs to a finite rigid family of target-edge / saturated-nonedge correction skeletons.

A proof of this theorem, followed by elimination of the resulting rigid skeletons, is the direct path to Level 4 and then an all-large-r contradiction.

---

# Certified success level

- Level 1: d3 closure obtained.
- Level 2: full low-endpoint elimination not yet; d1/d2 shell geometry is fixed-width and all non-fully-decorated d2 plateau classes are O(1)-bounded.
- **Level 3: achieved** — high endpoint is a finite three-owner bounded-complement skeleton.
- Level 4: **not yet achieved**, but a genuine third coordinate `zeta` with strict repeated-class monotonicity is proved.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **Fully-decorated fixed-class d2 plateau compatibility:** eliminate or rigidify distinct-support systems and zeta-balanced repeated correction cycles for one shell pair `S subset X`.