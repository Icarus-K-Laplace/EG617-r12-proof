# Global Support-Compatibility V2 Synthesis

Status: `PROVED_ANALYTIC` as a structural synthesis under the stated pivot/support hypotheses. This file does **not** claim the global EG617 theorem or the full high-backend bridge is closed.

Purpose: collect the now-proved global machinery into one theorem architecture and identify the smallest remaining structural bridge. The high backend should no longer be organized as eight independent edge layers.

## 1. Master variables

For a maximal pivot p with shell A and residual core H, regular owner rows carry:

- shell missing sets `S_y`;
- core supports `D_y` with `|D_y|=|S_y|=d_y`;
- core excess `kappa_v`;
- internal support defect `mu(D_y)`;
- shell/core correction `e_F(S_y,D_y)`;
- q-loss `ell_y=q-q_y`;
- global decoration labels g and lexicographic secondary potential tau.

The exact multi-S exchange identity is

`ell_y=a_y-kappa(D_y)-mu(D_y)-e_F(S_y,D_y)`.                (V1)

Summing gives the exact multi-pivot compatibility law

`sum_y ell_y=sum_y a_y-Phi_multi`,                           (V2)

with

`Phi_multi=sum_v lambda_v kappa_v`
`          +sum_y mu(D_y)`
`          +sum_y e_F(S_y,D_y)`.                            (V3)

Support incidence forces decoration:

`g_v>=kappa_v+lambda_v-1`.                                  (V4)

Repeated supports therefore create either strict repivot loss or fully-decorated missing-set escape.

These are the global conservation laws behind all regimes below.

## 2. Regime I — low-support / bounded-transversal regime

### 2.1 Common-S block-transversal theorem

For pairwise-disjoint d-supports with at most c target cross edges per block pair and `alpha(H)<=3`, the block-transversal inequality is

`C(N,2)-floor(N^2/3) <= (c/d^2) C(N,2)`.                   (V5)

Sharp certified values include

- `T(2,1)=6`;
- `T(3,1)=3`;
- `T(3,2)=6`.

A maximal support matching therefore yields bounded hitting sets of sizes

- 12 for d2/c1;
- 9 for d3/c1;
- 18 for d3/c2.

Thus failure to extract a forbidden disjoint matching automatically creates bounded-transversal incidence concentration.

### 2.2 q32 multi-S d3 extraction

For simultaneous regular d3 rows at a maximal pivot with `q<=32`, any two rows y,z satisfy

`|S_y intersect S_z|+|D_y intersect D_z|>=3`.               (V6)

Hence

`D_y intersect D_z=empty => S_y=S_z`.                       (V7)

Therefore every pairwise-disjoint support matching automatically becomes a common-S subsystem. Block transversals then give

`nu<=6`,                                                     (V8)

and every such multi-S support system has an at-most18-point core transversal.

Repeated d3 supports obey the multi-S dichotomy:

- if some owner missing triple is not fully decorated, the support satisfies
  `kappa(D)+mu(D)<=1`;
- otherwise every owner missing triple is fully decorated.

Thus the q32 multi-S problem has already reduced to

> bounded-transversal high-codegree geometry versus fully-decorated missing triples.   (V9)

### 2.3 Common-S total-charge localization

For a common-S family with owner set Y and leftover shell block T,

`W=sum_H(kappa_v+e_F(v,S))`

satisfies

`W<=K+q+e_M(S)-e_M(T)`                                      (V10)

and hence

`W<=K+q+C(d,2)`.                                             (V11)

In the source-reported q32/CORE211 channel (`K=2`):

- d3: `W<=37`;
- d2: `W<=35`.

This turns many equality geometries into immediate scalar contradictions.

## 3. Regime II — support systems classified by allowance

The correct structural split is by row allowance relative to support size, not by edge layer.

### 3.1 Subcritical allowance: `a<=d-1`

If `s=|S intersect X|<d`, then:

1. plateau rows are singleton support classes and at most3 exist;
2. every strict-loss support is disjoint from every distinct support class;
3. distinct strict supports carry at most `a-1` target cross edges;
4. block-transversal capacity bounds the number of distinct strict support classes;
5. all excess owner count is forced onto repeated isolated supports.

For r=12 d3 with a<=2:

- plateau owners <=3;
- distinct strict support classes <=3;
- total distinct support classes <=6.

