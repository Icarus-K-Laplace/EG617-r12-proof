# Three-Anchor K=6 / c=4 (10,9,9) Full Closure

Status: **PROVED_ANALYTIC**.

This theorem eliminates the entire `(10,9,9)` four-connector equality partition at `K=6`.

Combined with the c=2, c=3 and `(10,10,8)` closures, it removes the whole K=6 three-anchor equality layer.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- `GLOBAL_THREE_ANCHOR_K6_C4_TWO_K9_DOMINATOR_FULL_CLOSURE.md`;
- the three-anchor partition theorem;
- common missed-set clique / common-nonneighbour machinery;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

No solver and no E-layer label are used.

---

## 1. Setup

Let the block sizes be

`|X1|=10`, `|X2|=|X3|=9`,

with anchors `a1,a2,a3`.

The four pair-connectors have signatures:

- two A-connectors missing `a1`;
- one B-connector missing `a2`;
- one C-connector missing `a3`.

The retained dominator-capacity theorem gives at most one anchor-compatible dominator for each K9 block, and the exactly-two-dominator theorem already excludes the state with one dominator on each K9.

Therefore it remains only to exclude total dominator count zero or one.

We use explicit local excess bounds rather than the older coarse four-/five-unit labels.

---

## 2. Explicit cost of a B- or C-type bad connector

Consider B, which misses anchor `a2` and fails to dominate the opposite K9 block `X3`.

Let

`P=X1\N(B)`, `Q=X3\N(B)`,

`p=|P|>=1`, `q=|Q|>=1`,

`k=kappa_B`.

Let `epsilon` be the number of connector neighbours of B.
The degree equation gives

`p+q >= 9+epsilon-k`.                                       (1)

Because B and `a2` are nonadjacent, `P union Q` is a target clique.
Ignoring any possible dominator of X3 only weakens the estimate.  Hence

- every point of P has the ten-neighbour base `X1 union {a1}` and all q neighbours in Q;
- every point of Q has the nine-neighbour base `X3 union {a3}` and all p neighbours in P.

Thus

> `C_B = k + p(q-2)_+ + q(p-3)_+`                           (2)

is a valid explicit excess lower bound.

### Lemma

`C_B>=4`.

#### Proof

- If `q=1`, then (1) gives `k>=8+epsilon-p`; together with `(p-3)_+` this gives at least5.
- If `p=1`, the symmetric calculation gives at least6.
- If `p,q>=2`:
  - for `p=2`, (1) plus `2(q-2)` gives at least5;
  - for `p>=3`, the minimum occurs on the small boundary `q=2,p=3`, where (1) gives `k>=4`; all larger values only increase the bound.

Hence `C_B>=4`.

The same theorem holds for C by symmetry.

---

## 3. Different missed-anchor explicit costs are additive

Take two exceptional connectors with different missed anchors.
Their private missed blocks are disjoint; their local ledgers can overlap only on one shared exclusive block.

Suppose a shared witness is forced adjacent to private missed sets of sizes A and B.  If its fixed base leaves charge threshold c, then its actual excess is at least

`(A+B-c)_+`.

For nonnegative A,B and positive c,

> `(A+B-c)_+ >= (A-c)_+ +(B-c)_+`.                          (3)

Therefore the actual excess at every shared witness dominates the sum of the amounts charged by the two separate local ledgers.

Consequently explicit defect costs belonging to different missed-anchor types are additive.

This is the same global compatibility mechanism used in the c=3 and `(10,10,8)` closures.

---

# 4. Zero dominators are impossible

If no connector dominates either K9, then in particular B and C are both bad.

By Section2,

`C_B>=4`, `C_C>=4`.

They have different missed anchors, so Section3 makes the costs additive:

`K>=C_B+C_C>=8`.

This contradicts `K=6`.

Therefore the zero-dominator regime is empty.

---

# 5. Exactly one dominator: A-type dominator

Suppose the unique dominator is one of the two A-connectors.

Then neither B nor C is a dominator, so both are bad.
Exactly as in Section4,

`K>=4+4=8`,

contradiction.

Thus the unique dominator cannot be A-type.

---

# 6. Exactly one dominator: natural B/C dominator

Assume, without loss of generality, that B is the unique dominator and dominates X3.
Then C is bad, so

`C_C>=4`.

Both A-connectors are non-dominating; choose either one, call it A.  Since it misses anchor a1 and is not a dominator of either K9, it misses nonempty sets

`P subset X2`, `Q subset X3`,

with sizes p,q>=1.

Because B dominates X3, every point of Q has one additional fixed target neighbour.  The explicit local cost of A is therefore

> `C_A = k + p(q-3)_+ + q(p-2)_+`,                          (4)

where the degree equation gives

`p+q >= 8+epsilon-k`.                                       (5)

### Lemma

`C_A>=3`.

#### Proof

- If one of p,q equals one, (5) immediately gives a bound at least4.
- If p,q>=2:
  - for p=2 the minimum occurs at q=3, where `k>=3` and the block terms vanish;
  - for p>=3 the q=2 boundary already gives at least5, and larger q only increases the block term.

Thus `C_A>=3`.

The bad C-connector and A have different missed anchors.  Their explicit ledgers overlap only on X2, and the additivity inequality (3) applies there.
Therefore

`K>=C_C+C_A>=4+3=7`,

contradicting `K=6`.

The case in which C is the unique dominator is symmetric.

Hence exactly one dominator is impossible.

---

# 7. Complete closure

The exactly-two-dominator regime was already closed by
`GLOBAL_THREE_ANCHOR_K6_C4_TWO_K9_DOMINATOR_FULL_CLOSURE.md`,
and the dominator-capacity theorem excludes any higher occupancy of a K9 slot.
Sections4--6 exclude total dominator count zero or one.

Therefore

> **there is no three-anchor K=6 core in the `(10,9,9)` c=4 partition.**

This completes the last c=4 partition.

---

## Reusable principle

The proof isolates a global exceptional-cost additivity principle:

> when two connector defects miss different anchors, their private missed blocks are disjoint and any shared-block excess is convexly additive.  Hence a small global excess budget cannot support several connector exceptions of different anchor types.

This turns dominator-slot scarcity directly into a global excess contradiction.