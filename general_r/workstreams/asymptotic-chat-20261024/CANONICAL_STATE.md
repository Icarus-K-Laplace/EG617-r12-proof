# CANONICAL STATE — EG617 general-r asymptotic synthesis

Updated: 2026-10-24

Branch: `workstream/general-r-asymptotic-20261024`

## Headline status

**Problem 617 is NOT proved unconditionally for all sufficiently large r.**

The strongest current synthesis theorem is:

> **Theorem S68 — CONDITIONAL_ON_A_C*_D + ASYMPTOTIC_ANALYTIC.**
>
> For every `r>=68`, if the front residual/design dichotomy H_A, the remaining endpoint terminal closure H_C*, and the design-terminal nonextension H_D hold at r, then `P(r)` holds.

The Exact Three-Anchor hypothesis H_B is no longer assumed for r>=68; it is derived from the legal core contract using parity, near-anchor reduction and the sibling AES theorem.

## 1. Current strongest theorem: r>=68

`H_A + H_C* + H_D => P(r)` for every `r>=68`.

If H_B is explicitly assumed, the corresponding composition works already for every `r>=12`.

## 2. Hypotheses still required

### H_A — OPEN
All-large-r front extraction: every counterexample reaches either a legal `4r+1` residual/core contract or a controlled `5r+1` design-like terminal.

### H_C* — OPEN
Only the remaining endpoint terminal closure is needed, not necessarily a universal repivot potential. Current unresolved scalable backend content is concentrated in d2, plus d0/d1 and the finite high skeleton.

### H_D — OPEN
Robust classification/nonextension of the `5r+1` design-like terminal. Exact affine-plane nonextension is already proved; the missing step is stability/classification into that rigid class.

### H_B — PROVED_ANALYTIC for r>=68
Not an asymptotic hypothesis above 68. Still open in the sibling theorem for 12<=r<=67.

## 3. Current minimal r0

- H_B-free minimal-hypothesis synthesis record: **68**.
- With H_B assumed: **12**.
- Unconditional Problem 617 r0: **not yet finite/proved** because H_A, H_C*, H_D remain open.

Relative to the start of this workstream, the H_B-free synthesized threshold improved from no finite value to 68.

## 4. Inequality controlling r0

The current 68 is controlled only by the sibling three-anchor complement/AES threshold:

`2r-9 > 5(3r-1)/8`

iff

`r>67`.

No current backend endpoint inequality intrinsically requires r=68.

## 5. Master asymptotic ledger identity

With residual deficit

`epsilon=D_r(4r+1)-e(F)`

and core excess

`K=2e(H)-r(3r-1)`,

> **`K=6r+6-2epsilon-2q`**

or equivalently

> **`q+epsilon=3r+3-K/2`.**

K is always even.

Consequences:

- `K>=7` is exactly equivalent to `K>=8`;
- baseline `K>=2` gives `q<=3r+2-epsilon`;
- anchor `K>=8` gives `q<=3r-1-epsilon`.

## 6. Endpoint width / terminal boundedness

Under K>=8:

`d in {0,1,2,3,r-2,r-1,r}`.

So the support-degree family has O(1) endpoint width.

Current stronger terminal information:

- d3 common-S: **closed**;
- high endpoint: **at most 3 owners**, shell interaction kernel `<=9`, core incidence signatures `<=8`; hence a finite bounded-complement skeleton;
- d2: **still scalable**; one-loss three-class states obey `K+a+b>=r`;
- d0/d1: not yet frozen.

Therefore the entire backend is **not yet proved to have O(1) exact combinatorial type count**, because d2 multiplicities/charge parameters and d0/d1 remain scalable. The high endpoint itself is O(1)-skeletonized.

## 7. Certified small-r-only pathologies

1. d2 concentrated state `K=8,a=3,b=1`: requires `r<=12`.
2. d4 / d=(r-3) medium-support family: impossible for r>=15 from baseline K>=2; impossible for every r>=12 under K>=8.
3. four high owners: coarse slope contradiction for r>=13; r=12 equality separately closed.
4. balanced `(r+1,r+1,r+1)` near-anchor coarse-cover exception: only r=12.
5. d3 allowance-five/top-q frontier: stronger than small-r-only — completely closed under A+B for all r>=12.

## 8. Sibling result most sensitive for r0

Numerically: **three-anchor threshold 68** is the only current source of the value 68.

For unconditional existence of any all-large-r theorem, however, the more serious blocker is **H_A front extraction**, followed by H_C* and H_D.

Thus:

- improve B => lower r0;
- prove A/C*/D at any finite thresholds => convert the conditional synthesis into a genuine infinite-family theorem.

## 9. New multicolour / decoration synthesis

The architecture-side shell dichotomy gives a slope-half bound on low regular shell vertices. Combining it with the stronger sibling bound of at most three high regular owners yields

> **`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`**

for the number tau of decorated shell vertices in the fixed-deficit near-extremal branch.

Hence for fixed epsilon,

> **`tau >= r/2-O_epsilon(1)`.**

Together with exact transport

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`,

this says any fixed-deficit non-improving terminal must organize a linear number of decorations into a rigid incidence system. This is currently the best candidate for bypassing a full global repivot-potential theorem.

## 10. Next highest-leverage inequalities

Two targets, in order:

### Backend d2 target

From the exact d2 one-loss three-class barrier

`K+a+b>=r`,

prove any upper bound

> **`K+a <= (1-c)r+O(1)`**

for some fixed c>0 in every terminal branch. This would kill the scalable three-class d2 family for all sufficiently large r.

Alternative: force common-S owner demand

`N>(1/2+c)r-O(1)`

and contradict the multicolour slope-half capacity.

### Potential/design target

Use

`tau>=r/2-O_epsilon(1)`

to show a legal repivot strictly increases tau unless the decoration incidence matrix has an O(1)-parameter design form. Such a theorem could merge H_C* and part of H_D into one asymptotic rigidity statement.

## Imported sibling heads used in this state

- architecture base: `3dc54c38e13a71e8a12330c3c36b1aa1063aacaa`;
- three-anchor: `0c226d78e39e3da2a594f8a6121a864d2efa09ea`;
- repivot termination: `2974fd80882a4545a3a1a569418405ec4e3bdebc`;
- near-extremal shell dichotomy: `578830ff3fd9eab94f2bb5a498d90a1a303ba2e1`.

## Files in this workstream

- `CANONICAL_STATE.md`
- `ASSUMPTION_LEDGER.md`
- `ASYMPTOTIC_INEQUALITIES.md`
- `R0_TRACKER.md`
- `SUFFICIENTLY_LARGE_R_THEOREM.md`
- `DEPENDENCY_DAG.md`
- `PROGRESS_LOG.md`
- `SMALL_R_ARTIFACTS.md`
- `HYPOTHESIS_SENSITIVITY.md`
