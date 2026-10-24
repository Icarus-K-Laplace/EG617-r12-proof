# Recurrence-replacement potentials

Status: `PROVED_SYMBOLIC` / `PROVED_ANALYTIC` as marked below.

Purpose: replace large portions of the r=12 front-end recurrence by scalar invariants that are genuinely uniform in r.

---

## 1. Exact all-colour excess ledger

Let `R_a` be a canonical state on

`n=ar+1`

vertices inside the full r-edge-colouring. Let colour 0 be the target / least colour. Assume

`alpha(G_0[R_a])<=a`.

For each colour `i=1,...,r-1`, the balanced-colouring condition implies

`alpha(G_i[R_a])<=r`,

because every `r+1` vertices must contain an edge of every colour.

Recall that the minimum number of edges in an n-vertex graph with independence number at most k is

`p_k(n)`.

At `n=ar+1`,

`p_a(n)=a*C(r,2)+r`,

and

`p_r(n)=r*C(a,2)+a`.

Define nonnegative edge excesses

`x_0=e(G_0[R_a])-p_a(n)`,

`x_i=e(G_i[R_a])-p_r(n)` for `1<=i<=r-1`.

Since the r colour classes partition all edges of `K_n`, one has the exact identity

> `x_0 + sum_{i=1}^{r-1} x_i = S_a(r)`,

where

> `S_a(r) = [a(a-1)r + 2a - 2r]/2`.

### Proof

Subtract the baseline

`p_a(n)+(r-1)p_r(n)`

from `C(n,2)` and simplify.

Status: `PROVED_SYMBOLIC`.

### Monotonicity

The ledger changes by the exact amount

> `S_a(r)-S_{a-1}(r)=(a-1)r+1`.

Thus `S_a` is a genuine scalar potential associated with one block-extraction step.

Status: `PROVED_SYMBOLIC`.

### Consequence: one near-minimal non-target colour

For every canonical state,

> `min_{1<=i<=r-1} x_i <= floor(S_a(r)/(r-1))`.

For fixed a and large r this upper bound tends to

`a(a-1)/2 - 1`.

Hence a high-stop state necessarily contains at least one non-target colour whose restriction is only O(a^2) edges above the exact `p_r(ar+1)` minimum. This is an explicit finite-width stability interface for the multicolour structure.

Status: `PROVED_SYMBOLIC`.

---

## 2. Alpha saturation on the canonical ray

A canonical state satisfying the critical-ray budget

`e(R_a)<=B_a=p_a(ar+1)+C(r,2)`

cannot have independence number below a.

### Theorem

For every `a>=2`,

> `alpha(R_a)=a`.

### Proof

The canonical construction gives `alpha(R_a)<=a`. Suppose instead `alpha(R_a)<=a-1`.

Then

`e(R_a)>=p_{a-1}(ar+1)`.

By Cauchy / convexity of the balanced-clique minimizer,

`p_{a-1}(n) >= [n^2/(a-1)-n]/2`.

At `n=ar+1`, the difference between this lower bound and the canonical budget is

`[r^2 + ar + r - a + 2]/[2(a-1)] > 0`.

Thus

`p_{a-1}(ar+1)>B_a`,

contradicting the canonical edge budget.

Status: `PROVED_SYMBOLIC`.

### Interpretation

Every canonical state carries an actual independent a-set. The parameter a is therefore not merely an inherited upper cap; it is exact.

In particular, every canonical `5r+1` terminal has `alpha=5` automatically, without an irreducibility hypothesis.

---

## 3. Critical-core potential

Because

`|R_a|=ar+1`

and

`alpha(R_a)=a`,

one has

`chi(R_a)>=r+1`.

Therefore every canonical state contains an induced `(r+1)`-critical graph `Q`.

At a first K_r-free stop, `omega(Q)<=r-1`, so `Q` is not complete.

Let

`q=|Q|`.

The hereditary least-colour cap gives

`e(Q)<=D_r(q)`.

### 3.1 Dirac-cap collision

Dirac's critical-graph bound states that a noncomplete `(r+1)`-critical graph satisfies

`2e(Q)>=r q+r-2`.

Combining this with the hereditary cap yields

> `q>=3r-2`.

Indeed:

- for `q=r+t<2r`, one obtains

  `D_r(q)-[rq+r-2]/2 = -[rt+2r-t^2-t-2]/2 <0`;

- for `q=2r+t`, `0<=t<r`, one obtains

  `D_r(q)-[rq+r-2]/2 = -(t+1)(r-t-2)/2`,

  which is negative for `t<=r-3`.

Status: `PROVED_ANALYTIC`.

External input: Dirac's colour-critical edge theorem.

### 3.2 Kostochka--Yancey refinement: q >= 3r-1

The sharper Kostochka--Yancey bound is

`e(Q) >= ((r+1)/2-1/r) q - (r+1)(r-2)/(2r)`.

At `q=3r-2`, the hereditary cap lies below this lower bound by

`(r-3)(r-2)/(2r)`.

Therefore, for `r>=4`,

> `q>=3r-1`.

Status: `PROVED_ANALYTIC`.

External input: Kostochka--Yancey, *Ore's conjecture on color-critical graphs is almost true*, JCTB 109 (2014), 73--101.

### 3.3 Exact residue feasibility polynomial

Write

`q=l r+t`, `0<=t<r`.

Since

`p_r(q)=r*C(l,2)+l t`,

compatibility of the hereditary cap with the Kostochka--Yancey lower bound requires the single scalar inequality

> `P_{l,t}(r)<=0`,

where

`P_{l,t}(r)
 = r^2(-l^2+3l+t-1)
   + r(-2lt-2l-t^2+2t+1)
   -2t+2`.

This follows from the exact identity

`D_r(lr+t)-KY_{r+1}(lr+t) = -P_{l,t}(r)/(2r)`.

Status: `PROVED_SYMBOLIC` conditional only on the external KY theorem.

### Why this matters

The fixed-r recurrence stored thousands of `(a,n,h,...)` arithmetic states. The critical-core potential compresses every candidate canonical stop to:

1. one integer quotient `l`;
2. one residue `t`;
3. one explicit quadratic feasibility test `P_{l,t}(r)<=0`.

For fixed `l` and large r, middle residues are automatically forbidden; feasible q-values lie in bounded-width windows near multiples of r. For example, the first possible critical-core order is `3r-1`.

This does not yet prove the NO-HIGH-STOP lemma, but it is a genuine bounded-width reduction rather than a parameterized replay of the r=12 tree.

---

## 4. Current recurrence-replacement picture

The r=12 outer recurrence has now been replaced by four symbolic layers:

1. **ray invariant:** `n-ra=s`;
2. **induced trimming:** every anchor defect normalizes to `s=1`;
3. **exact slack potential:** `S_a(r)`;
4. **critical-core potential:** `P_{l,t}(r)`.

The remaining missing theorem is structural rather than arithmetic:

> show that a first K_r-free canonical stop with `a>=6` is incompatible with the multicolour excess ledger / near-minimal colour partitions, or else reduce it to the exact `5r+1` terminal.

That is the current single front-end blocker.