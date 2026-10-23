# Global Support Bridge Frontier

Status: `OPEN`.

This file records the single structural bridge that should replace independent E333--E340 case closure.

It depends on `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`, whose charging, packing, overlap and low-charge-witness statements are `PROVED_ANALYTIC`.

## 1. Target bridge lemma

### Extremal Support-Extraction / Equality-Rigidity Bridge

Let F be a legal r=12 residual graph under the retained pivot contract, and let p be a lexicographically maximal `(q,tau)` pivot in any unresolved high-backend layer.

Then at least one of the following should hold.

### Alternative I — direct improving repivot

There is a common-missing-set owner family `Y` with support hypergraph I such that

`Phi(I) := sum_v lambda_v w_v + sum_y mu(D_y)`

violates the strengthened global compatibility bound

`Phi(I) <= N a - L_min`,

where

`L_min=max(0,N-floor(n/(d-s)))`.

Equivalently the exact support-gain identity forces some `q_y>q`, contradicting maximality.

### Alternative II — rigid equality geometry

The support system attains equality or near-equality in the global compatibility theorem. Then all locally free quantities are forced into one of a small number of global geometries:

1. `d=2`: low-charge two-block / matching geometry;
2. `d=3`: common-pair, four-set, sunflower, or dense repeated-K3 geometry;
3. `d=4/9/10`: the corresponding plateau block geometries already appearing in the q36--q38 joint-row analysis;
4. shell-poor one-spoke states: a simultaneous low-charge/triangle-cover geometry rather than independent one-spoke cases.

Each equality geometry must then be excluded by one global hereditary-cap / excess / independence argument.

The desired final theorem is that every geometry in Alternative II is impossible.

If both alternatives are proved exhaustively, no high-backend survivor exists.

## 2. Why this is the right bridge

The local shell families differ in labels, but their load-bearing data are the same:

- a common missing object S;
- owner count N;
- support size d;
- support incidence degrees lambda_v;
- charge w_v=kappa_v+e_F(v,S);
- row allowance a;
- support internal missing count mu(D);
- overlap codegrees;
- target cross-density between disjoint supports;
- q-loss and tau transport under repivot.

The exact identity

`sum(q-q_y)=Na-sum lambda_v w_v-sum mu(D_y)`

shows that these are not merely analogous quantities: they are the complete accounting variables for total repivot gain/loss in a common-S family.

## 3. Existing families already covered

### E333

Status: `KILLED` relative to the retained V4 forcing contract.

The five necessary families

- D2-A,
- D2-B,
- D2-C,
- D2-D,
- R9

all enter the d=2 common-S framework.

Their repetition lower bounds `(8,8,5,7,9)` are therefore best viewed as lower bounds on the size of one support-incidence system, not five unrelated cases.

V5 shows that the low-charge alternative forces capacity bounds 4/6 except for one allowance-two equality system. That equality system is exactly the two-clique-plus-perfect-matching geometry and is excluded by the residual edge ledger.

Thus E333 is already the first completed application of the Global Support-Compatibility architecture.

### E334

Current source-reported V7 state, pending independent package replay:

- maximal pivot forced to `q=32`, `e(H)=211`, so `K=2`;
- q30/core213 and q31/core212 are excluded;
- unresolved structures are the d3 eleven-view system, `r=2/allowance=2`, and `r=1/allowance=3`.

All three are naturally support-incidence problems:

- the r=2/A2 and r=1/A3 branches are repeated two-point/common-S capacity states;
- the d3 eleven-view branch is a 3-uniform support hypergraph with a very small CORE211 excess budget.

Therefore E334 should not receive three unrelated final proofs. The target is to show that each branch satisfies Alternative I or falls into the same small equality list in Alternative II.

### E335--E337

V6 already proves the d=2 capacity theorem through core213 (`K<=6`) whenever such a family is forced.

The genuinely new obstacle at higher K is not a new shell case but the loss of an outside zero-charge witness. The correct replacement is the low-charge theorem

`alpha(H[U\N(v)])<=2`.

The bridge task is to use a charge-1 or charge-2 outside witness to force a near-equality version of the V5 two-block geometry.

### E338--E340

The q36--q38 work has independently rediscovered the same structure:

