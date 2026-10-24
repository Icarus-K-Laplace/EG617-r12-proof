# Progress log

## 2026-10-24 — Round 1: r=12 reverse engineering -> Level A core theorem

### NEW THEOREM / LEMMA

**General residual-core minimum-degree theorem.**

### Hypotheses

For `r>=17`, `H` has `3r-1` vertices, `alpha(H)<=3`, `omega(H)<=r-1`, and inherits the least-color hereditary cap on every induced subgraph.

### Exact conclusion

`delta(H)>=r`.

### Proof sketch

1. A `2r` induced obstruction with alpha at most 2 is impossible by exact cap + triangle-free complement + AES.
2. Hence `delta(H)>=r-1`.
3. If `d(v)=r-1`, the complement on the `2r-1` nonneighbors is non-bipartite triangle-free with exactly `(r-1)^2` or `(r-1)^2+1` edges.
4. A shortest-odd-cycle argument forces a `C5`; the remaining `2r-6` vertices are exactly a near-complete bipartite graph with total defect at most one.
5. Full hereditary cap on `C5 + one bipartition side + b` forces every row defect from the neighbor set `B=N_H(v)` into the nonneighbor set to be at most 8.
6. Any complement edge inside `B` needs two row defects summing to at least `r`; `omega(H)<=r-1` forces such a complement edge.
7. Contradiction for `r>=17`.

### Dependency

External: Andrasfai--Erdos--Sos; Erdos non-bipartite triangle-free edge bound.

Internal: hereditary least-color cap only. No backend.

### Independent of r?

Symbolic proof; threshold `r>=17` is explicit.

### Minimal remaining counterconfiguration if threshold not met

For `6<=r<=16`, only the exact degree-`r-1` near-Mantel/C5 boundary remains; no claim of existence.

### GitHub commits

- dependency map: `548ba50884d7d67ba1731b5e3d792aea0ad109fb`
- first boundary compression: `b92a7ee777b18dd78e24c340f87236d61998d136`
- upgraded full `delta(H)>=r` theorem: `9728aa35d3c7de6404cf86758435ba023d8b27c1`

---

## 2026-10-24 — Round 2: close the entire 4r+1 residual branch

### NEW THEOREM / LEMMA

**Residual branch closure theorem.**

### Hypotheses

For `r>=17`, `F` has `4r+1` vertices, `alpha(F)<=4`, `omega(F)<=r-1`, and inherits the hereditary cap.

### Exact conclusion

- `delta(F)=r+1`;
- there is a degree-`(r+1)` pivot `p`;
- `H=F-N[p]` has

  `|H|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`.

### Proof sketch

The core theorem implies a `3r` exclusion. A vertex of degree at most `r` in `F` would leave a `3r` induced nonneighbor subset with alpha at most 3, contradiction. Thus `delta(F)>=r+1`. The exact cap `D_r(4r+1)=2r^2+4r+4` rules out `delta(F)>=r+2`, so equality and a legal pivot follow.

### Dependency

`CORE_MINDEG_BOUNDARY_THEOREM.md` + AES for the derived `3r` exclusion.

### Independent of r?

Uniform symbolic/analytic proof for all `r>=17`.

### External theorem?

AES, via the core theorem and `3r` exclusion.

### Minimal failure point

No failure inside Branch A for `r>=17`; the only missing source is extraction of `F` itself.

### GitHub commit

`9740d0c798ea1374a5825c798bc808954f429ffc`

---

## 2026-10-24 — Round 3: eliminate anchor-defect rays

### NEW THEOREM / LEMMA

**Affine outer-ray invariant + induced trimming normalization.**

### Hypotheses

Minimum-degree anchor `d=r-s`, canonical block extraction, inherited edge budget.

### Exact conclusion

After `j` blocks, with `a=r-1-j`, the raw state has

`n=ar+s`.

For every `s>=1`, an induced `ar+1` subgraph exists with edge budget no larger than the critical `s=1` budget.

Thus all anchor defects normalize to one critical ray.

### Proof sketch

- exact algebra gives `n-ra=s`;
- averaging over induced `(ar+1)`-subsets and a factored polynomial inequality gives budget preservation.

### Dependency

Only the minimum-degree pivot identity and block edge count.

### Independent of r?

Yes.

### External theorem?

Brooks is used separately to guarantee an anchor with `d<=r-1`.

### Minimal failure point

None for normalization. The remaining issue is where greedy `K_r` extraction first stops.

### GitHub commits

- ray invariant: `7d36261a29192bd60b92d728a127ae6125d8d224`
- canonical normalization/extraction: `07cd8fb58ffd93d234b1e8b6104f939175d7fbda`

---

## 2026-10-24 — Round 4: exact 5r+1 terminal

### NEW THEOREM / LEMMA

**Irreducible 5r+1 terminal contract.**

### Hypotheses

The canonical greedy process first becomes `K_r`-free at `a=5`, and no `4r+1` Branch-A induced subgraph is already present.

### Exact conclusion

`T_r` satisfies

- order `5r+1`;
- `alpha=5`, `omega<=r-1`;
- hereditary cap;
- `e<=3r^2-2r`;
- no `K_r`;
- `delta>=r`;
- the hypergraph of independent 5-sets has transversal number at least `r+1`;
- every degree-r row has an explicit independent-4 witness property.

