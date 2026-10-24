# Termination Theorem

## Target

The intended final statement is:

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

The final contradiction theorem is **OPEN**. The shell-side endpoint classification is now fixed-width.

---

# Theorem A — Conditional Fixed-Width Endpoint Compression

Assume A+B and `r>=12`, and choose a pivot maximal in `(q,tau)`.

Then every regular shell vertex lies in one of the following endpoint classes:

1. `d=0`: neutral pivot symmetry; quotient it.
2. `d=1`: one-vertex excess exchange; all shell missing partners lie in a set of at most five vertices, hence at most five shell common-S classes.
3. `d=2`: all shell missing-set endpoints lie in a set of at most six vertices, hence at most fifteen shell common-S classes.
4. `d=3`: eliminated by the d3 equality B-floor plus the declared low-charge Bridge-B absorption.
5. `d>=r-2`: at most three such owners exist in the whole shell; their interaction is an r-independent bounded-complement kernel.

No degree `4<=d<=r-3` occurs.

Consequently:

> **The number of shell-side endpoint support types is bounded by an absolute constant independent of r.**

There is no surviving r-growing shell-support case tree.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem B — Shell-Incidence Endpoint Kernel

For shell vertices define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Then

`sum_A t_s=2e(M)+G_A=2q-G_A<=6r-2`.

For any regular owner y with shell missing set S of size d and `b=e_M(S)`, singleton transport gives pointwise

> `sigma_s=t_s-(r+1-d)-m_S(s)>=0` for every `s in S`,

and, after summing,

> `sum_{s in S} t_s=d(r+1-d)+a_y+b_y`.

### d1 consequence

For `S={s}`,

`t_s>=r`.

Thus all d1 shell support points lie in

`C_1={s:t_s>=r}`

with

> `|C_1|<=5`.

### d2 consequence

For `S={u,v}` and `b=e_M(S)`,

`t_u,t_v>=r-1+b`.

Let `U_2` be the union of all d2 shell support pairs. Then

> `|U_2|<=6`,

so there are at most

> `C(6,2)=15`

d2 shell classes.

Writing

`h_u=t_u-(r-1)`,

each d2 class satisfies

> `a_{uv}=h_u+h_v-b_{uv}`.

If `m=|U_2|`,

`sum_{u in U_2} h_u <= (6-m)r+m-2`.

At the maximal support-universe boundary `m=6`,

`sum h_u<=4`

and the total number of d2 owners is at most two. Thus even the maximal six-point shell kernel has bounded multiplicity/allowance.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem C — High Endpoint Three-Owner / Bounded-Complement Reduction

Under A+B, `r>=12`, all regular owners with `d>=r-2` form a set of size at most three.

Writing

`s=r-d in {0,1,2}`,

every high-endpoint state is represented by a finite skeleton with

- at most three owners;
- shell target-neighbour complements of size at most two;
- a shell interaction kernel of size at most nine;
- at most eight core owner-incidence signature classes.

The combinatorial skeleton family is independent of r.

**Status:** `PROVED_CONDITIONAL`.

This achieves the requested **Level 3** high-endpoint reduction.

---

# Theorem D — Low-Endpoint Owner Clique Lemma

For `r>=12`, any two regular owners x,y with `d_x,d_y<=3` are target-adjacent.

Indeed, if they were target-nonadjacent, zero-gap would require

`S_x union S_y=A`,

whereas

`|S_x union S_y|<=6<r+1=|A|`.

Therefore all regular low-endpoint owners, together with the pivot p, form a target clique. Since `omega(F)<=r-1`, the total number of regular low-endpoint owners is at most

> `r-2`.

At hereditary equality, the multicolor equality regular-clique obstruction can sharpen this linear owner count further, but the fixed-width shell classification above does not need that refinement.

**Status:** `PROVED_SYMBOLIC`.

---

# Theorem E — d2 scalar/core-support barrier

For every d2 common-S system,

> `W=K+2r-2+a+b`.

For an exact-one-loss common-hub subsystem with three distinct core support classes, the existing charge barrier gives

`W>=3r-2`,

hence

> `K+a+b>=r`.

Thus any difficult three-class d2 terminal must carry a linearly high excess/allowance budget. The shell pair S itself, however, now belongs to one of at most fifteen fixed classes.

**Status:** exact identity `PROVED_SYMBOLIC`; three-class consequence `PROVED_CONDITIONAL`.

---

# Theorem F — Plateau Cycle Rigidity

For a closed legal repivot cycle in a fixed residual graph,

`sum Delta q=0`, `sum Delta K=0`.

If every edge is non-improving in `(q,tau)`, then every edge is simultaneously q-flat and tau-flat. Every repeated support on such a cycle has a fully decorated shell partner.

Thus any no-improvement cycle reduces to simultaneous equality classification inside the finite endpoint classes above.

**Status:** `PROVED_SYMBOLIC`.

---

# Potential status

`(q,tau)` is a genuine bounded lexicographic potential.

K is not a new coordinate because

`Delta K=-2 Delta q`.

On a q-flat plateau,

`Q2=sum_{v in H} kappa_v^2`

is a bounded integer and has an exact repivot update formula in `POTENTIAL.md`. Hence

`Phi_3=(q,tau,Q2)`

is a legitimate candidate refinement, but universal Q2 monotonicity is not proved.

The finite d2 shell kernel suggests a potentially sharper refinement by the ordered multiplicity/defect profile of the at-most-fifteen fixed d2 classes.

---

# What remains for Level 4 / Level 5

After Theorems A–F, a global terminal can only be assembled from:

- at most five d1 shell classes, with q/tau-flat one-point core exchanges;
- at most fifteen d2 shell classes, each carrying owner multiplicity, core support sets, and transported loss/excess;
- within a d2 class, the known one-loss common-hub / at-most-three-core-support-class structure and isolated deep-loss blocks;
- at most three high-endpoint owners;
- simultaneous equality cycles among these finitely many classes.

Thus **all r-growing combinatorial complexity has moved off the shell support hypergraph and into multiplicity/core-support data inside a constant number of classes.**

The correct next theorem is now:

> **Finite-Class d2 Core Multi-Pivot Theorem.** Fix a d2 shell class `S={u,v}`. With shell parameters `b`, `h_u`, `h_v`, `sigma_u`, `sigma_v`, and `a=h_u+h_v-b` fixed, any family of legal owners that is simultaneously non-improving in `(q,tau)` either admits a strict increase in a bounded refinement of the potential or collapses to a finite impossible core-support skeleton.

Proving this uniformly, then summing over at most fifteen shell classes, would remove the last scalable endpoint mechanism and is the most direct route to a sufficiently-large-r contradiction.

---

# Certified success level

- Level 1: d3 closure obtained.
- Level 2: full low endpoint elimination not yet; however d1/d2 **shell geometry is completely fixed-width**.
- **Level 3: achieved** — high endpoint reduced to a finite three-owner bounded-complement skeleton.
- Level 4: open — no globally strict third potential coordinate yet.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **Finite-class d2 core-support multi-pivot compatibility:** eliminate or rigidify simultaneous non-improving owner families inside one fixed d2 shell class, then combine across the at-most-fifteen classes.