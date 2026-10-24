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

The valid low-allowance and matching reductions are:

- `a=0`: `|E(Q)|<=3`;
- `a=1`: `|E(Q)|<=9`;
- for `a>=2`,
  > **`nu(Q)(a-1)<=W<=4r+9-a`;**
- at `a=2`, all zero-weight support vertices number at most three, and the zero-free `(1,1)` target-support subgraph has maximum degree at most three;
- the induced hereditary capacity inequality from `D2_DISTINCT_SUPPORT_REDUCTION.md` holds in its stated range.

**Status:** `PROVED_CONDITIONAL`.

The attempted stronger claim `nu(Q)<=3` independent of allowance is **retracted**: it incorrectly used `alpha(F)<=3`. The actual backend has `alpha(F)<=4`.

---

# Theorem H — Exact fourth potential coordinate and plateau-distance compression

Define

`eta(p)`
` = #{ regular shell owners x with d_p(x)=1 and`
`       (q_x,tau_x,zeta(x))=(q_p,tau_p,zeta(p)) }`.

Then

> **`Phi_4=(q,tau,zeta,eta)`**

is a genuine bounded lexicographic potential.

For a neutral-free distinct d2 common-S plateau let `G_S` be the support-intersection graph. The exact transition identity gives

`eta(p_D)>=deg_(G_S)(D)`.

Hence at a `Phi_4`-maximal pivot

> **`Delta(G_S)<=eta`.**

A greedy independent set in `G_S` yields a pairwise-disjoint q-flat subfamily of size at least

> **`ceil(N/(eta+1))`.**

So support overlap is not a free scalable parameter: it is charged to the d1 plateau population.

The eta population lies in at most five d1 shell classes. In the neutral-free slice one such class has `N_1>=ceil(eta/5)` distinct singleton supports. If c is its allowance, then under the inherited core cap `K<=2r-2`,

> **`(N_1-1)c<=3r-2`.**

Thus linear eta forces a linear d1 class with O(1) allowance.

**Status:** eta/transition theorem `PROVED_SYMBOLIC`; d1 scale-transfer bound `PROVED_CONDITIONAL`.

This is the first certified fourth potential coordinate.

---

# Theorem I — Allowance-2 Clean Pair-Exchange Orbit

In any pairwise-disjoint q-flat `a=2` d2 subfamily, at most three supports contain a zero-weight endpoint. Every other support is a clean target K2 with endpoint weights `(1,1)`.

Let `D_i,D_j` be two disjoint clean supports. Repivot through the owner of `D_i`. Then `D_j` remains

- a d2 support;
- q/tau/zeta-flat;
- a target K2;
- endpoint weights exactly `(1,1)` relative to the new shell pair `D_i`.

Therefore a disjoint clean subsystem is closed under exchanging the distinguished shell pair with any clean core pair.

The old shell pair becomes one reverse support of exactly one of three symbolic types:

1. clean target K2 `(1,1)`;
2. target K2 `(0,2)`;
3. target nonedge `(0,1)`.

Between two clean blocks the target cross graph is a matching of size0,1,or2 by row closure.

Since the `(1,1)` support graph has maximum degree3, every unbounded `a=2` branch contains an unbounded clean matching subsystem, and every linear-size branch contains a linear-size one.

Hence the scalable `a=2` terminal is no longer an arbitrary bounded-degree graph. It contains the rigid design object

> **clean pair-exchange design + O(1) zero-containing special blocks.**

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem J — d2 scalar/core-support barrier

For every d2 common-S system,

> `W=K+2r-2+a+b`.

A three-class exact-one-loss common-hub subsystem requires

> `K+a+b>=r`.

**Status:** identity `PROVED_SYMBOLIC`; barrier `PROVED_CONDITIONAL`.

---

# Theorem K — Plateau cycle rigidity

A closed `(q,tau)`-non-improving cycle is q/tau-flat edgewise. Repeated-class edges are controlled exactly by zeta. If zeta is also flat, Theorem F collapses the repeated part to a two-state involution.

Distinct d2 overlap is controlled by eta. The first genuinely scalable distinct branch `a=2` contains a repivot-closed clean pair-exchange design by Theorem I.