### Proof sketch

Alpha equality is now automatic from the canonical budget. Branch-A irreducibility is exactly equivalent to the independent-5 hypergraph resisting every r-vertex transversal. Minimum degree follows because a degree at most `r-1` vertex leaves at least `4r+1` nonneighbors with alpha at most 4.

### Dependency

Residual branch closure + alpha-saturation theorem.

### Independent of r?

Symbolic; terminal use currently paired with `r>=17` residual closure.

### External theorem?

None beyond dependencies.

### Minimal failure point

Whether the terminal exists remains open.

### GitHub commits

- initial terminal: `4d2feba3cf8c52f9099fe14b7953eb637148df46`
- alpha-equality strengthening: `fc774dd80d94c1abc508c285f435d5a5eedfbea2`

---

## 2026-10-24 — Round 5: scalar recurrence replacement

### NEW THEOREM / LEMMA

**Exact multicolour slack potential + critical-core potential.**

### Hypotheses

Canonical state `R_a` on `ar+1` vertices inside the full balanced r-colouring.

### Exact conclusions

1. If `x_0` is the target-colour excess above `p_a` and `x_i` the other colours' excess above `p_r`, then

   `x_0 + sum x_i = S_a(r)=[a(a-1)r+2a-2r]/2`.

2. `S_a-S_{a-1}=(a-1)r+1`.
3. Every canonical state has exact `alpha(R_a)=a`.
4. Every canonical state contains an induced `(r+1)`-critical core.
5. At a `K_r`-free stop, its critical-core order is at least `3r-1` for `r>=4`.
6. Writing the critical-core order as `lr+t`, `0<=t<r`, compatibility with the hereditary cap and Kostochka--Yancey is exactly one quadratic inequality `P_{l,t}(r)<=0`.

### Proof sketch

The slack identity is exact edge partitioning across all r colours after subtracting their individual Turan minima. Alpha saturation follows because `p_{a-1}(ar+1)` already exceeds the canonical edge budget. Critical-core order is obtained by colliding Dirac/Kostochka--Yancey lower bounds with the hereditary least-color upper cap.

### Dependency

- internal: canonical ray + full balanced-colouring alpha constraints;
- external: Dirac critical-graph bound and Kostochka--Yancey 2014.

### Independent of r?

The identities are fully symbolic; the sharpened `|Q|>=3r-1` holds for `r>=4`.

### Minimal remaining counterconfiguration

A first `K_r`-free stop with `a>=6` satisfying simultaneously exact alpha saturation, the `S_a` ledger, the hereditary cap, and a critical-core residue passing `P_{l,t}(r)<=0`.

### GitHub commit

`76f65dca0f1bf755a93b2a25331a238bd73383b2`

---

## 2026-10-24 — Round 6: high-stop concentration + exact predecessor interface

### NEW THEOREM / LEMMA A — Simultaneous excess concentration

### Hypotheses

First `K_r`-free canonical stop `R_a`, `a>=6`, `r>=a+1`, with exact ledger `sum_i x_i=S_a(r)`.

### Exact conclusion

At least `floor(r/2)` non-target colors satisfy

`x_i<=C_{a,r}:=ceil(2S_a(r)/(r-1))<=a^2-1`.

For each such color, its complement is `K_{r+1}`-free and exactly `x_i` edges below the Turán maximum. For `a=6,r>=41`, at least `floor(r/2)` colors have `x_i<=29`.

### Proof sketch

Markov counting: if more than half of the `r-1` non-target excesses exceeded `C_{a,r}`, their sum would exceed `S_a(r)`. The bound `C_{a,r}<=a^2-1` follows from `r>=a+1`.

### Dependency / range

Purely symbolic, uniform for all canonical `a<=r-1`; no external theorem.

### Status

`PROVED_SYMBOLIC`. This is edge-count near-extremality only; it does not yet give an edit-distance partition theorem.

### NEW THEOREM / LEMMA B — Critical-core residue windows

### Hypotheses

Critical core order `q=lr+t`, `0<=t<r`, with `P_{l,t}(r)<=0` and `l>=2`.

### Exact conclusion

For `r>=R_l=l(l-1)^2(l-2)+2l+2`, feasibility forces

`t<=l^2-3l+1` or `r-t<=l^2-l-1`.

For `a=6,r>=614`, the only possible core-order windows are

`[3r-1,3r+1]`, `[4r-5,4r+5]`, `[5r-11,5r+11]`, `[6r-19,6r+1]`.

### Proof sketch

Rewrite `P/r` as a concave quadratic in `t`, and also in `u=r-t`. At the first integer outside each proposed boundary window and at the midpoint, the corresponding quadratic is positive for `r>=R_l`; concavity excludes the entire middle interval.

### Dependency / range

Symbolic algebra plus the already-approved Kostochka--Yancey compatibility inequality. Uniform for each fixed `l` once `r>=R_l`; not uniform for unbounded `a` without further work.

### Status

`PROVED_ANALYTIC` as a necessary-condition reduction. It kills all middle residues, but does not eliminate the surviving windows or close `a=6`.

### NEW THEOREM / LEMMA C — First-stop predecessor interface

