# Termination Theorem

## Target

The intended final statement is:

> **Endpoint Repivot Stability Theorem.** For every sufficiently large r, under hypotheses A+B, every admissible local pivot view either admits a strict increase of a bounded lexicographic repivot potential or belongs to a finite r-independent family of rigid endpoint configurations, all of which are impossible.

This full theorem is **OPEN**.

What is now proved is the following endpoint-compression theorem, which removes every r-growing family except d2.

---

# Theorem A — Conditional Endpoint Compression

Assume A+B and `r>=12`. Choose a pivot maximal in

`(q,tau)`.

Then every regular shell vertex belongs to one of the following classes:

1. `d=0`: neutral pivot symmetry; quotient it.
2. `d=1`: one-vertex excess exchange.
3. `d=2`: the only scalable support-interaction endpoint.
4. `d=3`: eliminated by the strengthened d3 charge/B-floor plus the existing low-charge Bridge-B absorption.
5. `d>=r-2`: at most three such vertices exist in the entire shell, and their interaction is encoded by an r-independent bounded-complement skeleton.

No degree `4<=d<=r-3` occurs.

Moreover:

- every closed `(q,tau)`-non-improving repivot cycle is entirely q-flat and tau-flat;
- K cannot serve as an additional potential coordinate because `Delta K=-2 Delta q`;
- every repeated support on such a plateau cycle has a fully decorated shell partner;
- every d2 common-S system has exact charge
  `W=K+2r-2+a+b`;
- a three-class d2 one-loss common-hub terminal must satisfy
  `K+a+b>=r`.

**Status:** `PROVED_CONDITIONAL`.

## Proof map

- medium-degree elimination: quadratic base + `q<=3r-1`;
- d0: direct repivot identity;
- d3: equality B-floor + low-charge absorption;
- high endpoint: Four-Owner Missing-Edge Count + r=12 equality regular-clique obstruction;
- cycle statement: telescoping q/K and tau;
- d2 scalar reduction: exact common-S ledger + pattern charge barrier.

---

# Theorem B — High Endpoint Reduction

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

# Candidate refinement

On a q-flat plateau define

`Q2=sum kappa_v^2`.

It is bounded by `K^2` and has an exact repivot update formula recorded in `POTENTIAL.md`.

Therefore

`Phi_3=(q,tau,Q2)`

is a legitimate bounded lexicographic potential candidate.

What is not yet proved is that every non-rigid equal-(q,tau) view admits a repivot increasing Q2. A different signature/overlap coordinate may be needed.

---

# Remaining route to a sufficiently-large-r contradiction

After Theorem A, a global terminal can only be assembled from:

- d1 one-vertex exchanges;
- d2 linearly-high equality/positive-loss systems (`K+a+b>=r` in the three-class branch) and isolated deep-loss blocks;
- at most three high-endpoint bounded-complement owners;
- simultaneous equality cycles among these pieces.

The high endpoint no longer scales with r. The d3 endpoint is gone. Hence any sufficiently-large-r obstruction must now be carried by d2 (with d1 acting only as a one-point transport interface).

A Level-5 theorem will follow from either of the following two statements:

### Route I — d2 plateau instability

Prove that every d2 state satisfying `K+a+b>=r` has a strict repivot improvement in a bounded refinement of `(q,tau)` unless it is a finite rigid design; then kill that design by hereditary/support compatibility.

### Route II — multi-pivot d2 defect sum

Prove a cycle/sum inequality showing that a family of non-improving d2 repivots cannot simultaneously carry the linearly high scalar charge required by `K+a+b>=r`.

Either route would leave only O(1) high owners plus d1 exchanges and should yield a genuine all-large-r terminal theorem.

---

# Certified success level

- Level 1: d3 closure obtained (conditional on the declared upstream low-charge assets).
- Level 2: not yet; d1/d2 remain.
- **Level 3: achieved** — high endpoint reduced to a finite three-owner bounded-complement skeleton.
- Level 4: open — no globally strict refined potential yet.
- Level 5: open — no certified absolute r0 yet.
- Level 6: open.

# Single blocker

> **D2 linearly-high plateau stability:** eliminate/rigidify all non-improving d2 systems whose scalar budget reaches the necessary range `K+a+b>=r`.