- common d2/d3 rows in the q36 low-clique regime;
- common-S support overlap/cross-density constraints;
- repeated-support decoration forcing;
- d4/d9 plateau geometries;
- the q38 K4,9 equality family, already killed;
- shell-poor one-spoke states, now coupled by a simultaneous triangle-cover / decoration interface.

The remaining problem is coverage/extraction: prove that every surviving top-q shell feeds one of the global support systems above, rather than treating each q36/q37/q38 shell separately.

## 4. Front-end compatibility

The front-end Q31 work was also closed by global multi-row/core-capacity rather than a single local row contradiction. Q32/Q33 retain the same qualitative problem: a small amount of correction slack must be globally compatible across multiple pivots.

The support-gain identity is algebraically the same kind of potential statement. A front-end version should be sought by replacing the backend charge `w_v` with the corresponding labelled 47-core correction weight.

This is currently `CONDITIONAL`: the exact front-end variable translation has not yet been written as a theorem.

If that translation succeeds, the paper can present one higher-level principle:

> locally admissible pivots cannot all be globally compatible once support/correction incidence exceeds the extremal charge budget.

## 5. The unique missing bridge

The project should now target one statement:

> **Bridge Lemma.** Every unresolved r=12 maximal-pivot survivor contains a common-support incidence subsystem for which either the Global Support-Compatibility inequality is strict in the forbidden direction, or every inequality is forced to equality and the resulting equality geometry belongs to an explicitly classified finite list that violates the inherited density/independence contracts.

This is one bridge even though its proof may have 2--3 structural regimes.

The smallest acceptable split is expected to be:

1. low-support regime (`d=2,3`);
2. large-support / plateau regime (`d=4,9,10`);
3. shell-poor one-spoke regime.

A proof requiring separate E333,...,E340 arguments should be considered a fallback, not the primary architecture.

## 6. Equality cases to classify

When the global inequality is non-strict, record all equalities simultaneously:

- every plateau row saturates `w(D)+mu(D)=a`;
- every plateau support has exactly the allowed number s of decorated vertices;
- clean support vertices are private;
- overlap inequalities saturate;
- disjoint-support cross-edge bounds saturate;
- outside low-charge witnesses saturate the alpha-two deletion condition;
- core excess K is concentrated on the smallest possible set;
- hereditary D(n) caps are saturated on the induced base-plus-support sets.

This should leave only a small extremal geometry, analogous to the already-killed two-clique-plus-perfect-matching and K4,9 equality states.

## 7. What would close which layers

If the Bridge Lemma is proved under the current backend contract:

- E333 is already closed and becomes a corollary/example;
- E334--E337 would close provided the source-reported maximal-pivot forcing inputs are independently certified and mapped into the bridge hypotheses;
- E338--E340 would close once the current q36--q38 coverage reductions are shown to exhaust the low-support / plateau / shell-poor regimes.

Thus the bridge is capable in principle of closing the entire high backend in one structural theorem.

It does not by itself close the still-open front-end Q32/Q33 states; that additionally needs the 47-core correction-weight translation described in Section 4.

## 8. Generalization beyond r=12

The core theorem is parameterized by

- shell size h;
- core size n;
- support size d;
- row allowance a;
- missing-set decoration count s;
- total charge/excess;
- hereditary cap function.

The exact charging and plateau-packing arguments therefore plausibly extend to r>=13.

The r-specific inputs are currently:

- the original reduction producing the pivot contract;
- the all-pivot core minimum-degree theorem;
- the hereditary D(n) constants;
- the finite equality-geometry exclusions.

A successful Bridge Lemma written with symbolic h,n,d,a would therefore make r=12 the first substantial application of a more general extremal repivot-compatibility theorem rather than an isolated computer-assisted case closure.

## 9. Immediate research program

Priority order from this point:

1. prove the low-support (`d=2,3`) Bridge Lemma using low-charge witnesses `t=0,1,2`;
2. derive the equality classification from simultaneous saturation of (G1)--(G16);
3. fit the q36--q38 large-support plateau families into the same statement;
4. integrate the shell-poor one-spoke simultaneous interface;
5. only then fall back to individual edge-layer closure if a genuine structural split remains.