### Hypotheses

`R_a` is the first `K_r`-free state, and `B=K_r` is the target clique removed from predecessor `R_{a+1}`.

### Exact conclusion

For each outside vertex `v`, the `r` edges `vB` either contain one target edge and every non-target color exactly once, or contain no target edge and exactly one duplicated non-target color. If `q_0` is the target cross-edge count and `z_i` counts duplicated color `i`, then

`sum_i z_i=ar+1-q_0`,

`x_0(R_{a+1})=x_0(R_a)+q_0`,

`x_i(R_{a+1})=x_i(R_a)+z_i`.

### Proof sketch

Every `r+1`-vertex set `B union {v}` must contain every color; `B` already supplies the target color. Counting the remaining `r` cross-edges yields the two alternatives and the excess increment identities.

### Dependency / range

Exact balanced-coloring property only; all r.

### Status

`PROVED_SYMBOLIC`. The lemma is a new input for the clique-transversal route, but no induced `R_{a-1}` theorem follows yet.

### Minimal remaining counterconfiguration

A first high stop satisfying the excess ledger, simultaneous near-Turán edge counts, one of the surviving critical-core windows, and the predecessor near-permutation interface.

### GitHub commit

`365f6b4e98fc49cd5586eef97afde2d52c0e8e35`

---

## Current single blocker

Status: **`OPEN`**.

**NO-HIGH-STOP LEMMA:** a canonical greedy process cannot first become `K_r`-free at `a>=6` for all sufficiently large `r`.

Round 6 did not close this theorem. Round 7 closed the uniform partition-stability subgap using Füredi's theorem and proved a global near-resolvable design with at most `3S_a(r)` bad pairs. However, `a=6` is still open; no high-a induction trim or design-trimming contradiction is proved.

If this is closed, the requested front-end dichotomy is proved for all `r>=17` (or whatever final threshold the lemma requires).

Latest state / proposal commits:

- `CANONICAL_STATE.md`: `00b152a60dbb479cb32e233a3a7480ecebbb2a03`
- `OPEN_GAPS.md`: `a671769e80c9aeb4702c4848fe63d08165395871`
- `NO_HIGH_STOP_ROUND2_LEMMAS.md`: `c4886cf7f4f8f2cfbc0a0ab23b737c7e83303cea`.
---

## 2026-10-24 — Round 7: uniform partition stability -> global near-resolvable design

### NEW THEOREM / LEMMA

**Global near-resolvable design theorem for a first high stop.**

### Hypotheses

First `K_r`-free canonical stop `R_a`, with `n=ar+1`, exact all-colour ledger `sum_i x_i=S_a(r)`, and inherited hereditary caps.

### Exact conclusions

For every color i, let `F_i` be the complement of its color graph; the target color uses `k_0=a`, and each non-target color uses `k_i=r`. Then `F_i` is `K_{k_i+1}`-free with exact Turán deficit `x_i`.

By Füredi's quantitative Turán theorem, there is a `k_i`-part partition with at most `x_i` internal edges to delete. If `I_i` counts internal edges, `M_i` missing cross-pairs, and `Delta_i` part-size imbalance, then

`I_i<=x_i`, `Delta_i+M_i=x_i+I_i<=2x_i`, and `I_i+M_i<=3x_i`.

The part sizes `s_j` satisfy

`sum_j (s_j-q)^2=2 Delta_i+1<=4x_i+1`,

where `q=r` for the target partition and `q=a` for non-target partitions.

Summing over all colors yields

`sum_i I_i<=S_a(r)`, `sum_i M_i<=2S_a(r)`, and total partition defects `<=3S_a(r)`.

Therefore at most `3S_a(r)` vertex pairs fail to be represented by exactly one block of their actual color and by no block of any other color. For fixed `a`, this is `O(r)` bad pairs among `Theta(r^2)` total pairs: a global approximate pairwise-balanced/resolvable design.

### Proof sketch

Use Füredi's theorem that a `K_{k+1}`-free graph with `t_k(n)-x` edges can be made `k`-partite by deleting at most `x` edges. The identity `x=Delta+M-I` gives the stated bounds. A pair that is in no partition block is charged to a missing cross-pair defect; a pair in multiple color blocks is charged to an internal-edge defect in at least one of those colors.

### Dependency

Internal: exact all-colour excess ledger. External: Füredi's quantitative Turán stability bound, as recalled by Balogh–Clemen–Lavrov–Lidický–Pfender, *Making K_{r+1}-free graphs r-partite* (2021), DOI `10.1017/S0963548320000590`.

### Independent of r?

Yes: the partition/edit bounds are uniform in the growing clique parameter. The total bad-pair count is symbolic in `a,r`.

### Does this close NO-HIGH-STOP?

No. The near-design can have `O(r)` exceptional pairs, on the same scale as the missing-class budget. Their incidence pattern has not yet been shown to admit an `r`-vertex transversal or to contradict first-stop minimality.

### New status

- uniform partition stability: `PROVED_ANALYTIC`;
- global near-resolvable design: `PROVED_ANALYTIC`;
- `a=6` exclusion: `OPEN`;
- arbitrary `a>=7` induction trim: `OPEN`;
- `NO-HIGH-STOP`: `OPEN`.

