# Global Forcing-to-Master Allowance/Loss Coverage Theorem

Status: **PROVED_ANALYTIC** under the explicit common-S hypotheses stated below.

Purpose: identify exactly which support/allowance regimes are already forced into the global support-compatibility machinery, and isolate the genuinely open structural bridge.  This theorem is a synthesis theorem; it does not assert that every historical shell survivor has already been extracted into a common-S owner family.

Dependencies:

- `GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md`;
- `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md`;
- `GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md`;
- `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`;
- `GLOBAL_LARGE_SUPPORT_DECORATED_ESCAPE_THEOREM.md`;
- `GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md`;
- exact common-S exchange identity;
- lexicographic tau-maximality for repeated supports when `s=|S intersect X|<d`.

No solver and no E-layer label are used.

---

# 1. General common-S loss coordinates

Let `Y` be a common-S regular owner family in the r=12 shell, with

- support/missing-set size `d`;
- common ambient allowance `a`;
- row support defect

  `Delta_y=w(D_y)+mu(D_y)`;

- q-loss

  `ell_y=q-q_y>=0`.

The exact exchange identity gives

> `Delta_y=a-ell_y`.                                      (1)

For a proper overlap of `D_y` with a distinct d-support E, with overlap size h,

`h(d-h)<=Delta_y`.

Every proper overlap has `h(d-h)>=d-1`.  Therefore define the overlap-loss threshold

> `ell_* = a-(d-1)`.                                     (2)

Then `GLOBAL_LOSS_LAYER_DESCENT_THEOREM.md` gives:

- if `ell_y>ell_*`, `D_y` is disjoint from every distinct support class;
- if `ell_y=ell_*`, every proper overlap is saturated: `h in {1,d-1}` and all shared common-S charge is zero;
- only rows with `ell_y<ell_*` retain genuine higher-slack overlap freedom.

Thus the phrase **genuine higher-slack row** has an exact meaning:

> `ell_y < a-(d-1)`.                                      (3)

---

# 2. Non-fully-decorated repeated supports gain one unit of loss automatically

Assume

` s:=|S intersect X| < d `.

If a support class D is repeated by at least two owners, every vertex of D is globally decorated by the repeated owner incidences.  Repivoting D at the same q-level would change the lexicographic decoration statistic by

`tau_D-tau_p = d-s >0`.

Hence tau-maximality forbids a repeated plateau support.  Therefore every repeated support satisfies

> `ell>=1`.                                                (4)

This is the repeated-support strict-loss bridge.

Combining (2)--(4) immediately yields the key coverage fact:

> if `a<=d`, every non-fully-decorated repeated support is already either
> - boundary one-loss / overlap-saturated, or
> - support-isolated.

There is no uncontrolled repeated-support overlap geometry below or at first high slack.

---

# 3. d=2 coverage

Take `d=2`.

The overlap threshold is `d-1=1`.

## 3.1 Subcritical allowance

If

`a<=1`,

`GLOBAL_SUBCRITICAL_ALLOWANCE_DECOMPOSITION.md` applies whenever `s<2`.

The support system is a bounded plateau part plus pairwise-disjoint strict target-K2 blocks, and the strict cross allowance is at most `a-1<=0`.

Thus the d2 system is already in the global block/transversal architecture.

## 3.2 First high slack

If

`a=2`,

`GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md` is exhaustive for `s<2`:

- plateau: at most3 singleton rows;
- one-loss: boundary one-loss and hence governed by `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`;
- loss>=2: isolated zero-defect K2 support classes, at most3 classes, multiplicity at most9 per class.

Therefore d2/A2 contains no arbitrary overlap geometry.

## 3.3 Genuine higher slack

If `a>=3`, formula (3) says genuine overlap slack occurs only when

> `ell <= a-2`.                                           (5)

For a repeated support, (4) also gives `ell>=1`.
Hence the only repeated-support rows not already descended to boundary/isolated geometry lie in the explicit shallow-loss window

> **`1 <= ell <= a-2`.**                                  (6)

For example:

- a=3: only `ell=1` is genuinely new;
- a=4: only `ell=1,2` are genuinely new;
- all larger-loss rows are already boundary-saturated or isolated.

Thus every unresolved high-slack d2 problem is a finite shallow-loss problem, not a new global support geometry.

---

# 4. d=3 coverage

Take `d=3`, so the proper-overlap threshold is two.

## 4.1 Subcritical allowance

If

`a<=2`,

then for `s<3` the subcritical theorem applies:

- plateau rows form at most3 singleton classes;
- strict supports are disjoint from every distinct support class;
- distinct strict blocks have low cross density.

This is already inside the matching/transversal architecture.

## 4.2 First high slack

If

`a=3`,

`GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md` is exhaustive for `s<3`:

- plateau <=3 singleton rows;
- exact one-loss rows enter the zero-signature / sunflower master theorem;
- loss>=2 rows are isolated low-cross 3-blocks, at most3 distinct classes, multiplicity at most8 per class.

Thus d3/A3 also contains no uncontrolled overlap geometry.

## 4.3 Genuine higher slack

If `a>=4`, equation (3) gives genuine overlap freedom only for