Thus q32/d3 common-S is an isolated-block packing problem, not a general overlap problem.

### 3.2 First high slack: `a=d`

If `s<d`, the support system decomposes into:

1. at most3 singleton plateau rows;
2. an exact one-loss subsystem with support defect `d-1`;
3. higher-loss support classes disjoint from every distinct class.

Every proper overlap in the one-loss subsystem is an equality event with zero-charge intersection.

The zero-charge incidence-signature theorem then decomposes the interacting one-loss layer into canonical sunflowers.

For d2:

- one zero-charge hub;
- target-K2 supports;
- charge1 private leaves;
- at most3 distinct support classes.

For d3:

- Type H: common zero hub + target-K3 supports + two unit-charge petals;
- Type P: common zero target-edge pair + two-edge/K3 supports + one charge1/2 petal;
- at most3 distinct support classes per pattern;
- full four-set geometry is impossible.

### 3.3 First-high-slack owner capacities

Hereditary sunflower packing gives whole-pattern owner bounds without multiplicity-partition enumeration:

- d2 common-hub one-loss pattern: `N<=9`;
- d3 Type P: `N<=8`;
- d3 Type H: `N<=9` in general, and `N<=8` whenever total charge `W<=61`.

Since low-excess q32 channels have `W<=37`, the effective d3 one-loss capacity there is uniformly

`N<=8`.                                                      (V12)

Three-class charge barriers further give, in the 35-core:

- d2 common-hub: `W>=34`;
- d3 Type P: `W>=33`;
- d3 Type H: `W>=62`.

Thus equality windows are scalar and narrow rather than combinatorially arbitrary.

## 4. Repeated-support bridge independent of common S

If one nonempty d-point core support D is used by m regular owners, the owners form a target clique even if their missing sets differ.

For

`W_D={p} union Y_D union D`,

the exact number of missing target edges is

`d+mu(D)`.                                                   (V13)

Therefore every hereditary cap implies

`d+mu(D)>=Delta(m+d+1)`,                                    (V14)

where `Delta(t)=C(t,2)-Dcap(t)`.

For r=12 this gives unconditional multiplicity bounds

- d2: m<=9;
- d3: m<=8;
- d4: m<=7.

When repetition also occurs in a common-S family with `s<d`, exact tau transport forces at least one unit of q-loss and hence an internal-density lower bound. The repeated-support hereditary packing theorem then converts repivot dynamics directly into a multiplicity cap.

Thus repetition is no longer a local-case phenomenon: it has a universal dense-block obstruction.

## 5. Regime III — large-support decorated escape

For q36--q38 and support sizes d=4 or9,

`d(13-d)=36`,

so the common row allowance satisfies

`a<=2<d-1`.                                                  (V15)

Hence these are automatically subcritical.

If `s<d`, the subcritical theorem gives:

- at most3 plateau classes;
- at most3 distinct strict low-cross support classes.

The only escape is

`S subseteq X`, i.e. `s=d`: the entire missing set is globally decorated.   (V16)

Common-S owner count is then bounded by

`N<=13-d`.                                                   (V17)

At maximal owner count:

- d=4, N=9;
- d=9, N=4;

the shell missing geometry is the same K4,9 equality state (up to side exchange) when there are no extra internal missing edges on S.

The already-proved q36--q38 K4,9 closure is therefore an equality-case exclusion of the global decorated-escape theorem, not an isolated case proof.

The only unresolved large-support bridge is the **non-maximal fully-decorated escape** (`s=d`, `N<13-d`).

The d10/q<=33 family obeys the same dichotomy and has owner count at most3 in the fully-decorated escape.

## 6. Regime IV — shell-poor one-spoke compatibility

The q36 shell-poor branch contains at least five one-spoke core pivots v_i.

Each has a 22-point anti-neighbourhood Z_i in the 35-core satisfying

`g(Z_i)>=11`,                                                (V18)

while the total core-decoration budget is

`G_H<=28`.                                                   (V19)

Therefore, if k one-spoke pivots are present,

`sum_u g_u m_u>=11k`,                                       (V20)

where m_u is the number of anti-neighbourhoods containing u.

Consequences:

- `max m_u>=ceil(11k/28)`;
- for k=5 at least7 decoration units occur in at least two anti-neighbourhoods;
- for k=5 total pairwise shared decoration mass is at least27;
- for k>=6 some decorated core vertex belongs to at least3 anti-neighbourhoods.

For a core-nonedge pair of one-spoke pivots, their two shell labels hit every triangle of the shell missing graph.

Thus shell-poor is now one weighted high-codegree / triangle-cover system, not five independent near-Mantel problems.

## 7. Global structural theorem

Combining Sections1--6 gives the present strongest form of the requested theorem.

> **Global Support-Compatibility Structural Theorem (V2).**
> Under the retained r=12 pivot contracts, every support system for which the exact row/pivot hypotheses above are available is forced into one of the following structural mechanisms:
>
> 1. **improving-repivot / charge overload:** the exact multi-pivot compatibility inequality is violated;
> 2. **subcritical isolated-block regime:** bounded plateau plus pairwise-disjoint low-cross strict supports;
> 3. **first-high-slack sunflower regime:** bounded plateau, isolated deep-loss blocks, and finitely many zero-charge sunflower patterns with global owner-capacity bounds;
> 4. **fully-decorated escape:** the missing set itself consumes the decoration budget, with K4,9 as the maximal-owner d4/d9 equality state;
> 5. **shell-poor weighted-incidence regime:** a bounded total correction budget is forced to have high codegree across many one-spoke anti-neighbourhoods.
>
> Repeated supports in every regime are controlled by one dense-block hereditary theorem.   (V21)

This is a structural theorem, not yet a proof that all five alternatives are impossible.

## 8. What is now genuinely OPEN

The former list `E333,...,E340` has been reduced conceptually to three bridge problems.

### Bridge A — bounded-transversal / high-codegree low-support rigidity

For multi-S d3 q32 systems whose supports are mostly distinct and hit an at-most18-point transversal, prove that the pair-intersection law forces one of:

- a repeated near-K3 support;
- a common hub/pair sunflower;
- a fully-decorated missing triple;
- a forbidden hereditary packing.

### Bridge B — non-maximal fully-decorated large-support escape

For d4/d9 (and analogously d10), classify `s=d` states with owner count below `13-d` and prove that they either repivot upward or extend to the already-killed maximal equality geometry.

### Bridge C — shell-poor weighted high-codegree compatibility

Classify the extremal weighted incidence design forced by (V18)--(V20), coupled with K4-free complement-core geometry and the two-label shell-triangle-cover condition.

These are the smallest current structural regimes. Falling back to E-layer-by-E-layer closure before these three bridges are tested would lose the main mathematical compression already achieved.

## 9. Relation to existing E-layers

- E333 is already a completed application of Regime I/II plus equality-rigidity.
- Source-reported E334 q32/core211 residuals lie in low-support Regime I/II once their exact view-to-owner mapping is supplied.
- E335--E337 should inherit the same structure with larger charge windows rather than new shell cases.
- E338--E340 q36--q38 large-support work is now organized by Regime III; K4,9 is its maximal equality state.
- q36 shell-poor coverage is Regime IV.

Therefore the high backend is no longer naturally an eight-case theorem.

## 10. Front-end interface

The multi-S identity (V2), repetition-induced decoration (V4), and lexicographic transport are abstract multi-pivot compatibility mechanisms.

A front-end Q32/Q33 analogue would require translating the labelled 47-core correction variables into the same gain/loss language. This translation is still OPEN.

If achieved, the paper can state one higher-level principle covering both front and back:

> locally admissible pivots cannot all be globally compatible once correction/support incidence exceeds the extremal budget.

## 11. Higher-r prospects

The following parts are parameterized and transfer directly once an analogous pivot reduction exists:

- exact multi-S gain/loss accounting;
- repetition-induced decoration;
- block-transversal extraction;
- matching-cover reduction;
- subcritical allowance decomposition;
- first-high-slack loss-layer decomposition;
- zero-charge incidence-signature compression;
- hereditary support/sunflower packing;
- repeated-support dense-block obstruction;
- weighted neighbourhood-incidence concentration.

The r=12-specific inputs are now concentrated in:

- core independence/clique bounds;
- hereditary cap values;
- the all-pivot minimum-degree contract;
- equality-state exclusions such as K4,9.

Thus r=12 is already functioning as the first substantial application of a broader extremal repivot-compatibility framework.