### GitHub commits

- theorem asset: `c4886cf7f4f8f2cfbc0a0ab23b737c7e83303cea`
- canonical state: `00b152a60dbb479cb32e233a3a7480ecebbb2a03`
- open gaps: `a671769e80c9aeb4702c4848fe63d08165395871`
---

## 2026-10-24 — Round 8: predecessor label capacity + target-complement hub localization

### NEW LEMMA A — Label capacity on the predecessor clique interface

Let `B=K_r` be the target-color clique deleted from `R_{a+1}` to obtain first stop `R_a`, and let `z_i` count vertices whose `B`-cross edges duplicate non-target color `i`.

For each non-target color `i`, the vertices with a unique `i`-colored neighbor `b` in `B` form a color-`i` clique: for any pair `u,v` in this class, the `r+1` set `(B\\{b}) union {u,v}` contains every color other than `i`, forcing `uv` to have color `i`.

These classes are target-independent and therefore have size at most `alpha(G_0[R_a])=a`. There are `r` classes, and they cover `ar+1-z_i` vertices, so

`z_i>=1` for every non-target color.

Consequently `sum_i z_i>=r-1` and `q_0<= (a-1)r+2`, where `q_0` is the number of target-color cross edges from `R_a` to `B`.

The exact class-hole identity is

`sum_{b in B}(a-|S_{i,b}|)=z_i-1`.

If `z_i=1`, all `r` label classes have size exactly `a`. This is a stronger exact incidence statement than the original monotonicity of excesses.

### NEW LEMMA B — Fixed-a hub localization

Let `F_0=bar(G_0[R_a])`. The all-color ledger gives `x_0<=S_a(r)`, and Füredi stability gives a partition into `a` parts with

`M_0<=2x_0`, `sum_j(|V_j|-r)^2<=4x_0+1`.

For fixed `a>=6` and `r>=200a(a-1)+1`, every part has size at least `0.9r`, and `M_0<=a(a-1)r`. If an internal edge `uv` of `F_0` had neither endpoint missing at least `2r/5` cross-neighbors to any other part, their common neighborhoods in each other part would have size at least `r/10`. A random transversal across these common neighborhoods has probability at most `100M_0/r^2<1` of containing any missing cross-pair, so some transversal is a `K_{a+1}` together with `uv`, contradiction.

Thus every internal edge is incident to a hub with missing cross-degree at least `2r/5` to some part. Since total missing cross-degree is `2M_0`,

`|H|<=5M_0/r<=5a(a-1)`.

For `a=6`, `S_6=14r+6`; the sharper calculation gives `r>=5601`, `M_0<=28r+12`, and `|H|<=140`.

Deleting `H` makes every target partition part a target-color clique. This localizes all internal defects but does not show the hub-protection parts have a common sink; directed cycles of protection remain possible.

### What remains open

- `a=6` has not been eliminated.
- No hub-propagation theorem or correct-budget `R_5` extraction has been proved.
- `NO-HIGH-STOP` remains `OPEN`.

### GitHub commits

- label-capacity lemma: `c67a1e18ecd3e8b443513f1a272892aa225386fc`
- canonical state: `06d8ab213b721aebd36b0fc06b5862277eaa6fa3`
- open gaps: `ad962ed6dd44eb32a634727dd4aa52eaa16c0fa7`
---

## 2026-10-24 — Round 9: absolute-width target groups and product-cover hub theorem

### NEW THEOREM A — Constant-width target ideal groups

Let `F_0=bar(G_0[R_a])` and use the Füredi partition into `a` target ideal groups `V_j`, with `s_j=|V_j|`. The internal target-complement edge count satisfies `D<=x_0`, while for each group

`e(F_0[V_j])=sum_{i>0}e(G_i[V_j]) >= (r-1)p_r(s_j) >= (r-1)(s_j-r)_+`.

Thus, with `P=sum_j(s_j-r)_+`,

`(r-1)P<=D<=x_0<=S_a(r)=(binom(a,2)-1)r+a`.

For `r>=binom(a,2)+a+1`, integer rounding gives `P<=binom(a,2)-1`. Since `sum_j(s_j-r)=1`,

`r-binomial(a,2)+2 <= s_j <= r+binomial(a,2)-1`.

For `a=6`, every target ideal group has size `r-13` through `r+14` for all `r>=22`. This replaces the earlier `r+O(sqrt r)` energy estimate with an absolute-width theorem.

### NEW THEOREM B — Product-cover / cylinder inequality

Let `C_0` be the graph of target-color edges crossing distinct target ideal groups, so `e(C_0)=M_0`, and let `L=min_j s_j`. For every internal edge `uv` of `F_0` in one group,

`d_{C_0}(u)+d_{C_0}(v) >= L-M_0/L`.

Proof: every transversal choosing one vertex from each other target group, together with `u,v`, would be a `K_{a+1}` in `F_0` unless it contains a cross pair absent from `F_0`, i.e. a target-color cross edge. Each such edge incident to `u` or `v` covers at most `1/L` of the transversal space; all other cross edges together cover at most `M_0/L^2`. The union bound yields the inequality.

### NEW THEOREM C — Improved bounded hub cover

