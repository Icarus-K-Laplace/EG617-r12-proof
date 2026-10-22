# E406 full closure

Status: `PROVED EMPTY` under the explicit T61 hereditary-cap parent contract.

This is the canonical E406 theorem. It supersedes the earlier `E406_FULL_CLOSURE_COMPOSED.md`, whose only remaining caveat was independent replay of the V7 q30 plateau theorem. That theorem has now been independently reconstructed as `Q30_HEREDITARY_PROMOTION_CANONICAL.md`.

## Theorem

There is no 61-vertex T61 h13 parent R satisfying

- `e(R)=406`;
- `delta(R)=13`;
- `alpha(R)<=5`;
- `omega(R)<=11`;
- all inherited density caps and shell/core contracts.

Equivalently,

`T61(E406)=empty`.

## 1. S31 supplies a low pivot

The audited S31 strict-descent theorem applies to the same E406 parent and gives a degree-13 pivot p with

`q_p<=30`.

No stronger conclusion about q_p is assumed here.

## 2. Every low pivot reaches a genuine q30 pivot

By `E406_LOW_TO_Q30_BRIDGE.md`, any E406 degree-13 pivot with q<=30 lies in a parent containing a genuine degree-13 q30 pivot.

The bridge is fully analytic:

- q22 and q23 are impossible;
- q24--q26 have regular d2/d3 promotion witnesses to q>=27;
- direct jumps from those witnesses to q31 are impossible by the inserted-core minimum-degree equations;
- q27 and q28 are impossible;
- q29 has a regular middle-degree witness and can only promote to q30, not directly to q31.

Thus fix a genuine q30 pivot r.

Its 47-core has285 edges and minimum degree at least12.

## 3. q30 necessarily reaches q31 in at most two regular repivots

Apply `Q30_HEREDITARY_PROMOTION_CANONICAL.md`.

Every q30 pivot either has an immediate regular repivot of charge at least31, or its shell belongs to one of two analytically exhaustive no-immediate-rise families.

- Family I (`K_(3,k)` plus isolates, k=8,9,10) is incompatible with the global excess budget and alpha/omega constraints after the equal-or-disjoint row decomposition.
- Family II (`K_(2,11)` plus one exceptional missing edge) cannot persist for two regular repivots: its ten forced outside pairs become pairwise target-anticomplete and create an independent set far larger than alpha(R)<=5.

Therefore some sequence of at most two regular repivots from r reaches a pivot y with

`q_y>=31`.

For E406 the universal 284-core floor gives `q_y<=31`, hence

`q_y=31`.

If two steps are used, the intermediate pivot has q30. Therefore the final step is an actual adjacent pivot-graph edge

`q30 -> q31`.

## 4. The final-rise distance is one of six classes

Orient the final edge from the q30 pivot p to the q31 pivot y. Let

`d=d_M(y)`.

At q30 the old core has minimum degree at least12. The exact repivot formula gives

`q_y=d(13-d)+rho+h+kappa+b`,

with all correction terms nonnegative.

Since q_y=31,

`d(13-d)<=31`.

Thus

`d in {0,1,2,3,10,11,12}`.

The case d=0 cannot change the 47-core edge count, hence cannot change q from30 to31. Therefore

`d in {1,2,3,10,11,12}`.

## 5. Every possible final-rise distance is empty

All six classes have independent proof bodies.

### d=1

Closed by

- `E406_D1_MATCHING2_REDUCTION.md`;
- `E406_D1_KAPLUS2_CLOSURE.md`;
- `E406_D1_FULL_CLOSURE.md`.

The final matching-two 4-edge cover geometries `C4` and paw are both impossible.

### d=2

Closed by

- `E406_D2_RETAINED_BLOCK.md`;
- `E406_D2_EGE2_CLOSURE.md`;
- `E406_D2_E1_CLEAN_SUPPORTS.md`;
- `E406_D2_E1_ED0_CLOSURE.md`;
- `E406_D2_E1_ED1_CLOSURE.md`.

The retained-star layers e>=2 are impossible, and the sole e=1 terminal is empty in both possible old-core pair geometries.

### d=3

The q30->q31 d3 normal forms reduce to Type A / Type B. Type B is empty. Type A is compressed to the O5/O4 support system.

The full closure is the union of:

- `E406_D3_TYPE_B_CLOSURE.md`;
- `E406_D3_TYPEA_O5_FULL_CLOSURE.md`;
- `E406_D3_NO_FOURFULL.md`;
- `E406_D3_O4_SIMPLE_ETA0_FULL_CLOSURE.md`;
- `E406_D3_O4_SIMPLE_ETA1_FULL_CLOSURE.md`;
- `E406_D3_O4_TRIPLE2DOUBLE_ETA0_CLOSURE.md`;
- `E406_D3_O4_TRIPLE2DOUBLE_ETA1_CLOSURE.md`;
- `E406_D3_O4_TWO_TRIPLES_CLOSURE.md`.

Hence d3 is empty.

### d=10

Closed in `E406_Q31_PLATFORM_SUPPORT_RIGIDITY.md`: the pure reverse K10 support and the two remaining K10/K10-e supports violate the inherited D(13)/D(14) caps.

### d=11

Closed by `E406_D11_FULL_CLOSURE.md` after the exact three-star-block reduction. The final equality-star geometry contradicts the zero-slack / PAIR-13 system.

### d=12

Closed by

- `E406_D12_MATCHING_REDUCTION.md`;
- `E406_D12_MATCHING2_SMALL_COVER.md`;
- `E406_D12_FULL_CLOSURE.md`.

The only remaining `K4-e`, `C4`, and paw small-cover geometries all force inserted vertices of new-core degree at most11, contradicting the minimum-degree12 theorem.

Thus no q30->q31 final-rise edge exists.

## 6. Contradiction

Sections 1--3 force an actual q30->q31 adjacent regular repivot in every hypothetical E406 parent.

Sections 4--5 prove that every possible distance of such an edge is impossible.

Contradiction.

Therefore

> **E406 is empty.**

## Dependency boundary

This theorem does not use any E407/E408 result and does not use backend E333--E340. It is independent of Astra A's current E407/E408 assignment and Astra B's high-backend assignment.

The full EG617 r=12 theorem remains open because E407/E408 and E333--E340 are separate obligations.
