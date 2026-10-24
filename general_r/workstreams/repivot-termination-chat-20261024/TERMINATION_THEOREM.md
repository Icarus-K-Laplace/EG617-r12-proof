# Termination Theorem

## Target

The intended final statement is:

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

This full theorem is **OPEN**.

What is now proved is a strong endpoint-compression package. All medium degrees disappear; d3 disappears; the high endpoint has at most three owners; and the low d1/d2 shell supports admit constant-size heavy transversals.

---

# Theorem A — Conditional Endpoint Compression

Assume A+B and `r>=12`. Choose a pivot maximal in `(q,tau)`.

Every regular shell vertex belongs to one of:

1. `d=0`: neutral pivot symmetry; quotient it.
2. `d=1`: one-vertex excess exchange; all shell missing partners lie in at most five heavy shell vertices.
3. `d=2`: the only scalable support-interaction endpoint; every shell missing pair meets a six-vertex heavy set and every unbounded family of distinct pairs is confined to at most four stars.
4. `d=3`: eliminated by the strengthened d3 charge/B-floor plus the existing low-charge Bridge-B absorption.
5. `d>=r-2`: at most three such vertices exist in the entire shell, and their interaction is encoded by an r-independent bounded-complement skeleton.

No degree `4<=d<=r-3` occurs.

Moreover:

- every closed `(q,tau)`-non-improving repivot cycle is entirely q-flat and tau-flat;
- K cannot serve as an additional potential coordinate because `Delta K=-2 Delta q`;
- every repeated support on such a plateau cycle has a fully decorated shell partner;
- every d2 common-S system has exact charge `W=K+2r-2+a+b`;
- a three-class d2 one-loss common-hub terminal must satisfy `K+a+b>=r`.

**Status:** `PROVED_CONDITIONAL`.

---

# Theorem B — High Endpoint Three-Owner / Bounded-Complement Reduction

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

This is the requested **Level 3** high-endpoint result.

---

# Theorem C — Plateau Cycle Rigidity

For a closed regular-repivot cycle in a fixed residual F:

`sum Delta q=0`, `sum Delta K=0`.

If every edge is non-improving in `(q,tau)`, then each edge has

`Delta q=Delta tau=Delta K=0`.

Every repeated support on the cycle is fully decorated on its shell partner.

Thus no-improvement cycles reduce to simultaneous equality classification.

**Status:** `PROVED_SYMBOLIC`.

---

# Theorem D — Low-Endpoint Shell Heavy-Cover Compression

Define

`t_s=d_M(s)+g_s=e_F(s,H)`

for shell vertices. Then

`sum_A t_s=2e(M)+G_A<=2q<=6r-2`.

For any regular owner y, using its singleton common-S representation with missing set S of size d, allowance a and `b=e_M(S)`, one has the exact identity

> **`sum_{s in S} t_s=d(r+1-d)+a+b`.**

Consequences:

### d1

The unique shell missing partner satisfies `t_s>=r`. Hence all d1 shell supports belong to a fixed set of at most five vertices. Thus there are at most five d1 common-S classes.

### d2

Every missing pair `{s,t}` satisfies

`t_s+t_t>=2(r-1)`.

Therefore every pair meets

`C_2={v:t_v>=r-1}`,

with

`|C_2|<=6`.

More sharply, let

`P={v:2t_v>=3(r-1)}` and `Q={v:2t_v>=r-1}`.

Then `|P|<=4`, `|Q|<=12`, and every d2 missing pair either

- is incident with P, hence belongs to one of at most four scalable star families; or
- lies entirely inside Q, an at-most-twelve-point bounded core.

Thus arbitrary r-growing d2 support graphs are impossible: all unbounded distinct-support diversity is star-shaped around at most four hubs.

**Status:** `PROVED_CONDITIONAL`.

This is the key new compression on the previously unique scalable endpoint.

---

# Candidate refinement

On a q-flat plateau define

`Q2=sum kappa_v^2`.

It is bounded by `K^2` and has an exact repivot update formula in `POTENTIAL.md`. Thus

`Phi_3=(q,tau,Q2)`

is a legitimate bounded lexicographic candidate.

What is not yet proved is universal Q2 improvement outside the rigid families. A signature/star multiplicity coordinate may be sharper for the remaining d2 star systems.

---

# Remaining route to a sufficiently-large-r contradiction

After Theorems A–D, a global terminal can only be assembled from:

- at most five d1 shell-support classes, each a one-vertex exchange system;
- d2 support systems consisting of an at-most-twelve-vertex bounded core plus at most four scalable stars;
- within d2, the linearly-high equality/positive-loss regime `K+a+b>=r` and isolated deep-loss blocks;
- at most three high-endpoint bounded-complement owners;
- simultaneous equality cycles among these pieces.

The remaining r-growth is therefore no longer an arbitrary support hypergraph. It is confined to **at most four weighted d2 stars** (plus owner multiplicities inside finitely many fixed support classes).

A Level-5 theorem should now target the following narrower statement:

> **D2 Star Termination Lemma.** In a `(q,tau)`-maximal state, no scalable d2 star centered at a heavy shell vertex can support the linearly-high equality/positive-loss budget `K+a+b>=r` without either (i) producing a strict plateau-coordinate improvement, (ii) collapsing to repeated fully-decorated support, or (iii) violating a multi-pivot transported-excess sum.

Proving this for one star and summing over the at most four hubs would leave only O(1)-sized endpoint kernels.

---

# Certified success level

- Level 1: d3 closure obtained (conditional on the declared upstream low-charge assets).
- Level 2: not yet; d1/d2 terminal elimination remains, although their shell-support geometry is now bounded/heavy-star compressed.
- **Level 3: achieved** — high endpoint reduced to a finite three-owner bounded-complement skeleton.
- Level 4: open — no globally strict refined potential yet.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **D2 heavy-star plateau stability:** eliminate or rigidify the at most four scalable d2 star systems in the linearly-high regime `K+a+b>=r`.