Let `H_r=L-M_0/L` and `X={v:d_{C_0}(v)>=H_r/2}`. If `H_r>0`, every internal target-complement edge meets `X`, and

`|X|<=4M_0/H_r`.

For `a=6`, `L>=r-13`, `M_0<=2x_0<=28r+12`. For `r>=1000`,

`H_r>=r-42`,
`|X|<=4(28r+12)/(r-42)<117`.

Therefore **at most 116 hubs suffice for all `r>=1000`**; outside them, every target ideal group is an actual target-color clique.

### Interpretation / limitation

The target-side structure is now much more rigid: absolute-width groups and a constant-size hub kernel are proved. This still does not show that the `O(r)` non-target block defects propagate through the same kernel, nor does it rule out directed cycles of hub protection. `NO-HIGH-STOP` remains `OPEN`.

### GitHub commits

- strengthened hub theorem: `4e4c0511944a9e4cf8c615e8e289696349dfc2c9`
- canonical state: `2b7d1fb36538ce32c276c083445d114bdb8aef01`
- open gaps: `6a576e565b977a478fc67e1b89acd5580c894c9e`
---

## 2026-10-24 — Round 10: all-color Brouwer floors, exact-alpha audit, and scalar countermodel

### NEW THEOREM A — Simultaneous Brouwer excess floors

At an exact high stop, let `F_i=bar(G_i)` and let `x_i=t_{k_i}(n)-e(F_i)`, with `k_0=a`, `k_i=r` for `i>0`, and `n=ar+1`.

- Target color: `F_0` is `K_{a+1}`-free and not `a`-partite because `alpha(F_0)=omega(G_0)<=r-1`, so `n>a(r-1)`. Brouwer gives `x_0>=r-1`. Kang–Pikhurko's equality classification rules out equality, since every equality graph has an independent set of size at least `floor(n/a)=r`. Thus `x_0>=r`.

- Non-target color: `F_i` is `K_{r+1}`-free and `alpha(F_i)=omega(G_i)<=a`, since a color-`i` clique is target-independent. It cannot be `r`-partite because that would imply `n<=ar`. Brouwer gives `x_i>=floor(n/r)-1=a-1`.

Using `sum_i x_i=S_a(r)=(binom(a,2)-1)r+a`,

`x_0<=(binom(a,2)-a)r+2a-1`,
`sum_{i>0}(x_i-(a-1))<=(binom(a,2)-a-1)r+2a-1`.

For `a=6`: `x_0<=9r+11` and `sum_{i>0}(x_i-5)<=8r+11`.

### NEW CONSEQUENCE — sharpened target groups and hubs

Since `D<=x_0` and `(r-1)P<=D` for `P=sum_j(|V_j|-r)_+`, the target ideal groups satisfy `r-8<=|V_j|<=r+9` for `a=6,r>=22`. Also `M_0<=2x_0<=18r+22`.

With `L>=r-8`, the product-cover theorem gives `H_r=L-M_0/L>=r-27` for `r>=1000`; hence

`|X|<=4(18r+22)/(r-27)<75`.

Therefore **`|X|<=74` for `a=6,r>=1000`**, improving the previous 116-hub bound.

### NEW AUDIT — exact target independence number

For fixed `a>=6`, if `r>=a^2`, the excess ledger forces `alpha(G_0)=a`: if `alpha(G_0)<=a-1`, then `e(G_0)>=p_{a-1}(n)`, but

`p_{a-1}(n)-p_a(n)>=n^2/(2a(a-1))-a/8>S_a(r)`.

For `a=6`, the same inequality works for `r>=24`. This threshold is not uniform for `a` growing with `r`; that regime remains separately open.

### Adversarial audit — scalar constraints still permit a formal high-stop budget

For `a=6`, the assignment

`x_0=9r+11`, `x_i=5`, `z_i=1`, `q_0=5r+2`,
`(|V_j|)=(r+1,r,r,r,r,r)`, `Delta=0`, `D=7`, `M_0=9r+18`, `|X|=7`

passes the exact excess ledger, predecessor increments, target partition identity, stability budgets, group-size bounds, hub cardinality, and global cross-pair count. Place all `r-1` duplicated vertices in the `r+1` group so that the label classes can be transversals at the group-count level.

This is an **abstract parameter countermodel, not a graph counterexample**: it does not verify the full color-graph incidence, every `K_{r+1}`-free condition, or the equality-case structure of all `F_i`. It demonstrates that scalar-ledger rearrangements alone cannot close `NO-HIGH-STOP`.

### Status

- Brouwer floors: `PROVED_ANALYTIC` (conditional on the established high-stop contract and cited non-partite Turán/equality theorems).
- Improved `a=6` group range and hub bound: `PROVED_ANALYTIC`.
- Exact-alpha forcing: `PROVED_ANALYTIC` for fixed `a,r>=a^2`; for `a=6,r>=24`.
- Abstract ledger feasibility model: `ABSTRACT_PARAMETER_COUNTERMODEL`, not a real graph counterexample.
- `NO-HIGH-STOP`: **`OPEN`**.

### Next highest-priority task

Classify the equality / small-defect Brouwer templates for non-target colors and align their two-star defect pattern with the exact predecessor classes `S_{i,b}`. Prove a joint incidence-packing inequality linking those templates to `D`, `M_0`, and the bounded hub kernel. Do not spend another round on scalar-only inequalities or the already-closed core minimum-degree theorem.

