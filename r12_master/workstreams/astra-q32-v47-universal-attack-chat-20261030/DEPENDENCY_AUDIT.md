# Independent dependency ledger

## Original inputs

- CORE: |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11. These are the user-specified true Q32 hypotheses and the explicit parent interface.
- T61: the actual 61-point target F has alpha(F)<=5, omega(F)<=11, delta(F)=13 and e(F)=408, with p-A target and p-H non-target. Needed for the source audit, not the core nonexistence proof.
- COLOR: twelve colors own every edge exactly once, and every non-target color has alpha<=12. Together with T61 this gives omega(C)<=5.
- EXT1: ordinary Turan's theorem and Kang-Pikhurko 2005 Theorem1 at n=25,r=2. These are the only external mathematical theorems needed for U6.
- EXT2: Kang-Pikhurko Theorems1 and4 at n=61,r=12, used only for the source audit and not for U6.

## Conclusion dependencies

| Result | Status | Inputs |
|---|---|---|
|Degree12 independent four-set|PROVED|CORE; ordinary Turan|
|Private-clique / five-point reduction|PROVED|CORE|
|Common-neighbor inequality U2|PROVED|CORE; EXT1 at25,2|
|At most one external point complete to a K10, U3|PROVED|U2; CORE clique cap and excess budget|
|Two-K11 pair spends all excess, U4|PROVED|CORE; independent5 blocker|
|Two-template theorem U1|PROVED|preceding lemmas; support counting; rotation|
|Mixed-pair capacity U5|PROVED|CORE; independent5 blocker; positive-part inequality|
|P impossibility|PROVED|U1,U3,U5; disjointness of the two clique pairs|
|D impossibility|PROVED|U1,U3; distinct support clique pairs; explicit zero-count accounting|
|Universal core nonexistence U6|PROVED|U1 and the two template contradictions|
|All-m full-support Q32 nonexistence|PROVED under the stated true parent contract|U6; every such configuration supplies CORE|
|Type-I source classification|PROVED_CONDITIONAL on T61,COLOR,EXT2|independent source audit; not used by U6|
|Common five-point four-part partition|PROVED as an intermediate necessary deduction|U1; unique color ownership; not used by U6|
|Failed search diagnostics and finite proof checks|COMPUTATION_CERTIFIED|complete edge lists and independent standard-library verifier|
|Q33, E407 and full EG617(r=12) closure|OPEN here|outside this proof and write scope|

## Sibling isolation

Read-only audits were performed at the frozen heads in source_manifest.json. A's old target-K6 exclusion is retracted. Its newer partition work is not a premise. The balancedness-only source warning is distinguished from the actual embedded T61 target-alpha5 assumption.

B's final audit head is db515bab1a203ccae131c3953ffe2a8ecef539a6, after its initial 43f22404cbcc15b13fb8a12d003e60e9fef9bde7 snapshot. Its new K4-e/Z4 closure is recorded as that branch's claim, not independently imported. C's support calculations, D's V12 calculations and the previous Astra 3+7 theorem are also unused.

No AGENTS.md was found in the checked relevant repository trees or local workspace scan. The new branch was absent initially and was created from global workstream b0459807acd4b7e386148056ddf77d7998918893. All submitted changes are confined to the new directory; no global, sibling, old Astra or default-branch update is authorized or performed here.

## Proof acceptance boundary

- True CORE assumptions and target clique cap11: pass.
- No unverified sibling theorem: pass.
- All m=8,9,10: covered through the identical core projection.
- Exceptional points and all source profiles: unrestricted; no placement-dependent proof step.
- Analytic contradiction: complete in steps1-8; P gives8>6 and D gives10>6.
- Finite verifier: executed successfully; receipt and result artifact retained.
- Root import: a self-contained theorem is supplied for independent review; integration is not performed here.

The verifier does not formally certify the prose or the external theorem. It independently checks every finite arithmetic/support ingredient and the recorded diagnostic graphs. Neither a solver proof nor exhaustive graph enumeration is claimed. The final theorem's force comes from the analytic contradiction, with exactly the dependencies above.
