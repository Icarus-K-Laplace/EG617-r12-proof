# Canonical state — 2026-10-21

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For a legitimate residual `F in R(4,49)`, current clean machinery uses a degree-13 pivot `p` with shell `A` of size 13 and 35-core `H`:

`e(F) = 91 + q + e(H)`.

The clean core floor is

`H in R(3,35) => e(H) >= 211`.

Current backend lower frontier is `E332`:

- `E329`, `E330`, `E331` have analytic closures in the reconstructed DAG, with the uniform `q=27` theorem as a dependency.
- Any genuine `E332` survivor must admit a pivot with `(q,e(H))=(30,211)`.
- For `e(H)=211`, the core degree multiset is one of
  - `14,12^34`,
  - `13^2,12^33`.

Thus the active lowest backend object is:

`E332 : q30 shell + almost-12-regular 211-edge 35-core`.

Higher layers `E333...E340` remain open as a unified high-layer problem.

## Front-end

The correct modern objective is **not** to prove an exact `e(F)=325` residual. The needed bridge is:

`hypothetical K_145 counterexample -> legitimate F in R(4,49)`.

Important current assets:

- seven genuine `K_12` blocks naturally lead to a 61-point residual / O61 route;
- eight genuine `K_12` blocks leave a 49-point residual;
- under the eight-block hypothesis the high-cross branch can be eliminated analytically, yielding `alpha(Y)<=4` for the 49-point residual;
- S31 strict descent is proved under its explicit 61-point / 406-edge parent contract;
- S27 is closed under its certified contract;
- S30 remains the active front-end bottleneck.

## S30 audit correction

Historical statements that the full `(5,7,8,8)` profile is closed are too strong.

What is actually proved analytically is the specified row-labelled branch under explicit singleton-adjacency assumptions. These hypotheses must remain visible in the final proof DAG.

## Estimated completion

- structural understanding: ~80–85%
- complete auditable theorem: ~60–65% (central estimate ~63%)

The estimate is heuristic and is not a proof-status metric.