### GitHub commits

- Brouwer floors + scalar audit: `e1628f77a9818ab85bf2de09169f8977156f69fb`
- canonical state: `ffd70661b2487739cb92d6983d61cc71cb17371d`
- open gaps: `424a0acab12d6e4366c4d6e2bbbf1b7f225fa3dc`
### Round 10 follow-up — sharpened partial `TD(6,r)` block count

The explicit partial-design bound no longer needs a simultaneous `x_i` good-color cutoff: the exact predecessor identity alone gives `sum_i z_i<=6r+1<=7r`. Fewer than `sqrt(r)/2` colors can have `z_i>14sqrt(r)`, so at least `r-1-sqrt(r)/2` colors are good. Each contributes at least `r-14sqrt(r)+1-|X|` full classes avoiding hubs.

With the new `|X|<=74` bound, each good color contributes at least `r-14sqrt(r)-73` clean transversal blocks, and

`(r-1-sqrt(r)/2)(r-14sqrt(r)-73) >= r^2-(29/2)r^(3/2)-67r`.

Thus the explicit `a=6` high-stop geometry contains at least `r^2-14.5r^(3/2)-67r` pairwise-linear partial resolvable transversal blocks for `r>=1000`. This is a sharper necessary structure, not an exact TD or a contradiction.

### GitHub commits for follow-up

- theorem / improved TD bound: `57201f7dd23dca8a64ebfbbbace7ff38ca7317b4`
- canonical state: `0fed2bcec9b9ae695903642cc783e741cbef6f3d`
- open gaps: `c749557ab3e781663b814b3486a9e36028f05f2b`
---

## 2026-10-24 — Round 11: exact predecessor-label defect identity

### NEW THEOREM A — Exact edge-defect identity

For each non-target color `i`, let `S_{i,b}` be the unique-label class at predecessor vertex `b`, let `Z_i` be the `z_i` duplicated-color vertices, let `h_b=a-|S_{i,b}|`, and set `Q_i=sum_b binom(h_b,2)`. If

- `M_i` counts color-`i` edges between distinct `S_{i,b}` classes;
- `H_i` counts color-`i` edges from `Z_i` to the classes;
- `K_i` counts color-`i` edges inside `Z_i`;

then

`M_i+H_i+K_i=x_i+(a-1)z_i+1-Q_i`.

Proof: count the complement `F_i=bar(G_i)` edges by the three pair types, expand `sum_{b<c}s_bs_c` using `sum h_b=z_i-1`, and use `t_r(ar+1)=t_r(ar)+(r-1)a`. The concentration correction `Q_i` is necessary.

### NEW THEOREM B — Duplicate-label pair obstruction

For a duplicate vertex `v` with color-`i` labels `b,c`, define `A_b=N_{F_i}(v)∩S_{i,b}` and `A_c=N_{F_i}(v)∩S_{i,c}`. Every pair in `A_b×A_c` must have color `i`, because otherwise `(B\{b,c})∪{v,u,w}` would be an `(r+1)`-set omitting color `i`. Since `A_b∪A_c` is independent in `F_i` and `alpha(F_i)<=a`,

`|A_b|+|A_c|<=a`.

Summing edges incident to each duplicate gives

`H_i>=a z_i-sum_b h_b deg_{L_i}(b)>=z_i(a-z_i+1)`

when positive, where `L_i` is the multigraph of duplicated label pairs. Combining with the exact identity yields

`M_i+K_i<=x_i+(z_i-1)^2-Q_i`.

For `z_i=1`, `K_i=0` and `M_i>=|A_b||A_c|`; therefore

`x_i>=a-1+(|A_b|-1)(|A_c|-1)`.

Thus a non-target color at the Brouwer floor `x_i=a-1` must have one of the two duplicate-label classes with exactly one `F_i`-neighbor of the duplicate vertex.

### Sharpness and adversarial audit

The Kang–Pikhurko extremal construction gives a genuine per-color graph/interface profile with `a=6,x_i=5,z_i=6,Q_i=10`, `M_i=5,H_i=6,K_i=15`; the identity gives `26=5+5·6+1-10`. This is not a full `r`-coloring or a global counterexample. It proves that assuming `z_i=1` is invalid and that the new local inequalities are sharp on the known extremal template.

### Status

- Exact defect identity: `PROVED_SYMBOLIC`.
- Duplicate-label pair obstruction: `PROVED_SYMBOLIC`.
- One-duplicate strengthened excess inequality: `PROVED_SYMBOLIC`.
- `NO-HIGH-STOP`: **`OPEN`**. The new results constrain each color's local extremal pattern but do not yet prevent compatible reuse of hubs/labels across different colors.

### GitHub commits

- theorem file: `43cecbcb44a36d0f001273e3ddd29826dd6c2214`
- canonical state: `b02c3910576efdb0e369d9b07dc719ab5774222e`
- open gaps: `8435a6d6d56956d02f0476c933ff5e0907ad36c0`

### Next highest-priority task