Thus every surviving long correction cycle must be assembled from

- the balanced repeated two-chamber block;
- bounded-allowance d1 plateau states;
- the clean pair-exchange design;
- at most three high-endpoint owners.

**Status:** `PROVED_SYMBOLIC` / `PROVED_CONDITIONAL` as above.

---

# Theorem L — Exact Clean-Pair Block Model and High-Density Reduction

For the allowance-2 clean terminal, every block pair is one of the seven partial matchings of K_2,2. Independent transversals are encoded by a 2-CNF formula. Exhaustive enumeration of all 7^6 labelled four-block patterns gives a minimum of six target cross edges for an unsatisfiable four-block restriction.

Let U be the union of m clean blocks and G=overline(H[U]). Then G is K4-free, every block is an independent pair in G, and every pair of blocks has at least two cross edges in G. For each x in U,

delta(G)>=max(m-1,2m-r-2).

If m>=ceil(4r/3+3), then delta(G)>5|U|/8. The Andrasfai-Erdos-Sos theorem makes G 3-partite, so U is covered by three target cliques and m<=floor(3(r-1)/2).

**Status:** block encoding and local enumeration PROVED_SYMBOLIC / finite-exhaustive; high-density reduction PROVED_CONDITIONAL; Clean Pair Nonextension remains OPEN. The high-density interval is still linear and nonempty.

# Theorem M — Reversible Fifth-Coordinate Obstruction

For Q2=sum kappa_v^2, the exact increment is

Delta Q2 =
sum_{z in H\D_y}[2 kappa_z delta_z+delta_z^2]
+sum_{s in S_y}[sigma_s-e_F(s,D_y)]^2
-sum_{u in D_y}kappa_u^2,

where delta_z=e_F(z,S_y)-e_H(z,D_y).

For a clean endpoint z in another block, its contribution simplifies to a_z-b_zi, where a_z=e_F(z,S) and b_zi=e_H(z,D_i); no sign follows from the clean weight equation alone.

More fundamentally, every legal repivot is reversible. If a move is Phi4-flat, its reverse is Phi4-flat and has the opposite Q2 increment. Therefore the proposed universal condition “every nontrivial Phi4-flat move strictly increases Q2” is DISPROVED AS STATED. Q2 may select a maximal representative but cannot alone eliminate a reversible terminal.

# Theorem N — Bounded-Allowance d1 Terminal Ledger

For a fixed d1 singleton class of allowance c and multiplicity N, distinct q-flat supports remain a d1 class under one-point exchange, with transported excess

kappa'_u_j=c-e_H(u_i,u_j),  w'_u_j=c.

The known bounds are:

- c=0 implies N<=3;
- c>=1 implies N<=r-2 by the low-owner clique cap;
- (N-1)c<=3r-2 under K<=2r-2;
- eta=Omega(r) forces c=O(1).

These bounds do not imply an absolute N bound for c>=1.

**Status:** exact transition and scale transfer PROVED_CONDITIONAL; final d1 absorption OPEN.

# Theorem O — Six-Type Optional-Degree Bound in the AES Branch

Assume A+B and m>=ceil(4r/3+3). In the AES 3-partition, the clean block counts x,y,z all satisfy x,y,z>=a=m-r+1>=ceil(r/3)+4. The two type triples T0=(A0,B1,C0) and T1=(A1,B0,C1) each have no H edges between their classes.

Assign every outside vertex one fully-seen witness class in each triple. For each type class T in part i, the assigned count N_T is at most s_i+2, where n_i=r-1-s_i. The three assignment slacks in either triple sum to exactly four. The transported endpoint identity yields

t_x<=kappa_x+u_T-1<=4,

where t_x is the optional cross-block H-degree. Thus the optional cross-block graph has maximum degree at most four.

**Status:** PROVED_CONDITIONAL. This is a structural theorem, not nonextension.

# Theorem P — Off-Part Witness Excess Dichotomy

If an outside vertex o has no pair of fully-seen witness classes from the same AES part, then any witness pair from T0,T1 is off-part. One residual class triple has one optional relation of maximum degree four, one block matching, and one empty relation. Since every class has size at least a>4, fewer than a-4 neighbours of o in that residual triple would leave an independent transversal of size three. Therefore