> `ell <= a-3`.                                           (7)

For repeated supports, tau-maximality gives `ell>=1` whenever `s<3`.
Hence the only repeated-support rows outside the existing master/descent machinery occupy

> **`1 <= ell <= a-3`.**                                  (8)

In particular:

- a=4: only the exact one-loss row `ell=1` is genuinely higher-slack;
- a=5: only `ell=1,2`;
- all deeper-loss rows have already descended to overlap-saturation or support isolation.

This formally explains why the historical q36 A4/A5 work repeatedly collapsed into a small number of equality rows: loss-layer descent makes that phenomenon structural.

---

# 5. Large supports d=4 and d=9 at q<=38

For `d in {4,9}` the base exchange term is

`d(13-d)=36`.

At the high-right ceiling `q<=38`, the common allowance satisfies

> `a<=2<d-1`.                                              (9)

Therefore all **non-fully-decorated** d4/d9 systems are automatically subcritical.  By `GLOBAL_LARGE_SUPPORT_DECORATED_ESCAPE_THEOREM.md` they consist of

- at most3 plateau singleton classes;
- at most3 strict pairwise-disjoint low-cross blocks.

No additional large-support overlap classification is needed in this regime.

Now assume S is fully decorated.
The exact shell budget gives

> `q>=dN+d`,                                                (10)

so at q<=38

- d=4: `N<=8=12-d`;
- d=9: `N<=3=12-d`.

At maximum possible fully-decorated owner count `N=12-d`, there is exactly one leftover shell vertex x.  `GLOBAL_LARGE_SUPPORT_ONE_LEFTOVER_BRIDGE.md` gives

> `d_M(x)+g_x <= q-36 <=2`.                               (11)

Hence the maximal fully-decorated large-support state automatically descends to the d0/d1/d2 or decorated-one-spoke interface.

Therefore the only fully-decorated d4/d9 states not yet automatically descended by the current theorem stack are

> **`N <= 11-d`, equivalently at least two leftover shell vertices.**   (12)

These are the genuine large-support multi-leftover bridge.

---

# 6. Exhaustive coverage table

Within a common-S family, the current global theorem stack gives the following exact coverage map.

|support size|regime|status under global structural machinery|
|---:|---|---|
|d=2|s<2, a<=1|subcritical; covered|
|d=2|s<2, a=2|first-high-slack decomposition; covered|
|d=2|s<2, a>=3|only shallow-loss rows `1<=ell<=a-2` remain genuinely high-slack|
|d=3|s<3, a<=2|subcritical; covered|
|d=3|s<3, a=3|first-high-slack decomposition; covered|
|d=3|s<3, a>=4|only shallow-loss rows `1<=ell<=a-3` remain genuinely high-slack|
|d=4,9|s<d, q<=38|automatically subcritical; covered|
|d=4,9|s=d, N=12-d, q<=38|one-leftover descent to local defect <=2; covered by low-support interface|
|d=4,9|s=d, N<=11-d|multi-leftover fully-decorated bridge remains OPEN|

The table is exhaustive for the stated common-S regimes.

---

# 7. Minimal remaining forcing-to-master bridge

After this theorem, the structural bridge is no longer an unstructured collection of E335--E340 cases.

It consists of only three logically distinct tasks.

## Bridge A — common-S extraction

Show that every historical surviving shell family contains an active subsystem which can be expressed in the common-S owner language used above, or directly triggers the three-anchor envelope.

## Bridge B — low-support shallow-loss equality

For d2/d3 systems with ambient allowance above first high slack, classify only the finite shallow-loss window

`1<=ell<=a-d` in the equivalent notation above:

- d2: `1<=ell<=a-2`;
- d3: `1<=ell<=a-3`.

Rows beyond this window are already boundary-saturated or isolated by loss-layer descent.

## Bridge C — fully-decorated large-support multi-leftover descent

For d4/d9, only fully-decorated systems with at least two leftover shell vertices are not automatically returned to the low-support interface.

The required theorem is now precise:

> convert the total shell slack carried by two or more leftover vertices into either
> - one low-defect leftover suitable for the d0/d1/d2/one-spoke machinery;
> - a three-signature anchor obstruction;
> - or a dense-decoration contradiction.

No independent K4,9-style classification is needed.

---

# 8. Relation to the strengthened three-anchor theorem

`GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md` gives

`K>=8`, `e(H)>=214`

whenever three pairwise nonadjacent degree-12 anchors exist.  Hence the three-signature branch now obeys

> `q<=E-305`.

Therefore the final backend programme can be stated without E-layer case labels:

1. extract a common-S subsystem or three anchors;
2. if three anchors occur, apply the `E-305` envelope;
3. otherwise use the allowance/loss coverage table above;
4. solve only Bridges B and C plus the common-S extraction step.

This is the current smallest theorem-level description of the remaining backend obstruction.

---

# 9. Portability

The proof architecture is parameterized by

- shell size;
- support size d;
- overlap threshold d-1;
- q-loss;
- the independence-number bound used in block/transversal packing;
- the hereditary density-cap function.

Thus the coverage theorem is not intrinsically tied to E333--E340 or even to r=12.  For larger r, only the numerical thresholds and cap functions change.