Classify the cross-color reuse obstruction: use the fact that each color with a near-extremal KP template forces a duplicated-label pair and a complete bipartite color-`i` patch, while any vertex pair can belong to only one color. Determine whether the resulting family of label-pair patches can fit inside the `a=6` target-group/hub incidence budget, and build an explicit abstract incidence family if scalar constraints still allow it.
---

## 2026-10-24 — Round 12: linear-defect alignment theorem

### NEW THEOREM A — Stability-part alignment

For each non-target color `i`, let `P_{i,j}` be the Füredi stability partition of `F_i=bar(G_i)` with internal edges `I_i^*<=x_i` and missing cross-pairs `M_i^*<=2x_i`. The exact predecessor label classes `S_{i,b}` are disjoint independent sets in `F_i` of sizes at most `a`.

- A full class `|S_{i,b}|=a` split across stability parts creates at least `a-1` missing cross-pairs. Therefore at most `2x_i/(a-1)` full classes are split.
- If a stability part contains exactly one full label class plus extra vertices, each extra vertex needs an internal `F_i` edge to that class (otherwise `alpha(F_i)>a`); such classes charge at most `I_i^*`.
- If a part contains `k>=2` full classes, each pair of classes has at least `a` internal `F_i` edges between them: the bipartite cross graph on `2a` vertices has independence number at most `a`, so its vertex-cover number and edge count are at least `a`. Since `k<=2 binom(k,2)`, all full classes in multi-class parts number at most `2I_i^*/a`.

Thus at most `2x_i/(a-1)+2x_i` full label classes fail to equal a stability part.

### NEW THEOREM B — Linear-defect partial resolvable `TD(a,r)`

A predecessor class is clean if it is full, equals a stability part, and avoids the target hub set `X`. Such a class is a transversal of the `a` target groups, since every group outside `X` is a target-color clique.

Across all non-target colors, the number of non-clean classes is at most

`sum_i(z_i-1) + (2/(a-1)+2)sum_i x_i + (r-1)|X|`.

Use `sum_i(z_i-1)<=(a-1)r+2`, `sum_{i>0}x_i<=S_a(r)-x_0<=(binom(a,2)-2)r+a` from `x_0>=r`, and `|X|=O_a(1)`. Therefore only `O_a(r)` of the `r(r-1)` classes fail to be clean, and every fixed-a high stop forces a partial resolvable `TD(a,r)` with `r^2-O_a(r)` blocks.

For `a=6,r>=1000`, the bound `|X|<=74` gives

`non-clean <= (5r+2)+(12/5)(13r+6)+74(r-1) <=111r`,

so at least **`r^2-112r`** clean transversal blocks exist.

### Independent audit and limitations

- Split classes are charged to disjoint missing cross-pairs; contained classes are charged to internal edges; the two-full-class case uses `alpha(F_i)<=a` and the elementary identity `alpha+tau=2a` for the induced bipartite cross graph.
- A clean class has size `a`, avoids all hubs, and is independent in `F_i`; each target group outside the hub set is a target clique, so it meets every group at most once and therefore exactly once.
- Blocks of one color are disjoint; blocks of different colors share at most one vertex. This proves pairwise linearity and partial resolvability.
- This is not a completion theorem. `O(r)` exceptional classes remain, and `NO-HIGH-STOP` remains `OPEN`.

### GitHub commits

- theorem file: `9c2a3e2d507853e1310706348fa466eaffe44c47`
- canonical state: `76d50bd75f9c2a993c3b3343e800852d2acffa8d`
- open gaps: `f3827e8c9b75e30de4fa10e6277cb934b64bd716`

### Next highest-priority task

Analyze the `O(r)` exceptional classes. Determine whether the duplicate-label patches forced by the exact `r+1`-set property can be packed into a pairwise-linear design with the target-group hub incidences, or whether they force an earlier valid `R_5`. The first objective is an exact obstruction theorem for the exceptional-block incidence graph, not another asymptotic estimate.
### Round 12 follow-up — design-only countermodel audit

For every prime power `r>=7`, a field-based `TD(r+1,r)` restricts to `TD(6,r)`. Deleting one parallel class leaves `r^2-r` blocks in `r-1` parallel classes. Adding one unused point to one group gives group sizes `(r+1,r,r,r,r,r)` without changing the blocks. For `r>=112`, this meets the lower bound `r^2-112r`.

This is only an abstract design model, not a full edge-coloring or a canonical high-stop graph. It establishes that even a pairwise-linear near-complete TD with `r-1` parallel classes is not contradictory by density alone. The next theorem must use the exceptional blocks' actual colors/labels and the target hub incidence.

### Latest GitHub commits

- theorem file (alignment theorem + design-only audit): `32ba6cef7c246f3dd82db2b002a8a8575c103c8d`
- canonical state: `8bd13d7fd50b3441d65d3ac755a724d0596a0156`
- open gaps: `92eb7de76041b80fd9e37865a0073c5a96f6a096`
- progress log: this update

### Current status

`NO-HIGH-STOP = OPEN`. The best new necessary structure is a partial resolvable `TD(6,r)`-type system with at least `r^2-112r` clean blocks for `r>=1000`, plus at most 74 target hubs. The explicit design-only model rules out using this density as a contradiction. The next task is to classify and jointly charge the `O(r)` exceptional label classes.
---

