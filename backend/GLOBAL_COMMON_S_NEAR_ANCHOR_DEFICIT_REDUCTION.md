# Global Common-S Near-Anchor Deficit Reduction

Status: **PROVED_ANALYTIC** under the same contract as `GLOBAL_COMMON_S_ALLOWANCE_ANCHOR_TRANSPORT.md`.

This theorem converts the d3 common-missing-triangle higher-slack sector into a parameterized near-three-anchor problem.  It is a reduction theorem, not yet a full closure of A4/A5/A6.

---

## 1. Setup

Use the common-S owner setup of `GLOBAL_COMMON_S_ALLOWANCE_ANCHOR_TRANSPORT.md`.

Assume now

- `d=3`;
- the common missing triple `S={s1,s2,s3}` is target-independent, equivalently `e_M(S)=3`;
- `a` is the exact common-S ambient allowance;
- for each `s in S`, `sigma_s=m_L(s)+g_s-r>=0`.

The allowance-localization theorem gives

`a=e_M(S)+sum_S sigma_s`,

hence

> **`sum_(s in S) sigma_s = a-3`.**                      (NA1)

---

## 2. Exact near-anchor excess after owner repivot

Fix any owner y.  In the repivot core H_y, the three points of S remain pairwise target-nonadjacent.

The exact anchor-transport identity is

`d_(H_y)(s)-12 = sigma_s-|D_s intersect D_y|`.

Summing over the three points of S gives

> **`h_y := sum_(s in S)(d_(H_y)(s)-12)`**
> **`= (a-3)-sum_(s in S)|D_s intersect D_y|`.**          (NA2)

Therefore

> **`0<=h_y<=a-3`.**                                      (NA3)

The lower bound follows from the all-pivot minimum-degree-12 theorem.

Thus every d3 common-missing-triangle owner repivot contains an independent triple whose **total degree excess above 12 is at most a-3**.

---

## 3. Exact shallow-slack hierarchy

Equation (NA3) gives the following uniform interpretation.

### a=3

`h_y=0` for every owner.  The three points of S are three pairwise nonadjacent degree-12 anchors.  Hence the existing global three-anchor theorem applies immediately and

`q_y<=E-305`.

### a=4

Every owner core contains an independent triple with total excess at most1.  Consequently its degree pattern on S is either

- `(12,12,12)`, entering the existing three-anchor envelope; or
- a permutation of `(13,12,12)`.

There is no other local degree geometry.

### a=5

Every owner core contains an independent triple with total excess at most2.  The only possible degree-excess patterns on S are partitions of 0,1,2:

- `(0,0,0)`;
- `(1,0,0)`;
- `(2,0,0)`;
- `(1,1,0)`.

### a=6

The same statement holds with total excess at most3.

Thus the historical A4/A5/A6 shallow-loss missing-triangle sector is not a collection of unrelated support cases.  It is one parameterized near-anchor family indexed only by

> `h=sum_S(d-12) <= a-3`.

---

## 4. The next reusable theorem

The correct continuation is a graph-theoretic theorem independent of shell labels:

> **Near-Three-Anchor Excess Problem.**
>
> Let H be a 35-point graph with `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.  Suppose H contains three pairwise nonadjacent vertices whose total degree excess above12 is at most h.  Determine the sharp lower bound `K>=Phi(h)` for total core excess
>
> `K=sum_v(d_H(v)-12)`.

The known global three-anchor theorem is exactly the case

`Phi(0)>=8`.

Any nontrivial extension to h=1,2,3 immediately feeds back into the backend shallow-loss bridge through (NA2)--(NA3).

For example, if one proves `Phi(1)>=8`, then every d3/A4 missing-triangle owner is either already in the three-anchor envelope or still forces the same `K>=8` global cost; no A4 support-multiplicity classification would remain in that sector.

---

## 5. Why this is structurally preferable

The reduction separates two logically different issues:

1. shell/support geometry, already solved here by exact allowance and transport identities;
2. a pure 35-point graph problem about an almost-minimum-degree independent triple.

The latter has no E-layer label, no common-S language and no solver dependence.  It is therefore the natural candidate for the next paper-level reusable theorem.

---

## 6. Portability

For a larger-r residual problem, the same calculation converts missing-clique allowance into the total excess of the transported independent set relative to the new core minimum degree.  Only the shell size and minimum-degree baseline change.