d_H(o,U)>=3a-4,  kappa_o>=3a-4-r>=8.

For X such exceptional outside vertices,

X(3a-4-r)<=K_O<=2r-2-K_U.

The claim that every outside vertex sees an entire part is NOT established; the exceptional set may still be linear near the lower AES threshold.

**Status:** PROVED_CONDITIONAL.

# Theorem Q — Exact Three-Part Assignment Budget

Assign each nonexceptional outside vertex to a part it sees completely. Let g_i be the group sizes, u_i=s_i+2-g_i, and rho_x count outside neighbours of x in U_i that are not in the assigned group O_i. Then

sum_i u_i=4+X,

t_x+rho_x=kappa_x+u_i-1,

and

2 e_opt + E_foreign = K_U + sum_i n_i(u_i-1).

This is an exact no-double-counting identity. It does not by itself contradict K<=2r-2.

**Status:** PROVED_CONDITIONAL; full Clean Pair Nonextension OPEN.

# Theorem R — Independent d1 Excess Budget

For a d1 singleton class of allowance c and multiplicity N, every support has kappa in {c-1,c}. Therefore

N(c-1)<=K_U<=2r-2,

alongside (N-1)c<=3r-2 and N<=r-2. For fixed c>=2 this remains a linear bound, and c=1 remains open.

**Status:** PROVED_CONDITIONAL; bounded-allowance d1 absorption OPEN.

# Explicit audit retractions

The earlier `Missing-Pair / Neutral-Population Bound` is **not a theorem** under the actual backend. In particular the statements

`kappa(D)>=zeta-1`, `a>=zeta`

must not be used; they relied on treating an independent 4-set in F as forbidden.

Likewise the allowance-independent distinct-support `nu(Q)<=3` / six-hub collapse is retracted for the same reason.

---

# Potential status

Current preferred potential:

> **`Phi_4=(q,tau,zeta,eta)`.**

All four coordinates are genuine bounded integers. Zeta has an exact class-exchange law and eta has an exact intersection-to-d1 transport law.

A bounded fifth-coordinate candidate remains

`Q2=sum_{v in H}kappa_v^2`.

Universal strict increase on every reversible Phi4-flat move is DISPROVED_AS_STATED; Q2 may still select a representative but cannot alone eliminate the terminal.

---

# Remaining route to Level 4 / Level 5

The principal scalable terminal has now changed form.

The old blocker

> arbitrary fully-decorated distinct-support d2 plateau at `a>=2`

has been reduced to:

1. bounded-allowance d1 concentration, when eta is large;
2. weighted d2 matching compression, when eta is small;
3. at the first scalable level `a=2`, a large repivot-closed clean pair-exchange design plus O(1) special blocks.

The next target is therefore:

> **Clean Pair Nonextension Theorem.** Eliminate a sufficiently large clean K2 block system in which every inter-block target graph is a matching, no four blocks admit an independent transversal, and repivot may exchange the distinguished block without leaving the clean family.

The preferred routes are:

- hereditary-cap/stability contradiction;
- clique-cap contradiction;
- multicolor nonextension;
- or a different structural terminal elimination; universal strict Q2 increase is impossible by reversibility.

A successful theorem here would close the first genuinely scalable allowance layer and push the backend materially toward Level 5.

---

# Certified success level

- Level 1: d3 closure obtained.
- Level 2: full low-endpoint elimination not yet; shell geometry is fixed-width and the first two distinct d2 allowance layers are absolutely bounded.
- **Level 3: achieved** — high endpoint is a finite three-owner bounded-complement skeleton.
- **Level 4: partially achieved** — `Phi_4=(q,tau,zeta,eta)` is a genuine four-coordinate potential; the only scalable flat terminal currently visible is the clean pair design / bounded-allowance d1 package.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **Clean Pair Nonextension + bounded-allowance d1 absorption.** In the AES high-density branch, control the exceptional set X and close the exact budget 2 e_opt + E_foreign = K_U + sum_i n_i(u_i-1); in parallel, turn N(c-1)<=K_U into an absolute d1 multiplicity bound. The lower-density branch m<ceil(4r/3+3) remains open.