## 2026-10-24 — Round 13: missing-slot budget and a 7–28 hub kernel

### NEW THEOREM A — Global missing-group-slot budget

For every predecessor label class `S_{i,b}`, let `g_{i,b}` be the number of target groups it meets. With `h_{i,b}=6-|S_{i,b}|` and `c_{i,b}=|S_{i,b}|-g_{i,b}`, its missing-group slots satisfy

`m_{i,b}=6-g_{i,b}=h_{i,b}+c_{i,b}`.

The exact hole identity gives `sum h=5r+2-q0<=5r+2`. Every repeated-group excess `c` is charged to internal `F0` edges: for group multiplicities `t_j`, `c=sum(t_j-1)<=sum binom(t_j,2)`. Such pairs are distinct across all color classes, so `sum c<=D<=x0<=9r+11`. Therefore

`W=sum m_{i,b}<=14r+13`.

### NEW THEOREM B — Each hub consumes at least `(r-65)/2` missing slots

For a hub `x` in group `V_j`, let `W_x` sum the missing slots of all label classes containing `x`. At most one non-target color is duplicated at `x`; write `u_x∈{0,1}` for this event. For each other group `V_k`, every class containing `x` that meets `V_k` gives a distinct non-target neighbor of `x` in that group; different colors cannot give the same neighbor because a pair has only one color. If `m_{x,k}` classes containing `x` omit `V_k`,

`d_C0(x,V_k)<=s_k-r+1+u_x+m_{x,k}`.

Summing over the five other groups yields

`d_C0(x)<=r+6-s_j+5u_x+W_x<=19+W_x`,

using `s_j>=r-8`. The existing hub threshold is `d_C0(x)>=(r-27)/2`, hence

`W_x>=(r-65)/2`.

### NEW THEOREM C — Finite hub kernel

The total hub-slot incidence satisfies

`sum_{x∈X}W_x<=W+15|X|(|X|-1)`.

Indeed, a class with `k>=2` hubs contributes at most `(k-1)m<=30` surcharge beyond its one contribution to `W`; each such class contains a hub pair, and no hub pair can occur in two different color classes. Thus there are at most `binom(|X|,2)` multi-hub classes.

Combining this with `W<=14r+13` gives

`|X|(r-65)/2<=14r+13+15|X|(|X|-1)`.

The old hub theorem gives `|X|<=74` for `r>=1000`. For `29<=k<=74`, `f(k)=k(r-65)/2-15k(k-1)` is increasing when `r>=26272`; moreover `f(29)>14r+13` for `r>=26272`. Hence `|X|<=28` in that range.

For the lower bound, put `delta_j=s_j-r`, so `sum delta_j=1`. Since the target graph is `K_r`-free, `alpha(F0[V_j])<=r-1`; therefore the minimum vertex-cover number of `F0[V_j]` is at least `delta_j+1` for each `delta_j>=0`. Since `X∩V_j` covers all internal `F0` edges, summing over non-smaller groups gives `|X|>=7`. Thus

`7<=|X|<=28` for `a=6,r>=26272`.

### NEW CONSEQUENCE — cleaner partial design

With `|X|<=28`, the non-clean class bound becomes

`(5r+2)+(12/5)(13r+6)+28(r-1)<=65r`.

Thus any high stop in this range forces a pairwise-linear partial resolvable `TD(6,r)` with at least **`r^2-66r` blocks**.

### Independent proof audit

- The hub degree inequality uses only exact class membership and uniqueness of edge colors; it does not assume all classes are clean or full.
- The global missing-slot budget separates holes from repeated-group excess, and the latter is charged to distinct internal target-complement edges.
- The multi-hub surcharge is bounded because a fixed pair of hubs can share at most one monochromatic label class.
- The lower bound `|X|>=7` uses only the target `K_r`-free condition plus the existing statement that every internal target-complement edge meets `X`.
- The constants were checked at the endpoint `r=26272`: the inequality already excludes `|X|=29`, and monotonicity excludes all `29..74`.

### Status

- Missing-slot budget: `PROVED_ANALYTIC`.
- Hub slot-consumption inequality: `PROVED_ANALYTIC`.
- `7<=|X|<=28` for `a=6,r>=26272`: `PROVED_ANALYTIC` conditional on earlier stability/hub-cover lemmas.
- Partial-design lower bound `r^2-66r`: `PROVED_ANALYTIC` conditional on the earlier alignment theorem.
- `NO-HIGH-STOP`: **`OPEN`**. The hub kernel is finite but nonempty; the exceptional label classes are still not excluded.

### GitHub commits

- theorem file: `1946183077f52b30dc0a15fcfd63fecd1032b407`
- canonical state: `326f85832f0700fe90946b067312294817b850af`
- open gaps: `1e74eb8f448389dbb3509e47ebef8bcd03bd42ee`
- progress log: this update

### Next highest-priority task

Use the fact that each of the 7–28 hubs has a missing-slot incidence of at least `(r-65)/2`, but the global slot budget is only `14r+13` plus the finite multi-hub surcharge. Classify the equality regime in this incidence inequality and determine whether the resulting 7–28 group-local hub pattern forces a rainbow-star / resolvable terminal or contradicts the exact predecessor-label pair obstruction. Do not revert to a scalar-only argument.